"""Grade cycle 8 (plural covers and plural probes, cases_cover/) with the several-match grader's functions.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.several_match_02.grade_covers RUN_DIR

Per trial: the set acted on against the targets (method.md scoring). A missed target is reported with its placement
(placements_cover.json); a decoy acted on is a fact failure, reported with the fact it tests. For a plural probe
(no target), acting on the decoy is the failure. Final answers are kept for review: the fact method also counts
presenting the decoy as the match. Writes grades-<run name>.json.
"""
from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

from grounding.runs.several_match_01 import grade as base

HERE = Path(__file__).resolve().parent


def labels_by_id(case, ids):
    return {i: [f'"{i}"', f"'{i}'", f"={i}"] for i in ids}


def main(run: Path):
    placements = json.loads((HERE / "placements_cover.json").read_text())
    trials, by_class, by_fact = [], defaultdict(Counter), defaultdict(Counter)
    for att in sorted(run.glob("t*/*/attempt-*")):
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
        seen = base.first_seen(att, labels_by_id(case, targets | set(claims)))
        kind = "probe" if not targets else ("hard" if cid.endswith("-H") else "easy")
        traj = next(p for p in (att / "solver").glob("*.json") if p.name != "config.json")
        final = str(json.loads(traj.read_text()).get("final") or "")
        row = {"trial": f"{att.parent.parent.name}/{cid}", "kind": kind,
               "missing": {t: {"placement": place.get(t, "?"), "first_seen": seen.get(t)} for t in sorted(missing)},
               "decoys_acted": {d: claims[d] for d in sorted(extra & set(claims))},
               "other_acted": sorted(extra - set(claims)), "final": final[:500]}
        row["diligence"] = "missed" if missing else "complete"
        row["discrimination"] = "decoy acted" if row["decoys_acted"] else "clean"
        trials.append(row)
        for t in targets:
            by_class[place.get(t, "?")]["placed"] += 1
            by_class[place.get(t, "?")]["found"] += t in got
        for d, fact in claims.items():
            by_fact[(kind, fact)]["trials"] += 1
            by_fact[(kind, fact)]["acted"] += d in got
    summary = {
        "trials": len(trials),
        "by kind": {k: dict(Counter((t["diligence"], t["discrimination"]) for t in trials if t["kind"] == k))
                    for k in ("easy", "hard", "probe")},
        "targets found by placement": {c: f"{v['found']}/{v['placed']}" for c, v in sorted(by_class.items())},
        "decoy acted on, by kind and fact": {f"{k} {f}": f"{v['acted']}/{v['trials']}"
                                              for (k, f), v in sorted(by_fact.items())},
    }
    out = HERE / f"grades-{run.name}.json"
    out.write_text(json.dumps({"summary": summary, "trials": trials}, indent=1) + "\n")
    print(json.dumps(summary, indent=1))
    for t in trials:
        if t["missing"] or t["decoys_acted"] or t["other_acted"]:
            print(f"{t['trial']:20} {t['kind']:5} missing={t['missing']} decoys={t['decoys_acted']} "
                  f"other={t['other_acted'][:3]}")


if __name__ == "__main__":
    main(Path(sys.argv[1]))
