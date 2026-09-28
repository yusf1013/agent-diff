"""Source 3: a scan of each trial's API calls for the replica gaps the replica notes document (plan.md).

    python grounding/runs/attribution_01/scan_traces.py

The gaps are those of `autogen_02/inputs/<domain>/replica.md`: ignored filters, failing queries, and writes the
replica rejects. It reads only the trial's own records (trajectory, seed, diff, termination), never a label or a
verdict. Two rule sets are scored:

- **naive:** any ignored-filter call that returned an item the agent then changed (the run's diff names it), any
  documented failing query, any rejected write, or a termination other than `done`.
- **counterfactual:** the gap must have decided the outcome.
  - An ignored-filter call returned an item the agent then changed, and the real service, honouring the filter,
    would not have returned it (judged from the seed): the mock.
  - A documented failing query errored, and the agent then changed nothing ("a solver that concludes 'none' after
    such an error has not established anything"): the mock.
  - The replica rejected a write whose value the request itself asks for, or a label id the seed defines: the test.
  - The trial did not end on its own: the harness.

Writes source3_traces.json. No model calls.
"""
from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import unquote_plus

HERE = Path(__file__).resolve().parent
RUNS = HERE.parent
ROOTS = [RUNS / "autogen_02/runs", RUNS / "fact_coverage_02/runs"]
NOT_AGENT = ("test-wording", "test-construction", "mock", "harness")
ACTORS = {"U01AGENBOT9", "u-actor", "30000000001", "jordan.lee@northwind.example", "T1"}
OWN_KEY = {"channels": "channel_id", "messages": "message_id"}  # a changed row's own id; "id" otherwise
REF_KEYS = {"channel_id", "message_id", "parent_id", "thread_ts", "issueId", "issue_id", "file_id", "item_id",
            "event_id", "documentId", "document_id"}  # what an inserted row attaches to
STOP = {"the", "and", "for", "with", "from", "that", "this"}
NAME_KEYS = ("identifier", "name", "title", "summary", "channel_name")


def param(a: str, name: str) -> str | None:
    m = re.search(r"(?<![\w])" + name + r"=([^&\"'\s]+(?:\s[^&\"'\s=]+)*)", a)
    return unquote_plus(m.group(1)) if m else None


def gql_eq(a: str, field: str, inner: str = "id") -> str | None:
    q = a.replace('\\"', '"')
    m = re.search(field + r"\s*:\s*\{\s*(?:some\s*:\s*\{\s*)?" + inner + r"\s*:\s*\{\s*eq\s*:\s*\"([^\"]+)\"", q)
    return m.group(1) if m else None


def rows_of(seed: dict, *tables: str) -> list[dict]:
    return [r for t in tables for r in seed.get(t) or []]


def by_id(seed: dict, item: str, *tables: str) -> dict | None:
    return next((r for r in rows_of(seed, *tables) if str(r.get("id", r.get("channel_id"))) == item), None)


def box_excludes(a, item, seed):
    query, types = param(a, "query"), (param(a, "content_types") or "").lower()
    rec = by_id(seed, item, "box_files", "box_folders")
    if not query or not types or rec is None:
        return None
    fields = []
    if "name" in types:
        fields.append(rec.get("name") or "")
    if "description" in types:
        fields.append(rec.get("description") or "")
    if "comments" in types:
        fields += [c.get("message") or "" for c in rows_of(seed, "box_comments") if str(c.get("file_id")) == item]
    if "tag" in types:
        fields += [str(rec.get("tags") or "")]
    text = " ".join(fields).lower()
    words = [w for w in re.findall(r"[a-z0-9]{3,}", query.lower()) if w not in STOP]
    return not all(w in text for w in words) if words else None


def slack_excludes(a, item, seed):
    types = param(a, "types")
    rec = by_id(seed, item, "channels")
    if not types or rec is None:
        return None
    kind = "private_channel" if rec.get("is_private") else "public_channel"
    return kind not in types


def calendar_excludes(a, item, seed):
    wanted = [unquote_plus(x) for x in re.findall(r"eventTypes?=([^&\"'\s]+)", a)]
    rec = by_id(seed, item, "calendar_events")
    if not wanted or rec is None:
        return None
    kind = rec.get("event_type") or rec.get("eventType") or "default"
    return kind not in ",".join(wanted)


def linear_issues_excludes(a, item, seed):
    rec = by_id(seed, item, "issues")
    if rec is None:
        return None
    parent, sub = gql_eq(a, "parent"), gql_eq(a, "subscribers")
    if parent:
        return rec.get("parentId") != parent
    if sub:
        subs = {r.get("userId") or r.get("user_id") for r in rows_of(seed, "issue_subscriber_user_association")
                if (r.get("issueId") or r.get("issue_id")) == item}
        return sub not in subs
    return None


