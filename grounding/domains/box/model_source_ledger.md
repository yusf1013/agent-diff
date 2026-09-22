# Box model source ledger

Revision: `4691d3f076db2cdcccdc840c110aa797fa3196dc`. Scope and mapping discipline: [contextualization](contextualization.md). The full declaration/field index is [source_inventory.json](source_inventory.json), and reviewed decisions are [model.json](model.json).

## Persistence: forward coverage

| Source table | Disposition / destination | Field treatment and reason |
|---|---|---|
| `box_collections` ([schema.py:40](../../../backend/src/services/box/database/schema.py)) | entity → Collection | Named grouping of files and folders; no stored owner relationship. Identity: `id`; FK roles: —; stored values (including separately interpreted references): `type`, `name`, `collection_type`. Exact declarations and constraints are in the inventory. |
| `box_users` ([schema.py:74](../../../backend/src/services/box/database/schema.py)) | entity → User | Box account/profile. Other objects expose mini profiles; the actor endpoint exposes the full profile. Identity: `id`; FK roles: —; stored values (including separately interpreted references): `type`, `name`, `login`, `status`, `job_title`, `phone`, `address`, `avatar_url`, `language`, `timezone`, `space_amount`, `space_used`, `max_upload_size`, `notification_email`, `role`, `enterprise`, `tracking_codes`, `can_see_managed_users`, `is_sync_enabled`, `is_external_collab_restricted`, `is_exempt_from_device_limits`, `is_exempt_from_login_verification`, `is_platform_access_only`, `my_tags`, `hostname`, `external_app_user_id`, `created_at`, `modified_at`. Exact declarations and constraints are in the inventory. |
| `box_folders` ([schema.py:228](../../../backend/src/services/box/database/schema.py)) | entity → Folder | Hierarchical container with independent creator, modifier and owner roles. Identity: `id`; FK roles: `parent_id`, `created_by_id`, `modified_by_id`, `owned_by_id`; stored values (including separately interpreted references): `type`, `name`, `description`, `size`, `item_status`, `path`, `etag`, `sequence_id`, `tags`, `collections`, `shared_link`, `folder_upload_email`, `created_at`, `modified_at`, `trashed_at`, `purged_at`, `content_created_at`, `content_modified_at`, `sync_state`, `has_collaborations`, `can_non_owners_invite`, `is_externally_owned`, `is_collaboration_restricted_to_enterprise`, `can_non_owners_view_collaborators`, `is_accessible_via_shared_link`, `is_associated_with_app_item`, `permissions`, `allowed_shared_link_access_levels`, `allowed_invitee_roles`, `watermark_info`, `classification`, `box_metadata`. Exact declarations and constraints are in the inventory. |
| `box_files` ([schema.py:619](../../../backend/src/services/box/database/schema.py)) | entity → File | File metadata and membership in a folder, collections and version history. Identity: `id`; FK roles: `parent_id`, `created_by_id`, `modified_by_id`, `owned_by_id`; stored values (including separately interpreted references): `type`, `name`, `description`, `size`, `item_status`, `path`, `etag`, `sequence_id`, `sha_1`, `file_version_id`, `version_number`, `comment_count`, `extension`, `lock`, `tags`, `collections`, `shared_link`, `permissions`, `is_package`, `is_accessible_via_shared_link`, `is_externally_owned`, `has_collaborations`, `is_associated_with_app_item`, `allowed_invitee_roles`, `shared_link_permission_options`, `expiring_embed_link`, `watermark_info`, `box_metadata`, `representations`, `classification`, `uploader_display_name`, `created_at`, `modified_at`, `trashed_at`, `purged_at`, `content_created_at`, `content_modified_at`, `expires_at`, `disposition_at`. Exact declarations and constraints are in the inventory. |
| `box_file_versions` ([schema.py:1027](../../../backend/src/services/box/database/schema.py)) | entity → FileVersion | Identified version of a file, with optional version-owned binary content and MIME value. Identity: `id`; FK roles: `file_id`, `modified_by_id`, `trashed_by_id`, `restored_by_id`; stored values (including separately interpreted references): `type`, `version_number`, `sha_1`, `size`, `name`, `uploader_display_name`, `trashed_at`, `restored_at`, `purged_at`, `created_at`, `modified_at`. Exact declarations and constraints are in the inventory. |
| `box_file_contents` ([schema.py:1128](../../../backend/src/services/box/database/schema.py)) | folded_value → FileVersion | Unique version-owned binary value; preserve record id and presence inside FileVersion.content. All fields follow this disposition: `id`, `version_id`, `content`, `content_type`. Exact declarations and constraints are in the inventory. |
| `box_comments` ([schema.py:1159](../../../backend/src/services/box/database/schema.py)) | entity → Comment | Comment on a file, optionally replying to another comment on that file. Identity: `id`; FK roles: `file_id`, `created_by_id`; stored values (including separately interpreted references): `type`, `message`, `tagged_message`, `item_id`, `item_type`, `is_reply_comment`, `created_at`, `modified_at`. Exact declarations and constraints are in the inventory. |
| `box_tasks` ([schema.py:1248](../../../backend/src/services/box/database/schema.py)) | entity → Task | Review or completion request attached to a file. Identity: `id`; FK roles: `item_id`, `created_by_id`; stored values (including separately interpreted references): `type`, `message`, `action`, `is_completed`, `completion_rule`, `item_type`, `due_at`, `created_at`. Exact declarations and constraints are in the inventory. |
| `box_task_assignments` ([schema.py:1314](../../../backend/src/services/box/database/schema.py)) | entity → TaskAssignment | Assignment of a task to a user, with its own identity, resolution and optional file reference. Identity: `id`; FK roles: `task_id`, `item_id`, `assigned_to_id`, `assigned_by_id`; stored values (including separately interpreted references): `type`, `item_type`, `message`, `resolution_state`, `assigned_at`, `reminded_at`, `completed_at`. Exact declarations and constraints are in the inventory. |
| `box_hubs` ([schema.py:1400](../../../backend/src/services/box/database/schema.py)) | entity → Hub | Named curation space with creator/updater roles. Identity: `id`; FK roles: `created_by_id`, `updated_by_id`; stored values (including separately interpreted references): `type`, `title`, `description`, `is_ai_enabled`, `is_collaboration_restricted_to_enterprise`, `can_non_owners_invite`, `can_shared_link_be_created`, `view_count`, `created_at`, `updated_at`. Exact declarations and constraints are in the inventory. |
| `box_hub_items` ([schema.py:1474](../../../backend/src/services/box/database/schema.py)) | entity → HubItem | Identified, ordered entry in a hub pointing to a tagged item. File and folder tags resolve local resources; other tags remain opaque. Identity: `id`; FK roles: `hub_id`, `added_by_id`; stored values (including separately interpreted references): `type`, `item_id`, `item_type`, `item_name`, `position`, `added_at`. Exact declarations and constraints are in the inventory. |

