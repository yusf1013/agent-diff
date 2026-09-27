"""Run a set of variant cases on the solver: a main pass, then one retry pass for infrastructure errors and timeouts.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.autogen_02.kit.solve --cases-dir DIR --out RUN \
        [--cases ID ...] [--trials 3]

Uses fact_coverage_02's runner and the shared Purdue rate limiter, exactly as autogen_01's queue did. Solver runs wait
for any other solver run in progress, so two runs never compete for the limit.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
import time
from pathlib import Path

from grounding.paths import REPO_ROOT

LAUNCH = [sys.executable, str(REPO_ROOT / "grounding/runs/fact_coverage_02/launch.py")]


def solver_busy() -> bool:
    out = subprocess.run(["ps", "-eo", "args"], capture_output=True, text=True).stdout
    return any("fact_coverage_02.run" in line and "--out" in line for line in out.splitlines())


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
    for extra in ([], ["--concurrency", "3", "--retry-infrastructure", "--retry-timeouts"]):
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
