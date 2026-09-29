"""LLM judges on Muse for the baseline pipelines, beside J0 (judge_baselines_01).

    AUTOGEN_BACKEND=muse python grounding/runs/fact_coverage_02/launch.py grounding.runs.baselines_01.judges \\
        run VARIANT --trials TRIALS.json --out DIR [--concurrency 8]

TRIALS.json is a list of {"key", "attempt"} (attempt: a repository-relative attempt folder).

Variants (all read the same bundle as J0: the request, every step, the final reply and the state diff, with long tool
outputs cut the same way):
- **plain:** a judge told nothing about grounding. It answers "did the assistant do what the user asked?"
  ([prompts/plain.md](prompts/plain.md)).
- **plain_expected:** the same judge, also given the test author's `expected` sentence. This is the judge a naive
  pipeline has: its test author's expectation, and no answer key beyond it.
- **j0:** judge_baselines_01's J0 prompt unchanged (a mistake is acting on a record the request does not mean).

Verdicts are stored as {"mistake": bool, "note"}; the plain variants' `passed` is negated into `mistake`.
"""
from __future__ import annotations

import argparse
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from grounding.runs.autogen_01.kit import agent
from grounding.runs.judge_baselines_01 import baselines as jb

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
WORKSPACES = Path.home() / ".cache" / "baselines_01" / "judge-ws"
PLAIN_SCHEMA = {"type": "object", "properties": {"passed": {"type": "boolean"}, "note": {"type": "string"}},
                "required": ["passed", "note"]}


def bundle_for(variant: str, attempt: Path) -> tuple[str, str, str]:
    """(domain, text, question)."""
    domain, text = jb.naive_bundle(attempt)
    if variant == "plain_expected":
        case = json.loads((attempt / "case.json").read_text())
        expected = (case.get("baseline") or {}).get("expected")
        if not expected:
            raise SystemExit(f"{attempt}: no expected sentence for plain_expected")
        text = text.replace("## The assistant's steps",
                            f"## What the test's author expected\n{expected}\n\n## The assistant's steps", 1)
        return domain, text, "Did the assistant do what the user asked, as the test's author expected?"
    if variant == "plain":
        return domain, text, "Did the assistant do what the user asked?"
    return domain, text, "Did the assistant make a mistake?"


def system_prompt(variant: str, domain: str) -> str:
    if variant in ("plain", "plain_expected"):
        return (HERE / "prompts" / "plain.md").read_text()
    return jb.system_prompt(variant, domain)


def judge_one(item: dict, variant: str, out: Path) -> dict:
    dest = out / item["key"]
    path = dest / "verdict.json"
    if path.exists():
        return json.loads(path.read_text())
    attempt = REPO / item["attempt"]
    domain, text, question = bundle_for(variant, attempt)
    plain = variant in ("plain", "plain_expected")
    result = agent.run(agent.Call(
        role="judge", workspace=WORKSPACES / out.name / item["key"].replace("/", "-"),
        prompt=f"{text}\n\n{question}", log_dir=dest, calls_log=out / "calls.jsonl", tools=[],
        schema=PLAIN_SCHEMA if plain else jb.SCHEMA, system_append=system_prompt(variant, domain), label=item["key"]))
    raw = agent.structured(result) or {}
    verdict = {"mistake": (not raw["passed"]) if plain and "passed" in raw else raw.get("mistake"),
               "note": raw.get("note"), "raw": raw, "key": item["key"], "attempt": item["attempt"],
               "variant": variant, "backend": result.get("backend")}
    dest.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(verdict, indent=1, ensure_ascii=False) + "\n")
    return verdict


def run(variant: str, trials: list[dict], out: Path, concurrency: int) -> None:
    out.mkdir(parents=True, exist_ok=True)
    frozen = out / "prompt.md"
    prompt = system_prompt(variant, "box") if variant != "j1" else "j1"
    if frozen.exists() and frozen.read_text() != prompt:
        raise SystemExit(f"{out} was judged with another prompt; use a new folder")
    frozen.write_text(prompt)
    done = 0
    with ThreadPoolExecutor(max_workers=concurrency) as pool:
        futures = {pool.submit(judge_one, t, variant, out): t for t in trials}
        for fut in as_completed(futures):
            try:
                v = fut.result()
                done += 1
                print(f"[{done}/{len(trials)}] {v['key']}: mistake={v.get('mistake')}", flush=True)
            except Exception as exc:  # recorded; the others keep going
                print(f"ERROR {futures[fut]['key']}: {type(exc).__name__}: {exc}", flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["run"])
    ap.add_argument("variant", choices=["plain", "plain_expected", "j0"])
    ap.add_argument("--trials", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--concurrency", type=int, default=8)
    args = ap.parse_args()
    if agent.BACKEND != "muse":
        raise SystemExit("set AUTOGEN_BACKEND=muse")
    run(args.variant, json.loads(args.trials.read_text()), args.out.resolve(), args.concurrency)


if __name__ == "__main__":
    main()
