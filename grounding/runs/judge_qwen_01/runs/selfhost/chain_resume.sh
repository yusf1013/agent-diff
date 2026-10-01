#!/bin/bash
# Resume after the pause (the lead's order, 2026-09-30 afternoon): the second labelled pass into runs/selfhost_repeat,
# then the rest of the full replay into runs/selfhost. Same settings as before; 16 calls in flight.
cd /home/yusf/PyProj/agent-diff/.claude/worktrees/judge_qwen
L="/home/yusf/PyProj/agent-diff/backend/.venv/bin/python grounding/runs/fact_coverage_02/launch.py grounding.runs.judge_qwen_01.replay run"
mkdir -p grounding/runs/judge_qwen_01/runs/selfhost_repeat
echo "repeat starts $(date -u +%FT%T)" >> grounding/runs/judge_qwen_01/runs/selfhost/chain.log
SOLVER_BACKEND=selfhost $L --set labelled --out runs/selfhost_repeat --concurrency 16 \
    > grounding/runs/judge_qwen_01/runs/selfhost_repeat/run_labelled.log 2>&1
echo "repeat ended $(date -u +%FT%T), exit $?; the rest starts" >> grounding/runs/judge_qwen_01/runs/selfhost/chain.log
SOLVER_BACKEND=selfhost $L --set all --out runs/selfhost --concurrency 16 \
    > grounding/runs/judge_qwen_01/runs/selfhost/run_all_resume.log 2>&1
echo "rest ended $(date -u +%FT%T), exit $?" >> grounding/runs/judge_qwen_01/runs/selfhost/chain.log
