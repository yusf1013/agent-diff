You check test cases for an AI assistant that acts in a workspace on a user's behalf. You read carefully
and literally, the way the user who wrote the request would mean it.

---

A user sent the assistant this request in their Box workspace:

    "Add the tag needs-follow-up to all the files in the Vendor Contracts folder that Dana Whitfield owns, that were uploaded before June 15, and that have a comment from Priya Nair posted on June 20."

The user is Jordan Lee. Below is every Box file in the workspace, with what the assistant can see about it. Which of
them does the user's request ask the assistant to act on?

List the id of every record the request covers, and only those. Read each condition of the request as the user
would mean it. If you cannot tell whether the user means a record, list it under `unsure` with the reason (and do
not list it in `ids`). Answer with JSON: {"ids": [...], "unsure": [{"id", "why"}], "notes": "..."}.

Records:
[
 {
  "id": "9101",
  "name": "Master Services Agreement.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-10T09:00:00+00:00",
  "modified_at": "2026-06-12T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91011",
    "file_id": "9101",
    "item_id": "9101",
    "item_type": "file",
    "message": "Let's revisit the payment terms before renewal.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9102",
  "name": "Vendor Services Agreement.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91021",
    "file_id": "9102",
    "item_id": "9102",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9103",
  "name": "Renewal Services Agreement.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-16T09:00:00+00:00",
  "modified_at": "2026-06-18T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91031",
    "file_id": "9103",
    "item_id": "9103",
    "item_type": "file",
    "message": "Let's finalize the SOW addendum.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9104",
  "name": "Support Services Agreement.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-10T09:00:00+00:00",
  "modified_at": "2026-06-11T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91041",
    "file_id": "9104",
    "item_id": "9104",
    "item_type": "file",
    "message": "Please loop in procurement on this.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-19T10:00:00+00:00",
    "modified_at": "2026-06-19T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9105",
  "name": "Maintenance Services Agreement.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-10T09:00:00+00:00",
  "modified_at": "2026-06-11T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91051",
    "file_id": "9105",
    "item_id": "9105",
    "item_type": "file",
    "message": "Following up after the site visit.",
    "created_by_id": "30000000006",
    "created_at": "2026-07-05T10:00:00+00:00",
    "modified_at": "2026-07-05T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9107",
  "name": "Employee Handbook.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000008 (Sam Rivera)",
  "created_by_id": "30000000008 (Sam Rivera)",
  "modified_by_id": "30000000008 (Sam Rivera)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-10T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Sam Rivera",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000008",
    "name": "Sam Rivera",
    "login": "sam.rivera@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": []
 },
 {
  "id": "9108",
  "name": "Campaign Brief.pdf",
  "parent_id": "9002",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-05-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Marketing Assets",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9002",
    "name": "Marketing Assets",
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
  "box_comments": []
 },
 {
  "id": "9109",
  "name": "Professional Services Agreement.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-10T09:00:00+00:00",
  "modified_at": "2026-06-12T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91052",
    "file_id": "9109",
    "item_id": "9109",
    "item_type": "file",
    "message": "Let's revisit the payment terms before renewal.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9110",
  "name": "Vendor Services Agreement.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-10T09:00:00+00:00",
  "modified_at": "2026-06-12T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91053",
    "file_id": "9110",
    "item_id": "9110",
    "item_type": "file",
    "message": "Let's revisit the payment terms before renewal.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9111",
  "name": "Vendor Services Agreement - draft 001.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91054",
    "file_id": "9111",
    "item_id": "9111",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9112",
  "name": "Vendor Services Agreement - draft 002.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91055",
    "file_id": "9112",
    "item_id": "9112",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9113",
  "name": "Vendor Services Agreement - draft 003.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91056",
    "file_id": "9113",
    "item_id": "9113",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9114",
  "name": "Vendor Services Agreement - draft 004.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91057",
    "file_id": "9114",
    "item_id": "9114",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9115",
  "name": "Vendor Services Agreement - draft 005.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91058",
    "file_id": "9115",
    "item_id": "9115",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9116",
  "name": "Vendor Services Agreement - draft 006.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91059",
    "file_id": "9116",
    "item_id": "9116",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9117",
  "name": "Vendor Services Agreement - draft 007.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91060",
    "file_id": "9117",
    "item_id": "9117",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9118",
  "name": "Vendor Services Agreement - draft 008.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91061",
    "file_id": "9118",
    "item_id": "9118",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9119",
  "name": "Vendor Services Agreement - draft 009.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91062",
    "file_id": "9119",
    "item_id": "9119",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9120",
  "name": "Vendor Services Agreement - draft 010.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91063",
    "file_id": "9120",
    "item_id": "9120",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9121",
  "name": "Vendor Services Agreement - draft 011.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91064",
    "file_id": "9121",
    "item_id": "9121",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9122",
  "name": "Vendor Services Agreement - draft 012.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91065",
    "file_id": "9122",
    "item_id": "9122",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9123",
  "name": "Vendor Services Agreement - draft 013.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91066",
    "file_id": "9123",
    "item_id": "9123",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9124",
  "name": "Vendor Services Agreement - draft 014.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91067",
    "file_id": "9124",
    "item_id": "9124",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9125",
  "name": "Vendor Services Agreement - draft 015.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91068",
    "file_id": "9125",
    "item_id": "9125",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9126",
  "name": "Vendor Services Agreement - draft 016.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91069",
    "file_id": "9126",
    "item_id": "9126",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9127",
  "name": "Vendor Services Agreement - draft 017.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91070",
    "file_id": "9127",
    "item_id": "9127",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9128",
  "name": "Vendor Services Agreement - draft 018.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91071",
    "file_id": "9128",
    "item_id": "9128",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9129",
  "name": "Vendor Services Agreement - draft 019.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91072",
    "file_id": "9129",
    "item_id": "9129",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9130",
  "name": "Vendor Services Agreement - draft 020.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91073",
    "file_id": "9130",
    "item_id": "9130",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9131",
  "name": "Vendor Services Agreement - draft 021.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91074",
    "file_id": "9131",
    "item_id": "9131",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9132",
  "name": "Vendor Services Agreement - draft 022.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91075",
    "file_id": "9132",
    "item_id": "9132",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9133",
  "name": "Vendor Services Agreement - draft 023.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91076",
    "file_id": "9133",
    "item_id": "9133",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9134",
  "name": "Vendor Services Agreement - draft 024.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91077",
    "file_id": "9134",
    "item_id": "9134",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9135",
  "name": "Vendor Services Agreement - draft 025.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91078",
    "file_id": "9135",
    "item_id": "9135",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9136",
  "name": "Vendor Services Agreement - draft 026.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91079",
    "file_id": "9136",
    "item_id": "9136",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9137",
  "name": "Vendor Services Agreement - draft 027.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91080",
    "file_id": "9137",
    "item_id": "9137",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9138",
  "name": "Vendor Services Agreement - draft 028.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91081",
    "file_id": "9138",
    "item_id": "9138",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9139",
  "name": "Vendor Services Agreement - draft 029.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91082",
    "file_id": "9139",
    "item_id": "9139",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9140",
  "name": "Vendor Services Agreement - draft 030.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91083",
    "file_id": "9140",
    "item_id": "9140",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9141",
  "name": "Vendor Services Agreement - draft 031.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91084",
    "file_id": "9141",
    "item_id": "9141",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9142",
  "name": "Vendor Services Agreement - draft 032.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91085",
    "file_id": "9142",
    "item_id": "9142",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9143",
  "name": "Vendor Services Agreement - draft 033.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91086",
    "file_id": "9143",
    "item_id": "9143",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9144",
  "name": "Vendor Services Agreement - draft 034.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91087",
    "file_id": "9144",
    "item_id": "9144",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9145",
  "name": "Vendor Services Agreement - draft 035.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91088",
    "file_id": "9145",
    "item_id": "9145",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9146",
  "name": "Vendor Services Agreement - draft 036.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91089",
    "file_id": "9146",
    "item_id": "9146",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9147",
  "name": "Vendor Services Agreement - draft 037.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91090",
    "file_id": "9147",
    "item_id": "9147",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9148",
  "name": "Vendor Services Agreement - draft 038.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91091",
    "file_id": "9148",
    "item_id": "9148",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9149",
  "name": "Vendor Services Agreement - draft 039.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91092",
    "file_id": "9149",
    "item_id": "9149",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9150",
  "name": "Vendor Services Agreement - draft 040.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91093",
    "file_id": "9150",
    "item_id": "9150",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9151",
  "name": "Vendor Services Agreement - draft 041.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91094",
    "file_id": "9151",
    "item_id": "9151",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9152",
  "name": "Vendor Services Agreement - draft 042.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91095",
    "file_id": "9152",
    "item_id": "9152",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9153",
  "name": "Vendor Services Agreement - draft 043.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91096",
    "file_id": "9153",
    "item_id": "9153",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9154",
  "name": "Vendor Services Agreement - draft 044.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91097",
    "file_id": "9154",
    "item_id": "9154",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9155",
  "name": "Vendor Services Agreement - draft 045.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91098",
    "file_id": "9155",
    "item_id": "9155",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9156",
  "name": "Vendor Services Agreement - draft 046.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91099",
    "file_id": "9156",
    "item_id": "9156",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9157",
  "name": "Vendor Services Agreement - draft 047.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91100",
    "file_id": "9157",
    "item_id": "9157",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9158",
  "name": "Vendor Services Agreement - draft 048.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91101",
    "file_id": "9158",
    "item_id": "9158",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9159",
  "name": "Vendor Services Agreement - draft 049.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91102",
    "file_id": "9159",
    "item_id": "9159",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9160",
  "name": "Vendor Services Agreement - draft 050.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91103",
    "file_id": "9160",
    "item_id": "9160",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9161",
  "name": "Vendor Services Agreement - draft 051.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91104",
    "file_id": "9161",
    "item_id": "9161",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9162",
  "name": "Vendor Services Agreement - draft 052.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91105",
    "file_id": "9162",
    "item_id": "9162",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9163",
  "name": "Vendor Services Agreement - draft 053.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91106",
    "file_id": "9163",
    "item_id": "9163",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9164",
  "name": "Vendor Services Agreement - draft 054.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91107",
    "file_id": "9164",
    "item_id": "9164",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9165",
  "name": "Vendor Services Agreement - draft 055.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91108",
    "file_id": "9165",
    "item_id": "9165",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9166",
  "name": "Vendor Services Agreement - draft 056.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91109",
    "file_id": "9166",
    "item_id": "9166",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9167",
  "name": "Vendor Services Agreement - draft 057.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91110",
    "file_id": "9167",
    "item_id": "9167",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9168",
  "name": "Vendor Services Agreement - draft 058.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91111",
    "file_id": "9168",
    "item_id": "9168",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9169",
  "name": "Vendor Services Agreement - draft 059.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91112",
    "file_id": "9169",
    "item_id": "9169",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9170",
  "name": "Vendor Services Agreement - draft 060.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91113",
    "file_id": "9170",
    "item_id": "9170",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9171",
  "name": "Vendor Services Agreement - draft 061.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91114",
    "file_id": "9171",
    "item_id": "9171",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9172",
  "name": "Vendor Services Agreement - draft 062.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91115",
    "file_id": "9172",
    "item_id": "9172",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9173",
  "name": "Vendor Services Agreement - draft 063.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91116",
    "file_id": "9173",
    "item_id": "9173",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9174",
  "name": "Vendor Services Agreement - draft 064.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91117",
    "file_id": "9174",
    "item_id": "9174",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9175",
  "name": "Vendor Services Agreement - draft 065.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91118",
    "file_id": "9175",
    "item_id": "9175",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9176",
  "name": "Vendor Services Agreement - draft 066.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91119",
    "file_id": "9176",
    "item_id": "9176",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9177",
  "name": "Vendor Services Agreement - draft 067.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91120",
    "file_id": "9177",
    "item_id": "9177",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9178",
  "name": "Vendor Services Agreement - draft 068.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91121",
    "file_id": "9178",
    "item_id": "9178",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9179",
  "name": "Vendor Services Agreement - draft 069.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91122",
    "file_id": "9179",
    "item_id": "9179",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9180",
  "name": "Vendor Services Agreement - draft 070.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91123",
    "file_id": "9180",
    "item_id": "9180",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9181",
  "name": "Vendor Services Agreement - draft 071.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91124",
    "file_id": "9181",
    "item_id": "9181",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9182",
  "name": "Vendor Services Agreement - draft 072.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91125",
    "file_id": "9182",
    "item_id": "9182",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9183",
  "name": "Vendor Services Agreement - draft 073.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91126",
    "file_id": "9183",
    "item_id": "9183",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9184",
  "name": "Vendor Services Agreement - draft 074.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91127",
    "file_id": "9184",
    "item_id": "9184",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9185",
  "name": "Vendor Services Agreement - draft 075.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91128",
    "file_id": "9185",
    "item_id": "9185",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9186",
  "name": "Vendor Services Agreement - draft 076.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91129",
    "file_id": "9186",
    "item_id": "9186",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9187",
  "name": "Vendor Services Agreement - draft 077.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91130",
    "file_id": "9187",
    "item_id": "9187",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9188",
  "name": "Vendor Services Agreement - draft 078.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91131",
    "file_id": "9188",
    "item_id": "9188",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9189",
  "name": "Vendor Services Agreement - draft 079.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91132",
    "file_id": "9189",
    "item_id": "9189",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9190",
  "name": "Vendor Services Agreement - draft 080.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91133",
    "file_id": "9190",
    "item_id": "9190",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9191",
  "name": "Vendor Services Agreement - draft 081.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91134",
    "file_id": "9191",
    "item_id": "9191",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9192",
  "name": "Vendor Services Agreement - draft 082.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91135",
    "file_id": "9192",
    "item_id": "9192",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9193",
  "name": "Vendor Services Agreement - draft 083.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91136",
    "file_id": "9193",
    "item_id": "9193",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9194",
  "name": "Vendor Services Agreement - draft 084.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91137",
    "file_id": "9194",
    "item_id": "9194",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9195",
  "name": "Vendor Services Agreement - draft 085.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91138",
    "file_id": "9195",
    "item_id": "9195",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9196",
  "name": "Vendor Services Agreement - draft 086.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91139",
    "file_id": "9196",
    "item_id": "9196",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9197",
  "name": "Vendor Services Agreement - draft 087.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91140",
    "file_id": "9197",
    "item_id": "9197",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9198",
  "name": "Vendor Services Agreement - draft 088.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91141",
    "file_id": "9198",
    "item_id": "9198",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9199",
  "name": "Vendor Services Agreement - draft 089.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91142",
    "file_id": "9199",
    "item_id": "9199",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9200",
  "name": "Vendor Services Agreement - draft 090.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91143",
    "file_id": "9200",
    "item_id": "9200",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9201",
  "name": "Vendor Services Agreement - draft 091.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91144",
    "file_id": "9201",
    "item_id": "9201",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9202",
  "name": "Vendor Services Agreement - draft 092.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91145",
    "file_id": "9202",
    "item_id": "9202",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9203",
  "name": "Vendor Services Agreement - draft 093.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91146",
    "file_id": "9203",
    "item_id": "9203",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9204",
  "name": "Vendor Services Agreement - draft 094.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91147",
    "file_id": "9204",
    "item_id": "9204",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 },
 {
  "id": "9205",
  "name": "Vendor Services Agreement - draft 095.pdf",
  "parent_id": "9000",
  "owned_by_id": "30000000005 (Dana Whitfield)",
  "created_by_id": "30000000005 (Dana Whitfield)",
  "modified_by_id": "30000000005 (Dana Whitfield)",
  "size": 48213,
  "extension": "pdf",
  "comment_count": 1,
  "tags": "[]",
  "created_at": "2026-06-20T09:00:00+00:00",
  "modified_at": "2026-06-10T09:00:00+00:00",
  "uploader_display_name": "Dana Whitfield",
  "folder path": "All Files / Vendor Contracts",
  "box_users": [
   {
    "id": "30000000005",
    "name": "Dana Whitfield",
    "login": "dana.whitfield@northwind.example",
    "status": "active",
    "role": "user",
    "created_at": "2025-01-10T00:00:00Z",
    "modified_at": "2025-01-10T00:00:00Z"
   }
  ],
  "box_folders": [
   {
    "id": "9000",
    "name": "Vendor Contracts",
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
  "box_comments": [
   {
    "id": "91148",
    "file_id": "9205",
    "item_id": "9205",
    "item_type": "file",
    "message": "Can we confirm the updated pricing?",
    "created_by_id": "30000000006",
    "created_at": "2026-06-20T10:00:00+00:00",
    "modified_at": "2026-06-20T10:00:00+00:00",
    "is_reply_comment": false,
    "box_users": [
     {
      "id": "30000000006",
      "name": "Priya Nair",
      "login": "priya.nair@northwind.example",
      "status": "active",
      "role": "user",
      "created_at": "2025-01-10T00:00:00Z",
      "modified_at": "2025-01-10T00:00:00Z"
     }
    ]
   }
  ]
 }
]
