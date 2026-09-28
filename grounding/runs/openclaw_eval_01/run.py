"""Run the frozen suite (or another cases folder) through OpenClaw on the self-hosted Qwen, k trials per test.

    SOLVER_BACKEND=selfhost python grounding/runs/fact_coverage_02/launch.py grounding.runs.openclaw_eval_01.run \
        --out grounding/runs/openclaw_eval_01/runs/<new run> [--cases-dir DIR] [--cases ID ...] [--trials 3] \
        [--concurrency 8] [--retry-infrastructure] [--read ID ...]

Start the self-host proxy first, through the launcher (it holds the key and the shared rate limiter):

    SOLVER_BACKEND=selfhost python grounding/runs/fact_coverage_02/launch.py \
        grounding.integrations.openclaw.purdue_proxy --backend selfhost

Each trial writes <out>/t<k>/<case_id>/attempt-XX, as fact_coverage_02's runner does, so judge v2's selection, Phase
4's scoring, review.py and blind_sample.py read it unchanged. An attempt is openclaw_transfer_01's
(integrations/openclaw/runtime.py) with:
- **the self-hosted Qwen** at its real limits (131,072-token context, 8,192 output tokens), through the proxy;
- **the judge's layout** (raw OpenClaw files under solver/openclaw/, steps in the toy record format);
- **no "Yes, go ahead." follow-up:** the judge grades turn 1.

Known defects (roadmap_01/known_defects.json, `frozen_suite`) and the PI's near-miss rulings (rulings.py) are
applied to the selected tests:
- "leave out", "dropped by the derivation", and a test the rulings leave out never run;
- "keep until DATE" runs only up to that local date, checked again as each attempt starts;
- "read before it runs" runs only when listed with --read.

The trials of one test start together; tests with a date limit go first. Completed attempts are never redone.
With --retry-infrastructure, attempts that ended in an infrastructure error are run again.
"""
from __future__ import annotations

import argparse
import asyncio
import hashlib
import json
import os
import re
import subprocess
import urllib.request
from datetime import date, datetime, timezone
from pathlib import Path

from grounding.integrations.agentdiff.runtime import write
from grounding.integrations.openclaw import runtime as oc
from grounding.integrations.openclaw.purdue_proxy import SELFHOST_PORT
from grounding.paths import REPO_ROOT
from grounding.runs.openclaw_eval_01 import rulings

HERE = Path(__file__).resolve().parent
SUITE = HERE / "suite" / "cases"
KNOWN_DEFECTS = HERE.parent / "roadmap_01" / "known_defects.json"
BACKEND = "selfhost"
UNTIL = re.compile(r"keep until (\d{4}-\d{2}-\d{2})")


def scenario_of(case_id: str) -> str:
    """P-G4-LIN-02-I11 -> G4-LIN-02; FP-AR-SLK-22-I11-I12 -> AR-SLK-22; AT-/U-/UC- variants alike."""
    stem = re.sub(r"^(AT|FP|P|UC|U|H)-", "", case_id)
    m = re.match(r"((?:[A-Z]+\d?-)?[A-Z]{3}-\d+)", stem)
    return m.group(1) if m else stem


def defect_actions() -> dict[str, str]:
    doc = json.loads(KNOWN_DEFECTS.read_text())
    return {e["id"]: e["frozen_suite"] for part in ("curated", "from_the_witness_check") for e in doc[part]}


def action_for(case_id: str, actions: dict[str, str]) -> str:
    return actions.get(case_id) or actions.get(scenario_of(case_id)) or "keep"


def date_limit(action: str) -> date | None:
    m = UNTIL.match(action)
    return date.fromisoformat(m.group(1)) if m else None


def select(cases_dir: Path, wanted: list[str] | None, read: set[str], today: date):
    """(tests to run as (case, path), left out as {case_id: reason}); date-limited tests first."""
    cases = {}
    for path in sorted(cases_dir.glob("*/*.json")):
        case = json.loads(path.read_text())
        cases[case["case_id"]] = (case, path)
    if wanted:
        missing = set(wanted) - set(cases)
        if missing:
            raise SystemExit(f"Unknown cases: {sorted(missing)}")
        cases = {c: cases[c] for c in wanted}
    actions = defect_actions()
    run, left_out = [], {}
    for case_id, item in cases.items():
        action = action_for(case_id, actions)
        until = date_limit(action)
        ruled = rulings.test_exclusion(item[0])
        if action.startswith(("leave out", "dropped")):
            left_out[case_id] = action
        elif ruled:
            left_out[case_id] = ruled
        elif action.startswith("read before") and case_id not in read:
            left_out[case_id] = f"{action} (not listed with --read)"
        elif until and today > until:
            left_out[case_id] = f"{action}: past the date"
        else:
            run.append(item)
    run.sort(key=lambda item: date_limit(action_for(item[0]["case_id"], actions)) is None)
    return run, left_out


def code_hashes() -> dict:
    """sha256 of the harness code this run used (the working tree may be ahead of git_commit)."""
    files = [Path(oc.__file__), Path(__file__), Path(oc.__file__).with_name("purdue_proxy.py"),
             oc.SHIM_DIR / "curl", oc.FAKE_CLOCK, *sorted(Path(oc.__file__).with_name("skills").rglob("*.md"))]
    return {str(f.relative_to(REPO_ROOT)): hashlib.sha256(f.read_bytes()).hexdigest() for f in files}


def git(*args) -> str:
    return subprocess.run(["git", *args], capture_output=True, text=True, cwd=REPO_ROOT).stdout.strip()


