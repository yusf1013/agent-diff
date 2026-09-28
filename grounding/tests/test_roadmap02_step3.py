"""Roadmap step 3's fixes to the generation kit: event time zones, the date check, the probe-trap drop, and the kit's
own seed helpers. The last two build recorded scenarios, so they need the backend's environment (DATABASE_URL)."""
import json
import os
import re
from pathlib import Path

import pytest

from grounding.runs.autogen_01.kit import scenario, seedops

RUNS = Path(__file__).resolve().parents[1] / "runs"


def test_local_offset_follows_the_zone_and_the_date():
    assert seedops.local_offset("2018-06-21T12:00:00", "America/Los_Angeles") == "-07:00"
    assert seedops.local_offset("2018-12-21T12:00:00", "America/Los_Angeles") == "-08:00"
    assert seedops.local_offset("2018-06-21T12:00:00", "America/New_York") == "-04:00"
    assert seedops.local_offset("2018-06-21T12:00:00", "Asia/Kolkata") == "+05:30"


def test_relative_dates_outside_calendar_are_sent_back():
    linear = {"domain": "linear", "request": "Set the estimate to 5 on the overdue high-priority issue."}
    calendar = {"domain": "calendar", "request": "Move this Thursday's design review to Room 5B."}
    plain = {"domain": "box", "request": "Tag the PDF that Leo Park modified last."}
    assert scenario._relative_dates(linear) and "overdue" in scenario._relative_dates(linear)[0]
    assert scenario._relative_dates(calendar) == []
    assert scenario._relative_dates(plain) == []  # "modified last" is not "last week"


def _latest(folder: Path):
    versions = sorted(folder.glob("scenario-v*.json"), key=lambda p: int(re.search(r"v(\d+)", p.name).group(1)))
    return json.loads(versions[-1].read_text())


def _build(folder: Path):
    s = _latest(folder)
    brief = {"scenario_id": s["scenario_id"], "domain": s["domain"],
             "facts": sorted({d["fact"] for d in s["reference"]["decoys"]})}
    return scenario.build(s, brief)


needs_db = pytest.mark.skipif(not os.getenv("DATABASE_URL"), reason="building seeds needs the backend environment")


@needs_db
def test_a_probe_without_its_trap_is_dropped_and_recorded():
    from grounding.runs.autogen_01.kit import derive
    case, _ = _build(RUNS / "autogen_02/runs/phase4_gen/G4-LIN-01")
    kept, dropped = derive.suite_with_dropped(case)
    assert "P-G4-LIN-01-I13" in {t["case_id"] for t, _ in dropped}
    assert "P-G4-LIN-01-I13" not in {t["case_id"] for t, _ in kept}
    assert all(m["errors"] for _, m in dropped)
    assert [t["case_id"] for t, _ in derive.suite(case)] == [t["case_id"] for t, _ in kept]


@needs_db
def test_events_take_their_calendars_zone():
    case, problems = _build(RUNS / "autogen_02/runs/phase4_gen/G4-CAL-06")
    zones = {c["id"]: c["time_zone"] for c in case["seed"]["calendars"]}
    for event in case["seed"]["calendar_events"]:
        assert event["start"]["timeZone"] == zones[event["calendar_id"]]
    assert not problems
