"""Every built case against the replica schema's unique keys (seedkit.unique_violations).

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.several_match_auto_01.unique_check

Added after five first-build easy cases failed to install in runs/p3 (a copied channel took a name already in the
team; a Linear copy took identifier WEB-1 in a seed whose issues have no number; channel copies carried their
messages with the same message_id). build.py now checks this before writing a case; this script checks the cases
already written. Prints the cases that break a key.
"""
from __future__ import annotations

import json
from pathlib import Path

from grounding.runs.several_match_auto_01 import seedkit

HERE = Path(__file__).resolve().parent


def main():
    bad = 0
    paths = sorted((HERE / "cases").glob("*/SMA-*.json"))
    for p in paths:
        case = json.loads(p.read_text())
        v = seedkit.unique_violations(case["seed"], case["domain"])
        if v:
            bad += 1
            print(p.stem, v[:2])
    print(f"{bad} of {len(paths)} cases break a unique key")


if __name__ == "__main__":
    main()
