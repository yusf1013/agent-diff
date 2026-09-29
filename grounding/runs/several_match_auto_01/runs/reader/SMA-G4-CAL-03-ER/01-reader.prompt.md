You check test cases for an AI assistant that acts in a workspace on a user's behalf. You read carefully
and literally, the way the user who wrote the request would mean it.

---

A user sent the assistant this request in their Google Calendar workspace:

    "On my primary calendar, move all the Budget reviews with Maya Chen on Thursday to Room 5B."

The user is u_actor. Below is every Google Calendar event in the workspace, with what the assistant can see about it. Which of
them does the user's request ask the assistant to act on?

List the id of every record the request covers, and only those. Read each condition of the request as the user
would mean it. If you cannot tell whether the user means a record, list it under `unsure` with the reason (and do
not list it in `ids`). Answer with JSON: {"ids": [...], "unsure": [{"id", "why"}], "notes": "..."}.

Records:
[
 {
  "id": "ev_budget_primary",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Budget review",
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
  "primary": true,
  "calendar_event_attendees": [
   {
    "id": 1,
    "event_id": "ev_budget_primary",
    "email": "maya.chen@northwind.example",
    "display_name": "Maya Chen",
    "response_status": "accepted",
    "optional": false,
    "organizer": false,
    "self": false,
    "resource": false
   }
  ]
 },
 {
  "id": "ev_budget_travel",
  "calendar_id": "jordan.travel@northwind.example",
  "summary": "Budget review",
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
   "dateTime": "2018-06-21T10:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "end": {
   "dateTime": "2018-06-21T11:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "start_datetime": "2018-06-21T10:00:00",
  "end_datetime": "2018-06-21T11:00:00",
  "calendar": "Jordan Lee Travel",
  "calendar owner": "jordan.lee@northwind.example",
  "in the user's calendar list": true,
  "user's access": "owner",
  "hidden in the list": false,
  "primary": false,
  "calendar_event_attendees": [
   {
    "id": 2,
    "event_id": "ev_budget_travel",
    "email": "maya.chen@northwind.example",
    "display_name": "Maya Chen",
    "response_status": "accepted",
    "optional": false,
    "organizer": false,
    "self": false,
    "resource": false
   }
  ]
 },
 {
  "id": "ev_budget_eng",
  "calendar_id": "eng@northwind.example",
  "summary": "Budget review",
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
   "dateTime": "2018-06-21T10:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "end": {
   "dateTime": "2018-06-21T11:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "start_datetime": "2018-06-21T10:00:00",
  "end_datetime": "2018-06-21T11:00:00",
  "calendar": "Engineering",
  "calendar owner": "jordan.lee@northwind.example",
  "in the user's calendar list": true,
  "user's access": "owner",
  "hidden in the list": false,
  "primary": false,
  "calendar_event_attendees": [
   {
    "id": 3,
    "event_id": "ev_budget_eng",
    "email": "maya.chen@northwind.example",
    "display_name": "Maya Chen",
    "response_status": "accepted",
    "optional": false,
    "organizer": false,
    "self": false,
    "resource": false
   }
  ]
 },
 {
  "id": "ev_roadmap_primary",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Roadmap sync",
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
  "primary": true,
  "calendar_event_attendees": [
   {
    "id": 4,
    "event_id": "ev_roadmap_primary",
    "email": "omar.haddad@northwind.example",
    "display_name": "Omar Haddad",
    "response_status": "accepted",
    "optional": false,
    "organizer": false,
    "self": false,
    "resource": false
   }
  ]
 },
 {
  "id": "ev_budget_friday",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Budget review",
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
    "id": 5,
    "event_id": "ev_budget_friday",
    "email": "sam.rivera@northwind.example",
    "display_name": "Sam Rivera",
    "response_status": "accepted",
    "optional": false,
    "organizer": false,
    "self": false,
    "resource": false
   }
  ]
 },
 {
  "id": "ev_budget_primary_sm0v",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Budget review",
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
  "primary": true,
  "calendar_event_attendees": [
   {
    "id": 6,
    "event_id": "ev_budget_primary_sm0v",
    "email": "maya.chen@northwind.example",
    "display_name": "Maya Chen",
    "response_status": "accepted",
    "optional": false,
    "organizer": false,
    "self": false,
    "resource": false
   }
  ]
 },
 {
  "id": "ev_budget_primary_sm1v",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Budget review",
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
  "primary": true,
  "calendar_event_attendees": [
   {
    "id": 7,
    "event_id": "ev_budget_primary_sm1v",
    "email": "maya.chen@northwind.example",
    "display_name": "Maya Chen",
    "response_status": "accepted",
    "optional": false,
    "organizer": false,
    "self": false,
    "resource": false
   }
  ]
 }
]
