You check test cases for an AI assistant that acts in a workspace on a user's behalf. You read carefully
and literally, the way the user who wrote the request would mean it.

---

A user sent the assistant this request in their Box workspace:

    "Move the due date to October 20, 2026 on all the tasks pat.kim@northwind.example created on September 14 asking to check the indemnity clause."

The user is Jordan Lee. Below is every Box task in the workspace, with what the assistant can see about it. Which of
them does the user's request ask the assistant to act on?

List the id of every record the request covers, and only those. Read each condition of the request as the user
would mean it. If you cannot tell whether the user means a record, list it under `unsure` with the reason (and do
not list it in `ids`). Answer with JSON: {"ids": [...], "unsure": [{"id", "why"}], "notes": "..."}.

Records:
[
 {
  "id": "8301",
  "item_id": "8201",
  "item_type": "file",
  "message": "Please check the indemnity clause",
  "action": "review",
  "is_completed": false,
  "completion_rule": "all_assignees",
  "due_at": "2026-10-05T17:00:00+00:00",
  "created_by_id": "30000000009 (Pat Kim)",
  "created_at": "2026-09-14T16:00:00+00:00",
  "box_users": [
   {
    "id": "30000000009",
    "name": "Pat Kim",
    "login": "pat.kim@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ]
 },
 {
  "id": "8302",
  "item_id": "8203",
  "item_type": "file",
  "message": "Please check the indemnity clause",
  "action": "review",
  "is_completed": false,
  "completion_rule": "all_assignees",
  "due_at": "2026-10-05T17:00:00+00:00",
  "created_by_id": "30000000010 (Pat Kimura)",
  "created_at": "2026-09-14T16:00:00+00:00",
  "box_users": [
   {
    "id": "30000000010",
    "name": "Pat Kimura",
    "login": "pat.kimura@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ]
 },
 {
  "id": "8303",
  "item_id": "8203",
  "item_type": "file",
  "message": "Please check the indemnity clause",
  "action": "review",
  "is_completed": false,
  "completion_rule": "all_assignees",
  "due_at": "2026-10-05T17:00:00+00:00",
  "created_by_id": "30000000009 (Pat Kim)",
  "created_at": "2026-09-15T16:00:00+00:00",
  "box_users": [
   {
    "id": "30000000009",
    "name": "Pat Kim",
    "login": "pat.kim@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ]
 },
 {
  "id": "8304",
  "item_id": "8202",
  "item_type": "file",
  "message": "Please check the payment terms",
  "action": "review",
  "is_completed": false,
  "completion_rule": "all_assignees",
  "due_at": "2026-10-05T17:00:00+00:00",
  "created_by_id": "30000000009 (Pat Kim)",
  "created_at": "2026-09-14T16:00:00+00:00",
  "box_users": [
   {
    "id": "30000000009",
    "name": "Pat Kim",
    "login": "pat.kim@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ]
 },
 {
  "id": "8305",
  "item_id": "8201",
  "item_type": "file",
  "message": "Please approve the invoice",
  "action": "review",
  "is_completed": false,
  "completion_rule": "all_assignees",
  "due_at": "2026-10-05T17:00:00+00:00",
  "created_by_id": "30000000009 (Pat Kim)",
  "created_at": "2026-09-14T16:00:00+00:00",
  "box_users": [
   {
    "id": "30000000009",
    "name": "Pat Kim",
    "login": "pat.kim@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ]
 },
 {
  "id": "8306",
  "item_id": "8201",
  "item_type": "file",
  "message": "Kindly check the indemnity clause",
  "action": "review",
  "is_completed": false,
  "completion_rule": "all_assignees",
  "due_at": "2026-10-05T17:00:00+00:00",
  "created_by_id": "30000000009 (Pat Kim)",
  "created_at": "2026-09-14T16:00:00+00:00",
  "box_users": [
   {
    "id": "30000000009",
    "name": "Pat Kim",
    "login": "pat.kim@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ]
 },
 {
  "id": "8307",
  "item_id": "8201",
  "item_type": "file",
  "message": "Please check the indemnity clause today",
  "action": "review",
  "is_completed": false,
  "completion_rule": "all_assignees",
  "due_at": "2026-10-05T17:00:00+00:00",
  "created_by_id": "30000000009 (Pat Kim)",
  "created_at": "2026-09-14T16:00:00+00:00",
  "box_users": [
   {
    "id": "30000000009",
    "name": "Pat Kim",
    "login": "pat.kim@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ]
 }
]
