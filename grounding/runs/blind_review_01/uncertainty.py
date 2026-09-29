"""Approximate stratified case-cluster bootstrap for weighted agreement."""
from __future__ import annotations

import json
import random
from collections import defaultdict
from pathlib import Path

from finalize import verify_lock
from metrics import group

HERE = Path(__file__).resolve().parent


def main():
    verify_lock()
    rows = json.loads((HERE / "comparison.json").read_text())
    manifest = json.loads((HERE / "manifest.json").read_text())
    clusters = defaultdict(lambda: defaultdict(list))
    case_strata = defaultdict(set)
    for r in rows:
        cid = r["key"].split("/")[-1]
        clusters[r["stratum"]][cid].append(r)
        case_strata[cid].add(r["stratum"])
    assert all(len(s) == 1 for s in case_strata.values())
    strata = [(manifest["strata"][st]["eligible"], list(c.values())) for st,c in clusters.items()]
    estimates = defaultdict(list)
    rng = random.Random(2026092913)
    for _ in range(5000):
        sums = defaultdict(lambda: [0.0, 0.0])
        for population, cases in strata:
            draw = [r for case in rng.choices(cases, k=len(cases)) for r in case]
            weight = population / len(draw)
            for r in draw:
                ref = r["reference"]["outcome"]
                if ref is None:
                    continue
                for comparator in ("judge", "pipeline"):
                    if r[comparator] is None:
                        continue
                    pred = r[comparator]["outcome"]
                    k = comparator + "_exact"
                    sums[k][0] += weight * (ref == pred)
                    sums[k][1] += weight
                    if group(ref) != "void" and group(pred) != "void":
                        k = comparator + "_binary"
                        sums[k][0] += weight * (group(ref) == group(pred))
                        sums[k][1] += weight
        for k, (num, den) in sums.items():
            if den:
                estimates[k].append(num / den)
    def interval(vals):
        vals = sorted(vals)
        return {"lower": vals[int(0.025 * (len(vals)-1))], "upper": vals[int(0.975 * (len(vals)-1))]}
    out = {"replicates": 5000, "seed": 2026092913, "level": 0.95,
           "method": "Percentile bootstrap; resample observed case clusters within each domain/form stratum; retain all sampled repetitions; recalibrate each stratum to its eligible size; exclude uncertain/void rows only for the applicable metric. Approximate: no finite-population correction and no model of reference-label uncertainty.",
           "mechanical_note": "All 67 mechanical labels agree. An empirical bootstrap would be degenerate; no misleading [100%,100%] interval is reported.",
           "intervals": {k: interval(v) for k,v in estimates.items()}}
    (HERE / "uncertainty.json").write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
