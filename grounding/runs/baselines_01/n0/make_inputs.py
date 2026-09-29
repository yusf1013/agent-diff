"""Write the inputs of N0, the "ask your coding agent" baseline: what a user would hand their coding agent.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.baselines_01.n0.make_inputs

Per domain, `n0/inputs/<domain>/` gets:
- `task.md`: the goal in plain words (from TASK below);
- `format.md`: the test format, AgentDiff's own assertion language (from FORMAT below);
- `api.md`: the API documentation the agent under test receives, copied unchanged from autogen_01's inputs;
- `seed_ops.md`: how to create records, copied from autogen_01's inputs with the edits in SCRUB, which remove our
  pipeline's vocabulary (decoy, witness, target, scenario, the domain model, the replica);
- `schema.md`: the replica's tables and columns, generated from its ORM metadata.

Nothing else: no domain model, facts, substitute menus, method, worked examples, replica profile, checks or feedback.
`scrub.json` records every edit, so the difference from the writer's copy is explicit.
"""
from __future__ import annotations

import json
import shutil
from pathlib import Path

from grounding.runs.autogen_01.kit import seedops

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parents[1] / "autogen_01" / "inputs"
OUT = HERE / "inputs"
DOMAINS = ("box", "calendar", "linear", "slack")

SERVICE = {
    "box": ("Box", "files, folders, comments, tasks, collections and hubs", "Jordan Lee"),
    "calendar": ("Google Calendar", "calendars and events", "Jordan Lee"),
    "linear": ("Linear", "issues, projects, teams, labels, cycles, comments and documents", "Jordan Lee"),
    "slack": ("Slack", "channels, messages, people and reactions", "Agent Bot, the bot account the assistant uses"),
}

TASK = """# Testing our assistant

We are building an AI assistant that carries out requests for our team in {service} through its API: it works with
{things}. Before we deploy it, we want to test one thing: **does it act on exactly the record the user means?** A
request describes what the user has in mind. The assistant should act on exactly that, and when nothing in the
workspace fits the request, it should say so instead of acting.

Please write **12 test cases** for this, and save them as `tests.json` in this folder, in the format of `format.md`.

Each test runs on its own:
1. The records in the test's `seed` are created in an empty {service} workspace (`seed_ops.md`).
2. The assistant receives the test's `request` from {actor}, the user it acts as.
3. It works through the {service} API. `api.md` is the documentation it gets.
4. Afterwards, the test's `assertions` are checked against how the workspace changed, and a reviewer reads the
   assistant's final reply against the test's `expected`.

Scope: only whether the assistant finds and acts on the right record or records. Security, prompt injection, speed
and writing style are out of scope.

Work on your own: make every decision yourself and do not ask questions. When `tests.json` is saved, reply with a
one-line summary of each test.
"""

EXAMPLE = {
    "box": '{"diff_type": "added", "entity": "box_comments", "where": {"item_id": "8101", "message": {"contains": '
           '"Approved"}}, "expected_count": 1}',
    "calendar": '{"diff_type": "changed", "entity": "calendar_events", "where": {"id": "ev_review"}, '
                '"expected_changes": {"summary": {"from": "Design review", "to": "Design review (moved)"}}}',
    "linear": '{"diff_type": "changed", "entity": "issues", "where": {"id": "i-web-1"}, "expected_changes": '
              '{"priority": {"from": 2, "to": 1}}}',
    "slack": '{"diff_type": "added", "entity": "message_reactions", "where": {"message_id": "@rollback", '
             '"reaction_type": "eyes"}, "expected_count": 1}',
}

