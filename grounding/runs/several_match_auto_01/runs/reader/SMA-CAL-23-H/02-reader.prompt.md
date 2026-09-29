You check test cases for an AI assistant that acts in a workspace on a user's behalf. You read carefully
and literally, the way the user who wrote the request would mean it.

---

A user sent the assistant this request in their Google Calendar workspace:

    "Delete all of Friday's architecture reviews that Kenji Sato (kenji.sato@northwind.example) attends as an optional guest."

The user is u_actor. Below is every Google Calendar event in the workspace, with what the assistant can see about it. Which of
them does the user's request ask the assistant to act on?

List the id of every record the request covers, and only those. Read each condition of the request as the user
would mean it. If you cannot tell whether the user means a record, list it under `unsure` with the reason (and do
not list it in `ids`). Answer with JSON: {"ids": [...], "unsure": [{"id", "why"}], "notes": "..."}.

Records:
[
 {
  "id": "ev_ar_target",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Architecture review",
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
  "primary": true,
  "calendar_event_attendees": [
   {
    "id": 1,
    "event_id": "ev_ar_target",
    "email": "kenji.sato@northwind.example",
    "display_name": "Kenji Sato",
    "response_status": "accepted",
    "optional": true,
    "organizer": false,
    "self": false,
    "resource": false
   },
   {
    "id": 2,
    "event_id": "ev_ar_target",
    "email": "aiko.mori@northwind.example",
    "display_name": "Aiko Mori",
    "response_status": "accepted",
    "optional": false,
    "organizer": false,
    "self": false,
    "resource": false
   }
  ]
 },
 {
  "id": "ev_ar_required",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Architecture review: storage",
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
   "dateTime": "2018-06-22T13:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "end": {
   "dateTime": "2018-06-22T14:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "start_datetime": "2018-06-22T13:00:00",
  "end_datetime": "2018-06-22T14:00:00",
  "calendar": "jordan.lee@northwind.example",
  "calendar owner": "jordan.lee@northwind.example",
  "in the user's calendar list": true,
  "user's access": "owner",
  "hidden in the list": false,
  "primary": true,
  "calendar_event_attendees": [
   {
    "id": 3,
    "event_id": "ev_ar_required",
    "email": "kenji.sato@northwind.example",
    "display_name": "Kenji Sato",
    "response_status": "accepted",
    "optional": false,
    "organizer": false,
    "self": false,
    "resource": false
   },
   {
    "id": 4,
    "event_id": "ev_ar_required",
    "email": "aiko.mori@northwind.example",
    "display_name": "Aiko Mori",
    "response_status": "accepted",
    "optional": false,
    "organizer": false,
    "self": false,
    "resource": false
   }
  ]
 },
 {
  "id": "ev_ar_satou",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Architecture review: search",
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
   "dateTime": "2018-06-22T15:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "end": {
   "dateTime": "2018-06-22T16:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "start_datetime": "2018-06-22T15:00:00",
  "end_datetime": "2018-06-22T16:00:00",
  "calendar": "jordan.lee@northwind.example",
  "calendar owner": "jordan.lee@northwind.example",
  "in the user's calendar list": true,
  "user's access": "owner",
  "hidden in the list": false,
  "primary": true,
  "calendar_event_attendees": [
   {
    "id": 5,
    "event_id": "ev_ar_satou",
    "email": "aiko.mori@northwind.example",
    "display_name": "Aiko Mori",
    "response_status": "accepted",
    "optional": false,
    "organizer": false,
    "self": false,
    "resource": false
   },
   {
    "id": 6,
    "event_id": "ev_ar_satou",
    "email": "kenji.satou@northwind.example",
    "display_name": "Kenji Satou",
    "response_status": "accepted",
    "optional": true,
    "organizer": false,
    "self": false,
    "resource": false
   }
  ]
 },
 {
  "id": "ev_ar_target_sm0v",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Architecture review sync",
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
  "primary": true,
  "calendar_event_attendees": [
   {
    "id": 7,
    "event_id": "ev_ar_target_sm0v",
    "email": "kenji.sato@northwind.example",
    "display_name": "Kenji Sato",
    "response_status": "accepted",
    "optional": true,
    "organizer": false,
    "self": false,
    "resource": false
   },
   {
    "id": 8,
    "event_id": "ev_ar_target_sm0v",
    "email": "aiko.mori@northwind.example",
    "display_name": "Aiko Mori",
    "response_status": "accepted",
    "optional": false,
    "organizer": false,
    "self": false,
    "resource": false
   }
  ]
 },
 {
  "id": "ev_ar_target_sm1c",
  "calendar_id": "team-events@northwind.example",
  "summary": "Architecture review Q4",
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
  "primary": false,
  "calendar_event_attendees": [
   {
    "id": 9,
    "event_id": "ev_ar_target_sm1c",
    "email": "kenji.sato@northwind.example",
    "display_name": "Kenji Sato",
    "response_status": "accepted",
    "optional": true,
    "organizer": false,
    "self": false,
    "resource": false
   },
   {
    "id": 10,
    "event_id": "ev_ar_target_sm1c",
    "email": "aiko.mori@northwind.example",
    "display_name": "Aiko Mori",
    "response_status": "accepted",
    "optional": false,
    "organizer": false,
    "self": false,
    "resource": false
   }
  ]
 },
 {
  "id": "ev_ar_target_sm2h",
  "calendar_id": "planning@northwind.example",
  "summary": "Architecture review - API",
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
  "primary": false,
  "calendar_event_attendees": [
   {
    "id": 11,
    "event_id": "ev_ar_target_sm2h",
    "email": "kenji.sato@northwind.example",
    "display_name": "Kenji Sato",
    "response_status": "accepted",
    "optional": true,
    "organizer": false,
    "self": false,
    "resource": false
   },
   {
    "id": 12,
    "event_id": "ev_ar_target_sm2h",
    "email": "aiko.mori@northwind.example",
    "display_name": "Aiko Mori",
    "response_status": "accepted",
    "optional": false,
    "organizer": false,
    "self": false,
    "resource": false
   }
  ]
 }
]
