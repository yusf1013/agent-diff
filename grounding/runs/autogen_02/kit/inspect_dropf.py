"""Print, per exemplar scenario, what a drop-F variant of each fact would do: the request, the query's conditions,
and for each fact the condition keys it drops, the facts sharing them, the freed near misses and the remaining
condition count. An aid for writing the Phase 1 requests by hand; it builds nothing.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.autogen_02.kit.inspect_dropf [SCENARIO ...]
"""
import sys

from grounding.runs.autogen_02.kit import policy
from grounding.runs.autogen_02.phase1_build import exemplars


def conditions(query, depth=0):
    for f in query.get("filters", []):
        yield depth, f"filter {f['key']}: {query['table']}.{f['field']} {f['op']} {f.get('value')!r} [{f.get('fact')}]"
    for e in query.get("edges", []):
        yield depth, f"edge {e.get('key')}: {query['table']} -> {e['node']['table']} [{e.get('fact')}]"
        yield from conditions(e["node"], depth + 1)


def main():
    only = set(sys.argv[1:])
    for case in exemplars():
        if only and case["case_id"] not in only:
            continue
        ref = case["references"][0]
        print(f"\n## {case['case_id']}: {case['prompt']}")
        for depth, line in conditions(ref["query"]):
            print("   " + "  " * depth + line)
        for fact in policy.facts_of(case):
            _, meta = policy.drop_f(case, fact, None)
            freed = [f"{c['witness']} ({c.get('family')}): {c.get('explanation')}" for c in ref["claims"]
                     if c["requirement"] in meta["dropped_facts"]]
            print(f" - {fact}: drop {meta['dropped_keys']} (facts {meta['dropped_facts']}); matches {meta['matches']}; "
                  f"conditions left {meta['conditions_left']}; problems {meta['problems'][:2]}")
            for f in freed:
                print(f"     freed: {f}")


if __name__ == "__main__":
    main()
