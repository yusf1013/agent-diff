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
FC_RUNS = HERE.parent / "fact_coverage_02" / "runs"
SINGLE_RUN = {"SLK-21": "method_new_slk21"}  # the fact method's run of each scenario's probes (method_new otherwise)
# Placements found invalid after the run. SLK-21's H and H2 put a target at 03:00 UTC on September 23, 20:00 on
# September 22 in the actor's time zone, so whether it matches is contestable (method.md, check 8; H3 moves it).
# A void target is neither required nor an error to act on.
VOID = {"SMC-SLK-21-H": {"1790132400.000101"}, "SMC-SLK-21-H2": {"1790132400.000101"}}


def labels_by_id(case, ids):
    return {i: [f'"{i}"', f"'{i}'", f"={i}"] for i in ids}


def single_target(source):
    """The fact method's result for a probe with singular wording on the same seed: (trials exposed, trials run).
    manual_labels.json lists the exposing trials; its scenario-artifact trials were superseded by SINGLE_RUN."""
    labels = json.loads((HERE.parent / "fact_coverage_02" / "manual_labels.json").read_text())
    run = SINGLE_RUN.get(source[2:].rsplit("-", 1)[0], "method_new")
    exposed = sum(1 for k, v in labels.items()
                  if k.startswith(run + "/") and k.endswith("/" + source) and v["outcome"] == "incorrect")
    return exposed, len(list((FC_RUNS / run).glob(f"t*/{source}")))


def probe_comparison(trials, cases):
    """The open question of method.md: does a plural probe expose a fact that the plural covers do not? Per plural
    probe: its fact, the singular probe's result, the plural probe's, and the plural covers' on the same fact."""
    rows = []
    for cid, case in sorted(cases.items()):
        if not case.get("source_probe"):
            continue
        fact = case["references"][0]["claims"][0]["requirement"]
        scen = cid.rsplit("-", 1)[0]
        mine = [t for t in trials if t["trial"].endswith("/" + cid)]
        covers = [t for t in trials if t["trial"].split("/")[1] in (f"{scen}-E", f"{scen}-H")]
        cover_hits = sum(1 for t in covers if fact in t["decoys_acted"].values())
        ex, n = single_target(case["source_probe"])
        rows.append({"probe": cid, "source": case["source_probe"], "fact": fact, "singular probe": f"{ex}/{n}",
                     "plural probe": f"{sum(1 for t in mine if t['decoys_acted'])}/{len(mine)}",
                     "plural covers": f"{cover_hits}/{len(covers)}"})
    return rows


def main(run: Path):
    placements = json.loads((HERE / "placements_cover.json").read_text())
    trials, by_class, by_fact, cases = [], defaultdict(Counter), defaultdict(Counter), {}
    for att in sorted(run.glob("t*/*/attempt-*")):
        if att != sorted(att.parent.glob("attempt-*"))[-1] or not (att / "environment/diff_run.json").exists():
            continue
        case = json.loads((att / "case.json").read_text())
        cid = case["case_id"]
        cases[cid] = case
        ref = case["references"][0]
        void = VOID.get(cid, set())
        targets = {str(t) for t in ref["expected"]} - void
        claims = {str(c["witness"]): c["requirement"] for c in ref["claims"]}
        got = base.acted(case, att) - void
        place = placements.get(cid, {})
        missing, extra = targets - got, got - targets
        seen = base.first_seen(att, labels_by_id(case, targets | set(claims)))
        kind = "probe" if not targets else ("easy" if cid.endswith("-E") else "hard")
        traj = next(p for p in (att / "solver").glob("*.json") if p.name != "config.json")
        final = str(json.loads(traj.read_text()).get("final") or "")
        row = {"trial": f"{att.parent.parent.name}/{cid}", "kind": kind,
               "missing": {t: {"placement": place.get(t, "?"), "first_seen": seen.get(t)} for t in sorted(missing)},
               "decoys_acted": {d: claims[d] for d in sorted(extra & set(claims))},
               "other_acted": sorted(extra - set(claims)), "final": final[:500]}
        row["tier"] = cid.rsplit("-", 1)[1]
        row["termination"] = json.loads((att / "execution_summary.json").read_text()).get("termination")
        # A timeout is a failure (the PI, 2026-09-28); its misses are not attributed to a placement.
        row["diligence"] = "timeout" if row["termination"] == "timeout" else "missed" if missing else "complete"
        row["discrimination"] = "decoy acted" if row["decoys_acted"] else "clean"
        trials.append(row)
        for t in targets if row["diligence"] != "timeout" else ():
            by_class[place.get(t, "?")]["placed"] += 1
            by_class[place.get(t, "?")]["found"] += t in got
        for d, fact in claims.items():
            by_fact[(kind, fact)]["trials"] += 1
            by_fact[(kind, fact)]["acted"] += d in got
    summary = {
        "trials": len(trials),
        "by kind": {k: dict(Counter(f"{t['diligence']}, {t['discrimination']}" for t in trials if t["kind"] == k))
                    for k in ("easy", "hard", "probe")},
        "by case": {c: dict(Counter(t["diligence"] for t in trials if t["trial"].endswith("/" + c)))
                    for c in sorted({t["trial"].split("/")[1] for t in trials if t["kind"] != "probe"})},
        "targets found by placement": {c: f"{v['found']}/{v['placed']}" for c, v in sorted(by_class.items())},
        "decoy acted on, by kind and fact": {f"{k} {f}": f"{v['acted']}/{v['trials']}"
                                              for (k, f), v in sorted(by_fact.items())},
        "plural probes against singular probes and plural covers": probe_comparison(trials, cases),
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
