"""The Muse judge's cost for the Sol round, from each verdict folder's calls.jsonl (autogen_01/kit/agent.py writes
one line per call: tokens, list-price and billed cost from Muse's model catalog; failed attempts included). Reports
give the list price. `total` is the Muse-written half's four sets (its cap $10 billed; report_01 reads it),
`total_regen` the regenerated half's three (the lead's cap: $25 at list price), `total_all` both.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.sol_eval_01.kit.cost
"""
from __future__ import annotations

import json
from pathlib import Path

from grounding.runs.sol_eval_01.kit import sets

EVAL = Path(__file__).resolve().parents[1] / "eval"


KEYS = ("calls", "failed", "list", "billed", "input", "cached", "output", "reasoning")


def add(rows: dict, names: list[str]) -> dict:
    total = {k: 0 for k in KEYS}
    for name in names:
        for k in KEYS:
            total[k] += rows.get(f"judged_{name}", {}).get(k, 0)
    return {k: round(v, 2) if isinstance(v, float) else v for k, v in total.items()}


def main():
    rows = {}
    for log in sorted(EVAL.glob("judged_*/calls.jsonl")):
        r = {k: 0 for k in KEYS}
        for line in log.read_text().splitlines():
            c = json.loads(line)
            r["calls"] += 1
            r["failed"] += bool(c.get("failed"))
            r["list"] += c.get("cost_usd_list_price") or 0
            r["billed"] += c.get("cost_usd_billed") or 0
            r["input"] += (c.get("input_tokens") or 0) + (c.get("cache_read_input_tokens") or 0)
            r["cached"] += c.get("cache_read_input_tokens") or 0
            r["output"] += c.get("output_tokens") or 0
            r["reasoning"] += c.get("reasoning_tokens") or 0
        rows[log.parent.name] = r
    out = {"folders": {n: {k: round(v, 2) if isinstance(v, float) else v for k, v in r.items()} for n, r in rows.items()},
           "total": add(rows, sets.of_half("muse")), "cap_billed_usd": 10,
           "total_regen": add(rows, sets.of_half("regen")), "cap_regen_list_usd": 25,
           "total_all": add(rows, list(sets.SETS))}
    (EVAL / "judge_cost.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
