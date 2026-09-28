"""Run a set of variant cases on the solver: a main pass, then one retry pass for infrastructure errors.

Since 2026-09-27 (roadmap_01) Purdue waiting is off the trial's time budget (grounding/solver/slack/agent_clock.py): a
cut by the wall ceiling counts as an infrastructure error and is retried; a cut by the agent's own budget ("timeout")
is the agent's and is graded, not retried. Earlier runs retried every timeout (`--retry-timeouts`).

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.autogen_02.kit.solve --cases-dir DIR --out RUN \
        [--cases ID ...] [--trials 3]
    SOLVER_BACKEND=selfhost python grounding/runs/fact_coverage_02/launch.py grounding.runs.autogen_02.kit.solve ... \
        --concurrency 24     # the self-hosted Qwen; keep at most about 48 in flight per session

Uses fact_coverage_02's runner and the backend's shared rate limiter, as autogen_01's queue did. A Purdue run waits for
any other Purdue run in progress, so two runs never compete for its small limit. A self-hosted run never waits: every
session's requests pass the same limiter (since 2026-09-27; see fact_coverage_02/launch.py).
"""
from __future__ import annotations

import argparse
import os
import subprocess
import sys
import time
from pathlib import Path

from grounding.paths import REPO_ROOT

LAUNCH = [sys.executable, str(REPO_ROOT / "grounding/runs/fact_coverage_02/launch.py")]


def backend_of(pid: str) -> str:
    """The solver backend a running process was started with (SOLVER_BACKEND in its environment; Purdue if absent or
    unreadable)."""
    try:
        env = Path(f"/proc/{pid}/environ").read_bytes().split(b"\0")
    except OSError:
        return "purdue"
    for item in env:
        if item.startswith(b"SOLVER_BACKEND="):
            return item.split(b"=", 1)[1].decode()
    return "purdue"


def busy(ps_lines, own_backend: str, backend=backend_of) -> bool:
    """Purdue runs go one at a time, since they share a small rate limit. Self-hosted runs never wait: the shared
    limiter paces every session on the machine (fact_coverage_02/launch.py)."""
    if own_backend == "selfhost":
        return False
    for line in ps_lines:
        pid, _, args = line.strip().partition(" ")
        if "fact_coverage_02.run" in args and "--out" in args and backend(pid) != "selfhost":
            return True
    return False


def solver_busy() -> bool:
    out = subprocess.run(["ps", "-eo", "pid,args"], capture_output=True, text=True).stdout
    return busy(out.splitlines()[1:], os.environ.get("SOLVER_BACKEND", "purdue"))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--cases-dir", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    p.add_argument("--cases", nargs="*")
    p.add_argument("--trials", type=int, default=3)
    p.add_argument("--concurrency", type=int, default=6)
    args = p.parse_args()
    while solver_busy():
        time.sleep(30)
    for extra in ([], ["--concurrency", "3", "--retry-infrastructure"]):
        cmd = ["grounding.runs.fact_coverage_02.run", "--out", str(args.out.resolve()), "--cases-dir",
               str(args.cases_dir.resolve()), "--trials", str(args.trials), "--concurrency", str(args.concurrency),
               *extra]
        if args.cases:
            cmd += ["--cases", *args.cases]
        print("+", " ".join(extra) or "main pass", flush=True)
        subprocess.run(LAUNCH + cmd, cwd=REPO_ROOT)
    print("solve done", flush=True)


if __name__ == "__main__":
    main()
