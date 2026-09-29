You check test cases for an AI assistant that acts in a workspace on a user's behalf. You read carefully
and literally, the way the user who wrote the request would mean it.

---

A user sent the assistant this request in their Box workspace:

    "Add the tag needs-audit to all the folders under Client Deliverables that are larger than 2 GB, have a shared link on them, and haven't been modified since May 1."

The user is Jordan Lee. Below is every Box folder in the workspace, with what the assistant can see about it. Which of
them does the user's request ask the assistant to act on?

List the id of every record the request covers, and only those. Read each condition of the request as the user
would mean it. If you cannot tell whether the user means a record, list it under `unsure` with the reason (and do
not list it in `ids`). Answer with JSON: {"ids": [...], "unsure": [{"id", "why"}], "notes": "..."}.

Records:
[
 {
  "id": "0",
  "name": "All Files",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "size": 0,
  "folder path": "",
  "box_folders": []
 },
 {
  "id": "9200",
  "name": "Client Deliverables",
  "parent_id": "0",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 0,
  "tags": "[]",
  "created_at": "2026-01-01T09:00:00+00:00",
  "modified_at": "2026-01-01T09:00:00+00:00",
  "folder path": "All Files",
  "box_folders": [
   {
    "id": "0",
    "name": "All Files",
    "owned_by_id": "30000000001",
    "size": 0
   }
  ]
 },
 {
  "id": "9201",
  "name": "Northwind Retainer",
  "parent_id": "9200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 2500000000,
  "tags": "[]",
  "created_at": "2026-01-05T09:00:00+00:00",
  "modified_at": "2026-04-15T10:00:00+00:00",
  "shared_link": "{\"url\": \"https://app.box.com/s/9201\", \"access\": \"company\", \"effective_access\": \"company\"}",
  "folder path": "All Files / Client Deliverables",
  "box_folders": [
   {
    "id": "9200",
    "name": "Client Deliverables",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-01-01T09:00:00+00:00",
    "modified_at": "2026-01-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "9202",
  "name": "Ridgeline Renewal",
  "parent_id": "9200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 1900000000,
  "tags": "[]",
  "created_at": "2026-01-06T09:00:00+00:00",
  "modified_at": "2026-04-10T09:00:00+00:00",
  "shared_link": "{\"url\": \"https://app.box.com/s/9202\", \"access\": \"company\", \"effective_access\": \"company\"}",
  "folder path": "All Files / Client Deliverables",
  "box_folders": [
   {
    "id": "9200",
    "name": "Client Deliverables",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-01-01T09:00:00+00:00",
    "modified_at": "2026-01-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "9203",
  "name": "Onboarding Assets",
  "parent_id": "9200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 50000000,
  "tags": "[]",
  "created_at": "2026-01-07T09:00:00+00:00",
  "modified_at": "2026-03-01T09:00:00+00:00",
  "shared_link": "{\"url\": \"https://app.box.com/s/9203\", \"access\": \"company\", \"effective_access\": \"company\"}",
  "folder path": "All Files / Client Deliverables",
  "box_folders": [
   {
    "id": "9200",
    "name": "Client Deliverables",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-01-01T09:00:00+00:00",
    "modified_at": "2026-01-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "9204",
  "name": "Compliance Archive",
  "parent_id": "9200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 2200000000,
  "tags": "[]",
  "created_at": "2026-01-08T09:00:00+00:00",
  "modified_at": "2026-04-20T09:00:00+00:00",
  "folder path": "All Files / Client Deliverables",
  "box_folders": [
   {
    "id": "9200",
    "name": "Client Deliverables",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-01-01T09:00:00+00:00",
    "modified_at": "2026-01-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "9205",
  "name": "Legacy Assets",
  "parent_id": "9200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 2300000000,
  "tags": "[]",
  "created_at": "2026-01-09T09:00:00+00:00",
  "modified_at": "2026-05-03T09:00:00+00:00",
  "shared_link": "{\"url\": \"https://app.box.com/s/9205\", \"access\": \"company\", \"effective_access\": \"company\"}",
  "folder path": "All Files / Client Deliverables",
  "box_folders": [
   {
    "id": "9200",
    "name": "Client Deliverables",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-01-01T09:00:00+00:00",
    "modified_at": "2026-01-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "9206",
  "name": "Enterprise Deliverables",
  "parent_id": "9200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 2400000000,
  "tags": "[]",
  "created_at": "2026-04-01T09:00:00+00:00",
  "modified_at": "2026-05-20T09:00:00+00:00",
  "shared_link": "{\"url\": \"https://app.box.com/s/9206\", \"access\": \"company\", \"effective_access\": \"company\"}",
  "folder path": "All Files / Client Deliverables",
  "box_folders": [
   {
    "id": "9200",
    "name": "Client Deliverables",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-01-01T09:00:00+00:00",
    "modified_at": "2026-01-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "9207",
  "name": "Vendor Contracts",
  "parent_id": "9200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 80000000,
  "tags": "[]",
  "created_at": "2026-01-10T09:00:00+00:00",
  "modified_at": "2026-05-10T09:00:00+00:00",
  "folder path": "All Files / Client Deliverables",
  "box_folders": [
   {
    "id": "9200",
    "name": "Client Deliverables",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-01-01T09:00:00+00:00",
    "modified_at": "2026-01-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "9300",
  "name": "Atlas Ventures",
  "parent_id": "0",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 500000000,
  "tags": "[]",
  "created_at": "2026-01-01T09:00:00+00:00",
  "modified_at": "2026-04-01T09:00:00+00:00",
  "folder path": "All Files",
  "box_folders": [
   {
    "id": "0",
    "name": "All Files",
    "owned_by_id": "30000000001",
    "size": 0
   }
  ]
 },
 {
  "id": "9301",
  "name": "Contoso Retainer",
  "parent_id": "9200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 2500000000,
  "tags": "[]",
  "created_at": "2026-01-05T09:00:00+00:00",
  "modified_at": "2026-04-15T10:00:00+00:00",
  "shared_link": "{\"url\": \"https://app.box.com/s/9201\", \"access\": \"company\", \"effective_access\": \"company\"}",
  "folder path": "All Files / Client Deliverables",
  "box_folders": [
   {
    "id": "9200",
    "name": "Client Deliverables",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-01-01T09:00:00+00:00",
    "modified_at": "2026-01-01T09:00:00+00:00"
   }
  ]
 },
 {
  "id": "9302",
  "name": "Northwind Engagement",
  "parent_id": "9200",
  "owned_by_id": "30000000001 (Jordan Lee)",
  "created_by_id": "30000000001 (Jordan Lee)",
  "modified_by_id": "30000000001 (Jordan Lee)",
  "size": 2500000000,
  "tags": "[]",
  "created_at": "2026-01-05T09:00:00+00:00",
  "modified_at": "2026-04-15T10:00:00+00:00",
  "shared_link": "{\"url\": \"https://app.box.com/s/9201\", \"access\": \"company\", \"effective_access\": \"company\"}",
  "folder path": "All Files / Client Deliverables",
  "box_folders": [
   {
    "id": "9200",
    "name": "Client Deliverables",
    "parent_id": "0",
    "owned_by_id": "30000000001",
    "created_by_id": "30000000001",
    "modified_by_id": "30000000001",
    "size": 0,
    "tags": "[]",
    "created_at": "2026-01-01T09:00:00+00:00",
    "modified_at": "2026-01-01T09:00:00+00:00"
   }
  ]
 }
]
