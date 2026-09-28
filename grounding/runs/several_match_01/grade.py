"""Grade the several-match trials (plan.md, "Measures"): the acted-on set against the targets, per placement class.

    python grounding/runs/several_match_01/grade.py [RUN_DIR]      # default runs/main

For each trial, from its diff and trajectory:
- the acted-on set: the rows of the reference's effect table that changed (the row itself, or the row an inserted
  row names in the effect's `field`);
- exact / incomplete (a proper subset of the targets) / over-inclusive (a non-target acted on) / both / nothing;
- per target: its placement class, whether it was acted on, and the first step whose response names it (by id, or
  by the name, title, identifier or text the seed gives it). A missed target never named in a response was never
  retrieved; one that was named was retrieved and not acted on.
The hand reading (plan.md) checks these against the final answers and records the mechanism of each miss in
reading.md. Writes grades.json.
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
NAME_KEYS = ("name", "title", "summary", "message_text", "identifier")


def acted(case: dict, att: Path) -> set[str]:
    effect = case["references"][0]["effect"]
    diff = (json.loads((att / "environment/diff_run.json").read_text()) or {}).get("diff") or {}
    table, field = effect["table"], effect.get("field")
    key = (effect.get("key") or ["id"])[0]
    out = set()
    for kind in effect.get("changes", ["insert", "update", "delete"]):
        for row in diff.get(kind + "s") or []:
            if row.get("__table__") != table:
                continue
            rec = row.get("after") or row.get("before") or row
            out.add(str(rec.get(field) if field else rec.get(key, rec.get("id"))))
    return out


def labels(case: dict, ids: set[str]) -> dict[str, list[str]]:
    """Strings that name each id in a response: the id, and the seed row's name-like fields."""
    out = {i: [i] for i in ids}
    for rows in case["seed"].values():
        for row in rows:
            rid = str(row.get("id", row.get("message_id", row.get("channel_id"))))
            if rid in out:
                out[rid] += [str(row[k]) for k in NAME_KEYS if isinstance(row.get(k), str) and len(row[k]) >= 6]
    return out


def first_seen(att: Path, names: dict[str, list[str]]) -> dict[str, int | None]:
    traj = next(p for p in (att / "solver").glob("*.json") if p.name != "config.json")
    steps = json.loads(traj.read_text()).get("steps") or []
    seen = {i: None for i in names}
    for n, s in enumerate(steps, 1):
        o = (s.get("observation") or {}).get("stdout", "")
        for i, ns in names.items():
            if seen[i] is None and any(x in o for x in ns):
                seen[i] = n
    return seen


def main(run: Path):
    placements = json.loads((HERE / "placements.json").read_text())
    trials, by_class = [], defaultdict(Counter)
    for att in sorted(run.glob("t*/*/attempt-*")):
        if att != sorted(att.parent.glob("attempt-*"))[-1]:
            continue
        case = json.loads((att / "case.json").read_text())
        sid = case["case_id"]
        ref = case["references"][0]
        targets = {str(t) for t in ref["expected"]}
        decoys = {str(c["witness"]) for c in ref["claims"]}
        got = acted(case, att)
        place = {}
        seed_ids = {str(v): v for v in targets}
        for k, v in placements[sid].items():  # placements name targets by id or by message ref
            place.update({t: v for t in targets if t == k})
        if len(place) < len(targets):  # message refs: map by the order of the scenario's target list
            scen = json.loads((HERE / "scenarios" / f"{sid}.json").read_text())
            for ref_name, tid in zip(scen["reference"]["target"], ref["expected"]):
                place.setdefault(str(tid), placements[sid].get(ref_name, "?"))
        names = labels(case, targets | decoys)
        seen = first_seen(att, names)
        missing, extra = targets - got, got - targets
        verdict = ("exact" if not missing and not extra else "nothing" if not got else
                   "incomplete" if missing and not extra else "over-inclusive" if extra and not missing else "both")
        traj = next(p for p in (att / "solver").glob("*.json") if p.name != "config.json")
        final = str(json.loads(traj.read_text()).get("final") or "")
        row = {"trial": f"{att.parent.parent.name}/{sid}", "verdict": verdict, "acted": sorted(got),
               "missing": {t: {"class": place.get(t), "first_seen": seen.get(t)} for t in sorted(missing)},
               "decoys_acted": sorted(extra & decoys), "other_acted": sorted(extra - decoys),
               "decoys_seen": {d: seen.get(d) for d in sorted(decoys)}, "final": final[:600]}
        trials.append(row)
        for t in targets:
            by_class[place.get(t, "?")]["targets"] += 1
            by_class[place.get(t, "?")]["acted"] += t in got
    summary = {"trials": len(trials), "verdicts": dict(Counter(t["verdict"] for t in trials)),
               "recall_by_class": {c: f"{v['acted']}/{v['targets']}" for c, v in sorted(by_class.items())},
               "decoys_acted": sum(len(t["decoys_acted"]) for t in trials),
               "misses_never_seen": sum(1 for t in trials for m in t["missing"].values() if m["first_seen"] is None),
               "misses_seen": sum(1 for t in trials for m in t["missing"].values() if m["first_seen"] is not None)}
    (HERE / "grades.json").write_text(json.dumps({"summary": summary, "trials": trials}, indent=1) + "\n")
    print(json.dumps(summary, indent=1))
    for t in trials:
        print(f"{t['trial']:18} {t['verdict']:14} missing={t['missing']} decoys={t['decoys_acted']} "
              f"other={t['other_acted']}")


if __name__ == "__main__":
    main(Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "runs/main")
