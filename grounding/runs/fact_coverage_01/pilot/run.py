"""Prepare and run FDC pilot cases on Purdue Qwen (manual judgments follow separately).

    python -m grounding.runs.fact_coverage_01.pilot.run --out <new run dir> [--cases ...] [--prepare-only]

Slack cases use the existing Slack runtime (install, visibility certification,
episode, diff, evaluator bundle); Box/Calendar/Linear cases use custom_runtime.
Both use the same Qwen settings, shared rate limiter and episode loop as the
recorded Purdue comparison. Every attempt keeps its own directory; completed
attempts are never overwritten. --prepare-only installs and probes each case,
then removes its template (no model calls).
"""
from __future__ import annotations

import argparse
import asyncio
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import subprocess

from grounding.integrations.agentdiff import custom_runtime, runtime
from grounding.integrations.agentdiff import smoke_runtime as smoke
from grounding.paths import REPO_ROOT

HERE = Path(__file__).resolve().parent


def load_cases(selected):
    cases = {}
    for path in sorted((HERE / "cases").glob("*/*.json")):
        case = json.loads(path.read_text())
        cases[case["case_id"]] = (case, path)
    if selected:
        missing = set(selected) - set(cases)
        if missing:
            raise SystemExit(f"Unknown cases: {sorted(missing)}")
        return [cases[c] for c in selected]
    return list(cases.values())


def solver_case(case):
    """Slack runtime input: the existing case contract, without our private credit claims."""
    keep = ("case_id", "prompt", "acting_user_id", "seed", "cards", "task_spec", "private")
    return {k: case[k] for k in keep if k in case}


async def execute(case, source, args, slot):
    root = args.out / case["case_id"]
    previous = sorted(root.glob("attempt-*/execution_summary.json"))
    if previous:
        latest = json.loads(previous[-1].read_text())
        interrupted = latest["status"] in ("preflight", "solver_running")  # process was stopped mid-attempt
        queued_out = latest.get("termination") == "timeout" and args.retry_timeouts
        if not ((args.retry_infrastructure and (latest["status"] == "infrastructure_error" or interrupted))
                or queued_out):
            return latest
    attempt = root / f"attempt-{len(previous) + 1:02}"
    attempt.mkdir(parents=True, exist_ok=False)
    (attempt / "case.json").write_text(source.read_text())
    state = {"case_id": case["case_id"], "domain": case["domain"], "status": "preflight",
             "started_utc": datetime.now(timezone.utc).isoformat()}
    runtime.write(attempt / "execution_summary.json", state)
    prepared = None
    async with slot:
        try:
            if case["domain"] == "slack":
                from grounding.solver.slack import compare_purdue  # noqa: F401  (installs the Purdue client patch)
                scase = solver_case(case)
                prepared = await asyncio.to_thread(runtime.prepare, scase, attempt / "environment/preflight",
                                                   args.database_url, args.base_url)
                cleanup = lambda: runtime.cleanup(prepared, args.database_url)  # noqa: E731
            else:
                prepared = await asyncio.to_thread(custom_runtime.prepare_custom, case,
                                                   attempt / "environment/preflight", args.database_url, args.base_url)
                cleanup = lambda: smoke.cleanup_isolated_template(prepared, args.database_url)  # noqa: E731
            if args.prepare_only:
                await asyncio.to_thread(cleanup)
                prepared = None
                state["status"] = "prepared_only"
                return state
            state["status"] = "solver_running"
            runtime.write(attempt / "execution_summary.json", state)
            if case["domain"] == "slack":
                config = compare_purdue.MODELS["qwen36"]
                record = await runtime.run_prepared(
                    scase, prepared, attempt / "solver", args.database_url, model=args.model,
                    environment_out=attempt / "environment", evaluation_inputs=attempt / "evidence",
                    max_output_tokens=config["max_output_tokens"], thinking_budget=None, rates=config["rates"],
                    record_requests=True, prompt_caching_label="none_purdue",
                    cost_source_label=compare_purdue.COST_SOURCE)
                if "final" in record:
                    (attempt / "solver/final_response.md").write_text(record["final"] + "\n")
            else:
                record = await custom_runtime.run_custom(case, prepared, attempt, args.database_url, model=args.model)
            prepared = None  # both run paths clean up their template
            # A cut by the wall ceiling ("ceiling") is the infrastructure's and is retried; a cut by the agent's own
            # time budget ("timeout") is the agent's and is graded (agent_clock.py, since 2026-09-27).
            state.update(termination=record.get("termination"), error=record.get("error"),
                         usage=record.get("usage"), turns=len(record.get("steps", [])), clock=record.get("clock"),
                         status="infrastructure_error"
                         if record.get("termination") in ("error", "setup_error", "ceiling")
                         or record.get("diff") is None and "evaluation" not in record else "completed")
        except Exception as exc:
            state.update(status="infrastructure_error", error=f"{type(exc).__name__}: {exc}")
            if prepared:
                try:
                    await asyncio.to_thread(cleanup)
                except Exception as cleanup_exc:
                    state["cleanup_error"] = f"{type(cleanup_exc).__name__}: {cleanup_exc}"
        finally:
            state["ended_utc"] = datetime.now(timezone.utc).isoformat()
            runtime.write(attempt / "execution_summary.json", state)
            print(json.dumps({k: state.get(k) for k in ("case_id", "status", "termination", "turns", "error")}),
                  flush=True)
    return state


