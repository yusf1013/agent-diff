"""Run the fact-coverage pilot cases (and the manual Slack suite) through the real OpenClaw agent.

    python -m grounding.runs.openclaw_transfer_01.run --out <new run dir> --cases BOX-01 CAL-01 [--concurrency 4]

Cases are read unchanged from grounding/runs/fact_coverage_01/pilot/cases/ (Box, Calendar, Linear)
and grounding/runs/manual_exemplars_01/cases/ (Slack). Each attempt gets its own directory;
completed attempts are never overwritten. The local Purdue proxy must be running
(python -m grounding.integrations.openclaw.purdue_proxy).
"""
from __future__ import annotations

import argparse
import asyncio
import hashlib
import json
import os
import subprocess
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

from grounding.integrations.agentdiff.runtime import write
from grounding.integrations.openclaw import runtime as oc
from grounding.integrations.openclaw.purdue_proxy import DEFAULT_PORT
from grounding.paths import REPO_ROOT

HERE = Path(__file__).resolve().parent
PILOT_CASES = REPO_ROOT / "grounding/runs/fact_coverage_01/pilot/cases"
SLACK_CASES = REPO_ROOT / "grounding/runs/manual_exemplars_01/cases"


def find_case(case_id: str) -> tuple[dict, Path]:
    for path in list(PILOT_CASES.glob(f"*/{case_id}.json")) + list((HERE / "cases").glob(f"*/{case_id}.json")):
        return json.loads(path.read_text()), path
    path = SLACK_CASES / f"{case_id}.json"
    if path.exists():
        case = json.loads(path.read_text())
        case.setdefault("domain", "slack")
        return case, path
    raise SystemExit(f"Unknown case: {case_id}")


async def execute(case: dict, source: Path, args, slot: asyncio.Semaphore) -> dict:
    root = args.out / case["case_id"]
    async with slot:  # attempts are created only when a lane is free
        previous = sorted(root.glob("attempt-*/execution_summary.json"))
        if previous:
            latest = json.loads(previous[-1].read_text())
            retry = args.retry_infrastructure and latest["status"] in ("infrastructure_error", "preflight", "solver_running")
            if not retry:
                return latest
        attempt = root / f"attempt-{len(previous) + 1:02}"
        attempt.mkdir(parents=True, exist_ok=False)
        (attempt / "case.json").write_text(source.read_text() if case["domain"] != "slack" else json.dumps(case, indent=1))
        summary = {"case_id": case["case_id"], "domain": case["domain"], "status": "preflight", "harness": "openclaw",
                   "started_utc": datetime.now(timezone.utc).isoformat()}
        write(attempt / "execution_summary.json", summary)
        try:
            await asyncio.to_thread(oc.run_attempt, case, attempt, database_url=args.database_url,
                                    backend_url=args.base_url, timeout_s=args.timeout, followup=not args.no_followup,
                                    keep_state=args.keep_state, summary=summary, variant=args.variant)
        except Exception as exc:  # recorded; other cases keep running
            summary.update(status="infrastructure_error", error=f"{type(exc).__name__}: {exc}")
    summary["ended_utc"] = datetime.now(timezone.utc).isoformat()
    write(attempt / "execution_summary.json", summary)
    print(json.dumps({k: summary.get(k) for k in ("case_id", "status", "termination", "turns", "error")}
                     | {"followup": (summary.get("followup") or {}).get("sent")}), flush=True)
    return summary


def summarize(out: Path) -> None:
    rows, totals = [], {}
    for path in sorted(out.glob("*/attempt-*/execution_summary.json")):
        s = json.loads(path.read_text())
        s["attempt_dir"] = str(path.parent.relative_to(out))
        rows.append(s)
        for k, v in (s.get("usage") or {}).items():
            if isinstance(v, (int, float)):
                totals[k] = round(totals.get(k, 0) + v, 1)
    write(out / "usage_summary.json", {"attempts": rows, "usage_totals": totals, "cost_usd": 0.0,
                                       "cost_source": "Purdue GenAI Studio has no per-token charge to this account; "
                                                      "tokens are provider-reported through the local proxy"})


def code_hashes() -> dict:
    """sha256 of the harness code this run used (the runner code may be ahead of git_commit)."""
    files = [Path(oc.__file__), Path(__file__), Path(oc.__file__).with_name("purdue_proxy.py"),
             *sorted(Path(oc.__file__).with_name("skills").rglob("*.md"))]
    return {str(f.relative_to(REPO_ROOT)): hashlib.sha256(f.read_bytes()).hexdigest() for f in files}


async def main_async(args) -> None:
    try:
        urllib.request.urlopen(f"http://127.0.0.1:{DEFAULT_PORT}/v1/models", timeout=30)
    except Exception as exc:
        raise SystemExit(f"Purdue proxy not reachable on port {DEFAULT_PORT}: {exc}")
    args.out.mkdir(parents=True, exist_ok=True)
    items = [find_case(c) for c in args.cases]
    plan = args.out / "plan.json"
    if not plan.exists():
        write(plan, {"started_utc": datetime.now(timezone.utc).isoformat(), "harness": "openclaw",
                     "git_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True, cwd=REPO_ROOT).strip(),
                     "agent": oc.AGENT_ID, "timeout_seconds_per_turn": args.timeout, "follow_up": not args.no_followup,
                     "workspace_variant": args.variant, "code_sha256": code_hashes(),
                     "prompt_prefix": oc.PREFIX, "cases": {c["case_id"]: c.get("case_sha256") for c, _ in items},
                     "judgment": "turn 1 graded from state after turn 1 and its reply; follow-up graded separately"})
    slot = asyncio.Semaphore(args.concurrency)
    results = await asyncio.gather(*(execute(c, p, args, slot) for c, p in items), return_exceptions=True)
    for (case, _), result in zip(items, results):
        if isinstance(result, BaseException):
            print(json.dumps({"case_id": case["case_id"], "status": "runner_error", "error": repr(result)[:300]}), flush=True)
    summarize(args.out)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--cases", nargs="+", required=True)
    parser.add_argument("--concurrency", type=int, default=2)
    parser.add_argument("--timeout", type=int, default=oc.TIMEOUT_SECONDS)
    parser.add_argument("--no-followup", action="store_true")
    parser.add_argument("--keep-state", action="store_true", help="keep each OpenClaw state directory")
    parser.add_argument("--variant", choices=sorted(oc.VARIANTS), help="workspace variant (default: unchanged)")
    parser.add_argument("--retry-infrastructure", action="store_true")
    parser.add_argument("--database-url", default="postgresql://postgres@127.0.0.1:15432/agentdiff_campaign")
    parser.add_argument("--base-url", default="http://127.0.0.1:18001")
    args = parser.parse_args()
    args.out = args.out.resolve()
    os.environ.setdefault("DATABASE_URL", args.database_url)  # backend seed modules read it at import time
    asyncio.run(main_async(args))


if __name__ == "__main__":
    main()
