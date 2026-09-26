Step 2. These are all the records in the service:

### calendar_event_attendees (4)
{"id": 1, "event_id": "ev_p_target", "email": "priya.nair@northwind.example", "display_name": "Priya Nair", "response_status": "accepted", "optional": false, "organizer": true, "self": false, "resource": false}
{"id": 3, "event_id": "ev_p_loc", "email": "omar.haddad@northwind.example", "display_name": "Omar Haddad", "response_status": "accepted", "optional": false, "organizer": true, "self": false, "resource": false}
{"id": 4, "event_id": "ev_p_loc", "email": "priya.nair@northwind.example", "display_name": "Priya Nair", "response_status": "accepted", "optional": false, "organizer": false, "self": false, "resource": false}
{"id": 5, "event_id": "ev_p_target", "email": "sam.rivera@northwind.example", "display_name": "Sam Rivera", "response_status": "accepted", "optional": false, "organizer": false, "self": false, "resource": false}
### calendar_events (2)
{"id": "ev_p_target", "calendar_id": "vendor-programs@northwind.example", "ical_uid": "ev_p_target@northwind.example", "summary": "Vendor onboarding", "status": "confirmed", "visibility": "default", "transparency": "opaque", "event_type": "default", "sequence": 0, "creator_email": "priya.nair@northwind.example", "creator_display_name": "Priya Nair", "organizer_email": "priya.nair@northwind.example", "organizer_display_name": "Priya Nair", "creator_self": false, "organizer_self": false, "created_at": "2018-05-01T00:00:00", "updated_at": "2018-05-01T00:00:00", "start": {"dateTime": "2018-06-21T11:00:00-07:00", "timeZone": "America/Los_Angeles"}, "end": {"dateTime": "2018-06-21T12:00:00-07:00", "timeZone": "America/Los_Angeles"}, "start_datetime": "2018-06-21T11:00:00", "end_datetime": "2018-06-21T12:00:00"}
{"id": "ev_p_loc", "calendar_id": "priya-team@northwind.example", "ical_uid": "ev_p_loc@northwind.example", "summary": "Roadmap review", "status": "confirmed", "visibility": "default", "transparency": "opaque", "event_type": "default", "sequence": 0, "creator_email": "omar.haddad@northwind.example", "creator_display_name": "Omar Haddad", "organizer_email": "omar.haddad@northwind.example", "organizer_display_name": "Omar Haddad", "creator_self": false, "organizer_self": false, "created_at": "2018-05-01T00:00:00", "updated_at": "2018-05-01T00:00:00", "start": {"dateTime": "2018-06-21T10:00:00-07:00", "timeZone": "America/Los_Angeles"}, "end": {"dateTime": "2018-06-21T11:00:00-07:00", "timeZone": "America/Los_Angeles"}, "start_datetime": "2018-06-21T10:00:00", "end_datetime": "2018-06-21T11:00:00"}
### calendar_list_entries (3)
{"id": "cle_jordan.lee@northwind.example", "user_id": "u_actor", "calendar_id": "jordan.lee@northwind.example", "access_role": "owner", "primary": true, "selected": true, "hidden": false, "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
{"id": "cle_priya-team@northwind.example", "user_id": "u_actor", "calendar_id": "priya-team@northwind.example", "access_role": "writer", "primary": false, "selected": true, "hidden": false, "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
{"id": "cle_vendor-programs@northwind.example", "user_id": "u_actor", "calendar_id": "vendor-programs@northwind.example", "access_role": "writer", "primary": false, "selected": true, "hidden": false, "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
### calendar_users (9)
{"id": "u_actor", "email": "jordan.lee@northwind.example", "display_name": "Jordan Lee", "self": true, "created_at": "2017-05-01T00:00:00", "updated_at": "2017-05-01T00:00:00"}
{"id": "u_priya", "email": "priya.nair@northwind.example", "display_name": "Priya Nair", "self": false, "created_at": "2017-05-01T00:00:00", "updated_at": "2017-05-01T00:00:00"}
{"id": "u_omar", "email": "omar.haddad@northwind.example", "display_name": "Omar Haddad", "self": false, "created_at": "2017-05-01T00:00:00", "updated_at": "2017-05-01T00:00:00"}
{"id": "u_maya", "email": "maya.chen@northwind.example", "display_name": "Maya Chen", "self": false, "created_at": "2017-05-01T00:00:00", "updated_at": "2017-05-01T00:00:00"}
{"id": "u_sam", "email": "sam.rivera@northwind.example", "display_name": "Sam Rivera", "self": false, "created_at": "2017-05-01T00:00:00", "updated_at": "2017-05-01T00:00:00"}
{"id": "u_dana", "email": "dana.whitfield@northwind.example", "display_name": "Dana Whitfield", "self": false, "created_at": "2017-05-01T00:00:00", "updated_at": "2017-05-01T00:00:00"}
{"id": "u_kenji", "email": "kenji.sato@northwind.example", "display_name": "Kenji Sato", "self": false, "created_at": "2017-05-01T00:00:00", "updated_at": "2017-05-01T00:00:00"}
{"id": "u_aiko", "email": "aiko.mori@northwind.example", "display_name": "Aiko Mori", "self": false, "created_at": "2017-05-01T00:00:00", "updated_at": "2017-05-01T00:00:00"}
{"id": "u_leo", "email": "leo.park@northwind.example", "display_name": "Leo Park", "self": false, "created_at": "2017-05-01T00:00:00", "updated_at": "2017-05-01T00:00:00"}
### calendars (3)
{"id": "jordan.lee@northwind.example", "summary": "jordan.lee@northwind.example", "description": "Primary calendar", "time_zone": "America/Los_Angeles", "owner_id": "u_actor", "data_owner": "jordan.lee@northwind.example", "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
{"id": "priya-team@northwind.example", "summary": "Priya Nair", "time_zone": "America/Los_Angeles", "owner_id": "u_priya", "data_owner": "priya.nair@northwind.example", "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
{"id": "vendor-programs@northwind.example", "summary": "Vendor programs", "description": "Vendor onboarding and reviews", "time_zone": "America/Los_Angeles", "owner_id": "u_dana", "data_owner": "dana.whitfield@northwind.example", "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}

Use your own conditions from step 1 as the author's conditions, with these ids:
- r1: The record is a meeting (calendar event).
- r2: The event's organizer is Priya Nair.
- r3: The event occurs on the coming Thursday, 2018-06-19 (read from Sunday 2018-06-17 00:01 America/Los_Angeles).
- r4: The action requested is to move the event's start time to 3:00 PM America/Los_Angeles on that same Thursday, keeping the original duration unchanged.

The candidate records are the rows of `calendar_events`: ev_p_target, ev_p_loc.
For every candidate, give the ids of the author's conditions it fails under the careful reading (an empty list if it meets all of them), whether a careful colleague could still argue that it meets the request (contestable), and a short note. Then say whether the author's conditions faithfully capture the request as you read it in step 1 (and what differs). For each ambiguity you listed, say whether a careful reader would genuinely be unsure which reading was meant, and whether the readings select different candidates. Finally, say whether the request reads like something a real user would write, without hints that only a test would contain.