"""Print the failing, void or unclear trials of a scored run that eval/judge_review.json does not cover yet.

    python3 -m grounding.runs.autogen_01.kit.show_unreviewed RUN   (for example solve_arm_r)
"""
import json
import sys
from pathlib import Path

from grounding.runs.autogen_01.kit.judge import COLLAPSE

STUDY = Path(__file__).resolve().parents[1]
run = sys.argv[1]
score = json.loads((STUDY / "runs" / f"{run}.score.json").read_text())
review = json.loads((STUDY / "eval" / "judge_review.json").read_text())
for t in score["tests"]:
    shown = [(k, r) for k, r in sorted(t["trials"].items())
             if (COLLAPSE.get(r["outcome"]) in ("fail", "void") or r["outcome"] in ("incomplete", "false_absence"))
             and f"{run}/{k}/{t['case_id']}" not in review]
    if not shown:
        continue
    print(f"### {t['case_id']} ({t.get('form')}, {t.get('fact')}, {t.get('family')}) exposed={t['exposed']}")
    for k, r in shown:
        judged = "judge" if r.get("judged") else "mechanical"
        print(f"  {k} {r['outcome']} {r['exposed']} mech={r.get('mechanism')} [{judged}] {str(r.get('note'))[:700]}")
