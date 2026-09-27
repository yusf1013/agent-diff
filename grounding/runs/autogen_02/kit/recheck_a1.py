"""Re-check autogen_01's derived tests of given scenarios with fdc (as its kit does since v2), to see whether a defect
found in an autogen_02 variant was already in the autogen_01 test it comes from.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.autogen_02.kit.recheck_a1 AP-SLK-03 AP2-SLK-03 ...
"""
import json
import sys
from pathlib import Path

from grounding.runs.autogen_01.kit.derive import normalize_effects
from grounding.runs.fact_coverage_01.pilot.common import finish

A1_RUNS = Path(__file__).resolve().parents[2] / "autogen_01" / "runs"

for sid in sys.argv[1:]:
    for path in sorted(A1_RUNS.glob(f"gen_arm_*/cases/*/*{sid}*.json")):
        case = normalize_effects(json.loads(path.read_text()))
        _, _, errors = finish(case)
        print(f"{path.parent.parent.parent.name}/{path.name}: {errors or 'ok'}")
