"""The evidence-only view for labelling the Sol round's blind trials: the request, the test's candidates (targets and
near misses with their facts, as the construction claims them), the solver's commands, responses and visible text,
its final answer and the state diff. No verdict, no mechanical triage, no label is read or printed.

Copied from blind_review_01/view.py (its --overview and --steps flags, its diff display), keyed by a trial key
(`<set>/<trial>/<case_id>`, as in eval/blind_<set>.json) instead of that study's manifest. The candidates block is
judge v2's own (`autogen_01.kit.bundle.candidates`), which reads only the case.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.sol_eval_01.kit.view KEY ... \
        [--overview] [--steps 3,5] [--seed] [--limit N] [--attempt attempt-01]
    python ... view --blind regular_p4 [--from N] [--to M]      # the blind sample's keys, in order, with index

--overview prints commands, the final answer and the diff only; --steps prints those steps' responses in full.
"""
from __future__ import annotations

import argparse
import ast
import json
from pathlib import Path

from grounding.runs.autogen_01.kit import bundle

STUDY = Path(__file__).resolve().parents[1]
RUNS = STUDY / "runs"


def attempt_dir(key: str, name: str | None = None) -> Path:
    run, trial, case_id = key.split("/")
    folder = RUNS / run / trial / case_id
    if name:
        return folder / name
    attempts = sorted(folder.glob("attempt-*"))
    if not attempts:
        raise SystemExit(f"{key}: no attempt yet")
    return attempts[-1]


def stdout_of(observation) -> str:
    """The command's output: OpenClaw records {'status': ..., 'stdout': ...} as a Python literal."""
    if isinstance(observation, dict):
        obs = observation
    else:
        try:
            obs = ast.literal_eval(str(observation))
        except (ValueError, SyntaxError):
            return str(observation)
    if isinstance(obs, dict):
        parts = [str(obs.get("stdout") or "")]
        if obs.get("stderr"):
            parts.append("STDERR: " + str(obs["stderr"]))
        if obs.get("status") not in (None, "success"):
            parts.append(f"STATUS: {obs.get('status')}")
        return "\n".join(p for p in parts if p)
    return str(obs)


def show(key: str, args) -> None:
    at = attempt_dir(key, args.attempt)
    case = json.loads((at / "case.json").read_text())
    summary = json.loads((at / "execution_summary.json").read_text())
    record = bundle.solver_record(at)
    print(f"\n===== {key} ({at.name}) =====")
    print(f"RUN: status={summary.get('status')} termination={summary.get('termination')} "
          f"turn_s={(summary.get('turn_durations_s') or [None])[0]} tool_calls={summary.get('turns')}"
          + (f" ERROR={summary.get('error')}" if summary.get("error") else ""))
    print("REQUEST:", case["prompt"])
    print("ACTOR:", case.get("acting_user_id"), "| CLOCK:", case.get("clock"))
    cand, _ = bundle.candidates(case)
    print("CANDIDATES (construction claims, to check against the evidence):\n" + cand)
    if args.seed:
        print("SEED:", json.dumps(case.get("seed"), ensure_ascii=False))
    selected = {int(n) for n in args.steps.split(",")} if args.steps else None
    for i, step in enumerate(record.get("steps", []), 1):
        if selected and i not in selected:
            continue
        text = (step.get("thinking") or "") + (step.get("text") or "")
        action = step.get("action") or ""
        if step.get("tool") is None and not action:
            continue  # the final reply, printed below
        print(f"STEP {i} [{step.get('tool')}]: {str(action)[:3000]}")
        if text.strip():
            print("  VISIBLE TEXT:", text.strip()[:2000])
        if args.overview:
            continue
        out = stdout_of(step.get("observation"))
        if step.get("tool") == "memory_search" and "belongs to agent main" in out:
            print("  RESPONSE: [memory_search unavailable: the agent database belongs to agent main (harness)]")
            continue
        if "SKILL.md" in str(action) or "/references/" in str(action):
            if not selected:
                print("  RESPONSE: [skill documentation, %d chars; --steps %d to read]" % (len(out), i))
                continue
        limit = None if selected else args.limit
        print("  RESPONSE:", out if limit is None or len(out) <= limit else
              out[:limit] + f" […{len(out) - limit} more chars; --steps {i}]")
    final = at / "solver" / "final_response.md"
    print("FINAL:", final.read_text().strip() if final.exists() else record.get("final"))
    diff_path = at / "environment" / "diff_run.json"
    if not diff_path.exists():
        print("DIFF: missing")
        return
    diff = json.loads(diff_path.read_text()).get("diff") or {}
    shown = 0
    for kind, rows in diff.items():
        for row in rows if isinstance(rows, list) else []:
            if kind == "inserts" and row.get("__table__") == "calendar_sync_tokens":
                continue
            shown += 1
            if kind == "updates":
                before, after = row.get("before", {}), row.get("after", {})
                changed = {k: [before.get(k), after.get(k)] for k in sorted(set(before) | set(after))
                           if before.get(k) != after.get(k)}
                ident = {k: v for k, v in after.items() if k == "id" or k.endswith("_id") or k == "ts"}
                print(f"DIFF {kind}: {row.get('__table__')} {json.dumps(ident, ensure_ascii=False)} "
                      f"changed {json.dumps(changed, ensure_ascii=False, default=str)[:1500]}")
            else:
                print(f"DIFF {kind}: {json.dumps(row, ensure_ascii=False, default=str)[:1500]}")
    if not shown:
        print("DIFF: no changes (calendar sync tokens aside)")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("keys", nargs="*")
    ap.add_argument("--blind", help="list a set's blind keys with their index")
    ap.add_argument("--from", dest="start", type=int, default=0)
    ap.add_argument("--to", type=int)
    ap.add_argument("--overview", action="store_true")
    ap.add_argument("--steps")
    ap.add_argument("--seed", action="store_true")
    ap.add_argument("--limit", type=int, default=2500)
    ap.add_argument("--attempt")
    args = ap.parse_args()
    if args.blind:
        keys = json.loads((STUDY / "eval" / f"blind_{args.blind}.json").read_text())["keys"]
        for i, k in enumerate(keys[args.start:args.to], args.start):
            print(i, k)
        return
    for key in args.keys:
        show(key, args)


if __name__ == "__main__":
    main()
