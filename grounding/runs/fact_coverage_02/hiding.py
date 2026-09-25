"""Hidden-target tests (method.md, "hidden-target tests"): the easy-path check and the per-trial hiding class.
No service calls.

    python -m grounding.runs.fact_coverage_02.hiding            # backtest on the recorded target-present trials

- easy_paths(case, ref): every entry point's easy path, as fdc queries rooted at the reference's table, evaluated
  on the seed. Entry points: nodes the request names (an identifying eq filter), text the request quotes (contains
  filters and name-like eq filters), the case's declared `lures`, and Calendar's primary calendar. The paths follow
  the replica (see method.md): Slack history includes thread replies; Box and Calendar search match descriptions.
- hiding_errors(case): the rule's violations for a hidden-target test; suite builders refuse them.
- first_seen(attempt, ref) and hiding_class(): the first appearance of target and decoy ids in what the agent saw.
"""
from __future__ import annotations

import argparse
import copy
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from grounding.runs.fact_coverage_01 import fdc

HERE = Path(__file__).resolve().parent


def J(parent, child, op="eq"):
    return {"parent": parent, "child": child, "op": op}


# (root table, entry table) -> chains of (table, join) steps from the root down to the entry node.
EASY = {
    ("box_files", "box_folders"): [[("box_folders", J("parent_id", "id"))]],
    ("box_folders", "box_folders"): [[("box_folders", J("parent_id", "id"))]],
    ("box_tasks", "box_folders"): [[("box_files", J("item_id", "id")), ("box_folders", J("parent_id", "id"))]],
    ("box_comments", "box_folders"): [[("box_files", J("file_id", "id")), ("box_folders", J("parent_id", "id"))]],
    ("box_tasks", "box_files"): [[("box_files", J("item_id", "id"))]],
    ("box_comments", "box_files"): [[("box_files", J("file_id", "id"))]],
    ("box_files", "box_collections"): [[("box_collections", J("collections", "id", "json_contains"))]],
    ("box_folders", "box_collections"): [[("box_collections", J("collections", "id", "json_contains"))]],
    ("issues", "teams"): [[("teams", J("teamId", "id"))]],
    ("issues", "users"): [[("users", J("assigneeId", "id"))], [("users", J("creatorId", "id"))]],
    ("issues", "projects"): [[("projects", J("projectId", "id"))]],
    ("issues", "cycles"): [[("cycles", J("cycleId", "id"))]],
    ("issues", "issues"): [[("issues", J("parentId", "id"))]],
    ("comments", "issues"): [[("issues", J("issueId", "id"))]],
    ("attachments", "issues"): [[("issues", J("issueId", "id"))]],
    ("issue_labels", "issue_labels"): [[("issue_labels", J("parentId", "id"))]],
    ("documents", "projects"): [[("projects", J("projectId", "id"))]],
    ("documents", "initiatives"): [[("initiatives", J("initiativeId", "id"))]],
    ("project_milestones", "projects"): [[("projects", J("projectId", "id"))]],
    ("users", "teams"): [[("team_memberships", J("id", "userId")), ("teams", J("teamId", "id"))]],
    ("messages", "channels"): [[("channels", J("channel_id", "channel_id"))]],
    ("messages", "users"): [[("users", J("user_id", "user_id"))]],
    ("channels", "users"): [[("messages", J("channel_id", "channel_id")), ("users", J("user_id", "user_id"))]],
    ("calendar_events", "calendars"): [[("calendars", J("calendar_id", "id"))]],
}
# Text search per root table: (chain to the searched table, searched fields). An empty chain searches the root.
SEARCH = {
    "box_files": [([], ["name", "description"])],
    "box_folders": [([], ["name", "description"])],
    "box_tasks": [([("box_files", J("item_id", "id"))], ["name", "description"])],
    "box_comments": [([("box_files", J("file_id", "id"))], ["name", "description"])],
    "issues": [([], ["title", "description"])],
    "messages": [([], ["message_text"])],
    "channels": [([("messages", J("channel_id", "channel_id"))], ["message_text"])],
    "calendar_events": [([], ["summary", "description", "location"])],
}
# Declared lures: a named path that is not an anchor of the query.
LURES = {
    "calendar_named": ("calendar_events", [("calendars", J("calendar_id", "id"))], ["summary"]),
}
# Containers are few, and the natural first call lists them all (conversations.list, calendarList, teams, hubs,
# labels): for such a target the listing of everything is an easy path. Added after the backtest (SLK-24).
GLOBAL = {"channels", "calendars", "calendar_list_entries", "teams", "box_hubs", "issue_labels", "users"}
# A derived root is listed through its seed table: without singleEvents, events.list returns the series.
SEED_ROOT = {"occurrences": "calendar_events"}
IDENT = {"name", "title", "summary", "email", "login", "identifier", "id", "key", "displayName", "display_name",
         "real_name", "username", "channel_name", "team_name", "user_id", "channel_id"}
