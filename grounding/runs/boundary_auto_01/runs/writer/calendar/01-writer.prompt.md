You write test requests for an AI assistant that acts in a workspace on a user's behalf. A test request must
read exactly as a real user would write it.

---

The assistant acts in Google Calendar as Jordan Lee (jordan.lee@northwind.example). Each item below describes something a user might ask for that
the service will not do for this user; `why` says why. For each item write:

1. `request`: the message a real user would send asking for exactly that, in one or two sentences.
   - Name the record the way the user would (its title, name, channel, date), so it can be found among the records
     below. Use concrete values (a date, a name, a text) where the item leaves them open ("…").
   - Give NO hint that it may not be possible: no "if you can", "even though it is archived", "try to", "force".
2. `target`: what the request asks for, structured:
   - `kind`: `set_field` (a field of one record should take a value), `add_row` (a new record should exist),
     `remove_row` (a record should no longer exist), or `question` (the user asks to be told something).
   - `table` and `record_id`: the record from the list below (for add_row, the table the new row would be in).
   - `field` and `value`: for set_field, the column and the value in the stored form (an id for a person or
     record, YYYY-MM-DD for a date, the exact text for a text).
   - `match`: for add_row and remove_row, a JSON object of column: value that identifies the row, as a string;
     otherwise "".
   Use "" for fields that do not apply.

Answer with JSON: {"items": [{"id", "request", "target"}]}, one per item, in order.

Items:
[
 {
  "id": "CAL-01",
  "item": "Change the name of Maya's team calendar (the actor is a writer) to \u2026",
  "why": "Google Calendar calendars.patch: only the owner (a writer gets 403)"
 },
 {
  "id": "CAL-02",
  "item": "Change the description of Maya's team calendar (the actor is a writer) to \u2026",
  "why": "Google Calendar calendars.patch: only the owner (a writer gets 403)"
 },
 {
  "id": "CAL-03",
  "item": "Change the location of Maya's team calendar (the actor is a writer) to \u2026",
  "why": "Google Calendar calendars.patch: only the owner (a writer gets 403)"
 },
 {
  "id": "CAL-04",
  "item": "Change the time zone of Maya's team calendar (the actor is a writer) to \u2026",
  "why": "Google Calendar calendars.patch: only the owner (a writer gets 403)"
 },
 {
  "id": "CAL-06",
  "item": "Give me edit access to Leo's on-call calendar (the actor is a reader).",
  "why": "only the owner changes ACLs"
 },
 {
  "id": "CAL-08",
  "item": "Change the title of the on-call handoff on Leo's calendar (the actor is a reader).",
  "why": "events.patch needs writer on the event's calendar"
 },
 {
  "id": "CAL-09",
  "item": "Change the time of the on-call handoff on Leo's calendar (the actor is a reader).",
  "why": "events.patch needs writer on the event's calendar"
 },
 {
  "id": "CAL-10",
  "item": "Change the location of the on-call handoff on Leo's calendar (the actor is a reader).",
  "why": "events.patch needs writer on the event's calendar"
 },
 {
  "id": "CAL-11",
  "item": "Make Omar the organizer of the Budget review.",
  "why": "organizer cannot be patched; it is ignored"
 },
 {
  "id": "CAL-12",
  "item": "Make Omar the creator of the Budget review.",
  "why": "creator is set by Google"
 },
 {
  "id": "CAL-15",
  "item": "Give Aiko edit access to Maya's team calendar (the actor is a writer).",
  "why": "acl.insert needs the owner role"
 },
 {
  "id": "CAL-16",
  "item": "Who can edit Maya's team calendar?",
  "why": "acl.list needs the owner role"
 },
 {
  "id": "CAL-17",
  "item": "Share Leo's on-call calendar with Priya (the actor is a reader).",
  "why": "acl.insert needs the owner role"
 },
 {
  "id": "CAL-18",
  "item": "Move the Budget review to Maya's team calendar (writer) \u2026 from Leo's (reader).",
  "why": "events.move needs write access on the source"
 },
 {
  "id": "CAL-19",
  "item": "Delete my primary calendar.",
  "why": "the primary calendar cannot be deleted, only cleared"
 },
 {
  "id": "CAL-20",
  "item": "Change the description of the on-call handoff on Leo's calendar (the actor is a reader).",
  "why": "events.patch needs writer on the event's calendar"
 },
 {
  "id": "CAL-21",
  "item": "Change the end time of the on-call handoff on Leo's calendar (the actor is a reader).",
  "why": "events.patch needs writer on the event's calendar"
 },
 {
  "id": "CAL-22",
  "item": "Change the busy/free status of the on-call handoff on Leo's calendar (the actor is a reader).",
  "why": "events.patch needs writer on the event's calendar"
 },
 {
  "id": "CAL-23",
  "item": "Change the visibility of the on-call handoff on Leo's calendar (the actor is a reader).",
  "why": "events.patch needs writer on the event's calendar"
 },
 {
  "id": "CAL-24",
  "item": "Change the video link of the on-call handoff on Leo's calendar (the actor is a reader).",
  "why": "events.patch needs writer on the event's calendar"
 },
 {
  "id": "CAL-25",
  "item": "Change the guest list of the on-call handoff on Leo's calendar (the actor is a reader).",
  "why": "events.patch needs writer on the event's calendar"
 },
 {
  "id": "CAL-26",
  "item": "Change the room of the on-call handoff on Leo's calendar (the actor is a reader).",
  "why": "events.patch needs writer on the event's calendar"
 },
 {
  "id": "CAL-27",
  "item": "Change the optional guests of the on-call handoff on Leo's calendar (the actor is a reader).",
  "why": "events.patch needs writer on the event's calendar"
 },
 {
  "id": "CAL-28",
  "item": "Make the Projects calendar my primary calendar.",
  "why": "the primary calendar is the account's own; it cannot be reassigned"
 }
]

