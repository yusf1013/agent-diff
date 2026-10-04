"""The day each test's dates are relative to: its anchor (the "now" it was written for), with the evidence.

A test's dates become offsets from its anchor day; at run time they are rendered from the real day (templates.py).
The anchor is a local day in a zone: Calendar's in Los Angeles (the calendars' zone, and the zone every Calendar
trial ran in), every other service's in America/Indiana/Indianapolis (this machine's zone, in which every other trial
ran). Rules, in order:

1. Calendar (scenarios and boundary tests): Sunday 2018-06-17, the day the writer's replica notes state as "now".
2. The overdue Linear scenario: 2026-09-30, the writer's own design. Its reference query defines "overdue" as due
   before 2026-09-30, and its third near miss is "due today", due 2026-09-30. It ran on a clock of 2026-09-25 (the
   2026-09-28 discussion), which moved that near miss five days into the future.
3. A scenario with a test clock: the clock's day (the moment its accepted version was written, or a day after its
   latest event; for the October-15 Linear scenario, a day after the near miss created on 2026-10-15).
4. A first-round scenario without a clock: the day it was written (2026-09-27 for Muse's; 2026-09-26 for the one
   Sonnet-written scenario among the by-products); it ran on the real clock.
5. A boundary test outside Calendar: the day its request was written (2026-09-29).
"""
from __future__ import annotations

import json
from dataclasses import dataclass, asdict
from datetime import date, datetime
from zoneinfo import ZoneInfo

from grounding.runs.report_01.kit.common import RUNS

CALENDAR_ZONE = "America/Los_Angeles"
LOCAL_ZONE = "America/Indiana/Indianapolis"
CALENDAR_DAY = date(2018, 6, 17)
DESIGNED = {"G4-LIN-02": (date(2026, 9, 30), "the writer's design: its query defines overdue as due before 2026-09-30, "
                                             "and its third near miss is 'due today' (due 2026-09-30)")}
PHASE4_CALLS = RUNS / "autogen_02/runs/phase4_gen/calls.jsonl"
SONNET_CALLS = [RUNS / f"autogen_01/runs/{g}/calls.jsonl" for g in ("gen_arm_r", "gen_arm_p", "gen_arm_p_v2")]
BOUNDARY_CALLS = RUNS / "boundary_auto_01/runs/calls.jsonl"


@dataclass(frozen=True)
class Anchor:
    day: date
    zone: str
    source: str
    clock: str | None = None        # the clock the test ran under, if any (for the record)

    def as_dict(self) -> dict:
        d = asdict(self)
        d["day"] = self.day.isoformat()
        return d


def _written(calls) -> dict[str, datetime]:
    out = {}
    for line in calls.read_text().splitlines():
        c = json.loads(line)
        if c.get("role") == "writer":
            t = datetime.fromisoformat(c["utc"])
            out[c["label"]] = max(out.get(c["label"], t), t)
    return out


_PHASE4 = None


def anchor_for(scenario: str, domain: str, case: dict) -> Anchor:
    global _PHASE4
    if case.get("written_for"):     # generated since 2026-10-03: the writer was given the date
        w = case["written_for"]
        return Anchor(date.fromisoformat(w["date"]), w["zone"], "the date its writer was given", None)
    clock = (case.get("clock") or {}).get("now")
    if domain == "calendar":
        return Anchor(CALENDAR_DAY, CALENDAR_ZONE, "the Calendar notes' stated now: Sunday, June 17, 2018, 00:01, "
                                                   "Los Angeles", clock)
    if scenario in DESIGNED:
        day, why = DESIGNED[scenario]
        return Anchor(day, LOCAL_ZONE, why, clock)
    if clock:
        instant = datetime.fromisoformat(clock.replace("Z", "+00:00"))
        return Anchor(instant.astimezone(ZoneInfo(LOCAL_ZONE)).date(), LOCAL_ZONE,
                      "the test's clock (the moment its accepted version was written, or a day after its latest event)",
                      clock)
    if scenario.startswith("BDA-"):
        written = max(_written(BOUNDARY_CALLS).values())
        return Anchor(written.astimezone(ZoneInfo(LOCAL_ZONE)).date(), LOCAL_ZONE,
                      "the day the boundary requests were written", None)
    if _PHASE4 is None:
        _PHASE4 = {}
        for calls in SONNET_CALLS + [PHASE4_CALLS]:
            _PHASE4.update(_written(calls))
    if scenario not in _PHASE4:
        raise SystemExit(f"{scenario}: no anchor (no clock and no writer call on record)")
    return Anchor(_PHASE4[scenario].astimezone(ZoneInfo(LOCAL_ZONE)).date(), LOCAL_ZONE,
                  "the day it was written (first round; it ran on the real clock)", None)
