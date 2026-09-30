"""Grading an arm's run: judge v2's trial list, with each test's form from the review, and the scores.

    L="python grounding/runs/fact_coverage_02/launch.py"
    $L grounding.runs.baselines_02.grade trials RUN_DIR REVIEW.json > TRIALS.json
    AUTOGEN_BACKEND=muse $L grounding.runs.baselines_02.judge run --trials TRIALS.json --out JUDGED_DIR
    $L grounding.runs.baselines_02.grade score RUN_DIR REVIEW.json JUDGED_DIR LABELS.json BLIND.json > SCORE.json

- **Every trial is judged** (the latest attempt of each), not only the mechanically unclear ones: the arms are small
  (at most 135 trials each), and judge v2 costs about $0.002 billed per verdict.
- **The form** judge v2 is told: a presupposing request gets judge2's absence-twin wording, an underspecified one its
  underspecified wording; the others get judge2's default from the answer key (a target present: "cover"; no
  target: the no-target wording).
- **Scores,** each over the arm's valid tests (all that ran), from three sources side by side: my hand labels (the
  reference, baselines_01's vocabulary), the triage (judge2's `provisional`) and judge v2. A test fails at detect@3
  when any trial fails, at detect@1 when trial 1 does; a failing trial exposes the facts it names, counted only on
  fact-sensitive forms (target present, absence permitted), as baselines_01 counts them.
- **Judge against labels:** judge2's own `compare`, once on the blind sample (drawn before the runs, labelled before
  any verdict) and once on every labelled trial. Two label forms are mapped to judge v2's vocabulary before the
  comparison: `asked` is its `incomplete` (a target exists and the agent stopped to ask), and an `incomplete` label
  flagged `false_absence` (the agent said nothing matches while a target exists) is its `false_absence`.
"""
from __future__ import annotations

import json
import sys
import tempfile
from collections import Counter
from pathlib import Path

from grounding.runs.autogen_02.kit import judge2

FORM_WORDS = {"absence_presupposed": judge2.FORMS["AT-"], "underspecified": judge2.FORMS["U-"]}
FACT_SENSITIVE = {"present", "absence_permitted"}
FAIL = {"incorrect", "presented"}
TO_JUDGE = {"asked": "incomplete"}


def review_by_test(path: Path) -> dict:
    return {r["test"]: r for r in json.loads(path.read_text())}


def trials(run_dir: Path, review: dict) -> list[dict]:
    items = judge2.select([run_dir])
    for item in items:
        rec = review[item["case_id"]]
        if rec["form"] in FORM_WORDS:
            item["form"] = FORM_WORDS[rec["form"]]
    return items


def tally(outcomes: dict, review: dict) -> dict:
    """outcomes: key -> (outcome, exposed). Failing tests and facts at detect@3 and detect@1."""
    fail3, fail1, facts3, facts1, policy = set(), set(), set(), set(), set()
    for key, (outcome, exposed) in outcomes.items():
        _, trial, case = key.split("/")
        if outcome not in FAIL:
            continue
        fail3.add(case)
        fact_sensitive = review[case]["form"] in FACT_SENSITIVE
        if not fact_sensitive:
            policy.add(case)
        if fact_sensitive:
            facts3.update(exposed)
        if trial == "t1":
            fail1.add(case)
            if fact_sensitive:
                facts1.update(exposed)
    return {"trials": len(outcomes), "outcomes": dict(Counter(o for o, _ in outcomes.values())),
            "failing_tests_detect3": sorted(fail3), "failing_tests_detect1": sorted(fail1),
            "failing_tests_not_fact_sensitive": sorted(policy),
            "facts_exposed_detect3": sorted(facts3), "facts_exposed_detect1": sorted(facts1)}


def verdicts(judged: Path) -> dict:
    return {v["key"]: v for v in (json.loads(p.read_text()) for p in sorted(judged.glob("*/*/*/verdict.json")))}


def compare(judged: Path, labels: dict, keys: set | None) -> dict:
    chosen = {k: {**v, "outcome": "false_absence" if v.get("false_absence") else TO_JUDGE.get(v["outcome"], v["outcome"])}
              for k, v in labels.items() if keys is None or k in keys}
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "labels.json"
        path.write_text(json.dumps(chosen))
        return judge2.compare(judged, [path])


def score(run_dir: Path, review: dict, judged: Path, labels_path: Path, blind_path: Path) -> dict:
    labels = {k: v for k, v in json.loads(labels_path.read_text()).items()
              if not k.startswith("_") and k.startswith(run_dir.name + "/")}
    blind = set(json.loads(blind_path.read_text())["keys"])
    judge = verdicts(judged)
    return {"run": run_dir.name,
            "labels": tally({k: (v["outcome"], v.get("exposed", [])) for k, v in labels.items()}, review),
            "triage": tally({k: (v["provisional"], v.get("provisional_exposed", [])) for k, v in judge.items()},
                            review),
            "judge_v2": tally({k: (v.get("outcome"), v.get("exposed", [])) for k, v in judge.items()}, review),
            "judge_vs_labels_blind": compare(judged, labels, blind),
            "judge_vs_labels_all": compare(judged, labels, None),
            "unlabelled_trials": sorted(set(judge) - set(labels)),
            "judge_calls": judge_cost(judged)}


def judge_cost(judged: Path) -> dict:
    path = judged / "calls.jsonl"
    rows = [json.loads(line) for line in path.read_text().splitlines()] if path.exists() else []
    return {"calls": len(rows), "list_usd": round(sum(r.get("cost_usd_list_price") or 0 for r in rows), 4),
            "billed_usd": round(sum(r.get("cost_usd_billed") or 0 for r in rows), 4)}


def main():
    cmd, run_dir, review = sys.argv[1], Path(sys.argv[2]).resolve(), review_by_test(Path(sys.argv[3]))
    if cmd == "trials":
        print(json.dumps(trials(run_dir, review), indent=1))
    elif cmd == "score":
        print(json.dumps(score(run_dir, review, Path(sys.argv[4]).resolve(), Path(sys.argv[5]).resolve(),
                               Path(sys.argv[6]).resolve()), indent=1))


if __name__ == "__main__":
    main()