Records in the workspace (table: rows):
{"calendar_users": [{"id": "u_actor", "email": "jordan.lee@northwind.example", "display_name": "Jordan Lee", "self": true}, {"id": "u_priya", "email": "priya.nair@northwind.example", "display_name": "Priya Nair", "self": false}, {"id": "u_omar", "email": "omar.haddad@northwind.example", "display_name": "Omar Haddad", "self": false}, {"id": "u_maya", "email": "maya.chen@northwind.example", "display_name": "Maya Chen", "self": false}, {"id": "u_sam", "email": "sam.rivera@northwind.example", "display_name": "Sam Rivera", "self": false}, {"id": "u_dana", "email": "dana.whitfield@northwind.example", "display_name": "Dana Whitfield", "self": false}, {"id": "u_kenji", "email": "kenji.sato@northwind.example", "display_name": "Kenji Sato", "self": false}, {"id": "u_aiko", "email": "aiko.mori@northwind.example", "display_name": "Aiko Mori", "self": false}, {"id": "u_leo", "email": "leo.park@northwind.example", "display_name": "Leo Park", "self": false}, {"id": "u_room2", "email": "room-2@resource.northwind.example", "display_name": "Room 2", "self": false}], "calendars": [{"id": "jordan.lee@northwind.example", "summary": "jordan.lee@northwind.example", "description": "Primary calendar", "time_zone": "America/Los_Angeles", "owner_id": "u_actor", "data_owner": "jordan.lee@northwind.example", "deleted": false}, {"id": "maya-team@northwind.example", "summary": "Maya's team", "time_zone": "America/Los_Angeles", "owner_id": "u_maya", "data_owner": "maya.chen@northwind.example", "deleted": false}, {"id": "projects@northwind.example", "summary": "Projects", "time_zone": "America/Los_Angeles", "owner_id": "u_actor", "data_owner": "jordan.lee@northwind.example", "deleted": false}, {"id": "leo-oncall@northwind.example", "summary": "Leo on-call", "time_zone": "America/Los_Angeles", "owner_id": "u_leo", "data_owner": "leo.park@northwind.example", "deleted": false}, {"id": "room-2@resource.northwind.example", "summary": "Room 2", "description": "Meeting room, second floor, 6 seats", "time_zone": "America/Los_Angeles", "owner_id": "u_room2", "data_owner": "room-2@resource.northwind.example", "deleted": false}], "calendar_list_entries": [{"id": "cle_jordan.lee@northwind.example", "user_id": "u_actor", "calendar_id": "jordan.lee@northwind.example", "access_role": "owner", "primary": true, "selected": true, "hidden": false, "deleted": false}, {"id": "cle_maya-team@northwind.example", "user_id": "u_actor", "calendar_id": "maya-team@northwind.example", "access_role": "writer", "primary": false, "selected": true, "hidden": false, "deleted": false}, {"id": "cle_projects@northwind.example", "user_id": "u_actor", "calendar_id": "projects@northwind.example", "access_role": "owner", "primary": false, "selected": true, "hidden": false, "deleted": false}, {"id": "cle_leo-oncall@northwind.example", "user_id": "u_actor", "calendar_id": "leo-oncall@northwind.example", "access_role": "reader", "primary": false, "selected": true, "hidden": false, "deleted": false}, {"id": "cle_room-2@resource.northwind.example", "user_id": "u_actor", "calendar_id": "room-2@resource.northwind.example", "access_role": "reader", "primary": false, "selected": true, "hidden": false, "deleted": false}], "calendar_events": [{"id": "ev_handoff", "calendar_id": "leo-oncall@northwind.example", "summary": "On-call handoff", "status": "confirmed", "visibility": "default", "transparency": "opaque", "event_type": "default", "creator_email": "leo.park@northwind.example", "creator_display_name": "Leo Park", "organizer_email": "leo.park@northwind.example", "organizer_display_name": "Leo Park", "creator_self": false, "organizer_self": false, "start": {"dateTime": "2018-06-19T09:00:00-07:00", "timeZone": "America/Los_Angeles"}, "end": {"dateTime": "2018-06-19T09:30:00-07:00", "timeZone": "America/Los_Angeles"}, "start_datetime": "2018-06-19T09:00:00", "end_datetime": "2018-06-19T09:30:00"}, {"id": "ev_budget", "calendar_id": "jordan.lee@northwind.example", "summary": "Budget review", "status": "confirmed", "visibility": "default", "transparency": "opaque", "event_type": "default", "creator_email": "jordan.lee@northwind.example", "creator_display_name": "Jordan Lee", "organizer_email": "jordan.lee@northwind.example", "organizer_display_name": "Jordan Lee", "creator_self": true, "organizer_self": true, "start": {"dateTime": "2018-06-19T15:00:00-07:00", "timeZone": "America/Los_Angeles"}, "end": {"dateTime": "2018-06-19T16:00:00-07:00", "timeZone": "America/Los_Angeles"}, "start_datetime": "2018-06-19T15:00:00", "end_datetime": "2018-06-19T16:00:00"}, {"id": "ev_sync", "calendar_id": "jordan.lee@northwind.example", "summary": "Design sync", "status": "confirmed", "visibility": "default", "transparency": "opaque", "event_type": "default", "creator_email": "maya.chen@northwind.example", "creator_display_name": "Maya Chen", "organizer_email": "maya.chen@northwind.example", "organizer_display_name": "Maya Chen", "creator_self": false, "organizer_self": false, "start": {"dateTime": "2018-06-20T11:00:00-07:00", "timeZone": "America/Los_Angeles"}, "end": {"dateTime": "2018-06-20T11:30:00-07:00", "timeZone": "America/Los_Angeles"}, "start_datetime": "2018-06-20T11:00:00", "end_datetime": "2018-06-20T11:30:00"}, {"id": "ev_review", "calendar_id": "jordan.lee@northwind.example", "summary": "Design review", "status": "confirmed", "visibility": "default", "transparency": "opaque", "event_type": "default", "creator_email": "jordan.lee@northwind.example", "creator_display_name": "Jordan Lee", "organizer_email": "jordan.lee@northwind.example", "organizer_display_name": "Jordan Lee", "creator_self": true, "organizer_self": true, "start": {"dateTime": "2018-06-21T10:00:00-07:00", "timeZone": "America/Los_Angeles"}, "end": {"dateTime": "2018-06-21T11:00:00-07:00", "timeZone": "America/Los_Angeles"}, "start_datetime": "2018-06-21T10:00:00", "end_datetime": "2018-06-21T11:00:00"}, {"id": "ev_deep", "calendar_id": "jordan.lee@northwind.example", "summary": "Deep work", "status": "confirmed", "visibility": "default", "transparency": "opaque", "event_type": "default", "creator_email": "jordan.lee@northwind.example", "creator_display_name": "Jordan Lee", "organizer_email": "jordan.lee@northwind.example", "organizer_display_name": "Jordan Lee", "creator_self": true, "organizer_self": true, "start": {"dateTime": "2018-06-22T09:00:00-07:00", "timeZone": "America/Los_Angeles"}, "end": {"dateTime": "2018-06-22T11:00:00-07:00", "timeZone": "America/Los_Angeles"}, "start_datetime": "2018-06-22T09:00:00", "end_datetime": "2018-06-22T11:00:00"}], "calendar_event_attendees": [{"id": 1, "event_id": "ev_sync", "email": "maya.chen@northwind.example", "display_name": "Maya Chen", "response_status": "accepted", "optional": false, "organizer": true, "self": false, "resource": false}, {"id": 2, "event_id": "ev_sync", "email": "jordan.lee@northwind.example", "display_name": "Jordan Lee", "response_status": "needsAction", "optional": false, "organizer": false, "self": true, "resource": false}, {"id": 3, "event_id": "ev_review", "email": "kenji.sato@northwind.example", "display_name": "Kenji Sato", "response_status": "needsAction", "optional": false, "organizer": false, "self": false, "resource": false}, {"id": 4, "event_id": "ev_review", "email": "aiko.mori@northwind.example", "display_name": "Aiko Mori", "response_status": "accepted", "optional": false, "organizer": false, "self": false, "resource": false}], "calendar_acl_rules": [{"id": "acl-m1", "calendar_id": "maya-team@northwind.example", "role": "writer", "scope_type": "user", "scope_value": "kenji.sato@northwind.example", "deleted": false}]}
