"""New Calendar scenarios for facts the pilot never tested (manual design). Now is Sunday 2018-06-17, Los Angeles.

Each has its target; probes are derived. Every claim carries its substitute family (method.md).
"""
from __future__ import annotations

from grounding.runs.fact_coverage_01.pilot.cases_calendar import ACTOR, EVENTS, PRIMARY, Seed, email
from grounding.runs.fact_coverage_01.pilot.common import DROP, REPLACE, SPLIT, claim, e, f, n, q, ref
from grounding.runs.fact_coverage_02.scenarios_box import fam


# ---------------------------------------------------------------------------
def cal_21():
    """Event end time and event description."""
    s = Seed()
    thu = "2018-06-21T{}:00"
    s.event("ev_ps_target", PRIMARY, "Planning session", thu.format("16:00"), thu.format("17:00"),
            description="Walk through the Q4 roadmap and owners")                                    # target
    s.event("ev_ps_starts", PRIMARY, "Planning session", thu.format("17:00"), thu.format("18:00"),
            description="Q4 roadmap follow-ups")                                                     # starts at 5pm
    s.event("ev_ps_late", PRIMARY, "Planning session", thu.format("16:30"), thu.format("17:30"),
            description="Q4 roadmap estimates")                                                      # ends at 5:30pm
    s.event("ev_ps_title", PRIMARY, "Q4 roadmap planning", thu.format("16:00"), thu.format("17:00"),
            description="Agenda to be confirmed")                                                    # only the title
    s.event("ev_ps_hiring", PRIMARY, "Planning session", thu.format("15:30"), thu.format("17:00"),
            description="Hiring plan for the autumn")                                                # other topic
    query = q("calendar_events", [f("f_sum", "summary", "contains_ci", "planning", "A:Event.summary"),
                                  f("f_end", "end_datetime", "eq", thu.format("17:00"), "A:Event.end"),
                                  f("f_desc", "description", "contains_ci", "q4 roadmap", "A:Event.description")])
    by_start = q("calendar_events", [f("f_sum", "summary", "contains_ci", "planning"),
                                     f("f_end", "start_datetime", "eq", thu.format("17:00")),
                                     f("f_desc", "description", "contains_ci", "q4 roadmap")])
    by_title = q("calendar_events", [f("f_sum", "summary", "contains_ci", "planning"),
                                     f("f_end", "end_datetime", "eq", thu.format("17:00")),
                                     f("f_desc", "summary", "contains_ci", "q4 roadmap")])
    claims = [
        fam(claim("A:Event.end", "ev_ps_starts", REPLACE(by_start, "end time replaced by start time"),
                  "Starts at 5pm on Thursday; it ends at 6pm.", alternative="Event.start"), "F1"),
        fam(claim("A:Event.end", "ev_ps_late", DROP("f_end"), "Ends at 5:30pm, the nearest wrong end time.",
                  alternative="nearest end time"), "F7"),
        fam(claim("A:Event.description", "ev_ps_title", REPLACE(by_title, "description replaced by title"),
                  "The title mentions the Q4 roadmap; the description does not.", alternative="Event.summary"), "F1"),
        fam(claim("A:Event.description", "ev_ps_hiring", DROP("f_desc"), "About the hiring plan."), "F0"),
    ]
    return {
        "case_id": "CAL-21", "domain": "calendar", "form": "present", "mode": "single", "acting_user_id": ACTOR,
        "seed": s.seed(),
        "prompt": "Move the planning session that ends at 5pm on Thursday and whose description mentions the Q4 "
                  "roadmap to Room 2B.",
        "references": [ref("CAL-21.r1", "Resolve the planning session",
                           "The planning session on Thursday 2018-06-21 ending at 17:00 local whose description mentions "
                           "the Q4 roadmap; only ev_ps_target.", "target", query, ["ev_ps_target"], claims,
                           paths=[{"entities": ["calendar_events"], "relationships": []}],
                           identifying=["calendar_events.summary", "calendar_events.end", "calendar_events.description"],
                           written=["calendar_events.location"],
                           effect={"table": "calendar_events", "changes": ["update"], "columns": ["location"]})],
        "probes": [("GET", EVENTS, {"timeMin": "2018-06-21T00:00:00-07:00", "timeMax": "2018-06-22T00:00:00-07:00",
                                    "singleEvents": "true"})],
    }


