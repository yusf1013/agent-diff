"""Collect the three services' manual verdicts into review.jsonl and print the funnel.
    python -m grounding.runs.related_work_01.p1.review"""
import json
from collections import Counter
from pathlib import Path

from grounding.runs.related_work_01.p1 import review_box, review_linear, review_slack

HERE = Path(__file__).parent


def main():
    candidates = [json.loads(l) for l in (HERE / "candidates.jsonl").read_text().splitlines()]
    rows = review_slack.verdicts(candidates) + review_box.verdicts(candidates) + review_linear.verdicts(candidates)
    reviewed = {r["variant"] for r in rows}
    missing = [c["variant"] for c in candidates if c["status"] == "review" and c["variant"] not in reviewed]
    assert not missing, missing
    (HERE / "review.jsonl").write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))
    by = {r["variant"]: r for r in rows}
    funnel = Counter()
    for c in candidates:
        status = c["status"] if c["status"] != "review" else "review:" + by[c["variant"]]["verdict"]
        funnel[(c["service"], c["mode"], status)] += 1
    for k in sorted(funnel):
        print(k, funnel[k])
    totals = Counter((c["mode"], (by[c["variant"]]["verdict"] if c["variant"] in by else c["status"])) for c in candidates)
    print()
    for k in sorted(totals):
        print(k, totals[k])


if __name__ == "__main__":
    main()
