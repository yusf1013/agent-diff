"""Generate scenarios for a list of briefs with Claude Code Sonnet writers, checks, replica pre-checks and a reader.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.autogen_01.kit.orchestrate \
        --briefs BRIEFS.json --run RUN_DIR [--concurrency 4] [--only ID ...]

For each brief:
1. A clean workspace outside the repository gets the brief, the method notes, the format, the two worked examples
   and the domain inputs. A writer session (Read, Write, Edit, Glob, Grep; no Bash) writes `scenario.json`.
2. Mechanical checks (`scenario.build`). Failures go back to the writer by resuming its session.
3. Replica pre-checks (`preflight.check`). Failures go back the same way.
4. A cold reader, a fresh session for every version it reads. Its findings go back the same way.
Every version of `scenario.json`, every finding and every call is kept under RUN_DIR/<id>/. Accepted scenarios
are expanded into their suites under RUN_DIR/cases/<domain>/, listed in RUN_DIR/suite.json.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import threading
import time
import traceback
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

from grounding.runs.autogen_01.kit import agent, derive, preflight, reader, scenario

KIT = Path(__file__).resolve().parent
STUDY = KIT.parent
DOMAINS = STUDY.parent.parent / "domains"
WORK = Path(os.environ.get("AUTOGEN_WORK", "/tmp/autogen-5840209d/ws"))
DB = os.environ.get("DATABASE_URL", "postgresql://postgres@127.0.0.1:15432/agentdiff_campaign")
BASE = os.environ.get("AGENTDIFF_BASE_URL", "http://127.0.0.1:18001")
MAX_CHECK_ROUNDS = 6      # writer turns answering mechanical or replica findings
MAX_READER_ROUNDS = 2     # writer turns answering reader findings
LOCK = threading.Lock()


def setup_workspace(ws: Path, brief: dict):
    if ws.exists():
        shutil.rmtree(ws)
    (ws / "docs").mkdir(parents=True)
    (ws / "domain").mkdir()
    shutil.copytree(KIT / "examples", ws / "examples")
    for name in ("method.md", "format.md"):
        shutil.copy(KIT / "docs" / name, ws / "docs" / name)
    d = brief["domain"]
    for name in ("facts.json", "replica.md", "seed_ops.md", "api.md"):
        shutil.copy(STUDY / "inputs" / d / name, ws / "domain" / name)
    shutil.copy(DOMAINS / d / "model.md", ws / "domain" / "model.md")
    visible = {k: brief[k] for k in ("scenario_id", "domain", "facts")}  # never the exemplar it is compared with
    (ws / "brief.json").write_text(json.dumps(visible, indent=1) + "\n")


def first_prompt(brief: dict) -> str:
    facts = json.loads((STUDY / "inputs" / brief["domain"] / "facts.json").read_text())["facts"]
    entries = "\n".join(json.dumps(f, ensure_ascii=False) for f in facts if f["id"] in brief["facts"])
    return (f"Write scenario `{brief['scenario_id']}` for the {brief['domain']} domain (see brief.json).\n\n"
            f"Facts your scenario must test (each needs at least one decoy):\n{entries}\n\n"
            "Start by reading docs/method.md, docs/format.md and the two examples, then the domain files. "
            "Save the scenario as scenario.json in your working directory.")


def feedback(kind: str, problems: list[str]) -> str:
    items = "\n".join(f"- {p}" for p in problems)
    lead = {"checks": "The mechanical checks of scenario.json found these problems:",
            "replica": "The replica pre-checks found these problems:",
            "reader": "A cold reader, who saw only the request and then the records, reports:",
            "missing": "There is no valid scenario.json in your working directory:"}[kind]
    return (f"{lead}\n{items}\n\nFix scenario.json (edit it in place), then reply with a short summary of what you "
            "changed.")


def generate(brief: dict, run_dir: Path) -> dict:
    sid = brief["scenario_id"]
    out = run_dir / sid
    out.mkdir(parents=True, exist_ok=True)
    ws = WORK / run_dir.name / sid / "writer"
    setup_workspace(ws, brief)
    calls_log = run_dir / "calls.jsonl"
    history = []
    started = time.time()

    def writer(prompt, resume=None):
        return agent.run(agent.Call(role="writer", workspace=ws, prompt=prompt, log_dir=out / "writer",
                                    calls_log=calls_log, tools=agent.FILE_TOOLS, write=True,
                                    system_append=(KIT / "prompts" / "writer.md").read_text(), resume=resume,
                                    label=sid, timeout=3600))

    result = writer(first_prompt(brief))
    session = result["session_id"]
    check_rounds = reader_rounds = 0
    version = 0
    status, case = "rejected", None
    while True:
        version += 1
        path = ws / "scenario.json"
        try:
            s = json.loads(path.read_text())
            (out / f"scenario-v{version:02}.json").write_text(path.read_text())
        except (FileNotFoundError, ValueError) as exc:
            s = None
            problems, kind = [f"{type(exc).__name__}: {exc}"], "missing"
        if s is not None:
            case, problems = scenario.build(s, brief)
            kind = "checks"
            if not problems:
                report, problems = preflight.check(case, out / f"preflight-v{version:02}", DB, BASE)
                kind = "replica"
            if not problems:
                verdict = reader.read(case, WORK / run_dir.name / sid / f"reader-v{version:02}",
                                      out / f"reader-v{version:02}", calls_log, sid)
                (out / f"reader-v{version:02}" / "verdict.json").write_text(json.dumps(verdict, indent=1))
                problems = reader.problems(case, verdict)
                kind = "reader"
        history.append({"version": version, "stage": kind, "problems": problems})
        if not problems:
            status = "accepted"
            break
        if kind == "reader":
            reader_rounds += 1
            if reader_rounds > MAX_READER_ROUNDS:
                break
        else:
            check_rounds += 1
            if check_rounds > MAX_CHECK_ROUNDS:
                break
        result = writer(feedback(kind, problems), resume=session)
    outcome = {"scenario_id": sid, "domain": brief["domain"], "brief": brief, "status": status,
               "versions": version, "check_rounds": check_rounds, "reader_rounds": reader_rounds,
               "history": history, "seconds": round(time.time() - started),
               "finished_utc": datetime.now(timezone.utc).isoformat()}
    (out / "outcome.json").write_text(json.dumps(outcome, indent=1) + "\n")
    if status == "accepted":
        (out / "case.json").write_text(json.dumps(case, indent=1, ensure_ascii=False) + "\n")
        write_suite(case, run_dir)
    return outcome


def write_suite(case: dict, run_dir: Path):
    tests = derive.suite(case)
    with LOCK:
        index_path = run_dir / "suite.json"
        index = json.loads(index_path.read_text()) if index_path.exists() else []
        index = [t for t in index if t["scenario"] != case["case_id"]]
        for test, meta in tests:
            path = run_dir / "cases" / case["domain"] / f"{test['case_id']}.json"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(test, indent=1, ensure_ascii=False) + "\n")
            index.append({"case_id": test["case_id"], "domain": case["domain"], **meta})
        index_path.write_text(json.dumps(sorted(index, key=lambda t: t["case_id"]), indent=1) + "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--briefs", type=Path, required=True)
    parser.add_argument("--run", type=Path, required=True)
    parser.add_argument("--concurrency", type=int, default=4)
    parser.add_argument("--only", nargs="*")
    args = parser.parse_args()
    briefs = json.loads(args.briefs.read_text())
    if args.only:
        briefs = [b for b in briefs if b["scenario_id"] in args.only]
    run_dir = args.run.resolve()
    run_dir.mkdir(parents=True, exist_ok=True)
    snapshot = run_dir / "kit_snapshot"
    if not snapshot.exists():  # the prompts and docs this run used
        shutil.copytree(KIT / "prompts", snapshot / "prompts")
        shutil.copytree(KIT / "docs", snapshot / "docs")
    with ThreadPoolExecutor(max_workers=args.concurrency) as pool:
        futures = {pool.submit(generate, b, run_dir): b for b in briefs}
        for fut in as_completed(futures):
            b = futures[fut]
            try:
                o = fut.result()
                print(f"{o['scenario_id']}: {o['status']} after {o['versions']} versions "
                      f"({o['check_rounds']} check, {o['reader_rounds']} reader rounds, {o['seconds']}s)", flush=True)
            except Exception:
                err = traceback.format_exc()
                (run_dir / b["scenario_id"]).mkdir(parents=True, exist_ok=True)
                (run_dir / b["scenario_id"] / "error.txt").write_text(err)
                print(f"{b['scenario_id']}: ERROR {err.splitlines()[-1]}", flush=True)


if __name__ == "__main__":
    main()
