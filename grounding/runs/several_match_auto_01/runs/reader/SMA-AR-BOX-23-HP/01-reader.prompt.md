You check test cases for an AI assistant that acts in a workspace on a user's behalf. You read carefully
and literally, the way the user who wrote the request would mean it.

---

A user sent the assistant this request in their Box workspace:

    "Add the tag design-review to all the PDFs in the Product Specs folder whose descriptions mention the mobile redesign, are under 2 MB, and have exactly 3 comments on them, not counting replies."

The user is Jordan Lee. Below is every Box file in the workspace, with what the assistant can see about it. Which of
them does the user's request ask the assistant to act on?

List the id of every record the request covers, and only those. Read each condition of the request as the user
would mean it. If you cannot tell whether the user means a record, list it under `unsure` with the reason (and do
not list it in `ids`). Answer with JSON: {"ids": [...], "unsure": [{"id", "why"}], "notes": "..."}.

Records:
[
 {
  "id": "8210",
  "name": "Mobile Nav Redesign Spec.pdf",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design spec for the mobile redesign of the navigation menu.",
  "size": 1800000,
  "extension": "pdf",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82101",
    "file_id": "8210",
    "item_id": "8210",
    "item_type": "file",
    "message": "Looks good, ready for dev.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82102",
    "file_id": "8210",
    "item_id": "8210",
    "item_type": "file",
    "message": "Can we add a fallback state?",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82103",
    "file_id": "8210",
    "item_id": "8210",
    "item_type": "file",
    "message": "Approved by design.",
    "created_by_id": "30000000008",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8211",
  "name": "Mobile Redesign Specs.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82111",
    "file_id": "8211",
    "item_id": "8211",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82112",
    "file_id": "8211",
    "item_id": "8211",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82113",
    "file_id": "8211",
    "item_id": "8211",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8212",
  "name": "Navigation Update Overview.pdf",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Summary of Q4 roadmap priorities for the platform team.",
  "size": 1800000,
  "extension": "pdf",
  "comment_count": 3,
  "tags": "[\"mobile-redesign\"]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82121",
    "file_id": "8212",
    "item_id": "8212",
    "item_type": "file",
    "message": "Priorities make sense.",
    "created_by_id": "30000000008",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82122",
    "file_id": "8212",
    "item_id": "8212",
    "item_type": "file",
    "message": "Move item 3 up.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82123",
    "file_id": "8212",
    "item_id": "8212",
    "item_type": "file",
    "message": "Updated the order.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8213",
  "name": "Mobile Redesign Spec v2.pdf",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design spec for the mobile redesign of the navigation menu, revised.",
  "size": 2100000,
  "extension": "pdf",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82131",
    "file_id": "8213",
    "item_id": "8213",
    "item_type": "file",
    "message": "Revision looks complete.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82132",
    "file_id": "8213",
    "item_id": "8213",
    "item_type": "file",
    "message": "One typo on page 2.",
    "created_by_id": "30000000008",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82133",
    "file_id": "8213",
    "item_id": "8213",
    "item_type": "file",
    "message": "Fixed, thanks.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8214",
  "name": "Mobile Redesign Spec Addendum.pdf",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design spec addendum for the mobile redesign of the navigation menu.",
  "size": 1800000,
  "extension": "pdf",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82141",
    "file_id": "8214",
    "item_id": "8214",
    "item_type": "file",
    "message": "Addendum reviewed.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82142",
    "file_id": "8214",
    "item_id": "8214",
    "item_type": "file",
    "message": "One more section needed.",
    "created_by_id": "30000000008",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82143",
    "file_id": "8214",
    "item_id": "82141",
    "item_type": "comment",
    "message": "Added the missing section.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": true
   }
  ]
 },
 {
  "id": "8215",
  "name": "Brand Guidelines.docx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Brand guidelines for external communications.",
  "size": 1200000,
  "extension": "docx",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
  "id": "8217",
  "name": "Payment Redesign Spec.pdf",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design spec for the payment redesign flow.",
  "size": 3000000,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
  "id": "8220",
  "name": "Campaign Brief.pdf",
  "parent_id": "8201",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Q4 marketing campaign brief and budget notes.",
  "size": 900000,
  "extension": "pdf",
  "comment_count": 0,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Marketing Assets",
  "box_folders": [
   {
    "id": "8201",
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
  "id": "8221",
  "name": "Mobile Menu Redesign Draft.pdf",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design spec for the mobile redesign of the navigation menu.",
  "size": 1800000,
  "extension": "pdf",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82144",
    "file_id": "8221",
    "item_id": "8221",
    "item_type": "file",
    "message": "Looks good, ready for dev.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82145",
    "file_id": "8221",
    "item_id": "8221",
    "item_type": "file",
    "message": "Can we add a fallback state?",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82146",
    "file_id": "8221",
    "item_id": "8221",
    "item_type": "file",
    "message": "Approved by design.",
    "created_by_id": "30000000008",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8222",
  "name": "Mobile Redesign Specs 01.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82147",
    "file_id": "8222",
    "item_id": "8222",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82148",
    "file_id": "8222",
    "item_id": "8222",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82149",
    "file_id": "8222",
    "item_id": "8222",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8223",
  "name": "Mobile Redesign Specs 02.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82150",
    "file_id": "8223",
    "item_id": "8223",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82151",
    "file_id": "8223",
    "item_id": "8223",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82152",
    "file_id": "8223",
    "item_id": "8223",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8224",
  "name": "Mobile Redesign Specs 03.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82153",
    "file_id": "8224",
    "item_id": "8224",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82154",
    "file_id": "8224",
    "item_id": "8224",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82155",
    "file_id": "8224",
    "item_id": "8224",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8225",
  "name": "Mobile Redesign Specs 04.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82156",
    "file_id": "8225",
    "item_id": "8225",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82157",
    "file_id": "8225",
    "item_id": "8225",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82158",
    "file_id": "8225",
    "item_id": "8225",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8226",
  "name": "Mobile Redesign Specs 05.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82159",
    "file_id": "8226",
    "item_id": "8226",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82160",
    "file_id": "8226",
    "item_id": "8226",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82161",
    "file_id": "8226",
    "item_id": "8226",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8227",
  "name": "Mobile Redesign Specs 06.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82162",
    "file_id": "8227",
    "item_id": "8227",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82163",
    "file_id": "8227",
    "item_id": "8227",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82164",
    "file_id": "8227",
    "item_id": "8227",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8228",
  "name": "Mobile Redesign Specs 07.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82165",
    "file_id": "8228",
    "item_id": "8228",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82166",
    "file_id": "8228",
    "item_id": "8228",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82167",
    "file_id": "8228",
    "item_id": "8228",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8229",
  "name": "Mobile Redesign Specs 08.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82168",
    "file_id": "8229",
    "item_id": "8229",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82169",
    "file_id": "8229",
    "item_id": "8229",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82170",
    "file_id": "8229",
    "item_id": "8229",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8230",
  "name": "Mobile Redesign Specs 09.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82171",
    "file_id": "8230",
    "item_id": "8230",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82172",
    "file_id": "8230",
    "item_id": "8230",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82173",
    "file_id": "8230",
    "item_id": "8230",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8231",
  "name": "Mobile Redesign Specs 10.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82174",
    "file_id": "8231",
    "item_id": "8231",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82175",
    "file_id": "8231",
    "item_id": "8231",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82176",
    "file_id": "8231",
    "item_id": "8231",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8232",
  "name": "Mobile Redesign Specs 11.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82177",
    "file_id": "8232",
    "item_id": "8232",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82178",
    "file_id": "8232",
    "item_id": "8232",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82179",
    "file_id": "8232",
    "item_id": "8232",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8233",
  "name": "Mobile Redesign Specs 12.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82180",
    "file_id": "8233",
    "item_id": "8233",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82181",
    "file_id": "8233",
    "item_id": "8233",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82182",
    "file_id": "8233",
    "item_id": "8233",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8234",
  "name": "Mobile Redesign Specs 13.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82183",
    "file_id": "8234",
    "item_id": "8234",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82184",
    "file_id": "8234",
    "item_id": "8234",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82185",
    "file_id": "8234",
    "item_id": "8234",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8235",
  "name": "Mobile Redesign Specs 14.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82186",
    "file_id": "8235",
    "item_id": "8235",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82187",
    "file_id": "8235",
    "item_id": "8235",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82188",
    "file_id": "8235",
    "item_id": "8235",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8236",
  "name": "Mobile Redesign Specs 15.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82189",
    "file_id": "8236",
    "item_id": "8236",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82190",
    "file_id": "8236",
    "item_id": "8236",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82191",
    "file_id": "8236",
    "item_id": "8236",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8237",
  "name": "Mobile Redesign Specs 16.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82192",
    "file_id": "8237",
    "item_id": "8237",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82193",
    "file_id": "8237",
    "item_id": "8237",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82194",
    "file_id": "8237",
    "item_id": "8237",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8238",
  "name": "Mobile Redesign Specs 17.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82195",
    "file_id": "8238",
    "item_id": "8238",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82196",
    "file_id": "8238",
    "item_id": "8238",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82197",
    "file_id": "8238",
    "item_id": "8238",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8239",
  "name": "Mobile Redesign Specs 18.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82198",
    "file_id": "8239",
    "item_id": "8239",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82199",
    "file_id": "8239",
    "item_id": "8239",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82200",
    "file_id": "8239",
    "item_id": "8239",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8240",
  "name": "Mobile Redesign Specs 19.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82201",
    "file_id": "8240",
    "item_id": "8240",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82202",
    "file_id": "8240",
    "item_id": "8240",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82203",
    "file_id": "8240",
    "item_id": "8240",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8241",
  "name": "Mobile Redesign Specs 20.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82204",
    "file_id": "8241",
    "item_id": "8241",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82205",
    "file_id": "8241",
    "item_id": "8241",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82206",
    "file_id": "8241",
    "item_id": "8241",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8242",
  "name": "Mobile Redesign Specs 21.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82207",
    "file_id": "8242",
    "item_id": "8242",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82208",
    "file_id": "8242",
    "item_id": "8242",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82209",
    "file_id": "8242",
    "item_id": "8242",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8243",
  "name": "Mobile Redesign Specs 22.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82210",
    "file_id": "8243",
    "item_id": "8243",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82211",
    "file_id": "8243",
    "item_id": "8243",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82212",
    "file_id": "8243",
    "item_id": "8243",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8244",
  "name": "Mobile Redesign Specs 23.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82213",
    "file_id": "8244",
    "item_id": "8244",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82214",
    "file_id": "8244",
    "item_id": "8244",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82215",
    "file_id": "8244",
    "item_id": "8244",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8245",
  "name": "Mobile Redesign Specs 24.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82216",
    "file_id": "8245",
    "item_id": "8245",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82217",
    "file_id": "8245",
    "item_id": "8245",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82218",
    "file_id": "8245",
    "item_id": "8245",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8246",
  "name": "Mobile Redesign Specs 25.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82219",
    "file_id": "8246",
    "item_id": "8246",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82220",
    "file_id": "8246",
    "item_id": "8246",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82221",
    "file_id": "8246",
    "item_id": "8246",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8247",
  "name": "Mobile Redesign Specs 26.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82222",
    "file_id": "8247",
    "item_id": "8247",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82223",
    "file_id": "8247",
    "item_id": "8247",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82224",
    "file_id": "8247",
    "item_id": "8247",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8248",
  "name": "Mobile Redesign Specs 27.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82225",
    "file_id": "8248",
    "item_id": "8248",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82226",
    "file_id": "8248",
    "item_id": "8248",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82227",
    "file_id": "8248",
    "item_id": "8248",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8249",
  "name": "Mobile Redesign Specs 28.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82228",
    "file_id": "8249",
    "item_id": "8249",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82229",
    "file_id": "8249",
    "item_id": "8249",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82230",
    "file_id": "8249",
    "item_id": "8249",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8250",
  "name": "Mobile Redesign Specs 29.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82231",
    "file_id": "8250",
    "item_id": "8250",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82232",
    "file_id": "8250",
    "item_id": "8250",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82233",
    "file_id": "8250",
    "item_id": "8250",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8251",
  "name": "Mobile Redesign Specs 30.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82234",
    "file_id": "8251",
    "item_id": "8251",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82235",
    "file_id": "8251",
    "item_id": "8251",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82236",
    "file_id": "8251",
    "item_id": "8251",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8252",
  "name": "Mobile Redesign Specs 31.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82237",
    "file_id": "8252",
    "item_id": "8252",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82238",
    "file_id": "8252",
    "item_id": "8252",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82239",
    "file_id": "8252",
    "item_id": "8252",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8253",
  "name": "Mobile Redesign Specs 32.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82240",
    "file_id": "8253",
    "item_id": "8253",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82241",
    "file_id": "8253",
    "item_id": "8253",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82242",
    "file_id": "8253",
    "item_id": "8253",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8254",
  "name": "Mobile Flow Redesign Notes.pdf",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design spec for the mobile redesign of the navigation menu.",
  "size": 1800000,
  "extension": "pdf",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82243",
    "file_id": "8254",
    "item_id": "8254",
    "item_type": "file",
    "message": "Looks good, ready for dev.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82244",
    "file_id": "8254",
    "item_id": "8254",
    "item_type": "file",
    "message": "Can we add a fallback state?",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82245",
    "file_id": "8254",
    "item_id": "8254",
    "item_type": "file",
    "message": "Approved by design.",
    "created_by_id": "30000000008",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8255",
  "name": "Mobile UX Redesign Spec.pdf",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design spec for the mobile redesign of the navigation menu.",
  "size": 1800000,
  "extension": "pdf",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82246",
    "file_id": "8255",
    "item_id": "8255",
    "item_type": "file",
    "message": "Looks good, ready for dev.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82247",
    "file_id": "8255",
    "item_id": "8255",
    "item_type": "file",
    "message": "Can we add a fallback state?",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82248",
    "file_id": "8255",
    "item_id": "8255",
    "item_type": "file",
    "message": "Approved by design.",
    "created_by_id": "30000000008",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8256",
  "name": "Mobile UX Redesign Spec - draft 001.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82249",
    "file_id": "8256",
    "item_id": "8256",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82250",
    "file_id": "8256",
    "item_id": "8256",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82251",
    "file_id": "8256",
    "item_id": "8256",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8257",
  "name": "Mobile UX Redesign Spec - draft 002.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82252",
    "file_id": "8257",
    "item_id": "8257",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82253",
    "file_id": "8257",
    "item_id": "8257",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82254",
    "file_id": "8257",
    "item_id": "8257",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8258",
  "name": "Mobile UX Redesign Spec - draft 003.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82255",
    "file_id": "8258",
    "item_id": "8258",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82256",
    "file_id": "8258",
    "item_id": "8258",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82257",
    "file_id": "8258",
    "item_id": "8258",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8259",
  "name": "Mobile UX Redesign Spec - draft 004.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82258",
    "file_id": "8259",
    "item_id": "8259",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82259",
    "file_id": "8259",
    "item_id": "8259",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82260",
    "file_id": "8259",
    "item_id": "8259",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8260",
  "name": "Mobile UX Redesign Spec - draft 005.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82261",
    "file_id": "8260",
    "item_id": "8260",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82262",
    "file_id": "8260",
    "item_id": "8260",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82263",
    "file_id": "8260",
    "item_id": "8260",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8261",
  "name": "Mobile UX Redesign Spec - draft 006.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82264",
    "file_id": "8261",
    "item_id": "8261",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82265",
    "file_id": "8261",
    "item_id": "8261",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82266",
    "file_id": "8261",
    "item_id": "8261",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8262",
  "name": "Mobile UX Redesign Spec - draft 007.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82267",
    "file_id": "8262",
    "item_id": "8262",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82268",
    "file_id": "8262",
    "item_id": "8262",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82269",
    "file_id": "8262",
    "item_id": "8262",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8263",
  "name": "Mobile UX Redesign Spec - draft 008.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82270",
    "file_id": "8263",
    "item_id": "8263",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82271",
    "file_id": "8263",
    "item_id": "8263",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82272",
    "file_id": "8263",
    "item_id": "8263",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8264",
  "name": "Mobile UX Redesign Spec - draft 009.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82273",
    "file_id": "8264",
    "item_id": "8264",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82274",
    "file_id": "8264",
    "item_id": "8264",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82275",
    "file_id": "8264",
    "item_id": "8264",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8265",
  "name": "Mobile UX Redesign Spec - draft 010.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82276",
    "file_id": "8265",
    "item_id": "8265",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82277",
    "file_id": "8265",
    "item_id": "8265",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82278",
    "file_id": "8265",
    "item_id": "8265",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8266",
  "name": "Mobile UX Redesign Spec - draft 011.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82279",
    "file_id": "8266",
    "item_id": "8266",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82280",
    "file_id": "8266",
    "item_id": "8266",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82281",
    "file_id": "8266",
    "item_id": "8266",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8267",
  "name": "Mobile UX Redesign Spec - draft 012.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82282",
    "file_id": "8267",
    "item_id": "8267",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82283",
    "file_id": "8267",
    "item_id": "8267",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82284",
    "file_id": "8267",
    "item_id": "8267",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8268",
  "name": "Mobile UX Redesign Spec - draft 013.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82285",
    "file_id": "8268",
    "item_id": "8268",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82286",
    "file_id": "8268",
    "item_id": "8268",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82287",
    "file_id": "8268",
    "item_id": "8268",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8269",
  "name": "Mobile UX Redesign Spec - draft 014.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82288",
    "file_id": "8269",
    "item_id": "8269",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82289",
    "file_id": "8269",
    "item_id": "8269",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82290",
    "file_id": "8269",
    "item_id": "8269",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8270",
  "name": "Mobile UX Redesign Spec - draft 015.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82291",
    "file_id": "8270",
    "item_id": "8270",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82292",
    "file_id": "8270",
    "item_id": "8270",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82293",
    "file_id": "8270",
    "item_id": "8270",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8271",
  "name": "Mobile UX Redesign Spec - draft 016.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82294",
    "file_id": "8271",
    "item_id": "8271",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82295",
    "file_id": "8271",
    "item_id": "8271",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82296",
    "file_id": "8271",
    "item_id": "8271",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8272",
  "name": "Mobile UX Redesign Spec - draft 017.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82297",
    "file_id": "8272",
    "item_id": "8272",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82298",
    "file_id": "8272",
    "item_id": "8272",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82299",
    "file_id": "8272",
    "item_id": "8272",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8273",
  "name": "Mobile UX Redesign Spec - draft 018.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82300",
    "file_id": "8273",
    "item_id": "8273",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82301",
    "file_id": "8273",
    "item_id": "8273",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82302",
    "file_id": "8273",
    "item_id": "8273",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8274",
  "name": "Mobile UX Redesign Spec - draft 019.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82303",
    "file_id": "8274",
    "item_id": "8274",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82304",
    "file_id": "8274",
    "item_id": "8274",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82305",
    "file_id": "8274",
    "item_id": "8274",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8275",
  "name": "Mobile UX Redesign Spec - draft 020.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82306",
    "file_id": "8275",
    "item_id": "8275",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82307",
    "file_id": "8275",
    "item_id": "8275",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82308",
    "file_id": "8275",
    "item_id": "8275",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8276",
  "name": "Mobile UX Redesign Spec - draft 021.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82309",
    "file_id": "8276",
    "item_id": "8276",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82310",
    "file_id": "8276",
    "item_id": "8276",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82311",
    "file_id": "8276",
    "item_id": "8276",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8277",
  "name": "Mobile UX Redesign Spec - draft 022.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82312",
    "file_id": "8277",
    "item_id": "8277",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82313",
    "file_id": "8277",
    "item_id": "8277",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82314",
    "file_id": "8277",
    "item_id": "8277",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8278",
  "name": "Mobile UX Redesign Spec - draft 023.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82315",
    "file_id": "8278",
    "item_id": "8278",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82316",
    "file_id": "8278",
    "item_id": "8278",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82317",
    "file_id": "8278",
    "item_id": "8278",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8279",
  "name": "Mobile UX Redesign Spec - draft 024.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82318",
    "file_id": "8279",
    "item_id": "8279",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82319",
    "file_id": "8279",
    "item_id": "8279",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82320",
    "file_id": "8279",
    "item_id": "8279",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8280",
  "name": "Mobile UX Redesign Spec - draft 025.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82321",
    "file_id": "8280",
    "item_id": "8280",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82322",
    "file_id": "8280",
    "item_id": "8280",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82323",
    "file_id": "8280",
    "item_id": "8280",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8281",
  "name": "Mobile UX Redesign Spec - draft 026.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82324",
    "file_id": "8281",
    "item_id": "8281",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82325",
    "file_id": "8281",
    "item_id": "8281",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82326",
    "file_id": "8281",
    "item_id": "8281",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8282",
  "name": "Mobile UX Redesign Spec - draft 027.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82327",
    "file_id": "8282",
    "item_id": "8282",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82328",
    "file_id": "8282",
    "item_id": "8282",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82329",
    "file_id": "8282",
    "item_id": "8282",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8283",
  "name": "Mobile UX Redesign Spec - draft 028.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82330",
    "file_id": "8283",
    "item_id": "8283",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82331",
    "file_id": "8283",
    "item_id": "8283",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82332",
    "file_id": "8283",
    "item_id": "8283",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8284",
  "name": "Mobile UX Redesign Spec - draft 029.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82333",
    "file_id": "8284",
    "item_id": "8284",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82334",
    "file_id": "8284",
    "item_id": "8284",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82335",
    "file_id": "8284",
    "item_id": "8284",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8285",
  "name": "Mobile UX Redesign Spec - draft 030.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82336",
    "file_id": "8285",
    "item_id": "8285",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82337",
    "file_id": "8285",
    "item_id": "8285",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82338",
    "file_id": "8285",
    "item_id": "8285",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8286",
  "name": "Mobile UX Redesign Spec - draft 031.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82339",
    "file_id": "8286",
    "item_id": "8286",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82340",
    "file_id": "8286",
    "item_id": "8286",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82341",
    "file_id": "8286",
    "item_id": "8286",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8287",
  "name": "Mobile UX Redesign Spec - draft 032.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82342",
    "file_id": "8287",
    "item_id": "8287",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82343",
    "file_id": "8287",
    "item_id": "8287",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82344",
    "file_id": "8287",
    "item_id": "8287",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8288",
  "name": "Mobile UX Redesign Spec - draft 033.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82345",
    "file_id": "8288",
    "item_id": "8288",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82346",
    "file_id": "8288",
    "item_id": "8288",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82347",
    "file_id": "8288",
    "item_id": "8288",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8289",
  "name": "Mobile UX Redesign Spec - draft 034.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82348",
    "file_id": "8289",
    "item_id": "8289",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82349",
    "file_id": "8289",
    "item_id": "8289",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82350",
    "file_id": "8289",
    "item_id": "8289",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8290",
  "name": "Mobile UX Redesign Spec - draft 035.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82351",
    "file_id": "8290",
    "item_id": "8290",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82352",
    "file_id": "8290",
    "item_id": "8290",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82353",
    "file_id": "8290",
    "item_id": "8290",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8291",
  "name": "Mobile UX Redesign Spec - draft 036.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82354",
    "file_id": "8291",
    "item_id": "8291",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82355",
    "file_id": "8291",
    "item_id": "8291",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82356",
    "file_id": "8291",
    "item_id": "8291",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8292",
  "name": "Mobile UX Redesign Spec - draft 037.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82357",
    "file_id": "8292",
    "item_id": "8292",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82358",
    "file_id": "8292",
    "item_id": "8292",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82359",
    "file_id": "8292",
    "item_id": "8292",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8293",
  "name": "Mobile UX Redesign Spec - draft 038.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82360",
    "file_id": "8293",
    "item_id": "8293",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82361",
    "file_id": "8293",
    "item_id": "8293",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82362",
    "file_id": "8293",
    "item_id": "8293",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8294",
  "name": "Mobile UX Redesign Spec - draft 039.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82363",
    "file_id": "8294",
    "item_id": "8294",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82364",
    "file_id": "8294",
    "item_id": "8294",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82365",
    "file_id": "8294",
    "item_id": "8294",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8295",
  "name": "Mobile UX Redesign Spec - draft 040.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82366",
    "file_id": "8295",
    "item_id": "8295",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82367",
    "file_id": "8295",
    "item_id": "8295",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82368",
    "file_id": "8295",
    "item_id": "8295",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8296",
  "name": "Mobile UX Redesign Spec - draft 041.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82369",
    "file_id": "8296",
    "item_id": "8296",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82370",
    "file_id": "8296",
    "item_id": "8296",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82371",
    "file_id": "8296",
    "item_id": "8296",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8297",
  "name": "Mobile UX Redesign Spec - draft 042.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82372",
    "file_id": "8297",
    "item_id": "8297",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82373",
    "file_id": "8297",
    "item_id": "8297",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82374",
    "file_id": "8297",
    "item_id": "8297",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8298",
  "name": "Mobile UX Redesign Spec - draft 043.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82375",
    "file_id": "8298",
    "item_id": "8298",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82376",
    "file_id": "8298",
    "item_id": "8298",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82377",
    "file_id": "8298",
    "item_id": "8298",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8299",
  "name": "Mobile UX Redesign Spec - draft 044.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82378",
    "file_id": "8299",
    "item_id": "8299",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82379",
    "file_id": "8299",
    "item_id": "8299",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82380",
    "file_id": "8299",
    "item_id": "8299",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8300",
  "name": "Mobile UX Redesign Spec - draft 045.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82381",
    "file_id": "8300",
    "item_id": "8300",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82382",
    "file_id": "8300",
    "item_id": "8300",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82383",
    "file_id": "8300",
    "item_id": "8300",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8301",
  "name": "Mobile UX Redesign Spec - draft 046.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82384",
    "file_id": "8301",
    "item_id": "8301",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82385",
    "file_id": "8301",
    "item_id": "8301",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82386",
    "file_id": "8301",
    "item_id": "8301",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8302",
  "name": "Mobile UX Redesign Spec - draft 047.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82387",
    "file_id": "8302",
    "item_id": "8302",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82388",
    "file_id": "8302",
    "item_id": "8302",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82389",
    "file_id": "8302",
    "item_id": "8302",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8303",
  "name": "Mobile UX Redesign Spec - draft 048.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82390",
    "file_id": "8303",
    "item_id": "8303",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82391",
    "file_id": "8303",
    "item_id": "8303",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82392",
    "file_id": "8303",
    "item_id": "8303",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8304",
  "name": "Mobile UX Redesign Spec - draft 049.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82393",
    "file_id": "8304",
    "item_id": "8304",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82394",
    "file_id": "8304",
    "item_id": "8304",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82395",
    "file_id": "8304",
    "item_id": "8304",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8305",
  "name": "Mobile UX Redesign Spec - draft 050.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82396",
    "file_id": "8305",
    "item_id": "8305",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82397",
    "file_id": "8305",
    "item_id": "8305",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82398",
    "file_id": "8305",
    "item_id": "8305",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8306",
  "name": "Mobile UX Redesign Spec - draft 051.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82399",
    "file_id": "8306",
    "item_id": "8306",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82400",
    "file_id": "8306",
    "item_id": "8306",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82401",
    "file_id": "8306",
    "item_id": "8306",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8307",
  "name": "Mobile UX Redesign Spec - draft 052.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82402",
    "file_id": "8307",
    "item_id": "8307",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82403",
    "file_id": "8307",
    "item_id": "8307",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82404",
    "file_id": "8307",
    "item_id": "8307",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8308",
  "name": "Mobile UX Redesign Spec - draft 053.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82405",
    "file_id": "8308",
    "item_id": "8308",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82406",
    "file_id": "8308",
    "item_id": "8308",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82407",
    "file_id": "8308",
    "item_id": "8308",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8309",
  "name": "Mobile UX Redesign Spec - draft 054.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82408",
    "file_id": "8309",
    "item_id": "8309",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82409",
    "file_id": "8309",
    "item_id": "8309",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82410",
    "file_id": "8309",
    "item_id": "8309",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8310",
  "name": "Mobile UX Redesign Spec - draft 055.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82411",
    "file_id": "8310",
    "item_id": "8310",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82412",
    "file_id": "8310",
    "item_id": "8310",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82413",
    "file_id": "8310",
    "item_id": "8310",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8311",
  "name": "Mobile UX Redesign Spec - draft 056.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82414",
    "file_id": "8311",
    "item_id": "8311",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82415",
    "file_id": "8311",
    "item_id": "8311",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82416",
    "file_id": "8311",
    "item_id": "8311",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8312",
  "name": "Mobile UX Redesign Spec - draft 057.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82417",
    "file_id": "8312",
    "item_id": "8312",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82418",
    "file_id": "8312",
    "item_id": "8312",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82419",
    "file_id": "8312",
    "item_id": "8312",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8313",
  "name": "Mobile UX Redesign Spec - draft 058.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82420",
    "file_id": "8313",
    "item_id": "8313",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82421",
    "file_id": "8313",
    "item_id": "8313",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82422",
    "file_id": "8313",
    "item_id": "8313",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8314",
  "name": "Mobile UX Redesign Spec - draft 059.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82423",
    "file_id": "8314",
    "item_id": "8314",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82424",
    "file_id": "8314",
    "item_id": "8314",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82425",
    "file_id": "8314",
    "item_id": "8314",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8315",
  "name": "Mobile UX Redesign Spec - draft 060.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82426",
    "file_id": "8315",
    "item_id": "8315",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82427",
    "file_id": "8315",
    "item_id": "8315",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82428",
    "file_id": "8315",
    "item_id": "8315",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8316",
  "name": "Mobile UX Redesign Spec - draft 061.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82429",
    "file_id": "8316",
    "item_id": "8316",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82430",
    "file_id": "8316",
    "item_id": "8316",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82431",
    "file_id": "8316",
    "item_id": "8316",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 },
 {
  "id": "8317",
  "name": "Mobile UX Redesign Spec - draft 062.xlsx",
  "parent_id": "8200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.",
  "size": 1800000,
  "extension": "xlsx",
  "comment_count": 3,
  "tags": "[]",
  "created_at": "2026-06-01T09:00:00+00:00",
  "modified_at": "2026-06-01T09:00:00+00:00",
  "uploader_display_name": "Jordan Lee",
  "folder path": "All Files / Product Specs",
  "box_folders": [
   {
    "id": "8200",
    "name": "Product Specs",
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
    "id": "82432",
    "file_id": "8317",
    "item_id": "8317",
    "item_type": "file",
    "message": "Budget looks right.",
    "created_by_id": "30000000005",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82433",
    "file_id": "8317",
    "item_id": "8317",
    "item_type": "file",
    "message": "Add Q4 line item.",
    "created_by_id": "30000000006",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   },
   {
    "id": "82434",
    "file_id": "8317",
    "item_id": "8317",
    "item_type": "file",
    "message": "Updated, thanks.",
    "created_by_id": "30000000007",
    "created_at": "2026-06-10T15:00:00+00:00",
    "modified_at": "2026-06-10T15:00:00+00:00",
    "is_reply_comment": false
   }
  ]
 }
]
