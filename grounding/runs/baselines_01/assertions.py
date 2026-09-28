"""A baseline test's own oracle: its AgentDiff assertions, evaluated offline on each trial's recorded diff.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.baselines_01.assertions RUN_DIR [--out OUT.json]

The spec is the benchmark's: the test's assertions plus the benchmark suite's `ignore_fields` for the service
(`examples/<service>/testsuites/<service>_bench.json`), compiled and evaluated by the backend's own engine
(`backend/src/platform/evaluationEngine`) against `environment/diff_run.json`. A spec the engine rejects counts as a
failed test with the engine's error, as it would in the benchmark.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO / "backend"))

from src.platform.evaluationEngine.assertion import AssertionEngine  # noqa: E402
from src.platform.evaluationEngine.compiler import DSLCompiler  # noqa: E402

IGNORE = {d: json.loads((REPO / f"examples/{d}/testsuites/{d}_bench.json").read_text()).get("ignore_fields", {})
          for d in ("box", "calendar", "linear", "slack")}


def evaluate(attempt: Path) -> dict:
    case = json.loads((attempt / "case.json").read_text())
    spec = {"version": "0.1", "ignore_fields": IGNORE[case["domain"]],
            "assertions": case["baseline"]["assertions"]}
    diff_path = attempt / "environment" / "diff_run.json"
    if not diff_path.exists():
        return {"passed": None, "error": "no diff recorded"}
    diff = json.loads(diff_path.read_text())["diff"]
    try:
        compiled = DSLCompiler().compile(spec)
    except Exception as exc:
        return {"passed": False, "error": f"spec rejected: {type(exc).__name__}: {str(exc)[:500]}"}
    try:
        result = AssertionEngine(compiled).evaluate(diff)
    except Exception as exc:
        return {"passed": False, "error": f"evaluation failed: {type(exc).__name__}: {str(exc)[:500]}"}
    return {"passed": bool(result.get("passed")), "failures": result.get("failures", [])[:10],
            "score": result.get("score")}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("run_dir", type=Path)
    ap.add_argument("--out", type=Path)
    args = ap.parse_args()
    out = {}
    for summary in sorted(args.run_dir.resolve().glob("t*/*/attempt-*/execution_summary.json")):
        attempt = summary.parent
        key = "/".join(attempt.parts[-3:-1])
        latest = sorted(attempt.parent.glob("attempt-*"))[-1]
        if attempt != latest:
            continue
        out[key] = evaluate(attempt)
    text = json.dumps(out, indent=1, default=str)
    if args.out:
        args.out.write_text(text + "\n")
    print(json.dumps({"trials": len(out), "passed": sum(1 for v in out.values() if v.get("passed")),
                      "failed": sum(1 for v in out.values() if v.get("passed") is False)}, indent=1))


if __name__ == "__main__":
    main()
