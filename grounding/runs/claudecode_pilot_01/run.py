"""Run a cases folder through Claude Code (backend.py), k trials per test, as openclaw_eval_01's runner does.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.claudecode_pilot_01.run \
        --out grounding/runs/claudecode_pilot_01/runs/<new run> [--cases-dir DIR] [--cases ID ...] [--trials 3] \
        [--concurrency 6] [--retry-infrastructure] [--read ID ...] [--backend plan|selfhost] [--auth token-file|login]

The selection is openclaw_eval_01.run's, imported unchanged: the known defects (roadmap_01/known_defects.json,
`frozen_suite`) and the PI's rulings decide what runs; "keep until DATE" and "read before it runs" work the same.
Each trial writes <out>/t<k>/<case_id>/attempt-XX with case.json and execution_summary.json, and a plan.json and
usage_summary.json per trial, so judge v2's selection, the scoring, review.py and blind_sample.py read it unchanged.
Completed attempts are never redone; with --retry-infrastructure, attempts that ended in an infrastructure error are
run again. A timeout is the agent's failure and is not re-run.
"""
from __future__ import annotations

import argparse
import asyncio
import hashlib
import json
import os
import subprocess
from datetime import date, datetime, timezone
from pathlib import Path

from grounding.integrations.agentdiff.runtime import write
from grounding.integrations.openclaw import runtime as oc
from grounding.paths import REPO_ROOT
from grounding.runs.claudecode_pilot_01 import backend as cc
from grounding.runs.openclaw_eval_01.run import KNOWN_DEFECTS, SUITE, action_for, date_limit, defect_actions, git, select

HERE = Path(__file__).resolve().parent


def code_hashes() -> dict:
    files = [Path(cc.__file__), Path(__file__), cc.FAKECLOCK_SRC, Path(oc.__file__), oc.SHIM_DIR / "curl",
             *sorted(cc.SKILLS.rglob("*.md"))]
    return {str(f.relative_to(REPO_ROOT)): hashlib.sha256(f.read_bytes()).hexdigest() for f in files}


def write_plan(trial_out: Path, args, items, left_out: dict, trial: int) -> None:
    plan = trial_out / "plan.json"
    if plan.exists():
        return
    write(plan, {
        "started_utc": datetime.now(timezone.utc).isoformat(), "harness": "claude-code",
        "claude_code_version": subprocess.run([cc.CLAUDE_BIN, "--version"], capture_output=True, text=True).stdout.strip(),
        "git_commit": git("rev-parse", "HEAD"), "git_describe": git("describe", "--tags", "--always", "--dirty"),
        "code_sha256": code_hashes(), "backend": args.backend, "model": args.model or
        (cc.SELFHOST_MODEL if args.backend == "selfhost" else cc.MODEL), "effort": args.effort, "tools": cc.TOOLS,
        "auth": args.auth or cc.default_auth(args.backend),
        "isolation": "per-run CLAUDE_CONFIG_DIR and working directory; --strict-mcp-config with no servers; "
                     "--setting-sources project; ENABLE_CLAUDEAI_MCP_SERVERS=false; a clean environment",
        "timeout_seconds_per_turn": args.timeout, "follow_up": False, "prompt_prefix": oc.PREFIX,
        "trial": trial, "trials_per_case": args.trials, "concurrency": args.concurrency,
        "cases_dir": str(args.cases_dir.relative_to(REPO_ROOT)),
        "cases": {c["case_id"]: c.get("case_sha256") for c, _ in items}, "left_out": left_out,
        "known_defects_sha256": hashlib.sha256(KNOWN_DEFECTS.read_bytes()).hexdigest(),
        "solver_context_excludes": ["references", "claims", "cards", "private", "coverage_claims"],
        "judgment": "turn 1 graded from the state after turn 1 and its reply (judge v2)"})


