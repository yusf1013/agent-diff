"""Cross the AgentDiff Slack suite's own assertion verdicts with the finalized hand labels.

Inputs (all in the repository, no model calls):
- grounding/reference_labels/slack/manifest.json and reports/: hand grounding labels of the latest saved run per case
  (59 cases, Claude Sonnet 5 via Bedrock, one trial each);
- the saved runs they bind to (grounding/runs/slack_baseline/...), which keep AgentDiff's own evaluation;
- grounding/domains/slack/analysis/analysis.json: per-obligation assertion coverage (yes / partial / no) and resolution.

Run from the repository root: python -m grounding.runs.related_work_01.pilot.slack_assertion_misses
Writes slack_assertion_misses.json next to this file.
"""
import collections
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).parent
LABELS = Path("grounding/reference_labels/slack")


def resolve(path):
    out = subprocess.run(["python", "-m", "grounding.paths", path], capture_output=True, text=True, check=True)
    return out.stdout.strip()


def main():
    analysis = {t["test_id"]: t for t in json.loads(Path("grounding/domains/slack/analysis/analysis.json").read_text())}
    manifest = json.loads((LABELS / "manifest.json").read_text())
    tests, obligations = [], []
    for case in manifest["cases"]:
        tid = case["test_id"]
        run = json.loads(Path(resolve(case["source_run"])).read_text())
        ev = run.get("evaluation") or {}
        report = json.loads((LABELS / case["report"]).read_text())
        models = sorted((run.get("usage") or {}).get("by_model", {}))
        labels = report["obligations"]
        tests.append({
            "test_id": tid, "assertions_passed": ev.get("passed"), "score": ev.get("score"),
            "termination": run.get("termination"), "models": models,
            "incorrect": sum(v == "demonstrated_incorrect" for v in labels.values()),
            "not_established": sum(v == "not_established" for v in labels.values()),
        })
        cards = analysis[tid]["obligations"]
        for key, label in labels.items():
            ob = cards[int(key) - 1]
            obligations.append({
                "test_id": tid, "obligation": int(key), "label": label,
                "assertion_coverage": ob["assertion_coverage"], "resolution": ob["card"]["Resolution"],
                "name": ob["card"]["Grounding obligation name"], "assertions_passed": ev.get("passed"),
            })
    failing = [t for t in tests if t["incorrect"]]
    summary = {
        "tests": len(tests),
        "solver_models": sorted({m for t in tests for m in t["models"]}),
        "tests_with_an_incorrect_obligation": len(failing),
        "of_those_assertions_passed": sum(bool(t["assertions_passed"]) for t in failing),
        "tests_failing_assertions_without_incorrect_obligation": sum(
            (t["assertions_passed"] is False) and not t["incorrect"] for t in tests),
        "obligations": len(obligations),
        "label_by_coverage": {f"{k[0]} / {k[1]}": v for k, v in sorted(collections.Counter(
            (o["label"], o["assertion_coverage"]) for o in obligations).items())},
        "incorrect_by_resolution": dict(collections.Counter(
            o["resolution"] for o in obligations if o["label"] == "demonstrated_incorrect")),
        "incorrect_in_assertion_passed_runs": sum(
            o["label"] == "demonstrated_incorrect" and bool(o["assertions_passed"]) for o in obligations),
    }
    out = {"summary": summary, "tests": tests,
           "not_correct": [o for o in obligations if o["label"] != "demonstrated_correct"]}
    (HERE / "slack_assertion_misses.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()