# ---------------------------------------------------------------------------
def cal_22():
    """Calendar description (the user asks by description; name and location are the substitutes)."""
    s = Seed()
    for cid, summary, description, location in [
        ("emea@northwind.example", "EMEA team", "Calendar for the London office", "Reading"),            # target
        ("london@northwind.example", "London office", "Calendar for the Paris office", "Paris"),         # name only
        ("uk-sites@northwind.example", "UK sites", "Calendar for the Berlin office", "London"),         # location only
        ("madrid@northwind.example", "Iberia team", "Calendar for the Madrid office", "Madrid"),        # other office
    ]:
        s.calendar(cid, summary, description=description)
        s.t["calendars"][-1]["location"] = location
    query = q("calendars", [f("f_desc", "description", "contains_ci", "london office", "A:Calendar.description")])
    claims = [
        fam(claim("A:Calendar.description", "london@northwind.example",
                  REPLACE(q("calendars", [f("f_desc", "summary", "contains_ci", "london office")]),
                          "description replaced by name"),
                  "Named London office; its description says Paris.", alternative="Calendar.summary"), "F1"),
        fam(claim("A:Calendar.description", "uk-sites@northwind.example",
                  REPLACE(q("calendars", [f("f_desc", "location", "eq", "London")]), "description replaced by location"),
                  "Located in London; its description says Berlin.", alternative="Calendar.location"), "F1"),
        fam(claim("A:Calendar.description", "madrid@northwind.example", DROP("f_desc"), "For the Madrid office."), "F0"),
    ]
    return {
        "case_id": "CAL-22", "domain": "calendar", "form": "present", "mode": "single", "acting_user_id": ACTOR,
        "seed": s.seed(),
        "prompt": f"Give Sam Rivera ({email('sam')}) read access to the calendar whose description says it is for the "
                  "London office.",
        "references": [ref("CAL-22.r1", "Resolve the calendar",
                           "The calendar whose description says it is for the London office; only emea@.", "target",
                           query, ["emea@northwind.example"], claims,
                           paths=[{"entities": ["calendars"], "relationships": []}],
                           identifying=["calendars.description"], written=["calendar_acl_rules"],
                           effect={"table": "calendar_acl_rules", "changes": ["insert"], "field": "calendar_id"})],
        "probes": [("GET", "/users/me/calendarList", None), ("GET", "/calendars/uk-sites@northwind.example", None)],
    }


# ---------------------------------------------------------------------------
def cal_23():
    """An attendee's email and optional flag."""
    s = Seed()
    fri = "2018-06-22T{}:00"
    s.event("ev_ar_target", PRIMARY, "Architecture review", fri.format("10:00"), fri.format("11:00"),
            attendees=[("kenji", "accepted", "optional"), ("aiko", "accepted")])                     # target
    s.event("ev_ar_required", PRIMARY, "Architecture review: storage", fri.format("13:00"), fri.format("14:00"),
            attendees=[("kenji", "accepted"), ("aiko", "accepted")])                                # Kenji required
    s.event("ev_ar_satou", PRIMARY, "Architecture review: search", fri.format("15:00"), fri.format("16:00"),
            attendees=[("aiko", "accepted")])                                                       # kenji.satou@
    s.att += 1
    s.t["calendar_event_attendees"].append({
        "id": s.att, "event_id": "ev_ar_satou", "email": "kenji.satou@northwind.example", "display_name": "Kenji Satou",
        "response_status": "accepted", "optional": True, "organizer": False, "self": False, "resource": False})
    day = [f("f_from", "start_datetime", "ge", fri.format("00:00")), f("f_to", "start_datetime", "lt", "2018-06-23T00:00:00")]
    guest = n("calendar_event_attendees", [f("f_email", "email", "eq", email("kenji"), "A:EventAttendee.email"),
                                           f("f_opt", "optional", "eq", True, "A:EventAttendee.optional")])
    query = q("calendar_events", [f("f_sum", "summary", "contains_ci", "architecture review")] + day,
              [e("e_att", "id", "event_id", guest, "R:EventAttendee.event_id")])
    claims = [
        fam(claim("A:EventAttendee.optional", "ev_ar_required", DROP("f_opt"), "Kenji is a required attendee."), "F0"),
        fam(claim("A:EventAttendee.email", "ev_ar_satou", DROP("f_email"),
                  "The optional guest is kenji.satou@, not kenji.sato@.", alternative="similar email"), "F8"),
    ]
    return {
        "case_id": "CAL-23", "domain": "calendar", "form": "present", "mode": "single", "acting_user_id": ACTOR,
        "seed": s.seed(),
        "prompt": f"Delete Friday's architecture review that Kenji Sato ({email('kenji')}) attends as an optional guest.",
        "references": [ref("CAL-23.r1", "Resolve the review to delete",
                           "Friday's architecture review with kenji.sato@ as an optional attendee; only ev_ar_target.",
                           "target", query, ["ev_ar_target"], claims,
                           paths=[{"entities": ["calendar_events", "calendar_event_attendees"],
                                   "relationships": ["calendar_event_attendees.event_id"]}],
                           identifying=["calendar_events.summary", "calendar_events.start",
                                        "calendar_event_attendees.email", "calendar_event_attendees.optional"],
                           effect={"table": "calendar_events", "changes": ["delete", "update"]})],
        "probes": [("GET", EVENTS, {"timeMin": "2018-06-22T00:00:00-07:00", "timeMax": "2018-06-23T00:00:00-07:00",
                                    "singleEvents": "true"})],
    }


