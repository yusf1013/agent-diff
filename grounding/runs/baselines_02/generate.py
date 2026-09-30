"""N0M and N1M written by Sonnet 5.5 through Claude Code: one session per service writes 12 tests from baselines_01's
inputs, with the loader's errors fed back until the tests load (at most three repair turns).

    AUTOGEN_BACKEND=claude AUTOGEN_MODEL=claude-sonnet-5-5 \\
    python grounding/runs/fact_coverage_02/launch.py grounding.runs.baselines_02.generate \\
        --arm n0m|n1m --run NAME [--domains box calendar ...]

- **The agent:** Claude Code through the generation kit (`autogen_01/kit/agent.py`): `claude -p` in a clean workspace
  outside the repository, restricted mode, file tools only, no MCP servers, effort `high` (the Muse arms' setting).
  The prompt is `task.md`'s text; the workspace holds the arm's five or six input files, as for the Muse arms.
- **Feedback:** none about the tests' design. If some tests do not load (invalid JSON, a missing field, a seed the
  seed operations reject), the same session gets baselines_01's repair prompt with exactly those errors, up to three
  times (baselines_01's rule for the full comparison: at most three turns).
- **A failed call** (a refusal, a timeout, an error) is kept on disk and stops the driver: the domain is run again
  under a new run name, in a fresh workspace, so a half-written workspace never carries over.
- **Evidence:** `runs/<NAME>/<domain>/`: the prompts, results and transcripts (`agent/`), every file the agent wrote
  per round (`workspace/roundN/`), the loading report (`load.json`) and the runnable cases (`cases/`). Usage per call
  goes to `runs/<NAME>/calls.jsonl` (`total_cost_usd` is Claude Code's list-price estimate; the plan bills nothing).
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

from grounding.runs.autogen_01.kit import agent
from grounding.runs.baselines_01.n0 import cases
from grounding.runs.baselines_01.n0.generate import REPAIR, load, snapshot

HERE = Path(__file__).resolve().parent
TWIN2 = HERE.parent / "baselines_01" / "twin2"
ARMS = {"n0m": (TWIN2 / "n0m" / "inputs", "SN0M"), "n1m": (TWIN2 / "n1m" / "inputs", "SN1M")}
WORK = Path(os.environ.get("BASELINES_WORK", Path.home() / ".cache" / "baselines_02" / "ws"))
DOMAINS = ("box", "calendar", "linear", "slack")
EFFORT = "high"
MAX_REPAIRS = 3
TIMEOUT = 3600


def call(ws: Path, out: Path, run: Path, prompt: str, label: str, resume: str | None = None) -> dict:
    return agent.run(agent.Call(role="coder", workspace=ws, prompt=prompt, log_dir=out / "agent",
                                calls_log=run / "calls.jsonl", tools=agent.FILE_TOOLS, write=True, resume=resume,
                                effort=EFFORT, label=label, timeout=TIMEOUT, retries=0))


def one_domain(domain: str, run: Path, inputs: Path, generator: str) -> dict:
    out = run / domain
    ws = WORK / f"{generator}-{run.name}" / domain
    if ws.exists() or out.exists():
        raise SystemExit(f"{ws} or {out} exists; use a new run name")
    ws.mkdir(parents=True)
    for f in sorted((inputs / domain).iterdir()):
        agent_input = ws / f.name
        agent_input.write_bytes(f.read_bytes())
    report = {"domain": domain, "generator": generator, "model": agent.MODEL, "effort": EFFORT, "rounds": []}
    prompt, session, label = (inputs / domain / "task.md").read_text(), None, f"{domain}/round1"
    for n in range(1, MAX_REPAIRS + 2):
        try:
            result = call(ws, out, run, prompt, label, resume=session)
        except RuntimeError as exc:  # kept as *.failed.json by the kit; stop here
            report["rounds"].append({"round": n, "failed": str(exc)[:2000]})
            (out / "load.json").write_text(json.dumps(report, indent=1) + "\n")
            raise SystemExit(f"{domain} round {n} failed; see {out / 'agent'}")
        session = result.get("session_id") or session
        snapshot(ws, out / "workspace" / f"round{n}")
        built, errors = load(domain, ws, generator)
        report["rounds"].append({"round": n, "session_id": result.get("session_id"),
                                 "num_turns": result.get("num_turns"), "cases": len(built), "errors": errors,
                                 "tests_written": cases.count_tests(ws / "tests.json")})
        if not errors:
            break
        prompt, label = REPAIR.format(errors="\n".join(f"- {e}" for e in errors)), f"{domain}/round{n + 1}"
    dest = out / "cases"
    dest.mkdir(parents=True, exist_ok=True)
    for case in built:
        (dest / f"{case['case_id']}.json").write_text(json.dumps(case, indent=1, ensure_ascii=False) + "\n")
    (out / "load.json").write_text(json.dumps(report, indent=1) + "\n")
    return report


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--arm", choices=sorted(ARMS), required=True)
    ap.add_argument("--run", required=True)
    ap.add_argument("--domains", nargs="*", default=list(DOMAINS))
    args = ap.parse_args()
    if agent.BACKEND != "claude" or agent.MODEL != "claude-sonnet-5-5":
        raise SystemExit("set AUTOGEN_BACKEND=claude and AUTOGEN_MODEL=claude-sonnet-5-5")
    inputs, generator = ARMS[args.arm]
    run = HERE / "runs" / args.run
    run.mkdir(parents=True, exist_ok=True)
    for d in args.domains:
        report = one_domain(d, run, inputs, generator)
        print(json.dumps({k: v for k, v in report.items() if k != "rounds"} |
                         {"rounds": [{k: v for k, v in r.items() if k != "errors"} | {"errors": len(r.get("errors", []))}
                                     for r in report["rounds"]]}), flush=True)


if __name__ == "__main__":
    main()
