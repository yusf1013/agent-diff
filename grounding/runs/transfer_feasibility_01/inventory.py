"""What each test depends on: the constructs a real-service seeding would have to create (no model calls).

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.transfer_feasibility_01.inventory

For each of the 565 final regular tests (openclaw_eval_01/runs/final_regular_with_6b.json) and the 441 valid policy
units (openclaw_eval_01's population plans, as policy.py builds them), from the case file the runs used:
- **constructs**: the (table, field) pairs the test reads. They come from the reference queries' filters and edges
  (with their fact tags), the near-miss claims' facts and the fields their mutations substitute (a SUB's join, a
  REPLACE's query), and the fields the request writes;
- **acting users**: distinct people other than the actor who must *do* something in the seed for it to be
  faithful on a real service: author, create, own, modify, upload, react, comment, resolve, assign, answer an
  invitation. Those need an account each. Assignees, members, grantees and invitees only need to exist;
- **dates**: whether the request names an absolute date, a weekday or relative date, or none, and whether the test
  runs on a fixed clock (Calendar's 2018-06-17 and known_defects' `clocks`);
- **flags**: records created after their last modification (openclaw_eval_01/impossible_times.json).

Writes inventory.json (one row per test or unit; each construct as "via|table|field|fact|to") and the construct
frequencies (constructs_seen.json).
"""
from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from grounding.runs.openclaw_eval_01 import policy

HERE = Path(__file__).resolve().parent
RUNS = HERE.parent
OC = RUNS / "openclaw_eval_01"
SUITES = ((OC / "suite_opaque" / "cases" / "suite.json", OC / "suite_opaque" / "cases"),
          (RUNS / "completion_01" / "suite" / "cases" / "suite.json", RUNS / "completion_01" / "suite" / "cases"))

ABSOLUTE = re.compile(r"\b(January|February|March|April|May|June|July|August|September|October|November|December)"
                      r"\s+\d{1,2}\b|\b\d{4}-\d{2}-\d{2}\b", re.I)
RELATIVE = re.compile(r"\b(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday|yesterday|today|tomorrow|"
                      r"tonight|this week|last week|next week|this month|last month|ago|overdue|morning|afternoon|"
                      r"evening|latest|most recent|newest|oldest|earliest|recently)\b", re.I)

# Seed fields that name a person who must act for the row to exist as seeded (an account each), per service.
ACTING = {
    "slack": {"messages": ["user_id"], "message_reactions": ["user_id"]},
    "linear": {"issues": ["creatorId"], "comments": ["userId", "resolvingUserId"], "attachments": ["creatorId"],
               "documents": ["creatorId", "updatedById"], "projects": ["creatorId"],
               "initiatives": ["creatorId"]},
    "box": {"box_files": ["created_by_id", "modified_by_id", "owned_by_id"],
            "box_folders": ["created_by_id", "modified_by_id", "owned_by_id"],
            "box_file_versions": ["modified_by_id"], "box_comments": ["created_by_id"],
            "box_tasks": ["created_by_id"], "box_task_assignments": ["assigned_by_id"],
            "box_hubs": ["created_by_id", "updated_by_id"], "box_hub_items": ["added_by_id"]},
    "calendar": {"calendars": ["owner_id"], "calendar_events": ["creator_email", "organizer_email"]},
}
# People who only need to exist (the actor or an admin can add them).
EXISTING = {
    "slack": {"channel_members": ["user_id"]},
    "linear": {"issues": ["assigneeId"], "team_memberships": ["userId"], "issue_subscriber_user_association": ["user_id"],
               "initiatives": ["ownerId"]},
    "box": {"box_task_assignments": ["assigned_to_id"]},
    "calendar": {"calendar_acl_rules": ["scope_value"], "calendar_event_attendees": ["email"]},
}
ACTORS = {"slack": {"U01AGENBOT9"}, "linear": {"u-actor"}, "box": {"30000000001"},
          "calendar": {"u_actor", "jordan.lee@northwind.example"}}


def load(path):
    return json.loads(Path(path).read_text())


def walk_query(node: dict, out: list, table: str | None = None):
    table = node.get("table", table)
    for f in node.get("filters", []):
        out.append({"table": table, "field": f["field"], "fact": f.get("fact"), "via": "filter"})
    for e in node.get("edges", []):
        child = e["node"].get("table")
        join = e.get("join") or {}
        out.append({"table": table, "field": join.get("parent"), "fact": e.get("fact"), "via": "edge",
                    "to": f"{child}.{join.get('child')}", "count": bool(e.get("count"))})
        walk_query(e["node"], out, child)


