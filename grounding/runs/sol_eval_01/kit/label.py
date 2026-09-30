"""Record my manual label for one blind trial of the Sol round, before any verdict on it exists or is read.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.sol_eval_01.kit.label KEY OUTCOME \
        [--exposed F ...] [--acted ID ...] [--mechanism M] --note "..." [--kind initial|adjudication|correction]

Writes eval/labels_<set>/<set>_blind.json (initial labels), `..._adjudications.json` or `..._corrections.json`, as
openclaw_eval_01/eval/labels_* and blind_review_01 keep them apart. An initial label is written once: a later change
goes to the corrections file with its reason, and the initial label stays. Each label records the attempt folder it
was written on (a retry may later supersede it). The outcome vocabulary is judge v2's (autogen_02/kit/prompts/
judge_v2.md). This script reads no verdict and no mechanical triage.
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

from grounding.runs.sol_eval_01.kit.view import attempt_dir

STUDY = Path(__file__).resolve().parents[1]
OUTCOMES = ("incorrect", "presented", "correct", "correct_absent", "false_absence", "incomplete", "not_established",
            "artifact")
MECHANISMS = ("skipped-check", "saw-mismatch-accepted", "misread", "none")
ABOUT = ("My labels (manual, session sol_score) for the blind sample of {set} (eval/blind_{set}.json, drawn before "
         "the run from the cases folder alone). Each trial is labelled from its evidence only (kit/view.py: request, "
         "candidates, commands, responses, final answer, diff), before any judge verdict on it is read, with judge "
         "v2's outcome definitions. Sol's reasoning is not recorded, so a mechanism rests on the final answer and on "
         "what the responses showed.")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("key")
    ap.add_argument("outcome", choices=OUTCOMES)
    ap.add_argument("--exposed", nargs="*", default=[])
    ap.add_argument("--acted", nargs="*", default=[])
    ap.add_argument("--mechanism", choices=MECHANISMS, default="none")
    ap.add_argument("--note", required=True)
    ap.add_argument("--kind", choices=("initial", "adjudication", "correction"), default="initial")
    ap.add_argument("--attempt", help="the attempt folder, when not the latest")
    args = ap.parse_args()
    run = args.key.split("/")[0]
    folder = STUDY / "eval" / f"labels_{run}"
    folder.mkdir(parents=True, exist_ok=True)
    name = {"initial": f"{run}_blind.json", "adjudication": f"{run}_adjudications.json",
            "correction": f"{run}_corrections.json"}[args.kind]
    path = folder / name
    doc = json.loads(path.read_text()) if path.exists() else {"_about": ABOUT.format(set=run) if args.kind == "initial"
                                                              else f"{args.kind}s of my blind labels for {run}; the "
                                                                   f"initial labels stay in {run}_blind.json"}
    blind = json.loads((STUDY / "eval" / f"blind_{run}.json").read_text())["keys"]
    if args.key not in blind:
        raise SystemExit(f"{args.key} is not in the blind sample")
    if args.kind == "initial" and args.key in doc:
        raise SystemExit(f"{args.key} already has an initial label; record a correction instead")
    attempt = attempt_dir(args.key, args.attempt)
    summary = json.loads((attempt / "execution_summary.json").read_text())
    if summary.get("status") != "completed" and args.outcome != "not_established":
        raise SystemExit(f"{args.key}: attempt {attempt.name} is {summary.get('status')}")
    doc[args.key] = {"outcome": args.outcome, "exposed": sorted(args.exposed), "acted_on": args.acted,
                     "mechanism": args.mechanism, "note": args.note, "attempt": attempt.name,
                     "labelled_utc": datetime.now(timezone.utc).isoformat(timespec="seconds")}
    path.write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n")
    n = sum(1 for k in doc if not k.startswith("_"))
    print(f"{args.kind} {args.key}: {args.outcome} {sorted(args.exposed)} ({n} in {path.name})")


if __name__ == "__main__":
    main()
