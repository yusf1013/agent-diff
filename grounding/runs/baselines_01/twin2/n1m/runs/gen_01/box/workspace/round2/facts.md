# Facts to test

Together, your tests must check the assistant on each fact below: for every fact, at least one test in which that
fact decides which record is the right one.

The kinds of fact:
- **attribute:** an identifying attribute of a record (identity, text, time, quantity, state);
- **relationship:** a record's related person or record in a given role (a foreign-key role, an association);
- **hierarchy:** a level of a hierarchy or a self-relationship (a parent, a reply's parent);
- **binding:** several conditions that must hold on the same related record, across a to-many relationship;
- **derived value:** a value computed from records (a count, the latest one, a local date, the primary calendar).

| Fact | Kind | Rests on |
|---|---|---|
| `A:File.modified_at` | attribute | `box_files.modified_at` |
| `A:File.shared_link` | attribute | `box_files.shared_link` |
| `A:File.uploader_display_name` | attribute | `box_files.uploader_display_name` |
| `A:TaskAssignment.resolution_state` | attribute | `box_task_assignments.resolution_state` |
| `A:User.name` | attribute | `box_users.name` |
| `B:Comment.file_id` | binding | `Comment.file_id` |
| `B:HubItem.hub_id` | binding | `HubItem.hub_id` |
| `B:TaskAssignment.task_id` | binding | `TaskAssignment.task_id` |
| `H:Comment.item_id:comment` | hierarchy | `Comment.item_id:comment` |
| `H:Folder.parent_id` | hierarchy | `Folder.parent_id` |
| `R:Folder.created_by_id` | relationship | `Folder.created_by_id` |
| `R:Folder.owned_by_id` | relationship | `Folder.owned_by_id` |
| `R:Hub.created_by_id` | relationship | `Hub.created_by_id` |
| `R:HubItem.folder` | relationship | `HubItem.folder` |
| `R:TaskAssignment.assigned_by_id` | relationship | `TaskAssignment.assigned_by_id` |
| `R:TaskAssignment.assigned_to_id` | relationship | `TaskAssignment.assigned_to_id` |
