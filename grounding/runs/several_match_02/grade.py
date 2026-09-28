"""Grade several_match_02 runs with several_match_01's grader (set against targets, per placement class).

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.several_match_02.grade RUN_DIR

Reads this study's placements.json and scenarios/, and writes grades-<run name>.json here.
"""
from __future__ import annotations

import sys
from pathlib import Path

from grounding.runs.several_match_01 import grade as base

HERE = Path(__file__).resolve().parent

def labels_by_id(case, ids):
    """Match records by id only: names such as event titles are shared by targets and near misses (cycle 4)."""
    return {i: [f'"{i}"', f"'{i}'", f"={i}"] for i in ids}


if __name__ == "__main__":
    run = Path(sys.argv[1])
    base.HERE = HERE
    base.labels = labels_by_id
    base.main(run)
    (HERE / "grades.json").rename(HERE / f"grades-{run.name}.json")
