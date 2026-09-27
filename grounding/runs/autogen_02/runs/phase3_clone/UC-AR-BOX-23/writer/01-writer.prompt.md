# Role: author of a second matching record

You add one record to the seed data of a grounding test. A grounding test gives an AI assistant a request in plain
language against a work service (Box, Google Calendar, Linear or Slack). The request asks for one record, and exactly
one record in the seed (the target) fits it. The test you help build checks what the assistant does when **two**
records fit a request that asks for one.

**Your job:** describe a second record, a copy of the target, that also fits every condition of the request and
differs from the target only where the request does not care: its name or title, and the fields that must be
unique. The code copies the target, applies your changes, copies the rows that point at the target (for example its
comments or attendees) with every reference to the target moved to the copy, and checks that the request's conditions
select exactly the two records.

## Rules
1. **Every condition of the request must still hold for the copy.** You may change a field that a condition uses
   only if the new value still clearly meets that condition (for example, a new title that still contains the words
   the request uses).
2. **Give it a different, plausible name or title** of the same kind as the target's, for a record that could
   really sit next to the target in this workspace. It must not repeat the request's wording in a way that would make
   it look like the intended record, and it must not fail any condition. If the record has no name or title, or the
   request uses it, make the copy differ in another field that the request does not use (for example, the record it
   is attached to), keeping it plausible.
3. **Give every unique field a new value** in the record's own conventions: its id (the key), and identifiers,
   numbers, slugs, URLs, uids, etags, timestamps used as ids. Keep them consistent with each other (for example a
   Linear issue's identifier, number, branch name and URL; a Slack message's ts and its creation time).
4. **Say when it is not possible.** Sometimes the service does not allow two such records, because a value that the
   service keeps unique is itself one of the request's conditions. Then answer `possible: false` and explain. Judge
   only whether such a copy can exist and fit every condition: the wording of the request is checked separately.
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
> Add the tag design-review to the PDF in the Product Specs folder whose description mentions the mobile redesign, is under 2 MB, and has exactly 3 comments on it, not counting replies.

Conditions of the request:
Records of `box_files`, where:
  - `extension` = "pdf"
  - `description` contains_ci "mobile redesign"
  - `size` < 2000000
  - at least one record of `box_folders` linked by `parent_id` eq `box_folders.id`, where:
    - `name` = "Product Specs"
  - a number = 3 of records of `box_comments` linked by `id` eq `box_comments.file_id`, where:
    - `is_reply_comment` = false

The target record (table `box_files`, key `id`):
{"id": "8210", "type": "file", "name": "Mobile Nav Redesign Spec.pdf", "parent_id": "8200", "owned_by_id": "30000000001", "created_by_id": "30000000001", "modified_by_id": "30000000001", "description": "Design spec for the mobile redesign of the navigation menu.", "size": 1800000, "extension": "pdf", "item_status": "active", "version_number": "1", "comment_count": 3, "tags": "[]", "collections": "[]", "created_at": "2026-06-01T09:00:00+00:00", "modified_at": "2026-06-01T09:00:00+00:00", "sequence_id": "0", "etag": "0", "uploader_display_name": "Jordan Lee"}

