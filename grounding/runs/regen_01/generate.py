"""Scenarios for the regeneration briefs (inputs/briefs_regen.json), with Phase 4's generator unchanged
(autogen_02/kit/generate.py: autogen_01's orchestrator on Muse, Phase 4's replica notes, its parse-failure fix) and
the frozen kit (tag grounding-freeze-01), as completion_01/generate.py ran it for roadmap 6b.

    AUTOGEN_BACKEND=muse AUTOGEN_WORK=<scratch>/ws/regen \
        python grounding/runs/fact_coverage_02/launch.py grounding.runs.regen_01.generate --run-name gen_01 \
        [--concurrency 6] [--only ID ...]

Writes runs/<run-name>/<scenario>/ as Phase 4 did (versions, checks, reader, outcome, the accepted case). Opaque ids
and test-side clocks are applied later, when the suite is built: the writer is asked about neither.
"""
from __future__ import annotations

import sys
from pathlib import Path

from grounding.runs.autogen_02.kit import generate as phase4  # noqa: F401  (patches the orchestrator as Phase 4 ran it)
from grounding.runs.autogen_01.kit import orchestrate

HERE = Path(__file__).resolve().parent


def main():
    args = sys.argv[1:]
    if "--run-name" not in args:
        raise SystemExit("--run-name is required (each batch or retry gets its own run folder)")
    i = args.index("--run-name")
    name = args[i + 1]
    del args[i:i + 2]
    sys.argv = ["generate", "--briefs", str(HERE / "inputs" / "briefs_regen.json"), "--run", str(HERE / "runs" / name),
                *args]
    orchestrate.main()


if __name__ == "__main__":
    main()
