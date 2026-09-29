"""The size of the OpenClaw experiment: per run, the trials (test x k), the attempts (with infrastructure retries),
agent time, model requests and tokens, from each attempt's execution_summary.json. Runs used for results only:
`full_02` (Box's tests and the first pass), `full_03`, `full_04`, the first pass's policy looks and the policy
populations. The stopped `full_01` (the harness leaked the test) and the smoke runs are counted apart.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.report_01.kit.scale

Writes numbers/scale.json.
"""
from __future__ import annotations

import statistics
from collections import Counter

from grounding.runs.report_01.kit.common import RUNS, load, write

OC = RUNS / "openclaw_eval_01/runs"


def run_stats(folder):
    trials, attempts, seconds, requests, tin, tout = 0, 0, [], 0, 0, 0
    status = Counter()
    for trial_dir in sorted(folder.glob("t*/*")):
        atts = sorted(trial_dir.glob("attempt-*"))
        if not atts:
            continue
        trials += 1
        attempts += len(atts)
        for a in atts:
            p = a / "execution_summary.json"
            if not p.exists():
                continue
            s = load(p)
            status[s.get("status")] += a == atts[-1]
            seconds.append(sum(s.get("turn_durations_s") or [0]))
            u = s.get("usage") or {}
            requests += u.get("requests", 0)
            tin += u.get("input_tokens", 0)
            tout += u.get("output_tokens", 0)
    return {"trials": trials, "attempts": attempts, "last_attempt_status": dict(status),
            "agent_hours": round(sum(seconds) / 3600, 1),
            "median_seconds": round(statistics.median(seconds), 1) if seconds else None,
            "model_requests": requests, "input_tokens_millions": round(tin / 1e6, 1),
            "output_tokens_millions": round(tout / 1e6, 2)}


def main():
    used = {"full_02": OC / "full_02", "full_03": OC / "full_03", "full_04": OC / "full_04"}
    for p in sorted((OC / "policy").glob("solve_*")):
        used[f"policy/{p.name}"] = p
    apart = {name: OC / name for name in ("full_01", "smoke_01", "smoke_02", "smoke_03")}
    out = {"used": {k: run_stats(v) for k, v in used.items()},
           "apart": {k: run_stats(v) for k, v in apart.items() if v.exists()}}
    tot = Counter()
    for r in out["used"].values():
        for k in ("trials", "attempts", "agent_hours", "model_requests", "input_tokens_millions",
                  "output_tokens_millions"):
            tot[k] += r[k]
    out["used_total"] = {k: round(v, 2) for k, v in tot.items()}
    print(write("scale", out))
    for k, v in out["used"].items():
        print(k, v)
    print("total", out["used_total"])
    print("apart", out["apart"])


if __name__ == "__main__":
    main()
