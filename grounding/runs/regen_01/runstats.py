"""How the three runs and their host-load re-runs ended, for the README's run table. No model calls.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.regen_01.runstats

Per run (each trial's latest attempt): trials, endings (status/termination), trials over the solver's budget
(rulings.over_budget: 10 minutes less limiter waits), trials retried for an infrastructure error, and the timeouts
under host load in both readings (score.under_load: fewer than 10 completed model requests with a median over 30 s;
`literal`: every completed request over 30 s). Per re-run folder (runs/<run>_load): how the re-runs ended. Writes
eval/run_stats.json.
"""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

from grounding.runs.regen_01 import rules, score

HERE = Path(__file__).resolve().parent
RUNS = HERE / "runs"


def stats(run_dir: Path) -> dict:
    ends, over, load, literal, retried, trials = Counter(), [], [], [], 0, 0
    for root in sorted(p for p in run_dir.glob("t*/*") if p.is_dir() and any(p.glob("attempt-*"))):
        trials += 1
        attempts = sorted(root.glob("attempt-*"))
        retried += len(attempts) > 1
        attempt = attempts[-1]
        summary = json.loads((attempt / "execution_summary.json").read_text())
        ends[f"{summary.get('status')}/{summary.get('termination')}"] += 1
        key = f"{root.parent.name}/{root.name}"
        if rules.rulings.over_budget(attempt):
            over.append(key)
        heavy = score.under_load(attempt)
        if heavy:
            load.append({"trial": key, **heavy})
            if heavy["literal"]:
                literal.append(key)
    return {"trials": trials, "endings": dict(ends), "over_budget": len(over), "retried_infrastructure": retried,
            "host_load_timeouts": len(load), "host_load_timeouts_literal": len(literal), "host_load": load,
            "over_budget_trials": over}


def main():
    out = {"_about": __doc__.split("\n\n")[0]}
    for run in ("full_01", "absence_01", "underspecified_01"):
        out[run] = stats(RUNS / run)
        if (RUNS / f"{run}_load").exists():
            out[f"{run}_load"] = stats(RUNS / f"{run}_load")
    (HERE / "eval" / "run_stats.json").write_text(json.dumps(out, indent=1) + "\n")
    for name, s in out.items():
        if not name.startswith("_"):
            print(name, {k: v for k, v in s.items() if k not in ("host_load", "over_budget_trials")})


if __name__ == "__main__":
    main()