ORM reverse relationships are projections of these roles, not extra edges. The full relationship declarations remain in the inventory. Composite pair associations are contracted once; owner-value folds remove only the storage split, preserving all values. No table is silently omitted.

## API: forward coverage

The operation inventory expands HTTP dispatchers by verb or records each actual GraphQL binding. Each operation maps to the families below. Within each handler the inventory retains accessed input keys, constructed object keys, keyword arguments, attribute expressions and helper calls; follow these to the corresponding entity fields/representations. Transport arguments (pagination, cursors, formatting, field selection), error/success envelopes and execution preconditions/effects are deferred to interface/behavior analysis. None establishes another domain entity.

| Family | Domain-bearing inputs/outputs and treatment |
|---|---|
| Account and search | User profile; File/Folder scalar matching and result projections. Query/paging/fields are interface mechanics. No WebLink persistence. |
| Folder operations | Folder identity, parent, role metadata, descriptive fields, collections, shared-link/upload/collaboration values, status and children/path views. |
| File operations | File metadata, parent, version selection, content/MIME and role projections; comments/tasks are views of their own related entities. Upload/download encodings and links are interface mechanics. |
| Comments | Comment body/tagged body, creator and file/reply target; deletion affects the record, not a new deletion entity. |
| Tasks | File task action/message/due/completion policy and embedded assignments; no separately dispatched assignment writer. |
| Hubs | Hub fields and tagged HubItem records; add only. Unsupported removal is a behavior/capability limitation. |
| Collections | Collection identity/name/type and File/Folder membership queried from JSON. |

