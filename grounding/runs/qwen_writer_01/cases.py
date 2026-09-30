"""Qwen's accepted scenarios, one per brief, across this study's generation runs. No model calls.

- **runs/gen_02** (medium effort, Claude Code's 32,000-token reply cap) accepted G4-BOX-03, G4-BOX-05 and G4-CAL-03
  before it was stopped. None of their writer replies reached the cap (largest 23,909, 30,103 and 16,526 tokens), and
  the cap changes nothing in the request but `max_tokens`, so gen_03's one change could not have changed them.
- **runs/gen_03** (the same with a 64,000-token cap): the other nine briefs.
- runs/gen_01_xhigh (the served default effort, stopped) is evidence only.

A brief accepted in more than one of these runs stops everything that reads this module.
"""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUNS = [HERE / "runs" / "gen_02", HERE / "runs" / "gen_03"]


def accepted() -> dict[str, Path]:
    """scenario id -> the folder of its accepted attempt (runs/gen_NN/<id>)."""
    found = defaultdict(list)
    for gen in RUNS:
        for outcome in sorted(gen.glob("G4-*/outcome.json")):
            o = json.loads(outcome.read_text())
            if o.get("status") == "accepted":
                found[o["scenario_id"]].append(outcome.parent)
    for sid, folders in found.items():
        if len(folders) > 1:
            raise SystemExit(f"{sid}: accepted in {[f.parent.name for f in folders]}")
    return {sid: folders[0] for sid, folders in sorted(found.items())}


def attempt(sid: str) -> Path | None:
    """The folder of the brief's attempt that counts: its accepted one, else its gen_03 attempt."""
    folder = accepted().get(sid)
    if folder:
        return folder
    last = RUNS[-1] / sid
    return last if last.exists() else None
