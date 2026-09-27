Step 2. These are all the records in the service:

### calendar_list_entries (5)
{"id": "cle_jordan.lee@northwind.example", "user_id": "u_actor", "calendar_id": "jordan.lee@northwind.example", "access_role": "owner", "primary": true, "selected": true, "hidden": false, "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
{"id": "cle_product_team_eng", "user_id": "u_actor", "calendar_id": "product_team_eng", "access_role": "writer", "primary": false, "selected": true, "hidden": false, "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
{"id": "cle_product_team_mkt", "user_id": "u_actor", "calendar_id": "product_team_mkt", "access_role": "reader", "primary": false, "selected": false, "hidden": false, "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
{"id": "cle_product_team_offsite", "user_id": "u_actor", "calendar_id": "product_team_offsite", "access_role": "writer", "primary": false, "selected": true, "hidden": false, "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
{"id": "cle_eng_roadmap", "user_id": "u_actor", "calendar_id": "eng_roadmap", "access_role": "reader", "primary": false, "selected": true, "hidden": false, "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
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
### calendars (7)
{"id": "jordan.lee@northwind.example", "summary": "jordan.lee@northwind.example", "description": "Primary calendar", "time_zone": "America/Los_Angeles", "owner_id": "u_actor", "data_owner": "jordan.lee@northwind.example", "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
{"id": "product_team_eng", "summary": "Product Team", "time_zone": "America/Los_Angeles", "owner_id": "u_priya", "data_owner": "priya.nair@northwind.example", "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
{"id": "product_team_mkt", "summary": "Product Team", "time_zone": "America/Los_Angeles", "owner_id": "u_dana", "data_owner": "dana.whitfield@northwind.example", "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
{"id": "product_team_offsite", "summary": "Product Team Offsite", "time_zone": "America/Los_Angeles", "owner_id": "u_maya", "data_owner": "maya.chen@northwind.example", "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
{"id": "eng_roadmap", "summary": "Engineering Roadmap", "time_zone": "America/Los_Angeles", "owner_id": "u_sam", "data_owner": "sam.rivera@northwind.example", "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
{"id": "us_holidays", "summary": "US Holidays", "time_zone": "America/Los_Angeles", "owner_id": "u_kenji", "data_owner": "kenji.sato@northwind.example", "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}
{"id": "design_team", "summary": "Design Team", "time_zone": "America/Los_Angeles", "owner_id": "u_leo", "data_owner": "leo.park@northwind.example", "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}

The author lists these conditions of the request:
- c1: the 'Product Team' calendar
- c2: that I currently have checked

The candidate records are the rows of `calendars`: jordan.lee@northwind.example, product_team_eng, product_team_mkt, product_team_offsite, eng_roadmap, us_holidays, design_team.
For every candidate, give the ids of the author's conditions it fails under the careful reading (an empty list if it meets all of them), whether a careful colleague could still argue that it meets the request (contestable), and a short note. Then say whether the author's conditions faithfully capture the request as you read it in step 1 (and what differs). For each ambiguity you listed, say whether a careful reader would genuinely be unsure which reading was meant, and whether the readings select different candidates. Finally, say whether the request reads like something a real user would write, without hints that only a test would contain.