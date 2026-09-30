"""Judge v2 (autogen_02/kit/judge2.py), unchanged, on Muse, for this study's runs; a judge call is refused once this
study's judge calls reach the cap ($3 billed; the lead, 2026-09-30).

    AUTOGEN_BACKEND=muse python grounding/runs/fact_coverage_02/launch.py grounding.runs.qwen_writer_01.judge \
        run --trials TRIALS.json --out grounding/runs/qwen_writer_01/runs/judged_RUN [--concurrency 4]

Any other judge2 command passes through (select, compare).
"""
from __future__ import annotations

import json
import os
from pathlib import Path

from grounding.runs.autogen_01.kit import agent
from grounding.runs.autogen_02.kit import judge2

HERE = Path(__file__).resolve().parent
CAP_BILLED = 3.0
_kit_run = agent.run


def judges_billed() -> float:
    total = 0.0
    for log in (HERE / "runs").glob("judged_*/calls.jsonl"):
        for line in log.read_text().splitlines():
            if line.strip():
                row = json.loads(line)
                if row.get("role") == "judge":
                    total += row.get("cost_usd_billed") or 0.0
    return total


def capped(call: agent.Call) -> dict:
    if call.role == "judge":
        spent = judges_billed()
        if spent >= CAP_BILLED - 0.05:
            raise RuntimeError(f"the judge's cap: ${spent:.2f} billed of ${CAP_BILLED:.2f}")
    return _kit_run(call)


if __name__ == "__main__":
    if os.environ.get("AUTOGEN_BACKEND") != "muse":
        raise SystemExit("set AUTOGEN_BACKEND=muse: judge v2 runs on Muse")
    agent.run = capped
    judge2.main()
