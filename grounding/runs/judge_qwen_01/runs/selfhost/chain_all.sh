#!/bin/bash
# Waits for the labelled replay (pid $1) to end, then runs the rest of the 2,139 into the same folder.
cd /home/yusf/PyProj/agent-diff/.claude/worktrees/judge_qwen
while kill -0 "$1" 2>/dev/null; do sleep 20; done
echo "labelled run ended $(date -u +%FT%T)" >> grounding/runs/judge_qwen_01/runs/selfhost/chain.log
SOLVER_BACKEND=selfhost /home/yusf/PyProj/agent-diff/backend/.venv/bin/python grounding/runs/fact_coverage_02/launch.py \
    grounding.runs.judge_qwen_01.replay run --set all --out runs/selfhost --concurrency 16 \
    > grounding/runs/judge_qwen_01/runs/selfhost/run_all.log 2>&1
echo "all run ended $(date -u +%FT%T), exit $?" >> grounding/runs/judge_qwen_01/runs/selfhost/chain.log
