"""The PI's rulings (roadmap_01/known_defects.json), applied to a test or a trial, for runs with the original ids or
the opaque ones (the discussion after 6a, 2026-09-28). The one place the runner, the policy stage and the scoring
learn which tests and trials count; the manual validity reviews are evidence behind the rulings, no longer read.

- **A test is left out** when its entry (or its scenario's) says "leave out" or "dropped by the derivation"; when
  it is a probe or a policy unit that holds a flawed near miss among its near misses (a unit where that record has
  become a match keeps it); or when it is a form a valid near miss's ruling leaves out (C_BILLING's and
  ev_budget_free's absence twins).
- **A trial does not count** when every record it acted on is a flawed near miss of its scenario.
- **A trial runs out the solver's budget** (the PI, 2026-09-28) when its agent time, rate-limiter waits excluded,
  passes 8 minutes: it is the solver's failure, not re-run. A policy unit's trial is "incorrect"; a regular test's
  trial exposes no fact.
- Near misses are ruled by their original ids; suite_opaque/ids/<scenario>.json (6a) and
  ../completion_01/suite/ids/<scenario>.json (6b) give their opaque ones.
"""
from __future__ import annotations

import functools
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
KNOWN_DEFECTS = HERE.parent / "roadmap_01" / "known_defects.json"
ID_DIRS = (HERE / "suite_opaque" / "ids", HERE.parent / "completion_01" / "suite" / "ids")  # 6a's scenarios, 6b's
FORMS = (("AT-", "absence twin"), ("UC-", "clone"), ("U-", "underspecified"), ("FP-", "fact probe"), ("P-", "probe"))
# The solver's time budget. The PI, 2026-09-28: a solver that runs out its budget (limiter waits excluded) fails the
# trial. On 2026-09-29 the PI set the budget to 10 minutes, since every OpenClaw run used OpenClaw's 600-second
# limit; the earlier 480-second reading (trials between 8 and 10 minutes counted as timed out) is withdrawn.
BUDGET_S = 600

# Duplicate policy units (the PI, 2026-09-29: count each pair once). The rule of one unit per dropped condition made
# two units of one request when two conditions gave the same words: the pair's request, actor and seed are
# identical, so it is one test. The second unit's trials count as further trials of the first.
DUPLICATE_UNITS = {"U-AP-SLK-03-message_reactions_user": "U-AP-SLK-03-message_reactions",
                   "U-G4-LIN-14-Issue_assigneeId-B": "U-G4-LIN-14-Issue_assigneeId"}


def merge_duplicate_units(valid: list[dict], outcomes: dict[str, dict]) -> list[dict]:
    """Fold DUPLICATE_UNITS into their primaries: the duplicate leaves `valid`, and its trials join the primary's
    outcomes under distinct keys. Returns the reduced list."""
    keep = []
    for u in valid:
        primary = DUPLICATE_UNITS.get(u["unit"])
        if primary is None:
            keep.append(u)
            continue
        for trial, outcome in (outcomes.get(u["unit"]) or {}).items():
            outcomes.setdefault(primary, {})[f"{trial}:{u['unit']}"] = outcome
    return keep


def over_budget(attempt: Path) -> bool:
    """The trial ran out the solver's budget: OpenClaw's turn limit (600 s) ended it, or its agent time minus
    rate-limiter waits passed BUDGET_S. Trials that spent over a quarter of the turn waiting for the shared limiter
    were re-run as infrastructure errors (runtime rule R2), so the waits never make a trial time out."""
    summary = json.loads((attempt / "execution_summary.json").read_text())
    if summary.get("status") != "completed":
        return False
    if summary.get("termination") == "timeout":
        return True
    turn = (summary.get("turn_durations_s") or [0])[0]
    return turn - ((summary.get("usage") or {}).get("limiter_wait_s") or 0) > BUDGET_S


def scenario_of(case_id: str) -> str:
    stem = re.sub(r"^(AT|FP|P|UC|U|H)-", "", case_id)
    m = re.match(r"((?:[A-Z]+\d?-)?[A-Z]{3}-\d+)", stem)
    return m.group(1) if m else stem


def form_of(case_id: str) -> str:
    return next((f for p, f in FORMS if case_id.startswith(p)), "cover")


@functools.cache
def _doc() -> dict:
    return json.loads(KNOWN_DEFECTS.read_text())


@functools.cache
def _mapping(scenario: str) -> dict[str, str]:
    for folder in ID_DIRS:
        path = folder / f"{scenario}.json"
        if path.exists():
            return json.loads(path.read_text())["ids"]
    return {}


def _both(scenario: str, witness: str) -> set[str]:
    """A near miss's original id and its opaque one."""
    return {witness, _mapping(scenario).get(witness, witness)}


def actions() -> dict[str, str]:
    """case or scenario id -> its frozen-suite action."""
    doc = _doc()
    return {e["id"]: e["frozen_suite"] for part in ("curated", "from_the_witness_check") for e in doc[part]}


def flawed(scenario: str) -> set[str]:
    return {w for n in _doc().get("near_misses", []) if n["scenario"] == scenario and n["ruling"] == "flawed"
            for w in _both(scenario, n["witness"])}


def left_out_forms(scenario: str) -> dict[str, str]:
    """Near miss (either id) -> the forms its ruling leaves out, for valid near misses with exceptions."""
    out = {}
    for n in _doc().get("near_misses", []):
        if n["scenario"] == scenario and n.get("leave_out"):
            for w in _both(scenario, n["witness"]):
                out[w] = n["leave_out"]
    return out


def witnesses(case: dict) -> set[str]:
    return {str(c["witness"]) for r in case["references"] for c in r.get("claims", [])}


def test_exclusion(case: dict) -> str | None:
    """Why the rulings leave this test out, or None."""
    cid = case["case_id"]
    scenario, form = scenario_of(cid), form_of(cid)
    action = actions().get(cid) or actions().get(scenario) or "keep"
    if action.startswith(("leave out", "dropped")):
        return f"known defect: {action}"
    held = witnesses(case)
    if form != "cover" and form != "fact probe":
        bad = sorted(held & flawed(scenario))
        if bad:
            return f"holds a flawed near miss: {bad}"
    for w, forms in left_out_forms(scenario).items():
        if w in held and form in forms:
            return f"{form} of near miss {w}, left out by its ruling"
    return None


def trial_not_counted(scenario: str, acted_on: list) -> str | None:
    acted = [str(a) for a in acted_on or []]
    bad = flawed(scenario)
    if acted and all(a in bad for a in acted):
        return f"acted only on flawed near misses {acted}"
    return None
