"""The Muse judge's cost for the Sol round, from each verdict folder's calls.jsonl (autogen_01/kit/agent.py writes
one line per call: tokens, list-price and billed cost from Muse's model catalog; failed attempts included). The
session's cap is $10 billed; reports give the list price.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.sol_eval_01.kit.cost
"""
from __future__ import annotations

import json
from pathlib import Path

EVAL = Path(__file__).resolve().parents[1] / "eval"


def main():
    total = {"calls": 0, "failed": 0, "list": 0.0, "billed": 0.0, "input": 0, "cached": 0, "output": 0, "reasoning": 0}
    rows = {}
    for log in sorted(EVAL.glob("judged_*/calls.jsonl")):
        r = {k: 0 for k in total}
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
        rows[log.parent.name] = {k: round(v, 2) if isinstance(v, float) else v for k, v in r.items()}
        for k in total:
            total[k] += r[k]
    out = {"folders": rows, "total": {k: round(v, 2) if isinstance(v, float) else v for k, v in total.items()},
           "cap_billed_usd": 10}
    (EVAL / "judge_cost.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
