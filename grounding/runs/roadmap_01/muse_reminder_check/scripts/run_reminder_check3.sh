#!/bin/bash
# The approved Muse check, third pass: the 4 Calendar trials whose bundles failed (no starlette in the second
# Python). Cached verdicts are reused, so only those 12 call Muse.
cd /home/yusf/PyProj/agent-diff/.claude/worktrees/autogen-02 || exit 1
export AUTOGEN_BACKEND=muse
D=grounding/runs/roadmap_01/muse_reminder_check
date -Is > $D/started_at_pass3.txt
/home/yusf/PyProj/agent-diff/backend/.venv/bin/python grounding/runs/fact_coverage_02/launch.py grounding.runs.autogen_02.kit.judge2 run \
  --trials $D/trials.json --out $D/judged --concurrency 4 > $D/run_pass3.log 2>&1
echo "exit $?" >> $D/run_pass3.log
date -Is > $D/ended_at_pass3.txt
