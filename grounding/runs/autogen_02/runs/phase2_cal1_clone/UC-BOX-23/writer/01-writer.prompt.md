# Role: author of a second matching record

You add one record to the seed data of a grounding test. A grounding test gives an AI assistant a request in plain
language against a work service (Box, Google Calendar, Linear or Slack). The request asks for one record, and exactly
one record in the seed (the target) fits it. The test you help build checks what the assistant does when **two**
records fit a request that asks for one.

**Your job:** describe a second record, a copy of the target, that also fits every condition of the request and
differs from the target only in what the request does not mention: its name or title, and the fields that must be
unique. The code copies the target, applies your changes, copies the rows that point at the target (for example its
comments or attendees), and checks that the request's conditions select exactly the two records.

## Rules
1. **Every condition of the request must still hold for the copy.** Change no field that a condition uses, and no
   field that the copied rows need.
2. **Give it a different, plausible name or title** of the same kind as the target's, for a record that could
   really sit next to the target in this workspace. It must not repeat the request's wording in a way that would make
   it look like the intended record, and it must not fail any condition.
3. **Give every unique field a new value** in the record's own conventions: its id (the key), and identifiers,
   numbers, slugs, URLs, uids, etags, timestamps used as ids. Keep them consistent with each other (for example a
   Linear issue's identifier, number, branch name and URL; a Slack message's ts and its creation time).
4. **Say when it is not possible.** Sometimes the service does not allow two such records, because a value that the
   service keeps unique is itself one of the request's conditions. Then answer `possible: false` and explain.
5. Touch nothing else. Other records stay as they are.

## Input
- The request, the service, and the conditions as a tree.
- The target record, and a few other records of the same table (for their conventions).
- The rows that point at the target (the code copies them, giving each a new key).
- The replica notes for the domain.

## Output
- `possible`, and `reason` (one or two sentences).
- `new_key`: the copy's key value.
- `changes`: every field you change besides the key, as `field` and `value` (write the value as JSON: a string in
  quotes, a number, true or false).
- `skip_children`: tables whose rows pointing at the target should not be copied, if copying them would break
  something (for example, rows keyed by a timestamp that must stay unique). Usually empty.


---

Service: Box.

Request:
> Add the tag renewal to the contract PDF whose description mentions the Initech renewal, that is larger than 2 MB and has at least three comments.

Conditions of the request:
Records of `box_files`, where:
  - `extension` = "pdf"
  - `description` contains_ci "initech renewal"
  - `size` > 2000000
  - a number >= 3 of records of `box_comments` linked by `id` eq `box_comments.file_id`

The target record (table `box_files`, key `id`):
{"id": "8101", "type": "file", "name": "Initech MSA.pdf", "parent_id": "8100", "owned_by_id": "30000000001", "created_by_id": "30000000001", "modified_by_id": "30000000001", "description": "Initech renewal terms for 2027", "size": 3400000, "extension": "pdf", "item_status": "active", "version_number": "1", "comment_count": 3, "tags": "[]", "collections": "[]", "created_at": "2026-06-01T09:00:00+00:00", "modified_at": "2026-06-01T09:00:00+00:00", "sequence_id": "0", "etag": "0", "uploader_display_name": "Jordan Lee"}

Other records of `box_files`, for their conventions:
{"id": "8102", "type": "file", "name": "Initech renewal.pdf", "parent_id": "8100", "owned_by_id": "30000000001", "created_by_id": "30000000001", "modified_by_id": "30000000001", "description": "Master terms, signed 2024", "size": 3100000, "extension": "pdf", "item_status": "active", "version_number": "1", "comment_count": 3, "tags": "[]", "collections": "[]", "created_at": "2026-06-01T09:00:00+00:00", "modified_at": "2026-06-01T09:00:00+00:00", "sequence_id": "0", "etag": "0", "uploader_display_name": "Jordan Lee"}
{"id": "8103", "type": "file", "name": "Initech SOW.pdf", "parent_id": "8100", "owned_by_id": "30000000001", "created_by_id": "30000000001", "modified_by_id": "30000000001", "description": "Initech renewal statement of work", "size": 1950000, "extension": "pdf", "item_status": "active", "version_number": "1", "comment_count": 3, "tags": "[]", "collections": "[]", "created_at": "2026-06-01T09:00:00+00:00", "modified_at": "2026-06-01T09:00:00+00:00", "sequence_id": "0", "etag": "0", "uploader_display_name": "Jordan Lee"}
{"id": "8104", "type": "file", "name": "Initech NDA.pdf", "parent_id": "8100", "owned_by_id": "30000000001", "created_by_id": "30000000001", "modified_by_id": "30000000001", "description": "Initech renewal NDA", "size": 2600000, "extension": "pdf", "item_status": "active", "version_number": "1", "comment_count": 2, "tags": "[]", "collections": "[]", "created_at": "2026-06-01T09:00:00+00:00", "modified_at": "2026-06-01T09:00:00+00:00", "sequence_id": "0", "etag": "0", "uploader_display_name": "Jordan Lee"}
{"id": "8105", "type": "file", "name": "Initech pricing.docx", "parent_id": "8100", "owned_by_id": "30000000001", "created_by_id": "30000000001", "modified_by_id": "30000000001", "description": "Initech renewal pricing", "size": 2900000, "extension": "docx", "item_status": "active", "version_number": "1", "comment_count": 3, "tags": "[]", "collections": "[]", "created_at": "2026-06-01T09:00:00+00:00", "modified_at": "2026-06-01T09:00:00+00:00", "sequence_id": "0", "etag": "0", "uploader_display_name": "Jordan Lee"}

