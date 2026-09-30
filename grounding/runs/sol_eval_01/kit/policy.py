"""The eight policy cells for Sol on the Muse-parent units, and Qwen's on the same units, under the fixed rule; and
the per-fact view. No model calls.

Copies `openclaw_eval_01/policy.py`'s `decide_population` with two changes: the units are the Muse-parent ones
(Phase 4's, source "phase4", and 6b's, source "completion_01"), without G4-LIN-08's six (clocked past the OpenAI
login's expiry); and Sol has no first-pass carve-out (Box's first-pass verdicts are Qwen's). Everything else is
imported unchanged from openclaw_eval_01/policy.py: the plans (`population_plan`), validity (`population_units`, the
PI's rulings), the budget (`population_outcomes`: a trial over OpenClaw's limit is "incorrect"), duplicates
(`rulings.merge_duplicate_units`), the rule (`pooled_decision`: cluster bootstrap over units, 20,000 resamples, seed
20260928, policy-level if p10 > 0.8, not if p90 < 0.8) and the other readings (`readings`). One addition, as in
kit/score.py: a provider stall recorded before runtime rule R3 caught it is void, not a budget failure.

The per-fact view copies report_01/kit/policy_space.py's loop: a unit's facts (`fact_id`, restricted to the catalog),
a fact failing at detect@3 when any trial of a unit holding it fails, at detect@1 when its first trial does.

    L="python grounding/runs/fact_coverage_02/launch.py"
    $L grounding.runs.sol_eval_01.kit.policy decide     # eval/policy_decisions.json (Sol and Qwen, both modes)
    $L grounding.runs.sol_eval_01.kit.policy regress    # the copy on Qwen's verdicts, all units: decisions_population_*.json

Sol's verdicts: eval/judged_policy_<mode>/. Qwen's: openclaw_eval_01/runs/policy/judged_population_<mode>,
judged_population_6b_<mode>, and for Box units the first pass ran, judged_<mode>_look*.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from grounding.runs.autogen_02.kit import sampler
from grounding.runs.openclaw_eval_01 import policy, rulings
from grounding.runs.report_01.kit.common import catalog, fact_id
from grounding.runs.sol_eval_01.kit.score import stalled

STUDY = Path(__file__).resolve().parents[1]
EVAL = STUDY / "eval"
QP = policy.OUT  # openclaw_eval_01/runs/policy
MUSE = ("phase4", "completion_01")
MODES = ("absence", "underspecified")


def left_out_clock() -> set[str]:
    sel = json.loads((STUDY / "cases" / "policy_selection.json").read_text())
    return {u for m in MODES for u in sel[m]["left_out_clock"]}


def outcomes_of(verdict_dirs: list[Path]) -> dict:
    """policy.population_outcomes, with a stalled attempt's trial dropped (void, to be re-run) instead of failed."""
    out = policy.population_outcomes(verdict_dirs)
    for d in verdict_dirs:
        for path in d.glob("*/*/*/verdict.json"):
            attempt = Path(json.loads(path.read_text()).get("attempt", ""))
            if attempt.exists() and stalled(attempt):
                out[path.parent.name].pop(path.parent.parent.name, None)
    return out


def qwen_outcomes(mode: str) -> dict:
    """Qwen's verdicts as decide_population reads them: the populations, then Box's first-pass units."""
    out = policy.population_outcomes([d for d in (QP / f"judged_population_{mode}", QP / f"judged_population_6b_{mode}")
                                      if d.exists()])
    earlier = policy.population_outcomes(sorted(QP.glob(f"judged_{mode}_look*")))
    ran = policy.first_pass_units(mode)
    for unit, trials in earlier.items():
        if unit in ran and unit not in out and "-BOX-" in unit:
            out[unit] = trials
    return out


def per_unit(valid: list[dict], outcomes: dict) -> list[tuple[int, int]]:
    rows = []
    for u in valid:
        usable = [o for o in outcomes.get(u["unit"], {}).values() if o in sampler.FAIL | sampler.PASS]
        if usable:
            rows.append((sum(o in sampler.FAIL for o in usable), len(usable)))
    return rows


def cell_units(mode: str, muse_only: bool) -> dict[str, list[dict]]:
    """cell -> its valid units in the fixed order (the PI's rulings), Muse-parent only when asked."""
    drop = left_out_clock() if muse_only else set()
    cells = {}
    for cell, seq in policy.population_plan(mode)["cells"].items():
        valid, _ = policy.population_units(seq)
        if muse_only:
            valid = [u for u in valid if u.get("source") in MUSE and u["unit"] not in drop]
        cells[cell] = valid
    return cells


