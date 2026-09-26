"""For chosen facts, print each hand-built and generated probe: the request, the decoy's explanation, and each trial's
outcome with the start of the solver's final answer.

    python3 -m grounding.runs.autogen_01.kit.contrast FACT [FACT ...]
"""
import json
import sys
from pathlib import Path

STUDY = Path(__file__).resolve().parents[1]
FEATURES = json.loads((STUDY / "eval" / "design_features.json").read_text())
FC2_RUNS = STUDY.parent / "fact_coverage_02" / "runs"
RUN_DIRS = {"hand-built, pilot facts": [FC2_RUNS / "method_pilot"],
            "hand-built, new facts": [FC2_RUNS / "method_new", FC2_RUNS / "method_new_lin25",
                                      FC2_RUNS / "method_new_slk21", STUDY / "runs" / "solve_control"],
            "generated, Arm R": [STUDY / "runs" / "solve_arm_r"], "generated, Arm P": [STUDY / "runs" / "solve_arm_p"],
            "generated, v2": [STUDY / "runs" / "solve_arm_p_v2"]}


def trials(origin, case_id):
    for run in RUN_DIRS[origin]:
        for t in ("t1", "t2", "t3"):
            attempts = sorted((run / t / case_id).glob("attempt-*"))
            if not attempts:
                continue
            final = attempts[-1] / "solver" / "final_response.md"
            text = final.read_text().strip().replace("\n", " ") if final.exists() else "(no final answer)"
            yield f"{run.name}/{t}", text


for fact in sys.argv[1:]:
    print(f"\n## {fact}")
    for r in FEATURES:
        if r["fact"] != fact:
            continue
        case = next((sorted((d / "t1" / r["case_id"]).glob("attempt-*")) for d in RUN_DIRS[r["origin"]]
                     if (d / "t1" / r["case_id"]).exists()), [])
        claim = json.loads((case[-1] / "case.json").read_text())["references"][0]["claims"][0] if case else {}
        print(f"\n**{r['origin']}: {r['case_id']}** ({r['family']}; failed {r['failures_3']}/{r['established_3']}; "
              f"{r['lure']})")
        print(f"- request: {r['prompt']}")
        print(f"- decoy: {claim.get('explanation')}")
        for where, text in trials(r["origin"], r["case_id"]):
            print(f"  - {where}: {text[:260]}")
