"""openclaw_eval_01's rulings (rulings.py) and runner, pointed at this study's own rulings. Import this module before
anything that reads `rulings`; it changes nothing on disk.

Qwen's scenarios carry the ids of the briefs they were written for (G4-BOX-03, …), the same as Muse's scenarios on
those briefs, which judge v2 needs (it recognizes generated tests by those prefixes). The PI's rulings in
roadmap_01/known_defects.json are about Muse's scenarios and are keyed by those ids, so here they are replaced
whole:
- **The rulings file:** [rulings.json](rulings.json), my rulings on Qwen's scenarios from my review (eval/review.json),
  in known_defects.json's format.
- **Opaque ids:** this study's suite/ids/ only (6a's and 6b's folders hold Muse's mappings under the same scenario
  ids).
- **The budget:** rulings.py's, 10 minutes (the PI, 2026-09-29).
"""
from __future__ import annotations

from pathlib import Path

from grounding.runs.openclaw_eval_01 import rulings
from grounding.runs.openclaw_eval_01 import run as runner

HERE = Path(__file__).resolve().parent
RULINGS = HERE / "rulings.json"

assert rulings.BUDGET_S == 600, "rulings.py's budget changed; check the PI's 10 minutes"
rulings.KNOWN_DEFECTS = RULINGS
runner.KNOWN_DEFECTS = RULINGS
rulings.ID_DIRS = (HERE / "suite" / "ids",)
rulings._doc.cache_clear()
rulings._mapping.cache_clear()
