#!/bin/bash
# The Sol round's policy units of the Muse-written half, after the regular runs finish: absence, then underspecified.
cd /home/yusf/PyProj/agent-diff
until [ -f grounding/runs/sol_eval_01/runs/regular_done.txt ]; do sleep 60; done
L="backend/.venv/bin/python grounding/runs/fact_coverage_02/launch.py grounding.runs.openclaw_eval_01.run --backend openai --trials 3 --concurrency 10"
$L --out grounding/runs/sol_eval_01/runs/policy_absence --cases-dir grounding/runs/sol_eval_01/cases/policy_absence > grounding/runs/sol_eval_01/runs/policy_absence.log 2>&1
$L --out grounding/runs/sol_eval_01/runs/policy_underspecified --cases-dir grounding/runs/sol_eval_01/cases/policy_underspecified > grounding/runs/sol_eval_01/runs/policy_underspecified.log 2>&1
echo "policy done $(date)" >> grounding/runs/sol_eval_01/runs/policy_done.txt
