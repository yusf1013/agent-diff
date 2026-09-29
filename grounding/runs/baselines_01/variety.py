"""Variety of a baseline's tests: how many different deciding details its tests use, and how many tests only reuse
details that another test of the same service already uses.

    python3 grounding/runs/baselines_01/variety.py REVIEW.json [...]

A test's deciding details are the facts on which its near misses differ from the request (review.json, `near_misses`
→ `fact`), the detail that tells the right record apart from its look-alike. Fixed 2026-09-28 before the twins ran;
round 1's values: N0 32 distinct over 42 tests with a near miss, 20 of them only reusing; N1 46 over 43, 9 reusing.
"""
from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict


def variety(review: list) -> dict:
    by = defaultdict(list)
    for r in review:
        by[r["test"].split("-")[1]].append(frozenset(n["fact"] for n in r["near_misses"] if n.get("fact")))
    out = {"tests_with_a_near_miss": 0, "distinct_deciding_details": 0, "tests_only_reusing": 0, "per_domain": {}}
    for domain, sets in sorted(by.items()):
        count = Counter(f for s in sets for f in s)
        with_nm = sum(1 for s in sets if s)
        reusing = sum(1 for s in sets if s and all(count[f] > 1 for f in s))
        out["per_domain"][domain] = {"tests_with_a_near_miss": with_nm, "distinct": len(count), "only_reusing": reusing}
        out["tests_with_a_near_miss"] += with_nm
        out["distinct_deciding_details"] += len(count)
        out["tests_only_reusing"] += reusing
    return out


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(path, json.dumps(variety(json.load(open(path)))))
