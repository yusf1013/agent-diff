"""Re-run the (current) mechanical checks on the accepted scenarios of generation runs, without agents or services.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.autogen_01.kit.recheck GEN_RUN [...]

Used after the main runs to see which accepted scenarios the checks added later would have sent back.
"""
import json
import sys
from pathlib import Path

from grounding.runs.autogen_01.kit import scenario

for run in sys.argv[1:]:
    for outcome_path in sorted(Path(run).glob("*/outcome.json")):
        o = json.loads(outcome_path.read_text())
        if o["status"] != "accepted":
            continue
        last = sorted(outcome_path.parent.glob("scenario-v*.json"))[-1]
        _, problems = scenario.build(json.loads(last.read_text()), o["brief"])
        if problems:
            print(f"{o['scenario_id']}:", *[f"\n  - {p[:300]}" for p in problems])
    print(run, "rechecked")
