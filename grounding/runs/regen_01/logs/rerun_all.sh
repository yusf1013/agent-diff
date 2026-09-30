#!/bin/bash
# Re-run the timeouts under host load on the quiet host (the lead, 2026-09-30), at most 12 in flight.
cd /home/yusf/PyProj/agent-diff/.claude/worktrees/regen
PY=/home/yusf/PyProj/agent-diff/backend/.venv/bin/python
L="$PY grounding/runs/fact_coverage_02/launch.py"
export SOLVER_BACKEND=selfhost
echo "=== rerun full_01 start $(date -u +%FT%TZ)"
$L grounding.runs.regen_01.rerun_load full_01 --concurrency 12
echo "=== rerun full_01 end $(date -u +%FT%TZ) exit $?"
echo "=== rerun absence_01 + underspecified_01 start $(date -u +%FT%TZ)"
$L grounding.runs.regen_01.rerun_load absence_01 --concurrency 4 &
$L grounding.runs.regen_01.rerun_load underspecified_01 --concurrency 2 &
wait
echo "RERUN DONE $(date -u +%FT%TZ)"