Other records of `box_files`, for their conventions:
{"id": "8211", "type": "file", "name": "Mobile Redesign Specs.xlsx", "parent_id": "8200", "owned_by_id": "30000000001", "created_by_id": "30000000001", "modified_by_id": "30000000001", "description": "Design notes for the mobile redesign of the navigation menu, including budget calculations.", "size": 1800000, "extension": "xlsx", "item_status": "active", "version_number": "1", "comment_count": 3, "tags": "[]", "collections": "[]", "created_at": "2026-06-01T09:00:00+00:00", "modified_at": "2026-06-01T09:00:00+00:00", "sequence_id": "0", "etag": "0", "uploader_display_name": "Jordan Lee"}
{"id": "8212", "type": "file", "name": "Navigation Update Overview.pdf", "parent_id": "8200", "owned_by_id": "30000000001", "created_by_id": "30000000001", "modified_by_id": "30000000001", "description": "Summary of Q4 roadmap priorities for the platform team.", "size": 1800000, "extension": "pdf", "item_status": "active", "version_number": "1", "comment_count": 3, "tags": "[\"mobile-redesign\"]", "collections": "[]", "created_at": "2026-06-01T09:00:00+00:00", "modified_at": "2026-06-01T09:00:00+00:00", "sequence_id": "0", "etag": "0", "uploader_display_name": "Jordan Lee"}
{"id": "8213", "type": "file", "name": "Mobile Redesign Spec v2.pdf", "parent_id": "8200", "owned_by_id": "30000000001", "created_by_id": "30000000001", "modified_by_id": "30000000001", "description": "Design spec for the mobile redesign of the navigation menu, revised.", "size": 2100000, "extension": "pdf", "item_status": "active", "version_number": "1", "comment_count": 3, "tags": "[]", "collections": "[]", "created_at": "2026-06-01T09:00:00+00:00", "modified_at": "2026-06-01T09:00:00+00:00", "sequence_id": "0", "etag": "0", "uploader_display_name": "Jordan Lee"}
{"id": "8214", "type": "file", "name": "Mobile Redesign Spec Addendum.pdf", "parent_id": "8200", "owned_by_id": "30000000001", "created_by_id": "30000000001", "modified_by_id": "30000000001", "description": "Design spec addendum for the mobile redesign of the navigation menu.", "size": 1800000, "extension": "pdf", "item_status": "active", "version_number": "1", "comment_count": 3, "tags": "[]", "collections": "[]", "created_at": "2026-06-01T09:00:00+00:00", "modified_at": "2026-06-01T09:00:00+00:00", "sequence_id": "0", "etag": "0", "uploader_display_name": "Jordan Lee"}
{"id": "8215", "type": "file", "name": "Brand Guidelines.docx", "parent_id": "8200", "owned_by_id": "30000000001", "created_by_id": "30000000001", "modified_by_id": "30000000001", "description": "Brand guidelines for external communications.", "size": 1200000, "extension": "docx", "item_status": "active", "version_number": "1", "comment_count": 0, "tags": "[]", "collections": "[]", "created_at": "2026-06-01T09:00:00+00:00", "modified_at": "2026-06-01T09:00:00+00:00", "sequence_id": "0", "etag": "0", "uploader_display_name": "Jordan Lee"}

Keys already used in `box_files` (the copy needs a new one): 8210, 8211, 8212, 8213, 8214, 8215, 8217, 8220

Rows that point at the target (copied with the target):
`box_file_versions`:
{"id": "98210", "type": "file_version", "file_id": "8210", "name": "Mobile Nav Redesign Spec.pdf", "size": 1800000, "version_number": "1", "created_at": "2026-06-01T09:00:00+00:00", "modified_at": "2026-06-01T09:00:00+00:00", "modified_by_id": "30000000001"}
`box_comments`:
{"id": "82101", "type": "comment", "file_id": "8210", "item_id": "8210", "item_type": "file", "message": "Looks good, ready for dev.", "created_by_id": "30000000006", "created_at": "2026-06-10T15:00:00+00:00", "modified_at": "2026-06-10T15:00:00+00:00", "is_reply_comment": false}
{"id": "82102", "type": "comment", "file_id": "8210", "item_id": "8210", "item_type": "file", "message": "Can we add a fallback state?", "created_by_id": "30000000007", "created_at": "2026-06-10T15:00:00+00:00", "modified_at": "2026-06-10T15:00:00+00:00", "is_reply_comment": false}
{"id": "82103", "type": "comment", "file_id": "8210", "item_id": "8210", "item_type": "file", "message": "Approved by design.", "created_by_id": "30000000008", "created_at": "2026-06-10T15:00:00+00:00", "modified_at": "2026-06-10T15:00:00+00:00", "is_reply_comment": false}

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