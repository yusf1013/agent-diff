#!/bin/bash
# The Sol round's policy units of the Muse-written half, after the regular runs finish. The OpenAI plan's weekly
# window was at 71% at 01:20 (shared with the harness session's Codex smoke), so every unit runs once first
# (absence, then underspecified), and the second and third trials follow only after that; the runner never
# redoes a completed attempt, so the later passes add t2 and t3.
cd /home/yusf/PyProj/agent-diff
until [ -f grounding/runs/sol_eval_01/runs/regular_done.txt ]; do sleep 60; done
L="backend/.venv/bin/python grounding/runs/fact_coverage_02/launch.py grounding.runs.openclaw_eval_01.run --backend openai --concurrency 10"
for trials in 1 3; do
  $L --trials $trials --out grounding/runs/sol_eval_01/runs/policy_absence --cases-dir grounding/runs/sol_eval_01/cases/policy_absence >> grounding/runs/sol_eval_01/runs/policy_absence.log 2>&1
  $L --trials $trials --out grounding/runs/sol_eval_01/runs/policy_underspecified --cases-dir grounding/runs/sol_eval_01/cases/policy_underspecified >> grounding/runs/sol_eval_01/runs/policy_underspecified.log 2>&1
  echo "policy trials=$trials pass done $(date)" >> grounding/runs/sol_eval_01/runs/policy_progress.txt
done
echo "policy done $(date)" >> grounding/runs/sol_eval_01/runs/policy_done.txt
