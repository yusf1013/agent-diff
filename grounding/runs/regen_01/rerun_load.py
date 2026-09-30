"""Re-run the trials that timed out under host load (score.py `under_load`: fewer than 10 completed model requests,
median over 30 s), each in the same trial slot, into a separate run folder, so the original attempts stay as the
evidence of the first reading (the lead, 2026-09-30: rerun them while the host is quiet, report both readings).
openclaw_eval_01's runner does the attempts (its `execute`, unchanged); rules.py is imported first.

    SOLVER_BACKEND=selfhost python grounding/runs/fact_coverage_02/launch.py grounding.runs.regen_01.rerun_load \
        RUN [--concurrency 12] [--list]

Finds RUN's host-load timeouts (its latest attempt per trial), then runs each (case, trial) once into
runs/<RUN>_load/t<k>/<case>/attempt-NN. --list only prints them. The quiet-host reading replaces each such trial by
its re-run; the as-run reading keeps the timeout (a failure that exposes no fact).
"""
from __future__ import annotations

import argparse
import asyncio
import json
import os
from pathlib import Path

from grounding.runs.regen_01 import rules, score  # noqa: F401  (rules before the runner)
from grounding.runs.openclaw_eval_01 import run as runner
from grounding.runs.autogen_01.kit import judge as v1

HERE = Path(__file__).resolve().parent


def load_trials(run: str) -> list[tuple[str, int]]:
    """(case id, trial number) of RUN's host-load timeouts, on each trial's latest attempt."""
    out = []
    for root in sorted(p for p in (HERE / "runs" / run).glob("t*/*") if p.is_dir() and any(p.glob("attempt-*"))):
        trial, case_id = root.parent.name, root.name
        attempt = v1.latest(HERE / "runs" / run, trial, case_id)
        if (attempt / "execution_summary.json").exists() and score.under_load(attempt):
            out.append((case_id, int(trial[1:])))
    return out


async def main_async(args, pairs):
    runner.check_proxy()
    cases_dir = HERE / "runs" / f"{args.run}_cases"
    paths = {p.stem: p for p in cases_dir.glob("*/*.json") if p.name != "suite.json"}
    slot = asyncio.Semaphore(args.concurrency)
    jobs = [runner.execute(json.loads(paths[c].read_text()), paths[c], k, args, slot) for c, k in pairs]
    results = await asyncio.gather(*jobs, return_exceptions=True)
    for (c, k), r in zip(pairs, results):
        status = r if isinstance(r, BaseException) else (r or {}).get("status")
        print(json.dumps({"case_id": c, "trial": k, "status": str(status)[:200]}), flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("run")
    parser.add_argument("--concurrency", type=int, default=12)
    parser.add_argument("--list", action="store_true")
    args = parser.parse_args()
    pairs = load_trials(args.run)
    print(f"{len(pairs)} host-load timeouts in {args.run}: {pairs}")
    if args.list or not pairs:
        return
    if os.getenv("SOLVER_BACKEND") != "selfhost":
        raise SystemExit("run through the launcher with SOLVER_BACKEND=selfhost")
    args.out = (HERE / "runs" / f"{args.run}_load").resolve()
    args.cases_dir = (HERE / "runs" / f"{args.run}_cases").resolve()
    args.retry_infrastructure, args.keep_state, args.timeout = True, False, runner.oc.TIMEOUT_SECONDS
    args.database_url = os.getenv("DATABASE_URL", "postgresql://postgres@127.0.0.1:15432/agentdiff_campaign")
    args.base_url, args.trials = "http://127.0.0.1:18001", 3
    items = [(json.loads(p.read_text()), p) for p in args.cases_dir.glob("*/*.json") if p.name != "suite.json"]
    for k in (1, 2, 3):
        (args.out / f"t{k}").mkdir(parents=True, exist_ok=True)
        runner.write_plan(args.out / f"t{k}", args, [i for i in items if (i[0]["case_id"], k) in set(pairs)], {}, k)
    asyncio.run(main_async(args, pairs))
    for k in (1, 2, 3):
        runner.summarize(args.out / f"t{k}")


if __name__ == "__main__":
    main()
