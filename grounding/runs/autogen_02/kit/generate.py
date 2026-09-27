"""Phase 4: generate scenarios for the rule-drawn briefs with autogen_01's pipeline on Muse (N7), with this study's
replica notes (which add the gaps autogen_01 found).

    AUTOGEN_BACKEND=muse python grounding/runs/fact_coverage_02/launch.py grounding.runs.autogen_02.kit.generate \
        --run grounding/runs/autogen_02/runs/phase4_gen --first N [--start K] [--concurrency 6] [--only ID ...]

Takes briefs K+1..N of inputs/briefs_phase4.json in their fixed order (K = 0 by default), or the `--only` ids.
Everything else is autogen_01's orchestrator unchanged (writer, mechanical checks, replica pre-checks, cold reader,
derived suites), with its prompts and method docs as they stand after autogen_01 (method v2), except one robustness
fix: a scenario the builder cannot parse (it raised on a query node without a table, G4-SLK-04 at 00:39) goes back
to the writer as a finding instead of ending the brief with an error.
"""
from __future__ import annotations

import json
import os
import shutil
import sys
from pathlib import Path

os.environ.setdefault("AUTOGEN_WORK", "/tmp/autogen-02/ws/gen")

from grounding.runs.autogen_01.kit import orchestrate  # noqa: E402

STUDY = Path(__file__).resolve().parents[1]
_setup = orchestrate.setup_workspace
_build = orchestrate.scenario.build


def setup_workspace(ws: Path, brief: dict):
    _setup(ws, brief)
    shutil.copy(STUDY / "inputs" / brief["domain"] / "replica.md", ws / "domain" / "replica.md")


def safe_build(s, brief):
    try:
        return _build(s, brief)
    except Exception as exc:  # a malformed scenario is a finding for the writer, not a crash
        return None, [f"The scenario could not be built ({type(exc).__name__}: {exc}). Check every query node "
                      "against docs/format.md (each node needs its table, filters and edges)."]


orchestrate.setup_workspace = setup_workspace
orchestrate.scenario.build = safe_build


def main():
    args = sys.argv[1:]

    def take(flag):
        if flag in args:
            i = args.index(flag)
            value = int(args[i + 1])
            del args[i:i + 2]
            return value
        return None
    first, start = take("--first"), take("--start") or 0
    briefs = json.loads((STUDY / "inputs" / "briefs_phase4.json").read_text())
    if "--only" in args:
        ids = []
    else:
        ids = [b["scenario_id"] for b in briefs[start:first]]
    sys.argv = ["generate", "--briefs", str(STUDY / "inputs" / "briefs_phase4.json"), *args]
    if ids:
        sys.argv += ["--only", *ids]
    orchestrate.main()


if __name__ == "__main__":
    main()
