# tests.json

```json
{"tests": [
  {"id": "T01",
   "request": "what the user writes to the assistant",
   "seed": [["operation", {"argument": "value"}]],
   "expected": "what a correct assistant does, in one or two sentences",
   "assertions": [{"diff_type": "added", "entity": "table", "where": {"column": "value"}, "expected_count": 1}]}
]}
```

- **`id`:** `T01` to `T12`.
- **`request`:** in the user's own words. It is all the assistant receives.
- **`seed`:** operations from `seed_ops.md`. Every test has its own seed, and tests share nothing.
- **`expected`:** read by a reviewer, together with the assistant's final reply and what it did.
- **`assertions`:** checked automatically against the rows that were added, removed or changed during the run. The
  test passes only if every assertion holds.

## Assertions

An assertion selects the rows of one table that changed in a given way:
- **`diff_type`:** `"added"`, `"removed"`, `"changed"` or `"unchanged"`.
- **`entity`:** the table (`schema.md`).
- **`where`:** predicates on columns; a bare value means equality. Predicates: `eq`, `ne`, `in`, `not_in`,
  `contains`, `not_contains`, `i_contains`, `starts_with`, `ends_with`, `i_starts_with`, `i_ends_with`, `regex`,
  `gt`, `gte`, `lt`, `lte`, `exists` (true or false), `has_any` and `has_all` (for lists).
- **`expected_count`:** a number, or `{"min": n, "max": m}`. The default is at least one for `added`, `removed`
  and `changed`, and zero for `unchanged`.
- **`expected_changes`** (for `changed` only): `{column: {"from": value or predicate, "to": value or
  predicate}}`. Only the listed columns may change, apart from timestamps and similar bookkeeping columns, which
  are ignored.

Ids in `where` are the ids you give records in the seed; `"@name"` stands for the id of the record whose `ref` is
`name`.

Example:

```json
{"diff_type": "added", "entity": "box_comments", "where": {"item_id": "8101", "message": {"contains": "Approved"}}, "expected_count": 1}
```