def linear_documents_excludes(a, item, seed):
    name = gql_eq(a, "project", "name")
    rec = by_id(seed, item, "documents")
    if not name or rec is None:
        return None
    proj = by_id(seed, str(rec.get("projectId")), "projects")
    return (proj or {}).get("name") != name


IGNORED_FILTERS = {  # gap -> (test on the call, would the real service exclude the item?)
    "box: search ignores content_types": (lambda a: "/search" in a and "content_types" in a, box_excludes),
    "slack: users.conversations ignores types": (lambda a: "users.conversations" in a and "types" in a,
                                                 slack_excludes),
    "calendar: events.list ignores eventTypes": (lambda a: "/events" in a and "eventType" in a, calendar_excludes),
    "linear: issues ignores parent and subscribers": (lambda a: bool(re.search(r"issues\s*\(\s*filter", a) and
                                                                     re.search(r"\b(parent|subscribers)\s*:", a)),
                                                      linear_issues_excludes),
    "linear: documents ignores a project name": (lambda a: "documents" in a and bool(
        re.search(r"project\s*:\s*\{\s*name", a)), linear_documents_excludes),
}
FAILING = {  # gap -> test on (action, stdout)
    "linear: projects queries fail": lambda a, o: bool(re.search(r"\bprojects?\s*[({]", a)) and '"errors"' in o,
    "linear: nested connections fail": lambda a, o: "Cannot return null for non-nullable field" in o,
}


def rejected(a: str, o: str, question: str, seed: dict) -> tuple[str, bool] | None:
    """A write the replica rejected with a documented validation error, and whether the test is to blame."""
    if "invalid_name" in o:
        name = param(a, "name") or ""
        asked = bool(name) and (f":{name}:" in question or name.replace("_", " ") in question.lower())
        return "slack: reaction name rejected", asked
    if "must be a UUID" in o:
        ids = set(re.findall(r"\"([\w-]+)\"", a.replace('\\"', '"')))
        seeded = {str(r.get("id")) for r in rows_of(seed, "issue_labels")}
        return "linear: non-UUID label id rejected", bool(ids & seeded)
    return None


def attempts():
    """Each key's labelled attempt: the one autogen_02's attempts.json names, else the latest."""
    labelled = json.loads((RUNS / "autogen_02/eval/labels_phase3/attempts.json").read_text())
    index = defaultdict(list)
    for root in ROOTS:
        for att in root.glob("**/attempt-*"):
            if att.is_dir() and (att / "solver").is_dir():
                index["/".join(att.parent.relative_to(root).parts[-3:])].append(att)
    return {k: next((a for a in v if a.name == labelled.get(k)), sorted(v)[-1]) for k, v in index.items()}


def acted_on(att: Path) -> set[str]:
    """Ids of what the run changed: a changed row's own id, or what an inserted row attaches to."""
    p = att / "environment/diff_run.json"
    if not p.exists():
        return set()
    diff = (json.loads(p.read_text()) or {}).get("diff") or {}
    out = set()
    for kind in ("inserts", "updates", "deletes"):
        for row in diff.get(kind) or []:
            rec = row.get("after") or row.get("before") or row
            keys = REF_KEYS if kind == "inserts" else {OWN_KEY.get(row.get("__table__"), "id")}
            out |= {str(v) for k, v in rec.items() if k in keys and v not in (None, "") and str(v) not in ACTORS}
    return out


def presented(o: str, final: str) -> set[str]:
    """Ids of the items in a response that the agent's final answer names (by id, identifier, name or title)."""
    try:
        data = json.loads(o)
    except ValueError:
        return set()
    out, stack, low = set(), [data], final.lower()
    while stack:
        x = stack.pop()
        if isinstance(x, dict):
            iid = x.get("id") or x.get("channel_id")
            names = [str(x[k]) for k in NAME_KEYS if isinstance(x.get(k), str) and len(x[k]) >= 4]
            if iid and (mentions(final, str(iid)) or any(n.lower() in low for n in names)):
                out.add(str(iid))
            stack += list(x.values())
        elif isinstance(x, list):
            stack += x
    return out


def mentions(text: str, token: str) -> bool:
    return bool(re.search(r"(?<![\w.-])" + re.escape(token) + r"(?![\w-])", text))


