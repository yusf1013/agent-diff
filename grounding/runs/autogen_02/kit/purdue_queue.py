"""The Purdue queue: solve runs one after another, in the order of a queue file that can grow while it runs.

    GROUNDING_ENV=/path/to/grounding/.env python grounding/runs/fact_coverage_02/launch.py \
        grounding.runs.autogen_02.kit.purdue_queue QUEUE.jsonl

Each line of QUEUE.jsonl is one run: {"name", "cases", "out", "log"}, with optional
- "after": a log file that must contain "solve done" first (a run started outside the queue);
- "gate": a file that must exist first, and "gate_timeout": seconds after which the gate opens anyway (so that a
  higher-priority run can be put ahead of this one without leaving Purdue idle when it is late);
- {"stop": true} ends the queue when reached.

The first line that is not done and whose conditions hold runs next. Finished runs are appended to
QUEUE.jsonl.done with their start and end times and the number of completed trials. A run that completes no trial
(for instance without the Purdue key, when the runner still prints "solve done") stops the queue.
"""
from __future__ import annotations

import datetime
import json
import os
import subprocess
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
PY = sys.executable


def now() -> str:
    return datetime.datetime.now().isoformat(timespec="seconds")


def done_names(done: Path) -> set[str]:
    if not done.exists():
        return set()
    return {json.loads(line)["name"] for line in done.read_text().splitlines() if line.strip()}


def completed(log: Path) -> int:
    return log.read_text(errors="replace").count('"status": "completed"') if log.exists() else 0


def main():
    queue = Path(sys.argv[1]).resolve()
    done = queue.with_name(queue.name + ".done")
    if not os.environ.get("GROUNDING_ENV"):
        raise SystemExit("GROUNDING_ENV must point at the file with the Purdue key")
    waiting_since: dict[str, float] = {}
    while True:
        entries = [json.loads(line) for line in queue.read_text().splitlines() if line.strip()]
        finished = done_names(done)
        chosen = None
        for e in entries:
            if e.get("stop"):
                if chosen is None:
                    print(f"{now()} queue: stop reached", flush=True)
                    return
                break
            if e["name"] in finished:
                continue
            after = e.get("after")
            if after and "solve done" not in (Path(after).read_text(errors="replace") if Path(after).exists() else ""):
                break  # runs keep their order: nothing after an unmet "after" starts
            gate = e.get("gate")
            if gate and not Path(gate).exists():
                first = waiting_since.setdefault(e["name"], time.time())
                if time.time() - first < float(e.get("gate_timeout", 1e12)):
                    break
                print(f"{now()} queue: gate of {e['name']} timed out, starting it", flush=True)
            chosen = e
            break
        if chosen is None:
            time.sleep(30)
            continue
        log = Path(chosen["log"])
        start = now()
        print(f"{start} queue: start {chosen['name']} ({chosen['cases']} -> {chosen['out']})", flush=True)
        with open(log, "a") as fh:
            rc = subprocess.call([PY, "grounding/runs/fact_coverage_02/launch.py", "grounding.runs.autogen_02.kit.solve",
                                  "--cases-dir", chosen["cases"], "--out", chosen["out"]], cwd=REPO, stdout=fh,
                                 stderr=subprocess.STDOUT)
        n = completed(log)
        with open(done, "a") as fh:
            fh.write(json.dumps({"name": chosen["name"], "start": start, "end": now(), "returncode": rc,
                                 "completed_trials": n}) + "\n")
        print(f"{now()} queue: end {chosen['name']} rc={rc} completed trials={n}", flush=True)
        if n == 0:
            print(f"{now()} queue: {chosen['name']} completed no trial; stopping", flush=True)
            return


if __name__ == "__main__":
    main()
