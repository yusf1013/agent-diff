"""Run cases through the toy harness with the pilot's own runner (unchanged), for the toy baseline of new cases.

    GENAI_API_KEY=... PURDUE_RATE_LIMIT_PER_MINUTE=20 \
    python -m grounding.runs.openclaw_transfer_01.toy_run --out runs/<new dir> --cases CAL-02R CAL-11R

Cases are found as in run.py (pilot cases, this folder's cases/, Slack suite). Keep the limiter budget at 20
so toy and OpenClaw runs share Purdue's real limit.
"""
from __future__ import annotations

import argparse
import asyncio
import os
from pathlib import Path

from grounding.runs.fact_coverage_01.pilot import run as pilot_run
from grounding.runs.openclaw_transfer_01.run import find_case


async def main_async(args) -> None:
    if not os.getenv("GENAI_API_KEY"):
        raise SystemExit("GENAI_API_KEY must be set")
    args.out.mkdir(parents=True, exist_ok=True)
    items = [find_case(c) for c in args.cases]
    slot = asyncio.Semaphore(args.concurrency)
    await asyncio.gather(*(pilot_run.execute(c, p, args, slot) for c, p in items), return_exceptions=True)
    pilot_run.summarize(args.out)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--cases", nargs="+", required=True)
    parser.add_argument("--concurrency", type=int, default=2)
    parser.add_argument("--model", default="qwen3.8:27b")
    parser.add_argument("--database-url", default="postgresql://postgres@127.0.0.1:15432/agentdiff_campaign")
    parser.add_argument("--base-url", default="http://127.0.0.1:18001")
    args = parser.parse_args()
    args.out = args.out.resolve()
    args.retry_infrastructure = args.retry_timeouts = args.prepare_only = False
    os.environ.setdefault("DATABASE_URL", args.database_url)
    asyncio.run(main_async(args))


if __name__ == "__main__":
    main()
