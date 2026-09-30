"""The accepted scenarios this study uses: one per brief, across its generation runs (runs/gen_*). No model calls.

A brief normally has one accepted attempt. The related-issue brief may have more (the lure rule in the README: at most
3 attempts, each in its own run); then inputs/choices.json names the run whose scenario is used, with the reason. A
brief with several accepted attempts and no recorded choice stops everything that reads this module.
"""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

from grounding.runs.autogen_01.kit.derive import normalize_effects

HERE = Path(__file__).resolve().parent
RUNS = HERE / "runs"
CHOICES = HERE / "inputs" / "choices.json"


def gens() -> list[Path]:
    return sorted(p for p in RUNS.glob("gen_*") if p.is_dir())


def accepted() -> dict[str, Path]:
    """scenario id -> the folder of the accepted attempt this study uses (runs/gen_NN/<id>)."""
    found = defaultdict(list)
    for gen in gens():
        for outcome in sorted(gen.glob("G4-*/outcome.json")):
            o = json.loads(outcome.read_text())
            if o.get("status") == "accepted":
                found[o["scenario_id"]].append(outcome.parent)
    choices = json.loads(CHOICES.read_text()) if CHOICES.exists() else {}
    out = {}
    for sid, folders in sorted(found.items()):
        if len(folders) == 1:
            out[sid] = folders[0]
            continue
        run = (choices.get(sid) or {}).get("run")
        pick = [f for f in folders if f.parent.name == run]
        if len(pick) != 1:
            raise SystemExit(f"{sid}: {len(folders)} accepted attempts ({[f.parent.name for f in folders]}); "
                             "record the one to use in inputs/choices.json")
        out[sid] = pick[0]
    return out


def accepted_cases() -> list[dict]:
    """The accepted cases, as the policy derivations take them (autogen_02's `normalize_effects`)."""
    out = []
    for sid, folder in accepted().items():
        case = json.loads((folder / "case.json").read_text())
        case["_arm"] = "regen_01"
        out.append(normalize_effects(case))
    return out
