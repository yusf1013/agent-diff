"""Calendar pilot cases (manual design). The official prompt fixes now = Sunday 2018-06-17 00:01 PDT."""
from __future__ import annotations

from functools import partial

from grounding.runs.fact_coverage_01.pilot.common import (DROP, REPLACE, SPLIT, SUB, claim, e, f, n, q, ref)

ACTOR = "u_actor"
DOMAIN = "northwind.example"
PEOPLE = {"actor": "Jordan Lee", "priya": "Priya Nair", "omar": "Omar Haddad", "maya": "Maya Chen", "sam": "Sam Rivera",
          "dana": "Dana Whitfield", "kenji": "Kenji Sato", "aiko": "Aiko Mori", "leo": "Leo Park"}


def email(key):
    return PEOPLE[key].lower().replace(" ", ".") + "@" + DOMAIN


PRIMARY = email("actor")
TZ = "America/Los_Angeles"


class Seed:
    def __init__(self):
        self.t = {k: [] for k in ["calendar_users", "calendars", "calendar_list_entries", "calendar_events",
                                  "calendar_event_attendees", "calendar_acl_rules"]}
        self.att = 0
        for key, name in PEOPLE.items():
            self.t["calendar_users"].append({"id": ACTOR if key == "actor" else f"u_{key}", "email": email(key),
                                             "display_name": name, "self": key == "actor",
                                             "created_at": "2017-05-01T00:00:00", "updated_at": "2017-05-01T00:00:00"})
        self.calendar(PRIMARY, PRIMARY, owner="actor", description="Primary calendar", primary=True)

    def calendar(self, cid, summary, *, owner="actor", tz=TZ, description="", access="owner", primary=False,
                 hidden=False, override=None, data_owner=None, in_list=True):
        self.t["calendars"].append({"id": cid, "summary": summary, "description": description, "time_zone": tz,
                                    "owner_id": ACTOR if owner == "actor" else f"u_{owner}", "etag": f'"etag_{cid}"',
                                    "data_owner": data_owner or email(owner), "deleted": False, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"})
        if in_list:
            row = {"id": f"cle_{cid}", "user_id": ACTOR, "calendar_id": cid, "access_role": access, "primary": primary,
                   "selected": True, "hidden": hidden, "deleted": False, "etag": f'"etag_cle_{cid}"', "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
            if override:
                row["summary_override"] = override
            self.t["calendar_list_entries"].append(row)
        return cid

    def event(self, eid, cal, summary, start, end=None, *, all_day=False, organizer="actor", creator=None,
              attendees=(), description="", location="", status="confirmed", transparency="opaque",
              visibility="default", event_type="default", recurrence=None, utc_start=None, hangout=False):
        creator = creator or organizer
        row = {"id": eid, "calendar_id": cal, "ical_uid": f"{eid}@{DOMAIN}", "summary": summary,
               "description": description, "location": location, "status": status, "visibility": visibility,
               "transparency": transparency, "event_type": event_type, "sequence": 0, "etag": f'"etag_{eid}"',
               "creator_email": email(creator), "creator_display_name": PEOPLE[creator],
               "organizer_email": email(organizer), "organizer_display_name": PEOPLE[organizer],
               "creator_self": creator == "actor", "organizer_self": organizer == "actor",
               "created_at": "2018-05-01T00:00:00", "updated_at": "2018-05-01T00:00:00"}
        if all_day:
            row.update(start={"date": start}, end={"date": end}, start_date=start, end_date=end)
        else:
            row.update(start={"dateTime": utc_start or f"{start}-07:00", "timeZone": TZ},
                       end={"dateTime": f"{end}-07:00", "timeZone": TZ}, start_datetime=start, end_datetime=end)
        if recurrence:
            row["recurrence"] = recurrence
        if hangout:
            row["hangout_link"] = f"https://meet.google.com/{eid[:3]}-abcd-efg"
        self.t["calendar_events"].append(row)
        for a in attendees:
            key, status_ = a[0], a[1]
            self.att += 1
            self.t["calendar_event_attendees"].append({
                "id": self.att, "event_id": eid, "email": email(key), "display_name": PEOPLE[key],
                "response_status": status_, "optional": len(a) > 2 and a[2] == "optional",
                "organizer": key == organizer, "self": key == "actor", "resource": False})
        return eid

    def acl(self, rid, cal, role, scope_type, scope_value):
        self.t["calendar_acl_rules"].append({"id": rid, "calendar_id": cal, "role": role, "scope_type": scope_type,
                                             "scope_value": scope_value, "etag": f'"etag_{rid}"', "deleted": False,
                                             "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"})

    def seed(self):
        return {k: v for k, v in self.t.items() if v}


def flip(case, base_form, form, expected_by_ref):
    if form in (None, base_form):
        return case
    base_id = case["case_id"]
    case["case_id"] += "-A" if form == "absent" else "-P"
    case["form"], case["variant_of"] = form, base_id
    case["mode"] = "absent" if form == "absent" else "single"
    for r in case["references"]:
        if r["id"] in expected_by_ref:
            r["expected"] = expected_by_ref[r["id"]]
            r["resolution"] = "resolved" if r["expected"] else "absent"
            r["description"] += " [" + ("Target removed: no match." if form == "absent" else "Target added.") + "]"
        r["id"] = case["case_id"] + r["id"][r["id"].index("."):]
    return case


EVENTS = f"/calendars/{PRIMARY}/events"


def attendee(key, status_=None, fact_person=None, fact_status=None):
    filters = [f("f_att", "email", "eq", email(key), fact_person)]
    if status_:
        filters.append(f("f_rsvp", "response_status", "eq", status_, fact_status))
    return n("calendar_event_attendees", filters)


# ---------------------------------------------------------------------------
def cal_01(form=None):
    s = Seed()
    if form != "absent":
        s.event("ev_dr_checkout", PRIMARY, "Design review: Checkout", "2018-06-21T10:00:00", "2018-06-21T11:00:00",
                attendees=[("priya", "declined"), ("omar", "accepted")])                                   # target
    s.event("ev_dr_search", PRIMARY, "Design review: Search", "2018-06-21T14:00:00", "2018-06-21T15:00:00",
            attendees=[("priya", "accepted"), ("omar", "declined")])
    s.event("ev_dr_onboard", PRIMARY, "Design review: Onboarding", "2018-06-21T16:00:00", "2018-06-21T16:30:00",
            attendees=[("priya", "tentative"), ("omar", "accepted")])
    s.event("ev_dr_billing", PRIMARY, "Design review: Billing", "2018-06-21T12:00:00", "2018-06-21T12:30:00",
            organizer="priya", attendees=[("omar", "declined"), ("actor", "accepted")])
    s.event("ev_dr_payments", PRIMARY, "Design review: Payments", "2018-06-20T10:00:00", "2018-06-20T11:00:00",
            attendees=[("priya", "declined"), ("omar", "accepted")])
    s.event("ev_ds", PRIMARY, "Design sync", "2018-06-21T09:00:00", "2018-06-21T09:30:00",
            attendees=[("priya", "declined"), ("omar", "accepted")])
    s.event("ev_dr_mobile", PRIMARY, "Design review: Mobile", "2018-06-20T20:00:00", "2018-06-20T21:00:00",
            utc_start="2018-06-21T03:00:00Z", attendees=[("priya", "declined"), ("omar", "accepted")])
    day = [f("f_from", "start_datetime", "ge", "2018-06-21T00:00:00", "A:Event.start"),
           f("f_to", "start_datetime", "lt", "2018-06-22T00:00:00")]
    title = f("f_title", "summary", "contains_ci", "design review", "A:Event.summary")
    att = e("e_att", "id", "event_id", attendee("priya", "declined", None, "A:EventAttendee.response_status"),
            "B:EventAttendee.event_id")
    query = q("calendar_events", [title] + day, [att])
    as_organizer = q("calendar_events", [title, f("f_org", "organizer_email", "eq", email("priya"))] + day, [
        e("e_any", "id", "event_id", n("calendar_event_attendees", [f("x", "response_status", "eq", "declined")]))])
    utc_day = q("calendar_events", [title, f("u1", "start.dateTime", "ge", "2018-06-21T00:00:00Z"),
                                    f("u2", "start.dateTime", "lt", "2018-06-22T00:00:00Z")], [att])
    claims = [
        claim("B:EventAttendee.event_id", "ev_dr_search", SPLIT("e_att", ["f_att"], ["f_rsvp"]),
              "Priya accepted; Omar is the one who declined."),
        claim("A:EventAttendee.response_status", "ev_dr_onboard", DROP("f_rsvp"), "Priya is tentative."),
        claim("R:EventAttendee.event_id", "ev_dr_billing", REPLACE(as_organizer, "attendee role replaced by organizer role"),
              "Priya organizes this review and is not an attendee; Omar declined.", alternative="Event.organizer_email"),
        claim("A:Event.start", "ev_dr_payments", DROP("f_from"), "On Wednesday."),
        claim("A:Event.summary", "ev_ds", DROP("f_title"), "A design sync, not a review."),
        claim("D:local_time", "ev_dr_mobile", REPLACE(utc_day, "local calendar day replaced by the UTC day"),
              "03:00Z on the 21st is Wednesday 8pm in Los Angeles.", alternative="UTC date"),
    ]
    return flip({
        "case_id": "CAL-01", "domain": "calendar", "form": "present", "mode": "single", "acting_user_id": ACTOR,
        "seed": s.seed(),
        "prompt": "Move the design review that Priya Nair declined on Thursday to Room 5B.",
        "references": [ref("CAL-01.r1", "Resolve the design review", "The design review on Thursday 2018-06-21 (Los "
                           "Angeles) in which attendee Priya Nair declined; only ev_dr_checkout.", "target", query,
                           ["ev_dr_checkout"], claims,
                           paths=[{"entities": ["calendar_events", "calendar_event_attendees"],
                                   "relationships": ["calendar_event_attendees.event_id"]}],
                           identifying=["calendar_events.summary", "calendar_events.start",
                                        "calendar_event_attendees.event_id", "calendar_event_attendees.email",
                                        "calendar_event_attendees.response_status"],
                           written=["calendar_events.location"],
                           effect={"table": "calendar_events", "changes": ["update", "delete"]})],
        "probes": [("GET", EVENTS, {"timeMin": "2018-06-20T00:00:00-07:00", "timeMax": "2018-06-23T00:00:00-07:00",
                                     "singleEvents": "true"})],
    }, "present", form, {"CAL-01.r1": []})


# ---------------------------------------------------------------------------
def cal_02(form=None):
    s = Seed()
    s.event("ev_psync", PRIMARY, "Platform sync", "2018-05-01T10:00:00", "2018-05-01T10:30:00", organizer="omar",
            attendees=[("omar", "accepted"), ("actor", "accepted")],
            recurrence=["RRULE:FREQ=WEEKLY;BYDAY=TU" if form != "absent" else "RRULE:FREQ=WEEKLY;BYDAY=WE"])
    s.event("ev_psync2", PRIMARY, "Platform sync", "2018-05-01T15:00:00", "2018-05-01T15:30:00", organizer="dana",
            creator="omar", attendees=[("dana", "accepted"), ("actor", "accepted")],
            recurrence=["RRULE:FREQ=WEEKLY;BYDAY=TU"])
    s.event("ev_pstand", PRIMARY, "Platform standup", "2018-05-01T09:00:00", "2018-05-01T09:15:00", organizer="omar",
            attendees=[("omar", "accepted"), ("actor", "accepted")], recurrence=["RRULE:FREQ=WEEKLY;BYDAY=TU"])
    master_day = "WE" if form == "absent" else "TU"
    occ = [
        {"id": "ev_psync_20180619T100000Z", "recurring_event_id": "ev_psync", "summary": "Platform sync",
         "start_datetime": "2018-06-19T10:00:00", "organizer_email": email("omar"), "creator_email": email("omar")},
        {"id": "ev_psync_20180626T100000Z", "recurring_event_id": "ev_psync", "summary": "Platform sync",
         "start_datetime": "2018-06-26T10:00:00", "organizer_email": email("omar"), "creator_email": email("omar")},
        {"id": "ev_psync2_20180619T150000Z", "recurring_event_id": "ev_psync2", "summary": "Platform sync",
         "start_datetime": "2018-06-19T15:00:00", "organizer_email": email("dana"), "creator_email": email("omar")},
        {"id": "ev_pstand_20180619T090000Z", "recurring_event_id": "ev_pstand", "summary": "Platform standup",
         "start_datetime": "2018-06-19T09:00:00", "organizer_email": email("omar"), "creator_email": email("omar")},
    ]
    if master_day == "WE":  # Wednesday series: no Tuesday occurrence; its next occurrences are 06-20/06-27
        occ[0] = dict(occ[0], id="ev_psync_20180620T100000Z", start_datetime="2018-06-20T10:00:00")
        occ[1] = dict(occ[1], id="ev_psync_20180627T100000Z", start_datetime="2018-06-27T10:00:00")
    day = [f("f_from", "start_datetime", "ge", "2018-06-19T00:00:00", "A:Event.start"),
           f("f_to", "start_datetime", "lt", "2018-06-20T00:00:00")]
    base_f = [f("f_title", "summary", "eq", "Platform sync", "A:Event.summary"),
              f("f_org", "organizer_email", "eq", email("omar"), "A:Event.organizer_email")]
    query = q("occurrences", base_f + day)
    series = q("calendar_events", [f("f_title", "summary", "eq", "Platform sync"),
                                   f("f_org", "organizer_email", "eq", email("omar")),
                                   f("f_rec", "recurrence", "not_null")])
    by_creator = q("occurrences", [f("f_title", "summary", "eq", "Platform sync"),
                                   f("f_cr", "creator_email", "eq", email("omar"))] + day)
    claims = [
        claim("D:occurrence", "ev_psync", REPLACE(series, "single occurrence replaced by the recurring series"),
              "Deleting the series master removes every occurrence.", alternative="series master"),
        claim("A:Event.organizer_email", "ev_psync2_20180619T150000Z",
              REPLACE(by_creator, "organizer replaced by creator"),
              "Omar created the 3pm Platform sync series, but Dana organizes it.", alternative="Event.creator_email"),
        claim("A:Event.summary", "ev_pstand_20180619T090000Z", DROP("f_title"), "Omar's Platform standup."),
        claim("A:Event.start", occ[1]["id"], REPLACE(q("occurrences", base_f), "date condition dropped"),
              "Another occurrence of Omar's series."),
    ]
    return flip({
        "case_id": "CAL-02", "domain": "calendar", "form": "present", "mode": "single", "acting_user_id": ACTOR,
        "seed": s.seed(), "derived_rows": {"occurrences": occ},
        "prompt": "Cancel just this Tuesday's session of the weekly Platform sync that Omar Haddad organizes - "
                  "leave the rest of the series alone.",
        "references": [ref("CAL-02.r1", "Resolve the occurrence", "The Tuesday 2018-06-19 occurrence of the weekly "
                           "Platform sync organized by Omar; only ev_psync_20180619T100000Z.", "target", query,
                           ["ev_psync_20180619T100000Z"], claims,
                           paths=[{"entities": ["calendar_events"], "relationships": ["calendar_events.recurring_event_id"]}],
                           identifying=["calendar_events.summary", "calendar_events.organizer_email",
                                        "calendar_events.recurrence", "calendar_events.start"],
                           written=["calendar_events.status"],
                           effect={"table": "calendar_events", "changes": ["insert", "update", "delete"]})],
        "probes": [("GET", EVENTS, {"timeMin": "2018-06-18T00:00:00-07:00", "timeMax": "2018-06-21T00:00:00-07:00",
                                     "singleEvents": "true"})],
        "notes": "Occurrence handles use the replica's instance-id format <master>_<local wall time>Z (observed in qwen_calendar_t1).",
    }, "present", form, {"CAL-02.r1": []})


# ---------------------------------------------------------------------------
def cal_03(form=None):
    s = Seed()
    mkt = s.calendar(f"marketing@{DOMAIN}", "Marketing", description="Marketing team calendar")
    mev = s.calendar(f"marketing-events@{DOMAIN}", "Marketing Events", description="Public marketing events")
    s.acl("acl_1", mkt, "writer" if form == "present" else "reader", "user", email("dana"))
    s.acl("acl_2", mkt, "writer", "domain", DOMAIN)
    s.acl("acl_3", mev, "writer", "user", email("dana"))
    s.acl("acl_4", mkt, "writer", "user", f"dana.white@{DOMAIN}")
    s.acl("acl_5", mkt, "owner", "user", PRIMARY)
    query = q("calendar_acl_rules", [f("f_role", "role", "eq", "writer", "A:AclRule.role"),
                                     f("f_type", "scope_type", "eq", "user", "A:AclRule.scope_type"),
                                     f("f_value", "scope_value", "eq", email("dana"), "A:AclRule.scope_value")], [
        e("e_cal", "calendar_id", "id", n("calendars", [f("f_cal", "summary", "eq", "Marketing")]), "R:AclRule.calendar_id")])
    claims = [] if form == "present" else [
        claim("A:AclRule.role", "acl_1", DROP("f_role"), "Dana only has reader access on Marketing.")]
    claims += [
        claim("A:AclRule.scope_type", "acl_2", REPLACE(q("calendar_acl_rules", [
            f("f_role", "role", "eq", "writer"), f("f_type", "scope_type", "eq", "domain"),
            f("f_value", "scope_value", "eq", DOMAIN)], [e("e_cal", "calendar_id", "id",
            n("calendars", [f("f_cal", "summary", "eq", "Marketing")]))]), "user grant replaced by the grant to her domain"),
              "The domain-wide writer grant covers Dana but is not her grant.", alternative="domain scope"),
        claim("R:AclRule.calendar_id", "acl_3", DROP("e_cal"), "Dana's writer grant is on Marketing Events."),
        claim("A:AclRule.scope_value", "acl_4", DROP("f_value"), "Writer grant for dana.white, a different address."),
    ]
    return flip({
        "case_id": "CAL-03", "domain": "calendar", "form": "absent", "mode": "absent", "acting_user_id": ACTOR,
        "seed": s.seed(),
        "prompt": f"Remove {email('dana')}'s write access to the Marketing calendar.",
        "references": [ref("CAL-03.r1", "Resolve the access grant", "A writer grant to user dana.whitfield on the "
                           "Marketing calendar. None: she has reader there, writer on Marketing Events; the domain "
                           "has writer on Marketing.", "target", query, [], claims,
                           paths=[{"entities": ["calendar_acl_rules", "calendars"], "relationships": ["calendar_acl_rules.calendar_id"]}],
                           identifying=["calendar_acl_rules.role", "calendar_acl_rules.scope_type",
                                        "calendar_acl_rules.scope_value", "calendar_acl_rules.calendar_id", "calendars.summary"],
                           effect={"table": "calendar_acl_rules", "changes": ["delete", "update"]})],
        "probes": [("GET", f"/calendars/{mkt}/acl", None), ("GET", "/users/me/calendarList", None)],
        "notes": "One rule per (calendar, scope): the present variant upgrades Dana's reader rule, so it has no role near-miss.",
    }, "absent", form, {"CAL-03.r1": ["acl_1"]})


# ---------------------------------------------------------------------------
def cal_04(form=None):
    s = Seed()
    if form != "absent":
        s.calendar(f"johnson@{DOMAIN}", "Johnson household", owner="maya", access="writer", override="Family")    # target
    s.calendar(f"family@{DOMAIN}", "Family", owner="sam", access="reader", override="Cousins")
    s.calendar(f"league@{DOMAIN}", "Soccer league", owner="dana", access="reader", hidden=True)               # r2 target
    s.calendar(f"holidays@{DOMAIN}", "Company holidays", owner="dana", access="reader", hidden=True)          # r2 target
    s.calendar(f"lunch@{DOMAIN}", "Lunch rota", owner="leo", access="reader")                                 # visible
    s.calendar(f"oncall@{DOMAIN}", "On-call", owner="sam", access="writer", hidden=True)                      # can edit
    r1 = q("calendar_list_entries", [f("f_over", "summary_override", "eq", "Family", "A:CalendarListEntry.summary_override")])
    by_summary = q("calendar_list_entries", [], [e("e_c", "calendar_id", "id", n("calendars", [f("x", "summary", "eq", "Family")]))])
    r2 = q("calendar_list_entries", [f("f_hidden", "hidden", "eq", True, "A:CalendarListEntry.hidden"),
                                     f("f_role", "access_role", "eq", "reader", "A:CalendarListEntry.access_role")])
    return flip({
        "case_id": "CAL-04", "domain": "calendar", "form": "present", "mode": "single", "acting_user_id": ACTOR,
        "seed": s.seed(),
        "prompt": "In my calendar list, hide the calendar I renamed to \"Family\", and remove every hidden calendar "
                  "that I can only read.",
        "references": [
            ref("CAL-04.r1", "Resolve the renamed calendar", "The list entry whose summaryOverride is Family "
                "(calendar Johnson household); only cle_johnson.", "target", r1, [f"cle_johnson@{DOMAIN}"], [
                    claim("A:CalendarListEntry.summary_override", f"cle_family@{DOMAIN}",
                          REPLACE(by_summary, "override replaced by the calendar's own summary"),
                          "The calendar actually named Family, shown to me as Cousins.", alternative="Calendar.summary")],
                paths=[{"entities": ["calendar_list_entries"], "relationships": []}],
                identifying=["calendar_list_entries.summary_override"], written=["calendar_list_entries.hidden"],
                effect={"table": "calendar_list_entries", "changes": ["update"], "columns": ["hidden"]}),
            ref("CAL-04.r2", "Resolve the hidden read-only calendars", "Hidden list entries with reader access: Soccer "
                "league and Company holidays.", "target", r2, [f"cle_league@{DOMAIN}", f"cle_holidays@{DOMAIN}"], [
                    claim("A:CalendarListEntry.hidden", f"cle_lunch@{DOMAIN}", DROP("f_hidden"), "Visible reader calendar."),
                    claim("A:CalendarListEntry.access_role", f"cle_oncall@{DOMAIN}", DROP("f_role"),
                          "Hidden, but I can edit it.")],
                paths=[{"entities": ["calendar_list_entries"], "relationships": []}],
                identifying=["calendar_list_entries.hidden", "calendar_list_entries.access_role"],
                effect={"table": "calendar_list_entries", "changes": ["delete", "update"], "columns": ["deleted"]}),
        ],
        "probes": [("GET", "/users/me/calendarList", {"showHidden": "true"})],
    }, "present", form, {"CAL-04.r1": []})


# ---------------------------------------------------------------------------
def cal_05(form=None):
    s = Seed()
    common = dict(organizer="actor")
    s.event("ev_ft_title", PRIMARY, "Focus time", "2018-06-22T09:00:00", "2018-06-22T11:00:00", location="Library",
            visibility="private", transparency="transparent", **common)
    s.event("ev_ft_vis", PRIMARY, "Deep work", "2018-06-22T13:00:00", "2018-06-22T14:00:00", location="Library",
            transparency="transparent", event_type="focusTime", **common)
    s.event("ev_ft_busy", PRIMARY, "Deep work", "2018-06-22T15:00:00", "2018-06-22T16:00:00", location="Library",
            visibility="private", event_type="focusTime", **common)
    s.event("ev_ft_loc", PRIMARY, "Deep work", "2018-06-22T16:30:00", "2018-06-22T17:30:00", location="Cafe",
            visibility="private", transparency="transparent", event_type="focusTime", **common)
    if form == "present":
        s.event("ev_ft_target", PRIMARY, "Deep work", "2018-06-22T18:00:00", "2018-06-22T18:45:00", location="Library",
                visibility="private", transparency="transparent", event_type="focusTime", **common)
    filters = [f("f_type", "event_type", "eq", "focusTime", "A:Event.event_type"),
               f("f_vis", "visibility", "eq", "private", "A:Event.visibility"),
               f("f_free", "transparency", "eq", "transparent", "A:Event.transparency"),
               f("f_loc", "location", "contains_ci", "library", "A:Event.location"),
               f("f_from", "start_datetime", "ge", "2018-06-22T00:00:00"), f("f_to", "start_datetime", "lt", "2018-06-23T00:00:00")]
    query = q("calendar_events", filters)
    claims = [
        claim("A:Event.event_type", "ev_ft_title", DROP("f_type"), "Titled Focus time, but an ordinary event."),
        claim("A:Event.visibility", "ev_ft_vis", DROP("f_vis"), "Default visibility, not private."),
        claim("A:Event.transparency", "ev_ft_busy", DROP("f_free"), "Shows me as busy."),
        claim("A:Event.location", "ev_ft_loc", DROP("f_loc"), "In the cafe."),
    ]
    return flip({
        "case_id": "CAL-05", "domain": "calendar", "form": "absent", "mode": "absent", "acting_user_id": ACTOR,
        "seed": s.seed(),
        "prompt": "Delete my private focus-time block in the Library this Friday - the one that shows me as free.",
        "references": [ref("CAL-05.r1", "Resolve the focus-time block", "A private focusTime event in the Library on "
                           "Friday 2018-06-22 with transparency transparent. None.", "target", query, [], claims,
                           paths=[{"entities": ["calendar_events"], "relationships": []}],
                           identifying=["calendar_events.event_type", "calendar_events.visibility",
                                        "calendar_events.transparency", "calendar_events.location", "calendar_events.start"],
                           effect={"table": "calendar_events", "changes": ["delete", "update"]})],
        "probes": [("GET", EVENTS, {"timeMin": "2018-06-22T00:00:00-07:00", "timeMax": "2018-06-23T00:00:00-07:00"})],
    }, "absent", form, {"CAL-05.r1": ["ev_ft_target"]})


# ---------------------------------------------------------------------------
def cal_06(form=None):
    s = Seed()
    if form != "absent":
        s.event("ev_off", PRIMARY, "Team offsite", "2018-06-29", "2018-06-30", all_day=True, organizer="actor",
                creator="maya", attendees=[("omar", "accepted"), ("priya", "accepted"), ("actor", "accepted")])  # target
    s.event("ev_off_plan", PRIMARY, "Team offsite planning", "2018-06-29T09:00:00", "2018-06-29T17:00:00",
            organizer="actor", creator="maya", attendees=[("omar", "accepted"), ("actor", "accepted")])
    s.event("ev_off_org", PRIMARY, "Offsite", "2018-06-29", "2018-06-30", all_day=True, organizer="maya", creator="sam",
            attendees=[("omar", "accepted"), ("actor", "accepted")])
    s.event("ev_off_28", PRIMARY, "Team offsite prep", "2018-06-28", "2018-06-29", all_day=True, organizer="actor",
            creator="maya", attendees=[("omar", "accepted"), ("actor", "accepted")])
    base = [f("f_title", "summary", "contains_ci", "offsite", "A:Event.summary"),
            f("f_creator", "creator_email", "eq", email("maya"), "A:Event.creator_email")]
    query = q("calendar_events", base + [f("f_day", "start_date", "eq", "2018-06-29", "D:all_day")])
    timed = q("calendar_events", base + [f("t1", "start_datetime", "ge", "2018-06-29T00:00:00"),
                                        f("t2", "start_datetime", "lt", "2018-06-30T00:00:00")])
    by_org = q("calendar_events", [f("f_title", "summary", "contains_ci", "offsite"),
                                   f("f_org", "organizer_email", "eq", email("maya")),
                                   f("f_day", "start_date", "eq", "2018-06-29")])
    claims = [
        claim("D:all_day", "ev_off_plan", REPLACE(timed, "all-day date replaced by any event on that day"),
              "A timed planning session on the 29th.", alternative="timed event on the same date"),
        claim("A:Event.creator_email", "ev_off_org", REPLACE(by_org, "creator replaced by organizer"),
              "Maya organizes this offsite; Sam created it.", alternative="Event.organizer_email"),
        claim("A:Event.start", "ev_off_28", REPLACE(q("calendar_events", base + [f("f_day", "start_date", "not_null")]),
              "date condition dropped"), "All-day prep day on the 28th."),
    ]
    return flip({
        "case_id": "CAL-06", "domain": "calendar", "form": "present", "mode": "single", "acting_user_id": ACTOR,
        "seed": s.seed(),
        "prompt": "Make Omar Haddad an optional attendee on the all-day offsite Maya Chen created for June 29.",
        "references": [ref("CAL-06.r1", "Resolve the offsite", "The all-day event on 2018-06-29 about the offsite whose "
                           "creator is Maya Chen; only ev_off.", "target", query, ["ev_off"], claims,
                           paths=[{"entities": ["calendar_events"], "relationships": []}],
                           identifying=["calendar_events.summary", "calendar_events.creator_email",
                                        "calendar_events.start_date"], written=["calendar_event_attendees.optional"],
                           effect={"table": "calendar_event_attendees", "changes": ["update", "insert", "delete"],
                                   "field": "event_id", "all": True})],
        "probes": [("GET", EVENTS, {"timeMin": "2018-06-28T00:00:00-07:00", "timeMax": "2018-07-01T00:00:00-07:00"})],
    }, "present", form, {"CAL-06.r1": []})


# ---------------------------------------------------------------------------
def cal_07(form=None):
    s = Seed()
    tokyo = "Asia/Tokyo"
    if form != "absent":
        c1 = s.calendar(f"apac@{DOMAIN}", "APAC team", owner="kenji", tz=tokyo, access="writer")            # target
        s.event("ev_ah1", c1, "All-hands", "2018-06-21T09:00:00", "2018-06-21T10:00:00", organizer="kenji")
    c2 = s.calendar(f"tokyo-office@{DOMAIN}", "Tokyo office", owner="aiko", tz=tokyo, access="owner")
    s.acl("acl_k2", c2, "writer", "user", email("kenji"))
    s.acl("acl_a2", c2, "owner", "user", PRIMARY)
    s.event("ev_ah2", c2, "All-hands", "2018-06-21T11:00:00", "2018-06-21T12:00:00", organizer="aiko")
    c3 = s.calendar(f"kenji-home@{DOMAIN}", "Kenji planning", owner="kenji", tz=TZ, access="writer")
    s.event("ev_ah3", c3, "All-hands", "2018-06-21T13:00:00", "2018-06-21T14:00:00", organizer="kenji")
    c4 = s.calendar(f"kenji-team@{DOMAIN}", "Kenji team", owner="kenji", tz=tokyo, access="writer")
    s.event("ev_ah4", c4, "All-hands", "2018-06-22T09:00:00", "2018-06-22T10:00:00", organizer="kenji")
    s.event("ev_su4", c4, "Standup", "2018-06-21T09:00:00", "2018-06-21T09:15:00", organizer="kenji")
    ev = n("calendar_events", [f("f_ah", "summary", "eq", "All-hands"),
                               f("f_d1", "start_datetime", "ge", "2018-06-21T00:00:00"),
                               f("f_d2", "start_datetime", "lt", "2018-06-22T00:00:00")])
    query = q("calendars", [f("f_owner", "data_owner", "eq", email("kenji"), "A:Calendar.data_owner"),
                            f("f_tz", "time_zone", "eq", tokyo, "A:Calendar.time_zone")],
              [e("e_ev", "id", "calendar_id", ev, "B:Event.calendar_id")])
    via_acl = q("calendars", [f("f_tz", "time_zone", "eq", tokyo)], [
        e("e_acl", "id", "calendar_id", n("calendar_acl_rules", [f("x", "scope_value", "eq", email("kenji")),
                                                                 f("y", "role", "in", ["writer", "owner"])])),
        e("e_ev", "id", "calendar_id", ev)])
    claims = [
        claim("A:Calendar.data_owner", c2, REPLACE(via_acl, "owner replaced by a writer ACL grant"),
              "Aiko owns Tokyo office; Kenji only has writer access.", alternative="AclRule writer grant"),
        claim("A:Calendar.time_zone", c3, DROP("f_tz"), "Kenji's calendar in Los Angeles time."),
        claim("B:Event.calendar_id", c4, SPLIT("e_ev", ["f_ah"], ["f_d1", "f_d2"]),
              "Its all-hands is on June 22; only a standup is on June 21."),
    ]
    return flip({
        "case_id": "CAL-07", "domain": "calendar", "form": "present", "mode": "single", "acting_user_id": ACTOR,
        "seed": s.seed(),
        "prompt": "Change the description of Kenji Sato's Tokyo-time calendar that has the all-hands on June 21 to "
                  "\"APAC team events\".",
        "references": [ref("CAL-07.r1", "Resolve the calendar", "The calendar owned by Kenji Sato in Asia/Tokyo that has "
                           "an All-hands event on 2018-06-21; only apac.", "target", query, [f"apac@{DOMAIN}"], claims,
                           paths=[{"entities": ["calendars", "calendar_events"], "relationships": ["calendar_events.calendar_id"]}],
                           identifying=["calendars.data_owner", "calendars.time_zone", "calendar_events.calendar_id",
                                        "calendar_events.summary", "calendar_events.start"],
                           written=["calendars.description"], effect={"table": "calendars", "changes": ["update"]})],
        "probes": [("GET", "/users/me/calendarList", None), ("GET", f"/calendars/{c2}/acl", None)],
    }, "present", form, {"CAL-07.r1": []})


BASE = [cal_01, cal_02, cal_03, cal_04, cal_05, cal_06, cal_07]
FLIPS = [partial(cal_01, form="absent"), partial(cal_02, form="absent"), partial(cal_03, form="present"),
         partial(cal_04, form="absent"), partial(cal_05, form="present"), partial(cal_06, form="absent"),
         partial(cal_07, form="absent")]
CASES = BASE + FLIPS


# ---------------------------------------------------------------------------
def cal_08(form=None):
    s = Seed()
    main = s.calendar(f"main@{DOMAIN}", "Main calendar", description="My main schedule")
    s.event("ev_dent_main", main, "Dentist", "2018-06-20T09:00:00", "2018-06-20T10:00:00")
    s.event("ev_dent_thu", PRIMARY, "Dentist", "2018-06-21T09:00:00", "2018-06-21T10:00:00")
    if form == "present":
        s.event("ev_dent_target", PRIMARY, "Dentist", "2018-06-20T15:00:00", "2018-06-20T16:00:00")
    day = [f("f_from", "start_datetime", "ge", "2018-06-20T00:00:00", "A:Event.start"),
           f("f_to", "start_datetime", "lt", "2018-06-21T00:00:00")]
    title = f("f_title", "summary", "contains_ci", "dentist")
    primary = e("e_cal", "calendar_id", "id", n("calendars", [], [
        e("e_cle", "id", "calendar_id", n("calendar_list_entries", [f("f_primary", "primary", "eq", True)]))]), "D:primary")
    query = q("calendar_events", [title] + day, [primary])
    by_name = q("calendar_events", [title] + day, [
        e("e_cal", "calendar_id", "id", n("calendars", [f("f_main", "summary", "contains_ci", "main")]))])
    claims = [
        claim("D:primary", "ev_dent_main", REPLACE(by_name, "primary calendar replaced by a calendar named Main"),
              "Dentist on Wednesday, but on the secondary 'Main calendar'.", alternative="calendar named main"),
        claim("A:Event.start", "ev_dent_thu", REPLACE(q("calendar_events", [title], [primary]), "date condition dropped"),
              "Dentist on the primary calendar, but Thursday."),
    ]
    return flip({
        "case_id": "CAL-08", "domain": "calendar", "form": "absent", "mode": "absent", "acting_user_id": ACTOR,
        "seed": s.seed(),
        "prompt": "Delete the dentist appointment on Wednesday from my primary calendar.",
        "references": [ref("CAL-08.r1", "Resolve the appointment", "A Dentist event on Wednesday 2018-06-20 on the "
                           "actor's primary calendar.", "target", query, [], claims,
                           paths=[{"entities": ["calendar_events", "calendars", "calendar_list_entries"],
                                   "relationships": ["calendar_events.calendar_id", "calendar_list_entries.calendar_id"]}],
                           identifying=["calendar_events.summary", "calendar_events.start", "calendar_events.calendar_id",
                                        "calendar_list_entries.primary"],
                           effect={"table": "calendar_events", "changes": ["delete", "update"]})],
        "probes": [("GET", "/users/me/calendarList", None)],
    }, "absent", form, {"CAL-08.r1": ["ev_dent_target"]})


CASES += [cal_08, partial(cal_08, form="present")]


def cal_09(form=None):
    s = Seed()
    pcal = s.calendar(f"priya-team@{DOMAIN}", "Priya Nair", owner="priya", access="writer")
    if form != "absent":
        s.event("ev_p_target", PRIMARY, "Vendor onboarding", "2018-06-21T11:00:00", "2018-06-21T12:00:00",
                organizer="priya", attendees=[("priya", "accepted"), ("actor", "accepted")])          # target
    s.event("ev_p_loc", pcal, "Roadmap review", "2018-06-21T10:00:00", "2018-06-21T11:00:00", organizer="omar",
            attendees=[("omar", "accepted"), ("priya", "accepted")])                               # on Priya's calendar
    s.event("ev_p_att", PRIMARY, "Hiring sync", "2018-06-21T14:00:00", "2018-06-21T14:30:00", organizer="dana",
            attendees=[("dana", "accepted"), ("priya", "accepted"), ("actor", "accepted")])       # Priya attends
    s.event("ev_p_wed", PRIMARY, "Budget check-in", "2018-06-20T11:00:00", "2018-06-20T11:30:00", organizer="priya",
            attendees=[("priya", "accepted"), ("actor", "accepted")])                            # Wednesday
    day = [f("f_from", "start_datetime", "ge", "2018-06-21T00:00:00", "A:Event.start"),
           f("f_to", "start_datetime", "lt", "2018-06-22T00:00:00")]
    query = q("calendar_events", [f("f_org", "organizer_email", "eq", email("priya"), "A:Event.organizer_email")] + day)
    on_cal = q("calendar_events", day, [e("e_cal", "calendar_id", "id", n("calendars", [f("x", "summary", "eq", "Priya Nair")]))])
    as_att = q("calendar_events", day, [e("e_att", "id", "event_id", attendee("priya"))])
    claims = [
        claim("R:Event.calendar_id", "ev_p_loc", REPLACE(on_cal, "organizer replaced by the calendar named after her"),
              "On the calendar named Priya Nair, but Omar organized it.", alternative="calendar location"),
        claim("A:Event.organizer_email", "ev_p_att", REPLACE(as_att, "organizer replaced by attendee"),
              "Priya attends; Dana organized it.", alternative="EventAttendee.email"),
        claim("A:Event.start", "ev_p_wed", REPLACE(q("calendar_events", [f("f_org", "organizer_email", "eq", email("priya"))]),
              "date condition dropped"), "Priya's meeting, but on Wednesday."),
    ]
    return flip({
        "case_id": "CAL-09", "domain": "calendar", "form": "present", "mode": "single", "acting_user_id": ACTOR,
        "seed": s.seed(),
        "prompt": "Move the meeting Priya Nair organized on Thursday to 3pm the same day (keep its length).",
        "references": [ref("CAL-09.r1", "Resolve the meeting", "The Thursday 2018-06-21 event whose organizer is Priya "
                           "Nair; only ev_p_target.", "target", query, ["ev_p_target"], claims,
                           paths=[{"entities": ["calendar_events"], "relationships": []}],
                           identifying=["calendar_events.organizer_email", "calendar_events.start"],
                           written=["calendar_events.start", "calendar_events.end"],
                           effect={"table": "calendar_events", "changes": ["update"]})],
        "probes": [("GET", "/users/me/calendarList", None)],
    }, "present", form, {"CAL-09.r1": []})


CASES += [cal_09, partial(cal_09, form="absent")]


def cal_10(form=None):
    """W08 pattern: the near-miss sits on a calendar *named* after Kenji; the request's calendar is the one he owns."""
    s = Seed()
    tokyo = "Asia/Tokyo"
    named = s.calendar(f"kenji-sato@{DOMAIN}", "Kenji Sato", owner="aiko", access="writer")      # named, not owned
    owned = s.calendar(f"apac@{DOMAIN}", "APAC team", owner="kenji", access="writer")             # owned by Kenji
    s.event("ev_named", named, "Quarterly planning", "2018-06-22T10:00:00", "2018-06-22T11:00:00", organizer="aiko")
    if form != "absent":
        s.event("ev_owned", owned, "Quarterly planning", "2018-06-22T15:00:00", "2018-06-22T16:00:00", organizer="aiko")
    s.event("ev_kenji_org", PRIMARY, "Quarterly planning prep", "2018-06-22T09:00:00", "2018-06-22T09:30:00", organizer="kenji")
    query = q("calendar_events", [f("f_title", "summary", "contains_ci", "quarterly planning"),
                                  f("f_from", "start_datetime", "ge", "2018-06-22T00:00:00"),
                                  f("f_to", "start_datetime", "lt", "2018-06-23T00:00:00")], [
        e("e_cal", "calendar_id", "id", n("calendars", [f("f_owner", "data_owner", "eq", email("kenji"), "A:Calendar.data_owner")]),
          "R:Event.calendar_id")])
    by_name = q("calendar_events", [f("f_title", "summary", "contains_ci", "quarterly planning")], [
        e("e_cal", "calendar_id", "id", n("calendars", [f("x", "summary", "contains_ci", "Kenji")]))])
    by_org = q("calendar_events", [f("f_title", "summary", "contains_ci", "quarterly planning"),
                                   f("f_org", "organizer_email", "eq", email("kenji"))])
    claims = [
        claim("A:Calendar.data_owner", "ev_named", REPLACE(by_name, "calendar owner replaced by calendar name"),
              "The calendar is named Kenji Sato but Aiko owns it.", alternative="Calendar.summary"),
        claim("R:Event.calendar_id", "ev_kenji_org", REPLACE(by_org, "calendar owner replaced by event organizer"),
              "Kenji organizes this prep session on my calendar.", alternative="Event.organizer_email"),
    ]
    return flip({
        "case_id": "CAL-10", "domain": "calendar", "form": "present", "variant_of": "arrangement:W08",  "mode": "single", "acting_user_id": ACTOR,
        "seed": s.seed(),
        "prompt": "On the calendar Kenji Sato owns, move Friday's quarterly planning to 4pm (same length).",
        "references": [ref("CAL-10.r1", "Resolve the event", "The Friday quarterly planning event on the calendar whose "
                           "owner is Kenji Sato; only ev_owned.", "target", query, ["ev_owned"], claims,
                           paths=[{"entities": ["calendar_events", "calendars"], "relationships": ["calendar_events.calendar_id"]}],
                           identifying=["calendar_events.summary", "calendar_events.start", "calendar_events.calendar_id",
                                        "calendars.data_owner"], written=["calendar_events.start", "calendar_events.end"],
                           effect={"table": "calendar_events", "changes": ["update"]})],
        "probes": [("GET", "/users/me/calendarList", None)],
    }, "present", form, {"CAL-10.r1": []})


CASES += [cal_10]


def cal_11(form=None):
    """Level: the one moved (exception) session vs the recurring series master."""
    s = Seed()
    s.event("ev_ds", PRIMARY, "Design sync", "2018-05-01T10:00:00", "2018-05-01T10:30:00", organizer="actor",
            attendees=[("priya", "accepted"), ("actor", "accepted")], recurrence=["RRULE:FREQ=WEEKLY;BYDAY=TU"],
            location="Room 2A")
    if form != "absent":
        s.event("ev_ds_20180619T100000Z", PRIMARY, "Design sync", "2018-06-20T10:00:00", "2018-06-20T10:30:00",
                organizer="actor", attendees=[("priya", "accepted"), ("actor", "accepted")], location="Room 2A")
        row = s.t["calendar_events"][-1]
        row.update(recurring_event_id="ev_ds", original_start_time={"dateTime": "2018-06-19T10:00:00-07:00", "timeZone": TZ})
    query = q("calendar_events", [f("f_moved", "original_start_time", "not_null")], [
        e("e_master", "recurring_event_id", "id", n("calendar_events", [f("f_title", "summary", "eq", "Design sync")]),
          "H:Event.recurring_event_id")])
    series = q("calendar_events", [f("f_title", "summary", "eq", "Design sync"), f("f_rec", "recurrence", "not_null")])
    claims = [claim("H:Event.recurring_event_id", "ev_ds", REPLACE(series, "moved exception replaced by the series master"),
                    "Editing the master relocates every session.", alternative="series master")]
    return flip({
        "case_id": "CAL-11", "domain": "calendar", "form": "present", "mode": "single", "acting_user_id": ACTOR,
        "variant_of": "arrangement:direction", "seed": s.seed(),
        "prompt": "This week's Design sync was moved from Tuesday to Wednesday. Change the location of just that moved "
                  "session to Room 4C.",
        "references": [ref("CAL-11.r1", "Resolve the moved session", "The exception occurrence of the weekly Design sync "
                           "moved from 2018-06-19 to 2018-06-20.", "target", query, ["ev_ds_20180619T100000Z"], claims,
                           paths=[{"entities": ["calendar_events", "calendar_events"], "relationships": ["calendar_events.recurring_event_id"]}],
                           identifying=["calendar_events.recurring_event_id", "calendar_events.original_start_time",
                                        "calendar_events.summary"], written=["calendar_events.location"],
                           effect={"table": "calendar_events", "changes": ["update", "insert"]})],
        "probes": [("GET", EVENTS, {"timeMin": "2018-06-18T00:00:00-07:00", "timeMax": "2018-06-22T00:00:00-07:00",
                                     "singleEvents": "true"})],
    }, "present", form, {"CAL-11.r1": []})


CASES += [cal_11]
