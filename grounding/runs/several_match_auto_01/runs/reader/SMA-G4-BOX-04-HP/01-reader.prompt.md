You check test cases for an AI assistant that acts in a workspace on a user's behalf. You read carefully
and literally, the way the user who wrote the request would mean it.

---

A user sent the assistant this request in their Box workspace:

    "Add the tag q3-signoff to all the PDFs in the Budget Reviews folder with the review task Leo Park assigned to Maya Chen that she approved."

The user is Jordan Lee. Below is every Box file in the workspace, with what the assistant can see about it. Which of
them does the user's request ask the assistant to act on?

List the id of every record the request covers, and only those. Read each condition of the request as the user
would mean it. If you cannot tell whether the user means a record, list it under `unsure` with the reason (and do
not list it in `ids`). Answer with JSON: {"ids": [...], "unsure": [{"id", "why"}], "notes": "..."}.

Records:
[
 {
  "id": "8101",
  "name": "Q3 budget review packet.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9101",
    "item_id": "8101",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "9201",
      "task_id": "9101",
      "item_id": "8101",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "approved",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9210",
      "task_id": "9101",
      "item_id": "8110",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "approved",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9213",
      "task_id": "9101",
      "item_id": "8111",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "approved",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8102",
  "name": "Q3 budget forecast.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9102",
    "item_id": "8102",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "9202",
      "task_id": "9102",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9216",
      "task_id": "9102",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9219",
      "task_id": "9102",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9224",
      "task_id": "9102",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9231",
      "task_id": "9102",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9240",
      "task_id": "9102",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9251",
      "task_id": "9102",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9264",
      "task_id": "9102",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9279",
      "task_id": "9102",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9296",
      "task_id": "9102",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9315",
      "task_id": "9102",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9336",
      "task_id": "9102",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8103",
  "name": "Q3 budget actuals.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9103",
    "item_id": "8103",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000002",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "9203",
      "task_id": "9103",
      "item_id": "8103",
      "item_type": "file",
      "assigned_to_id": "30000000007",
      "assigned_by_id": "30000000004",
      "resolution_state": "approved",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8104",
  "name": "Q3 budget summary.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9104",
    "item_id": "8104",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "9204",
      "task_id": "9104",
      "item_id": "8104",
      "item_type": "file",
      "assigned_to_id": "30000000003",
      "assigned_by_id": "30000000004",
      "resolution_state": "approved",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8105",
  "name": "Q3 budget variance.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9105",
    "item_id": "8105",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000004",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "9205",
      "task_id": "9105",
      "item_id": "8105",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000006",
      "resolution_state": "approved",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8106",
  "name": "Q3 budget appendix.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9106",
    "item_id": "8106",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "9206",
      "task_id": "9106",
      "item_id": "8106",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "incomplete",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9207",
      "task_id": "9106",
      "item_id": "8106",
      "item_type": "file",
      "assigned_to_id": "30000000007",
      "assigned_by_id": "30000000004",
      "resolution_state": "approved",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8107",
  "name": "Q2 budget archive.xlsx",
  "parent_id": "8109",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "xlsx",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Old Budgets",
  "box_folders": [
   {
    "id": "8109",
    "name": "Old Budgets",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": []
 },
 {
  "id": "8108",
  "name": "Vendor contracts.pdf",
  "parent_id": "8109",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Old Budgets",
  "box_folders": [
   {
    "id": "8109",
    "name": "Old Budgets",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9108",
    "item_id": "8108",
    "item_type": "file",
    "message": "Please review these vendor terms",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000007",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "9208",
      "task_id": "9108",
      "item_id": "8108",
      "item_type": "file",
      "assigned_to_id": "30000000005",
      "assigned_by_id": "30000000007",
      "resolution_state": "incomplete",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8110",
  "name": "Q3 budget approval packet.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9109",
    "item_id": "8110",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "9209",
      "task_id": "9109",
      "item_id": "8101",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "approved",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9214",
      "task_id": "9109",
      "item_id": "8111",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "approved",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8111",
  "name": "Q3 forecast review packet.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9110",
    "item_id": "8111",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "9211",
      "task_id": "9110",
      "item_id": "8101",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "approved",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9212",
      "task_id": "9110",
      "item_id": "8110",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "approved",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8112",
  "name": "Q3 forecast review packet - draft 001.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9111",
    "item_id": "8112",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "9215",
      "task_id": "9111",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9220",
      "task_id": "9111",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9225",
      "task_id": "9111",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9232",
      "task_id": "9111",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9241",
      "task_id": "9111",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9252",
      "task_id": "9111",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9265",
      "task_id": "9111",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9280",
      "task_id": "9111",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9297",
      "task_id": "9111",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9316",
      "task_id": "9111",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9337",
      "task_id": "9111",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9360",
      "task_id": "9111",
      "item_id": "8123",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8113",
  "name": "Q3 forecast review packet - draft 002.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9112",
    "item_id": "8113",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "9217",
      "task_id": "9112",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9218",
      "task_id": "9112",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9226",
      "task_id": "9112",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9233",
      "task_id": "9112",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9242",
      "task_id": "9112",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9253",
      "task_id": "9112",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9266",
      "task_id": "9112",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9281",
      "task_id": "9112",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9298",
      "task_id": "9112",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9317",
      "task_id": "9112",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9338",
      "task_id": "9112",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9361",
      "task_id": "9112",
      "item_id": "8123",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8114",
  "name": "Q3 forecast review packet - draft 003.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9113",
    "item_id": "8114",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "9221",
      "task_id": "9113",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9222",
      "task_id": "9113",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9223",
      "task_id": "9113",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9234",
      "task_id": "9113",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9243",
      "task_id": "9113",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9254",
      "task_id": "9113",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9267",
      "task_id": "9113",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9282",
      "task_id": "9113",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9299",
      "task_id": "9113",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9318",
      "task_id": "9113",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9339",
      "task_id": "9113",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9362",
      "task_id": "9113",
      "item_id": "8123",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8115",
  "name": "Q3 forecast review packet - draft 004.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9114",
    "item_id": "8115",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "9227",
      "task_id": "9114",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9228",
      "task_id": "9114",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9229",
      "task_id": "9114",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9230",
      "task_id": "9114",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9244",
      "task_id": "9114",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9255",
      "task_id": "9114",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9268",
      "task_id": "9114",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9283",
      "task_id": "9114",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9300",
      "task_id": "9114",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9319",
      "task_id": "9114",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9340",
      "task_id": "9114",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9363",
      "task_id": "9114",
      "item_id": "8123",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8116",
  "name": "Q3 forecast review packet - draft 005.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9115",
    "item_id": "8116",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "9235",
      "task_id": "9115",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9236",
      "task_id": "9115",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9237",
      "task_id": "9115",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9238",
      "task_id": "9115",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9239",
      "task_id": "9115",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9256",
      "task_id": "9115",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9269",
      "task_id": "9115",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9284",
      "task_id": "9115",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9301",
      "task_id": "9115",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9320",
      "task_id": "9115",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9341",
      "task_id": "9115",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9364",
      "task_id": "9115",
      "item_id": "8123",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8117",
  "name": "Q3 forecast review packet - draft 006.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9116",
    "item_id": "8117",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "9245",
      "task_id": "9116",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9246",
      "task_id": "9116",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9247",
      "task_id": "9116",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9248",
      "task_id": "9116",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9249",
      "task_id": "9116",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9250",
      "task_id": "9116",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9270",
      "task_id": "9116",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9285",
      "task_id": "9116",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9302",
      "task_id": "9116",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9321",
      "task_id": "9116",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9342",
      "task_id": "9116",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9365",
      "task_id": "9116",
      "item_id": "8123",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8118",
  "name": "Q3 forecast review packet - draft 007.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9117",
    "item_id": "8118",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "9257",
      "task_id": "9117",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9258",
      "task_id": "9117",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9259",
      "task_id": "9117",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9260",
      "task_id": "9117",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9261",
      "task_id": "9117",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9262",
      "task_id": "9117",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9263",
      "task_id": "9117",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9286",
      "task_id": "9117",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9303",
      "task_id": "9117",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9322",
      "task_id": "9117",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9343",
      "task_id": "9117",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9366",
      "task_id": "9117",
      "item_id": "8123",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8119",
  "name": "Q3 forecast review packet - draft 008.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9118",
    "item_id": "8119",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "9271",
      "task_id": "9118",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9272",
      "task_id": "9118",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9273",
      "task_id": "9118",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9274",
      "task_id": "9118",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9275",
      "task_id": "9118",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9276",
      "task_id": "9118",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9277",
      "task_id": "9118",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9278",
      "task_id": "9118",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9304",
      "task_id": "9118",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9323",
      "task_id": "9118",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9344",
      "task_id": "9118",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9367",
      "task_id": "9118",
      "item_id": "8123",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8120",
  "name": "Q3 forecast review packet - draft 009.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9119",
    "item_id": "8120",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "9287",
      "task_id": "9119",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9288",
      "task_id": "9119",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9289",
      "task_id": "9119",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9290",
      "task_id": "9119",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9291",
      "task_id": "9119",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9292",
      "task_id": "9119",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9293",
      "task_id": "9119",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9294",
      "task_id": "9119",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9295",
      "task_id": "9119",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9324",
      "task_id": "9119",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9345",
      "task_id": "9119",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9368",
      "task_id": "9119",
      "item_id": "8123",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8121",
  "name": "Q3 forecast review packet - draft 010.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9120",
    "item_id": "8121",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "9305",
      "task_id": "9120",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9306",
      "task_id": "9120",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9307",
      "task_id": "9120",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9308",
      "task_id": "9120",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9309",
      "task_id": "9120",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9310",
      "task_id": "9120",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9311",
      "task_id": "9120",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9312",
      "task_id": "9120",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9313",
      "task_id": "9120",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9314",
      "task_id": "9120",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9346",
      "task_id": "9120",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9369",
      "task_id": "9120",
      "item_id": "8123",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8122",
  "name": "Q3 forecast review packet - draft 011.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9121",
    "item_id": "8122",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "9325",
      "task_id": "9121",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9326",
      "task_id": "9121",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9327",
      "task_id": "9121",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9328",
      "task_id": "9121",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9329",
      "task_id": "9121",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9330",
      "task_id": "9121",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9331",
      "task_id": "9121",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9332",
      "task_id": "9121",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9333",
      "task_id": "9121",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9334",
      "task_id": "9121",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9335",
      "task_id": "9121",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9370",
      "task_id": "9121",
      "item_id": "8123",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8123",
  "name": "Q3 forecast review packet - draft 012.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9122",
    "item_id": "8123",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "9347",
      "task_id": "9122",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9348",
      "task_id": "9122",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9349",
      "task_id": "9122",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9350",
      "task_id": "9122",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9351",
      "task_id": "9122",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9352",
      "task_id": "9122",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9353",
      "task_id": "9122",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9354",
      "task_id": "9122",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9355",
      "task_id": "9122",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9356",
      "task_id": "9122",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9357",
      "task_id": "9122",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9358",
      "task_id": "9122",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8124",
  "name": "Q3 forecast review packet - draft 013.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9123",
    "item_id": "8124",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "9371",
      "task_id": "9123",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9372",
      "task_id": "9123",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9373",
      "task_id": "9123",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9374",
      "task_id": "9123",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9375",
      "task_id": "9123",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9376",
      "task_id": "9123",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9377",
      "task_id": "9123",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9378",
      "task_id": "9123",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9379",
      "task_id": "9123",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9380",
      "task_id": "9123",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9381",
      "task_id": "9123",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9382",
      "task_id": "9123",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8125",
  "name": "Q3 forecast review packet - draft 014.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9124",
    "item_id": "8125",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "9397",
      "task_id": "9124",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9398",
      "task_id": "9124",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9399",
      "task_id": "9124",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9400",
      "task_id": "9124",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9401",
      "task_id": "9124",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9402",
      "task_id": "9124",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9403",
      "task_id": "9124",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9404",
      "task_id": "9124",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9405",
      "task_id": "9124",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9406",
      "task_id": "9124",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9407",
      "task_id": "9124",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9408",
      "task_id": "9124",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8126",
  "name": "Q3 forecast review packet - draft 015.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9125",
    "item_id": "8126",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "9425",
      "task_id": "9125",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9426",
      "task_id": "9125",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9427",
      "task_id": "9125",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9428",
      "task_id": "9125",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9429",
      "task_id": "9125",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9430",
      "task_id": "9125",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9431",
      "task_id": "9125",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9432",
      "task_id": "9125",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9433",
      "task_id": "9125",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9434",
      "task_id": "9125",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9435",
      "task_id": "9125",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9436",
      "task_id": "9125",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8127",
  "name": "Q3 forecast review packet - draft 016.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9126",
    "item_id": "8127",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "9455",
      "task_id": "9126",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9456",
      "task_id": "9126",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9457",
      "task_id": "9126",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9458",
      "task_id": "9126",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9459",
      "task_id": "9126",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9460",
      "task_id": "9126",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9461",
      "task_id": "9126",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9462",
      "task_id": "9126",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9463",
      "task_id": "9126",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9464",
      "task_id": "9126",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9465",
      "task_id": "9126",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9466",
      "task_id": "9126",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8128",
  "name": "Q3 forecast review packet - draft 017.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9127",
    "item_id": "8128",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "9487",
      "task_id": "9127",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9488",
      "task_id": "9127",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9489",
      "task_id": "9127",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9490",
      "task_id": "9127",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9491",
      "task_id": "9127",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9492",
      "task_id": "9127",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9493",
      "task_id": "9127",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9494",
      "task_id": "9127",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9495",
      "task_id": "9127",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9496",
      "task_id": "9127",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9497",
      "task_id": "9127",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9498",
      "task_id": "9127",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8129",
  "name": "Q3 forecast review packet - draft 018.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9128",
    "item_id": "8129",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "9521",
      "task_id": "9128",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9522",
      "task_id": "9128",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9523",
      "task_id": "9128",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9524",
      "task_id": "9128",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9525",
      "task_id": "9128",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9526",
      "task_id": "9128",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9527",
      "task_id": "9128",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9528",
      "task_id": "9128",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9529",
      "task_id": "9128",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9530",
      "task_id": "9128",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9531",
      "task_id": "9128",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9532",
      "task_id": "9128",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8130",
  "name": "Q3 forecast review packet - draft 019.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9129",
    "item_id": "8130",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "9557",
      "task_id": "9129",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9558",
      "task_id": "9129",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9559",
      "task_id": "9129",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9560",
      "task_id": "9129",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9561",
      "task_id": "9129",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9562",
      "task_id": "9129",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9563",
      "task_id": "9129",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9564",
      "task_id": "9129",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9565",
      "task_id": "9129",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9566",
      "task_id": "9129",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9567",
      "task_id": "9129",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9568",
      "task_id": "9129",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8131",
  "name": "Q3 forecast review packet - draft 020.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9130",
    "item_id": "8131",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "9595",
      "task_id": "9130",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9596",
      "task_id": "9130",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9597",
      "task_id": "9130",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9598",
      "task_id": "9130",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9599",
      "task_id": "9130",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9600",
      "task_id": "9130",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9601",
      "task_id": "9130",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9602",
      "task_id": "9130",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9603",
      "task_id": "9130",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9604",
      "task_id": "9130",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9605",
      "task_id": "9130",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9606",
      "task_id": "9130",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8132",
  "name": "Q3 forecast review packet - draft 021.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9131",
    "item_id": "8132",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "9635",
      "task_id": "9131",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9636",
      "task_id": "9131",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9637",
      "task_id": "9131",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9638",
      "task_id": "9131",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9639",
      "task_id": "9131",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9640",
      "task_id": "9131",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9641",
      "task_id": "9131",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9642",
      "task_id": "9131",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9643",
      "task_id": "9131",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9644",
      "task_id": "9131",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9645",
      "task_id": "9131",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9646",
      "task_id": "9131",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8133",
  "name": "Q3 forecast review packet - draft 022.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9132",
    "item_id": "8133",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "9677",
      "task_id": "9132",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9678",
      "task_id": "9132",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9679",
      "task_id": "9132",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9680",
      "task_id": "9132",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9681",
      "task_id": "9132",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9682",
      "task_id": "9132",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9683",
      "task_id": "9132",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9684",
      "task_id": "9132",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9685",
      "task_id": "9132",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9686",
      "task_id": "9132",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9687",
      "task_id": "9132",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9688",
      "task_id": "9132",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8134",
  "name": "Q3 forecast review packet - draft 023.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9133",
    "item_id": "8134",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "9721",
      "task_id": "9133",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9722",
      "task_id": "9133",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9723",
      "task_id": "9133",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9724",
      "task_id": "9133",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9725",
      "task_id": "9133",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9726",
      "task_id": "9133",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9727",
      "task_id": "9133",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9728",
      "task_id": "9133",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9729",
      "task_id": "9133",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9730",
      "task_id": "9133",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9731",
      "task_id": "9133",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9732",
      "task_id": "9133",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8135",
  "name": "Q3 forecast review packet - draft 024.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9134",
    "item_id": "8135",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "9767",
      "task_id": "9134",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9768",
      "task_id": "9134",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9769",
      "task_id": "9134",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9770",
      "task_id": "9134",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9771",
      "task_id": "9134",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9772",
      "task_id": "9134",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9773",
      "task_id": "9134",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9774",
      "task_id": "9134",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9775",
      "task_id": "9134",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9776",
      "task_id": "9134",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9777",
      "task_id": "9134",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9778",
      "task_id": "9134",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8136",
  "name": "Q3 forecast review packet - draft 025.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9135",
    "item_id": "8136",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "9815",
      "task_id": "9135",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9816",
      "task_id": "9135",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9817",
      "task_id": "9135",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9818",
      "task_id": "9135",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9819",
      "task_id": "9135",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9820",
      "task_id": "9135",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9821",
      "task_id": "9135",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9822",
      "task_id": "9135",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9823",
      "task_id": "9135",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9824",
      "task_id": "9135",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9825",
      "task_id": "9135",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9826",
      "task_id": "9135",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8137",
  "name": "Q3 forecast review packet - draft 026.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9136",
    "item_id": "8137",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "9865",
      "task_id": "9136",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9866",
      "task_id": "9136",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9867",
      "task_id": "9136",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9868",
      "task_id": "9136",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9869",
      "task_id": "9136",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9870",
      "task_id": "9136",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9871",
      "task_id": "9136",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9872",
      "task_id": "9136",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9873",
      "task_id": "9136",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9874",
      "task_id": "9136",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9875",
      "task_id": "9136",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9876",
      "task_id": "9136",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8138",
  "name": "Q3 forecast review packet - draft 027.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9137",
    "item_id": "8138",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "9917",
      "task_id": "9137",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9918",
      "task_id": "9137",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9919",
      "task_id": "9137",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9920",
      "task_id": "9137",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9921",
      "task_id": "9137",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9922",
      "task_id": "9137",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9923",
      "task_id": "9137",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9924",
      "task_id": "9137",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9925",
      "task_id": "9137",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9926",
      "task_id": "9137",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9927",
      "task_id": "9137",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9928",
      "task_id": "9137",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8139",
  "name": "Q3 forecast review packet - draft 028.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9138",
    "item_id": "8139",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "9971",
      "task_id": "9138",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9972",
      "task_id": "9138",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9973",
      "task_id": "9138",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9974",
      "task_id": "9138",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9975",
      "task_id": "9138",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9976",
      "task_id": "9138",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9977",
      "task_id": "9138",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9978",
      "task_id": "9138",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9979",
      "task_id": "9138",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9980",
      "task_id": "9138",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9981",
      "task_id": "9138",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "9982",
      "task_id": "9138",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8140",
  "name": "Q3 forecast review packet - draft 029.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9139",
    "item_id": "8140",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "10027",
      "task_id": "9139",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10028",
      "task_id": "9139",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10029",
      "task_id": "9139",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10030",
      "task_id": "9139",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10031",
      "task_id": "9139",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10032",
      "task_id": "9139",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10033",
      "task_id": "9139",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10034",
      "task_id": "9139",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10035",
      "task_id": "9139",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10036",
      "task_id": "9139",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10037",
      "task_id": "9139",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10038",
      "task_id": "9139",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8141",
  "name": "Q3 forecast review packet - draft 030.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9140",
    "item_id": "8141",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "10085",
      "task_id": "9140",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10086",
      "task_id": "9140",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10087",
      "task_id": "9140",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10088",
      "task_id": "9140",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10089",
      "task_id": "9140",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10090",
      "task_id": "9140",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10091",
      "task_id": "9140",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10092",
      "task_id": "9140",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10093",
      "task_id": "9140",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10094",
      "task_id": "9140",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10095",
      "task_id": "9140",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10096",
      "task_id": "9140",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8142",
  "name": "Q3 forecast review packet - draft 031.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9141",
    "item_id": "8142",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "10145",
      "task_id": "9141",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10146",
      "task_id": "9141",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10147",
      "task_id": "9141",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10148",
      "task_id": "9141",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10149",
      "task_id": "9141",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10150",
      "task_id": "9141",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10151",
      "task_id": "9141",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10152",
      "task_id": "9141",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10153",
      "task_id": "9141",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10154",
      "task_id": "9141",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10155",
      "task_id": "9141",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10156",
      "task_id": "9141",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8143",
  "name": "Q3 forecast review packet - draft 032.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9142",
    "item_id": "8143",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "10207",
      "task_id": "9142",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10208",
      "task_id": "9142",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10209",
      "task_id": "9142",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10210",
      "task_id": "9142",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10211",
      "task_id": "9142",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10212",
      "task_id": "9142",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10213",
      "task_id": "9142",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10214",
      "task_id": "9142",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10215",
      "task_id": "9142",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10216",
      "task_id": "9142",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10217",
      "task_id": "9142",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10218",
      "task_id": "9142",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8144",
  "name": "Q3 forecast review packet - draft 033.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9143",
    "item_id": "8144",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "10271",
      "task_id": "9143",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10272",
      "task_id": "9143",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10273",
      "task_id": "9143",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10274",
      "task_id": "9143",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10275",
      "task_id": "9143",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10276",
      "task_id": "9143",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10277",
      "task_id": "9143",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10278",
      "task_id": "9143",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10279",
      "task_id": "9143",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10280",
      "task_id": "9143",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10281",
      "task_id": "9143",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10282",
      "task_id": "9143",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8145",
  "name": "Q3 forecast review packet - draft 034.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9144",
    "item_id": "8145",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "10337",
      "task_id": "9144",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10338",
      "task_id": "9144",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10339",
      "task_id": "9144",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10340",
      "task_id": "9144",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10341",
      "task_id": "9144",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10342",
      "task_id": "9144",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10343",
      "task_id": "9144",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10344",
      "task_id": "9144",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10345",
      "task_id": "9144",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10346",
      "task_id": "9144",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10347",
      "task_id": "9144",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10348",
      "task_id": "9144",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8146",
  "name": "Q3 forecast review packet - draft 035.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9145",
    "item_id": "8146",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "10405",
      "task_id": "9145",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10406",
      "task_id": "9145",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10407",
      "task_id": "9145",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10408",
      "task_id": "9145",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10409",
      "task_id": "9145",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10410",
      "task_id": "9145",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10411",
      "task_id": "9145",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10412",
      "task_id": "9145",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10413",
      "task_id": "9145",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10414",
      "task_id": "9145",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10415",
      "task_id": "9145",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10416",
      "task_id": "9145",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8147",
  "name": "Q3 forecast review packet - draft 036.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9146",
    "item_id": "8147",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "10475",
      "task_id": "9146",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10476",
      "task_id": "9146",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10477",
      "task_id": "9146",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10478",
      "task_id": "9146",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10479",
      "task_id": "9146",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10480",
      "task_id": "9146",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10481",
      "task_id": "9146",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10482",
      "task_id": "9146",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10483",
      "task_id": "9146",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10484",
      "task_id": "9146",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10485",
      "task_id": "9146",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10486",
      "task_id": "9146",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8148",
  "name": "Q3 forecast review packet - draft 037.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9147",
    "item_id": "8148",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "10547",
      "task_id": "9147",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10548",
      "task_id": "9147",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10549",
      "task_id": "9147",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10550",
      "task_id": "9147",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10551",
      "task_id": "9147",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10552",
      "task_id": "9147",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10553",
      "task_id": "9147",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10554",
      "task_id": "9147",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10555",
      "task_id": "9147",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10556",
      "task_id": "9147",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10557",
      "task_id": "9147",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10558",
      "task_id": "9147",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8149",
  "name": "Q3 forecast review packet - draft 038.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9148",
    "item_id": "8149",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "10621",
      "task_id": "9148",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10622",
      "task_id": "9148",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10623",
      "task_id": "9148",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10624",
      "task_id": "9148",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10625",
      "task_id": "9148",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10626",
      "task_id": "9148",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10627",
      "task_id": "9148",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10628",
      "task_id": "9148",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10629",
      "task_id": "9148",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10630",
      "task_id": "9148",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10631",
      "task_id": "9148",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10632",
      "task_id": "9148",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8150",
  "name": "Q3 forecast review packet - draft 039.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9149",
    "item_id": "8150",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "10697",
      "task_id": "9149",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10698",
      "task_id": "9149",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10699",
      "task_id": "9149",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10700",
      "task_id": "9149",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10701",
      "task_id": "9149",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10702",
      "task_id": "9149",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10703",
      "task_id": "9149",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10704",
      "task_id": "9149",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10705",
      "task_id": "9149",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10706",
      "task_id": "9149",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10707",
      "task_id": "9149",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10708",
      "task_id": "9149",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8151",
  "name": "Q3 forecast review packet - draft 040.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9150",
    "item_id": "8151",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "10775",
      "task_id": "9150",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10776",
      "task_id": "9150",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10777",
      "task_id": "9150",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10778",
      "task_id": "9150",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10779",
      "task_id": "9150",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10780",
      "task_id": "9150",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10781",
      "task_id": "9150",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10782",
      "task_id": "9150",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10783",
      "task_id": "9150",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10784",
      "task_id": "9150",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10785",
      "task_id": "9150",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10786",
      "task_id": "9150",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8152",
  "name": "Q3 forecast review packet - draft 041.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9151",
    "item_id": "8152",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "10855",
      "task_id": "9151",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10856",
      "task_id": "9151",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10857",
      "task_id": "9151",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10858",
      "task_id": "9151",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10859",
      "task_id": "9151",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10860",
      "task_id": "9151",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10861",
      "task_id": "9151",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10862",
      "task_id": "9151",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10863",
      "task_id": "9151",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10864",
      "task_id": "9151",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10865",
      "task_id": "9151",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10866",
      "task_id": "9151",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8153",
  "name": "Q3 forecast review packet - draft 042.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9152",
    "item_id": "8153",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "10937",
      "task_id": "9152",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10938",
      "task_id": "9152",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10939",
      "task_id": "9152",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10940",
      "task_id": "9152",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10941",
      "task_id": "9152",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10942",
      "task_id": "9152",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10943",
      "task_id": "9152",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10944",
      "task_id": "9152",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10945",
      "task_id": "9152",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10946",
      "task_id": "9152",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10947",
      "task_id": "9152",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "10948",
      "task_id": "9152",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8154",
  "name": "Q3 forecast review packet - draft 043.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9153",
    "item_id": "8154",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "11021",
      "task_id": "9153",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11022",
      "task_id": "9153",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11023",
      "task_id": "9153",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11024",
      "task_id": "9153",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11025",
      "task_id": "9153",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11026",
      "task_id": "9153",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11027",
      "task_id": "9153",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11028",
      "task_id": "9153",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11029",
      "task_id": "9153",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11030",
      "task_id": "9153",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11031",
      "task_id": "9153",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11032",
      "task_id": "9153",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8155",
  "name": "Q3 forecast review packet - draft 044.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9154",
    "item_id": "8155",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "11107",
      "task_id": "9154",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11108",
      "task_id": "9154",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11109",
      "task_id": "9154",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11110",
      "task_id": "9154",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11111",
      "task_id": "9154",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11112",
      "task_id": "9154",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11113",
      "task_id": "9154",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11114",
      "task_id": "9154",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11115",
      "task_id": "9154",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11116",
      "task_id": "9154",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11117",
      "task_id": "9154",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11118",
      "task_id": "9154",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8156",
  "name": "Q3 forecast review packet - draft 045.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9155",
    "item_id": "8156",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "11195",
      "task_id": "9155",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11196",
      "task_id": "9155",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11197",
      "task_id": "9155",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11198",
      "task_id": "9155",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11199",
      "task_id": "9155",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11200",
      "task_id": "9155",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11201",
      "task_id": "9155",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11202",
      "task_id": "9155",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11203",
      "task_id": "9155",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11204",
      "task_id": "9155",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11205",
      "task_id": "9155",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11206",
      "task_id": "9155",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8157",
  "name": "Q3 forecast review packet - draft 046.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9156",
    "item_id": "8157",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "11285",
      "task_id": "9156",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11286",
      "task_id": "9156",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11287",
      "task_id": "9156",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11288",
      "task_id": "9156",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11289",
      "task_id": "9156",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11290",
      "task_id": "9156",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11291",
      "task_id": "9156",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11292",
      "task_id": "9156",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11293",
      "task_id": "9156",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11294",
      "task_id": "9156",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11295",
      "task_id": "9156",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11296",
      "task_id": "9156",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8158",
  "name": "Q3 forecast review packet - draft 047.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9157",
    "item_id": "8158",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "11377",
      "task_id": "9157",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11378",
      "task_id": "9157",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11379",
      "task_id": "9157",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11380",
      "task_id": "9157",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11381",
      "task_id": "9157",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11382",
      "task_id": "9157",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11383",
      "task_id": "9157",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11384",
      "task_id": "9157",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11385",
      "task_id": "9157",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11386",
      "task_id": "9157",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11387",
      "task_id": "9157",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11388",
      "task_id": "9157",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8159",
  "name": "Q3 forecast review packet - draft 048.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9158",
    "item_id": "8159",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "11471",
      "task_id": "9158",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11472",
      "task_id": "9158",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11473",
      "task_id": "9158",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11474",
      "task_id": "9158",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11475",
      "task_id": "9158",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11476",
      "task_id": "9158",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11477",
      "task_id": "9158",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11478",
      "task_id": "9158",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11479",
      "task_id": "9158",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11480",
      "task_id": "9158",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11481",
      "task_id": "9158",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11482",
      "task_id": "9158",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8160",
  "name": "Q3 forecast review packet - draft 049.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9159",
    "item_id": "8160",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "11567",
      "task_id": "9159",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11568",
      "task_id": "9159",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11569",
      "task_id": "9159",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11570",
      "task_id": "9159",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11571",
      "task_id": "9159",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11572",
      "task_id": "9159",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11573",
      "task_id": "9159",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11574",
      "task_id": "9159",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11575",
      "task_id": "9159",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11576",
      "task_id": "9159",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11577",
      "task_id": "9159",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11578",
      "task_id": "9159",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8161",
  "name": "Q3 forecast review packet - draft 050.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9160",
    "item_id": "8161",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "11665",
      "task_id": "9160",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11666",
      "task_id": "9160",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11667",
      "task_id": "9160",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11668",
      "task_id": "9160",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11669",
      "task_id": "9160",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11670",
      "task_id": "9160",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11671",
      "task_id": "9160",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11672",
      "task_id": "9160",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11673",
      "task_id": "9160",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11674",
      "task_id": "9160",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11675",
      "task_id": "9160",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11676",
      "task_id": "9160",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8162",
  "name": "Q3 forecast review packet - draft 051.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9161",
    "item_id": "8162",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "11765",
      "task_id": "9161",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11766",
      "task_id": "9161",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11767",
      "task_id": "9161",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11768",
      "task_id": "9161",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11769",
      "task_id": "9161",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11770",
      "task_id": "9161",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11771",
      "task_id": "9161",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11772",
      "task_id": "9161",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11773",
      "task_id": "9161",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11774",
      "task_id": "9161",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11775",
      "task_id": "9161",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11776",
      "task_id": "9161",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8163",
  "name": "Q3 forecast review packet - draft 052.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9162",
    "item_id": "8163",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "11867",
      "task_id": "9162",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11868",
      "task_id": "9162",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11869",
      "task_id": "9162",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11870",
      "task_id": "9162",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11871",
      "task_id": "9162",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11872",
      "task_id": "9162",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11873",
      "task_id": "9162",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11874",
      "task_id": "9162",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11875",
      "task_id": "9162",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11876",
      "task_id": "9162",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11877",
      "task_id": "9162",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11878",
      "task_id": "9162",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8164",
  "name": "Q3 forecast review packet - draft 053.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9163",
    "item_id": "8164",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "11971",
      "task_id": "9163",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11972",
      "task_id": "9163",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11973",
      "task_id": "9163",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11974",
      "task_id": "9163",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11975",
      "task_id": "9163",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11976",
      "task_id": "9163",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11977",
      "task_id": "9163",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11978",
      "task_id": "9163",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11979",
      "task_id": "9163",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11980",
      "task_id": "9163",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11981",
      "task_id": "9163",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "11982",
      "task_id": "9163",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8165",
  "name": "Q3 forecast review packet - draft 054.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9164",
    "item_id": "8165",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "12077",
      "task_id": "9164",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12078",
      "task_id": "9164",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12079",
      "task_id": "9164",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12080",
      "task_id": "9164",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12081",
      "task_id": "9164",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12082",
      "task_id": "9164",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12083",
      "task_id": "9164",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12084",
      "task_id": "9164",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12085",
      "task_id": "9164",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12086",
      "task_id": "9164",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12087",
      "task_id": "9164",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12088",
      "task_id": "9164",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8166",
  "name": "Q3 forecast review packet - draft 055.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9165",
    "item_id": "8166",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "12185",
      "task_id": "9165",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12186",
      "task_id": "9165",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12187",
      "task_id": "9165",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12188",
      "task_id": "9165",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12189",
      "task_id": "9165",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12190",
      "task_id": "9165",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12191",
      "task_id": "9165",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12192",
      "task_id": "9165",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12193",
      "task_id": "9165",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12194",
      "task_id": "9165",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12195",
      "task_id": "9165",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12196",
      "task_id": "9165",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8167",
  "name": "Q3 forecast review packet - draft 056.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9166",
    "item_id": "8167",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "12295",
      "task_id": "9166",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12296",
      "task_id": "9166",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12297",
      "task_id": "9166",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12298",
      "task_id": "9166",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12299",
      "task_id": "9166",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12300",
      "task_id": "9166",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12301",
      "task_id": "9166",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12302",
      "task_id": "9166",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12303",
      "task_id": "9166",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12304",
      "task_id": "9166",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12305",
      "task_id": "9166",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12306",
      "task_id": "9166",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8168",
  "name": "Q3 forecast review packet - draft 057.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9167",
    "item_id": "8168",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "12407",
      "task_id": "9167",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12408",
      "task_id": "9167",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12409",
      "task_id": "9167",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12410",
      "task_id": "9167",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12411",
      "task_id": "9167",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12412",
      "task_id": "9167",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12413",
      "task_id": "9167",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12414",
      "task_id": "9167",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12415",
      "task_id": "9167",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12416",
      "task_id": "9167",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12417",
      "task_id": "9167",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12418",
      "task_id": "9167",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8169",
  "name": "Q3 forecast review packet - draft 058.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9168",
    "item_id": "8169",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "12521",
      "task_id": "9168",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12522",
      "task_id": "9168",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12523",
      "task_id": "9168",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12524",
      "task_id": "9168",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12525",
      "task_id": "9168",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12526",
      "task_id": "9168",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12527",
      "task_id": "9168",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12528",
      "task_id": "9168",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12529",
      "task_id": "9168",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12530",
      "task_id": "9168",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12531",
      "task_id": "9168",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12532",
      "task_id": "9168",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8170",
  "name": "Q3 forecast review packet - draft 059.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9169",
    "item_id": "8170",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "12637",
      "task_id": "9169",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12638",
      "task_id": "9169",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12639",
      "task_id": "9169",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12640",
      "task_id": "9169",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12641",
      "task_id": "9169",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12642",
      "task_id": "9169",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12643",
      "task_id": "9169",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12644",
      "task_id": "9169",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12645",
      "task_id": "9169",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12646",
      "task_id": "9169",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12647",
      "task_id": "9169",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12648",
      "task_id": "9169",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8171",
  "name": "Q3 forecast review packet - draft 060.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9170",
    "item_id": "8171",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "12755",
      "task_id": "9170",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12756",
      "task_id": "9170",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12757",
      "task_id": "9170",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12758",
      "task_id": "9170",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12759",
      "task_id": "9170",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12760",
      "task_id": "9170",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12761",
      "task_id": "9170",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12762",
      "task_id": "9170",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12763",
      "task_id": "9170",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12764",
      "task_id": "9170",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12765",
      "task_id": "9170",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12766",
      "task_id": "9170",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8172",
  "name": "Q3 forecast review packet - draft 061.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9171",
    "item_id": "8172",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "12875",
      "task_id": "9171",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12876",
      "task_id": "9171",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12877",
      "task_id": "9171",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12878",
      "task_id": "9171",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12879",
      "task_id": "9171",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12880",
      "task_id": "9171",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12881",
      "task_id": "9171",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12882",
      "task_id": "9171",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12883",
      "task_id": "9171",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12884",
      "task_id": "9171",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12885",
      "task_id": "9171",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12886",
      "task_id": "9171",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8173",
  "name": "Q3 forecast review packet - draft 062.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9172",
    "item_id": "8173",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "12997",
      "task_id": "9172",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12998",
      "task_id": "9172",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "12999",
      "task_id": "9172",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13000",
      "task_id": "9172",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13001",
      "task_id": "9172",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13002",
      "task_id": "9172",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13003",
      "task_id": "9172",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13004",
      "task_id": "9172",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13005",
      "task_id": "9172",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13006",
      "task_id": "9172",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13007",
      "task_id": "9172",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13008",
      "task_id": "9172",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8174",
  "name": "Q3 forecast review packet - draft 063.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9173",
    "item_id": "8174",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "13121",
      "task_id": "9173",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13122",
      "task_id": "9173",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13123",
      "task_id": "9173",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13124",
      "task_id": "9173",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13125",
      "task_id": "9173",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13126",
      "task_id": "9173",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13127",
      "task_id": "9173",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13128",
      "task_id": "9173",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13129",
      "task_id": "9173",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13130",
      "task_id": "9173",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13131",
      "task_id": "9173",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13132",
      "task_id": "9173",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8175",
  "name": "Q3 forecast review packet - draft 064.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9174",
    "item_id": "8175",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "13247",
      "task_id": "9174",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13248",
      "task_id": "9174",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13249",
      "task_id": "9174",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13250",
      "task_id": "9174",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13251",
      "task_id": "9174",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13252",
      "task_id": "9174",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13253",
      "task_id": "9174",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13254",
      "task_id": "9174",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13255",
      "task_id": "9174",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13256",
      "task_id": "9174",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13257",
      "task_id": "9174",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13258",
      "task_id": "9174",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8176",
  "name": "Q3 forecast review packet - draft 065.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9175",
    "item_id": "8176",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "13375",
      "task_id": "9175",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13376",
      "task_id": "9175",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13377",
      "task_id": "9175",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13378",
      "task_id": "9175",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13379",
      "task_id": "9175",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13380",
      "task_id": "9175",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13381",
      "task_id": "9175",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13382",
      "task_id": "9175",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13383",
      "task_id": "9175",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13384",
      "task_id": "9175",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13385",
      "task_id": "9175",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13386",
      "task_id": "9175",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8177",
  "name": "Q3 forecast review packet - draft 066.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9176",
    "item_id": "8177",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "13505",
      "task_id": "9176",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13506",
      "task_id": "9176",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13507",
      "task_id": "9176",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13508",
      "task_id": "9176",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13509",
      "task_id": "9176",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13510",
      "task_id": "9176",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13511",
      "task_id": "9176",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13512",
      "task_id": "9176",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13513",
      "task_id": "9176",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13514",
      "task_id": "9176",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13515",
      "task_id": "9176",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13516",
      "task_id": "9176",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8178",
  "name": "Q3 forecast review packet - draft 067.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9177",
    "item_id": "8178",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "13637",
      "task_id": "9177",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13638",
      "task_id": "9177",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13639",
      "task_id": "9177",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13640",
      "task_id": "9177",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13641",
      "task_id": "9177",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13642",
      "task_id": "9177",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13643",
      "task_id": "9177",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13644",
      "task_id": "9177",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13645",
      "task_id": "9177",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13646",
      "task_id": "9177",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13647",
      "task_id": "9177",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13648",
      "task_id": "9177",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8179",
  "name": "Q3 forecast review packet - draft 068.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9178",
    "item_id": "8179",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "13771",
      "task_id": "9178",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13772",
      "task_id": "9178",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13773",
      "task_id": "9178",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13774",
      "task_id": "9178",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13775",
      "task_id": "9178",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13776",
      "task_id": "9178",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13777",
      "task_id": "9178",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13778",
      "task_id": "9178",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13779",
      "task_id": "9178",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13780",
      "task_id": "9178",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13781",
      "task_id": "9178",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13782",
      "task_id": "9178",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8180",
  "name": "Q3 forecast review packet - draft 069.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9179",
    "item_id": "8180",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "13907",
      "task_id": "9179",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13908",
      "task_id": "9179",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13909",
      "task_id": "9179",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13910",
      "task_id": "9179",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13911",
      "task_id": "9179",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13912",
      "task_id": "9179",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13913",
      "task_id": "9179",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13914",
      "task_id": "9179",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13915",
      "task_id": "9179",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13916",
      "task_id": "9179",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13917",
      "task_id": "9179",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "13918",
      "task_id": "9179",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8181",
  "name": "Q3 forecast review packet - draft 070.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9180",
    "item_id": "8181",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "14045",
      "task_id": "9180",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14046",
      "task_id": "9180",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14047",
      "task_id": "9180",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14048",
      "task_id": "9180",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14049",
      "task_id": "9180",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14050",
      "task_id": "9180",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14051",
      "task_id": "9180",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14052",
      "task_id": "9180",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14053",
      "task_id": "9180",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14054",
      "task_id": "9180",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14055",
      "task_id": "9180",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14056",
      "task_id": "9180",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8182",
  "name": "Q3 forecast review packet - draft 071.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9181",
    "item_id": "8182",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "14185",
      "task_id": "9181",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14186",
      "task_id": "9181",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14187",
      "task_id": "9181",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14188",
      "task_id": "9181",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14189",
      "task_id": "9181",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14190",
      "task_id": "9181",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14191",
      "task_id": "9181",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14192",
      "task_id": "9181",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14193",
      "task_id": "9181",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14194",
      "task_id": "9181",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14195",
      "task_id": "9181",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14196",
      "task_id": "9181",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8183",
  "name": "Q3 forecast review packet - draft 072.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9182",
    "item_id": "8183",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "14327",
      "task_id": "9182",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14328",
      "task_id": "9182",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14329",
      "task_id": "9182",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14330",
      "task_id": "9182",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14331",
      "task_id": "9182",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14332",
      "task_id": "9182",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14333",
      "task_id": "9182",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14334",
      "task_id": "9182",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14335",
      "task_id": "9182",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14336",
      "task_id": "9182",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14337",
      "task_id": "9182",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14338",
      "task_id": "9182",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8184",
  "name": "Q3 forecast review packet - draft 073.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9183",
    "item_id": "8184",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "14471",
      "task_id": "9183",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14472",
      "task_id": "9183",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14473",
      "task_id": "9183",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14474",
      "task_id": "9183",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14475",
      "task_id": "9183",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14476",
      "task_id": "9183",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14477",
      "task_id": "9183",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14478",
      "task_id": "9183",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14479",
      "task_id": "9183",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14480",
      "task_id": "9183",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14481",
      "task_id": "9183",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14482",
      "task_id": "9183",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8185",
  "name": "Q3 forecast review packet - draft 074.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9184",
    "item_id": "8185",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "14617",
      "task_id": "9184",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14618",
      "task_id": "9184",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14619",
      "task_id": "9184",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14620",
      "task_id": "9184",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14621",
      "task_id": "9184",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14622",
      "task_id": "9184",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14623",
      "task_id": "9184",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14624",
      "task_id": "9184",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14625",
      "task_id": "9184",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14626",
      "task_id": "9184",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14627",
      "task_id": "9184",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14628",
      "task_id": "9184",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8186",
  "name": "Q3 forecast review packet - draft 075.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9185",
    "item_id": "8186",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "14765",
      "task_id": "9185",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14766",
      "task_id": "9185",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14767",
      "task_id": "9185",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14768",
      "task_id": "9185",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14769",
      "task_id": "9185",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14770",
      "task_id": "9185",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14771",
      "task_id": "9185",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14772",
      "task_id": "9185",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14773",
      "task_id": "9185",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14774",
      "task_id": "9185",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14775",
      "task_id": "9185",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14776",
      "task_id": "9185",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8187",
  "name": "Q3 forecast review packet - draft 076.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9186",
    "item_id": "8187",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "14915",
      "task_id": "9186",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14916",
      "task_id": "9186",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14917",
      "task_id": "9186",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14918",
      "task_id": "9186",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14919",
      "task_id": "9186",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14920",
      "task_id": "9186",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14921",
      "task_id": "9186",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14922",
      "task_id": "9186",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14923",
      "task_id": "9186",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14924",
      "task_id": "9186",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14925",
      "task_id": "9186",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "14926",
      "task_id": "9186",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8188",
  "name": "Q3 forecast review packet - draft 077.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9187",
    "item_id": "8188",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "15067",
      "task_id": "9187",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15068",
      "task_id": "9187",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15069",
      "task_id": "9187",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15070",
      "task_id": "9187",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15071",
      "task_id": "9187",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15072",
      "task_id": "9187",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15073",
      "task_id": "9187",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15074",
      "task_id": "9187",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15075",
      "task_id": "9187",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15076",
      "task_id": "9187",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15077",
      "task_id": "9187",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15078",
      "task_id": "9187",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8189",
  "name": "Q3 forecast review packet - draft 078.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9188",
    "item_id": "8189",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "15221",
      "task_id": "9188",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15222",
      "task_id": "9188",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15223",
      "task_id": "9188",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15224",
      "task_id": "9188",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15225",
      "task_id": "9188",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15226",
      "task_id": "9188",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15227",
      "task_id": "9188",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15228",
      "task_id": "9188",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15229",
      "task_id": "9188",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15230",
      "task_id": "9188",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15231",
      "task_id": "9188",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15232",
      "task_id": "9188",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8190",
  "name": "Q3 forecast review packet - draft 079.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9189",
    "item_id": "8190",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "15377",
      "task_id": "9189",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15378",
      "task_id": "9189",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15379",
      "task_id": "9189",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15380",
      "task_id": "9189",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15381",
      "task_id": "9189",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15382",
      "task_id": "9189",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15383",
      "task_id": "9189",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15384",
      "task_id": "9189",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15385",
      "task_id": "9189",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15386",
      "task_id": "9189",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15387",
      "task_id": "9189",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15388",
      "task_id": "9189",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8191",
  "name": "Q3 forecast review packet - draft 080.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9190",
    "item_id": "8191",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "15535",
      "task_id": "9190",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15536",
      "task_id": "9190",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15537",
      "task_id": "9190",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15538",
      "task_id": "9190",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15539",
      "task_id": "9190",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15540",
      "task_id": "9190",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15541",
      "task_id": "9190",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15542",
      "task_id": "9190",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15543",
      "task_id": "9190",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15544",
      "task_id": "9190",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15545",
      "task_id": "9190",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15546",
      "task_id": "9190",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8192",
  "name": "Q3 forecast review packet - draft 081.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9191",
    "item_id": "8192",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "15695",
      "task_id": "9191",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15696",
      "task_id": "9191",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15697",
      "task_id": "9191",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15698",
      "task_id": "9191",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15699",
      "task_id": "9191",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15700",
      "task_id": "9191",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15701",
      "task_id": "9191",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15702",
      "task_id": "9191",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15703",
      "task_id": "9191",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15704",
      "task_id": "9191",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15705",
      "task_id": "9191",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15706",
      "task_id": "9191",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8193",
  "name": "Q3 forecast review packet - draft 082.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9192",
    "item_id": "8193",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "15857",
      "task_id": "9192",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15858",
      "task_id": "9192",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15859",
      "task_id": "9192",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15860",
      "task_id": "9192",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15861",
      "task_id": "9192",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15862",
      "task_id": "9192",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15863",
      "task_id": "9192",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15864",
      "task_id": "9192",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15865",
      "task_id": "9192",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15866",
      "task_id": "9192",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15867",
      "task_id": "9192",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "15868",
      "task_id": "9192",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8194",
  "name": "Q3 forecast review packet - draft 083.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9193",
    "item_id": "8194",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "16021",
      "task_id": "9193",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16022",
      "task_id": "9193",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16023",
      "task_id": "9193",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16024",
      "task_id": "9193",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16025",
      "task_id": "9193",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16026",
      "task_id": "9193",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16027",
      "task_id": "9193",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16028",
      "task_id": "9193",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16029",
      "task_id": "9193",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16030",
      "task_id": "9193",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16031",
      "task_id": "9193",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16032",
      "task_id": "9193",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8195",
  "name": "Q3 forecast review packet - draft 084.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9194",
    "item_id": "8195",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "16187",
      "task_id": "9194",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16188",
      "task_id": "9194",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16189",
      "task_id": "9194",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16190",
      "task_id": "9194",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16191",
      "task_id": "9194",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16192",
      "task_id": "9194",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16193",
      "task_id": "9194",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16194",
      "task_id": "9194",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16195",
      "task_id": "9194",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16196",
      "task_id": "9194",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16197",
      "task_id": "9194",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16198",
      "task_id": "9194",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8196",
  "name": "Q3 forecast review packet - draft 085.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9195",
    "item_id": "8196",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "16355",
      "task_id": "9195",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16356",
      "task_id": "9195",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16357",
      "task_id": "9195",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16358",
      "task_id": "9195",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16359",
      "task_id": "9195",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16360",
      "task_id": "9195",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16361",
      "task_id": "9195",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16362",
      "task_id": "9195",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16363",
      "task_id": "9195",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16364",
      "task_id": "9195",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16365",
      "task_id": "9195",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16366",
      "task_id": "9195",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8197",
  "name": "Q3 forecast review packet - draft 086.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9196",
    "item_id": "8197",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "16525",
      "task_id": "9196",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16526",
      "task_id": "9196",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16527",
      "task_id": "9196",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16528",
      "task_id": "9196",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16529",
      "task_id": "9196",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16530",
      "task_id": "9196",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16531",
      "task_id": "9196",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16532",
      "task_id": "9196",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16533",
      "task_id": "9196",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16534",
      "task_id": "9196",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16535",
      "task_id": "9196",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16536",
      "task_id": "9196",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8198",
  "name": "Q3 forecast review packet - draft 087.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9197",
    "item_id": "8198",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "16697",
      "task_id": "9197",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16698",
      "task_id": "9197",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16699",
      "task_id": "9197",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16700",
      "task_id": "9197",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16701",
      "task_id": "9197",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16702",
      "task_id": "9197",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16703",
      "task_id": "9197",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16704",
      "task_id": "9197",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16705",
      "task_id": "9197",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16706",
      "task_id": "9197",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16707",
      "task_id": "9197",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16708",
      "task_id": "9197",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8199",
  "name": "Q3 forecast review packet - draft 088.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9198",
    "item_id": "8199",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "16871",
      "task_id": "9198",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16872",
      "task_id": "9198",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16873",
      "task_id": "9198",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16874",
      "task_id": "9198",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16875",
      "task_id": "9198",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16876",
      "task_id": "9198",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16877",
      "task_id": "9198",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16878",
      "task_id": "9198",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16879",
      "task_id": "9198",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16880",
      "task_id": "9198",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16881",
      "task_id": "9198",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "16882",
      "task_id": "9198",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8200",
  "name": "Q3 forecast review packet - draft 089.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9199",
    "item_id": "8200",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "17047",
      "task_id": "9199",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17048",
      "task_id": "9199",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17049",
      "task_id": "9199",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17050",
      "task_id": "9199",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17051",
      "task_id": "9199",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17052",
      "task_id": "9199",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17053",
      "task_id": "9199",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17054",
      "task_id": "9199",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17055",
      "task_id": "9199",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17056",
      "task_id": "9199",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17057",
      "task_id": "9199",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17058",
      "task_id": "9199",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8201",
  "name": "Q3 forecast review packet - draft 090.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9200",
    "item_id": "8201",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "17225",
      "task_id": "9200",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17226",
      "task_id": "9200",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17227",
      "task_id": "9200",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17228",
      "task_id": "9200",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17229",
      "task_id": "9200",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17230",
      "task_id": "9200",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17231",
      "task_id": "9200",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17232",
      "task_id": "9200",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17233",
      "task_id": "9200",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17234",
      "task_id": "9200",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17235",
      "task_id": "9200",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17236",
      "task_id": "9200",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8202",
  "name": "Q3 forecast review packet - draft 091.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9201",
    "item_id": "8202",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "17405",
      "task_id": "9201",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17406",
      "task_id": "9201",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17407",
      "task_id": "9201",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17408",
      "task_id": "9201",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17409",
      "task_id": "9201",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17410",
      "task_id": "9201",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17411",
      "task_id": "9201",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17412",
      "task_id": "9201",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17413",
      "task_id": "9201",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17414",
      "task_id": "9201",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17415",
      "task_id": "9201",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17416",
      "task_id": "9201",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8203",
  "name": "Q3 forecast review packet - draft 092.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "9202",
    "item_id": "8203",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "17587",
      "task_id": "9202",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17588",
      "task_id": "9202",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17589",
      "task_id": "9202",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17590",
      "task_id": "9202",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17591",
      "task_id": "9202",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17592",
      "task_id": "9202",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17593",
      "task_id": "9202",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17594",
      "task_id": "9202",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17595",
      "task_id": "9202",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17596",
      "task_id": "9202",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17597",
      "task_id": "9202",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17598",
      "task_id": "9202",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   },
   {
    "id": "17679",
    "item_id": "8203",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": []
   },
   {
    "id": "17864",
    "item_id": "8203",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": []
   },
   {
    "id": "18051",
    "item_id": "8203",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": []
   }
  ]
 },
 {
  "id": "8204",
  "name": "Q3 forecast review packet - draft 093.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "17680",
    "item_id": "8204",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "17771",
      "task_id": "17680",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17772",
      "task_id": "17680",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17773",
      "task_id": "17680",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17774",
      "task_id": "17680",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17775",
      "task_id": "17680",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17776",
      "task_id": "17680",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17777",
      "task_id": "17680",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17778",
      "task_id": "17680",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17779",
      "task_id": "17680",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17780",
      "task_id": "17680",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17781",
      "task_id": "17680",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17782",
      "task_id": "17680",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 },
 {
  "id": "8205",
  "name": "Q3 forecast review packet - draft 094.pdf",
  "parent_id": "8100",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Budget Reviews",
  "box_folders": [
   {
    "id": "8100",
    "name": "Budget Reviews",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-06-01T09:00:00+00:00",
    "modified_at": "2026-06-01T09:00:00+00:00"
   }
  ],
  "box_tasks": [
   {
    "id": "17865",
    "item_id": "8205",
    "item_type": "file",
    "message": "Please review the Q3 budget figures",
    "action": "review",
    "is_completed": false,
    "completion_rule": "all_assignees",
    "created_by_id": "30000000006",
    "created_at": "2026-06-01T09:00:00+00:00",
    "box_task_assignments": [
     {
      "id": "17957",
      "task_id": "17865",
      "item_id": "8102",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17958",
      "task_id": "17865",
      "item_id": "8112",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17959",
      "task_id": "17865",
      "item_id": "8113",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17960",
      "task_id": "17865",
      "item_id": "8114",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17961",
      "task_id": "17865",
      "item_id": "8115",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17962",
      "task_id": "17865",
      "item_id": "8116",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17963",
      "task_id": "17865",
      "item_id": "8117",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17964",
      "task_id": "17865",
      "item_id": "8118",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17965",
      "task_id": "17865",
      "item_id": "8119",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17966",
      "task_id": "17865",
      "item_id": "8120",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17967",
      "task_id": "17865",
      "item_id": "8121",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     },
     {
      "id": "17968",
      "task_id": "17865",
      "item_id": "8122",
      "item_type": "file",
      "assigned_to_id": "30000000002",
      "assigned_by_id": "30000000004",
      "resolution_state": "completed",
      "assigned_at": "2026-06-01T09:00:00+00:00"
     }
    ]
   }
  ]
 }
]
