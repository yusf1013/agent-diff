"""The covers the automation starts from: the fact method's cover scenarios with one target.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.several_match_auto_01.population [--show]

Three sources, each in the kit's case format (a seed, a request, a reference with one expected target and its
near-miss claims):
- fact_coverage_02's hand-built covers (`cases_new`: BOX/CAL/LIN/SLK-21…), the phase-1 method's inputs;
- autogen_01's 49 accepted generated scenarios;
- autogen_02's Phase 4 accepted scenarios (written by Muse).
A cover qualifies when its reference expects exactly one record, and its request acts on that record.
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

from grounding.runs.autogen_02.kit import population as a2pop

HERE = Path(__file__).resolve().parent
FC2 = HERE.parent / "fact_coverage_02" / "cases_new"
HAND = ("BOX-21", "BOX-22", "BOX-23", "BOX-24", "CAL-21", "CAL-22", "CAL-23", "CAL-24",
        "LIN-21", "LIN-22", "LIN-23", "LIN-24", "LIN-25", "LIN-26", "SLK-21", "SLK-22", "SLK-23", "SLK-24")


def hand_covers() -> list[dict]:
    out = []
    for cid in HAND:
        path = next(FC2.glob(f"*/{cid}.json"))
        case = json.loads(path.read_text())
        case["_arm"] = "fact_coverage_02"
        out.append(case)
    return out


def covers() -> list[dict]:
    """Every qualifying cover, hand-built first, then generated."""
    out = []
    for case in hand_covers() + a2pop.scenarios() + a2pop.phase4_scenarios():
        refs = case.get("references") or []
        if len(refs) != 1 or len(refs[0].get("expected") or []) != 1:
            continue
        out.append(case)
    return out


def describe(case: dict) -> dict:
    ref = case["references"][0]
    return {"id": case["case_id"], "arm": case.get("_arm"), "domain": case["domain"], "prompt": case["prompt"],
            "target": ref["expected"][0], "table": (ref.get("effect") or {}).get("table"),
            "facts": sorted({c["requirement"] for c in ref.get("claims") or []}),
            "seed": {t: len(rows) for t, rows in case["seed"].items() if isinstance(rows, list)}}


def main(show: bool):
    cs = covers()
    print(len(cs), "covers;", dict(Counter(c["domain"] for c in cs)), dict(Counter(c.get("_arm") for c in cs)))
    if show:
        for c in cs:
            d = describe(c)
            print(f"{d['id']:28} {d['domain']:8} {d['table'] or '?':22} {d['prompt'][:110]}")
    (HERE / "population.json").write_text(json.dumps([describe(c) for c in cs], indent=1) + "\n")


if __name__ == "__main__":
    main("--show" in sys.argv)
