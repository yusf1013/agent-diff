"""Print every failing or unclear trial of a scored generated run with the judge's verdict, for manual reading.

    python3 -m grounding.runs.autogen_01.kit.show_failures SCORE.json
"""
import json
import sys

from grounding.runs.autogen_01.kit.judge import COLLAPSE

score = json.loads(open(sys.argv[1]).read())
for t in score["tests"]:
    shown = [(k, r) for k, r in sorted(t["trials"].items())
             if COLLAPSE.get(r["outcome"]) in ("fail", "void") or r["outcome"] in ("incomplete", "false_absence")]
    if not shown:
        continue
    print(f"### {t['case_id']} ({t.get('form')}, {t.get('fact')}, {t.get('family')}) exposed={t['exposed']}")
    for k, r in shown:
        judged = "judge" if r.get("judged") else "mechanical"
        print(f"  {k} {r['outcome']} {r['exposed']} mech={r.get('mechanism')} [{judged}] {str(r.get('note'))[:420]}")
