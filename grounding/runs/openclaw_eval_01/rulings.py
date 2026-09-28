"""The PI's rulings (roadmap_01/known_defects.json), applied to a test or a trial, for runs with the original ids or
the opaque ones (the discussion after 6a, 2026-09-28). The one place the runner, the policy stage and the scoring
learn which tests and trials count; the manual validity reviews are evidence behind the rulings, no longer read.

- **A test is left out** when its entry (or its scenario's) says "leave out" or "dropped by the derivation"; when
  it is a probe or a policy unit that holds a flawed near miss among its near misses (a unit where that record has
  become a match keeps it); or when it is a form a valid near miss's ruling leaves out (C_BILLING's and
  ev_budget_free's absence twins).
- **A trial does not count** when every record it acted on is a flawed near miss of its scenario.
- Near misses are ruled by their original ids; suite_opaque/ids/<scenario>.json gives their opaque ones.
"""
from __future__ import annotations

import functools
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
KNOWN_DEFECTS = HERE.parent / "roadmap_01" / "known_defects.json"
IDS = HERE / "suite_opaque" / "ids"
FORMS = (("AT-", "absence twin"), ("UC-", "clone"), ("U-", "underspecified"), ("FP-", "fact probe"), ("P-", "probe"))


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
    path = IDS / f"{scenario}.json"
    return json.loads(path.read_text())["ids"] if path.exists() else {}


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