def decide_cell(valid: list[dict], outcomes: dict, looks: list[int]) -> dict:
    outcomes = {k: dict(v) for k, v in outcomes.items()}
    valid = rulings.merge_duplicate_units(valid, outcomes)
    missing = [u["unit"] for u in valid if not outcomes.get(u["unit"])]
    decision = policy.pooled_decision(per_unit(valid, outcomes))
    if missing:
        decision["decision"] = f"incomplete: {len(missing)} valid units without verdicts"
    parts = {}
    for name, src in (("phase4_only", "phase4"), ("6b_only", "completion_01")):
        part = [u for u in valid if u.get("source") == src]
        parts[name] = {k: v for k, v in policy.pooled_decision(per_unit(part, outcomes)).items() if k != "decision"}
    return {"valid_units": len(valid), "missing": missing, **decision,
            "readings": policy.readings(valid, outcomes, looks), **parts}


def facts_view(cells: dict[str, list[dict]], outcomes: dict) -> dict:
    """report_01/kit/policy_space.py's per-fact loop over the given units."""
    cat = catalog()
    out, facts_valid, fail3, fail1 = {}, set(), set(), set()
    for cell, valid in sorted(cells.items()):
        d = cell.split("/")[0]
        fv, f3, f1 = set(), set(), set()
        for u in valid:
            got = outcomes.get(u["unit"], {})
            fs = {fact_id(d, f) for f in u["facts"]} & set(cat[d])
            fv |= fs
            if any(o in sampler.FAIL for o in got.values()):
                f3 |= fs
            if got.get("t1") in sampler.FAIL:
                f1 |= fs
        out[cell] = {"facts_valid": len(fv), "facts_failing_detect3": len(f3), "facts_failing_detect1": len(f1)}
        facts_valid |= {f"{d} {f}" for f in fv}
        fail3 |= {f"{d} {f}" for f in f3}
        fail1 |= {f"{d} {f}" for f in f1}
    return {"cells": out, "facts_valid": sorted(facts_valid), "facts_failing_detect3": sorted(fail3),
            "facts_failing_detect1": sorted(fail1)}


def regress() -> None:
    """The copy on Qwen's verdicts over every valid unit must give decisions_population_<mode>.json's rate, bounds,
    decision and writer parts."""
    for mode in MODES:
        theirs = json.loads((QP / f"decisions_population_{mode}.json").read_text())
        outcomes, looks = qwen_outcomes(mode), policy.population_plan(mode)["looks"]
        for cell, valid in cell_units(mode, muse_only=False).items():
            mine = decide_cell(valid, outcomes, looks)
            keys = ("valid_units", "units", "failing_trials", "usable_trials", "rate", "p10", "p90", "decision")
            assert {k: mine.get(k) for k in keys} == {k: theirs[cell].get(k) for k in keys}, (cell, mine, theirs[cell])
            for part in ("phase4_only", "6b_only"):
                if part in theirs[cell]:
                    assert mine[part] == theirs[cell][part], (cell, part, mine[part], theirs[cell][part])
            assert mine["readings"] == theirs[cell]["readings"], (cell, "readings")
            print(f"{cell}: reproduced ({mine['rate']} [{mine['p10']}, {mine['p90']}] {mine['decision']})")


def decide() -> dict:
    result = {"_about": "The eight policy cells on the Muse-parent units (Phase 4 and 6b), without G4-LIN-08's six "
                        "units: Sol's verdicts, and Qwen's on the same units (and on all Muse-parent units). Rule: "
                        "openclaw_eval_01/policy.py pooled_decision, fixed before the Qwen round's runs.",
              "left_out_clock": sorted(left_out_clock())}
    for mode in MODES:
        looks = policy.population_plan(mode)["looks"]
        sol = outcomes_of([EVAL / f"judged_policy_{mode}"])
        qwen = qwen_outcomes(mode)
        cells = cell_units(mode, muse_only=True)
        with_clock = {}
        for cell, seq in policy.population_plan(mode)["cells"].items():
            valid, _ = policy.population_units(seq)
            with_clock[cell] = [u for u in valid if u.get("source") in MUSE]
        result[mode] = {
            "cells": {cell: {"sol": decide_cell(valid, sol, looks), "qwen_same_units": decide_cell(valid, qwen, looks),
                             "qwen_with_g4_lin_08": decide_cell(with_clock[cell], qwen, looks)}
                      for cell, valid in cells.items()},
            "facts": {"sol": facts_view(cells, sol), "qwen_same_units": facts_view(cells, qwen)}}
    return result


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "regress":
        regress()
    elif cmd == "decide":
        result = decide()
        (EVAL / "policy_decisions.json").write_text(json.dumps(result, indent=1) + "\n")
        for mode in MODES:
            for cell, r in result[mode]["cells"].items():
                print(cell, " | ".join(f"{who}: {r[who].get('valid_units')} units {r[who].get('rate')} "
                                       f"[{r[who].get('p10')}, {r[who].get('p90')}] {r[who].get('decision')}"
                                       for who in ("sol", "qwen_same_units")))
    else:
        raise SystemExit(__doc__)


if __name__ == "__main__":
    main()