# ---------------------------------------------------------------------------
def cal_24():
    """Calendar location (the user asks by location; description, name and time zone are the substitutes)."""
    s = Seed()
    for cid, summary, description, location, tz in [
        ("apac@northwind.example", "APAC events", "Regional events", "Tokyo", "Asia/Tokyo"),          # target
        ("jp-team@northwind.example", "Japan team", "Tokyo team calendar", "Osaka", "Asia/Tokyo"),   # description only
        ("tokyo@northwind.example", "Tokyo", "Office calendar", "Singapore", "Asia/Singapore"),      # name only
        ("kr-team@northwind.example", "Korea team", "Seoul team", "Seoul", "Asia/Tokyo"),           # Tokyo time zone only
        ("anz@northwind.example", "ANZ events", "Regional events", "Sydney", "Australia/Sydney"),    # other city
    ]:
        s.calendar(cid, summary, description=description, tz=tz)
        s.t["calendars"][-1]["location"] = location
    query = q("calendars", [f("f_loc", "location", "eq", "Tokyo", "A:Calendar.location")])

    def instead(field, op, value, note):
        return REPLACE(q("calendars", [f("f_loc", field, op, value)]), note)

    claims = [
        fam(claim("A:Calendar.location", "jp-team@northwind.example",
                  instead("description", "contains_ci", "tokyo", "location replaced by description"),
                  "Its description says Tokyo; it is located in Osaka.", alternative="Calendar.description"), "F1"),
        fam(claim("A:Calendar.location", "tokyo@northwind.example", instead("summary", "eq", "Tokyo", "location replaced by name"),
                  "Named Tokyo; located in Singapore.", alternative="Calendar.summary"), "F1"),
        fam(claim("A:Calendar.location", "kr-team@northwind.example",
                  instead("time_zone", "eq", "Asia/Tokyo", "location replaced by time zone"),
                  "Uses Tokyo time; located in Seoul.", alternative="Calendar.time_zone"), "F6"),
        fam(claim("A:Calendar.location", "anz@northwind.example", DROP("f_loc"), "Located in Sydney."), "F0"),
    ]
    return {
        "case_id": "CAL-24", "domain": "calendar", "form": "present", "mode": "single", "acting_user_id": ACTOR,
        "seed": s.seed(),
        "prompt": "Set the description of my calendar located in Tokyo to \"APAC offsite planning\".",
        "references": [ref("CAL-24.r1", "Resolve the calendar",
                           "The calendar whose location is Tokyo; only apac@.", "target", query,
                           ["apac@northwind.example"], claims,
                           paths=[{"entities": ["calendars"], "relationships": []}], identifying=["calendars.location"],
                           written=["calendars.description"],
                           effect={"table": "calendars", "changes": ["update"], "columns": ["description"]})],
        "probes": [("GET", "/users/me/calendarList", None), ("GET", "/calendars/kr-team@northwind.example", None)],
    }


SCENARIOS = [cal_21, cal_22, cal_23, cal_24]
