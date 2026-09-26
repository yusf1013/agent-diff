"""Run a generated suite on the solver, retry trials without a result once, judge, and score.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.autogen_01.kit.solve \
        --gen-run RUN_DIR --out SOLVER_RUN_DIR [--trials 3] [--concurrency 6] [--judge-concurrency 4]

Steps (each resumable: finished trials and verdicts are never redone):
1. fact_coverage_02's runner on RUN_DIR/cases at 3 trials (Qwen via Purdue, the shared rate limiter);
2. one retry pass at concurrency 3 for infrastructure errors, interrupted attempts and timeouts, as in
   fact_coverage_02;
3. the judge on every trial that is not mechanically clean, plus a 20% sample of the clean ones;
4. the scorer, written to SOLVER_RUN_DIR/score.json.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from grounding.paths import REPO_ROOT

LAUNCH = [sys.executable, str(REPO_ROOT / "grounding/runs/fact_coverage_02/launch.py")]


def step(*args):
    print("+", " ".join(str(a) for a in args[:6]), "...", flush=True)
    subprocess.run(LAUNCH + [str(a) for a in args], check=True, cwd=REPO_ROOT)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--gen-run", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--trials", type=int, default=3)
    parser.add_argument("--concurrency", type=int, default=6)
    parser.add_argument("--judge-concurrency", type=int, default=4)
    parser.add_argument("--skip-solver", action="store_true", help="judge and score an existing solver run")
    args = parser.parse_args()
    gen, out = args.gen_run.resolve(), args.out.resolve()
    cases = gen / "cases"
    if not args.skip_solver:
        step("grounding.runs.fact_coverage_02.run", "--out", out, "--cases-dir", cases, "--trials", args.trials,
             "--concurrency", args.concurrency)
        step("grounding.runs.fact_coverage_02.run", "--out", out, "--cases-dir", cases, "--trials", args.trials,
             "--concurrency", 3, "--retry-infrastructure", "--retry-timeouts")
    trials_file = out.parent / f"{out.name}.judge_trials.json"
    result = subprocess.run(LAUNCH + ["grounding.runs.autogen_01.kit.judge", "select-run", "--run-dir", str(out),
                                      "--suite", str(gen / "suite.json")], check=True, cwd=REPO_ROOT,
                            capture_output=True, text=True)
    trials_file.write_text(result.stdout)
    print(f"{len(json.loads(result.stdout))} trials to judge", flush=True)
    judged = out.parent / f"{out.name}_judged"
    step("grounding.runs.autogen_01.kit.judge", "run", "--trials", trials_file, "--out", judged,
         "--concurrency", args.judge_concurrency)
    step("grounding.runs.autogen_01.kit.score_run", "--solver-run", out, "--suite", gen / "suite.json",
         "--judged", judged, "--json", out.parent / f"{out.name}.score.json")


if __name__ == "__main__":
    main()
