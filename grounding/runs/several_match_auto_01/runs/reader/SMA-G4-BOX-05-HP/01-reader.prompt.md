You check test cases for an AI assistant that acts in a workspace on a user's behalf. You read carefully
and literally, the way the user who wrote the request would mean it.

---

A user sent the assistant this request in their Box workspace:

    "Add the tag q3-close to all the PDFs in the Finance Reports folder owned by Maya Chen that Leo Park modified last."

The user is Jordan Lee. Below is every Box file in the workspace, with what the assistant can see about it. Which of
them does the user's request ask the assistant to act on?

List the id of every record the request covers, and only those. Read each condition of the request as the user
would mean it. If you cannot tell whether the user means a record, list it under `unsure` with the reason (and do
not list it in `ids`). Answer with JSON: {"ids": [...], "unsure": [{"id", "why"}], "notes": "..."}.

Records:
[
 {
  "id": "8201",
  "name": "Q3 revenue summary.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000002 (Maya Chen)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8202",
  "name": "Q3 expense summary.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8203",
  "name": "Q3 forecast summary.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8204",
  "name": "Q3 revenue summary.xlsx",
  "parent_id": "8102",
  "owned_by_id": "30000000002 (Maya Chen)",
  "created_by_id": "30000000002 (Maya Chen)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "xlsx",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Archive",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8102",
    "name": "Finance Archive",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8205",
  "name": "Q3 payroll summary.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000002 (Maya Chen)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Maya Chen",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000002",
    "name": "Maya Chen",
    "login": "maya.chen@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8206",
  "name": "Q3 sales summary.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000002 (Maya Chen)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8207",
  "name": "Q3 revenue report.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000002 (Maya Chen)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8208",
  "name": "Q3 revenue report - draft 001.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8209",
  "name": "Q3 revenue report - draft 002.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8210",
  "name": "Q3 revenue report - draft 003.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8211",
  "name": "Q3 revenue report - draft 004.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8212",
  "name": "Q3 revenue report - draft 005.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8213",
  "name": "Q3 revenue report - draft 006.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8214",
  "name": "Q3 revenue report - draft 007.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8215",
  "name": "Q3 revenue report - draft 008.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8216",
  "name": "Q3 revenue report - draft 009.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8217",
  "name": "Q3 revenue report - draft 010.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8218",
  "name": "Q3 revenue report - draft 011.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8219",
  "name": "Q3 revenue report - draft 012.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8220",
  "name": "Q3 revenue report - draft 013.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8221",
  "name": "Q3 revenue report - draft 014.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8222",
  "name": "Q3 revenue report - draft 015.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8223",
  "name": "Q3 revenue report - draft 016.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8224",
  "name": "Q3 revenue report - draft 017.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8225",
  "name": "Q3 revenue report - draft 018.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8226",
  "name": "Q3 revenue report - draft 019.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8227",
  "name": "Q3 revenue report - draft 020.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8228",
  "name": "Q3 revenue report - draft 021.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8229",
  "name": "Q3 revenue report - draft 022.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8230",
  "name": "Q3 revenue report - draft 023.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8231",
  "name": "Q3 revenue report - draft 024.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8232",
  "name": "Q3 revenue report - draft 025.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8233",
  "name": "Q3 revenue report - draft 026.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8234",
  "name": "Q3 revenue report - draft 027.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8235",
  "name": "Q3 revenue report - draft 028.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8236",
  "name": "Q3 revenue report - draft 029.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8237",
  "name": "Q3 revenue report - draft 030.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8238",
  "name": "Q3 revenue report - draft 031.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8239",
  "name": "Q3 revenue report - draft 032.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8240",
  "name": "Q3 revenue report - draft 033.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8241",
  "name": "Q3 revenue report - draft 034.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8242",
  "name": "Q3 revenue report - draft 035.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8243",
  "name": "Q3 revenue report - draft 036.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8244",
  "name": "Q3 revenue report - draft 037.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8245",
  "name": "Q3 revenue report - draft 038.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8246",
  "name": "Q3 revenue report - draft 039.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8247",
  "name": "Q3 revenue report - draft 040.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8248",
  "name": "Q3 revenue report - draft 041.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8249",
  "name": "Q3 revenue report - draft 042.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8250",
  "name": "Q3 revenue report - draft 043.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8251",
  "name": "Q3 revenue report - draft 044.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8252",
  "name": "Q3 revenue report - draft 045.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8253",
  "name": "Q3 revenue report - draft 046.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8254",
  "name": "Q3 revenue report - draft 047.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8255",
  "name": "Q3 revenue report - draft 048.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8256",
  "name": "Q3 revenue report - draft 049.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8257",
  "name": "Q3 revenue report - draft 050.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8258",
  "name": "Q3 revenue report - draft 051.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8259",
  "name": "Q3 revenue report - draft 052.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8260",
  "name": "Q3 revenue report - draft 053.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8261",
  "name": "Q3 revenue report - draft 054.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8262",
  "name": "Q3 revenue report - draft 055.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8263",
  "name": "Q3 revenue report - draft 056.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8264",
  "name": "Q3 revenue report - draft 057.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8265",
  "name": "Q3 revenue report - draft 058.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8266",
  "name": "Q3 revenue report - draft 059.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8267",
  "name": "Q3 revenue report - draft 060.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8268",
  "name": "Q3 revenue report - draft 061.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8269",
  "name": "Q3 revenue report - draft 062.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8270",
  "name": "Q3 revenue report - draft 063.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8271",
  "name": "Q3 revenue report - draft 064.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8272",
  "name": "Q3 revenue report - draft 065.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8273",
  "name": "Q3 revenue report - draft 066.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8274",
  "name": "Q3 revenue report - draft 067.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8275",
  "name": "Q3 revenue report - draft 068.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8276",
  "name": "Q3 revenue report - draft 069.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8277",
  "name": "Q3 revenue report - draft 070.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8278",
  "name": "Q3 revenue report - draft 071.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8279",
  "name": "Q3 revenue report - draft 072.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8280",
  "name": "Q3 revenue report - draft 073.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8281",
  "name": "Q3 revenue report - draft 074.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8282",
  "name": "Q3 revenue report - draft 075.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8283",
  "name": "Q3 revenue report - draft 076.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8284",
  "name": "Q3 revenue report - draft 077.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8285",
  "name": "Q3 revenue report - draft 078.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8286",
  "name": "Q3 revenue report - draft 079.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8287",
  "name": "Q3 revenue report - draft 080.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8288",
  "name": "Q3 revenue report - draft 081.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8289",
  "name": "Q3 revenue report - draft 082.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8290",
  "name": "Q3 revenue report - draft 083.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8291",
  "name": "Q3 revenue report - draft 084.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8292",
  "name": "Q3 revenue report - draft 085.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8293",
  "name": "Q3 revenue report - draft 086.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8294",
  "name": "Q3 revenue report - draft 087.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8295",
  "name": "Q3 revenue report - draft 088.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8296",
  "name": "Q3 revenue report - draft 089.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8297",
  "name": "Q3 revenue report - draft 090.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8298",
  "name": "Q3 revenue report - draft 091.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8299",
  "name": "Q3 revenue report - draft 092.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8300",
  "name": "Q3 revenue report - draft 093.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8301",
  "name": "Q3 revenue report - draft 094.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8302",
  "name": "Q3 revenue report - draft 095.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8303",
  "name": "Q3 revenue report - draft 096.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8304",
  "name": "Q3 revenue report - draft 097.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "8305",
  "name": "Q3 revenue report - draft 098.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000003 (Maya Lopez)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000004 (Leo Park)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Leo Park",
  "folder path": "All Files / Finance Reports",
  "box_users": [
   {
    "id": "30000000004",
    "name": "Leo Park",
    "login": "leo.park@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "8100",
    "name": "Finance Reports",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ]
 }
]
