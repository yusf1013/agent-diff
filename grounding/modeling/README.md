# Reproducing the domain models and route counts

The conceptual decisions are manual research annotations in each domain's
`model.json`. The tools inventory source, render those decisions, check accounting,
and count routes. They do **not** infer a conceptual model from tables or certify
natural-language request validity.

Start with [the comparison](../domains/route_comparison.md), then the relevant
domain's contextualization, model and source ledger. The adopted
[modeling protocol](../protocols/conceptual_meta_model.md) remains unchanged.

## Source inventory and projection

Use the repository's Python 3.14 environment because Box source uses syntax that
older parsers reject. From the repository root, for each of `box`, `calendar`,
and `linear`:

```bash
backend/.venv/bin/python -m grounding.modeling.inventory box --out grounding/domains/box/source_inventory.json
python -m grounding.modeling.render box
```

Linear also records the ORM/GraphQL relationship surface, mapped type fields and
declared/bound root operations:

```bash
PYTHONPATH=backend backend/.venv/bin/python -m grounding.modeling.linear_surface
```

Regeneration of an inventory after source changes is **not** approval of the old
model. Review new/changed source using the protocol, update manual decisions, and
repeat the reverse audit before claiming refreshed counts.

The explicit audit annotations are in each domain's `model_audit.json`; `render`
projects them into the existing source ledger. They map every operation to
reviewed API field groups and record concrete reverse checks and qualifications.
The structural `model.json` and reported counts are frozen by
`audit_baseline.json` for this completion pass: changing them requires discussion
with the user. Field-accounting artifacts are evidence, not extra model fields.

For Linear, reproduce the exhaustive disposition index for fields declared on
mapped GraphQL types with:

```bash
PYTHONPATH=backend backend/.venv/bin/python -m grounding.modeling.linear_field_accounting
```

The completed checks and newly recorded limitations are summarized in
[the completion audit](../domains/modeling_completion_audit.md).

## Offline checks

```bash
DATABASE_URL=sqlite:// PYTHONPATH=backend backend/.venv/bin/python -m grounding.modeling.verify
```

The Calendar import requires a database URL. This command constructs an unused
in-memory engine; it opens no application database, creates no tables, and makes
no service/model calls. It checks live SQLAlchemy metadata against the declaration
inventory, field/relationship accounting, and risky serializer/GraphQL shapes.

## Exact route counts

The structural definition matches Slack's existing route probe:

- Each nonempty path is counted in both directions.
- Parallel edges with different relationship roles remain distinct.
- An entity **type** cannot repeat in a path. Self relationships are therefore
  excluded, even when an ordinary hierarchy/recurrence request would use them.
- Attributes, resolution modes, derived shortcuts and structured-value paths are
  not multiplied into these counts.

For small graphs the independent exhaustive enumerator needs only Python:

```bash
python -m grounding.modeling.routes grounding/domains/box/model.json --method dfs
```

Linear is too large to materialize the paths. Install `graphillion==2.1` in a
separate Python 3.13 environment (the run used
`/tmp/grounding-route-count-venv`), then run:

```bash
OMP_NUM_THREADS=1 /tmp/grounding-route-count-venv/bin/python -m grounding.modeling.verify_routes
OMP_NUM_THREADS=1 /tmp/grounding-route-count-venv/bin/python -m grounding.modeling.routes grounding/domains/linear/model.json --out grounding/domains/linear/route_counts.json
```

Run the second command for Box and Calendar too. Graphillion represents the exact
path set as a compressed decision diagram; this is neither sampling nor a depth
cutoff. Each relationship is subdivided using a unique auxiliary vertex to retain
parallel roles, and auxiliary vertices must have degree zero or two so they cannot
be endpoints. Multiply undirected nonempty paths by two. Box additionally excludes
paths requiring the same HubItem to have both the file and folder tag.

`verify_routes` compares full length histograms against independent DFS for Slack
(2,870 full / 212 screened), Box, Calendar, and 30 deterministic random multigraphs
with and without incompatible-edge exclusions. This validates the counting
mechanism; the manual model still determines what should be counted.

The direct-read screen uses reviewed `read_witnesses`. It does not certify that
every attribute is exposed, arbitrary populations are discoverable, permissions
allow the task, or a route describes ordinary work. Empty witnesses mean excluded
from this particular read screen, not proof that no mutation/aggregate/partial
observation can reveal related information. No ordinary-use inclusion decisions
are inferred by these scripts.
