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
  "id": "8255",
  "name": "Mobile Nav Redesign Spec.pdf",
  "parent_id": "8254",
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
  "folder path": "All Files / Product Specs / Current",
  "box_folders": [
   {
    "id": "8254",
    "name": "Current",
    "parent_id": "8200",
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
    "id": "82244",
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
    "id": "82245",
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
 }
]
