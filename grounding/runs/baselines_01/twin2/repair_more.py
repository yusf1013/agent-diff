"""One more repair turn for a domain whose tests still do not load after the generator's one repair turn (a deviation
from round 1's protocol, recorded in the log and in `load.json`; at most two such turns per domain).

    AUTOGEN_BACKEND=muse python grounding/runs/fact_coverage_02/launch.py \\
        grounding.runs.baselines_01.twin2.repair_more --gen GEN_DIR --domain DOMAIN --generator N0M

The turn resumes the same session with the generator's own repair prompt and the loader's current errors (invalid
JSON, a missing field, a seed the seed operations reject), as a user would paste them again. It says nothing about the
tests' design. Our writer gets such load feedback until its drafts load; the baseline's cap of one turn was ours. The round is snapshotted as `workspace/roundN`,
appended to `load.json`, and the cases are rewritten from the result.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from grounding.runs.autogen_01.kit import agent
from grounding.runs.baselines_01.n0 import cases
from grounding.runs.baselines_01.n0.generate import REPAIR, WORK, load, snapshot


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gen", type=Path, required=True)
    ap.add_argument("--domain", required=True)
    ap.add_argument("--generator", required=True)
    args = ap.parse_args()
    if agent.BACKEND != "muse":
        raise SystemExit("set AUTOGEN_BACKEND=muse")
    run = args.gen.resolve()
    out = run / args.domain
    ws = WORK / f"{args.generator}-{run.name}" / args.domain
    report = json.loads((out / "load.json").read_text())
    errors = report["rounds"][-1]["errors"]
    if not errors:
        raise SystemExit("the tests already load")
    n = report["rounds"][-1]["round"] + 1
    call = agent.Call(role="coder", workspace=ws, prompt=REPAIR.format(errors="\n".join(f"- {e}" for e in errors)),
                      log_dir=out / "agent", calls_log=run / "calls.jsonl", tools=agent.FILE_TOOLS, write=True,
                      resume=report["rounds"][0]["session_id"], label=f"{args.domain}/round{n}", timeout=3600)
    agent.run(call)
    snapshot(ws, out / "workspace" / f"round{n}")
    built, errors = load(args.domain, ws, args.generator)
    report["rounds"].append({"round": n, "cases": len(built), "errors": errors,
                             "tests_written": cases.count_tests(ws / "tests.json"),
                             "note": "extra repair turn with the loader's errors, beyond the protocol's one (log)"})
    dest = out / "cases"
    dest.mkdir(parents=True, exist_ok=True)
    for case in built:
        (dest / f"{case['case_id']}.json").write_text(json.dumps(case, indent=1, ensure_ascii=False) + "\n")
    (out / "load.json").write_text(json.dumps(report, indent=1) + "\n")
    print(json.dumps(report["rounds"][-1]))


if __name__ == "__main__":
    main()
