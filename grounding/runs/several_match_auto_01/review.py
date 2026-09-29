"""Review the judge's reported failures, for its true and false positives.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.several_match_auto_01.review [--all]

For each failed trial in grades.json (a missed target, a near miss or another record acted on):
- a near miss acted on: which of the reference query's conditions it fails (fdc, filter by filter and edge by edge),
  so the failure's ground is visible;
- a missed target: its placement and whether the agent's trajectory ever mentioned its id;
- the final answer's head.
A failure is a true positive when the diff shows the action (by construction), the record fails a stated condition
(or is a missed target of a valid case), and the case was valid. The verdicts I record go to review.json.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from grounding.runs.fact_coverage_01 import fdc

HERE = Path(__file__).resolve().parent


def failing_conditions(seed, query, row):
    out = []
    for f in query.get("filters") or []:
        if not fdc.compare(fdc.get_field(row, f["field"]), f["op"], f.get("value")):
            out.append(f"{f['field']} {f['op']} {f.get('value')!r} (has {fdc.get_field(row, f['field'])!r})")
    for e in query.get("edges") or []:
        kids = fdc._joined(seed, query["table"], row, e)
        ok = [k for k in kids if fdc.node_matches(seed, e["node"], k)]
        if "count" in e:
            if not fdc.compare(len(ok), e["count"]["op"], e["count"]["value"]):
                out.append(f"count of {e['node']['table']} {e['count']['op']} {e['count']['value']} (has {len(ok)})")
        elif not ok:
            out.append(f"no {e['node']['table']} meeting {json.dumps(e['node'].get('filters'))[:140]}")
    return out


def main(show_all):
    grades = json.loads((HERE / "grades.json").read_text())
    for t in grades["trials"]:
        if t["diligence"] == "complete" and t["discrimination"] == "clean" and not t["other_acted"] and not show_all:
            continue
        run, (tk, cid) = t["run"], t["trial"].split("/")
        att = sorted((HERE / "runs" / run / tk / cid).glob("attempt-*"))[-1]
        case = json.loads((att / "case.json").read_text())
        q, seed = case["references"][0]["query"], case["seed"]
        rows = {str(fdc.handle(q, r)): r for r in seed.get(q["table"]) or []}
        print(f"== {t['trial']} ({t['diligence']}, {t['discrimination']}) {case['prompt'][:150]}")
        for d, fact in t["decoys_acted"].items():
            print(f"   near miss {d} [{fact}] fails: {failing_conditions(seed, q, rows[d])}")
        for d in t["other_acted"]:
            r = rows.get(d)
            print(f"   other {d} fails: {failing_conditions(seed, q, r) if r else 'not a record of the kind'}")
        if t["missing"]:
            traj = next(p for p in (att / "solver").glob("*.json") if p.name != "config.json").read_text()
            print("   missed:", {m: (p, "seen" if m in traj else "never seen") for m, p in t["missing"].items()})
        print("   final:", t["final"][:260].replace("\n", " "))


if __name__ == "__main__":
    main("--all" in sys.argv)
