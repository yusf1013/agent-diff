"""List accepted scenarios whose effect locator has no usable key for its table (the diff attribution needs one).

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.autogen_01.kit.check_effects GEN_RUN [...]
"""
import json
import sys
from pathlib import Path

from grounding.runs.autogen_01.kit.derive import effect_key

for run in sys.argv[1:]:
    for path in sorted(Path(run).glob("*/case.json")):
        case = json.loads(path.read_text())
        for ref in case["references"]:
            effect = ref.get("effect")
            if not effect:
                continue
            key = effect.get("key")
            proper = effect_key(case["domain"], effect["table"])
            if key != proper and (key or ["id"]) != proper:
                print(f"{path.parent.name} {ref['id']}: table {effect['table']} key {key} -> {proper}")
