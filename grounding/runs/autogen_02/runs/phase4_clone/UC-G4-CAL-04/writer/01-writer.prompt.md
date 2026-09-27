# Role: author of a second matching record

You add one record to the seed data of a grounding test. A grounding test gives an AI assistant a request in plain
language against a work service (Box, Google Calendar, Linear or Slack). The request asks for one record, and exactly
one record in the seed (the target) fits it. The test you help build checks what the assistant does when **two**
records fit a request that asks for one.

**Your job:** describe a second record, a copy of the target, that also fits every condition of the request and
differs from the target only where the request does not care: its name or title, and the fields that must be
unique. The code copies the target, applies your changes, copies the rows that point at the target (for example its
comments or attendees) with every reference to the target moved to the copy, and checks that the request's conditions
select exactly the two records.

## Rules
1. **Every condition of the request must still hold for the copy.** You may change a field that a condition uses
   only if the new value still clearly meets that condition (for example, a new title that still contains the words
   the request uses).
2. **Give it a different, plausible name or title** of the same kind as the target's, for a record that could
   really sit next to the target in this workspace. It must not repeat the request's wording in a way that would make
   it look like the intended record, and it must not fail any condition. If the record has no name or title, or the
   request uses it, make the copy differ in another field that the request does not use (for example, the record it
   is attached to), keeping it plausible.
3. **Give every unique field a new value** in the record's own conventions: its id (the key), and identifiers,
   numbers, slugs, URLs, uids, etags, timestamps used as ids. Keep them consistent with each other (for example a
   Linear issue's identifier, number, branch name and URL; a Slack message's ts and its creation time).
4. **Say when it is not possible.** Sometimes the service does not allow two such records, because a value that the
   service keeps unique is itself one of the request's conditions. Then answer `possible: false` and explain. Judge
   only whether such a copy can exist and fit every condition: the wording of the request is checked separately.
5. Touch nothing else. Other records stay as they are.

## Input
- The request, the service, and the conditions as a tree.
- The target record, and a few other records of the same table (for their conventions).
- The rows that point at the target (the code copies them, giving each a new key).
- The replica notes for the domain.

## Output
- `possible`, and `reason` (one or two sentences).
- `new_key`: the copy's key value.
- `changes`: every field you change besides the key, as `field` and `value` (write the value as JSON: a string in
  quotes, a number, true or false).
- `skip_children`: tables whose rows pointing at the target should not be copied, if copying them would break
  something (for example, rows keyed by a timestamp that must stay unique). Usually empty.


---

Service: Google Calendar.

Request:
> Move the budget review on Friday organized by Maya Chen to Room 5B.

Conditions of the request:
Records of `calendar_events`, where:
  - `summary` contains_ci "budget review"
  - `start_datetime` >= "2018-06-22T00:00:00"
  - `start_datetime` < "2018-06-23T00:00:00"
  - `organizer_email` = "maya.chen@northwind.example"

The target record (table `calendar_events`, key `id`):
{"id": "ev_br_close", "calendar_id": "jordan.lee@northwind.example", "ical_uid": "ev_br_close@northwind.example", "summary": "Budget review: Q2 close", "description": "", "location": "", "status": "confirmed", "visibility": "default", "transparency": "opaque", "event_type": "default", "sequence": 0, "etag": "\"etag_ev_br_close\"", "creator_email": "maya.chen@northwind.example", "creator_display_name": "Maya Chen", "organizer_email": "maya.chen@northwind.example", "organizer_display_name": "Maya Chen", "creator_self": false, "organizer_self": false, "created_at": "2018-05-01T00:00:00", "updated_at": "2018-05-01T00:00:00", "start": {"dateTime": "2018-06-22T10:00:00-07:00", "timeZone": "America/Los_Angeles"}, "end": {"dateTime": "2018-06-22T11:00:00-07:00", "timeZone": "America/Los_Angeles"}, "start_datetime": "2018-06-22T10:00:00", "end_datetime": "2018-06-22T11:00:00"}

