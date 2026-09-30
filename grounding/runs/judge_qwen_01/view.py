"""Evidence-only view of a final execution, by key, for the manual adjudications.

    python grounding/runs/judge_qwen_01/view.py KEY [KEY ...] [--brief] [--steps 3,5] [--seed] [--no-thinking]

Adapted from blind_review_01/view.py, which is keyed by that review's sample ids. It shows the request, the test form
(the line the judges were given), the construction's references (targets and decoys, hypotheses to check against the
evidence), the solver's steps (reasoning, command, response), its final answer and the state diff.

It never shows a verdict, a reference label, the scorer's triage or the bundle's "Mechanical attribution" section:
it imports nothing that computes them, and reads only the attempt folder, plus the "Test form" line of the judges'
saved input.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
OC = HERE.parent / "openclaw_eval_01" / "runs"


def read(p: Path):
    return json.loads(p.read_text())


def compact(x) -> str:
    return json.dumps(x, ensure_ascii=False, separators=(",", ":"))


def locate(key: str) -> tuple[Path, str]:
    """The attempt folder judged for this key (the latest attempt, as the judges' selection took), and the form line."""
    run, trial, case_id = key.split("/")
    base = OC / run if run.startswith("full_") else OC / "policy" / run
    attempt = sorted((base / trial / case_id).glob("attempt-*"))[-1]
    judged = OC / f"judged_{run}" / key if run.startswith("full_") else \
        OC / "policy" / run.replace("solve_", "judged_", 1) / key
    form = "?"
    prompts = sorted(judged.glob("*-judge.prompt.md"))
    if prompts:
        form = next((line for line in prompts[-1].read_text().splitlines() if line.startswith("Test form:")), "?")
    return attempt, form


def show(key: str, args) -> None:
    at, form = locate(key)
    case = read(at / "case.json")
    records = [p for p in (at / "solver").glob("*.json") if p.name != "config.json"]
    solver = read(records[0]) if records else {}
    summary = read(at / "execution_summary.json")
    selected = {int(n) for n in args.steps.split(",")} if args.steps else None
    print(f"\n===== {key} ({case['domain']}), {at.name} =====")
    print(form)
    print("REQUEST:", case["prompt"])
    print("ACTOR:", case.get("acting_user_id"))
    for i, ref in enumerate(case["references"]):
        fields = ("name", "use", "description", "expected", "claims", "resolution", "written", "query")
        print(f"REFERENCE /references/{i}:", compact({k: ref.get(k) for k in fields}))
    if args.seed:
        print("FULL SEED:", compact(case.get("seed")))
    print("TERMINATION:", solver.get("termination"), "STATUS:", summary.get("status"),
          "ERROR:" if summary.get("error") else "", summary.get("error") or "")
    for i, step in enumerate(solver.get("steps", [])):
        if selected and i + 1 not in selected:
            continue
        thinking = step.get("thinking") or step.get("text") or ""
        if not thinking:
            thinking = " ".join(c.get("text", "") for c in (step.get("response") or {}).get("content", [])
                                if c.get("type") == "text")
        action = step.get("action") or compact(step.get("arguments"))
        print(f"STEP {i + 1} (/steps/{i}):", action)
        if thinking and not args.no_thinking:
            text = str(thinking)
            print("REASONING:", text[:600] + " [abridged]" if args.brief and not selected and len(text) > 600 else text)
        if not args.brief or selected:
            print("OBSERVATION:", compact(step.get("observation")))
    final = at / "solver" / "final_response.md"
    print("FINAL:", final.read_text() if final.exists() else solver.get("final"))
    dp = at / "environment" / "diff_run.json"
    if not dp.exists():
        print("DIFF: missing")
        return
    diff = read(dp).get("diff") or {}
    for cat, vals in diff.items():
        for i, item in enumerate(vals) if isinstance(vals, list) else []:
            if cat == "inserts" and item.get("__table__") == "calendar_sync_tokens":
                continue
            if cat == "updates":
                before, after = item.get("before", {}), item.get("after", {})
                changed = {k: [before.get(k), after.get(k)] for k in sorted(set(before) | set(after))
                           if before.get(k) != after.get(k)}
                ids = {k: v for k, v in after.items() if k == "id" or k.endswith("_id")}
                print(f"DIFF /diff/{cat}/{i}:", compact({"table": item.get("__table__"), "after_id": ids,
                                                          "changed": changed}))
            else:
                print(f"DIFF /diff/{cat}/{i}:", compact(item))
    if not any(diff.values()):
        print("DIFF: no changes")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("keys", nargs="+")
    ap.add_argument("--brief", action="store_true", help="abridged reasoning, no responses")
    ap.add_argument("--steps", help="comma-separated one-based steps, shown in full")
    ap.add_argument("--seed", action="store_true")
    ap.add_argument("--no-thinking", action="store_true")
    args = ap.parse_args()
    for key in args.keys:
        show(key, args)


if __name__ == "__main__":
    main()
