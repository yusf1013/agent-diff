You check test cases for an AI assistant that acts in a workspace on a user's behalf. You read carefully
and literally, the way the user who wrote the request would mean it.

---

A user sent the assistant this request in their Google Calendar workspace:

    "Move all the planning sessions that end at 5pm on Thursday and whose description mentions the Q4 roadmap to Room 2B."

The user is u_actor. Below is every Google Calendar event in the workspace, with what the assistant can see about it. Which of
them does the user's request ask the assistant to act on?

List the id of every record the request covers, and only those. Read each condition of the request as the user
would mean it. If you cannot tell whether the user means a record, list it under `unsure` with the reason (and do
not list it in `ids`). Answer with JSON: {"ids": [...], "unsure": [{"id", "why"}], "notes": "..."}.

Records:
[
 {
  "id": "ev_ps_target",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Planning session",
  "description": "Walk through the Q4 roadmap and owners",
  "status": "confirmed",
  "visibility": "default",
  "transparency": "opaque",
  "event_type": "default",
  "creator_email": "jordan.lee@northwind.example",
  "creator_display_name": "Jordan Lee",
  "organizer_email": "jordan.lee@northwind.example",
  "organizer_display_name": "Jordan Lee",
  "created_at": "2018-05-01T00:00:00",
  "updated_at": "2018-05-01T00:00:00",
  "start": {
   "dateTime": "2018-06-21T16:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "end": {
   "dateTime": "2018-06-21T17:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "start_datetime": "2018-06-21T16:00:00",
  "end_datetime": "2018-06-21T17:00:00",
  "calendar": "jordan.lee@northwind.example",
  "calendar owner": "jordan.lee@northwind.example",
  "in the user's calendar list": true,
  "user's access": "owner",
  "hidden in the list": false,
  "primary": true
 },
 {
  "id": "ev_ps_starts",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Planning session",
  "description": "Q4 roadmap follow-ups",
  "status": "confirmed",
  "visibility": "default",
  "transparency": "opaque",
  "event_type": "default",
  "creator_email": "jordan.lee@northwind.example",
  "creator_display_name": "Jordan Lee",
  "organizer_email": "jordan.lee@northwind.example",
  "organizer_display_name": "Jordan Lee",
  "created_at": "2018-05-01T00:00:00",
  "updated_at": "2018-05-01T00:00:00",
  "start": {
   "dateTime": "2018-06-21T17:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "end": {
   "dateTime": "2018-06-21T18:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "start_datetime": "2018-06-21T17:00:00",
  "end_datetime": "2018-06-21T18:00:00",
  "calendar": "jordan.lee@northwind.example",
  "calendar owner": "jordan.lee@northwind.example",
  "in the user's calendar list": true,
  "user's access": "owner",
  "hidden in the list": false,
  "primary": true
 },
 {
  "id": "ev_ps_late",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Planning session",
  "description": "Q4 roadmap estimates",
  "status": "confirmed",
  "visibility": "default",
  "transparency": "opaque",
  "event_type": "default",
  "creator_email": "jordan.lee@northwind.example",
  "creator_display_name": "Jordan Lee",
  "organizer_email": "jordan.lee@northwind.example",
  "organizer_display_name": "Jordan Lee",
  "created_at": "2018-05-01T00:00:00",
  "updated_at": "2018-05-01T00:00:00",
  "start": {
   "dateTime": "2018-06-21T16:30:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "end": {
   "dateTime": "2018-06-21T17:30:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "start_datetime": "2018-06-21T16:30:00",
  "end_datetime": "2018-06-21T17:30:00",
  "calendar": "jordan.lee@northwind.example",
  "calendar owner": "jordan.lee@northwind.example",
  "in the user's calendar list": true,
  "user's access": "owner",
  "hidden in the list": false,
  "primary": true
 },
 {
  "id": "ev_ps_title",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Q4 roadmap planning",
  "description": "Agenda to be confirmed",
  "status": "confirmed",
  "visibility": "default",
  "transparency": "opaque",
  "event_type": "default",
  "creator_email": "jordan.lee@northwind.example",
  "creator_display_name": "Jordan Lee",
  "organizer_email": "jordan.lee@northwind.example",
  "organizer_display_name": "Jordan Lee",
  "created_at": "2018-05-01T00:00:00",
  "updated_at": "2018-05-01T00:00:00",
  "start": {
   "dateTime": "2018-06-21T16:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "end": {
   "dateTime": "2018-06-21T17:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "start_datetime": "2018-06-21T16:00:00",
  "end_datetime": "2018-06-21T17:00:00",
  "calendar": "jordan.lee@northwind.example",
  "calendar owner": "jordan.lee@northwind.example",
  "in the user's calendar list": true,
  "user's access": "owner",
  "hidden in the list": false,
  "primary": true
 },
 {
  "id": "ev_ps_hiring",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Planning session",
  "description": "Hiring plan for the autumn",
  "status": "confirmed",
  "visibility": "default",
  "transparency": "opaque",
  "event_type": "default",
  "creator_email": "jordan.lee@northwind.example",
  "creator_display_name": "Jordan Lee",
  "organizer_email": "jordan.lee@northwind.example",
  "organizer_display_name": "Jordan Lee",
  "created_at": "2018-05-01T00:00:00",
  "updated_at": "2018-05-01T00:00:00",
  "start": {
   "dateTime": "2018-06-21T15:30:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "end": {
   "dateTime": "2018-06-21T17:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "start_datetime": "2018-06-21T15:30:00",
  "end_datetime": "2018-06-21T17:00:00",
  "calendar": "jordan.lee@northwind.example",
  "calendar owner": "jordan.lee@northwind.example",
  "in the user's calendar list": true,
  "user's access": "owner",
  "hidden in the list": false,
  "primary": true
 },
 {
  "id": "ev_ps_target_sm0v",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Planning session Q4",
  "description": "Walk through the Q4 roadmap and owners",
  "status": "confirmed",
  "visibility": "default",
  "transparency": "opaque",
  "event_type": "default",
  "creator_email": "jordan.lee@northwind.example",
  "creator_display_name": "Jordan Lee",
  "organizer_email": "jordan.lee@northwind.example",
  "organizer_display_name": "Jordan Lee",
  "created_at": "2018-05-01T00:00:00",
  "updated_at": "2018-05-01T00:00:00",
  "start": {
   "dateTime": "2018-06-21T16:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "end": {
   "dateTime": "2018-06-21T17:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "start_datetime": "2018-06-21T16:00:00",
  "end_datetime": "2018-06-21T17:00:00",
  "calendar": "jordan.lee@northwind.example",
  "calendar owner": "jordan.lee@northwind.example",
  "in the user's calendar list": true,
  "user's access": "owner",
  "hidden in the list": false,
  "primary": true
 },
 {
  "id": "ev_ps_target_sm1c",
  "calendar_id": "team-events@northwind.example",
  "summary": "Team planning session",
  "description": "Walk through the Q4 roadmap and owners",
  "status": "confirmed",
  "visibility": "default",
  "transparency": "opaque",
  "event_type": "default",
  "creator_email": "jordan.lee@northwind.example",
  "creator_display_name": "Jordan Lee",
  "organizer_email": "jordan.lee@northwind.example",
  "organizer_display_name": "Jordan Lee",
  "created_at": "2018-05-01T00:00:00",
  "updated_at": "2018-05-01T00:00:00",
  "start": {
   "dateTime": "2018-06-21T16:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "end": {
   "dateTime": "2018-06-21T17:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "start_datetime": "2018-06-21T16:00:00",
  "end_datetime": "2018-06-21T17:00:00",
  "calendar": "Team events",
  "calendar owner": "jordan.lee@northwind.example",
  "in the user's calendar list": true,
  "user's access": "owner",
  "hidden in the list": false,
  "primary": false
 },
 {
  "id": "ev_ps_target_sm2h",
  "calendar_id": "planning@northwind.example",
  "summary": "Planning session review",
  "description": "Walk through the Q4 roadmap and owners",
  "status": "confirmed",
  "visibility": "default",
  "transparency": "opaque",
  "event_type": "default",
  "creator_email": "jordan.lee@northwind.example",
  "creator_display_name": "Jordan Lee",
  "organizer_email": "jordan.lee@northwind.example",
  "organizer_display_name": "Jordan Lee",
  "created_at": "2018-05-01T00:00:00",
  "updated_at": "2018-05-01T00:00:00",
  "start": {
   "dateTime": "2018-06-21T16:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "end": {
   "dateTime": "2018-06-21T17:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "start_datetime": "2018-06-21T16:00:00",
  "end_datetime": "2018-06-21T17:00:00",
  "calendar": "Planning",
  "calendar owner": "jordan.lee@northwind.example",
  "in the user's calendar list": true,
  "user's access": "owner",
  "hidden in the list": true,
  "primary": false
 }
]