NAMELIKE = {"name", "title", "summary", "channel_name"}
ALIASES = {"calendar_list_entries": ["calendar_id"]}  # the public id the API shows for a seed row


def _chain(root, chain, leaf):
    """An fdc query on `root` that follows `chain` and ends in the node `leaf`."""
    query = {"table": root, "key": None, "filters": [], "edges": []}
    node = query
    for i, (table, join) in enumerate(chain):
        child = leaf if i == len(chain) - 1 else {"table": table, "filters": [], "edges": []}
        node["edges"].append({"key": f"p{i}", "join": join, "node": child})
        node = child
    return query


def _nodes(node, root=True):
    if not root:
        yield node
    for edge in node.get("edges", []):
        yield from _nodes(edge["node"], False)


def _text_filters(query):
    for node in [query] + list(_nodes(query)):
        for f in node.get("filters", []):
            if f["op"] == "contains_ci" or (f["op"] == "eq" and f["field"] in NAMELIKE and isinstance(f.get("value"), str)):
                yield f["value"]


def _search(root, chain, fields, phrase):
    out = []
    for field in fields:
        leaf = {"table": chain[-1][0] if chain else root,
                "filters": [{"key": "s", "field": field, "op": "contains_ci", "value": phrase}], "edges": []}
        out.append(_chain(root, chain, leaf) if chain else {"table": root, "filters": leaf["filters"], "edges": []})
    return out


def easy_paths(case, ref):
    """[(label, [handles])] for every entry point's easy path."""
    query, seed = ref["query"], case["seed"]
    root, key = SEED_ROOT.get(query["table"], query["table"]), query.get("key", ["id"])
    paths = []
    if root in GLOBAL:
        paths.append((f"all {root}", [{"table": root, "filters": [], "edges": []}]))
    for node in _nodes(query):
        named = [f for f in node.get("filters", []) if f["op"] in ("eq", "in") and f["field"] in IDENT]
        if not named:
            continue
        leaf = {"table": node["table"], "filters": copy.deepcopy(node.get("filters", [])),
                "edges": copy.deepcopy(node.get("edges", []))}
        for chain in EASY.get((root, node["table"]), []):
            label = f"{node['table']}[{','.join(str(f.get('value')) for f in named)}] via " + \
                    ".".join(step[1]["parent"] for step in chain)
            paths.append((label, [_chain(root, chain, leaf)]))
    primary = [e["calendar_id"] for e in seed.get("calendar_list_entries", [])
               if e.get("user_id") == case.get("acting_user_id") and e.get("primary")]
    in_primary = {"key": "d", "field": "calendar_id", "op": "in", "value": primary}
    for phrase in dict.fromkeys(_text_filters(query)):
        for chain, fields in SEARCH.get(root, []):
            queries = _search(root, chain, fields, phrase)
            if root == "calendar_events":  # q searches one calendar: the primary unless another is chosen
                for q in queries:
                    q["filters"].append(in_primary)
            paths.append((f"search '{phrase}'", queries))
    for lure in case.get("lures", []):
        lroot, chain, fields = LURES[lure["path"]]
        if lroot == root:
            paths.append((f"{lure['path']} '{lure['phrase']}'", _search(root, chain, fields, lure["phrase"])))
    if root == "calendar_events" and primary:
        paths.append(("primary calendar", [{"table": root, "edges": [], "filters": [in_primary]}]))
    out = []
    for label, queries in paths:
        handles = set()
        for q in queries:
            q["key"] = key
            handles |= {json.dumps(h, sort_keys=True) if not isinstance(h, str) else h for h in fdc.evaluate(seed, q)}
        out.append((label, sorted(handles)))
    return out


