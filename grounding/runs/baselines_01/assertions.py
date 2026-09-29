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
# --faithful: what n0/inputs/*/format.md told the baselines, which the engine does not do. (1) It listed an "unchanged"
# diff type, which the engine's schema rejects (its README lists it); here it becomes "changed" with a count of 0, what
# the tests mean by it ("this record stays as it is"), whatever count they gave. (2) It said timestamps "and similar bookkeeping columns" are ignored; the benchmark's lists miss
# some that change on every write, added here.
BOOKKEEPING = {"box": ["path", "modified_by_id"], "calendar": [],
               "linear": ["priorityLabel", "prioritySortOrder", "sortOrder"], "slack": []}


def faithful_spec(domain: str, assertions: list) -> dict:
    fixed = []
    for a in assertions:
        a = dict(a)
        if a.get("diff_type") == "unchanged":
            a["diff_type"], a["expected_count"] = "changed", 0
        fixed.append(a)
    ignore = json.loads(json.dumps(IGNORE[domain]))
    ignore["global"] = list(dict.fromkeys(list(ignore.get("global", [])) + BOOKKEEPING[domain]))
    return {"version": "0.1", "ignore_fields": ignore, "assertions": fixed}


def evaluate(attempt: Path, faithful: bool = False) -> dict:
    case = json.loads((attempt / "case.json").read_text())
    spec = faithful_spec(case["domain"], case["baseline"]["assertions"]) if faithful else {
        "version": "0.1", "ignore_fields": IGNORE[case["domain"]], "assertions": case["baseline"]["assertions"]}
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
    ap.add_argument("--faithful", action="store_true", help="evaluate as format.md described (see BOOKKEEPING)")
    args = ap.parse_args()
    out = {}
    for summary in sorted(args.run_dir.resolve().glob("t*/*/attempt-*/execution_summary.json")):
        attempt = summary.parent
        key = "/".join(attempt.parts[-3:-1])
        latest = sorted(attempt.parent.glob("attempt-*"))[-1]
        if attempt != latest:
            continue
        out[key] = evaluate(attempt, args.faithful)
    text = json.dumps(out, indent=1, default=str)
    if args.out:
        args.out.write_text(text + "\n")
    print(json.dumps({"trials": len(out), "passed": sum(1 for v in out.values() if v.get("passed")),
                      "failed": sum(1 for v in out.values() if v.get("passed") is False)}, indent=1))


if __name__ == "__main__":
    main()
