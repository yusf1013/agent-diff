"""Dates belong to the test (grounding/common/dates.py; grounding/runs/dates_02): templates render back to the test as
written on its anchor day, move with the run day, and a test made for a shifted agent clock is refused (no network)."""
import json
import sys
from datetime import date, datetime, timezone
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO))

from grounding.common import dates  # noqa: E402

SUITE = REPO / "grounding/runs/dates_02/suite"


def load(rel):
    return json.loads((SUITE / rel).read_text())


def test_a_template_renders_back_to_the_test_as_written_on_its_anchor_day():
    t = load("cases/linear/G4-LIN-08.json")
    back = dates.at_anchor(t)
    assert "Set the priority of the 3-point sub-issue of MOB-42 due on October 15 to High." == back["prompt"]
    assert "⟦" not in json.dumps(back)


def test_the_world_moves_with_the_run_day_and_keeps_its_relations():
    t = load("cases/linear/G4-LIN-02.json")       # designed for 2026-09-30: one issue overdue, a near miss due today
    case, info = dates.for_run(t, now=datetime(2026, 11, 20, 15, 0, tzinfo=timezone.utc))
    assert info["run_day"] == "2026-11-20" and info["shift_days"] == 51 and info["mode"] == "day"
    issues = {i["identifier"]: i["dueDate"] for i in case["seed"]["issues"] if i.get("dueDate")}
    assert "2026-11-20" in issues.values()        # the "due today" near miss is due on the run day
    assert "⟦" not in json.dumps(case)


def test_weekdays_are_rewritten_to_the_run_week():
    t = load("cases/calendar/G4-CAL-01.json")      # "... at 10am on Thursday ..." written for Sunday 2018-06-17
    case, info = dates.for_run(t, now=datetime(2026, 10, 3, 19, 0, tzinfo=timezone.utc))   # Saturday in Los Angeles
    assert "on Wednesday" in case["prompt"] and info["run_day"] == "2026-10-03"
    starts = [e["start"].get("dateTime", "") for e in case["seed"]["calendar_events"]]
    assert any(s.startswith("2026-10-07T10:00:00-07:00") for s in starts)


def test_a_month_condition_moves_by_whole_months():
    t = load("cases/box/G4-BOX-16.json")           # "the Harbor launch folder created in March"
    assert t["dates"]["mode"] == "month"
    case, _ = dates.for_run(t, now=datetime(2026, 12, 5, 15, 0, tzinfo=timezone.utc))
    assert "created in May" in case["prompt"]


def test_slack_is_held_at_its_written_days():
    t = load("cases/slack/G4-SLK-10.json")
    case, info = dates.for_run(t, now=datetime(2027, 1, 5, tzinfo=timezone.utc))
    assert info["mode"] == "fixed" and case["prompt"] == dates.at_anchor(t)["prompt"]


def test_a_test_made_for_a_shifted_clock_is_refused():
    with pytest.raises(RuntimeError, match="discontinued"):
        dates.for_run({"case_id": "G4-LIN-02", "domain": "linear", "clock": {"now": "2026-09-25T16:00:00Z"}})
    with pytest.raises(RuntimeError, match="discontinued"):
        dates.for_run({"case_id": "G4-CAL-01", "domain": "calendar"})
    plain = {"case_id": "G4-BOX-01", "domain": "box", "prompt": "x"}
    assert dates.for_run(plain) == (plain, None)
