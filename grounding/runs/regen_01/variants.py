"""The regenerated scenarios' drop-F (underspecified) variants: autogen_02's derivation unchanged (`variants2 dropf`,
on Muse: code relaxes one condition of the reference, the writer rewords the request without it, code checks the
wording and the cold reader reads it; up to two repairs), for this study's accepted scenarios (cases.py), as
completion_01/variants.py ran it for roadmap 6b.

    AUTOGEN_BACKEND=muse AUTOGEN_VARIANT_WS=<scratch>/ws/variants python grounding/runs/fact_coverage_02/launch.py \
        grounding.runs.regen_01.variants --out grounding/runs/regen_01/runs/dropf_01 [--concurrency 4] \
        [--scenarios ID ...]

Every accepted variant gets my manual read before it runs (the standing rule, with its question: can the action be
done to each intended match?). policy_units.py --dropf DIR then builds the units with opaque ids and clocks.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

from grounding.runs.autogen_02.kit import variants2
from grounding.runs.regen_01.cases import accepted_cases

variants2.source_cases = lambda source: accepted_cases()  # this study's scenarios in place of Phase 4's
if os.environ.get("AUTOGEN_VARIANT_WS"):
    variants2.WORKSPACES = Path(os.environ["AUTOGEN_VARIANT_WS"])


def main():
    sys.argv = ["variants2", "dropf", "--source", "phase4", *sys.argv[1:]]
    variants2.main()


if __name__ == "__main__":
    main()
