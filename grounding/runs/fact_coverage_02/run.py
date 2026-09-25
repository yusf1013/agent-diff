"""Run cases on Purdue Qwen with a fixed number of trials per case (trials are metadata, not budget).

    python -m grounding.runs.fact_coverage_02.run --out <new run dir> [--cases-dir DIR] [--cases ID ...] \
        [--trials 3] [--concurrency 6] [--prepare-only] [--retry-infrastructure] [--retry-timeouts] [--pairs tK/ID ...]

Each trial writes to <out>/t<k>/<case_id>/attempt-XX, exactly as the pilot runner does, so the pilot's analysis
tools read it unchanged. The trials of one case are queued next to each other, so they run together. The episode
itself (install, probes, Qwen loop, diff, cleanup) is the pilot's unchanged `execute`.
"""
from __future__ import annotations

import argparse
import asyncio
import copy
import json
import os
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from grounding.integrations.agentdiff import runtime
from grounding.integrations.agentdiff import smoke_runtime as smoke
from grounding.paths import REPO_ROOT
from grounding.runs.fact_coverage_01.pilot.run import execute, summarize

HERE = Path(__file__).resolve().parent


def load_cases(cases_dir: Path, selected):
    cases = {}
    for path in sorted(cases_dir.glob("*/*.json")):
        case = json.loads(path.read_text())
        cases[case["case_id"]] = (case, path)
    if selected:
        missing = set(selected) - set(cases)
        if missing:
            raise SystemExit(f"Unknown cases: {sorted(missing)}")
        return [cases[c] for c in selected]
    return list(cases.values())


def write_plan(out: Path, args, items, trial: int):
    plan = out / "plan.json"
    if plan.exists():
        return
    runtime.write(plan, {
        "started_utc": datetime.now(timezone.utc).isoformat(),
        "git_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True, cwd=REPO_ROOT).strip(),
        "model": args.model, "max_output_tokens": smoke.QWEN_MAX_OUTPUT_TOKENS,
        "turn_limit": smoke.TURN_LIMIT, "timeout_seconds": smoke.EPISODE_TIMEOUT_SECONDS,
        "trial": trial, "trials_per_case": args.trials, "prepare_only": args.prepare_only,
        "cases_dir": str(args.cases_dir.relative_to(REPO_ROOT)),
        "rate_limit_per_minute": os.getenv("PURDUE_RATE_LIMIT_PER_MINUTE"),
        "cases": {c["case_id"]: c["case_sha256"] for c, _ in items},
        "solver_context_excludes": ["references", "claims", "cards", "private", "coverage_claims"],
        "judgment": "manual review of trajectory, final answer and diff; no evaluator or native score"})


async def main_async(args):
    if not args.prepare_only and not os.getenv("GENAI_API_KEY"):
        raise SystemExit("GENAI_API_KEY must be set for Purdue runs")
    items = load_cases(args.cases_dir, args.cases)
    trials = [1] if args.prepare_only else list(range(1, args.trials + 1))
    trial_args = {}
    for k in trials:
        sub = copy.copy(args)
        sub.out = args.out / f"t{k}"
        sub.out.mkdir(parents=True, exist_ok=True)
        write_plan(sub.out, args, items, k)
        trial_args[k] = sub
    slot = asyncio.Semaphore(args.concurrency)
    pairs = set(args.pairs or [])  # "t2/LIN-05": only these trial/case pairs run (targeted retries)
    # Case-major order: the trials of one case start together.
    await asyncio.gather(*(execute(case, path, trial_args[k], slot) for case, path in items for k in trials
                           if not pairs or f"t{k}/{case['case_id']}" in pairs))
    for sub in trial_args.values():
        summarize(sub.out)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--cases-dir", type=Path, default=HERE / "cases")
    parser.add_argument("--cases", nargs="*")
    parser.add_argument("--trials", type=int, default=3)
    parser.add_argument("--prepare-only", action="store_true")
    parser.add_argument("--retry-infrastructure", action="store_true",
                        help="Retry attempts that failed for infrastructure reasons or were interrupted")
    parser.add_argument("--retry-timeouts", action="store_true",
                        help="Retry episodes that hit the 480 s limit")
    parser.add_argument("--pairs", nargs="*",
                        help="Run only these trial/case pairs, e.g. t2/LIN-05 (retry just the trials with no result)")
    parser.add_argument("--concurrency", type=int, default=6)
    parser.add_argument("--model", default="qwen3.8:27b")
    parser.add_argument("--database-url", default="postgresql://postgres@127.0.0.1:15432/agentdiff_campaign")
    parser.add_argument("--base-url", default="http://127.0.0.1:18001")
    args = parser.parse_args()
    args.out = args.out.resolve()
    args.cases_dir = args.cases_dir.resolve()
    asyncio.run(main_async(args))


if __name__ == "__main__":
    main()
