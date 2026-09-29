You check test cases for an AI assistant that acts in a workspace on a user's behalf. You read carefully
and literally, the way the user who wrote the request would mean it.

---

A user sent the assistant this request in their Google Calendar workspace:

    "Give Sam Rivera (sam.rivera@northwind.example) read access to all the calendars whose description says it is for the London office."

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
  "id": "emea@northwind.example",
  "summary": "EMEA team",
  "description": "Calendar for the London office",
  "time_zone": "America/Los_Angeles",
  "owner_id": "u_actor",
  "data_owner": "jordan.lee@northwind.example",
  "deleted": false,
  "created_at": "2018-01-01T00:00:00",
  "updated_at": "2018-01-01T00:00:00",
  "location": "Reading"
 },
 {
  "id": "london@northwind.example",
  "summary": "London office",
  "description": "Calendar for the Paris office",
  "time_zone": "America/Los_Angeles",
  "owner_id": "u_actor",
  "data_owner": "jordan.lee@northwind.example",
  "deleted": false,
  "created_at": "2018-01-01T00:00:00",
  "updated_at": "2018-01-01T00:00:00",
  "location": "Paris"
 },
 {
  "id": "uk-sites@northwind.example",
  "summary": "UK sites",
  "description": "Calendar for the Berlin office",
  "time_zone": "America/Los_Angeles",
  "owner_id": "u_actor",
  "data_owner": "jordan.lee@northwind.example",
  "deleted": false,
  "created_at": "2018-01-01T00:00:00",
  "updated_at": "2018-01-01T00:00:00",
  "location": "London"
 },
 {
  "id": "madrid@northwind.example",
  "summary": "Iberia team",
  "description": "Calendar for the Madrid office",
  "time_zone": "America/Los_Angeles",
  "owner_id": "u_actor",
  "data_owner": "jordan.lee@northwind.example",
  "deleted": false,
  "created_at": "2018-01-01T00:00:00",
  "updated_at": "2018-01-01T00:00:00",
  "location": "Madrid"
 },
 {
  "id": "emea@northwind.example-sm49",
  "summary": "London team",
  "description": "Calendar for the London office",
  "time_zone": "America/Los_Angeles",
  "owner_id": "u_actor",
  "data_owner": "jordan.lee@northwind.example",
  "deleted": false,
  "created_at": "2018-01-01T00:00:00",
  "updated_at": "2018-01-01T00:00:00",
  "location": "Reading"
 },
 {
  "id": "emea@northwind.example-sm50",
  "summary": "London ops",
  "description": "Calendar for the London office",
  "time_zone": "America/Los_Angeles",
  "owner_id": "u_actor",
  "data_owner": "jordan.lee@northwind.example",
  "deleted": false,
  "created_at": "2018-01-01T00:00:00",
  "updated_at": "2018-01-01T00:00:00",
  "location": "Reading"
 }
]
