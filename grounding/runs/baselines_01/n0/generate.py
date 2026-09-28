"""N0, "ask your coding agent": one Muse Code session per domain writes 12 tests from n0/inputs/<domain>/.

    AUTOGEN_BACKEND=muse python grounding/runs/fact_coverage_02/launch.py \\
        grounding.runs.baselines_01.n0.generate --run NAME [--domains box calendar ...]

- **The agent:** Muse Code with the kit's settings (`autogen_01/kit/agent.py`: model, effort, sandbox, file tools, no
  shell or web), and Muse's default reminders, as a user's coding agent would run. The prompt is `task.md`'s text;
  the folder holds `task.md`, `format.md`, `api.md`, `seed_ops.md` and `schema.md` (see `make_inputs.py`).
- **Feedback:** none about the tests' design. If some tests cannot be loaded (invalid JSON, a missing field, a seed
  the seed operations reject), the agent gets one repair turn in the same session with exactly those errors, as a
  user would paste them back. Both rounds are recorded, so "loads at first" and "loads after one repair" are both
  known.
- **Evidence:** under `n0/runs/<NAME>/<domain>/`: the agent's prompt, transcript, events and result (`agent/`),
  every file the agent wrote (`workspace/`, per round), and the loading report (`load.json`). Usage goes to
  `n0/runs/<NAME>/calls.jsonl`.

The workspaces live outside the repository, as the sandbox requires (`BASELINES_WORK`, default
~/.cache/baselines_01/ws).
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
from pathlib import Path

from grounding.runs.autogen_01.kit import agent
from grounding.runs.baselines_01.n0 import cases

HERE = Path(__file__).resolve().parent
INPUTS = HERE / "inputs"
WORK = Path(os.environ.get("BASELINES_WORK", Path.home() / ".cache" / "baselines_01" / "ws"))
DOMAINS = ("box", "calendar", "linear", "slack")
N_TESTS = 12

REPAIR = """Some tests in `tests.json` could not be loaded:

{errors}

Please fix `tests.json` so that every test loads, and reply with a one-line summary of what you changed."""


def snapshot(ws: Path, dest: Path) -> None:
    dest.mkdir(parents=True, exist_ok=True)
    for f in ws.iterdir():
        if f.is_file():
            shutil.copy(f, dest / f.name)


def load(domain: str, ws: Path) -> tuple[list[dict], list[str]]:
    """(cases, errors) from the workspace's tests.json."""
    path = ws / "tests.json"
    if not path.exists():
        return [], ["`tests.json` does not exist."]
    try:
        data = json.loads(path.read_text())
    except json.JSONDecodeError as exc:
        return [], [f"`tests.json` is not valid JSON: {exc}"]
    return cases.from_tests(domain, data)


def one_domain(domain: str, run: Path) -> dict:
    out = run / domain
    ws = WORK / run.name / domain
    if ws.exists() or out.exists():
        raise SystemExit(f"{ws} or {out} exists; use a new run name")
    ws.mkdir(parents=True)
    for f in sorted((INPUTS / domain).iterdir()):
        shutil.copy(f, ws / f.name)
    prompt = (INPUTS / domain / "task.md").read_text()
    call = agent.Call(role="coder", workspace=ws, prompt=prompt, log_dir=out / "agent", calls_log=run / "calls.jsonl",
                      tools=agent.FILE_TOOLS, write=True, label=f"{domain}/round1", timeout=3600)
    result = agent.run(call)
    snapshot(ws, out / "workspace" / "round1")
    built, errors = load(domain, ws)
    report = {"domain": domain, "rounds": [{"round": 1, "session_id": result.get("session_id"),
                                            "cases": len(built), "errors": errors,
                                            "tests_written": cases.count_tests(ws / "tests.json")}]}
    if errors:
        text = REPAIR.format(errors="\n".join(f"- {e}" for e in errors))
        call2 = agent.Call(role="coder", workspace=ws, prompt=text, log_dir=out / "agent",
                           calls_log=run / "calls.jsonl", tools=agent.FILE_TOOLS, write=True,
                           resume=result.get("session_id"), label=f"{domain}/round2", timeout=3600)
        agent.run(call2)
        snapshot(ws, out / "workspace" / "round2")
        built, errors = load(domain, ws)
        report["rounds"].append({"round": 2, "cases": len(built), "errors": errors,
                                 "tests_written": cases.count_tests(ws / "tests.json")})
    dest = out / "cases"
    dest.mkdir(parents=True, exist_ok=True)
    for case in built:
        (dest / f"{case['case_id']}.json").write_text(json.dumps(case, indent=1, ensure_ascii=False) + "\n")
    (out / "load.json").write_text(json.dumps(report, indent=1) + "\n")
    return report


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--domains", nargs="*", default=list(DOMAINS))
    args = ap.parse_args()
    if agent.BACKEND != "muse":
        raise SystemExit("set AUTOGEN_BACKEND=muse")
    run = HERE / "runs" / args.run
    run.mkdir(parents=True, exist_ok=True)
    for d in args.domains:
        report = one_domain(d, run)
        print(json.dumps(report), flush=True)


if __name__ == "__main__":
    main()
