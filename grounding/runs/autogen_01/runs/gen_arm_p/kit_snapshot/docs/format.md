# scenario.json

One JSON object. The worked examples (`examples/`) show every part.

```json
{
 "scenario_id": "from the brief",
 "domain": "box | calendar | linear | slack",
 "request": "the natural request, without any escape clause",
 "answer": "one | all",
 "seed": [["operation", {"arguments": "..."}], "..."],
 "conditions": [{"id": "c1", "text": "the phrase of the request", "facts": ["catalog fact ids"]}],
 "reference": {
  "name": "what the request acts on, in a few words",
  "target": ["id or @ref"],
  "query": {"the reference query": "..."},
  "decoys": [{"witness": "id or @ref", "fact": "catalog fact id", "family": "F0..F8",
              "substitute": "what it offers instead", "mutation": {"...": "..."},
              "explanation": "one sentence: which condition it fails, and how"}],
  "effect": {"table": "where acting on a record shows", "changes": ["update"]},
  "written": ["table.column the action writes"]
 },
 "other_references": [],
 "write": {"the API call that performs the request on the target": "..."},
 "probes": []
}
```

## Fields
- **`answer`**: `"one"` when the request is about a single record, `"all"` when it acts on every match. For "all",
  `target` lists every matching record.
- **`seed`**: see `seed_ops.md`. Give the target and every decoy a `ref`, or use literal ids.
- **`conditions`**: split the request into the phrases that identify the record. Each condition lists the catalog
  facts it rests on. Every decoy's `fact` must appear in exactly the condition(s) the decoy fails.
- **`reference.query`**: a query over the seed that selects exactly `target` (below).
- **`reference.decoys`**: one entry per decoy. The `mutation` edits the query so that the edited query selects the
  decoy while the original does not. That is the mechanical check that the decoy fails this fact and only this fact.
  `explanation` is read by people and by the judge.
- **`reference.effect`**: where the solver's action shows in the state diff.
  - `table`: the table that changes.
  - `changes`: the change kinds, from `insert`, `update` and `delete`.
  - `field` (optional): when the changed row is not the target itself, the column of that row that holds the
    target's id. For example, a new reaction row names its message in `message_id`, and a new label association
    names its label in `issue_label_id`.
  - `key` (optional): the primary key of the changed table, when it is not `id`.

  Examples:
  - tagging a file: `{"table": "box_files", "changes": ["update"]}`;
  - adding a reaction: `{"table": "message_reactions", "changes": ["insert"], "key": ["message_id", "user_id",
    "reaction_type"], "field": "message_id"}`;
  - adding a label to an issue: `{"table": "issue_label_issue_association", "changes": ["insert"], "key":
    ["issue_id", "issue_label_id"], "field": "issue_id"}`.
- **`other_references`** (optional): other records the request names that the solver must also find, with no
  decoys. Example: the file to add to a hub. Each is `{"name", "target", "query"}`.
- **`write`**: the call a correct solver would make, run once against a fresh copy of your seed to prove the action
  works on the target:
  - Box or Calendar: `{"method": "PUT", "path": "/files/8101", "body": {"tags": ["renewal"]}}` (optional `params`,
    `headers`);
  - Linear: `{"graphql": "mutation { issueUpdate(id: \"i-web-1\", input: {priority: 2}) { success } }"}`;
  - Slack: `{"slack": "reactions.add", "params": {"channel": "C_INC", "timestamp": "@target", "name": "eyes"}}`.
- **`probes`** (optional): extra read calls whose responses show how a decoy differs, in the same form as a Box or
  Calendar read: `["GET", "/files/8101/comments", null]`. For Linear: `["POST", "/graphql", {"query": "{ ... }"}]`.
  The pipeline already reads every seeded record through the normal detail and listing calls.

## The reference query
A query is a tree of **nodes** rooted at the table of the record acted on. A root row matches when every filter on
its node holds, and every edge finds at least one joined row that matches the edge's node, recursively. The filters
of one node all apply to the same row.

```json
{"table": "box_files", "key": ["id"],
 "filters": [{"key": "f_ext", "field": "extension", "op": "eq", "value": "pdf", "fact": "A:File.extension"}],
 "edges": [{"key": "e_owner", "join": {"parent": "owned_by_id", "child": "id", "op": "eq"}, "fact": "R:File.owned_by_id",
            "node": {"table": "box_users", "filters": [{"key": "f_owner", "field": "name", "op": "eq", "value": "Maya Chen"}],
                     "edges": []}}]}
```

- **`key`**: the root table's primary key; you may omit it. It is `["id"]` for Box, Calendar and Linear tables.
  Slack tables use their own keys: `user_id` for users, `channel_id` for channels, `message_id` for messages.
- **Filter**: `{"key", "field", "op", "value", "fact"?}`.
  - `key` must be unique in the query; mutations refer to it.
  - `field` is a column; a dotted path reads into a JSON column (`"start.dateTime"`).
  - `op` is one of:
    - `eq`, `ne`;
    - `in`, `not_in` (the value is a list);
    - `contains_ci`, `not_contains_ci` (case-insensitive substring);
    - `json_has` (a JSON list column holds the value);
    - `lt`, `le`, `gt`, `ge` (numbers, or ISO times compared as instants);
    - `is_null`, `not_null` (no value).
- **Edge**: `{"key", "join": {"parent", "child", "op"}, "node", "fact"?, "closure"?, "count"?, "negate"?}`.
  - The join compares a column of this node's row (`parent`) with a column of the child table (`child`) using
    `op`:
    - `eq`;
    - `json_contains`: the parent's JSON list holds the child's value, as in a folder's `collections` holding a
      collection id;
    - `json_in`: the child's JSON list holds the parent's value.
  - `closure: true` follows the join repeatedly through the same table (one or more steps); `"star"` also includes
    the row itself (zero or more steps).
  - `count: {"op": "eq", "value": 2}` counts the matching child rows instead of requiring one.
  - `negate: true` requires that no child row matches.
- **`fact`** on a filter or an edge records which catalog fact it realizes. It is used in reports only.
- **`argmax` / `argmin`** (optional, on the root): a column. Only the matching rows with the largest or smallest
  value are kept ("the latest …").

## Mutations
A decoy's mutation turns the query into one that selects the decoy. The check requires two things: the mutated
query selects the witness, and the original does not.
- **`{"type": "DROP", "target": "f_ext"}`**: remove one filter. Or drop an edge's join, so that any row of that
  table meeting the node's conditions will do, related or not.
- **`{"type": "SUB", "target": "e_owner", "replacement": {…an edge…}}`**: replace an edge. This is how an F1
  sibling role is written (`created_by_id` for `owned_by_id`). The replacement keeps the same `key`.
- **`{"type": "SPLIT", "target": "e_att", "groups": [["f_att"], ["f_rsvp"]]}`**: the edge's node conditions may be
  met by different child rows (F5).
- **`{"type": "LEVEL", "target": "e_parent", "closure": true}`**: toggle an edge's closure (F4).
- **`{"type": "REPLACE", "query": {…a full query…}, "note": "…"}`**: an explicit alternative query. Use it when
  the substitute changes the query's shape: F2, F3 or F6 decoys, a derived view, or a count condition dropped.

Every witness must be different, and every decoy's mutation must be killed by its witness. If the check reports
"not killed", either the decoy also meets the original query (it is not a near miss), or the mutation does not
select it (it fails more than this one fact).