def scan(att: Path) -> dict:
    traj = next(p for p in (att / "solver").glob("*.json") if p.name != "config.json")
    d = json.loads(traj.read_text())
    seed_p = att / "environment/initial_state.json"
    seed = json.loads(seed_p.read_text()) if seed_p.exists() else {}
    question = d.get("question") or ""
    final = str(d.get("final") or "")
    case_p = att / "case.json"
    has_target = (json.loads(case_p.read_text()).get("form") != "absent") if case_p.exists() else True
    asks = "?" in question or bool(re.match(r"\s*(which|what|who|how|list|tell)\b", question, re.I))
    concluded_none = bool(re.search(r"\b(no|none|not found|couldn't find|could not find|doesn't exist|does not "
                                    r"exist|there (is|are) no)\b", final, re.I))
    items = acted_on(att)
    hits, naive, cf = [], [], []
    first_seen: dict[str, int] = {}  # item -> the first step whose response mentions it
    for i, s in enumerate(d.get("steps") or [], 1):
        a = s.get("action") or ""
        a = a if isinstance(a, str) else json.dumps(a)
        obs = s.get("observation") or {}
        o = obs.get("stdout", "") if isinstance(obs, dict) else str(obs)
        for gap, (test, excludes) in IGNORED_FILTERS.items():
            if test(a):
                shown = items or presented(o, final)  # with no change, what the final answer names
                back = {t: excludes(a, t, seed) for t in sorted(shown) if mentions(o, t)}
                hits.append({"step": i, "gap": gap, "returned_acted_on": back})
                if back:
                    naive.append(("mock", gap, i))
                # the ignored filter introduced the item: the agent had not seen it before this response
                if any(v is True and first_seen.get(t, i) == i for t, v in back.items()):
                    cf.append(("mock", gap, i))
        for t in items or presented(o, final):
            if mentions(o, t):
                first_seen.setdefault(t, i)
        for gap, test in FAILING.items():
            if test(a, o):
                hits.append({"step": i, "gap": gap})
                naive.append(("mock", gap, i))
                # the test has a target, and the agent concluded none: changed nothing, or answered "none"
                if has_target and (concluded_none if asks else not items):
                    cf.append(("mock", gap + ", then concluded none", i))
        rej = rejected(a, o, question, seed)
        if rej:
            hits.append({"step": i, "gap": rej[0], "test_to_blame": rej[1]})
            naive.append(("test-construction", rej[0], i))
            if rej[1]:
                cf.append(("test-construction", rej[0], i))
    term = d.get("termination")
    if term not in ("done", None):
        naive.append(("harness", f"termination {term}", None))
        if term != "turn_limit" and not items:  # a turn limit is the agent's own budget; a prior write decided
            cf.append(("harness", f"termination {term} before any change", None))
    top = lambda fl: (Counter(f[0] for f in fl).most_common(1) or [[None]])[0][0]
    return {"attempt": att.relative_to(RUNS).as_posix(), "termination": term, "has_target": has_target,
            "acted_on": sorted(items),
            "hits": hits, "naive": [list(f) for f in naive], "counterfactual": [list(f) for f in cf],
            "named_naive": top(naive), "named_counterfactual": top(cf)}


def table(rows, scans, rule):
    tab = defaultdict(Counter)
    for r in rows:
        s = scans[r["key"]]
        flagged = bool(s[rule])
        tab[r["owner"]]["trials"] += 1
        tab[r["owner"]]["flagged"] += flagged
        named = s["named_" + rule]
        tab[r["owner"]]["named_right"] += flagged and (named == r["owner"] or named in r["also"])
    return {o: dict(tab[o]) for o in ("agent", "none") + NOT_AGENT}


def main():
    rows = json.loads((HERE / "devset.json").read_text())["rows"]
    atts = attempts()
    scans = {r["key"]: scan(atts[r["key"]]) for r in rows}
    result = {"naive": table(rows, scans, "naive"), "counterfactual": table(rows, scans, "counterfactual")}
    for rule in ("naive", "counterfactual"):
        print(f"\n== {rule}\nowner              trials flagged named_right")
        for o, c in result[rule].items():
            print(f"{o:18} {c.get('trials', 0):6d} {c.get('flagged', 0):7d} {c.get('named_right', 0):11d}")
    print("\ncounterfactual flags that disagree with the owner, and misses:")
    for r in rows:
        s = scans[r["key"]]
        f = bool(s["counterfactual"])
        if (f and r["owner"] not in NOT_AGENT) or (not f and r["owner"] in NOT_AGENT):
            mark = "MISS" if r["owner"] in NOT_AGENT else "FLAG"
            print(f"  {mark} {r['key']} owner={r['owner']} ({r['outcome']}) flags={s['counterfactual'][:2]}")
    unknown = Counter(h["gap"] for s in scans.values() for h in s["hits"]
                      for v in (h.get("returned_acted_on") or {}).values() if v is None)
    print("\nignored-filter returns the counterfactual could not judge:", dict(unknown))
    print("terminations:", Counter(s["termination"] for s in scans.values()))
    result["scans"] = scans
    (HERE / "source3_traces.json").write_text(json.dumps(result, indent=1) + "\n")


if __name__ == "__main__":
    main()
