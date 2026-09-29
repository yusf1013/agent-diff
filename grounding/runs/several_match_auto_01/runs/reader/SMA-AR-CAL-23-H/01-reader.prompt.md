You check test cases for an AI assistant that acts in a workspace on a user's behalf. You read carefully
and literally, the way the user who wrote the request would mean it.

---

A user sent the assistant this request in their Google Calendar workspace:

    "Move all the vendor syncs on Thursday that have Dana Whitfield as an optional attendee to Room 2C."

The user is u_actor. Below is every Google Calendar event in the workspace, with what the assistant can see about it. Which of
them does the user's request ask the assistant to act on?

List the id of every record the request covers, and only those. Read each condition of the request as the user
would mean it. If you cannot tell whether the user means a record, list it under `unsure` with the reason (and do
not list it in `ids`). Answer with JSON: {"ids": [...], "unsure": [{"id", "why"}], "notes": "..."}.

Records:
[
 {
  "id": "ev_vendor_target",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Vendor sync: Packaging",
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
  "primary": true,
  "calendar_event_attendees": [
   {
    "id": 1,
    "event_id": "ev_vendor_target",
    "email": "dana.whitfield@northwind.example",
    "display_name": "Dana Whitfield",
    "response_status": "accepted",
    "optional": true,
    "organizer": false,
    "self": false,
    "resource": false
   },
   {
    "id": 2,
    "event_id": "ev_vendor_target",
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
  "id": "ev_vendor_organizer",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Vendor sync: Freight",
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
   "dateTime": "2018-06-21T10:30:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "end": {
   "dateTime": "2018-06-21T11:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "start_datetime": "2018-06-21T10:30:00",
  "end_datetime": "2018-06-21T11:00:00",
  "calendar": "jordan.lee@northwind.example",
  "calendar owner": "jordan.lee@northwind.example",
  "in the user's calendar list": true,
  "user's access": "owner",
  "hidden in the list": false,
  "primary": true,
  "calendar_event_attendees": [
   {
    "id": 3,
    "event_id": "ev_vendor_organizer",
    "email": "kenji.sato@northwind.example",
    "display_name": "Kenji Sato",
    "response_status": "accepted",
    "optional": true,
    "organizer": false,
    "self": false,
    "resource": false
   },
   {
    "id": 4,
    "event_id": "ev_vendor_organizer",
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
  "id": "ev_vendor_white",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Vendor sync: Printing",
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
   "dateTime": "2018-06-21T12:30:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "start_datetime": "2018-06-21T12:00:00",
  "end_datetime": "2018-06-21T12:30:00",
  "calendar": "jordan.lee@northwind.example",
  "calendar owner": "jordan.lee@northwind.example",
  "in the user's calendar list": true,
  "user's access": "owner",
  "hidden in the list": false,
  "primary": true,
  "calendar_event_attendees": [
   {
    "id": 5,
    "event_id": "ev_vendor_white",
    "email": "dana.white@northwind.example",
    "display_name": "Dana White",
    "response_status": "accepted",
    "optional": true,
    "organizer": false,
    "self": false,
    "resource": false
   },
   {
    "id": 6,
    "event_id": "ev_vendor_white",
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
  "id": "ev_vendor_required",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Vendor sync: Labeling",
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
   "dateTime": "2018-06-21T13:30:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "end": {
   "dateTime": "2018-06-21T14:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "start_datetime": "2018-06-21T13:30:00",
  "end_datetime": "2018-06-21T14:00:00",
  "calendar": "jordan.lee@northwind.example",
  "calendar owner": "jordan.lee@northwind.example",
  "in the user's calendar list": true,
  "user's access": "owner",
  "hidden in the list": false,
  "primary": true,
  "calendar_event_attendees": [
   {
    "id": 7,
    "event_id": "ev_vendor_required",
    "email": "dana.whitfield@northwind.example",
    "display_name": "Dana Whitfield",
    "response_status": "accepted",
    "optional": false,
    "organizer": false,
    "self": false,
    "resource": false
   },
   {
    "id": 8,
    "event_id": "ev_vendor_required",
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
  "id": "ev_vendor_split",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Vendor sync: Ingredients",
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
  "primary": true,
  "calendar_event_attendees": [
   {
    "id": 9,
    "event_id": "ev_vendor_split",
    "email": "dana.whitfield@northwind.example",
    "display_name": "Dana Whitfield",
    "response_status": "accepted",
    "optional": false,
    "organizer": false,
    "self": false,
    "resource": false
   },
   {
    "id": 10,
    "event_id": "ev_vendor_split",
    "email": "leo.park@northwind.example",
    "display_name": "Leo Park",
    "response_status": "accepted",
    "optional": true,
    "organizer": false,
    "self": false,
    "resource": false
   }
  ]
 },
 {
  "id": "ev_budget_review",
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
   "dateTime": "2018-06-20T09:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "end": {
   "dateTime": "2018-06-20T09:30:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "start_datetime": "2018-06-20T09:00:00",
  "end_datetime": "2018-06-20T09:30:00",
  "calendar": "jordan.lee@northwind.example",
  "calendar owner": "jordan.lee@northwind.example",
  "in the user's calendar list": true,
  "user's access": "owner",
  "hidden in the list": false,
  "primary": true,
  "calendar_event_attendees": [
   {
    "id": 11,
    "event_id": "ev_budget_review",
    "email": "dana.whitfield@northwind.example",
    "display_name": "Dana Whitfield",
    "response_status": "accepted",
    "optional": false,
    "organizer": false,
    "self": false,
    "resource": false
   }
  ]
 },
 {
  "id": "ev_vendor_nextweek",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Vendor sync: Freight",
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
   "dateTime": "2018-06-28T09:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "end": {
   "dateTime": "2018-06-28T09:30:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "start_datetime": "2018-06-28T09:00:00",
  "end_datetime": "2018-06-28T09:30:00",
  "calendar": "jordan.lee@northwind.example",
  "calendar owner": "jordan.lee@northwind.example",
  "in the user's calendar list": true,
  "user's access": "owner",
  "hidden in the list": false,
  "primary": true,
  "calendar_event_attendees": [
   {
    "id": 12,
    "event_id": "ev_vendor_nextweek",
    "email": "kenji.sato@northwind.example",
    "display_name": "Kenji Sato",
    "response_status": "accepted",
    "optional": false,
    "organizer": false,
    "self": false,
    "resource": false
   },
   {
    "id": 13,
    "event_id": "ev_vendor_nextweek",
    "email": "sam.rivera@northwind.example",
    "display_name": "Sam Rivera",
    "response_status": "accepted",
    "optional": true,
    "organizer": false,
    "self": false,
    "resource": false
   }
  ]
 },
 {
  "id": "ev_vendor_target_sm0v",
  "calendar_id": "jordan.lee@northwind.example",
  "summary": "Vendor sync: Logistics",
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
  "primary": true,
  "calendar_event_attendees": [
   {
    "id": 14,
    "event_id": "ev_vendor_target_sm0v",
    "email": "dana.whitfield@northwind.example",
    "display_name": "Dana Whitfield",
    "response_status": "accepted",
    "optional": true,
    "organizer": false,
    "self": false,
    "resource": false
   },
   {
    "id": 15,
    "event_id": "ev_vendor_target_sm0v",
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
  "id": "ev_vendor_target_sm1c",
  "calendar_id": "team-events@northwind.example",
  "summary": "Vendor sync: Hardware",
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
   "dateTime": "2018-06-21T09:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "end": {
   "dateTime": "2018-06-21T09:30:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "start_datetime": "2018-06-21T09:00:00",
  "end_datetime": "2018-06-21T09:30:00",
  "calendar": "Team events",
  "calendar owner": "jordan.lee@northwind.example",
  "in the user's calendar list": true,
  "user's access": "owner",
  "hidden in the list": false,
  "primary": false,
  "calendar_event_attendees": [
   {
    "id": 16,
    "event_id": "ev_vendor_target_sm1c",
    "email": "dana.whitfield@northwind.example",
    "display_name": "Dana Whitfield",
    "response_status": "accepted",
    "optional": true,
    "organizer": false,
    "self": false,
    "resource": false
   },
   {
    "id": 17,
    "event_id": "ev_vendor_target_sm1c",
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
  "id": "ev_vendor_target_sm2h",
  "calendar_id": "planning@northwind.example",
  "summary": "Vendor sync: Supplies",
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
   "dateTime": "2018-06-21T09:00:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "end": {
   "dateTime": "2018-06-21T09:30:00-07:00",
   "timeZone": "America/Los_Angeles"
  },
  "start_datetime": "2018-06-21T09:00:00",
  "end_datetime": "2018-06-21T09:30:00",
  "calendar": "Planning",
  "calendar owner": "jordan.lee@northwind.example",
  "in the user's calendar list": true,
  "user's access": "owner",
  "hidden in the list": true,
  "primary": false,
  "calendar_event_attendees": [
   {
    "id": 18,
    "event_id": "ev_vendor_target_sm2h",
    "email": "dana.whitfield@northwind.example",
    "display_name": "Dana Whitfield",
    "response_status": "accepted",
    "optional": true,
    "organizer": false,
    "self": false,
    "resource": false
   },
   {
    "id": 19,
    "event_id": "ev_vendor_target_sm2h",
    "email": "sam.rivera@northwind.example",
    "display_name": "Sam Rivera",
    "response_status": "accepted",
    "optional": false,
    "organizer": false,
    "self": false,
    "resource": false
   }
  ]
 }
]