| Registered operation/binding | Handler evidence |
|---|---|
| `GET /users/me` | `get_user_me` — [routes.py:206](../../../backend/src/services/box/api/routes.py) |
| `GET /search` | `search_content` — [routes.py:1015](../../../backend/src/services/box/api/routes.py) |
| `POST /folders` | `create_folder` — [routes.py:618](../../../backend/src/services/box/api/routes.py) |
| `GET /folders/{folder_id}` | `get_folder_by_id` — [routes.py:691](../../../backend/src/services/box/api/routes.py) |
| `PUT /folders/{folder_id}` | `update_folder_by_id` — [routes.py:769](../../../backend/src/services/box/api/routes.py) |
| `DELETE /folders/{folder_id}` | `delete_folder_by_id` — [routes.py:863](../../../backend/src/services/box/api/routes.py) |
| `GET /folders/{folder_id}/items` | `list_folder_items` — [routes.py:926](../../../backend/src/services/box/api/routes.py) |
| `POST /files/content` | `upload_file` — [routes.py:1116](../../../backend/src/services/box/api/routes.py) |
| `GET /files/{file_id}` | `get_file_by_id` — [routes.py:249](../../../backend/src/services/box/api/routes.py) |
| `PUT /files/{file_id}` | `update_file_by_id` — [routes.py:330](../../../backend/src/services/box/api/routes.py) |
| `DELETE /files/{file_id}` | `delete_file_by_id` — [routes.py:443](../../../backend/src/services/box/api/routes.py) |
| `GET /files/{file_id}/content` | `download_file` — [routes.py:500](../../../backend/src/services/box/api/routes.py) |
| `POST /files/{file_id}/content` | `upload_file_version` — [routes.py:1217](../../../backend/src/services/box/api/routes.py) |
| `GET /files/{file_id}/download` | `download_file_direct` — [routes.py:562](../../../backend/src/services/box/api/routes.py) |
| `GET /files/{file_id}/comments` | `list_file_comments` — [routes.py:1383](../../../backend/src/services/box/api/routes.py) |
| `GET /files/{file_id}/tasks` | `list_file_tasks` — [routes.py:1519](../../../backend/src/services/box/api/routes.py) |
| `POST /comments` | `create_comment` — [routes.py:1313](../../../backend/src/services/box/api/routes.py) |
| `GET /comments/{comment_id}` | `get_comment_by_id` — [routes.py:1440](../../../backend/src/services/box/api/routes.py) |
| `PUT /comments/{comment_id}` | `update_comment_by_id` — [routes.py:1466](../../../backend/src/services/box/api/routes.py) |
| `DELETE /comments/{comment_id}` | `delete_comment_by_id` — [routes.py:1493](../../../backend/src/services/box/api/routes.py) |
| `POST /tasks` | `create_task` — [routes.py:1569](../../../backend/src/services/box/api/routes.py) |
| `GET /tasks/{task_id}` | `get_task_by_id` — [routes.py:1654](../../../backend/src/services/box/api/routes.py) |
| `PUT /tasks/{task_id}` | `update_task_by_id` — [routes.py:1680](../../../backend/src/services/box/api/routes.py) |
| `DELETE /tasks/{task_id}` | `delete_task_by_id` — [routes.py:1727](../../../backend/src/services/box/api/routes.py) |
| `GET /hubs` | `list_hubs` — [routes.py:1767](../../../backend/src/services/box/api/routes.py) |
| `POST /hubs` | `create_hub` — [routes.py:1828](../../../backend/src/services/box/api/routes.py) |
| `GET /hubs/{hub_id}` | `get_hub_by_id` — [routes.py:1876](../../../backend/src/services/box/api/routes.py) |
| `PUT /hubs/{hub_id}` | `update_hub_by_id` — [routes.py:1912](../../../backend/src/services/box/api/routes.py) |
| `GET /hub_items` | `get_hub_items` — [routes.py:1963](../../../backend/src/services/box/api/routes.py) |
| `POST /hubs/{hub_id}/manage_items` | `manage_hub_items` — [routes.py:2024](../../../backend/src/services/box/api/routes.py) |
| `GET /collections` | `list_collections` — [routes.py:2118](../../../backend/src/services/box/api/routes.py) |
| `GET /collections/{collection_id}` | `get_collection_by_id` — [routes.py:2154](../../../backend/src/services/box/api/routes.py) |
| `GET /collections/{collection_id}/items` | `get_collection_items` — [routes.py:2185](../../../backend/src/services/box/api/routes.py) |

