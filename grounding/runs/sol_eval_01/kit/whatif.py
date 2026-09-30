"""What changes if the PI rules one more near miss flawed: Sol's and Qwen's regular totals on the same tests, and the
policy cells of that near miss's service, for both agents. Prints only; nothing is saved. No model calls.

Adds one entry ({"scenario", "witness", "ruling": "flawed"}, as the rulings file records G4-BOX-11's "Seaport
Archive 2024") to a temporary copy of roadmap_01/known_defects.json, points openclaw_eval_01/rulings.py at it, and
reruns this kit's own copies unchanged: kit/score.py's `adjudicate` and `combine` (Sol with the stall rule, Qwen's
full_02/03/04 without it), kit/compare_qwen.py's `totals` and `facts` over the tests Sol keeps, and kit/policy.py's
`decide_cell` and `facts_view` on the Muse-parent units.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.sol_eval_01.kit.whatif G4-BOX-15 9102
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
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    scenario, witness = sys.argv[1], sys.argv[2]
    domain = score._domain(scenario)
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
    print(f"with {scenario} {witness} flawed: Sol's tests left out {sorted(left)}")
    print("regular, Sol:", compare_qwen.totals(sol))
    print("regular, Qwen on the same tests:", compare_qwen.totals(qwen))
    print("Sol's facts at detect@3:", sorted(f"{d} {f}" for d, f in compare_qwen.facts(sol, "exposed")))
    for mode in policy.MODES:
        looks = policy.policy.population_plan(mode)["looks"]
        outcomes = {"sol": policy.outcomes_of([policy.EVAL / f"judged_policy_{mode}"]),
                    "qwen": policy.qwen_outcomes(mode)}
        cells = policy.cell_units(mode, muse_only=True)
        for cell, valid in sorted(cells.items()):
            if cell.startswith(domain):
                rows = {who: policy.decide_cell(valid, got, looks) for who, got in outcomes.items()}
                print(f"{cell}: {len(valid)} units | " + " | ".join(
                    f"{who} {r['failing_trials']}/{r['usable_trials']} {r['rate']} [{r['p10']}, {r['p90']}] "
                    f"{r['decision']}" for who, r in rows.items()))
        print(f"{mode} facts (valid, failing @3, @1):", {
            who: (len(v["facts_valid"]), len(v["facts_failing_detect3"]), len(v["facts_failing_detect1"]))
            for who, v in ((who, policy.facts_view(cells, got)) for who, got in outcomes.items())})


if __name__ == "__main__":
    main()
