"""Phase 4: generate scenarios for the rule-drawn briefs with autogen_01's pipeline on Muse (N7), with this study's
replica notes (which add the gaps autogen_01 found).

    AUTOGEN_BACKEND=muse python grounding/runs/fact_coverage_02/launch.py grounding.runs.autogen_02.kit.generate \
        --run grounding/runs/autogen_02/runs/phase4_gen --first N [--concurrency 6]

Takes the first N briefs of inputs/briefs_phase4.json in their fixed order. Everything else is autogen_01's
orchestrator unchanged (writer, mechanical checks, replica pre-checks, cold reader, derived suites), with its prompts
and method docs as they stand after autogen_01 (method v2).
"""
from __future__ import annotations

import os
import shutil
import sys
from pathlib import Path

os.environ.setdefault("AUTOGEN_WORK", "/tmp/autogen-02/ws/gen")

from grounding.runs.autogen_01.kit import orchestrate  # noqa: E402

STUDY = Path(__file__).resolve().parents[1]
_setup = orchestrate.setup_workspace


def setup_workspace(ws: Path, brief: dict):
    _setup(ws, brief)
    shutil.copy(STUDY / "inputs" / brief["domain"] / "replica.md", ws / "domain" / "replica.md")


orchestrate.setup_workspace = setup_workspace


def main():
    args = sys.argv[1:]
    first = None
    if "--first" in args:
        i = args.index("--first")
        first = int(args[i + 1])
        del args[i:i + 2]
    import json
    briefs = json.loads((STUDY / "inputs" / "briefs_phase4.json").read_text())
    ids = [b["scenario_id"] for b in briefs[:first]] if first else [b["scenario_id"] for b in briefs]
    sys.argv = ["generate", "--briefs", str(STUDY / "inputs" / "briefs_phase4.json"), *args, "--only", *ids]
    orchestrate.main()


if __name__ == "__main__":
    main()
