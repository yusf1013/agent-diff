"""openclaw_eval_01's rulings (rulings.py), taught this study's scenarios, and the solver budget as the PI settled it.
Import this module before anything that reads `rulings`; it changes nothing on disk.

- **Opaque ids:** the rulings name near misses by their original ids and look up the opaque ones in the suites' id
  folders; this study's (suite/ids/) is added to 6a's and 6b's. My rulings on this study's near misses are appended to
  roadmap_01/known_defects.json (the lead's decision, 2026-09-30), keyed by their scenario ids.
- **The budget:** 10 minutes on OpenClaw (the PI, 2026-09-29: every final run used OpenClaw's 600-second limit;
  grounding/protocols/briefs/README.md). A trial runs out the budget when OpenClaw's own turn limit ended it
  (termination "timeout"), or its turn time, rate-limiter waits excluded, passed 600 s. rulings.py still reads the
  withdrawn 8 minutes (BUDGET_S 480); `budget_8min` keeps that reading for comparisons.
"""
from __future__ import annotations

import json
from pathlib import Path

from grounding.runs.openclaw_eval_01 import rulings

HERE = Path(__file__).resolve().parent
BUDGET_S = 600
if HERE / "suite" / "ids" not in rulings.ID_DIRS:
    rulings.ID_DIRS = (*rulings.ID_DIRS, HERE / "suite" / "ids")
    rulings._mapping.cache_clear()

budget_8min = rulings.over_budget


def over_budget(attempt: Path) -> bool:
    summary = json.loads((attempt / "execution_summary.json").read_text())
    if summary.get("status") != "completed":
        return False
    if summary.get("termination") == "timeout":
        return True
    turn = (summary.get("turn_durations_s") or [0])[0]
    return turn - ((summary.get("usage") or {}).get("limiter_wait_s") or 0) > BUDGET_S


rulings.over_budget = over_budget
