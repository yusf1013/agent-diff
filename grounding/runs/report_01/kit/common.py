"""Paths and helpers shared by the report's number scripts (no model calls, no agent runs).

Every script reads committed run records under `grounding/runs/` and writes one JSON file into `../numbers/`.
Run from the repository root with the kit's Python (backend/.venv), for example:

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.report_01.kit.coverage
"""
from __future__ import annotations

import json
from pathlib import Path

from grounding.runs.autogen_01.inputs.make_briefs import SLACK_ALIASES
from grounding.runs.openclaw_eval_01 import rulings

RUNS = Path(__file__).resolve().parents[2]
NUMBERS = Path(__file__).resolve().parents[1] / "numbers"
DOMAINS = ("box", "calendar", "linear", "slack")

# Who wrote each generation run's scenarios. Arms R, P and P v2 differ in the writer's instructions (autogen_01).
WRITERS = {"autogen_01/runs/gen_arm_r": "Sonnet R", "autogen_01/runs/gen_arm_p": "Sonnet P",
           "autogen_01/runs/gen_arm_p_v2": "Sonnet P v2", "autogen_02/runs/phase4_gen": "Muse Phase 4",
           "completion_01/runs/gen_01": "Muse 6b", "completion_01/runs/gen_02": "Muse 6b"}
WRITER_ORDER = ("Sonnet R", "Sonnet P", "Sonnet P v2", "Muse Phase 4", "Muse 6b")

# The two suites: 6a's frozen suite (78 scenarios) and 6b's (23 scenarios), each an index and a cases folder.
SUITES = ((RUNS / "openclaw_eval_01/suite/suite.json", RUNS / "openclaw_eval_01/suite/cases"),
          (RUNS / "completion_01/suite/cases/suite.json", RUNS / "completion_01/suite/cases"))


def load(path):
    return json.loads(Path(path).read_text())


def write(name: str, data) -> Path:
    NUMBERS.mkdir(exist_ok=True)
    out = NUMBERS / f"{name}.json"
    out.write_text(json.dumps(data, indent=1) + "\n")
    return out


def fact_id(domain: str, fact: str) -> str:
    """The catalog's id for a claimed fact (autogen_01's Slack briefs used older names for five facts)."""
    return SLACK_ALIASES.get(fact, fact) if domain == "slack" else fact


def catalog() -> dict[str, dict[str, dict]]:
    """domain -> fact id -> the catalog's record (fact_coverage_01/catalog)."""
    return {d: {r["id"]: r for r in load(RUNS / "fact_coverage_01/catalog" / f"{d}.json")["requirements"]}
            for d in DOMAINS}


def replica_gaps() -> dict[str, list[str]]:
    """domain -> the catalog facts the replicas cannot serve (autogen_02's exclusion list for briefs)."""
    gaps = load(RUNS / "autogen_02/inputs/briefs_phase4.excluded.json")
    return {d: sorted(gaps.get(d, [])) for d in DOMAINS}


def suite_tests():
    """(index row, case) for every derived test the two suites keep (the witness check's drops are not in them)."""
    for index, folder in SUITES:
        for m in load(index):
            yield m, load(folder / m["domain"] / f"{m['case_id']}.json")


def valid_claims(case: dict):
    """(fact, witness, family) for each near-miss claim that earns credit: the test is not left out by the PI's
    rulings and the near miss is not ruled flawed. Empty for a left-out test. The family is the writer's label
    (fact_coverage_02/method.md: F1-F8 a designated substitute, F0 a plain near miss)."""
    if rulings.test_exclusion(case):
        return []
    bad = rulings.flawed(rulings.scenario_of(case["case_id"]))
    return [(fact_id(case["domain"], c["requirement"]), str(c["witness"]), c.get("family") or "?")
            for ref in case["references"] for c in ref.get("claims", []) if str(c["witness"]) not in bad]
