Step 2. These are all the records in the service:

### calendar_acl_rules (1)
{"id": "user:jordan.lee@northwind.example", "calendar_id": "berlin-trip-team@northwind.example", "role": "owner", "scope_type": "user", "scope_value": "jordan.lee@northwind.example", "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
### calendar_list_entries (7)
{"id": "cle_jordan.lee@northwind.example", "user_id": "u_actor", "calendar_id": "jordan.lee@northwind.example", "access_role": "owner", "primary": true, "selected": true, "hidden": false, "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
{"id": "cle_berlin-trip@northwind.example", "user_id": "u_actor", "calendar_id": "berlin-trip@northwind.example", "access_role": "owner", "primary": false, "selected": true, "hidden": false, "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
{"id": "cle_berlin-trip-2017@northwind.example", "user_id": "u_actor", "calendar_id": "berlin-trip-2017@northwind.example", "access_role": "owner", "primary": false, "selected": true, "hidden": false, "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
{"id": "cle_berlin-trip-flights@northwind.example", "user_id": "u_actor", "calendar_id": "berlin-trip-flights@northwind.example", "access_role": "owner", "primary": false, "selected": true, "hidden": false, "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
{"id": "cle_berlin-trip-team@northwind.example", "user_id": "u_actor", "calendar_id": "berlin-trip-team@northwind.example", "access_role": "owner", "primary": false, "selected": true, "hidden": false, "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
{"id": "cle_berlin-trip-family@northwind.example", "user_id": "u_actor", "calendar_id": "berlin-trip-family@northwind.example", "access_role": "owner", "primary": false, "selected": true, "hidden": false, "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
{"id": "cle_denver-office@northwind.example", "user_id": "u_actor", "calendar_id": "denver-office@northwind.example", "access_role": "writer", "primary": false, "selected": true, "hidden": false, "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
### calendar_users (10)
{"id": "u_actor", "email": "jordan.lee@northwind.example", "display_name": "Jordan Lee", "self": true, "created_at": "2017-05-01T00:00:00", "updated_at": "2017-05-01T00:00:00"}
{"id": "u_priya", "email": "priya.nair@northwind.example", "display_name": "Priya Nair", "self": false, "created_at": "2017-05-01T00:00:00", "updated_at": "2017-05-01T00:00:00"}
{"id": "u_omar", "email": "omar.haddad@northwind.example", "display_name": "Omar Haddad", "self": false, "created_at": "2017-05-01T00:00:00", "updated_at": "2017-05-01T00:00:00"}
{"id": "u_maya", "email": "maya.chen@northwind.example", "display_name": "Maya Chen", "self": false, "created_at": "2017-05-01T00:00:00", "updated_at": "2017-05-01T00:00:00"}
{"id": "u_sam", "email": "sam.rivera@northwind.example", "display_name": "Sam Rivera", "self": false, "created_at": "2017-05-01T00:00:00", "updated_at": "2017-05-01T00:00:00"}
{"id": "u_dana", "email": "dana.whitfield@northwind.example", "display_name": "Dana Whitfield", "self": false, "created_at": "2017-05-01T00:00:00", "updated_at": "2017-05-01T00:00:00"}
{"id": "u_kenji", "email": "kenji.sato@northwind.example", "display_name": "Kenji Sato", "self": false, "created_at": "2017-05-01T00:00:00", "updated_at": "2017-05-01T00:00:00"}
{"id": "u_aiko", "email": "aiko.mori@northwind.example", "display_name": "Aiko Mori", "self": false, "created_at": "2017-05-01T00:00:00", "updated_at": "2017-05-01T00:00:00"}
{"id": "u_leo", "email": "leo.park@northwind.example", "display_name": "Leo Park", "self": false, "created_at": "2017-05-01T00:00:00", "updated_at": "2017-05-01T00:00:00"}
{"id": "u_jordanlees", "email": "jordan.lees@northwind.example", "display_name": "Jordan Lees", "self": false, "created_at": "2017-05-01T00:00:00", "updated_at": "2017-05-01T00:00:00"}
### calendars (7)
{"id": "jordan.lee@northwind.example", "summary": "jordan.lee@northwind.example", "description": "Primary calendar", "time_zone": "America/Los_Angeles", "owner_id": "u_actor", "data_owner": "jordan.lee@northwind.example", "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
{"id": "berlin-trip@northwind.example", "summary": "Berlin trip", "description": "Flights, hotel and things to do for the trip.", "time_zone": "America/Los_Angeles", "owner_id": "u_actor", "data_owner": "jordan.lee@northwind.example", "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
{"id": "berlin-trip-2017@northwind.example", "summary": "Berlin trip 2017", "description": "Planner from last summer's trip.", "time_zone": "America/Denver", "owner_id": "u_actor", "data_owner": "jordan.lee@northwind.example", "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
{"id": "berlin-trip-flights@northwind.example", "summary": "Berlin trip flights", "description": "Flight and airport transfer notes for the Berlin trip.", "time_zone": "Europe/Berlin", "owner_id": "u_actor", "data_owner": "jordan.lee@northwind.example", "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
{"id": "berlin-trip-team@northwind.example", "summary": "Berlin trip team", "description": "Team planning for the Berlin trip.", "time_zone": "America/Los_Angeles", "owner_id": "u_actor", "data_owner": "priya.nair@northwind.example", "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
{"id": "berlin-trip-family@northwind.example", "summary": "Berlin trip family", "description": "The family's Berlin trip plans.", "time_zone": "America/Los_Angeles", "owner_id": "u_actor", "data_owner": "jordan.lees@northwind.example", "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
{"id": "denver-office@northwind.example", "summary": "Denver office", "description": "Shared calendar for the Denver office.", "time_zone": "America/Denver", "owner_id": "u_omar", "data_owner": "omar.haddad@northwind.example", "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}

The author lists these conditions of the request:
- c1: the Berlin trip calendar
- c2: still on Los Angeles time
- c3: I own

The candidate records are the rows of `calendars`: jordan.lee@northwind.example, berlin-trip@northwind.example, berlin-trip-2017@northwind.example, berlin-trip-flights@northwind.example, berlin-trip-team@northwind.example, berlin-trip-family@northwind.example, denver-office@northwind.example.
For every candidate, give the ids of the author's conditions it fails under the careful reading (an empty list if it meets all of them), whether a careful colleague could still argue that it meets the request (contestable), and a short note. Then say whether the author's conditions faithfully capture the request as you read it in step 1 (and what differs). For each ambiguity you listed, say whether a careful reader would genuinely be unsure which reading was meant, and whether the readings select different candidates. Finally, say whether the request reads like something a real user would write, without hints that only a test would contain.