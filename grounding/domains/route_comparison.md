# Box, Calendar and Linear: models and exact route counts

Manually extracted from the implemented replicas at revision
`4691d3f076db2cdcccdc840c110aa797fa3196dc`, following the same
[conceptual modeling protocol](../protocols/conceptual_meta_model.md) as Slack.
This work does not change that protocol, existing cards, coverage catalog or
generation prompts. No experimental LLM, solver or paid API calls were made.

The initial broad audit summaries were insufficiently explicit. The subsequent
[completion audit](modeling_completion_audit.md) records field-level/grouped API
dispositions, concrete reverse checks, diagram corrections and newly documented
interface limitations. It preserved all model and count files unchanged.

## Results

| Domain | Persistence tables reviewed | Conceptual entities | Relationship roles (including self roles) | Structural routes | Routes surviving the direct-read screen | After tagged-target consistency |
|---|---:|---:|---:|---:|---:|---:|
| Slack, existing reference | 15 | 13 | 20 | 2,870 | 212¹ | 212¹ |
| **Box** | 11 | 10 | 29 | **12,398** | **7,146** | **6,500** |
| **Calendar** | 10 | 7 | 10 | **168** | **30** | **30** |
| **Linear** | 59 | 49 | 159 | **989,643,546,920** | **58,820,072,198** | **58,820,072,198** |

¹ Slack's 212 is its existing capability screen, reproduced exactly by the new
counter. Its later ordinary-request inclusion review retained **174** and excluded
38. The new domains have **not** undergone that ordinary-request inclusion review;
none of their numbers is a proposed final coverage denominator comparable to 174.
The new direct-read screens inspect actual projections/field shapes more closely
than Slack's original entity/edge flags. Structural counts use exactly the same
definition across all four domains.

The counts are exact graph counts, not estimates. They include both directions,
preserve distinct relationship roles, forbid repeated entity types, and impose
**no arbitrary depth cutoff**. They exclude direct/terminal attributes, resolution
modes, structured-value paths and derived shortcuts. Excluded self relationships
are still in each domain model. This counting convention consequently leaves out
useful requests involving folder ancestry, event recurrence or repeated entity
types; it is not an enumeration of every possible grounding request.

The longest structural routes contain 8 relationship edges in Box, 5 in Calendar
and 21 in Linear. Full length distributions, excluded roles, model hashes and
counter versions are in each `route_counts.json`.

## Why these are conceptual models rather than table counts

- **Box:** the unique version-owned binary-content storage split is folded into
  FileVersion. File/folder collection membership and tagged hub/comment references
  are included even though they are not foreign keys. No group, enterprise or
  collaboration entity is invented from a JSON value or public Box documentation.
- **Calendar:** user settings become a keyed value collection; synchronization
  tokens and watch transport state are explicitly deferred. Event participants and
  stored reminder records retain their identities. Virtual recurring occurrences
  are derived Event representations. Email-addressed people are not automatically
  equated with local User records.
- **Linear:** nine pair-only association tables become relationships, and the
  unique per-user settings record becomes a value. Attributed/identified links
  remain entities. Minimal implemented records stay minimal: for example, the
  Reaction table has no emoji or reacting-user field, despite the richer public
  GraphQL type. There is one additional interpreted state reference beyond the FK
  graph, validated in `teamUpdate`.

All 80 tables, 1,033 columns, and 278 operation bindings have source inventories
and ledger dispositions. Linear's 207 bindings comprise 57 Query roots, 134
Mutation roots and 16 nested fields. Calendar's 38 operations include its batch
wrapper; the 37 inner aliases reuse the direct handlers. The ledgers record the
dedicated reverse audit and qualifications rather than treating enumeration as
proof of semantic correctness.

## What the read screen means

A retained relationship has a source-backed way to observe its modeled link:
an actual response field, nested record, scoped list, or interpreted reference.
An inverse observation can suffice; a missing convenience endpoint does not
automatically remove a relationship. Read witnesses and exclusions are recorded
in `model.json`; Linear also has a reproducible field-shape ledger.

This is a **screen**, not a claim that every remaining route can be used for an
ordinary, fully discoverable task in every environment. Actor scope, available
attributes, historical versus current views, permissions and predicate semantics
still matter. Exclusion from this screen does not assert that no mutation,
aggregate or partial query could reveal related information.

Specific differences found during extraction:

| Domain | Source-supported qualification |
|---|---|
| Box | Dispatched version and hub-entry projections hide several stored user roles. File metadata exposes a selected version, not a complete version-history endpoint. One HubItem cannot simultaneously have `item_type=file` and `item_type=folder`; removing paths requiring both eliminates a further 646 screened routes. |
| Calendar | Creator/organizer payloads are separate from their local User FKs. `dataOwner` can differ from the Calendar owner FK. API reminders use JSON rather than EventReminder records. Calendar lists/settings are actor-scoped, not a general user-directory traversal. |
| Linear | A declared GraphQL field does not establish a handler. Many ORM lists lack the connection wrapper their SDL type expects. Some roles remain readable through the inverse side; others do not. Stored label-ID caches and association tables can disagree. Publicly declared fields on minimal entities must not be assumed implemented. |

Linear's large number comes from composing numerous distinct roles and connections
through shared entities such as Issue, User, Team, Project and DocumentContent.
It is not caused by multiplying attributes or resolution modes. Some short routes
are ordinary—issues in projects led by Maya, for example—but source-level
connectivity alone cannot establish that the billions of longer combinations
describe useful requests. No such usefulness claim is made here.

## Artifacts

| Domain | Contextualization | Model | Source ledger | Exact counts |
|---|---|---|---|---|
| Box | [context](box/contextualization.md) | [model](box/model.md) | [ledger](box/model_source_ledger.md) | [counts](box/route_counts.json) |
| Calendar | [context](calendar/contextualization.md) | [model](calendar/model.md) | [ledger](calendar/model_source_ledger.md) | [counts](calendar/route_counts.json) |
| Linear | [context](linear/contextualization.md) | [model](linear/model.md) | [ledger](linear/model_source_ledger.md) | [counts](linear/route_counts.json) |

Each domain also contains `source_inventory.json` and the reviewed `model.json`.
Linear's [API surface](linear/api_surface.json) records mapped relationship field
shapes, read reachability, mapped type fields and all declared/bound root fields.

## Verification

- Compared every inventoried table/column, primary key, FK, nullability and
  column-level uniqueness with live SQLAlchemy metadata, without opening a DB.
- Checked model/source accounting, association contractions and relationship IDs.
- Exercised actual serializer and executable GraphQL behavior for the risky
  distinctions above, without service calls.
- Reproduced Slack's 2,870 and 212 exact counts. Compared entire length
  distributions against an independent exhaustive enumerator for Box, Calendar
  and 30 deterministic random multigraphs, including incompatible-edge cases.
- Used compressed exact set counting for Linear rather than enumerating nearly a
  trillion paths. The same mechanism passed those independent checks.

Commands and algorithm details: [modeling tools](../modeling/README.md).
