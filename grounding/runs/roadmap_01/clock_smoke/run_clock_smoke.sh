#!/bin/bash
# The approved Purdue smoke run of the agent clock: 6 Linear cases whose first attempts timed out under the old
# wall-clock budget, 1 trial each, on Qwen, with the study's solve wrapper (main pass, then infrastructure retries).
cd /home/yusf/PyProj/agent-diff/.claude/worktrees/autogen-02 || exit 1
export GROUNDING_ENV=/home/yusf/PyProj/agent-diff/grounding/.env
S=grounding/runs/roadmap_01/clock_smoke
date -Is > $S/started_at.txt
/home/yusf/PyProj/agent-diff/backend/.venv/bin/python grounding/runs/fact_coverage_02/launch.py \
  grounding.runs.autogen_02.kit.solve --cases-dir $S/cases --out $S/solve --trials 1 > $S/run.log 2>&1
echo "exit $?" >> $S/run.log
date -Is > $S/ended_at.txt
