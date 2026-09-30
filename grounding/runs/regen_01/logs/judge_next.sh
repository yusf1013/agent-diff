#!/bin/bash
until grep -q "JUDGE DONE" /tmp/claude-1002/-home-yusf-PyProj-agent-diff--claude-worktrees-regen/2b026929-2835-4ddd-bd6c-3dec2f4c5c6c/scratchpad/logs/judge_1.log; do sleep 30; done
/tmp/claude-1002/-home-yusf-PyProj-agent-diff--claude-worktrees-regen/2b026929-2835-4ddd-bd6c-3dec2f4c5c6c/scratchpad/judge_all.sh underspecified_01 full_01_load absence_01_load underspecified_01_load
