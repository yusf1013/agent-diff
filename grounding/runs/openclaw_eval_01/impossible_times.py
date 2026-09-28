"""Seed records whose creation time is later than their last-modified time, which the real services never produce.
Found on 2026-09-27 in the blind sample: OpenClaw's Qwen called one such near miss "likely an intentionally planted
trap in the test" and remarked on another. Reads the frozen suite; no model calls.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.openclaw_eval_01.impossible_times

Writes impossible_times.json beside this file: per scenario, the records (and whether each is the target or a near
miss, with its fact) where created_at > modified_at (Box) or created_at > updated_at (the other services).
"""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAIRS = (("created_at", "modified_at"), ("created_at", "updated_at"))


def main():
    found = defaultdict(dict)
    tests = defaultdict(set)
    for path in sorted((HERE / "suite" / "cases").glob("*/*.json")):
        case = json.loads(path.read_text())
        claims = {str(c["witness"]): c["requirement"] for r in case["references"] for c in r["claims"]}
        targets = {str(x) for r in case["references"] for x in r["expected"]}
        sid = case.get("scenario") or case["case_id"]
        for table, rows in case["seed"].items():
            for row in rows if isinstance(rows, list) else []:
                if not isinstance(row, dict):
                    continue
                for created, modified in PAIRS:
                    a, b = row.get(created), row.get(modified)
                    if isinstance(a, str) and isinstance(b, str) and a[:19] > b[:19]:
                        rid = str(row.get("id"))
                        role = "target" if rid in targets else f"near miss ({claims[rid]})" if rid in claims else "other"
                        found[table + "/" + rid].setdefault("where", set()).add(path.stem)
                        found[table + "/" + rid].update(table=table, id=rid, created=a, modified=b)
                        found[table + "/" + rid].setdefault("roles", set()).add(role)
                        tests[path.stem].add(rid)
    rows = [{**{k: v for k, v in r.items() if k not in ("where", "roles")}, "roles": sorted(r["roles"]),
             "tests": sorted(r["where"])} for r in found.values()]
    doc = {"_about": __doc__.split("\n\n")[0], "records": len(rows), "tests": len(tests),
           "records_by_role": {role: sum(role in r["roles"] for r in rows)
                               for role in sorted({x for r in rows for x in r["roles"]})}, "rows": rows}
    (HERE / "impossible_times.json").write_text(json.dumps(doc, indent=1) + "\n")
    print(json.dumps({k: v for k, v in doc.items() if k != "rows"}, indent=1))


if __name__ == "__main__":
    main()
