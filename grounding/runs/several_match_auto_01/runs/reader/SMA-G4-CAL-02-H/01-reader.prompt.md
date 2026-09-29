You check test cases for an AI assistant that acts in a workspace on a user's behalf. You read carefully
and literally, the way the user who wrote the request would mean it.

---

A user sent the assistant this request in their Google Calendar workspace:

    "Set the color of all the sprint retrospectives in Room 5B created by Kenji Sato to red."

The user is u_actor. Below is every Google Calendar event in the workspace, with what the assistant can see about it. Which of
them does the user's request ask the assistant to act on?

List the id of every record the request covers, and only those. Read each condition of the request as the user
would mean it. If you cannot tell whether the user means a record, list it under `unsure` with the reason (and do
not list it in `ids`). Answer with JSON: {"ids": [...], "unsure": [{"id", "why"}], "notes": "..."}.

Records:
[
 {
  "id": "ev_target",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Sprint retrospective",
  "location": "Room 5B",
  "status": "confirmed",
  "visibility": "default",
  "transparency": "opaque",
  "event_type": "default",
  "creator_email": "kenji.sato@northwind.example",
  "creator_display_name": "Kenji Sato",
  "organizer_email": "omar.haddad@northwind.example",
  "organizer_display_name": "Omar Haddad",
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
  "id": "ev_decoy_title",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Sprint retrospective follow-up",
  "location": "Room 5B",
  "status": "confirmed",
  "visibility": "default",
  "transparency": "opaque",
  "event_type": "default",
  "creator_email": "kenji.sato@northwind.example",
  "creator_display_name": "Kenji Sato",
  "organizer_email": "omar.haddad@northwind.example",
  "organizer_display_name": "Omar Haddad",
  "created_at": "2018-05-01T00:00:00",
  "updated_at": "2018-05-01T00:00:00",
  "start": {
   "dateTime": "2018-06-21T14:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "end": {
   "dateTime": "2018-06-21T15:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "start_datetime": "2018-06-21T14:00:00",
  "end_datetime": "2018-06-21T15:00:00",
  "calendar": "jordan.lee@northwind.example",
  "calendar owner": "jordan.lee@northwind.example",
  "in the user's calendar list": true,
  "user's access": "owner",
  "hidden in the list": false,
  "primary": true
 },
 {
  "id": "ev_decoy_location",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Sprint retrospective",
  "description": "Notes from the last session in Room 5B; please bring a laptop.",
  "location": "Room 5A",
  "status": "confirmed",
  "visibility": "default",
  "transparency": "opaque",
  "event_type": "default",
  "creator_email": "kenji.sato@northwind.example",
  "creator_display_name": "Kenji Sato",
  "organizer_email": "omar.haddad@northwind.example",
  "organizer_display_name": "Omar Haddad",
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
  "id": "ev_decoy_organizer",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Sprint retrospective",
  "location": "Room 5B",
  "status": "confirmed",
  "visibility": "default",
  "transparency": "opaque",
  "event_type": "default",
  "creator_email": "leo.park@northwind.example",
  "creator_display_name": "Leo Park",
  "organizer_email": "kenji.sato@northwind.example",
  "organizer_display_name": "Kenji Sato",
  "created_at": "2018-05-01T00:00:00",
  "updated_at": "2018-05-01T00:00:00",
  "start": {
   "dateTime": "2018-06-21T15:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "end": {
   "dateTime": "2018-06-21T16:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "start_datetime": "2018-06-21T15:00:00",
  "end_datetime": "2018-06-21T16:00:00",
  "calendar": "jordan.lee@northwind.example",
  "calendar owner": "jordan.lee@northwind.example",
  "in the user's calendar list": true,
  "user's access": "owner",
  "hidden in the list": false,
  "primary": true
 },
 {
  "id": "ev_decoy_creator",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Sprint retrospective",
  "location": "Room 5B",
  "status": "confirmed",
  "visibility": "default",
  "transparency": "opaque",
  "event_type": "default",
  "creator_email": "kenji.satou@northwind.example",
  "creator_display_name": "Kenji Satou",
  "organizer_email": "omar.haddad@northwind.example",
  "organizer_display_name": "Omar Haddad",
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
  "id": "ev_bg_lunch",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Team lunch",
  "location": "Cafeteria",
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
  "id": "ev_bg_review",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Design review",
  "location": "Room 5B",
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
   "dateTime": "2018-06-21T09:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "end": {
   "dateTime": "2018-06-21T09:30:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "start_datetime": "2018-06-21T09:00:00",
  "end_datetime": "2018-06-21T09:30:00",
  "calendar": "jordan.lee@northwind.example",
  "calendar owner": "jordan.lee@northwind.example",
  "in the user's calendar list": true,
  "user's access": "owner",
  "hidden in the list": false,
  "primary": true
 },
 {
  "id": "ev_target_sm0v",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Sprint retrospective",
  "location": "Room 5B",
  "status": "confirmed",
  "visibility": "default",
  "transparency": "opaque",
  "event_type": "default",
  "creator_email": "kenji.sato@northwind.example",
  "creator_display_name": "Kenji Sato",
  "organizer_email": "omar.haddad@northwind.example",
  "organizer_display_name": "Omar Haddad",
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
  "id": "ev_target_sm1c",
  "calendar_id": "team-events@northwind.example",
  "summary": "Sprint retrospective",
  "location": "Room 5B",
  "status": "confirmed",
  "visibility": "default",
  "transparency": "opaque",
  "event_type": "default",
  "creator_email": "kenji.sato@northwind.example",
  "creator_display_name": "Kenji Sato",
  "organizer_email": "omar.haddad@northwind.example",
  "organizer_display_name": "Omar Haddad",
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
  "calendar": "Team events",
  "calendar owner": "jordan.lee@northwind.example",
  "in the user's calendar list": true,
  "user's access": "owner",
  "hidden in the list": false,
  "primary": false
 },
 {
  "id": "ev_target_sm2h",
  "calendar_id": "planning@northwind.example",
  "summary": "Sprint retrospective",
  "location": "Room 5B",
  "status": "confirmed",
  "visibility": "default",
  "transparency": "opaque",
  "event_type": "default",
  "creator_email": "kenji.sato@northwind.example",
  "creator_display_name": "Kenji Sato",
  "organizer_email": "omar.haddad@northwind.example",
  "organizer_display_name": "Omar Haddad",
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
  "calendar": "Planning",
  "calendar owner": "jordan.lee@northwind.example",
  "in the user's calendar list": true,
  "user's access": "owner",
  "hidden in the list": true,
  "primary": false
 }
]
