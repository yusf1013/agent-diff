Step 2. These are all the records in the service:

### calendar_acl_rules (5)
{"id": "acl_team_kenji", "calendar_id": "design-team@northwind.example", "role": "writer", "scope_type": "user", "scope_value": "kenji.sato@northwind.example", "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
{"id": "acl_archive_kenji", "calendar_id": "design-archive@northwind.example", "role": "writer", "scope_type": "user", "scope_value": "kenji.sato@northwind.example", "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
{"id": "acl_sync_kenji", "calendar_id": "design-sync@northwind.example", "role": "reader", "scope_type": "user", "scope_value": "kenji.sato@northwind.example", "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
{"id": "acl_sync_sam", "calendar_id": "design-sync@northwind.example", "role": "writer", "scope_type": "user", "scope_value": "sam.rivera@northwind.example", "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
{"id": "acl_team_kenji_clone", "calendar_id": "design-team-2@northwind.example", "role": "writer", "scope_type": "user", "scope_value": "kenji.sato@northwind.example", "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
### calendar_list_entries (5)
{"id": "cle_jordan.lee@northwind.example", "user_id": "u_actor", "calendar_id": "jordan.lee@northwind.example", "access_role": "owner", "primary": true, "selected": true, "hidden": false, "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
{"id": "cle_design-team@northwind.example", "user_id": "u_actor", "calendar_id": "design-team@northwind.example", "access_role": "owner", "primary": false, "selected": true, "hidden": false, "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
{"id": "cle_design-sync@northwind.example", "user_id": "u_actor", "calendar_id": "design-sync@northwind.example", "access_role": "owner", "primary": false, "selected": true, "hidden": false, "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
{"id": "cle_marketing@northwind.example", "user_id": "u_actor", "calendar_id": "marketing@northwind.example", "access_role": "owner", "primary": false, "selected": true, "hidden": false, "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
{"id": "cle_design-team@northwind.example_clone", "user_id": "u_actor", "calendar_id": "design-team-2@northwind.example", "access_role": "owner", "primary": false, "selected": true, "hidden": false, "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
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
### calendars (6)
{"id": "jordan.lee@northwind.example", "summary": "jordan.lee@northwind.example", "description": "Primary calendar", "time_zone": "America/Los_Angeles", "owner_id": "u_actor", "data_owner": "jordan.lee@northwind.example", "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
{"id": "design-team@northwind.example", "summary": "Design Team", "time_zone": "America/Los_Angeles", "owner_id": "u_actor", "data_owner": "jordan.lee@northwind.example", "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
{"id": "design-archive@northwind.example", "summary": "Design Team", "time_zone": "America/Los_Angeles", "owner_id": "u_actor", "data_owner": "jordan.lee@northwind.example", "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
{"id": "design-sync@northwind.example", "summary": "Design Team", "time_zone": "America/Los_Angeles", "owner_id": "u_actor", "data_owner": "jordan.lee@northwind.example", "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
{"id": "marketing@northwind.example", "summary": "Marketing", "time_zone": "America/Los_Angeles", "owner_id": "u_actor", "data_owner": "jordan.lee@northwind.example", "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
{"id": "design-team-2@northwind.example", "summary": "Design Team", "time_zone": "America/Los_Angeles", "owner_id": "u_actor", "data_owner": "jordan.lee@northwind.example", "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}

Use your own conditions from step 1 as the author's conditions, with these ids:
- r1: The record is for the calendar named 'Design Team'
- r2: The calendar is in the calendar list of Jordan Lee (jordan.lee@northwind.example)
- r3: Jordan Lee has shared that calendar with Kenji Sato
- r4: Kenji Sato's access to that calendar is as a writer (role is writer)

The candidate records are the rows of `calendars`: jordan.lee@northwind.example, design-team@northwind.example, design-archive@northwind.example, design-sync@northwind.example, marketing@northwind.example, design-team-2@northwind.example.
For every candidate, give the ids of the conditions it fails under the careful reading (an empty list if it meets all of them), whether a careful colleague could still argue that it meets the request (contestable), and a short note. Then say whether the conditions faithfully capture the request as you read it in step 1 (and what differs). For each ambiguity you listed, say whether a careful reader would genuinely be unsure which reading was meant, and whether the readings select different candidates. Say whether the request reads like something a real user would write, without hints that only a test would contain. Finally, say whether the request refers to one specific record, as "the ..." does (asks_for_one: true), as opposed to allowing any record of a kind ("a ...") or asking for several (asks_for_one: false), and why.