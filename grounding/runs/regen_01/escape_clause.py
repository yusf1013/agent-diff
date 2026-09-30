"""Two figures behind the README's policy findings. No model calls.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.regen_01.escape_clause

- **No-target trials with and without the escape clause:** the failure rate over every probe and fact probe trial of
  `full_01` (the request ends "If there isn't one, just tell me"; judge v2's verdict or the provisional label, as
  `phase4 score` has it) against every absence-twin trial of `absence_01` (no escape clause), a trial over the
  solver's budget counting as a failure in both, as the policy decision counts it.
- **Calendar absence by writer:** openclaw_eval_01's current suite (Sonnet's, Phase 4's and 6b's units) and this
  study's units, each source's pooled decision, so that the change of decision in a Muse-only suite can be traced.
Writes eval/escape_clause.json.
"""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

from grounding.runs.regen_01 import rules
from grounding.runs.regen_01 import policy_decide as PD
from grounding.runs.openclaw_eval_01 import policy as P

HERE = Path(__file__).resolve().parent
RUNS = HERE / "runs"
R = rules.rulings


def no_target_regular() -> dict:
    score = json.loads((RUNS / "full_01.score.json").read_text())
    fail = passed = void = 0
    for t in score["tests"]:
        if not t["case_id"].startswith(("P-", "FP-")):
            continue
        for trial, r in t["trials"].items():
            attempts = sorted((RUNS / "full_01" / trial / t["case_id"]).glob("attempt-*"))
            if attempts and R.over_budget(attempts[-1]) or r["outcome"] in ("incorrect", "presented"):
                fail += 1
            elif r["outcome"] == "correct_absent":
                passed += 1
            else:
                void += 1
    return {"failing": fail, "passing": passed, "void": void, "rate": round(fail / (fail + passed), 3)}


def absence_twins() -> dict:
    outcomes = P.population_outcomes([RUNS / "judged_absence_01"])
    fail = sum(o in P.sampler.FAIL for u in outcomes.values() for o in u.values())
    passed = sum(o in P.sampler.PASS for u in outcomes.values() for o in u.values())
    return {"failing": fail, "passing": passed, "rate": round(fail / (fail + passed), 3)}


def calendar_absence_by_source() -> dict:
    mode = "absence"
    outcomes = P.population_outcomes([d for d in (P.OUT / f"judged_population_{mode}",
                                                  P.OUT / f"judged_population_6b_{mode}") if d.exists()])
    valid, _ = P.population_units(P.population_plan(mode)["cells"]["calendar/absence"])
    by = defaultdict(list)
    for u in valid:
        by[u.get("source") or "Sonnet (autogen_01; units without a source)"].append(u)
    out = {src: {k: v for k, v in P.pooled_decision(PD.per_unit(us, outcomes)).items()
                 if k in ("units", "rate", "p10", "p90", "decision")} for src, us in sorted(by.items())}
    regen = json.loads((RUNS / "decisions_absence.json").read_text())["calendar/absence"]
    out["regen_01"] = {k: regen["by_source"]["regen_01"].get(k) for k in ("units", "rate", "p10", "p90", "decision")}
    return out


def main():
    result = {"_about": __doc__.split("\n\n")[0], "no_target_regular_with_escape_clause": no_target_regular(),
              "absence_twins_without_it": absence_twins(), "calendar_absence_by_source": calendar_absence_by_source()}
    (HERE / "eval" / "escape_clause.json").write_text(json.dumps(result, indent=1) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "_about"}, indent=1))


if __name__ == "__main__":
    main()
