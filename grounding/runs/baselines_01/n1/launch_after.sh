#!/bin/bash
# Start N1's run when the cycle 2 waiter (pid $1) has exited, keeping this session at 12 attempts in flight.
cd /home/yusf/PyProj/agent-diff/.claude/worktrees/baselines-01
until ! kill -0 "$1" 2>/dev/null; do sleep 30; done
echo "cycle 2 ended at $(date -Is); starting N1"
SOLVER_BACKEND=selfhost /home/yusf/PyProj/agent-diff/backend/.venv/bin/python grounding/runs/fact_coverage_02/launch.py \
  grounding.runs.openclaw_eval_01.run --out grounding/runs/baselines_01/n1/runs/gen_01/solve_01 \
  --cases-dir grounding/runs/baselines_01/n1/runs/gen_01/suite --trials 3 --concurrency 12
echo "N1 runner ended at $(date -Is)"
