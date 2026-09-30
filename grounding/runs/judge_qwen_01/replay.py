"""Replay judge v2 on Qwen: Muse's saved system and user text, the same output schema, the Qwen backend.

    L="python grounding/runs/fact_coverage_02/launch.py"
    $L grounding.runs.judge_qwen_01.replay select                      # sets/labelled.json, sets/all.json
    SOLVER_BACKEND=selfhost $L grounding.runs.judge_qwen_01.replay run --set labelled --out runs/selfhost \
        [--concurrency 16] [--keys KEY ...] [--limit N]

`select` writes the key lists: `all` is every final execution with a Muse verdict (2,139); `labelled` is those of
them with a reference label (the lead's 310 retained blind labels and blind_review_01's 133 with a Muse verdict).
Selection reads only which keys have a label, never a label's content, and `run` reads only the key lists.

`run` sends each execution's saved text (common.muse_prompt) through backend.run, and writes
`<out>/<run>/<trial>/<case_id>/verdict.json`, as judge2 does: the answer, plus the fields judge2 adds, copied from
Muse's verdict (they depend only on the execution). An execution with a verdict is skipped, so a run can resume.
"""
from __future__ import annotations

import argparse
import json
import random
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from grounding.runs.autogen_01.kit import agent
from grounding.runs.autogen_01.kit import judge as v1
from grounding.runs.judge_qwen_01 import backend
from grounding.runs.judge_qwen_01.common import HERE, attempt_path, judged_keys, labels, muse_prompt, muse_verdict

SETS = HERE / "sets"
COPIED = ("provisional", "provisional_exposed", "form", "targets", "kind")


def select():
    SETS.mkdir(exist_ok=True)
    everything = judged_keys()
    ref = labels()
    labelled = [k for k in everything if k in ref and (ref[k]["source"] == "lead" or ref[k]["has_llm"])]
    for name, keys in (("all", everything), ("labelled", labelled)):
        (SETS / f"{name}.json").write_text(json.dumps(keys, indent=1) + "\n")
        print(name, len(keys))


def judge_one(key: str, out: Path, calls_log: Path) -> dict:
    dest = out / key
    verdict_path = dest / "verdict.json"
    if verdict_path.exists():
        return json.loads(verdict_path.read_text())
    system, user = muse_prompt(key)
    muse = muse_verdict(key)
    result = backend.run(agent.Call(
        role="judge", workspace=Path("/tmp/judge-qwen-01/ws") / key.replace("/", "-"), prompt=user, log_dir=dest,
        calls_log=calls_log, tools=[], schema=v1.SCHEMA, system_append=system, label=key))
    verdict = agent.structured(result) or {}
    verdict.update(key=key, attempt=str(attempt_path(key)), muse_attempt=muse["attempt"],
                   **{k: muse.get(k) for k in COPIED}, judge="v2", backend=result.get("backend"),
                   model=result.get("model"), system_fingerprint=result.get("system_fingerprint"))
    verdict_path.write_text(json.dumps(verdict, indent=1, ensure_ascii=False) + "\n")
    return verdict


def run(keys: list[str], out: Path, concurrency: int):
    out.mkdir(parents=True, exist_ok=True)
    plan = out / "plan.json"
    if not plan.exists():
        plan.write_text(json.dumps({"settings": backend.settings(), "concurrency": concurrency,
                                    "schema": agent._strict_schema(v1.SCHEMA)}, indent=1) + "\n")
    calls_log = out / "calls.jsonl"
    todo = [k for k in keys if not (out / k / "verdict.json").exists()]
    random.Random(20260930).shuffle(todo)  # mix kinds and domains across the run
    print(f"{len(keys)} keys, {len(keys) - len(todo)} already judged, {len(todo)} to judge", flush=True)
    done = 0
    with ThreadPoolExecutor(max_workers=concurrency) as pool:
        futures = {pool.submit(judge_one, k, out, calls_log): k for k in todo}
        for fut in as_completed(futures):
            key = futures[fut]
            done += 1
            try:
                v = fut.result()
                print(f"[{done}/{len(todo)}] {key}: {v.get('outcome')} {v.get('exposed')}", flush=True)
            except Exception as exc:  # recorded in the attempt's failed.json; the execution stays unjudged
                print(f"[{done}/{len(todo)}] {key}: FAILED {exc}", flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("select")
    r = sub.add_parser("run")
    r.add_argument("--set", choices=["labelled", "all"])
    r.add_argument("--keys", nargs="+")
    r.add_argument("--out", type=Path, required=True)
    r.add_argument("--concurrency", type=int, default=16)
    r.add_argument("--limit", type=int)
    args = parser.parse_args()
    if args.cmd == "select":
        select()
        return
    keys = args.keys or json.loads((SETS / f"{args.set}.json").read_text())
    out = args.out if args.out.is_absolute() else HERE / args.out
    run(keys[:args.limit] if args.limit else keys, out, args.concurrency)


if __name__ == "__main__":
    sys.exit(main())
