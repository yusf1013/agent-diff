You check test cases for an AI assistant that acts in a workspace on a user's behalf. You read carefully
and literally, the way the user who wrote the request would mean it.

---

A user sent the assistant this request in their Google Calendar workspace:

    "Set the description of my calendars located in Tokyo to "APAC offsite planning"."

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
  "id": "apac@northwind.example",
  "summary": "APAC events",
  "description": "Regional events",
  "time_zone": "Asia/Tokyo",
  "owner_id": "u_actor",
  "data_owner": "jordan.lee@northwind.example",
  "deleted": false,
  "created_at": "2018-01-01T00:00:00",
  "updated_at": "2018-01-01T00:00:00",
  "location": "Tokyo"
 },
 {
  "id": "jp-team@northwind.example",
  "summary": "Japan team",
  "description": "Tokyo team calendar",
  "time_zone": "Asia/Tokyo",
  "owner_id": "u_actor",
  "data_owner": "jordan.lee@northwind.example",
  "deleted": false,
  "created_at": "2018-01-01T00:00:00",
  "updated_at": "2018-01-01T00:00:00",
  "location": "Osaka"
 },
 {
  "id": "tokyo@northwind.example",
  "summary": "Tokyo",
  "description": "Office calendar",
  "time_zone": "Asia/Singapore",
  "owner_id": "u_actor",
  "data_owner": "jordan.lee@northwind.example",
  "deleted": false,
  "created_at": "2018-01-01T00:00:00",
  "updated_at": "2018-01-01T00:00:00",
  "location": "Singapore"
 },
 {
  "id": "kr-team@northwind.example",
  "summary": "Korea team",
  "description": "Seoul team",
  "time_zone": "Asia/Tokyo",
  "owner_id": "u_actor",
  "data_owner": "jordan.lee@northwind.example",
  "deleted": false,
  "created_at": "2018-01-01T00:00:00",
  "updated_at": "2018-01-01T00:00:00",
  "location": "Seoul"
 },
 {
  "id": "anz@northwind.example",
  "summary": "ANZ events",
  "description": "Regional events",
  "time_zone": "Australia/Sydney",
  "owner_id": "u_actor",
  "data_owner": "jordan.lee@northwind.example",
  "deleted": false,
  "created_at": "2018-01-01T00:00:00",
  "updated_at": "2018-01-01T00:00:00",
  "location": "Sydney"
 },
 {
  "id": "apac@northwind.example-sm57",
  "summary": "Tokyo events",
  "description": "Regional events",
  "time_zone": "Asia/Tokyo",
  "owner_id": "u_actor",
  "data_owner": "jordan.lee@northwind.example",
  "deleted": false,
  "created_at": "2018-01-01T00:00:00",
  "updated_at": "2018-01-01T00:00:00",
  "location": "Tokyo"
 },
 {
  "id": "apac@northwind.example-sm58",
  "summary": "Tokyo offsite",
  "description": "Regional events",
  "time_zone": "Asia/Tokyo",
  "owner_id": "u_actor",
  "data_owner": "jordan.lee@northwind.example",
  "deleted": false,
  "created_at": "2018-01-01T00:00:00",
  "updated_at": "2018-01-01T00:00:00",
  "location": "Tokyo"
 }
]