def layout(case, ref):
    """Which decoys and targets the easy paths return, and the two predicates of the rule."""
    targets = {str(x) for x in ref.get("expected") or []}
    decoys = {str(c["witness"]): c["requirement"] for c in ref.get("claims", [])}
    paths = easy_paths(case, ref)
    on = set().union(*(set(h) for _, h in paths)) if paths else set()
    return {"paths": [(label, sorted(set(h) & (targets | set(decoys)))) for label, h in paths],
            "decoys_on": sorted(set(decoys) & on), "targets_on": sorted(targets & on),
            "strict": bool(set(decoys) & on) and not (targets & on),
            "weak": any(set(h) & set(decoys) and not set(h) & targets for _, h in paths)}


def hiding_errors(case):
    """For a hidden-target test: exactly one decoy on the easy paths and no target on any of them."""
    errs = []
    for ref in case["references"]:
        if not ref.get("claims") or not ref.get("expected"):
            continue
        lay = layout(case, ref)
        if len(lay["decoys_on"]) != 1:
            errs.append(f"{ref['id']}: easy paths return {len(lay['decoys_on'])} decoys, not 1 ({lay['paths']})")
        if lay["targets_on"]:
            errs.append(f"{ref['id']}: easy paths return the target {lay['targets_on']} ({lay['paths']})")
    return errs


# --- per trial: what the agent saw first -------------------------------------------------------------------------

def _pattern(value):
    return re.compile(r"(?<![\w-])" + re.escape(str(value)) + r"(?![\w-])")


def _observations(attempt):
    records = [p for p in (attempt / "solver").glob("*.json") if p.name != "config.json"]
    if not records:  # an episode that never started or has not finished
        return
    for step in json.loads(records[0].read_text())["steps"]:
        obs = step.get("observation")
        if isinstance(obs, dict):
            obs = obs.get("stdout") or obs.get("output") or json.dumps(obs)
        yield step["turn"], str(obs or "")


def _aliases(case, ref, witness):
    table = ref["query"]["table"]
    key = ref["query"].get("key", ["id"])[0]
    names = [str(witness)]
    for row in case["seed"].get(table, []):
        if str(row.get(key)) == str(witness):
            names += [str(row[c]) for c in ALIASES.get(table, []) if row.get(c)]
    return names


def first_seen(attempt, case, ref):
    """(turn, offset) of the first appearance of any target, and of the earliest decoy with its id."""
    targets = [a for t in ref.get("expected") or [] for a in _aliases(case, ref, t)]
    decoys = {a: str(c["witness"]) for c in ref.get("claims", []) for a in _aliases(case, ref, c["witness"])}
    t_first = d_first = None
    for turn, obs in _observations(attempt):
        for name in targets:
            m = _pattern(name).search(obs)
            if m and (t_first is None or (turn, m.start()) < t_first):
                t_first = (turn, m.start())
        for name, witness in decoys.items():
            m = _pattern(name).search(obs)
            if m and (d_first is None or (turn, m.start()) < d_first[:2]):
                d_first = (turn, m.start(), witness)
    return t_first, d_first


