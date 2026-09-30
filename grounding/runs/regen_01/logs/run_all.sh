#!/bin/bash
# regen_01's three runs, one after another, 3 trials, 16 in flight (the lead, 2026-09-30).
cd /home/yusf/PyProj/agent-diff/.claude/worktrees/regen
PY=/home/yusf/PyProj/agent-diff/backend/.venv/bin/python
CONC=${CONC:-16}
for run in full_01 absence_01 underspecified_01; do
  echo "=== $run start $(date -u +%FT%TZ) concurrency $CONC"
  SOLVER_BACKEND=selfhost $PY grounding/runs/fact_coverage_02/launch.py grounding.runs.regen_01.run \
    --out grounding/runs/regen_01/runs/$run --cases-dir grounding/runs/regen_01/runs/${run}_cases \
    --trials 3 --concurrency $CONC --retry-infrastructure
  echo "=== $run end $(date -u +%FT%TZ) exit $?"
done
echo "ALL DONE $(date -u +%FT%TZ)"
