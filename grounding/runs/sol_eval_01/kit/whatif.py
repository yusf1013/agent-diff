"""What changes if the PI rules one more near miss flawed: Sol's and Qwen's regular totals on the same tests, and the
policy cells of that near miss's service, for both agents. Prints the result; with --json also writes it to
eval/whatif_<scenario>_<witness>.json. Nothing else is saved, and no ruling is applied. No model calls.

Adds one entry ({"scenario", "witness", "ruling": "flawed"}, as the rulings file records G4-BOX-11's "Seaport
Archive 2024") to a temporary copy of roadmap_01/known_defects.json, points openclaw_eval_01/rulings.py at it, and
reruns this kit's own copies unchanged: kit/score.py's `adjudicate` and `combine` (Sol with the stall rule, Qwen's
full_02/03/04 without it), kit/compare_qwen.py's `totals` and `facts` over the tests Sol keeps, and kit/policy.py's
`decide_cell` and `facts_view` on the Muse-parent units.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.sol_eval_01.kit.whatif G4-BOX-15 9102 [--json]
"""
from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

from grounding.runs.openclaw_eval_01 import rulings
from grounding.runs.sol_eval_01.kit import compare_qwen, policy, score


class _Rulings(type(Path())):
    """The temporary rulings file; `adjudicate` records its path relative to grounding/runs."""

    def relative_to(self, *args, **kwargs):
        return Path("temporary") / self.name


def main():
    args = [a for a in sys.argv[1:] if a != "--json"]
    if len(args) != 2:
        raise SystemExit(__doc__)
    scenario, witness = args
    domain = score._domain(scenario)
    result = {"_about": f"What-if: {scenario}'s near miss {witness} ruled flawed (kit/whatif.py; not a ruling).",
              "scenario": scenario, "witness": witness}
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        doc = json.loads(rulings.KNOWN_DEFECTS.read_text())
        doc["near_misses"].append({"scenario": scenario, "witness": witness, "ruling": "flawed", "why": "what-if"})
        (tmp / "known_defects.json").write_text(json.dumps(doc))
        rulings.KNOWN_DEFECTS = _Rulings(tmp / "known_defects.json")
        rulings._doc.cache_clear()

        sol, left = [], []
        for s in score.SETS:
            adj = score.adjudicate(s, score.EVAL / f"{s}.score.json", score.EVAL / f"judged_{s}" / s,
                                   score.STUDY / "runs" / s)
            sol += adj["tests"]
            left += [x["case_id"] for x in adj["left_out_tests"]]
        runs, parts = score.QWEN / "runs", []
        for run, domains in (("full_02", {"box"}), ("full_03", {"calendar", "linear", "slack"}),
                             ("full_04", {"box", "calendar", "linear", "slack"})):
            path = tmp / f"qwen_{run}.json"
            path.write_text(json.dumps(score.adjudicate(run, runs / f"{run}.score.json", runs / f"judged_{run}" / run,
                                                        runs / run, stalls=False)))
            parts.append((run, domains, path))
        ids = {r["case_id"] for r in sol}
        qwen = [r for r in score.combine(parts)["tests"] if r["case_id"] in ids]
        result["regular"] = {"sol_tests_left_out": sorted(left), "sol": compare_qwen.totals(sol),
                             "qwen_same_tests": compare_qwen.totals(qwen),
                             "sol_facts_detect3": sorted(f"{d} {f}" for d, f in compare_qwen.facts(sol, "exposed"))}
        for mode in policy.MODES:
            looks = policy.policy.population_plan(mode)["looks"]
            outcomes = {"sol": policy.outcomes_of([policy.EVAL / f"judged_policy_{mode}"]),
                        "qwen_same_units": policy.qwen_outcomes(mode)}
            cells = policy.cell_units(mode, muse_only=True)
            result[mode] = {"cells": {}, "facts": {}}
            for cell, valid in sorted(cells.items()):
                if cell.startswith(domain):
                    result[mode]["cells"][cell] = {
                        who: {k: r[k] for k in ("valid_units", "failing_trials", "usable_trials", "rate", "p10", "p90",
                                                "decision")}
                        for who, r in ((who, policy.decide_cell(valid, got, looks)) for who, got in outcomes.items())}
            for who, got in outcomes.items():
                v = policy.facts_view(cells, got)
                result[mode]["facts"][who] = {k: len(v[k]) for k in ("facts_valid", "facts_failing_detect3",
                                                                     "facts_failing_detect1")}
    print(json.dumps(result, indent=1))
    if "--json" in sys.argv:
        out = score.EVAL / f"whatif_{scenario}_{witness}.json"
        out.write_text(json.dumps(result, indent=1) + "\n")
        print("wrote", out.relative_to(score.STUDY))


if __name__ == "__main__":
    main()
