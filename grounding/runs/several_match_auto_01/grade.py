"""The judge: grade solver trials on the generated plural cover cases (method.md, scoring).

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.several_match_auto_01.grade RUN_DIR [RUN_DIR ...]

Per trial, from the environment's diff: the set of records acted on against the targets. A missed target is
attributed to its placement (placements.json: V plain view, C another container, H hidden, C1 one folder down,
O another folder, P past a page); a near miss acted on is a fact failure, with the fact it tests; any other record
of the kind acted on is reported too. A timeout is a failure and is not attributed to a placement. The final
answers are kept for review. Writes grades.json (merged across the run directories given).
"""
from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

from grounding.runs.several_match_01 import grade as base

HERE = Path(__file__).resolve().parent


def main(runs):
    placements = json.loads((HERE / "placements.json").read_text())
    trials, by_place, by_fact = [], defaultdict(Counter), defaultdict(Counter)
    for run in runs:
        for att in sorted(Path(run).glob("t*/SMA-*/attempt-*")):
            if att != sorted(att.parent.glob("attempt-*"))[-1] or not (att / "environment/diff_run.json").exists():
                continue
            case = json.loads((att / "case.json").read_text())
            cid = case["case_id"]
            ref = case["references"][0]
            targets = {str(t) for t in ref["expected"]}
            claims = {str(c["witness"]): c["requirement"] for c in ref["claims"]}
            got = base.acted(case, att)
            place = placements.get(cid, {})
            missing, extra = targets - got, got - targets
            summary = json.loads((att / "execution_summary.json").read_text())
            traj = next(p for p in (att / "solver").glob("*.json") if p.name != "config.json")
            row = {"trial": f"{att.parent.parent.name}/{cid}", "run": Path(run).name, "cover": case.get("source_cover"),
                   "tier": cid.rsplit("-", 1)[1], "domain": case["domain"],
                   "termination": summary.get("termination"),
                   "missing": {t: place.get(t, "?") for t in sorted(missing)},
                   "decoys_acted": {d: claims[d] for d in sorted(extra & set(claims))},
                   "other_acted": sorted(extra - set(claims)),
                   "final": str(json.loads(traj.read_text()).get("final") or "")[:600]}
            row["diligence"] = "timeout" if row["termination"] == "timeout" else "missed" if missing else "complete"
            row["discrimination"] = "decoy acted" if row["decoys_acted"] else "clean"
            trials.append(row)
            if row["diligence"] != "timeout":
                for t in targets:
                    by_place[place.get(t, "?")]["placed"] += 1
                    by_place[place.get(t, "?")]["found"] += t in got
            for d, fact in claims.items():
                by_fact[fact]["trials"] += 1
                by_fact[fact]["acted"] += d in got
    summary = {
        "trials": len(trials),
        "by tier": {t: dict(Counter(f"{r['diligence']}, {r['discrimination']}" for r in trials if r["tier"] == t))
                    for t in ("E", "H")},
        "targets found by placement": {p: f"{v['found']}/{v['placed']}" for p, v in sorted(by_place.items())},
        "near misses acted on, by fact": {f: f"{v['acted']}/{v['trials']}" for f, v in sorted(by_fact.items())
                                          if v["acted"]},
    }
    (HERE / "grades.json").write_text(json.dumps({"summary": summary, "trials": trials}, indent=1) + "\n")
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main(sys.argv[1:])