## Validation scope

The completion audit below records both directions of review, corrections and remaining qualifications. Its manual source decisions are stored in model_audit.json; the earlier broad summary in model.json is not used as a substitute for those checks.

The modeling tools compare inventory with live ORM metadata, check all retained FK targets/cardinalities and operation mappings, and exercise risky serializer/GraphQL shapes offline. Mechanical accounting supplements the manual interpretation; it does not prove runtime correctness.

Route counting excludes repeated entity types, attributes, resolution modes and derived shortcuts. The read screen does not certify whole-route discovery, every attribute, permissions or ordinary-use meaningfulness. No ordinary-request inclusion review is claimed.

## Completion audit: explicit evidence mappings

Completed source-to-model accounting and model-to-source review for the frozen structural model, with the qualifications and validation limits below. No entity, stored attribute, relationship, or published route-count change was adopted.

This section supersedes the earlier broad audit summary. It records manual interpretation; inventories and checks establish accounting, not semantic correctness by themselves.

### Shared API field mappings

| ID | Source witness | Fields, disposition and model destination |
|---|---|---|
| B-A0 | [api/routes.py](../../../backend/src/services/box/api/routes.py) — `_principal_user_id; route handlers; _filter_fields` | **Represented:** actor is User from request context; route IDs select the named entity. **Deferred:** fields selection, limit/offset/marker, sorting, request IDs, ETags/conditional headers, error envelopes and CRUD preconditions. Result entries are projections, not new entity types. |
| B-A1 | [database/schema.py](../../../backend/src/services/box/database/schema.py) — `User.to_dict; User.to_mini_dict; _empty_user_mini` | **Represented:** full User fields map to same-named stored attributes, with ISO formatting for created_at/modified_at. Mini user contains only id/name/login. **Derived/fixed:** type=user; missing creator/modifier can serialize as id="", name="", login="" instead of a real User. A mini profile does not expose job_title/enterprise/role. Enterprise, notification_email and tracking_codes remain structured User values. |
| B-A2 | [database/schema.py](../../../backend/src/services/box/database/schema.py) — `Folder.to_dict; to_item_dict; to_search_dict; to_mini_dict` | **Represented:** id/name/description/size/status, etag/sequence_id, tags, dates, sync_state and stored permission/collaboration/classification/upload/shared-link values. metadata → Folder.box_metadata. created_by/modified_by/owned_by/parent → their FK roles and mini projections. **Derived:** item_collection.entries from children/files; total_count from their lengths (entries may intentionally be empty). No separate item-collection entity. Projection variants expose different subsets; File search folder_upload_email is fixed null. |
| B-A3 | [database/schema.py](../../../backend/src/services/box/database/schema.py) — `File.to_dict; to_item_dict; to_search_dict; to_mini_dict; _get_extension; _get_file_version_dict` | **Represented:** File scalar/date/flag/JSON fields at their stored names; sha1 → sha_1, metadata → box_metadata. created_by/modified_by/owned_by/parent → FK roles. **Derived:** extension falls back to the name suffix; file_version is versions[0] under version_number descending order, not a lookup of stored file_version_id. **Retained independently:** cached version_number/size/comment_count/sha_1 and selected version identity; serialization does not establish consistency of those caches. |
| B-A4 | [database/schema.py](../../../backend/src/services/box/database/schema.py) — `Folder._get_path_collection; File._get_path_collection; _get_collections_dict`; [database/operations.py](../../../backend/src/services/box/database/operations.py) — `get_collection_items; update_folder; update_file_collections` | **Derived:** path_collection.entries resolve stored slash-separated path IDs, or walk parent when path is unset; / yields an empty ancestor list. Counts/order wrap that view. **Represented:** collections IDs identify Collection membership, including IDs normalized from objects. **Fixed:** each mini collection uses name=Favorites and collection_type=favorites without loading those values. Collection reads use JSON containment of the scalar ID; a dict-valued seeded array may serialize but not match that query. Folder route updates and the separate validating helper are not interchangeable. |
| B-A5 | [database/schema.py](../../../backend/src/services/box/database/schema.py) — `FileVersion.to_mini_dict; FileContent`; [database/operations.py](../../../backend/src/services/box/database/operations.py) — `get_file_content; _create_file_version` | **Represented:** file_version.{id,sha1} → FileVersion.id/sha_1; optional version-owned FileContent.content/content_type remain folded values, retaining content-row id and existence. version query parameter selects a FileVersion belonging to the File. **Deferred:** redirect URL, attachment filename, MIME headers and upload transport. The unused full-version serializer lists stored user roles but does not establish read exposure. |
| B-A6 | [database/schema.py](../../../backend/src/services/box/database/schema.py) — `Comment.to_dict; to_list_dict`; [database/operations.py](../../../backend/src/services/box/database/operations.py) — `create_comment` | **Represented:** message/tagged_message/is_reply_comment/timestamps and creator role. item.{type,id} → tagged file or parent-comment reference. Reply creation derives required file_id from the parent comment. Scoped file-comment listing supplies file context even though list entries omit item. **Deferred:** tagged-message presentation; it is not automatically a managed mention entity. |
| B-A7 | [database/schema.py](../../../backend/src/services/box/database/schema.py) — `Task.to_dict; TaskAssignment.to_dict`; [database/operations.py](../../../backend/src/services/box/database/operations.py) — `create_task; update_task` | **Represented:** Task action/message/due_at/completion_rule/is_completed, file and creator roles. task_assignment_collection.entries are TaskAssignment identities, message/resolution_state/dates and assigned_to/assigned_by/optional item roles; total_count is derived. Embedded assignments retain their own IDs. No dispatched assignment creator/updater is inferred from this serializer. |
| B-A8 | [database/schema.py](../../../backend/src/services/box/database/schema.py) — `Hub.to_dict; HubItem.to_dict; HubItem.to_full_dict`; [database/operations.py](../../../backend/src/services/box/database/operations.py) — `add_item_to_hub` | **Represented:** Hub id/title/description/flags/view_count/dates and creator/updater. Dispatched HubItem output type/id/name maps to item_type/item_id/item_name, not HubItem.id. Parent hub context comes from the scoped list. Stored position/added_at/added_by/id are retained but not exposed by this projection. File/folder targets are resolved; other tags are opaque. Full-entry serializer is unused. manage_items results echo each operation plus outcome metadata; removal is unimplemented. |
| B-A9 | [database/schema.py](../../../backend/src/services/box/database/schema.py) — `Collection.to_dict`; [database/operations.py](../../../backend/src/services/box/database/operations.py) — `list_collections; get_collection_items` | **Represented:** Collection id/type/name/collection_type. No owner role exists. Members are existing File/Folder projections through JSON membership, not new item identities. Collection totals are derived; paging wrapper fields are deferred. |
| B-A10 | [database/operations.py](../../../backend/src/services/box/database/operations.py) — `search_content`; [api/routes.py](../../../backend/src/services/box/api/routes.py) — `search_content` | **Represented:** query selects File/Folder name or description among active items; type selects file/folder populations. Output is the search projection in B-A2/B-A3. **Deferred:** ranking/filter syntax and paging. The handler does not forward ancestor_folder_ids/file_extensions helper parameters, and search does not inspect file bytes or implement WebLink objects. |
| B-A11 | [database/operations.py](../../../backend/src/services/box/database/operations.py) — `update_file; update_folder` | **Represented:** shared_link and lock are existing structured File/Folder values; shared-link access, permissions.can_download/can_preview/can_edit, URL/password/count/effective fields are inside that value. Generated URL and default permission/count values do not establish independent link/permission entities or enforcement. Explicit null, absent input and defaults are operation semantics, not additional attributes. |

