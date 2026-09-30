"""The blind sample for judging this study's runs, drawn before the runs from the cases folders alone (so it cannot
depend on any outcome), stratified by service and form: 5 trials per stratum (all of a smaller stratum), 20 strata
(4 services x cover, probe, fact probe, absence twin, drop-F variant), about 100 trials. I label them by hand before
reading any verdict on them. No model calls.

    python3 grounding/runs/regen_01/blind.py SEED

Writes eval/blind_<run>.json for each run (full_01, absence_01, underspecified_01) in the format of autogen_02's
drawer (`keys`: run/trial/case), which judge v2's selection and comparison read, and eval/blind_strata.json: each
stratum's size in trials, the number drawn, and its weight (stratum size / drawn) for weighted estimates.
"""
from __future__ import annotations

import json
import random
import sys
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUNS = ("full_01", "absence_01", "underspecified_01")
PER_STRATUM = 5
TRIALS = ("t1", "t2", "t3")


def form(stem: str) -> str:
    for prefix, name in (("AT-", "absence"), ("U-", "underspecified"), ("FP-", "fact probe"), ("P-", "probe")):
        if stem.startswith(prefix):
            return name
    return "cover"


def main():
    seed = int(sys.argv[1])
    strata: dict[tuple[str, str], list[str]] = {}
    for run in RUNS:
        folder = HERE / "runs" / f"{run}_cases"
        for path in sorted(folder.glob("*/*.json")):
            if path.name == "suite.json":
                continue
            key = (path.parent.name, form(path.stem))
            strata.setdefault(key, []).extend(f"{run}/{t}/{path.stem}" for t in TRIALS)
    drawn, record = {run: [] for run in RUNS}, []
    for (domain, f), slots in sorted(strata.items()):
        rng = random.Random(f"{seed}:{domain}:{f}")
        pick = sorted(rng.sample(slots, min(PER_STRATUM, len(slots))))
        for key in pick:
            drawn[key.split("/")[0]].append(key)
        record.append({"domain": domain, "form": f, "trials": len(slots), "drawn": len(pick),
                       "weight": round(len(slots) / len(pick), 3) if pick else None})
    for run, keys in drawn.items():
        out = HERE / "eval" / f"blind_{run}.json"
        if out.exists():
            raise SystemExit(f"{out} exists: the sample is drawn once")
    (HERE / "eval").mkdir(exist_ok=True)
    now = datetime.now().isoformat()
    for run, keys in drawn.items():
        (HERE / "eval" / f"blind_{run}.json").write_text(json.dumps({
            "_about": "Blind sample for judge v2: drawn before the run from the cases folders alone, stratified by "
                      "service and form (blind.py); labelled by me before reading any verdict on these trials.",
            "cases_dir": f"grounding/runs/regen_01/runs/{run}_cases", "seed": seed, "drawn_at": now,
            "per_stratum": PER_STRATUM, "keys": sorted(keys)}, indent=1) + "\n")
    (HERE / "eval" / "blind_strata.json").write_text(json.dumps({"seed": seed, "drawn_at": now, "strata": record},
                                                                indent=1) + "\n")
    print(f"{sum(len(k) for k in drawn.values())} trials drawn: " + ", ".join(f"{r} {len(k)}" for r, k in drawn.items()))
    for s in record:
        print(f"  {s['domain']:9} {s['form']:15} {s['drawn']} of {s['trials']}")


if __name__ == "__main__":
    main()
