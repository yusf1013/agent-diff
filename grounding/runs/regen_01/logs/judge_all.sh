#!/bin/bash
# Judge v2 on Muse for this study's runs, one after another (regen_01 step 5).
cd /home/yusf/PyProj/agent-diff/.claude/worktrees/regen
PY=/home/yusf/PyProj/agent-diff/backend/.venv/bin/python
R=grounding/runs/regen_01
for run in "$@"; do
  echo "=== judge $run start $(date -u +%FT%TZ)"
  AUTOGEN_BACKEND=muse $PY grounding/runs/fact_coverage_02/launch.py grounding.runs.autogen_02.kit.judge2 run \
      --trials $R/runs/judge_$run.trials.json --out $R/runs/judged_$run --concurrency 6
  echo "=== judge $run end $(date -u +%FT%TZ) exit $?"
done
echo "JUDGE DONE"
