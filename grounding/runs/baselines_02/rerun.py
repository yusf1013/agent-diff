"""The quiet rerun of trials that timed out under host load (the lead's rule, 2026-09-30), as new attempts beside the
old ones.

    SOLVER_BACKEND=selfhost python grounding/runs/fact_coverage_02/launch.py grounding.runs.baselines_02.rerun \
        HOST_LOAD.json [--concurrency 2]

- **Which trials:** the keys of `runs/host_load.json` (`<run>/<trial>/<case>`) whose latest attempt is still the one
  recorded there. A trial whose rerun already ran is not run again.
- **How:** exactly `openclaw_eval_01/run.py`'s attempt (`runtime.run_attempt` with the same arguments: the case file
  from the arm's keyed suite, the 600-second budget, the judge's layout), written as the next `attempt-NN` of that
  trial. The runner itself never redoes a completed attempt, so this is its attempt body without that check. The
  old attempt stays as it is; the summary of the new one records why it ran.
- **When:** only when the host is quiet (no other study's solver on the self-host), checked by hand before running.
"""
from __future__ import annotations

import argparse
import asyncio
import json
from datetime import datetime, timezone
from pathlib import Path

from grounding.integrations.agentdiff.runtime import write
from grounding.integrations.openclaw import runtime as oc
from grounding.runs.openclaw_eval_01 import run as runner

HERE = Path(__file__).resolve().parent
SUITES = {"solve_sn0m_01": HERE / "runs" / "suite_sn0m_01", "solve_sn1m_01": HERE / "runs" / "suite_sn1m_01"}
REASON = "rerun: the earlier attempt timed out under host load (few requests at over 30 s each; the lead's rule)"


async def one(key: str, recorded: str, args, slot: asyncio.Semaphore) -> None:
    run, trial, case_id = key.split("/")
    root = HERE / "runs" / run / trial / case_id
    attempts = sorted(root.glob("attempt-*"))
    if attempts[-1].name != recorded:
        print(json.dumps({"key": key, "skipped": f"latest is {attempts[-1].name}, not {recorded}"}), flush=True)
        return
    source = next(SUITES[run].glob(f"*/{case_id}.json"))
    case = json.loads(source.read_text())
    async with slot:
        attempt = root / f"attempt-{len(attempts) + 1:02}"
        attempt.mkdir(parents=True, exist_ok=False)
        (attempt / "case.json").write_text(source.read_text())
        summary = {"case_id": case_id, "domain": case["domain"], "status": "preflight", "harness": "openclaw",
                   "backend": "selfhost", "trial": int(trial[1:]), "rerun_reason": REASON, "replaces": recorded,
                   "started_utc": datetime.now(timezone.utc).isoformat()}
        write(attempt / "execution_summary.json", summary)
        try:
            await asyncio.to_thread(oc.run_attempt, case, attempt, database_url=args.database_url,
                                    backend_url=args.base_url, timeout_s=oc.TIMEOUT_SECONDS, followup=False,
                                    keep_state=False, summary=summary, backend="selfhost", layout="judge")
        except Exception as exc:  # recorded, as the runner does
            summary.update(status="infrastructure_error", error=f"{type(exc).__name__}: {exc}")
        summary["ended_utc"] = datetime.now(timezone.utc).isoformat()
        write(attempt / "execution_summary.json", summary)
        print(json.dumps({k: summary.get(k) for k in ("case_id", "trial", "status", "termination", "turns")}),
              flush=True)


async def main_async(args) -> None:
    runner.BACKEND = "selfhost"
    runner.check_proxy()
    todo = {k: v["attempt"] for k, v in json.loads(args.host_load.read_text()).items() if not k.startswith("_")}
    slot = asyncio.Semaphore(args.concurrency)
    await asyncio.gather(*(one(k, a, args, slot) for k, a in sorted(todo.items())))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("host_load", type=Path)
    parser.add_argument("--concurrency", type=int, default=2)
    parser.add_argument("--database-url", default="postgresql://postgres@127.0.0.1:15432/agentdiff_campaign")
    parser.add_argument("--base-url", default="http://127.0.0.1:18001")
    args = parser.parse_args()
    asyncio.run(main_async(args))


if __name__ == "__main__":
    main()
