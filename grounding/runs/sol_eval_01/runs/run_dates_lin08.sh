#!/bin/bash
# The 16 tests of the October-15 Linear scenario (G4-LIN-08) that Sol never ran under the old agent clock, now run
# from their templates (grounding/runs/dates_02/suite), rendered to the run day; same harness as the rest of Sol's round
# (OpenClaw's own loop, the default login-store layout, 3 trials, 10 in flight).
cd /home/yusf/PyProj/agent-diff
L="backend/.venv/bin/python grounding/runs/fact_coverage_02/launch.py grounding.runs.openclaw_eval_01.run --backend openai --trials 3 --concurrency 10"
$L --out grounding/runs/sol_eval_01/runs/dates_lin08_regular --cases-dir grounding/runs/dates_02/suite/cases \
   --cases $(tr '\n' ' ' < grounding/runs/sol_eval_01/cases/dates_lin08_regular.txt) > grounding/runs/sol_eval_01/runs/dates_lin08_regular.log 2>&1
$L --out grounding/runs/sol_eval_01/runs/dates_lin08_policy --cases-dir grounding/runs/dates_02/suite/units \
   --cases $(tr '\n' ' ' < grounding/runs/sol_eval_01/cases/dates_lin08_policy.txt) > grounding/runs/sol_eval_01/runs/dates_lin08_policy.log 2>&1
echo "dates_lin08 done $(date)" >> grounding/runs/sol_eval_01/runs/dates_lin08_done.txt
