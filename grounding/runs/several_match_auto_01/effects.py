"""The change made to the targets in the trials the judge passes, per cover, beside the request.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.several_match_auto_01.effects

grade.py decides which records were acted on (a row of the effect table changed, keyed as the effect says); it does
not look at the value written. A trial that sets High where the request says Urgent, or adds the wrong tag, would
pass. This lists, for every passed trial on a valid test, the values written to the effect table (updated columns
other than the replicas' bookkeeping, and inserted rows' fields), grouped by cover, so every pass can be checked
against its request. Writes effects.json; my reading is recorded in review_verdicts.py (VALUES).
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

from grounding.runs.several_match_auto_01.side_effects import NOISE_COLS

HERE = Path(__file__).resolve().parent
INSERT_SKIP = {"id", "created_at", "updated_at", "createdAt", "updatedAt", "__table__", "etag"}
BOOKKEEPING = NOISE_COLS - {"tags"}  # side_effects.py drops tags outside the target table; here they are the value


def main():
    grades = json.loads((HERE / "grades.json").read_text())
    review = json.loads((HERE / "review.json").read_text())
    by_cover = defaultdict(lambda: {"request": "", "trials": 0, "values": Counter()})
    for t in grades["trials"]:
        if (review.get(t["trial"]) or {}).get("sample") != "pass":
            continue
        tk, cid = t["trial"].split("/")
        att = sorted((HERE / "runs" / t["run"] / tk / cid).glob("attempt-*"))[-1]
        case = json.loads((att / "case.json").read_text())
        effect = case["references"][0]["effect"]
        diff = (json.loads((att / "environment/diff_run.json").read_text()) or {}).get("diff") or {}
        entry = by_cover[t["cover"]]
        entry["request"] = case["prompt"]
        entry["trials"] += 1
        for kind in effect.get("changes") or ["insert", "update", "delete"]:
            for row in diff.get(kind + "s") or []:
                if row.get("__table__") != effect["table"]:
                    continue
                if kind == "update":
                    a, b = row.get("after") or {}, row.get("before") or {}
                    for c in a:
                        if c not in BOOKKEEPING and a.get(c) != b.get(c):
                            entry["values"][f"{c} -> {json.dumps(a.get(c), default=str)[:80]}"] += 1
                elif kind == "insert":
                    a = row.get("after") or row
                    fields = {c: v for c, v in a.items() if c not in INSERT_SKIP and not str(c).endswith("_id")
                              and v not in (None, "", [], {})}
                    entry["values"][f"insert {json.dumps(fields, default=str)[:120]}"] += 1
                else:
                    entry["values"]["delete"] += 1
    out = {k: {"request": v["request"], "passed trials": v["trials"], "values written": dict(v["values"])}
           for k, v in sorted(by_cover.items())}
    (HERE / "effects.json").write_text(json.dumps(out, indent=1) + "\n")
    for k, v in out.items():
        print(f"{k} ({v['passed trials']} passed): {v['request'][:150]}")
        for val, n in v["values written"].items():
            print(f"    {n:3}  {val}")


if __name__ == "__main__":
    main()
