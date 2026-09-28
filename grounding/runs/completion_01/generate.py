"""Roadmap 6b: scenarios for the 26 remaining briefs (inputs/briefs_6b.json), with Phase 4's generator unchanged
(autogen_02/kit/generate.py: autogen_01's orchestrator on Muse, Phase 4's replica notes, its parse-failure fix) and
the frozen kit (tag grounding-freeze-01).

    AUTOGEN_BACKEND=muse AUTOGEN_WORK=<scratch>/ws/gen6b \
        python grounding/runs/fact_coverage_02/launch.py grounding.runs.completion_01.generate [--concurrency 6] \
        [--only ID ...]

Writes runs/gen_01/<scenario>/ as Phase 4 did (versions, checks, reader, outcome, the accepted case). Opaque ids
and test-side clocks are applied later, when the suite is built (the discussion after 6a, 2026-09-28): the writer
is not asked about either.
"""
from __future__ import annotations

import sys
from pathlib import Path

from grounding.runs.autogen_02.kit import generate as phase4  # noqa: F401  (patches the orchestrator as Phase 4 ran it)
from grounding.runs.autogen_01.kit import orchestrate

HERE = Path(__file__).resolve().parent


def main():
    args = sys.argv[1:]
    name = "gen_01"
    if "--run-name" in args:  # a later run (gen_02: the briefs Muse's 402s stopped), so earlier attempts stay
        i = args.index("--run-name")
        name = args[i + 1]
        del args[i:i + 2]
    sys.argv = ["generate", "--briefs", str(HERE / "inputs" / "briefs_6b.json"), "--run", str(HERE / "runs" / name),
                *args]
    orchestrate.main()


if __name__ == "__main__":
    main()
