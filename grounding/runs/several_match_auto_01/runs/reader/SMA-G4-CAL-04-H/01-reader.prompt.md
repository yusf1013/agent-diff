You check test cases for an AI assistant that acts in a workspace on a user's behalf. You read carefully
and literally, the way the user who wrote the request would mean it.

---

A user sent the assistant this request in their Google Calendar workspace:

    "Move all the budget reviews on Friday organized by Maya Chen to Room 5B."

The user is u_actor. Below is every Google Calendar event in the workspace, with what the assistant can see about it. Which of
them does the user's request ask the assistant to act on?

List the id of every record the request covers, and only those. Read each condition of the request as the user
would mean it. If you cannot tell whether the user means a record, list it under `unsure` with the reason (and do
not list it in `ids`). Answer with JSON: {"ids": [...], "unsure": [{"id", "why"}], "notes": "..."}.

Records:
[
 {
  "id": "ev_br_close",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Budget review: Q2 close",
  "status": "confirmed",
  "visibility": "default",
  "transparency": "opaque",
  "event_type": "default",
  "creator_email": "maya.chen@northwind.example",
  "creator_display_name": "Maya Chen",
  "organizer_email": "maya.chen@northwind.example",
  "organizer_display_name": "Maya Chen",
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
  "id": "ev_br_utc",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Budget review: Q2 close",
  "status": "confirmed",
  "visibility": "default",
  "transparency": "opaque",
  "event_type": "default",
  "creator_email": "maya.chen@northwind.example",
  "creator_display_name": "Maya Chen",
  "organizer_email": "maya.chen@northwind.example",
  "organizer_display_name": "Maya Chen",
  "created_at": "2018-05-01T00:00:00",
  "updated_at": "2018-05-01T00:00:00",
  "start": {
   "dateTime": "2018-06-22T03:00:00Z",
   "timeZone": "America/Los_Angeles"
  },
  "end": {
   "dateTime": "2018-06-21T21:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "start_datetime": "2018-06-21T20:00:00",
  "end_datetime": "2018-06-21T21:00:00",
  "calendar": "jordan.lee@northwind.example",
  "calendar owner": "jordan.lee@northwind.example",
  "in the user's calendar list": true,
  "user's access": "owner",
  "hidden in the list": false,
  "primary": true
 },
 {
  "id": "ev_br_sat",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Budget review: Q2 close",
  "status": "confirmed",
  "visibility": "default",
  "transparency": "opaque",
  "event_type": "default",
  "creator_email": "maya.chen@northwind.example",
  "creator_display_name": "Maya Chen",
  "organizer_email": "maya.chen@northwind.example",
  "organizer_display_name": "Maya Chen",
  "created_at": "2018-05-01T00:00:00",
  "updated_at": "2018-05-01T00:00:00",
  "start": {
   "dateTime": "2018-06-23T10:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "end": {
   "dateTime": "2018-06-23T11:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "start_datetime": "2018-06-23T10:00:00",
  "end_datetime": "2018-06-23T11:00:00",
  "calendar": "jordan.lee@northwind.example",
  "calendar owner": "jordan.lee@northwind.example",
  "in the user's calendar list": true,
  "user's access": "owner",
  "hidden in the list": false,
  "primary": true
 },
 {
  "id": "ev_br_sync",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Budget sync: Q2 close",
  "status": "confirmed",
  "visibility": "default",
  "transparency": "opaque",
  "event_type": "default",
  "creator_email": "maya.chen@northwind.example",
  "creator_display_name": "Maya Chen",
  "organizer_email": "maya.chen@northwind.example",
  "organizer_display_name": "Maya Chen",
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
  "id": "ev_br_omar",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Budget review: Q2 close",
  "status": "confirmed",
  "visibility": "default",
  "transparency": "opaque",
  "event_type": "default",
  "creator_email": "omar.haddad@northwind.example",
  "creator_display_name": "Omar Haddad",
  "organizer_email": "omar.haddad@northwind.example",
  "organizer_display_name": "Omar Haddad",
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
  "id": "ev_bg_lunch",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Team lunch",
  "status": "confirmed",
  "visibility": "default",
  "transparency": "opaque",
  "event_type": "default",
  "creator_email": "leo.park@northwind.example",
  "creator_display_name": "Leo Park",
  "organizer_email": "leo.park@northwind.example",
  "organizer_display_name": "Leo Park",
  "created_at": "2018-05-01T00:00:00",
  "updated_at": "2018-05-01T00:00:00",
  "start": {
   "dateTime": "2018-06-18T12:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "end": {
   "dateTime": "2018-06-18T13:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "start_datetime": "2018-06-18T12:00:00",
  "end_datetime": "2018-06-18T13:00:00",
  "calendar": "jordan.lee@northwind.example",
  "calendar owner": "jordan.lee@northwind.example",
  "in the user's calendar list": true,
  "user's access": "owner",
  "hidden in the list": false,
  "primary": true
 },
 {
  "id": "ev_bg_mon",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Budget review: Q2 close",
  "status": "confirmed",
  "visibility": "default",
  "transparency": "opaque",
  "event_type": "default",
  "creator_email": "leo.park@northwind.example",
  "creator_display_name": "Leo Park",
  "organizer_email": "leo.park@northwind.example",
  "organizer_display_name": "Leo Park",
  "created_at": "2018-05-01T00:00:00",
  "updated_at": "2018-05-01T00:00:00",
  "start": {
   "dateTime": "2018-06-18T10:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "end": {
   "dateTime": "2018-06-18T11:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "start_datetime": "2018-06-18T10:00:00",
  "end_datetime": "2018-06-18T11:00:00",
  "calendar": "jordan.lee@northwind.example",
  "calendar owner": "jordan.lee@northwind.example",
  "in the user's calendar list": true,
  "user's access": "owner",
  "hidden in the list": false,
  "primary": true
 },
 {
  "id": "ev_br_close_sm0v",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Budget review: Q3 close",
  "status": "confirmed",
  "visibility": "default",
  "transparency": "opaque",
  "event_type": "default",
  "creator_email": "maya.chen@northwind.example",
  "creator_display_name": "Maya Chen",
  "organizer_email": "maya.chen@northwind.example",
  "organizer_display_name": "Maya Chen",
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
  "id": "ev_br_close_sm1c",
  "calendar_id": "team-events@northwind.example",
  "summary": "Budget review: Q1 close",
  "status": "confirmed",
  "visibility": "default",
  "transparency": "opaque",
  "event_type": "default",
  "creator_email": "maya.chen@northwind.example",
  "creator_display_name": "Maya Chen",
  "organizer_email": "maya.chen@northwind.example",
  "organizer_display_name": "Maya Chen",
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
  "calendar": "Team events",
  "calendar owner": "jordan.lee@northwind.example",
  "in the user's calendar list": true,
  "user's access": "owner",
  "hidden in the list": false,
  "primary": false
 },
 {
  "id": "ev_br_close_sm2h",
  "calendar_id": "planning@northwind.example",
  "summary": "Budget review: April close",
  "status": "confirmed",
  "visibility": "default",
  "transparency": "opaque",
  "event_type": "default",
  "creator_email": "maya.chen@northwind.example",
  "creator_display_name": "Maya Chen",
  "organizer_email": "maya.chen@northwind.example",
  "organizer_display_name": "Maya Chen",
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
  "calendar": "Planning",
  "calendar owner": "jordan.lee@northwind.example",
  "in the user's calendar list": true,
  "user's access": "owner",
  "hidden in the list": true,
  "primary": false
 }
]