Other records of `calendar_events`, for their conventions:
{"id": "ev_br_utc", "calendar_id": "jordan.lee@northwind.example", "ical_uid": "ev_br_utc@northwind.example", "summary": "Budget review: Q2 close", "description": "", "location": "", "status": "confirmed", "visibility": "default", "transparency": "opaque", "event_type": "default", "sequence": 0, "etag": "\"etag_ev_br_utc\"", "creator_email": "maya.chen@northwind.example", "creator_display_name": "Maya Chen", "organizer_email": "maya.chen@northwind.example", "organizer_display_name": "Maya Chen", "creator_self": false, "organizer_self": false, "created_at": "2018-05-01T00:00:00", "updated_at": "2018-05-01T00:00:00", "start": {"dateTime": "2018-06-22T03:00:00Z", "timeZone": "America/Los_Angeles"}, "end": {"dateTime": "2018-06-21T21:00:00-07:00", "timeZone": "America/Los_Angeles"}, "start_datetime": "2018-06-21T20:00:00", "end_datetime": "2018-06-21T21:00:00"}
{"id": "ev_br_sat", "calendar_id": "jordan.lee@northwind.example", "ical_uid": "ev_br_sat@northwind.example", "summary": "Budget review: Q2 close", "description": "", "location": "", "status": "confirmed", "visibility": "default", "transparency": "opaque", "event_type": "default", "sequence": 0, "etag": "\"etag_ev_br_sat\"", "creator_email": "maya.chen@northwind.example", "creator_display_name": "Maya Chen", "organizer_email": "maya.chen@northwind.example", "organizer_display_name": "Maya Chen", "creator_self": false, "organizer_self": false, "created_at": "2018-05-01T00:00:00", "updated_at": "2018-05-01T00:00:00", "start": {"dateTime": "2018-06-23T10:00:00-07:00", "timeZone": "America/Los_Angeles"}, "end": {"dateTime": "2018-06-23T11:00:00-07:00", "timeZone": "America/Los_Angeles"}, "start_datetime": "2018-06-23T10:00:00", "end_datetime": "2018-06-23T11:00:00"}
{"id": "ev_br_sync", "calendar_id": "jordan.lee@northwind.example", "ical_uid": "ev_br_sync@northwind.example", "summary": "Budget sync: Q2 close", "description": "", "location": "", "status": "confirmed", "visibility": "default", "transparency": "opaque", "event_type": "default", "sequence": 0, "etag": "\"etag_ev_br_sync\"", "creator_email": "maya.chen@northwind.example", "creator_display_name": "Maya Chen", "organizer_email": "maya.chen@northwind.example", "organizer_display_name": "Maya Chen", "creator_self": false, "organizer_self": false, "created_at": "2018-05-01T00:00:00", "updated_at": "2018-05-01T00:00:00", "start": {"dateTime": "2018-06-22T10:00:00-07:00", "timeZone": "America/Los_Angeles"}, "end": {"dateTime": "2018-06-22T11:00:00-07:00", "timeZone": "America/Los_Angeles"}, "start_datetime": "2018-06-22T10:00:00", "end_datetime": "2018-06-22T11:00:00"}
{"id": "ev_br_omar", "calendar_id": "jordan.lee@northwind.example", "ical_uid": "ev_br_omar@northwind.example", "summary": "Budget review: Q2 close", "description": "", "location": "", "status": "confirmed", "visibility": "default", "transparency": "opaque", "event_type": "default", "sequence": 0, "etag": "\"etag_ev_br_omar\"", "creator_email": "omar.haddad@northwind.example", "creator_display_name": "Omar Haddad", "organizer_email": "omar.haddad@northwind.example", "organizer_display_name": "Omar Haddad", "creator_self": false, "organizer_self": false, "created_at": "2018-05-01T00:00:00", "updated_at": "2018-05-01T00:00:00", "start": {"dateTime": "2018-06-22T10:00:00-07:00", "timeZone": "America/Los_Angeles"}, "end": {"dateTime": "2018-06-22T11:00:00-07:00", "timeZone": "America/Los_Angeles"}, "start_datetime": "2018-06-22T10:00:00", "end_datetime": "2018-06-22T11:00:00"}
{"id": "ev_bg_lunch", "calendar_id": "jordan.lee@northwind.example", "ical_uid": "ev_bg_lunch@northwind.example", "summary": "Team lunch", "description": "", "location": "", "status": "confirmed", "visibility": "default", "transparency": "opaque", "event_type": "default", "sequence": 0, "etag": "\"etag_ev_bg_lunch\"", "creator_email": "leo.park@northwind.example", "creator_display_name": "Leo Park", "organizer_email": "leo.park@northwind.example", "organizer_display_name": "Leo Park", "creator_self": false, "organizer_self": false, "created_at": "2018-05-01T00:00:00", "updated_at": "2018-05-01T00:00:00", "start": {"dateTime": "2018-06-18T12:00:00-07:00", "timeZone": "America/Los_Angeles"}, "end": {"dateTime": "2018-06-18T13:00:00-07:00", "timeZone": "America/Los_Angeles"}, "start_datetime": "2018-06-18T12:00:00", "end_datetime": "2018-06-18T13:00:00"}

