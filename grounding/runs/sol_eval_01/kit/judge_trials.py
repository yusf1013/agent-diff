"""The trials judge v2 judges in a Sol set, written to a file without printing any mechanical outcome (the blind
sample is labelled by hand while the judge runs).

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.sol_eval_01.kit.judge_trials SET [--add-retried]

- **Regular sets** use autogen_02's `phase4 select` unchanged (`judge.select_run` with judge2's triage: every trial
  that is not mechanically clean, 20% of the clean ones, seed 7) plus every trial of the blind sample, as the Qwen
  round did.
- **Policy sets** use judge2's `select`: every trial.
- **Left out for now:** every trial whose attempt ended in an infrastructure error or a provider stall, selected or
  not. The retry pass re-runs them. `--add-retried` then adds each of them with its new attempt, whatever its triage,
  so the first draw of clean trials stays as it was.

Writes eval/judge_<SET>.trials.json (the list judge2 `run` reads) and eval/judge_<SET>.selection.json (counts and the
trials left out, no outcomes).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from grounding.runs.autogen_01.kit import judge as v1
from grounding.runs.autogen_02.kit import judge2, phase4  # noqa: F401  (phase4 patches v1.triage with judge2's)
from grounding.runs.sol_eval_01.kit.score import stalled

STUDY = Path(__file__).resolve().parents[1]
EVAL = STUDY / "eval"


def ended_badly(attempt: Path) -> str | None:
    s = json.loads((attempt / "execution_summary.json").read_text())
    if s.get("status") != "completed":
        return f"{s.get('status')}: {s.get('error')}"
    if stalled(attempt):
        return "provider stall (runtime rule R3)"
    return None


def select(name: str) -> list[dict]:
    run_dir = (STUDY / "runs" / name).resolve()
    if name.startswith("regular"):
        items = v1.select_run(run_dir, (STUDY / "cases" / name / "suite.json").resolve())
        have = {f"{i['run']}/{i['trial']}/{i['case_id']}" for i in items}
        for key in json.loads((EVAL / f"blind_{name}.json").read_text())["keys"]:
            run, trial, case_id = key.split("/")
            if key not in have and (run_dir / trial / case_id).exists():
                items.append({"run_dir": str(run_dir), "run": run, "trial": trial, "case_id": case_id,
                              "blind_sample": True})
        for i in items:
            i.pop("provisional", None)  # the file names no outcome
        return items
    return judge2.select([run_dir])


def main():
    name = sys.argv[1]
    run_dir = (STUDY / "runs" / name).resolve()
    trials_path, record_path = EVAL / f"judge_{name}.trials.json", EVAL / f"judge_{name}.selection.json"
    if "--add-retried" in sys.argv:
        items = json.loads(trials_path.read_text())
        record = json.loads(record_path.read_text())
        first = {f"{i['trial']}/{i['case_id']}": i.get("attempt_at_selection") for i in items}
        added = []
        for summary in sorted(run_dir.glob("t*/*/attempt-*/execution_summary.json")):
            attempt = summary.parent
            trial, case_id = attempt.parts[-3], attempt.parts[-2]
            if attempt != v1.latest(run_dir, trial, case_id):
                continue
            key = f"{trial}/{case_id}"
            was_left_out = key in record["left_out"]
            if (key in first and first[key] != attempt.name) or was_left_out:
                if ended_badly(attempt):
                    continue
                if key not in first:
                    items.append({"run_dir": str(run_dir), "run": name, "trial": trial, "case_id": case_id,
                                  "retried": True, "attempt_at_selection": attempt.name})
                added.append(key)
                record["left_out"].pop(key, None)
        record.setdefault("added_after_retries", []).extend(added)
        trials_path.write_text(json.dumps(items, indent=1) + "\n")
        record_path.write_text(json.dumps(record, indent=1) + "\n")
        print(f"{name}: {len(added)} retried trials added or re-judged; {len(record['left_out'])} still left out")
        return
    if trials_path.exists():
        raise SystemExit(f"{trials_path} exists: the selection is drawn once (use --add-retried after the retries)")
    items, left_out = [], {}
    for item in select(name):
        attempt = v1.latest(Path(item["run_dir"]), item["trial"], item["case_id"])
        if ended_badly(attempt):
            continue
        items.append({**item, "attempt_at_selection": attempt.name})
    # Every trial that ended badly, selected or not: the retry pass re-runs them all, and --add-retried judges them.
    for summary in sorted(run_dir.glob("t*/*/attempt-*/execution_summary.json")):
        attempt = summary.parent
        trial, case_id = attempt.parts[-3], attempt.parts[-2]
        if attempt == v1.latest(run_dir, trial, case_id) and ended_badly(attempt):
            left_out[f"{trial}/{case_id}"] = ended_badly(attempt)
    trials_path.write_text(json.dumps(items, indent=1) + "\n")
    record = {"set": name, "to_judge": len(items),
              "blind_added": sum(1 for i in items if i.get("blind_sample")),
              "clean_sample": sum(1 for i in items if i.get("clean_sample")), "left_out": left_out}
    record_path.write_text(json.dumps(record, indent=1) + "\n")
    print({k: (len(v) if isinstance(v, dict) else v) for k, v in record.items()})


if __name__ == "__main__":
    main()
