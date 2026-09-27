#!/bin/bash
# The approved Muse check: judge v2 on batch 1's 30 blind-labelled trials, with reminders off for the judge.
cd /home/yusf/PyProj/agent-diff/.claude/worktrees/autogen-02 || exit 1
export AUTOGEN_BACKEND=muse
D=grounding/runs/roadmap_01/muse_reminder_check
date -Is > $D/started_at.txt
python3 grounding/runs/fact_coverage_02/launch.py grounding.runs.autogen_02.kit.judge2 run \
  --trials $D/trials.json --out $D/judged --concurrency 4 > $D/run.log 2>&1
echo "exit $?" >> $D/run.log
date -Is > $D/ended_at.txt
