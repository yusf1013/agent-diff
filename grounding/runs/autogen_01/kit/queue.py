"""Run several generated suites on the solver one after another, then judge and score each in the background.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.autogen_01.kit.queue GEN:SOLVE [GEN:SOLVE ...]

Solver runs share one rate limit, so they go strictly one at a time (each with its retry pass). As soon as a suite's
solver runs finish, its judging and scoring start in the background (`solve --skip-solver`), while the next suite
runs on the solver. A new queue first waits for any solver run already in progress.
"""
from __future__ import annotations

import subprocess
import sys
import time
from pathlib import Path

from grounding.paths import REPO_ROOT

LAUNCH = [sys.executable, str(REPO_ROOT / "grounding/runs/fact_coverage_02/launch.py")]
RUNS = Path(__file__).resolve().parents[1] / "runs"


def solver_busy() -> bool:
    out = subprocess.run(["ps", "-eo", "args"], capture_output=True, text=True).stdout
    return any("fact_coverage_02.run" in line and "--out" in line for line in out.splitlines())


def main():
    pairs = [a.split(":") for a in sys.argv[1:]]
    while solver_busy():
        time.sleep(30)
    judges = []
    for gen, solve in pairs:
        gen_dir, out = RUNS / gen, RUNS / solve
        for extra in ([], ["--concurrency", "3", "--retry-infrastructure", "--retry-timeouts"]):
            args = ["grounding.runs.fact_coverage_02.run", "--out", str(out), "--cases-dir", str(gen_dir / "cases"),
                    "--trials", "3", "--concurrency", "6", *extra]
            print("+", solve, " ".join(extra) or "main pass", flush=True)
            subprocess.run(LAUNCH + args, cwd=REPO_ROOT)
        log = open(Path("/tmp/autogen-5840209d") / f"judge_{solve}.log", "a")
        judges.append(subprocess.Popen(LAUNCH + ["grounding.runs.autogen_01.kit.solve", "--gen-run", str(gen_dir),
                                                 "--out", str(out), "--skip-solver", "--judge-concurrency", "3"],
                                       cwd=REPO_ROOT, stdout=log, stderr=subprocess.STDOUT))
        print("judging started:", solve, flush=True)
    for j in judges:
        j.wait()
    print("queue done", flush=True)


if __name__ == "__main__":
    main()
