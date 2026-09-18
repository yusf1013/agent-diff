# Box evidence-to-interface map

Use [sources.json](sources.json) for exact local sources and documentation pages. This is a vocabulary map, not an ER model or implementation claim.

| Seed/card vocabulary | Documented API projection or input |
|---|---|
| `box_users.id`, `.name`, `.login` | Authenticated user details from `GET /users/me`; the actor is supplied context. |
| `box_folders.id`, `.name`, `.description`, `.parent_id` | Folder `id`, `name`, `description`, and `parent.id`; parent relationships/path collections support folder ancestry. Root handle is 0. |
| `box_files.id`, `.name`, `.extension`, `.size`, `.parent_id` | File details/search/listing; filename/extension, byte size, parent and path collection. |
| `box_files.content` | Analytical name for downloaded file bytes from `GET /files/{file_id}/content` and uploaded content. Not a new seed database column. `box_file_versions.local_path` locates the allowed initial-state bytes for the annotator; it is not a solver identifying attribute. |
| `box_files.description`, `.tags`, `.shared_link`, `.collections`; `box_folders.tags` | Documented file/folder metadata inputs/projections; some do not occur in the initial JSON. Omission is not proof of a runtime default. |
| `box_files.item_status`, `box_folders.item_status` | Trash state is represented by `item_status`; Box deletions here are task-directed transitions to trashed, not assumed physical row removal. |
| `box_comments.id`, `.message`, `.item_id` | Comments use `id`, text `message`, and `item.id`; file-comment listing supplies the relation. Update/delete operations have official documentation beyond the local extract. |
| `box_tasks.id`, `.message`, `.item_id`, `.is_completed` | Seed task identity, text, linked file, and completion state. Completion is a task requirement recorded in native seed vocabulary; the current assertions do not check the resonance task. No claim that a task-update request directly accepts `is_completed`. |
| `box_hubs.id`, `.title`, `.description` | Hub listing/details/update fields in the local API extract. |
| `box_hub_items.item_id`, `.hub_id` | Hub-item membership references supplied to the documented manage-items operation. The initial hub-items collection is empty. |
| `box_collections.id`, `.name` | Collection listing identifies Favorites; file collections provide related membership where available. |

All card computation fields are local contributions. For file import/version updates, bytes are meaningful written content; automatically incremented version numbers are assertion evidence, not task-written attributes. For example, `box_148` grounds an existing file whose new version is checked by identity, but the assertion does not validate the appended content.