def hiding_class(t_first, d_first):
    if t_first is None and d_first is None:
        return "neither seen"
    if t_first is None:
        return "decoy only"
    if d_first is None:
        return "target only"
    if d_first[0] < t_first[0]:
        return "decoy first"
    if d_first[0] > t_first[0]:
        return "target first"
    return "together, decoy listed first" if d_first[1] < t_first[1] else "together, target listed first"


HIDDEN_HELD = {"decoy first", "decoy only"}


# --- backtest -----------------------------------------------------------------------------------------------------

def backtest(load, runs=("b1", "method_new", "method_new_lin25", "method_new_slk21")):
    from grounding.runs.fact_coverage_02.analyze import current
    from grounding.runs.fact_coverage_02.score import FAILED
    rows, per_ref = [], {}
    for t in load(list(runs)):
        for trial, res in sorted(t["trials"].items()):
            attempts = sorted((HERE / "runs" / t["run"] / trial / t["case_id"]).glob("attempt-*"))
            if not attempts or res["outcome"] in ("not_established", "artifact"):
                continue
            case = current(json.loads((attempts[-1] / "case.json").read_text()))
            if "just tell me" in case["prompt"]:
                continue
            for ref in case["references"]:
                if not ref.get("claims") or not ref.get("expected"):
                    continue
                if ref["id"] not in per_ref:
                    per_ref[ref["id"]] = {"test": t["case_id"], "layout": layout(case, ref), "classes": []}
                reqs = {c["requirement"] for c in ref["claims"]}
                cls = hiding_class(*first_seen(attempts[-1], case, ref))
                acted = res["outcome"] in FAILED and bool(set(res["exposed"]) & reqs)
                per_ref[ref["id"]]["classes"].append(cls + ("*" if acted else ""))
                rows.append({"ref": ref["id"], "trial": f"{t['run']}/{trial}", "class": cls, "acted": acted})
    return rows, per_ref


def main():
    argparse.ArgumentParser(description=__doc__).parse_args()
    from grounding.runs.fact_coverage_02.tables import load
    rows, per_ref = backtest(load)
    counts = defaultdict(Counter)
    for r in rows:
        counts[r["class"]]["trials"] += 1
        counts[r["class"]]["acted"] += r["acted"]
    print("## What the agent saw first, target-present trials\n")
    print("| First appearance | Trials | Acted on a decoy |\n|---|---:|---:|")
    for k in ["decoy only", "decoy first", "together, decoy listed first", "together, target listed first",
              "target first", "target only", "neither seen"]:
        if counts[k]["trials"]:
            print(f"| {k} | {counts[k]['trials']} | {counts[k]['acted']} |")
    print("\n## Backtest of the rule on the seeds\n")
    print("| Reference | Strict (no target on any path) | Weak (some path without the target) | Decoys on paths | "
          "Targets on paths | Trials (first appearance; * acted on a decoy) |\n|---|---|---|---|---|---|")
    confusion = Counter()
    for rid, v in sorted(per_ref.items()):
        lay = v["layout"]
        seen = any(c.rstrip("*") in HIDDEN_HELD for c in v["classes"])
        confusion[(lay["strict"], lay["weak"], seen)] += 1
        print(f"| {rid} | {'yes' if lay['strict'] else 'no'} | {'yes' if lay['weak'] else 'no'} | "
              f"{', '.join(lay['decoys_on']) or '-'} | {', '.join(lay['targets_on']) or '-'} | {'; '.join(v['classes'])} |")
    print("\n| Strict | Weak | Decoy came back without the target in some trial | References |\n|---|---|---|---:|")
    for (strict, weak, seen), n in sorted(confusion.items(), key=lambda kv: (not kv[0][0], not kv[0][1], not kv[0][2])):
        print(f"| {'yes' if strict else 'no'} | {'yes' if weak else 'no'} | {'yes' if seen else 'no'} | {n} |")


if __name__ == "__main__":
    main()
