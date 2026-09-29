"""Development check: print a few covers' reference queries compactly (root filters and edges).

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.several_match_auto_01.inspect_query ID ...
"""
from __future__ import annotations

import json
import sys

from grounding.runs.several_match_auto_01.population import covers


def compact(node, depth=0):
    pad = "  " * depth
    out = [f"{pad}table={node.get('table')} filters=" +
           json.dumps([(f.get('field'), f.get('op'), f.get('value'), f.get('fact')) for f in node.get('filters') or []])]
    for e in node.get("edges") or []:
        out.append(f"{pad}  edge join={e.get('join')} closure={e.get('closure')} count={e.get('count')} fact={e.get('fact')}")
        out += compact(e.get("node") or {}, depth + 2)
    return out


def main(ids):
    for c in covers():
        if c["case_id"] in ids:
            print("==", c["case_id"], "|", c["prompt"])
            print("\n".join(compact(c["references"][0]["query"])))


if __name__ == "__main__":
    main(set(sys.argv[1:]))
