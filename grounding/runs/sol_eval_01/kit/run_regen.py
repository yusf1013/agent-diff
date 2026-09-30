"""The Sol round on the regenerated half (regen_01's suite): runs its three sets through regen_01's runner
(openclaw_eval_01's runner with regen_01's rulings wrapper) on the PI's OpenAI plan, and stops everything if the
provider starts refusing for quota or rate limits. No judging; no model calls of its own.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.sol_eval_01.kit.run_regen [--store main]

`--store main` sets AGENTDIFF_OPENAI_STORE=main for the runner (the adapter's opt-in login-store layout, under which
memory_search works); without it the runner gets the default layout of the first half's runs. Each attempt's
solver/config.json records `openai_store`.

- **Sets:** regen_01/runs/full_01_cases (206 regular tests), absence_01_cases (72 units), underspecified_01_cases (59
  units), written to runs/regen_full_01, runs/regen_absence_01 and runs/regen_underspecified_01 (links into the main
  checkout's runs directory).
- **Order:** the plan's weekly window is limited, so every test runs once first (trial 1 of all three sets), then
  trials 2 and 3 (`--trials 3`; the runner never redoes a completed attempt), then one pass with
  `--retry-infrastructure`. 10 in flight, the runner's 10-minute turn limit, thinking "medium" (the adapter's default
  for the openai backend).
- **Stop rule:** after each finished attempt, its execution summary is read. If 3 of the last 20 attempts ended as
  infrastructure errors naming a provider limit (runtime.PROVIDER_LIMIT in the error or in `flags.provider_limits`),
  or 10 of the last 20 did not complete (infrastructure, runner or preflight errors), the runner's process group is
  stopped, nothing further starts, and regen_stopped.txt records why. Completed attempts are kept. The OpenClaw
  turns in flight run in their own sessions and finish on their own (at most 10, each within the 10-minute limit);
  with the runner stopped, their attempts get no summary.
- **Records** (in the main checkout's runs directory, beside the run folders): each pass's runner output in
  regen_<set>.log, progress in regen_progress.txt, and regen_done.txt at the end.
"""
from __future__ import annotations

import json
import os
import signal
import subprocess
import sys
from collections import deque
from datetime import datetime
from pathlib import Path

from grounding.integrations.openclaw.runtime import PROVIDER_LIMIT

STUDY = Path(__file__).resolve().parents[1]
REPO = STUDY.parents[2]
RUNS = STUDY / "runs"  # the run folders are links into the main checkout's runs directory
MAIN_RUNS = Path("/home/yusf/PyProj/agent-diff/grounding/runs/sol_eval_01/runs")  # logs and markers go there too
SETS = (("regen_full_01", "full_01_cases"), ("regen_absence_01", "absence_01_cases"),
        ("regen_underspecified_01", "underspecified_01_cases"))
LAUNCH = [sys.executable, str(REPO / "grounding/runs/fact_coverage_02/launch.py"), "grounding.runs.regen_01.run"]
recent: deque = deque(maxlen=20)


def note(path: str, text: str) -> None:
    with open(MAIN_RUNS / path, "a") as f:
        f.write(f"{datetime.now().isoformat(timespec='seconds')} {text}\n")


def limited(out: Path, line: dict) -> tuple[bool, bool]:
    """(an infrastructure error, one naming a provider limit) for a finished attempt's printed line."""
    if line.get("status") not in ("infrastructure_error", "runner_error", "preflight"):
        return False, False
    text = str(line.get("error") or "")
    attempts = sorted((out / f"t{line.get('trial')}" / str(line.get("case_id"))).glob("attempt-*"))
    if attempts and (attempts[-1] / "execution_summary.json").exists():
        summary = json.loads((attempts[-1] / "execution_summary.json").read_text())
        text += " " + " ".join((summary.get("flags") or {}).get("provider_limits") or [])
    return True, bool(PROVIDER_LIMIT.search(text))


def run(name: str, cases: str, trials: int, retry: bool, env: dict) -> str | None:
    out = RUNS / name
    args = LAUNCH + ["--backend", "openai", "--trials", str(trials), "--concurrency", "10", "--out", str(out),
                     "--cases-dir", str(REPO / "grounding/runs/regen_01/runs" / cases)]
    if retry:
        args.append("--retry-infrastructure")
    note("regen_progress.txt", f"start {name} trials={trials}{' retry' if retry else ''}")
    with open(MAIN_RUNS / f"{name}.log", "a") as log:
        proc = subprocess.Popen(args, cwd=REPO, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
                                start_new_session=True, env=env)
        for raw in proc.stdout:
            log.write(raw)
            log.flush()
            try:
                line = json.loads(raw)
            except ValueError:
                continue
            if "status" not in line or "trial" not in line:
                continue
            recent.append(limited(out, line))
            infra = sum(i for i, _ in recent)
            limits = sum(lim for _, lim in recent)
            if limits >= 3 or infra >= 10:
                reason = (f"{limits} of the last {len(recent)} attempts ended on a provider limit" if limits >= 3 else
                          f"{infra} of the last {len(recent)} attempts did not complete")
                os.killpg(proc.pid, signal.SIGTERM)
                proc.wait()
                return reason
        proc.wait()
    note("regen_progress.txt", f"done {name} trials={trials}{' retry' if retry else ''} (exit {proc.returncode})")
    return None


def main() -> None:
    for name, _ in SETS:
        if (RUNS / name).resolve() != MAIN_RUNS / name:
            raise SystemExit(f"{RUNS / name} must link to {MAIN_RUNS / name}")
    env = dict(os.environ)
    env.pop("AGENTDIFF_OPENAI_STORE", None)
    if sys.argv[1:] == ["--store", "main"]:
        env["AGENTDIFF_OPENAI_STORE"] = "main"
    elif sys.argv[1:]:
        raise SystemExit(__doc__)
    note("regen_progress.txt", f"login-store layout: {env.get('AGENTDIFF_OPENAI_STORE', 'default')}")
    plan = [(trials, False) for trials in (1, 3)] + [(3, True)]
    for trials, retry in plan:
        for name, cases in SETS:
            reason = run(name, cases, trials, retry, env)
            if reason:
                note("regen_stopped.txt", f"stopped during {name} trials={trials}{' retry' if retry else ''}: {reason}; "
                                          "the OpenClaw turns in flight finish on their own, without a summary")
                print(f"stopped: {reason}")
                return
    note("regen_done.txt", "all passes done")
    print("done")


if __name__ == "__main__":
    main()
