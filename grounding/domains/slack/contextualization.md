# Slack contextualization

Apply [the generic meta-model](../../protocols/conceptual_meta_model.md) with the source locations
and clarifications below. This records contextualization only; it is neither the
conceptual model nor its coverage ledger. The generic file is unchanged.

Scope: the Slack replica defined by repository revision
`920abcedd8a5ef071892dd1177aab17fe909a36d`. This inspection concerns source code,
not verification of a deployed database or running service.

## 1. Source instructions

These instructions locate and bound the inputs. They do not add mapping rules.

| Input | Source and extraction entry point |
|---|---|
| Database | [schema.py](../../../backend/src/services/slack/database/schema.py) defines the tables, fields, constraints, and enums using the service's [Base](../../../backend/src/services/slack/database/base.py). [seed_slack_template.py](../../../backend/utils/seed_slack_template.py), specifically `create_tables`, creates tables from that metadata. |
| API implementation | [main.py](../../../backend/src/platform/api/main.py) mounts the Slack router. In [methods.py](../../../backend/src/services/slack/api/methods.py), follow `routes` → `slack_endpoint` → `SLACK_HANDLERS` → handler and called helpers. Follow both direct ORM access and calls into [operations.py](../../../backend/src/services/slack/database/operations.py). |
| API documentation | [slack_api_full_docs.json](../../../examples/slack/testsuites/slack_docs/slack_api_full_docs.json) supplies method descriptions, request parameters, and request examples. Use it to interpret identifiers, conversation terminology, and structured inputs. It contains no response schemas; derive response meaning from handlers and serializers. |

Database definition checks also include the Slack migrations for
[bot status](../../../backend/src/platform/db/migrations/versions/b49e93fd90ec_slack_users_is_bot.py),
[message blocks](../../../backend/src/platform/db/migrations/versions/c8f3a2b1d9e4_slack_messages_blocks.py),
and [reaction keys](../../../backend/src/platform/db/migrations/versions/d1a2b3c4e5f6_slack_message_reactions_pk.py).
Their forward definitions agree with the corresponding current ORM constructs.
These are part of the database input, not an additional authority.

| Instruction | What would otherwise be missed or ambiguous? |
|---|---|
| Enumerate database tables from the full service metadata, not the seeder's `TABLE_ORDER` or populated records. | The schema defines 15 tables; the seed insertion list contains only seven. Seed-only extraction would omit implemented persistence structures. Lack of API use does not remove a table from database coverage or establish support for manipulating it. |
| Enumerate API operations from `SLACK_HANDLERS`, accounting for both route forms as entry aliases. | Two generic routes dispatch 27 named operations. Counting route declarations would undercount operations. The service [README](../../../backend/src/services/slack/README.md) also omits `auth.test` and `search.all`. |
| Trace shared serializers and request context as part of each operation's implementation. | `_serialize_conversation` and `_serialize_user` derive domain-bearing fields. `_principal_user_id` obtains the actor through request state populated by [IsolationMiddleware](../../../backend/src/platform/api/middleware.py). Handler bodies and database operations alone do not explain those representations. Platform environment management remains outside the Slack conceptual model. |

The documentation's 27 method keys match the dispatcher, but matching names do not
establish parameter or capability parity. For example, the documented `search.all`
description includes files, whereas its handler returns fixed empty file and post
results. Retain the generic rule that implementation takes precedence.

## 2. Candidate mapping additions

The existing database mapping rows cover the relational constructs encountered;
no additional relational category is needed. These two candidates make distinctions
that the generic tables leave implicit. Apply them for the Slack extraction while
keeping the generic file unchanged.

| Construct encountered | Mapping instruction | Why needed |
|---|---|---|
| Structured JSON in `Message.blocks` | Treat it as a structured attribute. Follow `_validate_blocks`, its validators, and `_blocks_to_mrkdwn` / `_element_to_mrkdwn` for meaningful nested types and references. Group uninterpreted content; do not invent entities for every JSON key or imply foreign-key enforcement for embedded references. | A single opaque-column mapping would hide classifications and user/channel references interpreted by the implementation. |
| Request values echoed without persistence | Identify their transient representation and defer operation-specific handling to the behavior model. In `chat_post_message`, attachments are returned but are not passed to `send_message`; blocks are persisted. | Receiving and returning a value does not establish a stored attribute or relationship. |

## 3. Existing mappings clarified

These findings guide application of existing identity, derived-information, and
constant-value mappings; they require no new mapping category.

| Construct encountered | Mapping instruction | Why needed |
|---|---|---|
| API names that differ from storage names | Trace values to their source before assigning identity or relationships. `chat_post_message` maps `thread_ts` to `parent_id` and returns `message_id` as `ts`; the schema also has a separate `ts` column. | Matching field names alone would attach API identity to the wrong stored field. |
| Serializer defaults, derivations, and placeholders | Trace their provenance, including actor-dependent values. Apply the existing derived/constant rules instead of inferring independent domain state. | Fields such as conversation `creator`, user avatar URLs, and empty search result categories can suggest stored facts or capabilities that their implementations do not provide. |

## 4. Application to the next stage

Use the generic ledger and conceptual-model sections without adding new sections
or disposition types. Identify database sources by class/field/constraint and API
sources by dispatch key plus handler/helper and relevant payload field. Shared
evidence can be recorded once and referenced by the operations that use it.

The generic stopping condition applies to the full database definitions and named
dispatch operations established above. Contextualization has identified how to
inspect them and the representation distinctions to preserve; complete element
coverage remains the work of the subsequent extraction and ledger.
