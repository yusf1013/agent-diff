"""Print the trials of a run compactly for labelling by hand: per case the request and the candidates, per trial the
write commands, the state diff, the final answer and the scorer's provisional outcome.

    python3 -m grounding.runs.autogen_02.kit.review RUN_DIR [--cases AT-BOX-21 ...] [--full CASE/TRIAL]

`--full t1/AT-BOX-21-I11` prints the whole judge bundle of one trial (every step and response).
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from grounding.runs.autogen_01.kit import bundle
from grounding.runs.autogen_01.kit import judge as v1
from grounding.runs.autogen_02.kit.judge2 import form_of, triage

WRITE = re.compile(r"-X\s*(POST|PUT|PATCH|DELETE)|--request\s+(POST|PUT|PATCH|DELETE)|\bmutation\b|"
                   r"chat\.(postMessage|update|delete)|reactions\.(add|remove)|conversations\.(setTopic|setPurpose|"
                   r"invite|kick|archive|rename|join|leave)|pins\.add|\s-d\s|--data", re.I)
NOISE = ("calendar_sync_tokens",)
UNFINISHED = {"solver_running", "preflight", "installing", "installed", "pending"}
READ = re.compile(r"\s-G\s(?!.*-X\s*(POST|PUT|PATCH|DELETE))")


def is_write(action: str) -> bool:
    if "graphql" in action:
        return bool(re.search(r"\bmutation\b", action))
    return bool(WRITE.search(action)) and not READ.search(action)


def trials(run_dir: Path, only: list[str] | None):
    for summary in sorted(run_dir.glob("t*/*/attempt-*/execution_summary.json")):
        attempt = summary.parent
        trial, case_id = attempt.parts[-3], attempt.parts[-2]
        if attempt != v1.latest(run_dir, trial, case_id):
            continue
        if only and not any(case_id.startswith(o) for o in only):
            continue
        if json.loads(summary.read_text()).get("status") in UNFINISHED:
            continue
        yield trial, case_id, attempt


def show(run_dir: Path, only: list[str] | None, brief: bool = False, skip: set | None = None):
    seen = set()
    rows = sorted((t for t in trials(run_dir, only) if f"{run_dir.name}/{t[0]}/{t[1]}" not in (skip or set())),
                  key=lambda t: (t[1], t[0]))
    for trial, case_id, attempt in rows:
        case, summary, tri = triage(run_dir.name, trial, attempt)
        if case_id not in seen:
            seen.add(case_id)
            cand, _ = bundle.candidates(case)
            print(f"\n{'#' * 100}\n## {case_id} ({case['domain']}; {form_of(case_id) or 'form ?'})\n"
                  f"REQUEST: {case['prompt']}\n{cand}")
        record = bundle.solver_record(attempt)
        steps = record.get("steps", [])
        limit = 220 if brief else 400
        writes = [f"  [{s.get('turn')}] {' '.join(str(s.get('action')).split())[:limit]}" for s in steps
                  if is_write(str(s.get("action") or ""))]
        final = ""
        if (attempt / "solver" / "final_response.md").exists():
            final = (attempt / "solver" / "final_response.md").read_text().strip()
        final = final or (record.get("final") or "")
        print(f"\n=== {case_id} {trial} [{summary.get('status')}/{record.get('termination') or summary.get('termination')}"
              f", {len(steps)} steps] provisional={tri['outcome']} exposed={tri['exposed']}")
        print("writes:\n" + ("\n".join(writes) if writes else "  (none)"))
        diff = bundle.diff_text(attempt).strip()
        if brief:
            diff = "\n".join(l for l in diff.splitlines() if not any(n in l for n in NOISE)).strip()
        print("diff: " + (diff[:600 if brief else 1200] if diff else "(none)"))
        final = " ".join(final.split()) if brief else final
        print("final: " + (final[:700 if brief else 1500] if final else "(none)"))


def full(run_dir: Path, key: str):
    trial, case_id = key.split("/")
    attempt = v1.latest(run_dir, trial, case_id)
    case, summary, tri = triage(run_dir.name, trial, attempt)
    print(bundle.build(case, attempt, form_of(case_id), tri, summary))


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("run_dir", type=Path)
    parser.add_argument("--cases", nargs="+")
    parser.add_argument("--full")
    parser.add_argument("--brief", action="store_true")
    parser.add_argument("--unlabelled", type=Path, help="a folder of label files: show only trials without a label")
    args = parser.parse_args()
    if args.full:
        full(args.run_dir.resolve(), args.full)
    else:
        skip = set()
        if args.unlabelled:
            for f in args.unlabelled.glob("*.json"):
                skip.update(k for k in json.loads(f.read_text()) if not k.startswith("_"))
        show(args.run_dir.resolve(), args.cases, args.brief, skip)


if __name__ == "__main__":
    main()
