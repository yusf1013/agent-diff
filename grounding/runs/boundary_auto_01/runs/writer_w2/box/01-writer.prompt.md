You write test requests for an AI assistant that acts in a workspace on a user's behalf. A test request must
read exactly as a real user would write it.

---

The assistant acts in Box as Jordan Lee, a Box admin. Each item below describes something a user might ask for that
the service will not do for this user; `why` says why. For each item write:

1. `request`: the message a real user would send asking for exactly that, in one or two sentences.
   - Name the record the way the user would (its title, name, channel, date), so it can be found among the records
     below. Use concrete values (a date, a name, a text) where the item leaves them open ("…").
   - Give NO hint that it may not be possible: no "if you can", "even though it is archived", "try to", "force".
   - Ask for the change itself, as a user who wants it made ("Set ...", "Change ...", "Make ...", "Move ..."). Never ask to "show" or "display" something as changed: that reads as a request to display it.
2. `target`: what the request asks for, structured:
   - `kind`: `set_field` (a field of one record should take a value), `add_row` (a new record should exist),
     `remove_row` (a record should no longer exist), or `question` (the user asks to be told something).
   - `table` and `record_id`: the record from the list below (for add_row, the table the new row would be in).
   - `field` and `value`: for set_field, the column and the value in the stored form (an id for a person or
     record, YYYY-MM-DD for a date, the exact text for a text).
   - `match`: for add_row and remove_row, a JSON object of column: value that identifies the row, as a string;
     otherwise "".
   Use "" for fields that do not apply.

Answer with JSON: {"items": [{"id", "request", "target"}]}, one per item, in order.

Items:
[
 {
  "id": "BOX-10",
  "item": "Make Leo Park the creator of Budget 2026.pdf.",
  "why": "created_by is set by Box"
 },
 {
  "id": "BOX-11",
  "item": "Make Leo Park the last modifier of Budget 2026.pdf.",
  "why": "modified_by follows the last change"
 },
 {
  "id": "BOX-25",
  "item": "Make Leo Park the creator of the Finance folder.",
  "why": "set by Box; not in the update schema"
 },
 {
  "id": "BOX-26",
  "item": "Make Leo Park the last modifier of the Finance folder.",
  "why": "set by Box; not in the update schema"
 },
 {
  "id": "BOX-27",
  "item": "Make Maya Chen the creator of the review task.",
  "why": "set by Box; not in the update schema"
 },
 {
  "id": "BOX-29",
  "item": "Make Priya the creator of the Finance hub.",
  "why": "set by Box; not in the update schema"
 },
 {
  "id": "BOX-30",
  "item": "Make Priya the last updater of the Finance hub.",
  "why": "set by Box; not in the update schema"
 }
]

Records in the workspace (table: rows):
{"box_users": [{"id": "30000000001", "name": "Jordan Lee", "login": "jordan.lee@northwind.example", "status": "active", "role": "admin"}, {"id": "30000000002", "name": "Maya Chen", "login": "maya.chen@northwind.example", "status": "active", "role": "user"}, {"id": "30000000003", "name": "Maya Lopez", "login": "maya.lopez@northwind.example", "status": "active", "role": "user"}, {"id": "30000000004", "name": "Leo Park", "login": "leo.park@northwind.example", "status": "active", "role": "user"}, {"id": "30000000005", "name": "Dana Whitfield", "login": "dana.whitfield@northwind.example", "status": "active", "role": "user"}, {"id": "30000000006", "name": "Priya Nair", "login": "priya.nair@northwind.example", "status": "active", "role": "user"}, {"id": "30000000007", "name": "Omar Haddad", "login": "omar.haddad@northwind.example", "status": "active", "role": "user"}, {"id": "30000000008", "name": "Sam Rivera", "login": "sam.rivera@northwind.example", "status": "active", "role": "user"}], "box_folders": [{"id": "0", "name": "All Files", "owned_by_id": "30000000001", "size": 0}, {"id": "7100", "name": "Finance", "parent_id": "0", "owned_by_id": "30000000001", "created_by_id": "30000000001", "modified_by_id": "30000000001", "size": 0, "tags": "[]"}, {"id": "7101", "name": "Q1", "parent_id": "7100", "owned_by_id": "30000000001", "created_by_id": "30000000001", "modified_by_id": "30000000001", "size": 0, "tags": "[]"}, {"id": "7102", "name": "Archive", "parent_id": "0", "owned_by_id": "30000000001", "created_by_id": "30000000001", "modified_by_id": "30000000001", "size": 0, "tags": "[]"}], "box_files": [{"id": "7111", "name": "Budget 2026.pdf", "parent_id": "7100", "owned_by_id": "30000000001", "created_by_id": "30000000001", "modified_by_id": "30000000001", "size": 48213, "extension": "pdf", "comment_count": 2, "tags": "[]", "uploader_display_name": "Jordan Lee"}, {"id": "7112", "name": "Budget 2026.docx", "parent_id": "7100", "owned_by_id": "30000000001", "created_by_id": "30000000001", "modified_by_id": "30000000001", "size": 48213, "extension": "docx", "comment_count": 0, "tags": "[]", "uploader_display_name": "Jordan Lee"}, {"id": "7113", "name": "Budget 2026.pdf", "parent_id": "7102", "owned_by_id": "30000000001", "created_by_id": "30000000001", "modified_by_id": "30000000001", "size": 48213, "extension": "pdf", "comment_count": 0, "tags": "[]", "uploader_display_name": "Jordan Lee"}], "box_file_versions": [{"id": "97111", "file_id": "7111", "name": "Budget 2026.pdf", "size": 48213, "modified_by_id": "30000000001"}, {"id": "97112", "file_id": "7112", "name": "Budget 2026.docx", "size": 48213, "modified_by_id": "30000000001"}, {"id": "97113", "file_id": "7113", "name": "Budget 2026.pdf", "size": 48213, "modified_by_id": "30000000001"}], "box_comments": [{"id": "71111", "file_id": "7111", "item_id": "7111", "item_type": "file", "message": "Totals look of.", "created_by_id": "30000000006", "is_reply_comment": false}, {"id": "71112", "file_id": "7111", "item_id": "7111", "item_type": "file", "message": "Numbers updated.", "created_by_id": "30000000007", "is_reply_comment": false}], "box_tasks": [{"id": "7120", "item_id": "7111", "item_type": "file", "message": "Review the contract", "action": "review", "is_completed": false, "completion_rule": "all_assignees", "created_by_id": "30000000001"}], "box_task_assignments": [{"id": "7121", "task_id": "7120", "item_id": "7111", "item_type": "file", "assigned_to_id": "30000000002", "assigned_by_id": "30000000001", "resolution_state": "incomplete", "assigned_at": "2026-06-01T09:00:00+00:00"}], "box_hubs": [{"id": "7300", "title": "Finance hub", "description": "Finance hub materials", "created_by_id": "30000000001", "updated_by_id": "30000000001", "is_ai_enabled": false, "is_collaboration_restricted_to_enterprise": false, "can_non_owners_invite": true, "can_shared_link_be_created": true, "view_count": 0}]}