async def execute(case: dict, source: Path, trial: int, args, slot: asyncio.Semaphore) -> dict | None:
    root = args.out / f"t{trial}" / case["case_id"]
    async with slot:
        previous = sorted(root.glob("attempt-*/execution_summary.json"))
        if previous:
            latest = json.loads(previous[-1].read_text())
            if not (args.retry_infrastructure and latest["status"] in ("infrastructure_error", "preflight",
                                                                       "solver_running")):
                return latest
        until = date_limit(action_for(case["case_id"], defect_actions()))
        if until and date.today() > until:
            line = {"case_id": case["case_id"], "trial": trial, "skipped": f"past {until}", "at": datetime.now().isoformat()}
            with open(args.out / "skipped.jsonl", "a") as handle:
                handle.write(json.dumps(line) + "\n")
            return None
        attempt = root / f"attempt-{len(previous) + 1:02}"
        attempt.mkdir(parents=True, exist_ok=False)
        (attempt / "case.json").write_text(source.read_text())
        summary = {"case_id": case["case_id"], "domain": case["domain"], "status": "preflight",
                   "harness": "claude-code", "backend": args.backend, "trial": trial,
                   "started_utc": datetime.now(timezone.utc).isoformat()}
        write(attempt / "execution_summary.json", summary)
        try:
            await asyncio.to_thread(cc.run_attempt, case, attempt, database_url=args.database_url,
                                    backend_url=args.base_url, timeout_s=args.timeout, followup=False,
                                    keep_state=args.keep_state, summary=summary, backend=args.backend,
                                    layout="judge", model=args.model, effort=args.effort, auth=args.auth)
        except Exception as exc:  # recorded; other tests keep running
            summary.update(status="infrastructure_error", error=f"{type(exc).__name__}: {exc}")
    summary["ended_utc"] = datetime.now(timezone.utc).isoformat()
    write(attempt / "execution_summary.json", summary)
    usage = summary.get("usage") or {}
    print(json.dumps({"case_id": case["case_id"], "trial": trial, "status": summary.get("status"),
                      "termination": summary.get("termination"), "turns": summary.get("turns"),
                      "seconds": (summary.get("turn_durations_s") or [None])[0],
                      "list_cost_usd": usage.get("list_cost_usd"), "error": summary.get("error")}), flush=True)
    return summary


def summarize(trial_out: Path) -> None:
    rows, totals = [], {}
    for path in sorted(trial_out.glob("*/attempt-*/execution_summary.json")):
        s = json.loads(path.read_text())
        s["attempt_dir"] = str(path.parent.relative_to(trial_out))
        rows.append(s)
        for k, v in (s.get("usage") or {}).items():
            if isinstance(v, (int, float)):
                totals[k] = round(totals.get(k, 0) + v, 4)
    write(trial_out / "usage_summary.json", {
        "attempts": rows, "usage_totals": totals, "cost_usd": 0.0,
        "cost_source": "runs on the Claude plan have no per-token charge (the plan's overage is off); "
                       "`list_cost_usd` is Claude Code's own estimate at list price, summed over attempts"})


async def main_async(args) -> None:
    items, left_out = select(args.cases_dir, args.cases, set(args.read or ()), date.today())
    trials = list(range(1, args.trials + 1))
    for k in trials:
        (args.out / f"t{k}").mkdir(parents=True, exist_ok=True)
        write_plan(args.out / f"t{k}", args, items, left_out, k)
    for case_id, reason in sorted(left_out.items()):
        print(json.dumps({"case_id": case_id, "left_out": reason}), flush=True)
    slot = asyncio.Semaphore(args.concurrency)
    jobs = [(case, path, k) for case, path in items for k in trials]  # case-major: a test's trials start together
    results = await asyncio.gather(*(execute(c, p, k, args, slot) for c, p, k in jobs), return_exceptions=True)
    for (case, _, k), result in zip(jobs, results):
        if isinstance(result, BaseException):
            print(json.dumps({"case_id": case["case_id"], "trial": k, "status": "runner_error",
                              "error": repr(result)[:300]}), flush=True)
    for k in trials:
        summarize(args.out / f"t{k}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--cases-dir", type=Path, default=SUITE)
    parser.add_argument("--cases", nargs="*")
    parser.add_argument("--trials", type=int, default=3)
    parser.add_argument("--concurrency", type=int, default=6)
    parser.add_argument("--timeout", type=int, default=cc.TIMEOUT_SECONDS, help="seconds per run")
    parser.add_argument("--read", nargs="*", help="'read before it runs' tests that have been read")
    parser.add_argument("--keep-state", action="store_true", help="keep each run directory (it holds no secret)")
    parser.add_argument("--retry-infrastructure", action="store_true")
    parser.add_argument("--database-url", default=os.getenv("DATABASE_URL",
                                                            "postgresql://postgres@127.0.0.1:15432/agentdiff_campaign"))
    parser.add_argument("--base-url", default="http://127.0.0.1:18001")
    parser.add_argument("--backend", choices=("plan", "selfhost"), default="plan",
                        help="plan: a Claude model on the PI's Claude plan; selfhost: the self-hosted Qwen")
    parser.add_argument("--model", help=f"default {cc.MODEL} (plan) or {cc.SELFHOST_MODEL} (selfhost)")
    parser.add_argument("--effort", default=cc.EFFORT)
    parser.add_argument("--auth", choices=("token-file", "login"),
                        help="plan runs: a setup-token file (the default when it exists) or the login's access token")
    args = parser.parse_args()
    if args.concurrency > 12:
        raise SystemExit("keep at most 12 Claude Code runs in flight on the plan")
    if args.backend == "selfhost" and args.concurrency > 1:
        raise SystemExit("the self-host is reached directly (no shared limiter): concurrency 1")
    args.out = args.out.resolve()
    args.cases_dir = args.cases_dir.resolve()
    os.environ.setdefault("DATABASE_URL", args.database_url)  # backend seed modules read it at import time
    asyncio.run(main_async(args))


if __name__ == "__main__":
    main()
