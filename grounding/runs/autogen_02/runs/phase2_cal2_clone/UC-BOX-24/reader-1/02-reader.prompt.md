Step 2. These are all the records in the service:

### box_file_versions (3)
{"id": "98201", "type": "file_version", "file_id": "8201", "name": "Acme MSA.pdf", "size": 48213, "version_number": "1", "created_at": "2026-06-01T09:00:00+00:00", "modified_at": "2026-06-01T09:00:00+00:00", "modified_by_id": "30000000001"}
{"id": "98202", "type": "file_version", "file_id": "8202", "name": "Indemnity clause review.pdf", "size": 48213, "version_number": "1", "created_at": "2026-06-01T09:00:00+00:00", "modified_at": "2026-06-01T09:00:00+00:00", "modified_by_id": "30000000001"}
{"id": "98203", "type": "file_version", "file_id": "8203", "name": "Globex MSA.pdf", "size": 48213, "version_number": "1", "created_at": "2026-06-01T09:00:00+00:00", "modified_at": "2026-06-01T09:00:00+00:00", "modified_by_id": "30000000001"}
### box_files (3)
{"id": "8201", "type": "file", "name": "Acme MSA.pdf", "parent_id": "8200", "owned_by_id": "30000000001", "created_by_id": "30000000001", "modified_by_id": "30000000001", "size": 48213, "extension": "pdf", "item_status": "active", "version_number": "1", "comment_count": 0, "tags": "[]", "collections": "[]", "created_at": "2026-06-01T09:00:00+00:00", "modified_at": "2026-06-01T09:00:00+00:00", "uploader_display_name": "Jordan Lee"}
{"id": "8202", "type": "file", "name": "Indemnity clause review.pdf", "parent_id": "8200", "owned_by_id": "30000000001", "created_by_id": "30000000001", "modified_by_id": "30000000001", "size": 48213, "extension": "pdf", "item_status": "active", "version_number": "1", "comment_count": 0, "tags": "[]", "collections": "[]", "created_at": "2026-06-01T09:00:00+00:00", "modified_at": "2026-06-01T09:00:00+00:00", "uploader_display_name": "Jordan Lee"}
{"id": "8203", "type": "file", "name": "Globex MSA.pdf", "parent_id": "8200", "owned_by_id": "30000000001", "created_by_id": "30000000001", "modified_by_id": "30000000001", "size": 48213, "extension": "pdf", "item_status": "active", "version_number": "1", "comment_count": 0, "tags": "[]", "collections": "[]", "created_at": "2026-06-01T09:00:00+00:00", "modified_at": "2026-06-01T09:00:00+00:00", "uploader_display_name": "Jordan Lee"}
### box_folders (2)
{"id": "0", "type": "folder", "name": "All Files", "owned_by_id": "30000000001", "item_status": "active", "size": 0}
{"id": "8200", "type": "folder", "name": "Legal", "parent_id": "0", "owned_by_id": "30000000001", "created_by_id": "30000000001", "modified_by_id": "30000000001", "item_status": "active", "size": 0, "tags": "[]", "collections": "[]", "created_at": "2026-06-01T09:00:00+00:00", "modified_at": "2026-06-01T09:00:00+00:00"}
### box_tasks (6)
{"id": "8301", "type": "task", "item_id": "8201", "item_type": "file", "message": "Please check the indemnity clause", "action": "review", "is_completed": false, "completion_rule": "all_assignees", "due_at": "2026-10-05T17:00:00+00:00", "created_by_id": "30000000009", "created_at": "2026-09-14T16:00:00+00:00"}
{"id": "8302", "type": "task", "item_id": "8203", "item_type": "file", "message": "Please check the indemnity clause", "action": "review", "is_completed": false, "completion_rule": "all_assignees", "due_at": "2026-10-05T17:00:00+00:00", "created_by_id": "30000000010", "created_at": "2026-09-14T16:00:00+00:00"}
{"id": "8303", "type": "task", "item_id": "8203", "item_type": "file", "message": "Please check the indemnity clause", "action": "review", "is_completed": false, "completion_rule": "all_assignees", "due_at": "2026-10-05T17:00:00+00:00", "created_by_id": "30000000009", "created_at": "2026-09-15T16:00:00+00:00"}
{"id": "8304", "type": "task", "item_id": "8202", "item_type": "file", "message": "Please check the payment terms", "action": "review", "is_completed": false, "completion_rule": "all_assignees", "due_at": "2026-10-05T17:00:00+00:00", "created_by_id": "30000000009", "created_at": "2026-09-14T16:00:00+00:00"}
{"id": "8305", "type": "task", "item_id": "8201", "item_type": "file", "message": "Please approve the invoice", "action": "review", "is_completed": false, "completion_rule": "all_assignees", "due_at": "2026-10-05T17:00:00+00:00", "created_by_id": "30000000009", "created_at": "2026-09-14T16:00:00+00:00"}
{"id": "8306", "type": "task", "item_id": "8202", "item_type": "file", "message": "Please check the indemnity clause", "action": "review", "is_completed": false, "completion_rule": "all_assignees", "due_at": "2026-10-05T17:00:00+00:00", "created_by_id": "30000000009", "created_at": "2026-09-14T16:00:00+00:00"}
### box_users (10)
{"id": "30000000001", "type": "user", "name": "Jordan Lee", "login": "jordan.lee@northwind.example", "status": "active", "role": "admin", "created_at": "2025-01-10T00:00:00Z", "modified_at": "2025-01-10T00:00:00Z"}
{"id": "30000000002", "type": "user", "name": "Maya Chen", "login": "maya.chen@northwind.example", "status": "active", "role": "user", "created_at": "2025-01-10T00:00:00Z", "modified_at": "2025-01-10T00:00:00Z"}
{"id": "30000000003", "type": "user", "name": "Maya Lopez", "login": "maya.lopez@northwind.example", "status": "active", "role": "user", "created_at": "2025-01-10T00:00:00Z", "modified_at": "2025-01-10T00:00:00Z"}
{"id": "30000000004", "type": "user", "name": "Leo Park", "login": "leo.park@northwind.example", "status": "active", "role": "user", "created_at": "2025-01-10T00:00:00Z", "modified_at": "2025-01-10T00:00:00Z"}
{"id": "30000000005", "type": "user", "name": "Dana Whitfield", "login": "dana.whitfield@northwind.example", "status": "active", "role": "user", "created_at": "2025-01-10T00:00:00Z", "modified_at": "2025-01-10T00:00:00Z"}
{"id": "30000000006", "type": "user", "name": "Priya Nair", "login": "priya.nair@northwind.example", "status": "active", "role": "user", "created_at": "2025-01-10T00:00:00Z", "modified_at": "2025-01-10T00:00:00Z"}
{"id": "30000000007", "type": "user", "name": "Omar Haddad", "login": "omar.haddad@northwind.example", "status": "active", "role": "user", "created_at": "2025-01-10T00:00:00Z", "modified_at": "2025-01-10T00:00:00Z"}
{"id": "30000000008", "type": "user", "name": "Sam Rivera", "login": "sam.rivera@northwind.example", "status": "active", "role": "user", "created_at": "2025-01-10T00:00:00Z", "modified_at": "2025-01-10T00:00:00Z"}
{"id": "30000000009", "type": "user", "name": "Pat Kim", "login": "pat.kim@northwind.example", "status": "active", "role": "user", "created_at": "2025-01-10T00:00:00Z", "modified_at": "2025-01-10T00:00:00Z"}
{"id": "30000000010", "type": "user", "name": "Pat Kimura", "login": "pat.kimura@northwind.example", "status": "active", "role": "user", "created_at": "2025-01-10T00:00:00Z", "modified_at": "2025-01-10T00:00:00Z"}

Use your own conditions from step 1 as the author's conditions, with these ids:
- r1: The record must be a task
- r2: The task must have been created by pat.kim@northwind.example
- r3: The task must have been created on September 14
- r4: The task must ask to check the indemnity clause

The candidate records are the rows of `box_tasks`: 8301, 8302, 8303, 8304, 8305, 8306.
For every candidate, give the ids of the conditions it fails under the careful reading (an empty list if it meets all of them), whether a careful colleague could still argue that it meets the request (contestable), and a short note. Then say whether the conditions faithfully capture the request as you read it in step 1 (and what differs). For each ambiguity you listed, say whether a careful reader would genuinely be unsure which reading was meant, and whether the readings select different candidates. Say whether the request reads like something a real user would write, without hints that only a test would contain. Finally, say whether the request asks for a single record (as opposed to allowing or asking for several), and why.