#!/bin/bash
# Start cycle 2 when cycle 1's runner (pid $1) has exited, so this session stays at 12 attempts in flight.
cd /home/yusf/PyProj/agent-diff/.claude/worktrees/baselines-01
until ! kill -0 "$1" 2>/dev/null; do sleep 30; done
echo "cycle 1 runner $1 ended at $(date -Is); starting cycle 2"
SOLVER_BACKEND=selfhost /home/yusf/PyProj/agent-diff/backend/.venv/bin/python grounding/runs/fact_coverage_02/launch.py \
  grounding.runs.openclaw_eval_01.run --out grounding/runs/baselines_01/cycle2/solve_01 \
  --cases-dir grounding/runs/baselines_01/cycle2/cases --trials 3 --concurrency 12
echo "cycle 2 runner ended at $(date -Is)"
