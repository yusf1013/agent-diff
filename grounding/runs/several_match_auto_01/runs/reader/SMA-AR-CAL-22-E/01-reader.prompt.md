You check test cases for an AI assistant that acts in a workspace on a user's behalf. You read carefully
and literally, the way the user who wrote the request would mean it.

---

A user sent the assistant this request in their Google Calendar workspace:

    "Change the time zone to America/New_York on all the Ops Rotation calendars I own whose description mentions weekend on-call coverage."

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
  "updated_at": "2018-01-01T00:00:00"
 },
 {
  "id": "ops-noram@northwind.example",
  "summary": "Ops Rotation – NORAM",
  "description": "Weekly rotation for handling production incidents and weekend on-call coverage across engineering.",
  "time_zone": "America/Los_Angeles",
  "owner_id": "u_actor",
  "data_owner": "jordan.lee@northwind.example",
  "deleted": false,
  "created_at": "2018-01-01T00:00:00",
  "updated_at": "2018-01-01T00:00:00",
  "location": "SF office, 4th floor conference room"
 },
 {
  "id": "ops-emea@northwind.example",
  "summary": "Ops Rotation – EMEA",
  "description": "Coordinates staffing schedules for the EMEA operations team.",
  "time_zone": "America/Los_Angeles",
  "owner_id": "u_actor",
  "data_owner": "jordan.lee@northwind.example",
  "deleted": false,
  "created_at": "2018-01-01T00:00:00",
  "updated_at": "2018-01-01T00:00:00",
  "location": "Weekend on-call coverage rota posted here every Friday."
 },
 {
  "id": "ops-apac@northwind.example",
  "summary": "Ops Rotation – APAC",
  "description": "Handles daytime shift scheduling for the APAC ops team.",
  "time_zone": "America/Los_Angeles",
  "owner_id": "u_actor",
  "data_owner": "jordan.lee@northwind.example",
  "deleted": false,
  "created_at": "2018-01-01T00:00:00",
  "updated_at": "2018-01-01T00:00:00"
 },
 {
  "id": "ops-latam@northwind.example",
  "summary": "Ops Rotation – LATAM",
  "description": "Tracks quarterly maintenance windows for LATAM data centers.",
  "time_zone": "America/Los_Angeles",
  "owner_id": "u_actor",
  "data_owner": "jordan.lee@northwind.example",
  "deleted": false,
  "created_at": "2018-01-01T00:00:00",
  "updated_at": "2018-01-01T00:00:00"
 },
 {
  "id": "marketing@northwind.example",
  "summary": "Marketing Calendar",
  "description": "Campaign launch schedule and content calendar.",
  "time_zone": "America/Los_Angeles",
  "owner_id": "u_maya",
  "data_owner": "maya.chen@northwind.example",
  "deleted": false,
  "created_at": "2018-01-01T00:00:00",
  "updated_at": "2018-01-01T00:00:00"
 },
 {
  "id": "standup@northwind.example",
  "summary": "Ops Standup",
  "description": "Daily standup notes for the ops team.",
  "time_zone": "America/Los_Angeles",
  "owner_id": "u_actor",
  "data_owner": "jordan.lee@northwind.example",
  "deleted": false,
  "created_at": "2018-01-01T00:00:00",
  "updated_at": "2018-01-01T00:00:00"
 },
 {
  "id": "ops-noram@northwind.example-sm221",
  "summary": "Ops Rotation - EMEA",
  "description": "Weekly rotation for handling production incidents and weekend on-call coverage across engineering.",
  "time_zone": "America/Los_Angeles",
  "owner_id": "u_actor",
  "data_owner": "jordan.lee@northwind.example",
  "deleted": false,
  "created_at": "2018-01-01T00:00:00",
  "updated_at": "2018-01-01T00:00:00",
  "location": "SF office, 4th floor conference room"
 },
 {
  "id": "ops-noram@northwind.example-sm222",
  "summary": "Ops Rotation - APAC",
  "description": "Weekly rotation for handling production incidents and weekend on-call coverage across engineering.",
  "time_zone": "America/Los_Angeles",
  "owner_id": "u_actor",
  "data_owner": "jordan.lee@northwind.example",
  "deleted": false,
  "created_at": "2018-01-01T00:00:00",
  "updated_at": "2018-01-01T00:00:00",
  "location": "SF office, 4th floor conference room"
 }
]
