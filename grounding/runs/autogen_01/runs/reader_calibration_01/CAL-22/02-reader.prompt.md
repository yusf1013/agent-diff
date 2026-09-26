Step 2. These are all the records in the service:

### calendar_list_entries (5)
{"id": "cle_jordan.lee@northwind.example", "user_id": "u_actor", "calendar_id": "jordan.lee@northwind.example", "access_role": "owner", "primary": true, "selected": true, "hidden": false, "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
{"id": "cle_emea@northwind.example", "user_id": "u_actor", "calendar_id": "emea@northwind.example", "access_role": "owner", "primary": false, "selected": true, "hidden": false, "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
{"id": "cle_london@northwind.example", "user_id": "u_actor", "calendar_id": "london@northwind.example", "access_role": "owner", "primary": false, "selected": true, "hidden": false, "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
{"id": "cle_uk-sites@northwind.example", "user_id": "u_actor", "calendar_id": "uk-sites@northwind.example", "access_role": "owner", "primary": false, "selected": true, "hidden": false, "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
{"id": "cle_madrid@northwind.example", "user_id": "u_actor", "calendar_id": "madrid@northwind.example", "access_role": "owner", "primary": false, "selected": true, "hidden": false, "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
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
### calendars (5)
{"id": "jordan.lee@northwind.example", "summary": "jordan.lee@northwind.example", "description": "Primary calendar", "time_zone": "America/Los_Angeles", "owner_id": "u_actor", "data_owner": "jordan.lee@northwind.example", "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
{"id": "emea@northwind.example", "summary": "EMEA team", "description": "Calendar for the London office", "time_zone": "America/Los_Angeles", "owner_id": "u_actor", "data_owner": "jordan.lee@northwind.example", "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00", "location": "Reading"}
{"id": "london@northwind.example", "summary": "London office", "description": "Calendar for the Paris office", "time_zone": "America/Los_Angeles", "owner_id": "u_actor", "data_owner": "jordan.lee@northwind.example", "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00", "location": "Paris"}
{"id": "uk-sites@northwind.example", "summary": "UK sites", "description": "Calendar for the Berlin office", "time_zone": "America/Los_Angeles", "owner_id": "u_actor", "data_owner": "jordan.lee@northwind.example", "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00", "location": "London"}
{"id": "madrid@northwind.example", "summary": "Iberia team", "description": "Calendar for the Madrid office", "time_zone": "America/Los_Angeles", "owner_id": "u_actor", "data_owner": "jordan.lee@northwind.example", "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00", "location": "Madrid"}

Use your own conditions from step 1 as the author's conditions, with these ids:
- r1: There is a calendar whose description field (not its name/title) explicitly states it is for the London office.
- r2: Exactly one such calendar exists among those Jordan Lee can access/manage sharing for.
- r3: The grantee is the person with email sam.rivera@northwind.example specifically, matched by that exact address rather than just the name.
- r4: A sharing permission is added/granted on that calendar for that person (not merely an invite to an event).
- r5: The permission level granted corresponds to 'read access' rather than an editing/managing level.

The candidate records are the rows of `calendars`: jordan.lee@northwind.example, emea@northwind.example, london@northwind.example, uk-sites@northwind.example, madrid@northwind.example.
For every candidate, give the ids of the author's conditions it fails under the careful reading (an empty list if it meets all of them), whether a careful colleague could still argue that it meets the request (contestable), and a short note. Then say whether the author's conditions faithfully capture the request as you read it in step 1 (and what differs). For each ambiguity you listed, say whether a careful reader would genuinely be unsure which reading was meant, and whether the readings select different candidates. Finally, say whether the request reads like something a real user would write, without hints that only a test would contain.