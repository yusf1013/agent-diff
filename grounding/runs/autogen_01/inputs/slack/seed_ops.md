# Slack seed operations

A seed is a list of `[operation, {arguments}]`. Every operation also accepts:
- `"ref": "name"`, so that `"@name"` stands for the created row's id anywhere in the scenario;
- `"set": {column: value}`, for extra columns of the created row.

**Messages get computed ids** (their `ts`). Always give a message a `ref`, and use `"@ref"` wherever you need its
id: as a reply's `parent`, in `reference.target`, as a decoy's `witness`, and in the write call.

## Already present
- **The workspace** Northwind (team `T1`).
- **The actor**, a bot user `U01AGENBOT9` ("Agent Bot"), a member of every channel you create.
- **People** (key → name; id `U_<KEY>`, username `first.last`, display name the first name): `priya` Priya Sharma,
  `diego` Diego Alvarez, `leo` Leo Park, `omar` Omar Haddad, `aisha` Aisha Khan, `maya` Maya Chen.

## Operations
| Operation | Arguments (defaults) | Creates |
|---|---|---|
| `person` | `key`, `name`, `username` (from the name), `display` (first name), `bot` (false), `role` (workspace role: "member", "admin", "owner") | a user (id `U_<KEY>`); use `set` for `email`, `title`, `timezone`, `is_active` |
| `channel` | `id` (for example "C_INC"), `name` (without #), `members` (person keys; the actor is always added), `private` (false), `topic` (""), `purpose` (""), `gc` (false) | a channel with its members; use `set` for `is_archived` or `created_at` |
| `dm` | `id`, `person` | a direct-message conversation between the actor and that person |
| `message` | `channel`, `author`, `text`, `at` (an ISO UTC instant such as "2026-09-21T14:06:00Z"; it also fixes the ts), `parent` ("@ref" of the thread root, for a reply), `mentions` ([] of person keys) | a message |
| `reaction` | `message` ("@ref"), `person`, `name` (an emoji name the replica accepts), `at` | a reaction on a message |
| `row` | `table`, `values` | any other row; required columns you leave out get neutral defaults |

Keep every message's instant on the same calendar day in all time zones from UTC-11 to UTC+11 when the day matters
(for example between 11:00 and 13:00 UTC), so that the day the agent computes from `ts` does not depend on its time
zone, unless the time zone is what you test.

## Example
```json
[["channel", {"id": "C_INC", "name": "incidents", "members": ["diego", "leo"]}],
 ["message", {"channel": "C_INC", "author": "leo", "text": "Checkout outage: 502s on /pay since 14:05 UTC.",
              "at": "2026-09-21T14:06:00Z", "ref": "root"}],
 ["message", {"channel": "C_INC", "author": "diego", "text": "Rolled back the gateway config.",
              "at": "2026-09-21T14:20:00Z", "parent": "@root", "ref": "target"}]]
```
