"""Development check: clone a cover's target once and show which of the query's conditions the copy fails.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.several_match_auto_01.debug_clone ID
"""
from __future__ import annotations

import copy
import json
import sys

from grounding.runs.fact_coverage_01 import fdc
from grounding.runs.several_match_auto_01 import seedkit
from grounding.runs.several_match_auto_01.population import covers


def main(cid):
    case = copy.deepcopy(next(c for c in covers() if c["case_id"] == cid))
    ref = case["references"][0]
    q, key = ref["query"], str(ref["expected"][0])
    deps = seedkit.dependents(case["seed"], case["domain"], q["table"], key)
    print("pk:", seedkit.pk(case["domain"], q["table"]), "dependents:", [(t, cols) for t, _, cols in deps])
    for t, _, _ in deps:
        print("  pk of", t, seedkit.pk(case["domain"], t))
    nk = seedkit.clone(case["seed"], case["domain"], q["table"], key, {},
                       new_key=None if q["table"] != "messages" else key[:-1] + "9")
    row = seedkit.find_row(case, q["table"], nk)
    print("copy key:", nk, "selected:", fdc.evaluate(case["seed"], q))
    for f in q.get("filters") or []:
        print("  filter", f["field"], f["op"], f.get("value"), "->", fdc.compare(fdc.get_field(row, f["field"]),
                                                                              f["op"], f.get("value")))
    for e in q.get("edges") or []:
        kids = fdc._joined(case["seed"], q["table"], row, e)
        print("  edge", e.get("join"), "joined rows:", len(kids),
              "matching:", sum(1 for k in kids if fdc.node_matches(case["seed"], e["node"], k)))
        for t in (case["seed"].get(e["node"]["table"]) or [])[-3:]:
            print("     tail row:", json.dumps(t, default=str)[:200])


if __name__ == "__main__":
    main(sys.argv[1])