Keys already used in `box_files` (the copy needs a new one): 8101, 8102, 8103, 8104, 8105

Rows that point at the target (copied with the target):
`box_file_versions`:
{"id": "98101", "type": "file_version", "file_id": "8101", "name": "Initech MSA.pdf", "size": 3400000, "version_number": "1", "created_at": "2026-06-01T09:00:00+00:00", "modified_at": "2026-06-01T09:00:00+00:00", "modified_by_id": "30000000001"}
`box_comments`:
{"id": "81010", "type": "comment", "file_id": "8101", "item_id": "8101", "item_type": "file", "message": "Reviewed section 1.", "created_by_id": "30000000006", "created_at": "2026-06-10T15:00:00+00:00", "modified_at": "2026-06-10T15:00:00+00:00", "is_reply_comment": false}
{"id": "81011", "type": "comment", "file_id": "8101", "item_id": "8101", "item_type": "file", "message": "Reviewed section 2.", "created_by_id": "30000000007", "created_at": "2026-06-10T15:00:00+00:00", "modified_at": "2026-06-10T15:00:00+00:00", "is_reply_comment": false}
{"id": "81012", "type": "comment", "file_id": "8101", "item_id": "8101", "item_type": "file", "message": "Reviewed section 3.", "created_by_id": "30000000008", "created_at": "2026-06-10T15:00:00+00:00", "modified_at": "2026-06-10T15:00:00+00:00", "is_reply_comment": false}

Replica notes:

# Box replica: how it differs from real Box, and its constraints

This replica is what the agent under test talks to. Where it differs from the real service, the replica decides.

## Reads
- **Folder listings** (`GET /folders/{id}/items`, `GET /folders/{id}`'s `item_collection`) return the short form of each
  item (id, type, etag, name, and for files a few timestamps), whatever `fields` asks for. Owner, tags, extension,
  comment count, collections and shared link need one `GET /files/{id}` or `GET /folders/{id}` per item. Creator
  and modifier appear in listings as mini users (name and login).
- **`GET /files/{id}`** returns the full file: name, description, size, extension, version_number, comment_count,
  tags, collections, shared_link, lock, created_by, modified_by, owned_by, parent, created_at, modified_at.
- **Search** (`GET /search?query=`) matches the **name or description** of files and folders. It reads only `type`
  and ignores `content_types`, so asking it to search comments or tags does nothing. Tasks and comments are never
  search results. `file_extensions` and `ancestor_folder_ids` work.
- **Comments** are listed per file (`GET /files/{id}/comments`), **tasks** per file (`GET /files/{id}/tasks`). A
  task carries its assignments (`task_assignment_collection`); there is no separate assignments route.
- **Hubs** need the header `box-version: 2025.0`: `GET /hubs`, `GET /hubs/{id}`, `GET /hub_items?hub_id=`.
- **Collections:** `GET /collections` lists the actor's collections (Favorites), `GET /collections/{id}/items`
  their items.
- There is no listing of a person's files, tasks or comments.

## Writes
- Tags are set with `PUT /files/{id}` or `PUT /folders/{id}` and body `{"tags": [...]}` (the whole list).
- A task's due date: `PUT /tasks/{id}` with `{"due_at": ...}`.
- Hub items: `POST /hubs/{id}/manage_items` (header `box-version: 2025.0`).
- The actor is an admin and can change any item in these seeds.

## Seeds
- The actor is Jordan Lee (`30000000001`). Seven other people exist by default (Maya Chen, Maya Lopez, Leo Park,
  Dana Whitfield, Priya Nair, Omar Haddad, Sam Rivera); more can be added.
- Ids are numeric strings. The root folder is `"0"`.


Describe the copy, following the rules.