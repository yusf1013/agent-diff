"""Show a baseline trial for hand labelling: request, the test author's expectation, the seed, the steps, the final
reply and the state changes. It never shows an assertion result or a judge verdict.

    python3 grounding/runs/baselines_01/label_view.py RUN_DIR CASE_ID [TRIAL ...] [--steps N] [--brief]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

WIDTH = 700


def short(value, n=WIDTH) -> str:
    text = value if isinstance(value, str) else json.dumps(value, ensure_ascii=False, default=str)
    return text if len(text) <= n else text[:n] + f" …(+{len(text) - n})"


def diff_lines(attempt: Path) -> list[str]:
    path = attempt / "environment" / "diff_run.json"
    if not path.exists():
        return ["(no diff recorded)"]
    diff = json.loads(path.read_text())["diff"]
    out = []
    skip = {"etag", "sequence_id", "modified_at", "updated_at", "updatedAt", "content_modified_at", "created_at"}
    for row in diff.get("inserts", []):
        out.append(f"+ {row.get('__table__')}: {short({k: v for k, v in row.items() if k != '__table__'}, 400)}")
    for row in diff.get("updates", []):
        before, after = row.get("before", {}), row.get("after", {})
        changed = {k: (before.get(k), after.get(k)) for k in after if before.get(k) != after.get(k) and k not in skip}
        ident = after.get("id") or after.get("channel_id") or after.get("message_id") or after.get("user_id")
        out.append(f"~ {row.get('__table__')} {ident}: {short(changed, 400)}")
    for row in diff.get("deletes", []):
        out.append(f"- {row.get('__table__')}: {short({k: v for k, v in row.items() if k != '__table__'}, 300)}")
    return out or ["(no changes)"]


def show(run_dir: Path, case_id: str, trial: str, steps: int, brief: bool = False) -> None:
    attempts = sorted((run_dir / trial / case_id).glob("attempt-*"))
    if not attempts:
        print(f"### {trial}/{case_id}: no attempt")
        return
    attempt = attempts[-1]
    summary = json.loads((attempt / "execution_summary.json").read_text())
    case = json.loads((attempt / "case.json").read_text())
    print(f"### {trial}/{case_id}  status={summary.get('status')} termination={summary.get('termination')} "
          f"attempts={len(attempts)}")
    record_path = next((p for p in sorted((attempt / "solver").glob("*.json")) if p.name != "config.json"), None)
    record = json.loads(record_path.read_text()) if record_path else {}
    for i, step in enumerate(record.get("steps", [])[:0 if brief else steps], 1):
        action = step.get("action") or step.get("arguments") or ""
        obs = step.get("observation")
        print(f"  [{i}] {short(action, 300)}")
        print(f"      -> {short(obs, 350)}")
    if not brief and len(record.get("steps", [])) > steps:
        print(f"  … {len(record['steps']) - steps} more steps")
    final = (attempt / "solver" / "final_response.md")
    print(f"  ({len(record.get('steps', []))} steps) REPLY:",
          short(final.read_text().strip() if final.exists() else record.get("final", ""), 500 if brief else 1500))
    for line in diff_lines(attempt):
        print("  DIFF", line)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    steps = int(sys.argv[sys.argv.index("--steps") + 1]) if "--steps" in sys.argv else 40
    if "--steps" in sys.argv:
        args.remove(str(steps))
    brief = "--brief" in sys.argv
    run_dir, case_id = Path(args[0]), args[1]
    trials = args[2:] or ["t1", "t2", "t3"]
    case = json.loads(next(run_dir.glob(f"t*/{case_id}/attempt-*/case.json")).read_text())
    base = case.get("baseline", {})
    print(f"## {case_id} ({case['domain']})")
    print("REQUEST:", case["prompt"])
    if base:
        print("EXPECTED:", base.get("expected"))
        if base.get("removed"):
            print("  REMOVED TARGET:", short(base["removed"], 300))
        for op in base.get("seed_ops", []):
            print("  SEED", short(op, 260))
    for ref in case.get("references", []):  # our own cases: the answer key, for labelling only
        print(f"  TARGET {ref.get('expected')}")
        for claim in ref.get("claims", []):
            print(f"  DECOY {claim.get('witness')} [{claim.get('requirement')} {claim.get('family')}]: "
                  f"{short(claim.get('explanation'), 300)}")
    if case.get("plain_twin"):
        print("  PLAIN TWIN:", case["plain_twin"]["note"])
    for trial in trials:
        show(run_dir, case_id, trial, steps, brief)


if __name__ == "__main__":
    main()
