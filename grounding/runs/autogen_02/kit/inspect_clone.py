"""Print, per exemplar scenario, the target row of the root table, its key, the fields the request's query uses, and
the rows that point at the target: an aid for choosing a clone's changes by hand. It builds nothing.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.autogen_02.kit.inspect_clone [SCENARIO ...]
"""
import json
import sys

from grounding.runs.autogen_01.kit.derive import _foreign_keys, effect_key
from grounding.runs.autogen_02.phase1_build import exemplars


def used_fields(query):
    out = set(f["field"] for f in query.get("filters", []))
    for e in query.get("edges", []):
        if e.get("join"):
            out.add(e["join"].get("parent"))
    return out


def main():
    only = set(sys.argv[1:])
    for case in exemplars():
        if only and case["case_id"] not in only:
            continue
        ref = case["references"][0]
        table = ref["query"]["table"]
        pk = effect_key(case["domain"], table)
        target = str(ref["expected"][0])
        row = next((r for r in case["seed"][table] if str(r.get(pk[0])) == target), None)
        print(f"\n## {case['case_id']}: {case['prompt']}")
        print(f"   root {table}, key {pk}, uses {sorted(used_fields(ref['query']))}")
        print(f"   target: {json.dumps(row, ensure_ascii=False)[:600]}")
        for child, col, ref_table, ref_col in _foreign_keys(case["domain"]):
            if ref_table == table and child in case["seed"] and child != table:
                n = sum(1 for r in case["seed"][child] if str(r.get(col)) == target)
                if n:
                    print(f"   points at it: {n} {child} row(s) via {col}; {child} key {effect_key(case['domain'], child)}")


if __name__ == "__main__":
    main()
