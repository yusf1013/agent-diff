You check test cases for an AI assistant that acts in a workspace on a user's behalf. You read carefully
and literally, the way the user who wrote the request would mean it.

---

A user sent the assistant this request in their Google Calendar workspace:

    "Hide all the Team Calendars that I have writer access to on my calendar list, and that are shared with the design team as a writer."

The user is u_actor. Below is every Google Calendar calendar in the workspace, with what the assistant can see about it. Which of
them does the user's request ask the assistant to act on?

List the id of every record the request covers, and only those. Read each condition of the request as the user
would mean it. If you cannot tell whether the user means a record, list it under `unsure` with the reason (and do
not list it in `ids`). Answer with JSON: {"ids": [...], "unsure": [{"id", "why"}], "notes": "..."}.

Records:
[
 {
  "id": "jordan.lee@northwind.example",
  "summary": "jordan.lee@northwind.example",
  "description": "Primary calendar",
  "time_zone": "America/Los_Angeles",
  "owner_id": "u_actor",
  "data_owner": "jordan.lee@northwind.example",
  "deleted": false,
  "created_at": "2018-01-01T00:00:00",
  "updated_at": "2018-01-01T00:00:00",
  "calendar_list_entries": [
   {
    "id": "cle_jordan.lee@northwind.example",
    "user_id": "u_actor",
    "calendar_id": "jordan.lee@northwind.example",
    "access_role": "owner",
    "primary": true,
    "selected": true,
    "hidden": false,
    "deleted": false,
    "created_at": "2018-01-01T00:00:00",
    "updated_at": "2018-01-01T00:00:00"
   }
  ],
  "calendar_acl_rules": []
 },
 {
  "id": "team-design@northwind.example",
  "summary": "Team Calendar",
  "time_zone": "America/Los_Angeles",
  "owner_id": "u_sam",
  "data_owner": "sam.rivera@northwind.example",
  "deleted": false,
  "created_at": "2018-01-01T00:00:00",
  "updated_at": "2018-01-01T00:00:00",
  "calendar_list_entries": [
   {
    "id": "cle_team-design@northwind.example",
    "user_id": "u_actor",
    "calendar_id": "team-design@northwind.example",
    "access_role": "writer",
    "primary": false,
    "selected": true,
    "hidden": false,
    "deleted": false,
    "created_at": "2018-01-01T00:00:00",
    "updated_at": "2018-01-01T00:00:00"
   }
  ],
  "calendar_acl_rules": [
   {
    "id": "acl-design-team",
    "calendar_id": "team-design@northwind.example",
    "role": "writer",
    "scope_type": "group",
    "scope_value": "design-team@northwind.example",
    "deleted": false,
    "created_at": "2018-01-01T00:00:00",
    "updated_at": "2018-01-01T00:00:00"
   }
  ]
 },
 {
  "id": "team-brand@northwind.example",
  "summary": "Team Calendar",
  "time_zone": "America/Los_Angeles",
  "owner_id": "u_dana",
  "data_owner": "dana.whitfield@northwind.example",
  "deleted": false,
  "created_at": "2018-01-01T00:00:00",
  "updated_at": "2018-01-01T00:00:00",
  "calendar_list_entries": [],
  "calendar_acl_rules": [
   {
    "id": "acl-brand-jordan",
    "calendar_id": "team-brand@northwind.example",
    "role": "writer",
    "scope_type": "user",
    "scope_value": "jordan.lee@northwind.example",
    "deleted": false,
    "created_at": "2018-01-01T00:00:00",
    "updated_at": "2018-01-01T00:00:00"
   },
   {
    "id": "acl-brand-design-team",
    "calendar_id": "team-brand@northwind.example",
    "role": "writer",
    "scope_type": "group",
    "scope_value": "design-team@northwind.example",
    "deleted": false,
    "created_at": "2018-01-01T00:00:00",
    "updated_at": "2018-01-01T00:00:00"
   }
  ]
 },
 {
  "id": "team-ops@northwind.example",
  "summary": "Team Calendar",
  "time_zone": "America/Los_Angeles",
  "owner_id": "u_actor",
  "data_owner": "jordan.lee@northwind.example",
  "deleted": false,
  "created_at": "2018-01-01T00:00:00",
  "updated_at": "2018-01-01T00:00:00",
  "calendar_list_entries": [],
  "calendar_acl_rules": [
   {
    "id": "acl-ops-design-team",
    "calendar_id": "team-ops@northwind.example",
    "role": "writer",
    "scope_type": "group",
    "scope_value": "design-team@northwind.example",
    "deleted": false,
    "created_at": "2018-01-01T00:00:00",
    "updated_at": "2018-01-01T00:00:00"
   }
  ]
 },
 {
  "id": "team-launch@northwind.example",
  "summary": "Team Calendar",
  "time_zone": "America/Los_Angeles",
  "owner_id": "u_kenji",
  "data_owner": "kenji.sato@northwind.example",
  "deleted": false,
  "created_at": "2018-01-01T00:00:00",
  "updated_at": "2018-01-01T00:00:00",
  "calendar_list_entries": [
   {
    "id": "cle_team-launch@northwind.example",
    "user_id": "u_actor",
    "calendar_id": "team-launch@northwind.example",
    "access_role": "writer",
    "primary": false,
    "selected": true,
    "hidden": false,
    "deleted": false,
    "created_at": "2018-01-01T00:00:00",
    "updated_at": "2018-01-01T00:00:00"
   }
  ],
  "calendar_acl_rules": [
   {
    "id": "acl-launch-design-team",
    "calendar_id": "team-launch@northwind.example",
    "role": "reader",
    "scope_type": "group",
    "scope_value": "design-team@northwind.example",
    "deleted": false,
    "created_at": "2018-01-01T00:00:00",
    "updated_at": "2018-01-01T00:00:00"
   },
   {
    "id": "acl-launch-product-team",
    "calendar_id": "team-launch@northwind.example",
    "role": "writer",
    "scope_type": "group",
    "scope_value": "product-team@northwind.example",
    "deleted": false,
    "created_at": "2018-01-01T00:00:00",
    "updated_at": "2018-01-01T00:00:00"
   }
  ]
 },
 {
  "id": "marketing-sync@northwind.example",
  "summary": "Marketing Sync",
  "time_zone": "America/Los_Angeles",
  "owner_id": "u_aiko",
  "data_owner": "aiko.mori@northwind.example",
  "deleted": false,
  "created_at": "2018-01-01T00:00:00",
  "updated_at": "2018-01-01T00:00:00",
  "calendar_list_entries": [
   {
    "id": "cle_marketing-sync@northwind.example",
    "user_id": "u_actor",
    "calendar_id": "marketing-sync@northwind.example",
    "access_role": "reader",
    "primary": false,
    "selected": true,
    "hidden": false,
    "deleted": false,
    "created_at": "2018-01-01T00:00:00",
    "updated_at": "2018-01-01T00:00:00"
   }
  ],
  "calendar_acl_rules": [
   {
    "id": "acl-marketing-team",
    "calendar_id": "marketing-sync@northwind.example",
    "role": "writer",
    "scope_type": "group",
    "scope_value": "marketing-team@northwind.example",
    "deleted": false,
    "created_at": "2018-01-01T00:00:00",
    "updated_at": "2018-01-01T00:00:00"
   }
  ]
 },
 {
  "id": "team-sales@northwind.example",
  "summary": "Team Calendar",
  "time_zone": "America/Los_Angeles",
  "owner_id": "u_leo",
  "data_owner": "leo.park@northwind.example",
  "deleted": false,
  "created_at": "2018-01-01T00:00:00",
  "updated_at": "2018-01-01T00:00:00",
  "calendar_list_entries": [
   {
    "id": "cle_team-sales@northwind.example",
    "user_id": "u_actor",
    "calendar_id": "team-sales@northwind.example",
    "access_role": "reader",
    "primary": false,
    "selected": true,
    "hidden": false,
    "deleted": false,
    "created_at": "2018-01-01T00:00:00",
    "updated_at": "2018-01-01T00:00:00"
   }
  ],
  "calendar_acl_rules": [
   {
    "id": "acl-sales-team",
    "calendar_id": "team-sales@northwind.example",
    "role": "writer",
    "scope_type": "group",
    "scope_value": "sales-team@northwind.example",
    "deleted": false,
    "created_at": "2018-01-01T00:00:00",
    "updated_at": "2018-01-01T00:00:00"
   }
  ]
 },
 {
  "id": "team-design@northwind.example-sm435",
  "summary": "Team Calendar",
  "time_zone": "America/Los_Angeles",
  "owner_id": "u_sam",
  "data_owner": "sam.rivera@northwind.example",
  "deleted": false,
  "created_at": "2018-01-01T00:00:00",
  "updated_at": "2018-01-01T00:00:00",
  "calendar_list_entries": [
   {
    "id": "cle_team-design@northwind.example-sm435",
    "user_id": "u_actor",
    "calendar_id": "team-design@northwind.example-sm435",
    "access_role": "writer",
    "primary": false,
    "selected": true,
    "hidden": false,
    "deleted": false,
    "created_at": "2018-01-01T00:00:00",
    "updated_at": "2018-01-01T00:00:00"
   }
  ],
  "calendar_acl_rules": [
   {
    "id": "acl-design-team-sm435",
    "calendar_id": "team-design@northwind.example-sm435",
    "role": "writer",
    "scope_type": "group",
    "scope_value": "design-team@northwind.example",
    "deleted": false,
    "created_at": "2018-01-01T00:00:00",
    "updated_at": "2018-01-01T00:00:00"
   }
  ]
 },
 {
  "id": "team-design@northwind.example-sm436",
  "summary": "Team Calendar",
  "time_zone": "America/Los_Angeles",
  "owner_id": "u_sam",
  "data_owner": "sam.rivera@northwind.example",
  "deleted": false,
  "created_at": "2018-01-01T00:00:00",
  "updated_at": "2018-01-01T00:00:00",
  "calendar_list_entries": [
   {
    "id": "cle_team-design@northwind.example-sm436",
    "user_id": "u_actor",
    "calendar_id": "team-design@northwind.example-sm436",
    "access_role": "writer",
    "primary": false,
    "selected": true,
    "hidden": false,
    "deleted": false,
    "created_at": "2018-01-01T00:00:00",
    "updated_at": "2018-01-01T00:00:00"
   }
  ],
  "calendar_acl_rules": [
   {
    "id": "acl-design-team-sm436",
    "calendar_id": "team-design@northwind.example-sm436",
    "role": "writer",
    "scope_type": "group",
    "scope_value": "design-team@northwind.example",
    "deleted": false,
    "created_at": "2018-01-01T00:00:00",
    "updated_at": "2018-01-01T00:00:00"
   }
  ]
 }
]
