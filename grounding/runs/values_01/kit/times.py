"""R5, a bounded probe (cycle 3): times the final reply states for the Calendar event it acted on, against that event's
stored times. No model calls. Needs data/values.json and data/reply.json.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.values_01.kit.times

Scope: Calendar executions whose diff writes a specified field of an event (location, colour, description). For each
such event, the reply's lines that name the event's title are read for time ranges ("10:00-11:00 AM", "3 to 4 pm").
A stated range matches when it equals the event's start and end in the event's own time zone or in the user's
(calendar_settings). A reply that states no range for the event is not comparable.

What it cannot see: times stated without the event's title on the line, single times ("at 10am"), dates and weekdays
(the tests' clocks make weekdays consistent), and times of events the agent did not write.

Writes data/times.json.
"""
from __future__ import annotations

import json
import re
from collections import Counter
from datetime import datetime
from zoneinfo import ZoneInfo

from grounding.runs.values_01.kit.common import DATA, executions, read, reply
from grounding.runs.values_01.kit.common import load

RANGE = re.compile(r"(?i)\b(\d{1,2})(?::(\d{2}))?\s*(a\.?m\.?|p\.?m\.?)?\s*(?:-|–|—|to)\s*(\d{1,2})(?::(\d{2}))?"
                   r"\s*(a\.?m\.?|p\.?m\.?)")


def to24(h: int, m: int, ap: str | None) -> tuple[int, int]:
    if ap:
        pm = ap.lower().startswith("p")
        h = h % 12 + (12 if pm else 0)
    return h, m


def ranges(line: str) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    """Stated ranges, with every plausible reading: an 'AM/PM' marker (seen in replies) leaves the half of the day
    open; a start without a marker takes the end's or the other half ('11:00-12:00 PM' is 11 AM to noon); a range
    that runs backwards ('11:00-12:00 AM') is also read with noon."""
    out = []
    for m in RANGE.finditer(line):
        h1, m1, ap1, h2, m2, ap2 = m.groups()
        h1, h2, m1, m2 = int(h1), int(h2), int(m1 or 0), int(m2 or 0)
        halves = ("am", "pm") if re.match(r"\s*/\s*(?:a|p)\.?m", line[m.end():], re.I) else (ap2,)
        for half in halves:
            end = to24(h2, m2, half)
            starts = [to24(h1, m1, ap1)] if ap1 else [to24(h1, m1, half), to24(h1, m1, "am"), to24(h1, m1, "pm")]
            for start in starts:
                out.append((start, end))
                if end < start:
                    out.append((start, ((end[0] + 12) % 24, end[1])))
    return sorted(set(out))


def local(dt: str, tz: str) -> tuple[int, int]:
    d = datetime.fromisoformat(dt).astimezone(ZoneInfo(tz))
    return d.hour, d.minute


def main():
    ex = {e["key"]: e for e in executions()}
    values, rep = read("values"), read("reply")
    rows, tally = [], Counter()
    for k, e in ex.items():
        if e["domain"] != "calendar" or not rep[k].get("checked"):
            continue
        recs = {x["record"] for x in values[k].get("values", []) if x["field"].startswith("calendar_events.")}
        if not recs:
            continue
        init = load(e["path"] / "environment/initial_state.json")
        user_tz = next((s.get("value") for s in init.get("calendar_settings", []) if s.get("setting_id") == "timezone"
                        or s.get("id") == "timezone"), None) or "America/Los_Angeles"
        events = {ev["id"]: ev for ev in init.get("calendar_events", [])}
        text = re.sub(r"\*\*|__|`", "", reply(e))
        for rid in recs:
            ev = events.get(rid)
            if not ev or not (ev.get("start") or {}).get("dateTime"):
                tally["no timed event"] += 1
                continue
            s, en = ev["start"]["dateTime"], ev["end"]["dateTime"]
            ev_tz = ev["start"].get("timeZone") or user_tz
            want = {(local(s, ev_tz), local(en, ev_tz)), (local(s, user_tz), local(en, user_tz))}
            title = (ev.get("summary") or "").lower()
            lines = [ln for ln in text.splitlines() if title and title in ln.lower()]
            stated = [r for ln in lines for r in ranges(ln)]
            if not stated:
                tally["not comparable"] += 1
                continue
            ok = any(r in want for r in stated)
            tally["match" if ok else "mismatch"] += 1
            if not ok:
                rows.append({"key": k, "kind": e["kind"], "event": rid, "title": ev.get("summary"),
                             "stored": sorted(want), "stated": stated, "lines": [ln.strip()[:200] for ln in lines][:3]})
    (DATA / "times.json").write_text(json.dumps({"tally": tally, "mismatches": rows}, indent=1, default=str) + "\n")
    print(dict(tally))
    for r in rows:
        print(r["key"], r["title"], "stored", r["stored"], "stated", r["stated"], "|", r["lines"][:1])


if __name__ == "__main__":
    main()
