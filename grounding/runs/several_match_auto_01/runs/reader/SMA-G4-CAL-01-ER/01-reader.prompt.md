You check test cases for an AI assistant that acts in a workspace on a user's behalf. You read carefully
and literally, the way the user who wrote the request would mean it.

---

A user sent the assistant this request in their Google Calendar workspace:

    "Move all the Budget Reviews starting at 10am on Thursday, organized by Dana Whitfield, to Room 5B — they're blocking time on my calendar."

The user is u_actor. Below is every Google Calendar event in the workspace, with what the assistant can see about it. Which of
them does the user's request ask the assistant to act on?

List the id of every record the request covers, and only those. Read each condition of the request as the user
would mean it. If you cannot tell whether the user means a record, list it under `unsure` with the reason (and do
not list it in `ids`). Answer with JSON: {"ids": [...], "unsure": [{"id", "why"}], "notes": "..."}.

Records:
[
 {
  "id": "ev_budget_10am",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Budget Review",
  "status": "confirmed",
  "visibility": "default",
  "transparency": "opaque",
  "event_type": "default",
  "creator_email": "dana.whitfield@northwind.example",
  "creator_display_name": "Dana Whitfield",
  "organizer_email": "dana.whitfield@northwind.example",
  "organizer_display_name": "Dana Whitfield",
  "created_at": "2018-05-01T00:00:00",
  "updated_at": "2018-05-01T00:00:00",
  "start": {
   "dateTime": "2018-06-21T10:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "end": {
   "dateTime": "2018-06-21T11:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "start_datetime": "2018-06-21T10:00:00",
  "end_datetime": "2018-06-21T11:00:00",
  "calendar": "jordan.lee@northwind.example",
  "calendar owner": "jordan.lee@northwind.example",
  "in the user's calendar list": true,
  "user's access": "owner",
  "hidden in the list": false,
  "primary": true
 },
 {
  "id": "ev_budget_creator",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Budget Review",
  "status": "confirmed",
  "visibility": "default",
  "transparency": "opaque",
  "event_type": "default",
  "creator_email": "dana.whitfield@northwind.example",
  "creator_display_name": "Dana Whitfield",
  "organizer_email": "maya.chen@northwind.example",
  "organizer_display_name": "Maya Chen",
  "created_at": "2018-05-01T00:00:00",
  "updated_at": "2018-05-01T00:00:00",
  "start": {
   "dateTime": "2018-06-21T10:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "end": {
   "dateTime": "2018-06-21T11:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "start_datetime": "2018-06-21T10:00:00",
  "end_datetime": "2018-06-21T11:00:00",
  "calendar": "jordan.lee@northwind.example",
  "calendar owner": "jordan.lee@northwind.example",
  "in the user's calendar list": true,
  "user's access": "owner",
  "hidden in the list": false,
  "primary": true
 },
 {
  "id": "ev_budget_attendee",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Budget Review",
  "status": "confirmed",
  "visibility": "default",
  "transparency": "opaque",
  "event_type": "default",
  "creator_email": "priya.nair@northwind.example",
  "creator_display_name": "Priya Nair",
  "organizer_email": "priya.nair@northwind.example",
  "organizer_display_name": "Priya Nair",
  "created_at": "2018-05-01T00:00:00",
  "updated_at": "2018-05-01T00:00:00",
  "start": {
   "dateTime": "2018-06-21T10:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "end": {
   "dateTime": "2018-06-21T11:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "start_datetime": "2018-06-21T10:00:00",
  "end_datetime": "2018-06-21T11:00:00",
  "calendar": "jordan.lee@northwind.example",
  "calendar owner": "jordan.lee@northwind.example",
  "in the user's calendar list": true,
  "user's access": "owner",
  "hidden in the list": false,
  "primary": true
 },
 {
  "id": "ev_budget_11am",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Budget Review",
  "status": "confirmed",
  "visibility": "default",
  "transparency": "opaque",
  "event_type": "default",
  "creator_email": "dana.whitfield@northwind.example",
  "creator_display_name": "Dana Whitfield",
  "organizer_email": "dana.whitfield@northwind.example",
  "organizer_display_name": "Dana Whitfield",
  "created_at": "2018-05-01T00:00:00",
  "updated_at": "2018-05-01T00:00:00",
  "start": {
   "dateTime": "2018-06-21T11:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "end": {
   "dateTime": "2018-06-21T12:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "start_datetime": "2018-06-21T11:00:00",
  "end_datetime": "2018-06-21T12:00:00",
  "calendar": "jordan.lee@northwind.example",
  "calendar owner": "jordan.lee@northwind.example",
  "in the user's calendar list": true,
  "user's access": "owner",
  "hidden in the list": false,
  "primary": true
 },
 {
  "id": "ev_budget_9am",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Budget Review",
  "status": "confirmed",
  "visibility": "default",
  "transparency": "opaque",
  "event_type": "default",
  "creator_email": "dana.whitfield@northwind.example",
  "creator_display_name": "Dana Whitfield",
  "organizer_email": "dana.whitfield@northwind.example",
  "organizer_display_name": "Dana Whitfield",
  "created_at": "2018-05-01T00:00:00",
  "updated_at": "2018-05-01T00:00:00",
  "start": {
   "dateTime": "2018-06-21T09:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "end": {
   "dateTime": "2018-06-21T10:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "start_datetime": "2018-06-21T09:00:00",
  "end_datetime": "2018-06-21T10:00:00",
  "calendar": "jordan.lee@northwind.example",
  "calendar owner": "jordan.lee@northwind.example",
  "in the user's calendar list": true,
  "user's access": "owner",
  "hidden in the list": false,
  "primary": true
 },
 {
  "id": "ev_budget_free",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Budget Review",
  "status": "confirmed",
  "visibility": "default",
  "transparency": "transparent",
  "event_type": "default",
  "creator_email": "dana.whitfield@northwind.example",
  "creator_display_name": "Dana Whitfield",
  "organizer_email": "dana.whitfield@northwind.example",
  "organizer_display_name": "Dana Whitfield",
  "created_at": "2018-05-01T00:00:00",
  "updated_at": "2018-05-01T00:00:00",
  "start": {
   "dateTime": "2018-06-21T10:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "end": {
   "dateTime": "2018-06-21T11:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "start_datetime": "2018-06-21T10:00:00",
  "end_datetime": "2018-06-21T11:00:00",
  "calendar": "jordan.lee@northwind.example",
  "calendar owner": "jordan.lee@northwind.example",
  "in the user's calendar list": true,
  "user's access": "owner",
  "hidden in the list": false,
  "primary": true
 },
 {
  "id": "ev_lunch",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Team Lunch",
  "status": "confirmed",
  "visibility": "default",
  "transparency": "transparent",
  "event_type": "default",
  "creator_email": "kenji.sato@northwind.example",
  "creator_display_name": "Kenji Sato",
  "organizer_email": "kenji.sato@northwind.example",
  "organizer_display_name": "Kenji Sato",
  "created_at": "2018-05-01T00:00:00",
  "updated_at": "2018-05-01T00:00:00",
  "start": {
   "dateTime": "2018-06-21T12:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "end": {
   "dateTime": "2018-06-21T13:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "start_datetime": "2018-06-21T12:00:00",
  "end_datetime": "2018-06-21T13:00:00",
  "calendar": "jordan.lee@northwind.example",
  "calendar owner": "jordan.lee@northwind.example",
  "in the user's calendar list": true,
  "user's access": "owner",
  "hidden in the list": false,
  "primary": true
 },
 {
  "id": "ev_budget_friday",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Budget Review",
  "status": "confirmed",
  "visibility": "default",
  "transparency": "opaque",
  "event_type": "default",
  "creator_email": "kenji.sato@northwind.example",
  "creator_display_name": "Kenji Sato",
  "organizer_email": "kenji.sato@northwind.example",
  "organizer_display_name": "Kenji Sato",
  "created_at": "2018-05-01T00:00:00",
  "updated_at": "2018-05-01T00:00:00",
  "start": {
   "dateTime": "2018-06-22T10:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "end": {
   "dateTime": "2018-06-22T11:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "start_datetime": "2018-06-22T10:00:00",
  "end_datetime": "2018-06-22T11:00:00",
  "calendar": "jordan.lee@northwind.example",
  "calendar owner": "jordan.lee@northwind.example",
  "in the user's calendar list": true,
  "user's access": "owner",
  "hidden in the list": false,
  "primary": true
 },
 {
  "id": "ev_budget_10am_sm0v",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Budget Review",
  "status": "confirmed",
  "visibility": "default",
  "transparency": "opaque",
  "event_type": "default",
  "creator_email": "dana.whitfield@northwind.example",
  "creator_display_name": "Dana Whitfield",
  "organizer_email": "dana.whitfield@northwind.example",
  "organizer_display_name": "Dana Whitfield",
  "created_at": "2018-05-01T00:00:00",
  "updated_at": "2018-05-01T00:00:00",
  "start": {
   "dateTime": "2018-06-21T10:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "end": {
   "dateTime": "2018-06-21T11:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "start_datetime": "2018-06-21T10:00:00",
  "end_datetime": "2018-06-21T11:00:00",
  "calendar": "jordan.lee@northwind.example",
  "calendar owner": "jordan.lee@northwind.example",
  "in the user's calendar list": true,
  "user's access": "owner",
  "hidden in the list": false,
  "primary": true
 },
 {
  "id": "ev_budget_10am_sm1v",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Budget Review",
  "status": "confirmed",
  "visibility": "default",
  "transparency": "opaque",
  "event_type": "default",
  "creator_email": "dana.whitfield@northwind.example",
  "creator_display_name": "Dana Whitfield",
  "organizer_email": "dana.whitfield@northwind.example",
  "organizer_display_name": "Dana Whitfield",
  "created_at": "2018-05-01T00:00:00",
  "updated_at": "2018-05-01T00:00:00",
  "start": {
   "dateTime": "2018-06-21T10:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "end": {
   "dateTime": "2018-06-21T11:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "start_datetime": "2018-06-21T10:00:00",
  "end_datetime": "2018-06-21T11:00:00",
  "calendar": "jordan.lee@northwind.example",
  "calendar owner": "jordan.lee@northwind.example",
  "in the user's calendar list": true,
  "user's access": "owner",
  "hidden in the list": false,
  "primary": true
 }
]