### Operation-to-field-group coverage

Every registered operation is assigned below. Shared response mappings are recorded once above. Operations retain their exact dispatch/source references in the preceding inventory.

| Operation | Applicable field mappings | Operation-specific qualification |
|---|---|---|
| `GET /users/me` | B-A0, B-A1 | Current actor only; not a user-directory endpoint. |
| `GET /search` | B-A0, B-A10, B-A2, B-A3 | query/type identify File or Folder; empty/unsupported searches do not create a new entity category. |
| `POST /folders` | B-A0, B-A2, B-A4, B-A11 | folder_id/parent.id select Folder roles; name/description/tags/collections/shared_link map to the existing fields. List items may include File projections (B-A3). |
| `GET /folders/{folder_id}` | B-A0, B-A2, B-A4, B-A11 | folder_id/parent.id select Folder roles; name/description/tags/collections/shared_link map to the existing fields. List items may include File projections (B-A3). |
| `PUT /folders/{folder_id}` | B-A0, B-A2, B-A4, B-A11 | folder_id/parent.id select Folder roles; name/description/tags/collections/shared_link map to the existing fields. List items may include File projections (B-A3). |
| `DELETE /folders/{folder_id}` | B-A0, B-A2, B-A4, B-A11 | folder_id/parent.id select Folder roles; name/description/tags/collections/shared_link map to the existing fields. List items may include File projections (B-A3). |
| `GET /folders/{folder_id}/items` | B-A0, B-A2, B-A4, B-A11 | folder_id/parent.id select Folder roles; name/description/tags/collections/shared_link map to the existing fields. List items may include File projections (B-A3). |
| `POST /files/content` | B-A0, B-A3, B-A5 | attributes.name and attributes.parent.id → File name/parent; multipart file → new version content. |
| `GET /files/{file_id}` | B-A0, B-A3, B-A4, B-A11 | file_id selects File; parent.id selects Folder. name/description/tags/collections/shared_link/lock map to existing values. |
| `PUT /files/{file_id}` | B-A0, B-A3, B-A4, B-A11 | file_id selects File; parent.id selects Folder. name/description/tags/collections/shared_link/lock map to existing values. |
| `DELETE /files/{file_id}` | B-A0, B-A3, B-A4, B-A11 | file_id selects File; parent.id selects Folder. name/description/tags/collections/shared_link/lock map to existing values. |
| `GET /files/{file_id}/content` | B-A0, B-A5 | file_id plus optional version; redirect is transport. |
| `POST /files/{file_id}/content` | B-A0, B-A3, B-A5 | file_id selects File; attributes.name and multipart file → version/name/content; versions are independently identified. |
| `GET /files/{file_id}/download` | B-A0, B-A5 | Same content selection; raw bytes are the deliverable. |
| `GET /files/{file_id}/comments` | B-A0, B-A6 | comment_id selects Comment, or file_id scopes the listing; message edits Comment.message. |
| `GET /files/{file_id}/tasks` | B-A0, B-A7 | task_id selects Task, or file_id scopes the listing; action/message/due_at/completion_rule map to Task. |
| `POST /comments` | B-A0, B-A6 | item.id/type and message/tagged_message select target and content. |
| `GET /comments/{comment_id}` | B-A0, B-A6 | comment_id selects Comment, or file_id scopes the listing; message edits Comment.message. |
| `PUT /comments/{comment_id}` | B-A0, B-A6 | comment_id selects Comment, or file_id scopes the listing; message edits Comment.message. |
| `DELETE /comments/{comment_id}` | B-A0, B-A6 | comment_id selects Comment, or file_id scopes the listing; message edits Comment.message. |
| `POST /tasks` | B-A0, B-A7 | item.id/type must name a file; action/message/due_at/completion_rule are Task values. |
| `GET /tasks/{task_id}` | B-A0, B-A7 | task_id selects Task, or file_id scopes the listing; action/message/due_at/completion_rule map to Task. |
| `PUT /tasks/{task_id}` | B-A0, B-A7 | task_id selects Task, or file_id scopes the listing; action/message/due_at/completion_rule map to Task. |
| `DELETE /tasks/{task_id}` | B-A0, B-A7 | task_id selects Task, or file_id scopes the listing; action/message/due_at/completion_rule map to Task. |
| `GET /hubs` | B-A0, B-A8 | hub_id selects Hub; title/description are the editable values. |
| `POST /hubs` | B-A0, B-A8 | hub_id selects Hub; title/description are the editable values. |
| `GET /hubs/{hub_id}` | B-A0, B-A8 | hub_id selects Hub; title/description are the editable values. |
| `PUT /hubs/{hub_id}` | B-A0, B-A8 | hub_id selects Hub; title/description are the editable values. |
| `GET /hub_items` | B-A0, B-A8 | hub_id supplies HubItem parent context; marker/limit are controls. |
| `POST /hubs/{hub_id}/manage_items` | B-A0, B-A8 | operations[].action controls behavior; operations[].item.{type,id} names a target. Per-operation errors are not entities. |
| `GET /collections` | B-A0, B-A9, B-A4 | collection_id selects Collection; entries preserve File/Folder identities. |
| `GET /collections/{collection_id}` | B-A0, B-A9, B-A4 | collection_id selects Collection; entries preserve File/Folder identities. |
| `GET /collections/{collection_id}/items` | B-A0, B-A9, B-A4 | collection_id selects Collection; entries preserve File/Folder identities. |

