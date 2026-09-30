#!/bin/bash
# The rest of the 6b regular set: 262 jobs failed instantly at 01:36-01:40 with a JSONDecodeError while
# roadmap_01/known_defects.json held merge-conflict markers (the lead's merge of exp/regen-01). The runner never
# redoes a completed attempt, so this runs the missing ones, alongside the policy pass, at a lower concurrency.
cd /home/yusf/PyProj/agent-diff
L="backend/.venv/bin/python grounding/runs/fact_coverage_02/launch.py grounding.runs.openclaw_eval_01.run --backend openai --trials 3 --concurrency 6"
$L --out grounding/runs/sol_eval_01/runs/regular_6b --cases-dir grounding/runs/completion_01/suite/cases \
   --cases $(tr '\n' ' ' < grounding/runs/sol_eval_01/cases/regular_6b.txt) >> grounding/runs/sol_eval_01/runs/regular_6b.log 2>&1
echo "regular done (6b completed in a second pass) $(date)" >> grounding/runs/sol_eval_01/runs/regular_done.txt
