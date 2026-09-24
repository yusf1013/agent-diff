"""Wording probe: the four weak facts with the relation spelled out (same seeds as the CON-*-alt cases)."""
from __future__ import annotations

import copy
from functools import partial

from grounding.runs.fact_coverage_01.pilot.cases_contrast import PAIRS, tag

REWORD = {
    "folder-creator": ("Sam Rivera created a client-tagged folder",
                       "Sam Rivera created (not necessarily owns) a client-tagged folder"),
    "event-creator": ("the all-day offsite Maya Chen created",
                      "the all-day offsite that Maya Chen created (she may not be its organizer)"),
    "hub-inclusion": ("that already includes the Launch assets folder",
                      "that already lists the Launch assets folder itself as one of its items"),
    "relation-direction": ("ENG-7 is blocked by the database migration issue.",
                           "ENG-7 is blocked by the database migration issue (that is, the migration issue blocks ENG-7)."),
}


def worded(label):
    case = tag(PAIRS[label][0], label, "alt")
    old, new = REWORD[label]
    assert old in case["prompt"], (label, case["prompt"])
    case["prompt"] = case["prompt"].replace(old, new)
    case["case_id"] = f"WRD-{label}"
    case["wording_probe"] = {"from": old, "to": new}
    for r in case["references"]:
        r["id"] = case["case_id"] + r["id"][r["id"].index("."):]
    return case


CASES = [partial(worded, label) for label in REWORD]
