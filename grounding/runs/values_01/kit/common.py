"""The 3,018 final executions and what every check reads from them. No model calls, no agent runs.

Each execution is one attempt folder under openclaw_eval_01/runs/ (the last attempt, as scored), keyed as in
report_01's final manifest (`numbers/concise.json` → `final_execution_keys`):
- regular: `<run>/<trial>/<case_id>` (full_02, full_03, full_04);
- policy: `<solve_run>/<trial>/<unit>` (the population runs, and Box's first-pass looks whose verdicts the population
  kept).

The grounding outcome is read for the cross-tabulation only, never by a check: for regular executions from the run's
score (judge v2's verdict, or the mechanical triage when no verdict was saved), for policy executions from the saved
verdict. Judge notes are not read.
"""
from __future__ import annotations

import json
import re
from functools import lru_cache
from pathlib import Path

from grounding.runs.report_01.kit import beyond
from grounding.runs.report_01.kit.common import RUNS, load

OC = RUNS / "openclaw_eval_01/runs"
HERE = Path(__file__).resolve().parents[1]
DATA = HERE / "data"
FAIL = {"incorrect", "presented"}


def scenario_of(case_id: str) -> str:
    m = re.match(r"^(?:P-|FP-|AT-|U-)?((?:AP2?|AR|G4)-[A-Z]{3}-\d+)", case_id)
    return m.group(1) if m else case_id


def grounding_class(outcome: str | None) -> str:
    if outcome in FAIL:
        return "fail"
    if outcome in {"correct", "correct_absent"}:
        return "pass"
    if outcome in {"false_absence", "incomplete"}:
        return "nonfail-other"
    return "void"


@lru_cache(maxsize=None)
def _scores() -> dict:
    """(run, trial, case_id) -> the regular trial's scored outcome."""
    out = {}
    for run in ("full_02", "full_03", "full_04"):
        for t in load(OC / f"{run}.score.json")["tests"]:
            for trial, r in t["trials"].items():
                out[(run, trial, t["case_id"])] = {"outcome": r["outcome"], "judged": bool(r.get("judged"))}
    return out


def executions() -> list[dict]:
    """Every final execution: key, attempt path, kind (regular, absence, underspecified), form, domain, case, scenario,
    trial, the grounding outcome (for cross-tabulation only), and the time flags."""
    from grounding.runs.openclaw_eval_01 import rulings
    rows = []
    for a, key, form in beyond.regular_trials():
        run, trial, case_id = key.split("/")
        s = _scores()[(run, trial, case_id)]
        rows.append({"key": key, "path": a, "kind": "regular", "form": form, "trial": trial, "case_id": case_id,
                     "outcome": s["outcome"], "llm_verdict": s["judged"]})
    for a, _, mode in beyond.policy_trials():
        key = "/".join(a.relative_to(OC / "policy").parts[:3])
        solve_run, trial, unit = key.split("/")
        v = OC / "policy" / solve_run.replace("solve_", "judged_", 1) / key / "verdict.json"
        outcome = load(v).get("outcome") if v.exists() else None
        rows.append({"key": key, "path": a, "kind": mode, "form": mode, "trial": trial, "case_id": unit,
                     "outcome": outcome, "llm_verdict": v.exists()})
    for r in rows:
        summary = load(r["path"] / "execution_summary.json")
        r["domain"] = summary["domain"]
        r["scenario"] = scenario_of(r["case_id"])
        r["timeout"] = summary.get("termination") == "timeout"
        r["over_480s"] = rulings.over_budget(r["path"])
        r["grounding"] = grounding_class(r["outcome"])
    final = set(load(RUNS / "report_01/numbers/concise.json")["final_execution_keys"])
    assert {r["key"] for r in rows} == final and len(rows) == 3018
    return rows


def dump(name: str, rows: list[dict]) -> None:
    """One compact JSON file per check family under data/ (empty fields dropped; readers use .get)."""
    DATA.mkdir(exist_ok=True)
    keep = [{k: v for k, v in r.items() if v not in (None, [], {}, False, "")} for r in rows]
    (DATA / f"{name}.json").write_text(json.dumps(keep, separators=(",", ":"), ensure_ascii=False, default=str) + "\n")


def read(name: str) -> dict:
    return {r["key"]: r for r in json.loads((DATA / f"{name}.json").read_text())}


def case(ex: dict) -> dict:
    return load(ex["path"] / "case.json")


def diff(ex: dict) -> dict:
    p = ex["path"] / "environment/diff_run.json"
    return load(p)["diff"] if p.exists() else {"inserts": [], "updates": [], "deletes": []}


def transcript(ex: dict) -> dict:
    solver = ex["path"] / "solver"
    files = [p for p in solver.glob("*.json") if p.name != "config.json"]
    return load(files[0]) if files else {}


def reply(ex: dict) -> str:
    p = ex["path"] / "solver/final_response.md"
    return p.read_text() if p.exists() else ""


def initial_state(ex: dict) -> dict:
    return load(ex["path"] / "environment/initial_state.json")
