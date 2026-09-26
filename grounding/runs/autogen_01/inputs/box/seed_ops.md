# Box seed operations

A seed is a list of `[operation, {arguments}]`. Every operation also accepts:
- `"ref": "name"`, so that `"@name"` stands for the created row's id anywhere in the scenario;
- `"set": {column: value}`, for extra columns of the created row.

Ids are strings of digits. Choose them yourself and keep them unique, for example `"8101"`.

## Already present
- **People** (key → name, login `first.last@northwind.example`): `JL` Jordan Lee (the actor, id `30000000001`),
  `MC` Maya Chen, `ML` Maya Lopez, `LP` Leo Park, `DW` Dana Whitfield, `PN` Priya Nair, `OH` Omar Haddad,
  `SR` Sam Rivera.
- **The root folder** `"0"` (All Files).

## Operations
| Operation | Arguments (defaults) | Creates |
|---|---|---|
| `person` | `key`, `name`, `login` (from the name), `id` (next free) | a user; refer to them by `key` afterwards |
| `folder` | `id`, `name`, `parent` ("0"), `owner` ("JL"), `creator` (owner), `modifier` (creator), `description` (""), `tags` ([]), `collections` ([] of collection ids), `created`, `modified` (ISO times, default 2026-06-01T09:00:00+00:00), `size` (0), `shared` (false, or an access level such as "company" or "open") | a folder |
| `file` | `id`, `name` (the extension comes from the name), `parent`, `owner` ("JL"), `creator` (owner), `modifier` (creator), `description` (""), `tags` ([]), `collections` ([]), `version` (1), `shared` (false or an access level), `locked` (false), `uploader` (modifier), `created`, `modified`, `size` (48213 bytes) | a file and its current version |
| `comment` | `id`, `file`, `author`, `message`, `reply_to` (a comment id, for a reply), `created` (2026-06-10T15:00:00+00:00) | a comment on a file (and the file's comment count) |
| `task` | `id`, `file`, `creator`, `message`, `action` ("review" or "complete"), `done` (false), `due` (null), `created` | a task on a file |
| `assign` | `id`, `task`, `to`, `by`, `state` ("incomplete"; also "completed", "approved", "rejected") | a task assignment |
| `collection` | `id`, `name` ("Favorites"), `collection_type` ("favorites") | the actor's collection; put items in it with their `collections` argument |
| `hub` | `id`, `title`, `creator` ("JL"), `updater` (creator), `description` ("<title> materials"), `created`, `updated` | a hub |
| `hub_item` | `id`, `hub`, `item` (a file or folder id), `item_type` ("file" or "folder"), `added_by` ("JL"), `position` (1) | an item in a hub |
| `row` | `table`, `values` | any other row; required columns you leave out get neutral defaults |

People arguments (`owner`, `creator`, `author`, `to`, …) take a person key.

## Example
```json
[["folder", {"id": "8100", "name": "Contracts"}],
 ["file", {"id": "8101", "name": "Initech MSA.pdf", "parent": "8100", "owner": "JL",
           "description": "Initech renewal terms for 2027", "size": 3400000, "ref": "target"}],
 ["comment", {"id": "81010", "file": "8101", "author": "PN", "message": "Reviewed section 1."}]]
```
