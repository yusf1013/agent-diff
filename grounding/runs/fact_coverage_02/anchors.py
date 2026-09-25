"""Anchor check: in a no-target probe, every entity the request names besides the target must still exist.

An anchor is a record the target points to and the request identifies, such as the group a label must belong to,
the team of an issue, the creator of a task or the channel of a message. In the reference query it is a joined node
reached through the target's foreign key (the join lands on the node's primary key) and constrained by filters.
If an anchor were missing, "there isn't one" would be true for the wrong reason (no Bug group at all, rather than
no Regression label in it), and a decoy could not count as a near miss.

    python -m grounding.runs.fact_coverage_02.anchors          # audit every probe and fact probe
"""
from __future__ import annotations

import json
from pathlib import Path

from grounding.runs.fact_coverage_01 import fdc
from grounding.runs.fact_coverage_01.pilot.variants import PRIMARY_KEYS

HERE = Path(__file__).resolve().parent


def anchors(node, domain, path=()):
    """Joined nodes that the parent row points to (join lands on the node's primary key) and that carry filters."""
    for edge in node.get("edges", []):
        join = edge.get("join") or {}
        child = edge["node"]
        pk = PRIMARY_KEYS.get(domain, {}).get(child["table"], "id")
        if join.get("child") == pk and (child.get("filters") or child.get("edges")):
            yield path + (edge.get("key"),), child
        yield from anchors(child, domain, path + (edge.get("key"),))


def missing_anchors(case):
    """Anchors of the no-target references that no row in the case's seed satisfies."""
    out = []
    for ref in case["references"]:
        if ref["expected"]:
            continue
        for path, node in anchors(ref["query"], case["domain"]):
            rows = case["seed"].get(node["table"], [])
            if not any(fdc.node_matches(case["seed"], node, r) for r in rows):
                out.append(f"{ref['id']}: no {node['table']} row for anchor {'/'.join(filter(None, path))}")
    return out


def main():
    checked, problems = 0, []
    for cases_dir in ("cases_new", "cases_pilot", "cases_factprobe"):
        for path in sorted((HERE / cases_dir).glob("*/*.json")):
            case = json.loads(path.read_text())
            if all(r["expected"] for r in case["references"]):
                continue  # target present: nothing was removed
            checked += 1
            problems += [f"{path.relative_to(HERE)}: {m}" for m in missing_anchors(case)]
    print(f"{checked} no-target cases checked; {len(problems)} missing anchors")
    for p in problems:
        print("  " + p)


if __name__ == "__main__":
    main()
