"""Per-test outcomes and yields of a generated suite's solver run, from the judge's verdicts.

    python -m grounding.runs.autogen_01.kit.score_run --solver-run DIR --suite SUITE.json --judged JUDGE_DIR [--json OUT]

A trial's outcome is the judge's verdict when it was judged, else the scorer's provisional label (only mechanically
clean trials go unjudged). A test exposes a fact when at least one established trial fails on that fact's decoy
(detect@3); detect@1 uses trial 1 only. Artifact and not-established trials do not count.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

from grounding.runs.autogen_01.kit.judge import COLLAPSE, latest, scored_exposed, triage

RUNS_ROOT = Path(__file__).resolve().parents[2]  # this repository's grounding/runs/
MARKER = "/grounding/runs/"


def same_attempt(recorded: str | None, attempt: Path) -> bool:
    """Whether a verdict's recorded attempt is this attempt: the same path from grounding/runs/ on, whichever checkout
    the judge ran in. (Until 2026-09-30 a plain string comparison: scored from another checkout than the judge's,
    every judged trial fell back to its triage.)"""
    if not recorded:
        return False
    return recorded == str(attempt) or (MARKER in recorded and
                                        recorded.split(MARKER, 1)[1] == str(attempt).split(MARKER, 1)[-1])


def attempt_found(recorded: str | None) -> bool:
    """The recorded attempt exists here, where recorded or re-rooted at this repository's grounding/runs/ (as
    openclaw_eval_01/policy.py's local_attempt resolves it)."""
    if not recorded:
        return False
    return Path(recorded).exists() or (MARKER in recorded and (RUNS_ROOT / recorded.split(MARKER, 1)[1]).exists())


def warn_unresolved(verdicts: list[Path]) -> None:
    """Loudly, on stderr: verdicts whose attempt cannot be found, so they count only if their path from
    grounding/runs/ on matches the scored attempt."""
    print(f"\n*** WARNING (autogen_01/kit/score_run.py): {len(verdicts)} verdicts name an attempt that cannot be found, "
          f"where recorded or re-rooted under {RUNS_ROOT}; each counts only if its path from grounding/runs/ on is the "
          f"scored attempt's, else its trial falls back to the triage. ***", file=sys.stderr)
    print(f"***   for example {verdicts[0]}\n", file=sys.stderr)


def trial_outcomes(solver_run: Path, judged: Path) -> dict:
    out, unresolved = {}, []
    for summary in sorted(solver_run.glob("t*/*/attempt-*/execution_summary.json")):
        attempt = summary.parent
        trial, case_id = attempt.parts[-3], attempt.parts[-2]
        if attempt != latest(solver_run, trial, case_id):
            continue
        verdict_path = judged / solver_run.name / trial / case_id / "verdict.json"
        v = json.loads(verdict_path.read_text()) if verdict_path.exists() else None
        if v is not None and not attempt_found(v.get("attempt")):
            unresolved.append(verdict_path)
        if v is not None and same_attempt(v.get("attempt"), attempt):  # a verdict on an older attempt does not count
            out[(case_id, trial)] = {"outcome": v["outcome"], "exposed": scored_exposed(v), "judged": True,
                                     "mechanism": v.get("mechanism"), "note": v.get("note")}
        else:
            _, _, tri = triage(solver_run.name, trial, attempt)
            out[(case_id, trial)] = {"outcome": tri["outcome"], "exposed": tri["exposed"] if COLLAPSE.get(
                tri["outcome"]) == "fail" else [], "judged": False}
    if unresolved:
        warn_unresolved(unresolved)
    return out


def contestable_facts(case_path: Path) -> set:
    """Facts whose every decoy in this test was marked contestable by the reader (reported with an asterisk)."""
    if not case_path.exists():
        return set()
    case = json.loads(case_path.read_text())
    by_fact = defaultdict(list)
    for ref in case["references"]:
        for c in ref["claims"]:
            by_fact[c["requirement"]].append(bool(c.get("contestable")))
    return {f for f, flags in by_fact.items() if flags and all(flags)}


def score(solver_run: Path, suite: Path, judged: Path) -> dict:
    meta = {t["case_id"]: t for t in json.loads(suite.read_text())}
    cases_dir = suite.parent / "cases"
    trials = trial_outcomes(solver_run, judged)
    tests = {}
    for (case_id, trial), r in trials.items():
        t = tests.setdefault(case_id, {**meta.get(case_id, {"case_id": case_id}), "trials": {}})
        t["trials"][trial] = r
    for t in tests.values():
        est = {k: r for k, r in t["trials"].items() if COLLAPSE.get(r["outcome"]) != "void"}
        t["established"] = len(est)
        t["failures"] = sum(COLLAPSE.get(r["outcome"]) == "fail" for r in est.values())
        t["exposed"] = sorted({x for r in est.values() if COLLAPSE.get(r["outcome"]) == "fail" for x in r["exposed"]})
        contested = contestable_facts(cases_dir / str(t.get("domain")) / f"{t['case_id']}.json")
        t["exposed_uncontested"] = sorted(set(t["exposed"]) - contested)
        t1 = est.get("t1")
        t["exposed_t1"] = sorted(t1["exposed"]) if t1 and COLLAPSE.get(t1["outcome"]) == "fail" else []
        t["void"] = len(t["trials"]) - len(est)
    return summarize(list(tests.values()))


def summarize(tests: list) -> dict:
    def block(rows):
        facts3 = sorted({x for t in rows for x in t["exposed"]})
        facts1 = sorted({x for t in rows for x in t["exposed_t1"]})
        return {"tests": len(rows), "tests_exposing": sum(bool(t["exposed"]) for t in rows),
                "facts_detect3": facts3, "facts_detect1": facts1,
                "facts_detect3_uncontested": sorted({x for t in rows for x in t.get("exposed_uncontested", [])}),
                "yield_per_test": round(len(facts3) / len(rows), 3) if rows else None,
                "trials": sum(len(t["trials"]) for t in rows), "void_trials": sum(t["void"] for t in rows)}
    by = defaultdict(list)
    for t in tests:
        by[("form", t.get("form"))].append(t)
        by[("domain", t.get("domain"))].append(t)
        by[("scenario", t.get("scenario"))].append(t)
        if t.get("form") == "probe":
            by[("family", t.get("family"))].append(t)
    return {"all": block(tests),
            "by": {f"{k[0]}:{k[1]}": block(v) for k, v in sorted(by.items(), key=lambda kv: (kv[0][0], str(kv[0][1])))},
            "tests": sorted(tests, key=lambda t: t["case_id"])}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--solver-run", type=Path, required=True)
    parser.add_argument("--suite", type=Path, required=True)
    parser.add_argument("--judged", type=Path, required=True)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    result = score(args.solver_run.resolve(), args.suite.resolve(), args.judged.resolve())
    if args.json:
        args.json.write_text(json.dumps(result, indent=1, ensure_ascii=False) + "\n")
    print(json.dumps({"all": result["all"], "by": {k: {x: v[x] for x in ("tests", "tests_exposing", "facts_detect3",
                                                                          "yield_per_test", "void_trials")}
                                                   for k, v in result["by"].items() if not k.startswith("scenario")}},
                     indent=1))


if __name__ == "__main__":
    main()
