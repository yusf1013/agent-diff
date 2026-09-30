# Linear seed operations

A seed is a list of `[operation, {arguments}]`. Every operation also accepts:
- `"ref": "name"`, so that `"@name"` stands for the created row's id anywhere in the test;
- `"set": {column: value}`, for extra columns of the created row (see the table's columns in `schema.md`).

Ids are short strings you choose, such as `"t-web"` or `"i-web-3"`, except labels: **label ids must be UUIDs**,
because the service rejects other label ids. Omit a label's id (one is generated) and give it a `ref`.

## Already present
- **The organization** Northwind.
- **People** (key → name; id `u-<key>`, email `first.last@northwind.example`, displayName the lowercase first name):
  `actor` Jordan Lee (the acting user, id `u-actor`), `maya` Maya Chen, `priya` Priya Nair, `leo` Leo Park, `sam`
  Sam Rivera, `dana` Dana Whitfield, `omar` Omar Haddad.

## Operations
| Operation | Arguments (defaults) | Creates |
|---|---|---|
| `person` | `key`, `name`, plus any users column (`email`, `displayName`, `guest`, `admin`, `active`, `timezone`, `statusLabel`, `app`, …) | a user (id `u-<key>`) |
| `team` | `id`, `name`, `key` (for example "WEB"), `parent` (a team id) | a team with the six workflow states Backlog, Todo, In Progress, In Review, Done, Canceled |
| `member` | `team`, `person`, `owner` (false) | a team membership |
| `label` | `name`, `id` (a UUID, or omit), `team` (null = workspace label), `parent` (a group label's id), `group` (false: true makes it a label group) | an issue label |
| `issue` | `id`, `team`, `title`, `state` ("Todo"), `assignee`, `creator` ("actor"), `priority` (0 none, 1 urgent, 2 high, 3 medium, 4 low), `estimate`, `due` (a date such as "2026-09-30"), `project`, `milestone`, `cycle`, `parent` (an issue id), `labels` ([] of label ids), `description` (""), `created` (2026-06-01T09:00:00), `subscribers` ([] of person keys), `number` (next in the team) | an issue, identifier `<KEY>-<number>` |
| `status` | `id`, `name`, `type` ("backlog", "planned", "started", "paused", "completed", "canceled"), `position` | a project status |
| `project` | `id`, `name`, `lead`, `creator` ("actor"), `status`, `state` ("started"), `start`, `target` (dates), `priority` (0-4), `description` | a project |
| `milestone` | `id`, `project`, `name`, `target` (a date), `status` ("unstarted", "next", "overdue", "done") | a project milestone |
| `cycle` | `id`, `team`, `number`, `starts`, `ends` (ISO times), `active`, `next`, `past`, `future`, `previous` (flags) | a cycle named "Cycle <number>" |
| `comment` | `id`, `issue`, `author`, `body`, `parent` (a comment id, for a reply), `resolver` (a person key; marks the thread resolved), `created`, `resolved` (ISO times) | a comment |
| `relation` | `id`, `issue`, `related`, `type` ("blocks", "related", "duplicate"; `issue` blocks `related`) | an issue relation |
| `attachment` | `id`, `issue`, `title`, `url`, `creator` ("actor"), `source` ("api") | an attachment |
| `initiative` | `id`, `name`, `owner`, `creator` ("actor"), `status` ("Planned", "Active", "Completed") | an initiative |
| `document` | `id`, `title`, `creator` ("actor"), `updater` (creator), `project`, `initiative`, `team`, `content` | a document |
| `row` | `table`, `values` | any other row (for example `notifications`, `organization_invites`, `project_relations`, `initiative_to_projects`); required columns you leave out get neutral defaults |

People arguments (`assignee`, `creator`, `author`, `lead`, …) take a person key.

## Example
```json
[["team", {"id": "t-web", "name": "Web", "key": "WEB"}],
 ["member", {"team": "t-web", "person": "maya"}],
 ["label", {"name": "Bug", "team": "t-web", "ref": "bug"}],
 ["issue", {"id": "i-web-1", "team": "t-web", "title": "Checkout button unresponsive on Safari",
            "assignee": "maya", "priority": 2, "labels": ["@bug"], "ref": "safari_bug"}]]
```
