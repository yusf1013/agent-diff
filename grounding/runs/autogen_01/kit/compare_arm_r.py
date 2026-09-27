"""Arm R, fact by fact: what the exemplars exposed against what the generated suites exposed, on the same facts.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.autogen_01.kit.compare_arm_r \
        --gen-run GEN_RUN --score SCORE.json [--json OUT]

The exemplar side counts the cover controls and single-decoy probes (reruns supersede v1), the same 76 tests as
fact_coverage_02 §6, at 3 trials. The generated side counts covers and probes; its fact probes are reported apart,
since the exemplars' 76 tests had none.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

EVAL = Path(__file__).resolve().parents[1] / "eval"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gen-run", type=Path, required=True)
    parser.add_argument("--score", type=Path, required=True)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    exemplars = json.loads((EVAL / "exemplar_outcomes.json").read_text())
    score = json.loads(args.score.read_text())
    tests = score["tests"]
    rows, totals = [], {"facts": 0, "ex": set(), "gen": set(), "gen_fp": set(), "ex_tests": 0, "gen_tests": 0,
                        "gen_fp_tests": 0, "accepted": 0}
    for outcome_path in sorted(args.gen_run.glob("*/outcome.json")):
        o = json.loads(outcome_path.read_text())
        ex_id = o["brief"].get("exemplar")
        ex = exemplars.get(ex_id, {})
        mine = [t for t in tests if t.get("scenario") == o["scenario_id"]]
        main_tests = [t for t in mine if t.get("form") in ("cover", "probe")]
        fp_tests = [t for t in mine if t.get("form") == "fact probe"]
        gen_exposed = {x for t in main_tests for x in t["exposed"]}
        fp_exposed = {x for t in fp_tests for x in t["exposed"]}
        for fact in o["brief"]["facts"]:
            rows.append({"scenario": ex_id, "fact": fact, "status": o["status"],
                         "exemplar_exposed": fact in ex.get("exposed", []),
                         "exemplar_uncontested": fact in ex.get("exposed_uncontested", []),
                         "generated_exposed": fact in gen_exposed,
                         "generated_fact_probe_exposed": fact in fp_exposed})
        totals["facts"] += len(o["brief"]["facts"])
        totals["ex"] |= {(ex_id, f) for f in ex.get("exposed", [])}
        totals["ex_tests"] += ex.get("tests", 0)
        if o["status"] == "accepted":
            totals["accepted"] += 1
            totals["gen"] |= {(ex_id, f) for f in gen_exposed if f in o["brief"]["facts"]}
            totals["gen_fp"] |= {(ex_id, f) for f in fp_exposed if f in o["brief"]["facts"]}
            totals["gen_tests"] += len(main_tests)
            totals["gen_fp_tests"] += len(fp_tests)
    both = sum(r["exemplar_exposed"] and r["generated_exposed"] for r in rows)
    only_ex = [f"{r['scenario']} {r['fact']}" for r in rows if r["exemplar_exposed"] and not r["generated_exposed"]]
    only_gen = [f"{r['scenario']} {r['fact']}" for r in rows if r["generated_exposed"] and not r["exemplar_exposed"]]
    result = {
        "briefs_accepted": totals["accepted"], "brief_facts": totals["facts"],
        "exemplar": {"tests": totals["ex_tests"], "facts_exposed": len(totals["ex"])},
        "generated": {"tests": totals["gen_tests"], "facts_exposed": len(totals["gen"]),
                      "fact_probe_tests": totals["gen_fp_tests"],
                      "facts_exposed_with_fact_probes": len(totals["gen"] | totals["gen_fp"])},
        "exposed_by_both": both, "only_exemplar": only_ex, "only_generated": only_gen, "rows": rows}
    print(json.dumps({k: v for k, v in result.items() if k != "rows"}, indent=1))
    if args.json:
        args.json.write_text(json.dumps(result, indent=1) + "\n")


if __name__ == "__main__":
    main()
