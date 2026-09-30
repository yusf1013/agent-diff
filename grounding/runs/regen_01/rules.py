"""openclaw_eval_01's rulings (rulings.py), taught this study's scenarios. Import this module before anything that
reads `rulings`; it changes nothing on disk.

- **Opaque ids:** the rulings name near misses by their original ids and look up the opaque ones in the suites' id
  folders; this study's (suite/ids/) is added to 6a's and 6b's. My rulings on this study's near misses are in
  roadmap_01/known_defects.json (the lead's decision, 2026-09-30), keyed by their scenario ids.
- **Duplicate units** of this study (two drop-F variants with the same request, actor and seed: one test, the PI's
  rule of 2026-09-29) are added to `rulings.DUPLICATE_UNITS` from DUPLICATES below, once the derivation shows them.
- **The budget** is rulings.py's own since the lead's update of 2026-09-30 (10 minutes: OpenClaw's 600-second turn
  limit ended the turn, or agent time without limiter waits passed 600 s); this module no longer overrides it.
"""
from __future__ import annotations

from pathlib import Path

from grounding.runs.openclaw_eval_01 import rulings

HERE = Path(__file__).resolve().parent
DUPLICATES = {"U-G4-SLK-16-message_reactions_user": "U-G4-SLK-16-message_reactions"}  # duplicates.py on runs/dropf_01

if HERE / "suite" / "ids" not in rulings.ID_DIRS:
    rulings.ID_DIRS = (*rulings.ID_DIRS, HERE / "suite" / "ids")
    rulings._mapping.cache_clear()
rulings.DUPLICATE_UNITS.update(DUPLICATES)