def constructs(case: dict) -> list[dict]:
    out = []
    for ref in case["references"]:
        walk_query(ref["query"], out)
        for c in ref.get("claims", []):
            out.append({"fact": c["requirement"], "via": "near miss", "witness": str(c["witness"]),
                        "family": c.get("family")})
            m = c.get("mutation") or {}
            if m.get("type") == "SUB" and m.get("replacement"):
                repl = m["replacement"]
                out.append({"table": ref["query"]["table"], "field": (repl.get("join") or {}).get("parent"),
                            "fact": None, "via": "near-miss substitute",
                            "to": f"{repl['node'].get('table')}.{(repl.get('join') or {}).get('child')}"})
                walk_query(repl["node"], out)
            if m.get("type") == "REPLACE" and m.get("query"):
                sub = []
                walk_query(m["query"], sub)
                for s in sub:
                    s["via"] = "near-miss substitute"
                out += sub
        for w in ref.get("written", []):
            t, _, f = w.partition(".")
            out.append({"table": t, "field": f, "fact": None, "via": "written"})
    return out


def people(case: dict, table_fields: dict) -> set[str]:
    actors = ACTORS[case["domain"]] | {str(case.get("acting_user_id"))}
    found = set()
    for table, fields in table_fields.get(case["domain"], {}).items():
        for row in case["seed"].get(table, []):
            for f in fields:
                v = row.get(f)
                if v not in (None, "", []) and str(v) not in actors:
                    found.add(str(v))
    return found


def responders(case: dict) -> set[str]:
    """Calendar attendees whose response someone other than the actor must give (not needsAction)."""
    if case["domain"] != "calendar":
        return set()
    actors = ACTORS["calendar"]
    return {a["email"] for a in case["seed"].get("calendar_event_attendees", [])
            if a.get("response_status") not in (None, "", "needsAction") and a.get("email") not in actors
            and not a.get("resource")}


def row(kind: str, case: dict, extra: dict, clocks: dict, impossible: dict) -> dict:
    prompt = case["prompt"]
    scenario = extra.get("scenario") or case["case_id"]
    acting = people(case, ACTING) | responders(case)
    return {"id": case["case_id"], "kind": kind, "domain": case["domain"], "form": extra.get("form"),
            "scenario": scenario, "run": extra.get("run"), "exposed": extra.get("exposed", []),
            "prompt": prompt, "constructs": constructs(case),
            "acting_users": sorted(acting), "existing_users": len(people(case, EXISTING) - acting),
            "absolute_date": bool(ABSOLUTE.search(prompt)), "relative_date": bool(RELATIVE.search(prompt)),
            "clock": "2018-06-17 (Calendar)" if case["domain"] == "calendar" else clocks.get(scenario),
            "impossible_times": case["case_id"] in impossible or scenario in impossible}


def main():
    cases = {}
    for index, folder in SUITES:
        for m in load(index):
            path = folder / m["domain"] / f"{m['case_id']}.json"
            if path.exists():
                cases[m["case_id"]] = (load(path), m)
    clocks = {c["scenario"]: c["now"] for c in load(RUNS / "roadmap_01" / "known_defects.json")["clocks"]}
    impossible = {t for r in load(OC / "impossible_times.json")["rows"] for t in r["tests"]}
    rows = []
    for t in load(OC / "runs" / "final_regular_with_6b.json")["tests"]:
        case, m = cases[t["case_id"]]
        rows.append(row("regular", case, {**m, **t}, clocks, impossible))
    for mode in ("absence", "underspecified"):
        for cell, seq in policy.population_plan(mode)["cells"].items():
            valid, _ = policy.population_units(seq)
            for u in valid:
                case = policy.unit_case(u)
                rows.append(row(mode, case, {"form": mode, "scenario": u.get("scenario")}, clocks, impossible))
    freq = defaultdict(Counter)
    for r in rows:
        seen = {(c.get("table"), c.get("field")) for c in r["constructs"] if c.get("table")}
        seen |= {("fact", c["fact"]) for c in r["constructs"] if c.get("fact")}
        for s in seen:
            freq[r["domain"]][f"{s[0]}.{s[1]}"] += 1
    compact = []
    for r in rows:  # one string per distinct construct keeps the file small
        seen = sorted({"|".join(str(c.get(k) or "") for k in ("via", "table", "field", "fact", "to"))
                       for c in r["constructs"]})
        compact.append({**r, "constructs": seen})
    (HERE / "inventory.json").write_text(json.dumps(compact, ensure_ascii=False, separators=(",", ":")) + "\n")
    (HERE / "constructs_seen.json").write_text(json.dumps(
        {d: dict(c.most_common()) for d, c in sorted(freq.items())}, indent=1) + "\n")
    kinds = Counter((r["domain"], r["kind"]) for r in rows)
    print(len(rows), "rows;", dict(kinds))
    acting = Counter(len(r["acting_users"]) for r in rows)
    print("acting users per test:", dict(sorted(acting.items())))
    for d in sorted(freq):
        print(d, len(freq[d]), "constructs")


if __name__ == "__main__":
    main()
