"""The policy decisions with this study's units: openclaw_eval_01's working rule (policy.py `pooled_decision`, fixed
before the population runs: all runs of every valid unit, units as the independent draws, a cluster bootstrap), on
the cells of a Muse-only suite. No model calls.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.regen_01.policy_decide absence|underspecified

Per cell (service and mode), the valid units by the rulings (`rules.py`: openclaw_eval_01's rulings with this
study's opaque ids and duplicates), with their verdicts:
- **Phase 4 and 6b** (Muse-written, in openclaw_eval_01's population plan, `source` phase4 or completion_01), with
  openclaw_eval_01's verdicts (the population runs; Box units the first pass ran keep its verdicts, as there);
- **this study's** (`source` regen_01), from runs/<absence_01|underspecified_01> and runs/judged_<run>/.
Reports the decision for the Muse-only suite (the three together), for this study's units alone, and for each
source apart, and writes runs/decisions_<mode>.json. A trial over the solver's budget is a failure (rulings.py).
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

from grounding.runs.regen_01 import rules
from grounding.runs.openclaw_eval_01 import policy as P

HERE = Path(__file__).resolve().parent
RUNS = HERE / "runs"
OE = P.OUT  # openclaw_eval_01/runs/policy
MUSE = ("phase4", "completion_01")
RUN = {"absence": "absence_01", "underspecified": "underspecified_01"}


def regen_cells(mode: str) -> dict[str, list[dict]]:
    """This study's valid units per cell: the cut's list, less any unit the rulings leave out now (a ruling made after
    the cut, such as G4-SLK-14's 'Marcus Webb Jr' near miss; the runner leaves such a unit out as well)."""
    run = RUN[mode]
    kept = json.loads((RUNS / f"{run}_cases.json").read_text())["tests"]
    by_unit = {u["unit"]: u for u in json.loads((HERE / "suite" / "units.json").read_text())["units"]}
    cells = defaultdict(list)
    for uid in kept:
        u = by_unit[uid]
        if rules.rulings.test_exclusion(json.loads((RUNS / f"{run}_cases" / u["domain"] / f"{uid}.json").read_text())):
            continue
        cells[f"{u['domain']}/{mode}"].append({**u, "source": "regen_01"})
    return cells


def per_unit(units: list[dict], outcomes: dict) -> list[tuple[int, int]]:
    out = []
    for u in units:
        usable = [o for o in outcomes.get(u["unit"], {}).values() if o in P.sampler.FAIL | P.sampler.PASS]
        if usable:
            out.append((sum(o in P.sampler.FAIL for o in usable), len(usable)))
    return out


def decide(mode: str) -> dict:
    lead_dirs = [OE / f"judged_population_{mode}", OE / f"judged_population_6b_{mode}"]
    first_dirs = sorted(OE.glob(f"judged_{mode}_look*"))
    mine = [RUNS / f"judged_{RUN[mode]}"]
    outcomes = P.population_outcomes([d for d in lead_dirs + mine if d.exists()])
    earlier = P.population_outcomes(first_dirs)
    ran = P.first_pass_units(mode)
    regen = regen_cells(mode)
    result = {}
    for cell, seq in P.population_plan(mode)["cells"].items():
        valid, _ = P.population_units(seq)
        muse = [u for u in valid if u.get("source") in MUSE]
        for u in muse:  # Box units the first pass ran keep its verdicts, as in openclaw_eval_01
            if u["domain"] == "box" and u["unit"] in ran and u["unit"] not in outcomes:
                outcomes[u["unit"]] = earlier.get(u["unit"], {})
        units = rules.rulings.merge_duplicate_units(muse + regen.get(cell, []), outcomes)
        missing = [u["unit"] for u in units if not outcomes.get(u["unit"])]
        decision = P.pooled_decision(per_unit(units, outcomes))
        if missing:
            decision["decision"] = f"incomplete: {len(missing)} valid units without verdicts"
        parts = {name: {k: v for k, v in P.pooled_decision(per_unit([u for u in units if u.get("source") in src],
                                                                     outcomes)).items()}
                 for name, src in (("regen_01", ("regen_01",)), ("phase4", ("phase4",)),
                                   ("6b", ("completion_01",)))}
        result[cell] = {"valid_units": len(units), "missing": missing, **decision, "by_source": parts}
    return result


def main():
    mode = sys.argv[1]
    result = decide(mode)
    (RUNS / f"decisions_{mode}.json").write_text(json.dumps(result, indent=1) + "\n")
    for cell, r in result.items():
        print(cell, {k: r.get(k) for k in ("valid_units", "rate", "p10", "p90", "decision")},
              {n: (p.get("units"), p.get("rate"), p.get("decision")) for n, p in r["by_source"].items()})


if __name__ == "__main__":
    main()