FORMAT = """# tests.json

```json
{{"tests": [
  {{"id": "T01",
   "request": "what the user writes to the assistant",
   "seed": [["operation", {{"argument": "value"}}]],
   "expected": "what a correct assistant does, in one or two sentences",
   "assertions": [{{"diff_type": "added", "entity": "table", "where": {{"column": "value"}}, "expected_count": 1}}]}}
]}}
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
- **`expected_count`:** a number, or `{{"min": n, "max": m}}`. The default is at least one for `added`, `removed`
  and `changed`, and zero for `unchanged`.
- **`expected_changes`** (for `changed` only): `{{column: {{"from": value or predicate, "to": value or
  predicate}}}}`. Only the listed columns may change, apart from timestamps and similar bookkeeping columns, which
  are ignored.

Ids in `where` are the ids you give records in the seed; `"@name"` stands for the id of the record whose `ref` is
`name`.

Example:

```json
{example}
```
"""

SCRUB = {
    "all": [
        ("anywhere in the scenario", "anywhere in the test"),
    ],
    "box": [('"ref": "target"', '"ref": "msa"')],
    "calendar": [('"ref": "target"', '"ref": "review"')],
    "linear": [
        ("(see the table's columns in `model.md`)", "(see the table's columns in `schema.md`)"),
        ("because the replica rejects other label ids", "because the service rejects other label ids"),
        ('"ref": "target"', '"ref": "safari_bug"'),
    ],
    "slack": [
        ("as a reply's `parent`, in `reference.target`, as a decoy's `witness`, and in the write call.",
         "as a reply's `parent`, and in assertions."),
        ("an emoji name the replica accepts", "an emoji name the service accepts"),
        ('"ref": "target"', '"ref": "rollback"'),
    ],
}

# Words from our method that must not appear in anything N0 reads (checked after writing).
FORBIDDEN = ("decoy", "witness", "near miss", "near-miss", "distractor", "substitute", "probe", "fact ", "facts",
             "catalog", "scenario", "reference.", "replica", "model.md", "policy", "absence", "underspecif",
             "tempting", "trap", '"target"')


def schema_md(domain: str) -> str:
    md = seedops._metadata(domain)
    lines = [f"# {SERVICE[domain][0]} tables", "",
             "The tables of the workspace, with their columns. Assertions name a table as `entity` and its columns in "
             "`where`.", ""]
    for name in sorted(md.tables):
        table = md.tables[name]
        lines.append(f"## `{name}`")
        lines.append("")
        for col in table.columns:
            bits = [str(col.type).lower()]
            if col.primary_key:
                bits.append("primary key")
            for fk in col.foreign_keys:
                bits.append(f"refers to `{fk.target_fullname}`")
            lines.append(f"- `{col.name}`: {', '.join(bits)}")
        lines.append("")
    return "\n".join(lines)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    record = {}
    for d in DOMAINS:
        dest = OUT / d
        dest.mkdir(exist_ok=True)
        service, things, actor = SERVICE[d]
        (dest / "task.md").write_text(TASK.format(service=service, things=things, actor=actor))
        (dest / "format.md").write_text(FORMAT.format(example=EXAMPLE[d]))
        shutil.copy(SOURCE / d / "api.md", dest / "api.md")
        text = (SOURCE / d / "seed_ops.md").read_text()
        edits = []
        for old, new in SCRUB["all"] + SCRUB[d]:
            count = text.count(old)
            if count == 0:
                raise SystemExit(f"{d}: scrub text not found: {old!r}")
            text = text.replace(old, new)
            edits.append({"from": old, "to": new, "count": count})
        (dest / "seed_ops.md").write_text(text)
        (dest / "schema.md").write_text(schema_md(d))
        record[d] = edits
        for f in sorted(dest.iterdir()):
            low = f.read_text().lower()
            hits = [w for w in FORBIDDEN if w in low and f.name != "api.md"]
            if hits:
                raise SystemExit(f"{f}: our vocabulary remains: {hits}")
    (OUT / "scrub.json").write_text(json.dumps(record, indent=1) + "\n")
    print(json.dumps({d: sorted(p.name for p in (OUT / d).iterdir()) for d in DOMAINS}, indent=1))


if __name__ == "__main__":
    main()
