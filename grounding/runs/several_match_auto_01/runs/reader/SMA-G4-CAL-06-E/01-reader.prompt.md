You check test cases for an AI assistant that acts in a workspace on a user's behalf. You read carefully
and literally, the way the user who wrote the request would mean it.

---

A user sent the assistant this request in their Google Calendar workspace:

    "Move all the Thursday quarterly planning lunches on Leo Park's calendar set to New York time to Room 5B."

The user is u_actor. Below is every Google Calendar event in the workspace, with what the assistant can see about it. Which of
them does the user's request ask the assistant to act on?

List the id of every record the request covers, and only those. Read each condition of the request as the user
would mean it. If you cannot tell whether the user means a record, list it under `unsure` with the reason (and do
not list it in `ids`). Answer with JSON: {"ids": [...], "unsure": [{"id", "why"}], "notes": "..."}.

Records:
[
 {
  "id": "ev_target",
  "calendar_id": "planning-ny@northwind.example",
  "summary": "Quarterly planning lunch",
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
  "calendar": "Team Planning",
  "calendar owner": "leo.park@northwind.example",
  "in the user's calendar list": true,
  "user's access": "writer",
  "hidden in the list": false,
  "primary": false,
  "calendars": [
   {
    "id": "planning-ny@northwind.example",
    "summary": "Team Planning",
    "time_zone": "America/New_York",
    "owner_id": "u_leo",
    "data_owner": "leo.park@northwind.example",
    "deleted": false,
    "created_at": "2018-01-01T00:00:00",
    "updated_at": "2018-01-01T00:00:00"
   }
  ]
 },
 {
  "id": "ev_d_acl",
  "calendar_id": "planning-shared@northwind.example",
  "summary": "Quarterly planning lunch",
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
  "calendar": "Team Planning",
  "calendar owner": "jordan.lee@northwind.example",
  "in the user's calendar list": true,
  "user's access": "owner",
  "hidden in the list": false,
  "primary": false,
  "calendars": [
   {
    "id": "planning-shared@northwind.example",
    "summary": "Team Planning",
    "time_zone": "America/New_York",
    "owner_id": "u_actor",
    "data_owner": "jordan.lee@northwind.example",
    "deleted": false,
    "created_at": "2018-01-01T00:00:00",
    "updated_at": "2018-01-01T00:00:00"
   }
  ]
 },
 {
  "id": "ev_d_sum",
  "calendar_id": "cal-leo-park@northwind.example",
  "summary": "Quarterly planning lunch",
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
  "calendar": "Leo Park",
  "calendar owner": "priya.nair@northwind.example",
  "in the user's calendar list": true,
  "user's access": "writer",
  "hidden in the list": false,
  "primary": false,
  "calendars": [
   {
    "id": "cal-leo-park@northwind.example",
    "summary": "Leo Park",
    "time_zone": "America/New_York",
    "owner_id": "u_priya",
    "data_owner": "priya.nair@northwind.example",
    "deleted": false,
    "created_at": "2018-01-01T00:00:00",
    "updated_at": "2018-01-01T00:00:00"
   }
  ]
 },
 {
  "id": "ev_d_parker",
  "calendar_id": "planning-parker@northwind.example",
  "summary": "Quarterly planning lunch",
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
  "calendar": "Team Planning",
  "calendar owner": "leo.parker@northwind.example",
  "in the user's calendar list": true,
  "user's access": "writer",
  "hidden in the list": false,
  "primary": false,
  "calendars": [
   {
    "id": "planning-parker@northwind.example",
    "summary": "Team Planning",
    "time_zone": "America/New_York",
    "owner_id": "u_leoparker",
    "data_owner": "leo.parker@northwind.example",
    "deleted": false,
    "created_at": "2018-01-01T00:00:00",
    "updated_at": "2018-01-01T00:00:00"
   }
  ]
 },
 {
  "id": "ev_d_chi",
  "calendar_id": "planning-chi@northwind.example",
  "summary": "Quarterly planning lunch",
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
  "calendar": "Team Planning",
  "calendar owner": "leo.park@northwind.example",
  "in the user's calendar list": true,
  "user's access": "writer",
  "hidden in the list": false,
  "primary": false,
  "calendars": [
   {
    "id": "planning-chi@northwind.example",
    "summary": "Team Planning",
    "time_zone": "America/Chicago",
    "owner_id": "u_leo",
    "data_owner": "leo.park@northwind.example",
    "deleted": false,
    "created_at": "2018-01-01T00:00:00",
    "updated_at": "2018-01-01T00:00:00"
   }
  ]
 },
 {
  "id": "ev_d_loc",
  "calendar_id": "planning-la@northwind.example",
  "summary": "Quarterly planning lunch",
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
  "calendar": "Team Planning",
  "calendar owner": "leo.park@northwind.example",
  "in the user's calendar list": true,
  "user's access": "writer",
  "hidden in the list": false,
  "primary": false,
  "calendars": [
   {
    "id": "planning-la@northwind.example",
    "summary": "Team Planning",
    "time_zone": "America/Los_Angeles",
    "owner_id": "u_leo",
    "data_owner": "leo.park@northwind.example",
    "deleted": false,
    "created_at": "2018-01-01T00:00:00",
    "updated_at": "2018-01-01T00:00:00",
    "location": "New York"
   }
  ]
 },
 {
  "id": "ev_bg_friday",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Quarterly planning lunch",
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
   "dateTime": "2018-06-22T12:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "end": {
   "dateTime": "2018-06-22T13:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "start_datetime": "2018-06-22T12:00:00",
  "end_datetime": "2018-06-22T13:00:00",
  "calendar": "jordan.lee@northwind.example",
  "calendar owner": "jordan.lee@northwind.example",
  "in the user's calendar list": true,
  "user's access": "owner",
  "hidden in the list": false,
  "primary": true,
  "calendars": [
   {
    "id": "jordan.lee@northwind.example",
    "summary": "jordan.lee@northwind.example",
    "description": "Primary calendar",
    "time_zone": "America/Los_Angeles",
    "owner_id": "u_actor",
    "data_owner": "jordan.lee@northwind.example",
    "deleted": false,
    "created_at": "2018-01-01T00:00:00",
    "updated_at": "2018-01-01T00:00:00"
   }
  ]
 },
 {
  "id": "ev_bg_standup",
  "calendar_id": "planning-ny@northwind.example",
  "summary": "Team standup",
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
   "dateTime": "2018-06-20T09:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "end": {
   "dateTime": "2018-06-20T09:30:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "start_datetime": "2018-06-20T09:00:00",
  "end_datetime": "2018-06-20T09:30:00",
  "calendar": "Team Planning",
  "calendar owner": "leo.park@northwind.example",
  "in the user's calendar list": true,
  "user's access": "writer",
  "hidden in the list": false,
  "primary": false,
  "calendars": [
   {
    "id": "planning-ny@northwind.example",
    "summary": "Team Planning",
    "time_zone": "America/New_York",
    "owner_id": "u_leo",
    "data_owner": "leo.park@northwind.example",
    "deleted": false,
    "created_at": "2018-01-01T00:00:00",
    "updated_at": "2018-01-01T00:00:00"
   }
  ]
 },
 {
  "id": "ev_target_sm0v",
  "calendar_id": "planning-ny@northwind.example",
  "summary": "Quarterly planning lunch Q2",
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
  "calendar": "Team Planning",
  "calendar owner": "leo.park@northwind.example",
  "in the user's calendar list": true,
  "user's access": "writer",
  "hidden in the list": false,
  "primary": false,
  "calendars": [
   {
    "id": "planning-ny@northwind.example",
    "summary": "Team Planning",
    "time_zone": "America/New_York",
    "owner_id": "u_leo",
    "data_owner": "leo.park@northwind.example",
    "deleted": false,
    "created_at": "2018-01-01T00:00:00",
    "updated_at": "2018-01-01T00:00:00"
   }
  ]
 },
 {
  "id": "ev_target_sm1v",
  "calendar_id": "planning-ny@northwind.example",
  "summary": "Quarterly planning lunch NYC",
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
  "calendar": "Team Planning",
  "calendar owner": "leo.park@northwind.example",
  "in the user's calendar list": true,
  "user's access": "writer",
  "hidden in the list": false,
  "primary": false,
  "calendars": [
   {
    "id": "planning-ny@northwind.example",
    "summary": "Team Planning",
    "time_zone": "America/New_York",
    "owner_id": "u_leo",
    "data_owner": "leo.park@northwind.example",
    "deleted": false,
    "created_at": "2018-01-01T00:00:00",
    "updated_at": "2018-01-01T00:00:00"
   }
  ]
 }
]
