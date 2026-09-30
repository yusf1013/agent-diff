"""Grading an arm's run: judge v2's trial list, with each test's form from the review, and the scores.

    L="python grounding/runs/fact_coverage_02/launch.py"
    $L grounding.runs.baselines_02.grade trials RUN_DIR REVIEW.json > TRIALS.json
    AUTOGEN_BACKEND=muse $L grounding.runs.autogen_02.kit.judge2 run --trials TRIALS.json --out JUDGED_DIR
    $L grounding.runs.baselines_02.grade score RUN_DIR REVIEW.json JUDGED_DIR [--assertions A.json] > SCORE.json

- **Every trial is judged** (the latest attempt of each), not only the mechanically unclear ones: the arms are small
  (at most 144 trials each), and judge v2 costs about $0.002 billed per verdict.
- **The form** judge v2 is told: a presupposing request gets judge2's absence-twin wording, an underspecified one its
  underspecified wording; the others get judge2's default from the answer key (a target present: "cover"; no
  target: the no-target wording).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from grounding.runs.autogen_02.kit import judge2

FORM_WORDS = {"absence_presupposed": judge2.FORMS["AT-"], "underspecified": judge2.FORMS["U-"]}


def review_by_test(path: Path) -> dict:
    return {r["test"]: r for r in json.loads(path.read_text())}


def trials(run_dir: Path, review: dict) -> list[dict]:
    items = judge2.select([run_dir])
    for item in items:
        rec = review[item["case_id"]]
        if rec["form"] in FORM_WORDS:
            item["form"] = FORM_WORDS[rec["form"]]
    return items


def main():
    cmd, run_dir, review = sys.argv[1], Path(sys.argv[2]).resolve(), review_by_test(Path(sys.argv[3]))
    if cmd == "trials":
        print(json.dumps(trials(run_dir, review), indent=1))


if __name__ == "__main__":
    main()