def summarize(out: Path):
    rows = []
    for path in sorted(out.glob("*/attempt-*/execution_summary.json")):
        s = json.loads(path.read_text())
        s["attempt_dir"] = str(path.parent.relative_to(out))
        rows.append(s)
    usage = {}
    for s in rows:
        for k, v in (s.get("usage") or {}).items():
            if isinstance(v, (int, float)):
                usage[k] = usage.get(k, 0) + v
    runtime.write(out / "usage_summary.json", {"attempts": rows, "usage_totals": usage,
                                                "cost_usd": 0.0, "cost_source": smoke.COST_SOURCE})


async def main_async(args):
    if not args.prepare_only and not os.getenv("GENAI_API_KEY"):
        raise SystemExit("GENAI_API_KEY must be set for Purdue runs")
    args.out.mkdir(parents=True, exist_ok=True)
    plan = args.out / "plan.json"
    items = load_cases(args.cases)
    if not plan.exists():
        runtime.write(plan, {"started_utc": datetime.now(timezone.utc).isoformat(),
                             "git_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True,
                                                                   cwd=REPO_ROOT).strip(),
                             "model": args.model, "max_output_tokens": smoke.QWEN_MAX_OUTPUT_TOKENS,
                             "model_note": "qwen3.6:27b (recorded comparison) is no longer served; qwen3.8:27b is the "
                                           "same-size successor listed by Purdue on 2026-09-23",
                             "turn_limit": smoke.TURN_LIMIT, "timeout_seconds": smoke.EPISODE_TIMEOUT_SECONDS,
                             "ceiling_seconds": smoke.EPISODE_CEILING_SECONDS, "clock": smoke.CLOCK_RULE,
                             "trials_per_case": 1, "prepare_only": args.prepare_only,
                             "cases": {c["case_id"]: c["case_sha256"] for c, _ in items},
                             "solver_context_excludes": ["references", "claims", "cards", "private", "coverage_claims"],
                             "judgment": "manual review of trajectory, final answer and diff; no evaluator or native score"})
    slot = asyncio.Semaphore(args.concurrency)
    await asyncio.gather(*(execute(c, p, args, slot) for c, p in items))
    summarize(args.out)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--cases", nargs="*")
    parser.add_argument("--prepare-only", action="store_true")
    parser.add_argument("--retry-infrastructure", action="store_true",
                        help="Retry attempts that failed for infrastructure reasons or were interrupted")
    parser.add_argument("--retry-timeouts", action="store_true",
                        help="Retry episodes cut by the 480 s budget. Since 2026-09-27 that budget is the agent's own "
                             "time (Purdue waiting excluded), so such a cut is normally graded, not retried; a cut by "
                             "the wall ceiling is an infrastructure error (--retry-infrastructure)")
    parser.add_argument("--concurrency", type=int, default=3)
    parser.add_argument("--model", default="qwen3.8:27b")
    parser.add_argument("--database-url", default="postgresql://postgres@127.0.0.1:15432/agentdiff_campaign")
    parser.add_argument("--base-url", default="http://127.0.0.1:18001")
    args = parser.parse_args()
    args.out = args.out.resolve()
    asyncio.run(main_async(args))


if __name__ == "__main__":
    main()
