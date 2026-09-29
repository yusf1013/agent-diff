"""Development check: do the covers' references carry a real selection query that fdc.check_reference can use to
validate clones and traps? Prints, per cover, the query's shape and fdc's verdict on the untouched seed.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.several_match_auto_01.inspect_refs
"""
from __future__ import annotations

import json

from grounding.runs.fact_coverage_01 import fdc
from grounding.runs.several_match_auto_01.population import covers


def main():
    for case in covers():
        ref = case["references"][0]
        q = ref.get("query") or {}
        _, errors = fdc.check_reference(case["seed"], ref)
        print(f"{case['case_id']:14} {case['domain']:8} query keys={sorted(q)[:6]} "
              f"expected={ref['expected']} fdc={'ok' if not errors else errors[:1]}")
    c = covers()[0]
    print(json.dumps(c["references"][0].get("query"), indent=1)[:1500])


if __name__ == "__main__":
    main()
