"""Trials of an OpenClaw run that ran out OpenClaw's turn limit, and which of them did so under host load (the lead,
2026-09-30: "a trial that times out with few requests at over 30 s each"). No model calls.

    python3 grounding/runs/qwen_writer_01/host_load.py [RUN]

For every trial whose latest attempt completed with termination "timeout", or whose turn, less rate-limiter waits,
passed the 600 s budget: its requests to the model (solver/requests.tar.xz, each request's `duration_s`), their
count and median duration. The rule, fixed before any such trial was read: "timeout under host load" when it made
at most 12 requests and their median took more than 30 s. Those trials are kept apart for a quiet rerun and counted
separately; the others are ordinary timeouts (the solver's failure, as the PI ruled). Writes eval/host_load_RUN.json.
"""
import json
import statistics
import sys
import tarfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
BUDGET_S = 600
MAX_REQUESTS = 12
MEDIAN_OVER_S = 30


def durations(attempt: Path) -> list[float]:
    solver = attempt / "solver"
    out = []
    if (solver / "requests.tar.xz").exists():
        with tarfile.open(solver / "requests.tar.xz") as tar:
            for m in tar.getmembers():
                if m.name.endswith(".meta.json"):
                    out.append(json.loads(tar.extractfile(m).read()).get("duration_s") or 0.0)
    else:
        out = [json.loads(p.read_text()).get("duration_s") or 0.0 for p in (solver / "requests").glob("*.meta.json")]
    return out


def main():
    run = sys.argv[1] if len(sys.argv) > 1 else "oc_01"
    rows = []
    for trial_dir in sorted((HERE / "runs" / run).glob("t*/*")):
        attempts = sorted(trial_dir.glob("attempt-*"))
        if not attempts or not (attempts[-1] / "execution_summary.json").exists():
            continue
        s = json.loads((attempts[-1] / "execution_summary.json").read_text())
        if s.get("status") != "completed":
            continue
        turn = (s.get("turn_durations_s") or [0])[0]
        wait = (s.get("usage") or {}).get("limiter_wait_s") or 0
        if s.get("termination") != "timeout" and turn - wait <= BUDGET_S:
            continue
        d = durations(attempts[-1])
        median = statistics.median(d) if d else None
        rows.append({"trial": f"{trial_dir.parent.name}/{trial_dir.name}", "attempt": attempts[-1].name,
                     "termination": s.get("termination"), "turn_s": turn, "limiter_wait_s": wait,
                     "requests": len(d), "median_request_s": round(median, 1) if median else None,
                     "requests_over_30s": sum(1 for x in d if x > 30),
                     "host_load": bool(d) and len(d) <= MAX_REQUESTS and median > MEDIAN_OVER_S})
    reclassified = []  # earlier attempts marked by reclassify_host_load.py and rerun on a quiet server
    for path in sorted((HERE / "runs" / run).glob("t*/*/attempt-*/execution_summary.json")):
        s = json.loads(path.read_text())
        if s.get("reclassified_from"):
            later = sorted(path.parent.parent.glob("attempt-*"))[-1]
            rerun = json.loads((later / "execution_summary.json").read_text()) if later != path.parent else {}
            d = durations(path.parent)
            reclassified.append({"trial": f"{path.parent.parent.parent.name}/{path.parent.parent.name}",
                                 "attempt": path.parent.name, "original": s["reclassified_from"],
                                 "turn_s": (s.get("turn_durations_s") or [0])[0], "requests": len(d),
                                 "median_request_s": round(statistics.median(d), 1) if d else None,
                                 "rerun": {"attempt": later.name, "status": rerun.get("status"),
                                           "termination": rerun.get("termination"),
                                           "turn_s": (rerun.get("turn_durations_s") or [None])[0],
                                           "requests": (rerun.get("usage") or {}).get("requests")}})
    out = {"run": run, "rule": f"timeout under host load: at most {MAX_REQUESTS} requests with a median over "
                               f"{MEDIAN_OVER_S} s", "trials": rows, "reclassified_and_rerun": reclassified}
    (HERE / "eval" / f"host_load_{run}.json").write_text(json.dumps(out, indent=1) + "\n")
    for r in rows:
        print(r)
    for r in reclassified:
        print("reclassified and rerun:", r)
    print(f"{len(rows)} timeouts in the latest attempts; {sum(r['host_load'] for r in rows)} under host load; "
          f"{len(reclassified)} reclassified and rerun")


if __name__ == "__main__":
    main()
