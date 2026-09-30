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
    $L grounding.runs.sol_eval_01.kit.policy decide [--before-br]   # eval/policy_decisions[_before_br].json (Sol and Qwen)
    $L grounding.runs.sol_eval_01.kit.policy decide --regen [--qwen DIR ...]  # eval/policy_decisions_regen.json
    $L grounding.runs.sol_eval_01.kit.policy decide --suite [--qwen DIR ...]  # eval/policy_decisions_suite.json (both halves)
    $L grounding.runs.sol_eval_01.kit.policy regress    # the copy on Qwen's verdicts, all units: decisions_population_*.json
    $L grounding.runs.sol_eval_01.kit.policy units      # Sol's case folders against the plans' Muse-parent units

Sol's verdicts: eval/judged_policy_<mode>/. Qwen's: openclaw_eval_01/runs/policy/judged_population_<mode>,
judged_population_6b_<mode>, and for Box units the first pass ran, judged_<mode>_look*.

The regenerated half (`decide --regen`): its units are regen_01's list (suite/units.json) restricted to the units its
cases folders hold, less any the rulings now leave out (regen_01's rulings wrapper is loaded through kit/sets.py). Its
duplicate pair is already cut from the folder, so each request runs once. The same rule decides each cell, with no
pre-registered order (the sequential reading then covers every unit and is not reported). Sol's verdicts:
eval/judged_regen_<mode>_01/; Qwen's, when the regen session has judged them, from the verdict folders given with
--qwen (judge2's layout, <dir>/<run>/<trial>/<unit>/verdict.json).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from grounding.runs.autogen_02.kit import sampler
from grounding.runs.openclaw_eval_01 import policy, rulings
from grounding.runs.report_01.kit.common import catalog, fact_id
from grounding.runs.sol_eval_01.kit import sets
from grounding.runs.sol_eval_01.kit.score import stalled, use_rulings_before_br

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
    sources = (("phase4_only", "phase4"), ("6b_only", "completion_01"))
    if any(u.get("source") == "regen_01" for u in valid):
        sources += (("regen_only", "regen_01"),)
    for name, src in sources:
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


def decide(suffix: str = "") -> dict:
    result = {"_about": "The eight policy cells on the Muse-parent units (Phase 4 and 6b), without G4-LIN-08's six "
                        "units: Sol's verdicts, and Qwen's on the same units (and on all Muse-parent units). Rule: "
                        "openclaw_eval_01/policy.py pooled_decision, fixed before the Qwen round's runs.",
              "left_out_clock": sorted(left_out_clock())}
    if suffix:
        result["rulings_file"] = "eval/known_defects_before_br.json (the file before the two blind-review rulings)"
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
    regular_vs_policy(result, EVAL / f"side_by_side_regular{suffix}.json")
    return result


def regular_vs_policy(result: dict, side: Path) -> None:
    """policy_space.py's "regular_vs_policy_facts": among the facts with a valid unit of the mode, which the regular
    tests expose (each agent on the same tests, kit/compare_qwen.py) and which fail a policy unit."""
    if not side.exists():
        return
    regular = json.loads(side.read_text())["facts_detect3"]
    for mode in MODES:
        overlap = {}
        for who, reg in (("sol", "sol"), ("qwen_same_units", "qwen_same_tests")):
            if who not in result[mode]["facts"]:
                continue
            view = result[mode]["facts"][who]
            valid, fails, exposed = set(view["facts_valid"]), set(view["facts_failing_detect3"]), set(regular[reg])
            overlap[who] = {"facts_with_a_valid_unit": len(valid),
                            "exposed_by_regular_and_failing_policy": len(valid & exposed & fails),
                            "failing_policy_only": len((valid & fails) - exposed),
                            "exposed_by_regular_only": len((valid & exposed) - fails),
                            "neither": len(valid - exposed - fails)}
        result[mode]["regular_vs_policy_facts"] = overlap


def regen_units(mode: str) -> dict[str, list[dict]]:
    """cell -> the regenerated half's valid units of one mode (see the docstring)."""
    listed = json.loads((sets.REGEN / "suite" / "units.json").read_text())["units"]
    folder = sets.SETS[f"regen_{mode}_01"]["cases"]
    cells: dict[str, list[dict]] = {}
    for u in listed:
        path = folder / u["domain"] / f"{u['unit']}.json"
        if u["mode"] != mode or not path.exists() or rulings.test_exclusion(json.loads(path.read_text())):
            continue
        cells.setdefault(f"{u['domain']}/{mode}", []).append({**u, "source": "regen_01"})
    return dict(sorted(cells.items()))


def decide_regen(qwen_dirs: list[Path]) -> dict:
    result = {"_about": "The eight policy cells on the regenerated half's units (regen_01): Sol's verdicts, and Qwen's "
                        "on the same units when given. Rule: openclaw_eval_01/policy.py pooled_decision."}
    for mode in MODES:
        cells = regen_units(mode)
        sol = outcomes_of([EVAL / f"judged_regen_{mode}_01"])
        mine = [d for d in qwen_dirs if mode in d.name]
        qwen = policy.population_outcomes(mine) if mine else {}
        result[mode] = {"units": sum(len(v) for v in cells.values()),
                        "cells": {cell: {"sol": decide_cell(valid, sol, []),
                                         **({"qwen_same_units": decide_cell(valid, qwen, [])} if qwen else {})}
                                  for cell, valid in cells.items()},
                        "facts": {"sol": facts_view(cells, sol), **({"qwen_same_units": facts_view(cells, qwen)}
                                                                   if qwen else {})},
                        "qwen_verdicts": [str(d) for d in mine]}
    regular_vs_policy(result, EVAL / "side_by_side_regular_regen.json")
    return result


def decide_suite(qwen_dirs: list[Path]) -> dict:
    """The eight cells on Sol's whole Muse-only suite: the first half's Muse-parent units (without G4-LIN-08's six) and
    the regenerated half's, pooled per cell as regen_01/policy_decide.py pools Qwen's Muse-only suite. Qwen on the same
    units (openclaw_eval_01's verdicts as qwen_outcomes reads them, and the regen session's from --qwen), and on the
    Muse-only suite as regen_01 decides it (with G4-LIN-08's six), which must reproduce regen_01's decisions."""
    result = {"_about": "The eight policy cells on Sol's whole Muse-only suite: the Muse-parent units of Phase 4 and 6b "
                        "(without G4-LIN-08's six) and the regenerated half's (regen_01). Sol's verdicts, Qwen's on the "
                        "same units, and Qwen's on regen_01's Muse-only suite (with G4-LIN-08's six). Rule: "
                        "openclaw_eval_01/policy.py pooled_decision; no pre-registered order.",
              "left_out_clock": sorted(left_out_clock())}
    for mode in MODES:
        first, regen = cell_units(mode, muse_only=True), regen_units(mode)
        cells = {c: first.get(c, []) + regen.get(c, []) for c in sorted(set(first) | set(regen))}
        with_clock = {}
        for cell, seq in policy.population_plan(mode)["cells"].items():
            valid, _ = policy.population_units(seq)
            with_clock[cell] = [u for u in valid if u.get("source") in MUSE] + regen.get(cell, [])
        sol = outcomes_of([EVAL / f"judged_policy_{mode}", EVAL / f"judged_regen_{mode}_01"])
        qwen = qwen_outcomes(mode)
        qwen.update(policy.population_outcomes([d for d in qwen_dirs if mode in d.name]))
        result[mode] = {
            "units": sum(len(v) for v in cells.values()),
            "cells": {cell: {"sol": decide_cell(valid, sol, []), "qwen_same_units": decide_cell(valid, qwen, []),
                             "qwen_with_g4_lin_08": decide_cell(with_clock[cell], qwen, [])}
                      for cell, valid in cells.items()},
            "facts": {"sol": facts_view(cells, sol), "qwen_same_units": facts_view(cells, qwen)},
            "qwen_verdicts": [str(d) for d in qwen_dirs if mode in d.name]}
    regular_vs_policy(result, EVAL / "side_by_side_regular_suite.json")
    return result


def units() -> None:
    """Sol's policy case folders must hold exactly the plans' valid Muse-parent units without G4-LIN-08's."""
    for mode in MODES:
        cells = cell_units(mode, muse_only=True)
        planned = {u["unit"] for v in cells.values() for u in v}
        folder = {p.stem for p in (STUDY / "cases" / f"policy_{mode}").glob("*/*.json")}
        print(mode, {"planned": len(planned), "in folder": len(folder), "planned, not in folder": sorted(planned - folder),
                     "in folder, not planned": sorted(folder - planned)},
              {cell: len(v) for cell, v in sorted(cells.items())})


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "regress":
        regress()
    elif cmd == "units":
        units()
    elif cmd == "decide" and ("--regen" in sys.argv or "--suite" in sys.argv):
        qwen = [Path(a) for a in sys.argv[sys.argv.index("--qwen") + 1:]] if "--qwen" in sys.argv else []
        if "--suite" in sys.argv:
            result, out = decide_suite(qwen), "policy_decisions_suite.json"
        else:
            result, out = decide_regen(qwen), "policy_decisions_regen.json"
        (EVAL / out).write_text(json.dumps(result, indent=1) + "\n")
        for mode in MODES:
            for cell, r in result[mode]["cells"].items():
                print(cell, " | ".join(f"{who}: {x.get('valid_units')} units {x.get('rate')} [{x.get('p10')}, "
                                       f"{x.get('p90')}] {x.get('decision')}" for who, x in r.items()))
    elif cmd == "decide":
        suffix = "_before_br" if "--before-br" in sys.argv else ""
        if suffix:
            use_rulings_before_br()
        result = decide(suffix)
        (EVAL / f"policy_decisions{suffix}.json").write_text(json.dumps(result, indent=1) + "\n")
        for mode in MODES:
            for cell, r in result[mode]["cells"].items():
                print(cell, " | ".join(f"{who}: {r[who].get('valid_units')} units {r[who].get('rate')} "
                                       f"[{r[who].get('p10')}, {r[who].get('p90')}] {r[who].get('decision')}"
                                       for who in ("sol", "qwen_same_units")))
    else:
        raise SystemExit(__doc__)


if __name__ == "__main__":
    main()
