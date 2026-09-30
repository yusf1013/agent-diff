#!/bin/bash
# The Sol round's regular tests of the Muse-written half: Phase 4 (suite_opaque) then 6b (completion_01), 3 trials.
cd /home/yusf/PyProj/agent-diff
L="backend/.venv/bin/python grounding/runs/fact_coverage_02/launch.py grounding.runs.openclaw_eval_01.run --backend openai --trials 3 --concurrency 10"
$L --out grounding/runs/sol_eval_01/runs/regular_p4 --cases-dir grounding/runs/openclaw_eval_01/suite_opaque/cases \
   --cases $(tr '\n' ' ' < grounding/runs/sol_eval_01/cases/regular_p4.txt) > grounding/runs/sol_eval_01/runs/regular_p4.log 2>&1
$L --out grounding/runs/sol_eval_01/runs/regular_6b --cases-dir grounding/runs/completion_01/suite/cases \
   --cases $(tr '\n' ' ' < grounding/runs/sol_eval_01/cases/regular_6b.txt) > grounding/runs/sol_eval_01/runs/regular_6b.log 2>&1
echo "regular done $(date)" >> grounding/runs/sol_eval_01/runs/regular_done.txt
