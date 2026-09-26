"""Re-check every derived test of a generated suite: does its reference still select exactly its expected set?

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.autogen_01.kit.check_derived GEN_RUN [...]

A probe or fact probe must have no match once the target is removed. A superlative condition ("the most recent")
breaks this: removing the target promotes the next candidate to the answer, so acting on it is correct, not a
failure. The scenario checks ran fdc on the cover only; this runs it on every derived test.
"""
import json
import sys
from pathlib import Path

from grounding.runs.fact_coverage_01 import fdc

bad = []
for run in sys.argv[1:]:
    for path in sorted(Path(run).glob("cases/*/*.json")):
        case = json.loads(path.read_text())
        seed = dict(case["seed"])
        for table, rows in case.get("derived_rows", {}).items():
            seed[table] = rows
        for ref in case["references"]:
            _, errors = fdc.check_reference(seed, ref)
            selection = [e for e in errors if "but query selects" in e]
            if selection:
                bad.append(f"{Path(run).name}/{path.name}: {selection[0][:200]}")
print("\n".join(bad) or "no derived test selects a record it should not")
print(len(bad), "derived tests whose reference selects something other than their expected set")
