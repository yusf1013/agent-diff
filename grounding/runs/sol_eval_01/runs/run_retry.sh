#!/bin/bash
# After the Sol round's sets finish: rerun the attempts that ended in infrastructure errors (R3: the intermittent
# "Unknown model" catalog resolution, provider limits), once per set, then record what is left.
cd /home/yusf/PyProj/agent-diff
until [ -f grounding/runs/sol_eval_01/runs/policy_done.txt ]; do sleep 120; done
L="backend/.venv/bin/python grounding/runs/fact_coverage_02/launch.py grounding.runs.openclaw_eval_01.run --backend openai --trials 3 --concurrency 8 --retry-infrastructure"
$L --out grounding/runs/sol_eval_01/runs/regular_p4 --cases-dir grounding/runs/openclaw_eval_01/suite_opaque/cases --cases $(tr '\n' ' ' < grounding/runs/sol_eval_01/cases/regular_p4.txt) > grounding/runs/sol_eval_01/runs/retry_regular_p4.log 2>&1
$L --out grounding/runs/sol_eval_01/runs/regular_6b --cases-dir grounding/runs/completion_01/suite/cases --cases $(tr '\n' ' ' < grounding/runs/sol_eval_01/cases/regular_6b.txt) > grounding/runs/sol_eval_01/runs/retry_regular_6b.log 2>&1
$L --out grounding/runs/sol_eval_01/runs/policy_absence --cases-dir grounding/runs/sol_eval_01/cases/policy_absence > grounding/runs/sol_eval_01/runs/retry_policy_absence.log 2>&1
$L --out grounding/runs/sol_eval_01/runs/policy_underspecified --cases-dir grounding/runs/sol_eval_01/cases/policy_underspecified > grounding/runs/sol_eval_01/runs/retry_policy_underspecified.log 2>&1
echo "retry done $(date)" >> grounding/runs/sol_eval_01/runs/retry_done.txt