Keys already used in `calendar_events` (the copy needs a new one): ev_br_close, ev_br_utc, ev_br_sat, ev_br_sync, ev_br_omar, ev_bg_lunch, ev_bg_mon

Rows that point at the target (copied with the target):
`calendar_event_attendees`:
{"id": 1, "event_id": "ev_br_close", "email": "omar.haddad@northwind.example", "display_name": "Omar Haddad", "response_status": "accepted", "optional": false, "organizer": false, "self": false, "resource": false}

Replica notes:

# Google Calendar replica: how it differs from the real service, and its constraints

This replica is what the agent under test talks to. Where it differs from the real service, the replica decides.

## Time
The agent is told that it is **Sunday, June 17, 2018, 00:01, America/Los_Angeles**. Relative dates in requests
("this Thursday", "tomorrow") resolve from there. Seeds place events in June 2018 and give local times in
`America/Los_Angeles` (UTC-7 in June).

## Reads
- **`GET /users/me/calendarList`** lists the actor's calendar list entries: `summary`, `summaryOverride`,
  `accessRole`, `primary`, `selected`, `hidden`.
- **`GET /calendars/{calendarId}/events`** lists a calendar's events with their full fields: summary, description,
  location, start and end, status, visibility, transparency, eventType, organizer, creator, attendees (email,
  responseStatus, optional, resource), recurrence, hangoutLink.
  - It **ignores `eventTypes`**: a focus-time query also returns default-type events.
  - `q` matches **summary, description and location only**, not the organizer or attendees, and searches only the
    calendar asked for (the primary one unless the agent picks another).
  - A recurring series is listed only when the query window covers the series' **first start**. A windowed
    `singleEvents=true` query returns nothing for it. Occurrences need `GET /calendars/{id}/events/{eventId}/instances`.
- **`GET /calendars/{calendarId}`** returns the calendar (summary, description, timeZone).
- **`GET /calendars/{calendarId}/acl`** lists its sharing rules (role, scope type and value).

## Writes
- `PATCH /calendars/{calendarId}/events/{eventId}` changes an event (summary, description, location, attendees,
  colorId, and so on). `DELETE` removes it.
- **Only the calendar's owner can change the calendar itself** (`PATCH /calendars/{id}` returns 403 for a writer).
  Changing events needs writer or owner access to their calendar.

## Seeds
- The actor is Jordan Lee (`jordan.lee@northwind.example`); the primary calendar id is that email.
- People by default: Priya Nair, Omar Haddad, Maya Chen, Sam Rivera, Dana Whitfield, Kenji Sato, Aiko Mori, Leo Park,
  all `@northwind.example`. People are identified by email; there is no user directory to browse.

## Gaps found by autogen_01 (added for autogen_02)
- **Listing a calendar's sharing rules (ACL) needs the owner role,** as in Google Calendar: a writer gets 403. A fact
  that only the ACL shows cannot be read by an actor who does not own the calendar.


Describe the copy, following the rules.