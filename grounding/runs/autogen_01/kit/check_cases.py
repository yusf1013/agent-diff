"""Static check of a generated suite's case files: every test's seed has no dangling foreign key.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.autogen_01.kit.check_cases RUN_DIR [...]
"""
import json
import sys
from pathlib import Path

from grounding.runs.autogen_01.kit import derive

bad = 0
for run in sys.argv[1:]:
    for path in sorted(Path(run).glob("cases/*/*.json")):
        case = json.loads(path.read_text())
        problems = derive.dangling(case)
        if problems:
            bad += 1
            print(path.name, problems[:3])
    print(run, "checked;", bad, "cases with dangling keys")