### Model-to-source checks

| Model elements | Source and concrete check | Result / qualification |
|---|---|---|
| All 10 entity meanings; 11 table dispositions; 190 columns | schema declarations and B-A1–B-A9; match each retained attribute to its exact column, each FK to its named edge, and FileContent to its fold. User.login uniqueness and nullable references compared with SQLAlchemy metadata. | No new entity/attribute is introduced by this accounting. IDs, source fields and folded presence remain visible; seed population is not the boundary. |
| All 29 relationship roles and both-end cardinalities | 24 retained FK roles plus File/Folder collections, two tagged hub targets and comment reply. FK targets/nullability/unique constraints checked; JSON references traced through get_collection_items/add_item_to_hub/create_comment. | No duplicate inverse edge. File/folder targets on one HubItem are mutually exclusive; existing tagged-path exclusion retained. Parent/name and hub/item indexes are not unique constraints. |
| Every diagram edge and identity participation | Each edge is rendered from the same reviewed role; identifying status comes from whether its FK contributes to the source PK. | Corrected solid-line overstatement. Retained entities use independent id keys; these FK links are non-identifying. Graph connectivity unchanged. |
| FileContent fold and FileVersion independence | Unique version_id versus own content-row id; get_file_content uses file/version identity and content_row, not an independent content-resource route. | Preserves absent content versus present bytes/MIME; FileVersion stays independently identified. No collapse of historical versions. |
| B1–B9 qualifications and derived views | B-A1–B-A11 trace actual called serializers and relevant helpers; check fallback mini profiles, cache versus selected version, collection defaults and parent/path views. | Derived projections do not become duplicate attributes/entities; dormant serializers do not prove access. Scalar collection-array and path-cache qualifications now explicit. |
| Every enum/state/classification | utils/enums.py; schema status/action/completion/default declarations; create_task/update_task; update_file/update_folder. | Item/user/task/shared-link vocabularies map to their existing values. BoxSortDirection and BoxErrorCode are interface vocabularies, not domain states. TaskAssignment.resolution_state is an open stored string; is_completed and other counters are not assumed continuously derived. |
| Persistence boundary and absence of separate Box migration additions | backend/utils/seed_box_template.py:create_tables invokes Base.metadata.create_all; scoped migration scan found no Box-specific extra domain table/column additions. | Complete current metadata remains the extraction boundary. Existing template/live-schema drift is not certified by source-only checks. |

### Findings and approval boundary

- Diagram notation corrected without changing a model node, field, role or count.
- API inventory and semantic mappings are now separate: every operation names its relevant reviewed field groups.
- No published graph/count change made. Remaining approval-sensitive findings, if any, must be recorded here before adoption.
- The create_comment handler docstring says replies return the file as item, but operations.create_comment preserves the parent-comment ID/type and Comment.to_dict returns it. The implementation supports the existing self-reference; the docstring is not authority.
