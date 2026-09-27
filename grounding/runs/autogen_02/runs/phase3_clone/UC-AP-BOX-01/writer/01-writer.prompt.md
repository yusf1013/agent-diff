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
> Add the tag ready-for-review to the folder in the Legal Archive that holds more than 800 MB of files, has a shared link open to anyone, and was modified after August 15, 2026.

Conditions of the request:
Records of `box_folders`, where:
  - `size` > 800000000
  - `shared_link.access` = "open"
  - `modified_at` > "2026-08-15T23:59:59+00:00"
  - at least one record of `box_folders` linked by `parent_id` eq `box_folders.id`, where:
    - `name` = "Legal Archive"

The target record (table `box_folders`, key `id`):
{"id": "9001", "type": "folder", "name": "Discovery Production Set", "parent_id": "9000", "owned_by_id": "30000000006", "created_by_id": "30000000006", "modified_by_id": "30000000006", "description": "", "item_status": "active", "size": 900000000, "tags": "[]", "collections": "[]", "created_at": "2026-01-05T09:00:00+00:00", "modified_at": "2026-08-20T10:00:00+00:00", "sequence_id": "0", "etag": "0", "shared_link": "{\"url\": \"https://app.box.com/s/9001\", \"access\": \"open\", \"effective_access\": \"open\"}"}

Other records of `box_folders`, for their conventions:
{"id": "0", "type": "folder", "name": "All Files", "parent_id": null, "owned_by_id": "30000000001", "description": "", "item_status": "active", "size": 0}
{"id": "9000", "type": "folder", "name": "Legal Archive", "parent_id": "0", "owned_by_id": "30000000006", "created_by_id": "30000000006", "modified_by_id": "30000000006", "description": "", "item_status": "active", "size": 0, "tags": "[]", "collections": "[]", "created_at": "2025-01-01T09:00:00+00:00", "modified_at": "2025-01-01T09:00:00+00:00", "sequence_id": "0", "etag": "0"}
{"id": "9002", "type": "folder", "name": "Discovery Custodian Files", "parent_id": "9000", "owned_by_id": "30000000006", "created_by_id": "30000000006", "modified_by_id": "30000000006", "description": "", "item_status": "active", "size": 760000000, "tags": "[]", "collections": "[]", "created_at": "2025-11-01T09:00:00+00:00", "modified_at": "2026-08-18T09:00:00+00:00", "sequence_id": "0", "etag": "0", "shared_link": "{\"url\": \"https://app.box.com/s/9002\", \"access\": \"open\", \"effective_access\": \"open\"}"}
{"id": "9003", "type": "folder", "name": "Discovery Vendor Files", "parent_id": "9000", "owned_by_id": "30000000006", "created_by_id": "30000000006", "modified_by_id": "30000000006", "description": "", "item_status": "active", "size": 850000000, "tags": "[]", "collections": "[]", "created_at": "2026-02-10T09:00:00+00:00", "modified_at": "2026-08-25T09:00:00+00:00", "sequence_id": "0", "etag": "0", "shared_link": "{\"url\": \"https://app.box.com/s/9003\", \"access\": \"company\", \"effective_access\": \"company\"}"}
{"id": "9004", "type": "folder", "name": "Discovery Draft Bundle", "parent_id": "9000", "owned_by_id": "30000000006", "created_by_id": "30000000006", "modified_by_id": "30000000006", "description": "", "item_status": "active", "size": 880000000, "tags": "[]", "collections": "[]", "created_at": "2026-08-22T09:00:00+00:00", "modified_at": "2026-07-01T09:00:00+00:00", "sequence_id": "0", "etag": "0", "shared_link": "{\"url\": \"https://app.box.com/s/9004\", \"access\": \"open\", \"effective_access\": \"open\"}"}

Keys already used in `box_folders` (the copy needs a new one): 0, 9000, 9001, 9002, 9003, 9004, 9005, 9006, 9100

Rows that point at the target (copied with the target):
(none)

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