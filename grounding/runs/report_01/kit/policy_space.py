"""RQ6: the policy tests on OpenClaw. Per cell (service x mode): the population decision (openclaw_eval_01's
`decisions_population_<mode>.json`, rule fixed before the runs), the first pass's decision, and the per-fact policy
space: the units derived for the cell (one absence twin per near-miss fact pair; one drop-F variant per dropped
condition), the valid ones under the PI's rulings, the ones with verdicts, the distinct catalog facts they hold, and
the facts with a failing trial (detect@3) or a failing first trial (detect@1).

A policy unit's fact is the fact of the near miss it keeps (absence) or of the condition it drops (drop-F).

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.report_01.kit.policy_space

Writes numbers/policy.json.
"""
from __future__ import annotations

from grounding.runs.autogen_02.kit import sampler
from grounding.runs.openclaw_eval_01 import policy
from grounding.runs.report_01.kit.common import DOMAINS, NUMBERS, RUNS, catalog, fact_id, load, write

P = RUNS / "openclaw_eval_01/runs/policy"


def main():
    cat = catalog()
    cov = load(NUMBERS / "coverage.json")["achieved"]
    out = {"cells": {}, "totals": {}}
    for mode in ("absence", "underspecified"):
        decisions = load(P / f"decisions_population_{mode}.json")
        first = load(P / f"decisions_{mode}.json")
        verdicts = [d for d in (P / f"judged_population_{mode}", P / f"judged_population_6b_{mode}") if d.exists()]
        outcomes = policy.population_outcomes(verdicts)
        earlier = policy.population_outcomes(sorted(P.glob(f"judged_{mode}_look*")))
        ran_first = policy.first_pass_units(mode)
        plan = policy.population_plan(mode)
        tot = {"units": 0, "valid": 0, "judged": 0, "facts_valid": 0, "facts_failing_detect3": 0,
               "facts_failing_detect1": 0, "facts_covered_regular": 0}
        for cell, seq in sorted(plan["cells"].items()):
            d = cell.split("/")[0]
            valid, _left = policy.population_units(seq)
            facts_valid, fail3, fail1 = set(), set(), set()
            judged = 0
            for u in valid:
                # Box's first-pass units keep their verdicts (openclaw_eval_01 README, "What ran").
                got = outcomes.get(u["unit"]) or (earlier.get(u["unit"], {}) if d == "box" and u["unit"] in ran_first
                                                  else {})
                fs = {fact_id(d, f) for f in u["facts"]} & set(cat[d])
                facts_valid |= fs
                if any(o in sampler.FAIL | sampler.PASS for o in got.values()):
                    judged += 1
                if any(o in sampler.FAIL for o in got.values()):
                    fail3 |= fs
                if got.get("t1") in sampler.FAIL:
                    fail1 |= fs
            dec = decisions[cell]
            fp = first.get(cell, {})
            row = {"units": len(seq), "valid": len(valid), "judged": judged,
                   "facts_valid": len(facts_valid), "facts_covered_regular": len(cov[d]["covered_facts"]),
                   "facts_failing_detect3": len(fail3), "facts_failing_detect1": len(fail1),
                   "failing_trials": dec["failing_trials"], "usable_trials": dec["usable_trials"],
                   "rate": dec["rate"], "p10": dec["p10"], "p90": dec["p90"], "decision": dec["decision"],
                   "first_pass_decision": fp.get("decision"),
                   "spread": dec["readings"]["spread"],
                   "any_of_runs": dec["readings"]["any_of_runs"], "all_runs": dec["readings"]["all_runs"],
                   "by_writer": {k: dec[k] for k in ("phase3_only", "phase4_only", "6b_only") if k in dec}}
            out["cells"][cell] = row
            for k in tot:
                tot[k] += row[k]
        out["totals"][mode] = tot
    # The per-fact policy space: one absence and one underspecified requirement per covered fact.
    covered = sum(len(cov[d]["covered_facts"]) for d in DOMAINS)
    out["per_fact_space"] = {"covered_facts": covered, "requirements": 2 * covered,
                             "facts_with_a_valid_unit": sum(t["facts_valid"] for t in out["totals"].values())}
    print(write("policy", out))
    for cell, r in out["cells"].items():
        print(cell, {k: v for k, v in r.items() if k not in ("any_of_runs", "all_runs", "by_writer", "spread")})
    print(out["totals"], out["per_fact_space"])


if __name__ == "__main__":
    main()
