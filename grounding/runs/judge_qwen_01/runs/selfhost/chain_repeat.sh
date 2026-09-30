#!/bin/bash
# After the full replay (pid $1) ends, judge the 443 labelled executions a second time, same settings, into
# runs/selfhost_repeat: Qwen's run-to-run agreement at its default sampling, and whether the bar holds on a second draw.
cd /home/yusf/PyProj/agent-diff/.claude/worktrees/judge_qwen
while kill -0 "$1" 2>/dev/null; do sleep 20; done
mkdir -p grounding/runs/judge_qwen_01/runs/selfhost_repeat
echo "full run ended $(date -u +%FT%T); repeat starts" >> grounding/runs/judge_qwen_01/runs/selfhost_repeat/chain.log
SOLVER_BACKEND=selfhost /home/yusf/PyProj/agent-diff/backend/.venv/bin/python grounding/runs/fact_coverage_02/launch.py \
    grounding.runs.judge_qwen_01.replay run --set labelled --out runs/selfhost_repeat --concurrency 16 \
    > grounding/runs/judge_qwen_01/runs/selfhost_repeat/run_labelled.log 2>&1
echo "repeat ended $(date -u +%FT%T), exit $?" >> grounding/runs/judge_qwen_01/runs/selfhost_repeat/chain.log