def write_plan(trial_out: Path, args, items, left_out: dict, trial: int) -> None:
    plan = trial_out / "plan.json"
    if plan.exists():
        return
    spec = oc.BACKENDS[BACKEND]
    write(plan, {
        "started_utc": datetime.now(timezone.utc).isoformat(), "harness": "openclaw",
        "openclaw_version": subprocess.run([oc.OPENCLAW_BIN, "--version"], capture_output=True, text=True,
                                           env={"PATH": os.environ["PATH"], "HOME": str(Path.home())}).stdout.strip(),
        "git_commit": git("rev-parse", "HEAD"), "git_describe": git("describe", "--tags", "--always", "--dirty"),
        "code_sha256": code_hashes(), "agent": oc.AGENT_ID, "backend": BACKEND,
        "model": f"{spec['provider']}/{spec['model']['id']}", "context_window": spec["model"]["contextWindow"],
        "max_output_tokens": spec["model"]["maxTokens"], "proxy_port": spec["port"],
        "endpoint": os.getenv("PURDUE_BASE_URL"), "rate_limit_file": os.getenv("PURDUE_RATE_LIMIT_FILE"),
        "rate_limit_per_minute": os.getenv("PURDUE_RATE_LIMIT_PER_MINUTE"),
        "timeout_seconds_per_turn": args.timeout, "follow_up": False, "prompt_prefix": oc.PREFIX,
        "trial": trial, "trials_per_case": args.trials, "concurrency": args.concurrency,
        "cases_dir": str(args.cases_dir.relative_to(REPO_ROOT)),
        "cases": {c["case_id"]: c.get("case_sha256") for c, _ in items}, "left_out": left_out,
        "known_defects_sha256": hashlib.sha256(KNOWN_DEFECTS.read_bytes()).hexdigest(),
        "solver_context_excludes": ["references", "claims", "cards", "private", "coverage_claims"],
        "judgment": "turn 1 graded from the state after turn 1 and its reply (judge v2)"})


async def execute(case: dict, source: Path, trial: int, args, slot: asyncio.Semaphore) -> dict | None:
    root = args.out / f"t{trial}" / case["case_id"]
    async with slot:  # an attempt is created only when a lane is free
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
        summary = {"case_id": case["case_id"], "domain": case["domain"], "status": "preflight", "harness": "openclaw",
                   "backend": BACKEND, "trial": trial, "started_utc": datetime.now(timezone.utc).isoformat()}
        write(attempt / "execution_summary.json", summary)
        try:
            await asyncio.to_thread(oc.run_attempt, case, attempt, database_url=args.database_url,
                                    backend_url=args.base_url, timeout_s=args.timeout, followup=False,
                                    keep_state=args.keep_state, summary=summary, backend=BACKEND, layout="judge")
        except Exception as exc:  # recorded; other tests keep running
            summary.update(status="infrastructure_error", error=f"{type(exc).__name__}: {exc}")
    summary["ended_utc"] = datetime.now(timezone.utc).isoformat()
    write(attempt / "execution_summary.json", summary)
    print(json.dumps({k: summary.get(k) for k in ("case_id", "trial", "status", "termination", "turns", "error")}),
          flush=True)
    return summary


def summarize(trial_out: Path) -> None:
    rows, totals = [], {}
    for path in sorted(trial_out.glob("*/attempt-*/execution_summary.json")):
        s = json.loads(path.read_text())
        s["attempt_dir"] = str(path.parent.relative_to(trial_out))
        rows.append(s)
        for k, v in (s.get("usage") or {}).items():
            if isinstance(v, (int, float)):
                totals[k] = round(totals.get(k, 0) + v, 1)
    write(trial_out / "usage_summary.json", {"attempts": rows, "usage_totals": totals, "cost_usd": 0.0,
                                             "cost_source": "the self-hosted Qwen has no per-token charge; tokens "
                                                            "are server-reported through the local proxy"})


def check_proxy() -> None:
    port = oc.BACKENDS[BACKEND]["port"]
    try:
        with urllib.request.urlopen(f"http://127.0.0.1:{port}/v1/models", timeout=60) as response:
            served = {m.get("id") for m in json.loads(response.read()).get("data", [])}
    except Exception as exc:
        raise SystemExit(f"self-host proxy not reachable on port {port}: {exc}")
    wanted = oc.BACKENDS[BACKEND]["model"]["id"]
    if wanted not in served:
        raise SystemExit(f"the proxy on port {port} serves {sorted(served)}, not {wanted}")


async def main_async(args) -> None:
    check_proxy()
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
    parser.add_argument("--concurrency", type=int, default=8)
    parser.add_argument("--timeout", type=int, default=oc.TIMEOUT_SECONDS, help="seconds per OpenClaw turn")
    parser.add_argument("--read", nargs="*", help="'read before it runs' tests that have been read")
    parser.add_argument("--keep-state", action="store_true", help="keep each OpenClaw state directory")
    parser.add_argument("--retry-infrastructure", action="store_true")
    parser.add_argument("--database-url", default=os.getenv("DATABASE_URL",
                                                            "postgresql://postgres@127.0.0.1:15432/agentdiff_campaign"))
    parser.add_argument("--base-url", default="http://127.0.0.1:18001")
    args = parser.parse_args()
    if os.getenv("SOLVER_BACKEND") != BACKEND:
        raise SystemExit("run through the launcher with SOLVER_BACKEND=selfhost (it records the shared limiter)")
    if args.concurrency > 48:
        raise SystemExit("keep at most 48 attempts in flight per session (grounding/solver/README.md)")
    args.out = args.out.resolve()
    args.cases_dir = args.cases_dir.resolve()
    os.environ.setdefault("DATABASE_URL", args.database_url)  # backend seed modules read it at import time
    asyncio.run(main_async(args))


if __name__ == "__main__":
    main()
