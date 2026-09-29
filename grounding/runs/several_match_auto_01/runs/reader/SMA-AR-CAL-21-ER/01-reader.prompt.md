You check test cases for an AI assistant that acts in a workspace on a user's behalf. You read carefully
and literally, the way the user who wrote the request would mean it.

---

A user sent the assistant this request in their Google Calendar workspace:

    "Move all the client syncs about finalizing the Meridian contract that end at 3:30 pm to Room 4C."

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
  "summary": "Client sync",
  "description": "Finalizing the Meridian contract renewal terms before signature.",
  "location": "Room 8B",
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
   "dateTime": "2018-06-21T15:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "end": {
   "dateTime": "2018-06-21T15:30:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "start_datetime": "2018-06-21T15:00:00",
  "end_datetime": "2018-06-21T15:30:00",
  "calendar": "jordan.lee@northwind.example",
  "calendar owner": "jordan.lee@northwind.example",
  "in the user's calendar list": true,
  "user's access": "owner",
  "hidden in the list": false,
  "primary": true
 },
 {
  "id": "ev_loc",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Client sync",
  "description": "Weekly check-in on the hiring pipeline.",
  "location": "Meridian contract signing suite",
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
   "dateTime": "2018-06-21T15:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "end": {
   "dateTime": "2018-06-21T15:30:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "start_datetime": "2018-06-21T15:00:00",
  "end_datetime": "2018-06-21T15:30:00",
  "calendar": "jordan.lee@northwind.example",
  "calendar owner": "jordan.lee@northwind.example",
  "in the user's calendar list": true,
  "user's access": "owner",
  "hidden in the list": false,
  "primary": true
 },
 {
  "id": "ev_plain",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Client sync",
  "description": "Reviewing the new onboarding checklist for interns.",
  "location": "Room 5A",
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
   "dateTime": "2018-06-21T15:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "end": {
   "dateTime": "2018-06-21T15:30:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "start_datetime": "2018-06-21T15:00:00",
  "end_datetime": "2018-06-21T15:30:00",
  "calendar": "jordan.lee@northwind.example",
  "calendar owner": "jordan.lee@northwind.example",
  "in the user's calendar list": true,
  "user's access": "owner",
  "hidden in the list": false,
  "primary": true
 },
 {
  "id": "ev_end_early",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Client sync",
  "description": "Finalizing the Meridian contract renewal terms before signature.",
  "location": "Room 3C",
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
   "dateTime": "2018-06-21T14:30:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "end": {
   "dateTime": "2018-06-21T15:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "start_datetime": "2018-06-21T14:30:00",
  "end_datetime": "2018-06-21T15:00:00",
  "calendar": "jordan.lee@northwind.example",
  "calendar owner": "jordan.lee@northwind.example",
  "in the user's calendar list": true,
  "user's access": "owner",
  "hidden in the list": false,
  "primary": true
 },
 {
  "id": "ev_start_swap",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Client sync",
  "description": "Finalizing the Meridian contract renewal terms before signature.",
  "location": "Room 6D",
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
   "dateTime": "2018-06-21T16:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "start_datetime": "2018-06-21T15:30:00",
  "end_datetime": "2018-06-21T16:00:00",
  "calendar": "jordan.lee@northwind.example",
  "calendar owner": "jordan.lee@northwind.example",
  "in the user's calendar list": true,
  "user's access": "owner",
  "hidden in the list": false,
  "primary": true
 },
 {
  "id": "ev_bg_payments",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Design review: Payments",
  "description": "Reviewing payment gateway integration options.",
  "location": "Room 9F",
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
   "dateTime": "2018-06-21T15:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "end": {
   "dateTime": "2018-06-21T15:30:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "start_datetime": "2018-06-21T15:00:00",
  "end_datetime": "2018-06-21T15:30:00",
  "calendar": "jordan.lee@northwind.example",
  "calendar owner": "jordan.lee@northwind.example",
  "in the user's calendar list": true,
  "user's access": "owner",
  "hidden in the list": false,
  "primary": true
 },
 {
  "id": "ev_bg_oneone",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "1:1 with manager",
  "description": "Career growth conversation about promotion timeline.",
  "location": "Room 2A",
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
   "dateTime": "2018-06-21T11:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "end": {
   "dateTime": "2018-06-21T11:30:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "start_datetime": "2018-06-21T11:00:00",
  "end_datetime": "2018-06-21T11:30:00",
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
  "description": "Casual team lunch at the food trucks.",
  "location": "Courtyard",
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
  "id": "ev_target_sm0v",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Client sync",
  "description": "Finalizing the Meridian contract renewal terms before signature.",
  "location": "Room 8B",
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
   "dateTime": "2018-06-21T15:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "end": {
   "dateTime": "2018-06-21T15:30:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "start_datetime": "2018-06-21T15:00:00",
  "end_datetime": "2018-06-21T15:30:00",
  "calendar": "jordan.lee@northwind.example",
  "calendar owner": "jordan.lee@northwind.example",
  "in the user's calendar list": true,
  "user's access": "owner",
  "hidden in the list": false,
  "primary": true
 },
 {
  "id": "ev_target_sm1v",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Client sync",
  "description": "Finalizing the Meridian contract renewal terms before signature.",
  "location": "Room 8B",
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
   "dateTime": "2018-06-21T15:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "end": {
   "dateTime": "2018-06-21T15:30:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "start_datetime": "2018-06-21T15:00:00",
  "end_datetime": "2018-06-21T15:30:00",
  "calendar": "jordan.lee@northwind.example",
  "calendar owner": "jordan.lee@northwind.example",
  "in the user's calendar list": true,
  "user's access": "owner",
  "hidden in the list": false,
  "primary": true
 }
]
