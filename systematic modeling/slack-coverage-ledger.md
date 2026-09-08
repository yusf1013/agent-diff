# Slack conceptual coverage ledger

Revision: `920abcedd8a5ef071892dd1177aab17fe909a36d`. Model destinations refer to
[slack-conceptual-model.md](slack-conceptual-model.md). This is source coverage;
no live database or HTTP integration verification is claimed.

Source shorthand: **DB** = [schema.py](../backend/src/services/slack/database/schema.py),
**API** = [methods.py](../backend/src/services/slack/api/methods.py),
**OPS** = [operations.py](../backend/src/services/slack/database/operations.py),
**DOC** = [local API documentation](../examples/slack/testsuites/slack_docs/slack_api_full_docs.json).
Class, function, dispatch key, and field names below locate evidence within these
files. Dispositions are **represented**, **derived**, **deferred**, or **omitted**;
each row identifies the relevant treatment explicitly.

## Database coverage

All stored fields are listed, grouped by common interpretation. IDs and foreign
keys map to model identities and diagram edges; `?` nullability is preserved in the
model. Datatype lengths, defaults, and ORM deletion behavior are deferred to action
validation/lifecycle contracts where relevant; they do not create new entities.

| ID | DB source and fields | Disposition and destination / qualification |
|---|---|---|
| D01 | `User`: `user_id`; `username`, `email`; `real_name`, `display_name`, `timezone`, `title`; `created_at`, `last_login`; `is_active`, `is_bot` | **Represented:** User identity, descriptive attributes, times, and nullable classifications. Username and email each have a unique constraint. API-derived profile fields are H02. |
| D02 | `Team`: `team_id`, `team_name`, `created_at` | **Represented:** Workspace ID, unique name, optional creation time. |
| D03 | `Channel`: `channel_id`, `channel_name`, `team_id`, `topic_text`, `purpose_text`, `is_private`, `is_dm`, `is_gc`, `created_at`, `is_archived`; `uq_channel_team_name` | **Represented:** Conversation identity, attributes, nullable workspace relationship, independent flags. Unique `(team_id, channel_name)` does not make name globally unique; null workspace also does not establish global uniqueness. |
| D04 | `Message`: `message_id`, `parent_id`, `channel_id`, `user_id`, `message_text`, `type`, `ts`, `blocks`, `created_at` | **Represented:** Message ID, optional self-parent, required conversation and author, text/type/timestamp/blocks/time. **Derived:** Thread grouping, A08. API `ts` comes from `message_id`, not stored `ts`. Nested blocks: H03. |
| D05 | `ChannelMember`: composite key `channel_id`, `user_id`; `joined_at` | **Represented:** Conversation membership and optional join time. Each pair occurs at most once. Neither FK requires a workspace-membership record. |
| D06 | `UserRole`: composite key `user_id`, `role_id`; `assigned_at` | **Represented:** Role assignment and optional time. A named-role assignment does not require `UserTeam`. No direct handler/operations access. |
| D07 | `MessageReaction`: composite key `message_id`, `user_id`, `reaction_type`; `created_at` | **Represented:** Reaction identity, emoji name and optional time, required user/message relationships. **Derived:** Grouped summary, A22. |
| D08 | `TeamRole`: `role_id`, `team_id`, `role_name` | **Represented:** Named role, required workspace, optional open role name. No relation equates it with `UserTeam.role`; no use in dispatched handlers. |
| D09 | `TeamSetting`: primary/foreign key `team_id`; `default_channel_id`, `allow_file_uploads` | **Represented:** Optional Workspace settings record, folded into owner. Each workspace has 0..1 settings record and 0..1 default conversation; a conversation may be default for many workspaces. Same-workspace consistency is not constrained. No direct handler/operations access. |
| D10 | `File`: `file_id`, `user_id`, `file_name`, `file_size`, `file_type`, `file_url`, `created_at` | **Represented:** File identity, required associated user (upload provenance is not established), optional metadata. No direct handler/operations access; empty `search.all` file results do not query this table. |
| D11 | `UserSetting`: primary/foreign key `user_id`; `notification_level` | **Represented:** Optional User settings record with nullable enum, folded into owner. Preserve record absence separately from null notification level. No direct handler/operations access. |
| D12 | `FileMessage`: `file_message_id`, `file_id`, `message_id` | **Represented:** File attachment record with required endpoints. The pair has no unique constraint, so duplicate pair records are possible. No direct handler/operations access. |
| D13 | `UserTeam`: composite key `user_id`, `team_id`; `role` | **Represented:** Workspace membership and nullable role enum. **Derived:** Owner/admin flags, H02. |
| D14 | `UserMention`: `mention_id`, `message_id`, `user_id`, `mentioned_at` | **Represented:** User mention record and optional time. Pair need not be unique. No direct handler/operations access; textual/block mentions do not populate it. |
| D15 | `MessageEdit`: `edit_id`, `message_id`, `edited_text`, `edited_at` | **Represented:** Edit record, required message, optional text/time. No direct handler/operations access; `OPS.update_message` mutates the message without creating an edit record. `Message.edits` has an ORM delete cascade, so `OPS.delete_message` can remove edit records indirectly. |

`UserTeamsRole` and `UserSettingsNotificationLevel` map to the role and notification
classifications. **Omitted:** unused `UserPresence`, which supplies no mapped field
or reachable API state. ORM `relationship()` declarations confirm navigation but
do not create additional edges beyond foreign keys; their cascades are **deferred**. No direct API access does not mean a table is isolated from API effects: ORM cascades and foreign-key constraints can involve it.

[Base](../backend/src/services/slack/database/base.py) and
[`create_tables`](../backend/utils/seed_slack_template.py) establish the complete
metadata boundary. Seed values do not narrow supported structure. The three Slack
migrations linked in [contextualization](slack-contextualization.md) confirm the
current bot field, blocks field, and reaction key. Database session machinery and
the empty `core/actions.py` scaffold supply no additional Slack concepts.

## Shared API evidence

These groups account for shared fields once. Operation rows below reference them.

| ID | Source | Disposition and model destination / reason |
|---|---|---|
| H01 | API `_serialize_conversation`, `_topic_payload`, `_channel_members` | **Represented:** `id`, `name`/`name_normalized`, `created`, `topic.value`, `purpose.value`, `is_archived`, stored conversation flags. **Derived:** type flags from `is_dm/is_gc/is_private`, `is_general` from name, `num_members` from memberships, DM `user` from another participant (actor fallback), DM `latest` from a selected message, `updated` from creation time, context/shared team IDs from supplied context or fallback. These are views, not new entities. |
| H01a | API `_serialize_conversation` defaults and synthetic fields | **Deferred:** `is_member` is an actual membership check only in some callers; others use default `True`. `creator` is the supplied creator or current actor, not stored historical authorship. With no stored creation time, `created` uses the current clock and `updated` copies that value. Topic/purpose `creator` and `last_set` are constants. DM `last_read` uses the latest message; other `last_read` values are zero, ordinary `latest` is null. DM `is_open=True`; ordinary `is_open` negates archive state. `unread_count`, `unread_count_display`, `priority`, `unlinked` are zero; sharing/frozen/read-only/thread-only flags are false; pending/previous-name arrays are empty; `parent_conversation` is null; locale is fixed. Preserve these as response semantics in the behavior model, not independent conceptual state. |
| H02 | API `_serialize_user`, `auth_test`, `users_info`, `users_list` | **Represented:** identity, username, email, real/display name, title, timezone, created time, active/bot flag. **Derived:** profile view and normalized-name copies/fallbacks; `deleted` from active flag; `is_admin`, `is_owner`, `is_primary_owner` from membership role; `is_app_user` from bot flag; `bot_id` is a string transformation, not another identity entity. Workspace context derives from membership; auth response workspace label/URL are generated, not `Team.team_name`. |
| H02a | API `_serialize_user` generated/default fields | **Deferred:** fallback workspace IDs, names and timezone, constant `tz_label/tz_offset`, `color`, empty phone/skype/status text/status emoji, false restriction/2FA flags; avatar hash and image URLs generated from user ID; `updated` uses creation time; requested locale uses timezone or `en-US`. These are compatibility output, not independently stored facts. `cache_ts` is **omitted** from the conceptual model as response cache metadata. |
| H03 | DB `Message.blocks`; API `VALID_BLOCK_TYPES`, `VALID_RICH_TEXT_ELEMENTS`, `VALID_RICH_TEXT_INNER_ELEMENTS`, `_validate_blocks`, `_validate_block` and called validators; `_blocks_to_mrkdwn`, `_element_to_mrkdwn` | **Represented:** structured JSON attribute, validated by chat handlers as an ordered list with accepted type tags; the JSONB column itself has no shape/tag constraint; nested `elements`, `text`, text type, style (`bold`, `italic`, `strike`, `code`), list style, embedded `user_id`/`channel_id`, links (`url`, text), emoji name, `image_url`/`slack_file`, `alt_text`, `fields`, `accessory`, `element`, `label`, `rows`. Unknown/uninterpreted nested content remains opaque within that value. **Derived:** text generated from supported block forms. **Deferred:** validation depth, required-shape checks, maximum count, JSON decoding, and format conversion. Embedded identifiers do not establish referential integrity or relational mention/file rows. |
| H04 | API `_principal_user_id`, `_get_env_team_id`, `_resolve_channel_id`, `_format_user_id`, `_format_channel_id`, `_resolve_user_id`, `_resolve_channel_filter`, `_build_dm_membership_cache` | **Represented:** actor, workspace, user/conversation identity and membership. **Derived:** lookups by ID, names, email, mention syntax, or DM participants; team context from channel or first user membership. **Deferred:** lookup ambiguity, access scope, input normalization, and fallback handling. [IsolationMiddleware](../backend/src/platform/api/middleware.py) supplies the actor/session boundary; credentials and environment metadata are **omitted** as platform concepts. |
| H05 | API chat attachment handling; `OPS.send_message`, `OPS.update_message` | **Deferred:** attachments are validated for content presence and echoed in the immediate chat response, but not stored. They must not be mapped to D12. Blocks and text are stored; update produces no D15 record. |
| H06 | API `_get_params_async`, `_get_params`, `_boolean`, `_parse_bool_param`, `_has_content`, `_encode_cursor`, `_decode_cursor`, `_slack_error`, `slack_endpoint`, query parsing/filtering/highlighting helpers | **Deferred:** HTTP/form/JSON representations, optional projection flags, query filters, pagination/sorting, validation/errors, permissions and mutation contracts. Success/error/warning envelopes and cursor/cache/random result identifiers add no domain entities. `SLACK_COMPAT_MODE` changes error HTTP status, not conceptual state. |

## API operation coverage

Every key in `SLACK_HANDLERS` appears below; both URL route forms dispatch to this
same set. A request field listed under controls is **deferred** through H06.
All operation-specific preconditions, effects, error paths, and transaction handling
are likewise deferred. Domain inputs and outputs are **represented** by the named
concepts unless explicitly marked derived, deferred, or omitted.

| ID / dispatch key → API function | Domain fields and conceptual destination | Controls, derived outputs, or qualification |
|---|---|---|
| A01 `auth.test` → `auth_test` | Acting User and Workspace; `user`, `user_id`, `team_id` | `team`, `url`, optional `bot_id` are generated (H02); actor H04. |
| A02 `chat.postMessage` → `chat_post_message` | `channel`, `text`, `blocks`, `thread_ts` → Conversation, Message, parent reference; response `ts`, author and content | H03–H05; `attachments` transient. Calls `OPS.send_message`. |
| A03 `chat.update` → `chat_update` | `channel`, `ts`, `text`, `blocks` → Message identity/content; returns message and possible parent reference | H03–H05; `attachments` transient. Calls `OPS.update_message`. |
| A04 `chat.delete` → `chat_delete` | `channel`, `ts` → Message and its Conversation; response echoes references | Calls `OPS.delete_message`; ownership/deletion contract deferred. |
| A05 `conversations.create` → `conversations_create` | `name`, `is_private` → Conversation attributes; actor's new membership; conversation output H01 | `OPS.create_channel`, `OPS.join_channel`; actual team from H04. |
| A06 `conversations.list` → `conversations_list` | Conversation collection and membership/count view H01 | `types`, `exclude_archived`, `limit`, `cursor`; calls `OPS.list_public_channels` and `OPS.list_user_channels`. H01a qualifies default membership flag. |
| A07 `conversations.history` → `conversations_history` | `channel` → Conversation; messages' `type`, `user`, `text`, `ts`, optional `thread_ts` and `blocks` | `oldest`, `latest`, `inclusive`, `limit`, `cursor` deferred. `latest` may be echoed; `pin_count=0` adds no pin concept. `OPS.list_channel_history`. |
| A08 `conversations.replies` → `conversations_replies` | `channel`, `ts` → Message anchor; message/author/content/parent references; derived `reply_count` and `parent_user_id` | `oldest`, `latest`, `inclusive`, `limit`, `cursor`. `subscribed=True`, `unread_count=0`, `last_read` from last returned message: deferred response semantics, not tracked reading/subscription state. `OPS.list_thread_messages`, `OPS.count_thread_replies`; one-parent resolution. |
| A09 `conversations.info` → `conversations_info` | `channel` → Conversation view H01 with checked membership | `include_locale`, `include_num_members`; H01a. |
| A10 `conversations.join` → `conversations_join` | `channel` and actor → Conversation membership; view H01 | `OPS.join_channel`; already-member warning is operation metadata. |
| A11 `conversations.invite` → `conversations_invite` | `channel`, `users` → Conversation memberships; view H01; error items reference users | `force`; `OPS.invite_user_to_channel` directly creates membership, no pending invitation entity. |
| A12 `conversations.open` → `conversations_open` | `channel` or `users` → existing Conversation or DM/group-DM with memberships | `return_im`, `prevent_creation`; H01; `no_op`/`already_open` are operation outcomes, not stored state. `OPS.find_or_create_dm_channel` or direct Channel creation plus `OPS.join_channel`. |
| A13 `conversations.archive` → `conversations_archive` | `channel` → Conversation archived flag | `OPS.archive_channel`; general-channel exception deferred. |
| A14 `conversations.unarchive` → `conversations_unarchive` | `channel` → Conversation archived flag | `OPS.unarchive_channel`. |
| A15 `conversations.rename` → `conversations_rename` | `channel`, `name` → Conversation identity/name; output H01 | `OPS.rename_channel`; checked membership flag. |
| A16 `conversations.setTopic` → `conversations_set_topic` | `channel`, `topic` → Conversation topic | `OPS.set_channel_topic`; no separate topic entity/history. |
| A17 `conversations.kick` → `conversations_kick` | `channel`, `user` → Conversation membership | `OPS.kick_user_from_channel`. |
| A18 `conversations.leave` → `conversations_leave` | `channel` and actor → Conversation membership | `OPS.leave_channel`; `not_in_channel` response is operation metadata. |
| A19 `conversations.members` → `conversations_members` | `channel` → Conversation memberships; `members` lists User IDs | `limit`, `cursor`; `OPS.list_members_in_channel`. |
| A20 `reactions.add` → `reactions_add` | `channel`/`channel_id`, `timestamp`/`ts`, `name` and actor → Reaction triple | `COMMON_REACTIONS`, `_normalize_reaction_name`; `OPS.get_reactions`, `OPS.add_emoji_reaction`. |
| A21 `reactions.remove` → `reactions_remove` | Same target/name/actor forms as A20 → Reaction triple | Same vocabulary; `OPS.get_reactions`, direct `session.delete`; unused `OPS.remove_emoji_reaction` is not this route's implementation. |
| A22 `reactions.get` → `reactions_get` | `channel`, `timestamp` → Message and reactions; author/text/ID/team | Derived reaction `name`, `users`, `count` grouping. `type=message`; fallback team string H01a pattern; `OPS.get_reactions`. |
| A23 `users.info` → `users_info` | `user` → User/profile view H02 | `include_locale`; `OPS.get_user`; team from target membership H04. |
| A24 `users.list` → `users_list` | User collection in workspace, profile view H02 | `include_locale`, `limit`, `cursor`; `OPS.list_users`; cache metadata H02a. |
| A25 `users.conversations` → `users_conversations` | `user` or actor → memberships and Conversation collection H01 | `limit`, `cursor`; `OPS.list_user_channels`; removes membership/count response fields. |
| A26 `search.messages` → `search_messages` | `query`/`q` references message text, author (`from`), conversation/DM participants (`in`), creation time (`before`/`after`). Matches join Message, Conversation, User. | Query syntax, `highlight`, `sort`, `sort_dir`, `count`, `page`, `cursor` deferred. Derived highlighted text, totals, and DM display name; generated `iid` and permalink are response artifacts. Uses H04 and direct ORM query. |
| A27 `search.all` → `search_all` | Delegates to A26, with the same message view and accepted request inputs | `files` and `posts` are fixed empty results: deferred compatibility fields, not operational file/post search. |

Documentation audit: all 27 method keys match dispatch. Every documented parameter
was compared with handler reads. The following are **omitted from conceptual
capability inference**, with their interface discrepancies deferred to the behavior
model:

- `token` is not read by Slack handlers; platform middleware supplies authentication.
- `chat.postMessage`: `metadata`, `mrkdwn`, `reply_broadcast`, `unfurl_links`,
  `unfurl_media`; `chat.update`: `metadata`, `reply_broadcast` are not read.
- Documented `team_id` is not read by `conversations.create`, `conversations.list`,
  `users.list`, `users.conversations`, `search.messages`, or `search.all`.
- `users.conversations` does not read documented `types` or `exclude_archived`.
- `reactions.remove`/`reactions.get` do not read `file` or `file_comment`;
  `reactions.get` does not read `full`.

Implementation-only aliases (`channel_id`, `ts`, `q`) and the `search.all` delegated
cursor are covered above. Documentation provides no response schemas; H01–H06 and
A01–A27 account for handler-produced conceptual fields and grouped compatibility
fields instead.

## Dedicated reverse audit

Completed against the recorded revision, starting from the model rather than the
source inventory. For each model element, the cited implementation was checked
for its meaning and strength, including optionality, identity, and qualifications.
The source files inspected have no working-tree changes relative to that revision.

| Model elements reviewed | Source witness and check | Result |
|---|---|---|
| Scope and all nine vocabulary entries | DB metadata, dispatch registry, H04 actor context; D01–D15 and A08 for domain terminology and derived threads | Supported within the stated implementation boundary. Platform concepts and action contracts remain explicitly outside this artifact. |
| All 13 entity entries: existence, identity, attributes, nullability, uniqueness | D01–D15; compared every listed attribute with its column, primary/unique key, explicit nullability or `Mapped` annotation. API message identity checked against A02–A04/A07–A08. | Supported. Separate message timestamp, nullable flags, and independent association-record IDs remain distinct. |
| Both folded settings records | D09/D11: owner FK is also the sole primary key; remaining fields are nullable | Supported: each owner has 0..1 settings record. Folding preserves record presence and null values. |
| All 20 diagram edges, both-end cardinalities, and identity participation | Matched each edge back to its FK and key membership. The default-conversation edge follows `TeamSetting.default_channel_id` through its owner key. Together with the two folded ownerships, this accounts for all 22 FKs. | Cardinalities supported. Corrected three left-side optional markers and 12 line styles; the eight relationships whose FKs contribute to child keys remain solid. Narrowed File–User label to associated user. |
| Relationship qualifications and excluded stronger roles | D03–D06, D09, D12–D14; `OPS.send_message`, A08, A12; D10 for File–User | Supported: no enforced flat thread tree, fixed lifetime DM size, cross-membership/default-workspace consistency, or pair uniqueness where not declared. File upload provenance was unsupported and removed. |
| Structured content and transient/synthetic information | H01–H05, `_validate_blocks`, chat handlers, `Message.edits` and `OPS.delete_message` | Qualified API list/tag validation separately from unrestricted JSONB shape. Replaced “no API use” with no direct access: edit deletion can occur by ORM cascade. Confirmed echoed attachments and synthetic response fields; recorded creation-time fallback in H01a. |
| All six derived-representation entries | A08 thread predicate/count; A22 grouping; H01 member count/latest ordering; H02 profile; A26–A27 message joins and result construction | Supported as views or groupings, without introducing independent stored entities. |
| All 11 state/classification rows and following vocabulary paragraphs | D01/D03/D04/D07–D11/D13, H01–H03, A06/A11/A20–A21; compared enum values and all three block-tag sets with code | Supported with storage/API distinctions. Confirmed unused `UserPresence` is neither mapped nor referenced by handlers/operations. |

Diagram notation was checked against the
[Mermaid ER syntax reference](https://mermaid.js.org/syntax/entityRelationshipDiagram.html#relationship-syntax):
optional endpoint markers depend on side, and solid/dashed lines distinguish
identifying from non-identifying relationships. This reference governs notation
only; it adds no Slack domain requirements.

After these corrections, every model element has reviewed source support or an
explicit qualification. Both directions now have a recorded audit: source-to-model
enumeration and interpretation above, and model-to-source support here. This is a
bounded source-based coverage argument, not proof of all runtime behavior.

## Validation and remaining qualifications

Targeted source checks challenge transformations rather than assuming them correct:

| Check | Source-grounded result |
|---|---|
| Absent settings versus an existing record with null values | D09/D11 permit both. Folding settings into optional owned attributes preserves both situations. |
| API `ts` versus stored `ts` | Posting constructs `message_id`; responses read it. D04 preserves the unused separate timestamp field instead of conflating it. |
| Reply to another reply | `OPS.send_message` checks same conversation but not root status. A08 follows one parent. Model describes direct-parent grouping, not a guaranteed flat tree. |
| Two users applying the same emoji to one message | D07's triple key allows this; repeated identical triples are excluded. A22 derives count/users from those records. |
| Duplicate file attachment or mention pair | D12/D14 have independent IDs and no pair uniqueness. Association identities remain in the model. |
| Blocks referencing a user or file | H03 stores structured data but does not populate D14/D12. Model keeps those representations separate. |
| Nullable workspace or conflicting conversation flags | D03 permits these; model preserves nullable cardinality and flags instead of assuming stronger subtype invariants. |

Mechanical checks matched all 15 tables and 72 mapped fields to D01–D15, and all
27 dispatch keys and handler names to A01–A27. Local document links and whitespace
checks passed. Isolated execution of serializer/content helpers also confirmed
actor-dependent creator output, default membership/topic fields, null-user-field
fallbacks, and embedded reference rendering without database lookup.

Shared representation helpers and documented parameter names are accounted for
above. This is source extraction with limited helper checks; dynamic action
correctness is not established, and no database-backed integration tests were run.

The meaning or intended synchronization of stored `Message.ts`, named roles versus
membership roles, and dormant edit/mention/file structures remains unspecified by
the active API. The model preserves their independent stored meaning without
inventing synchronization. Synthetic API state and inconsistent flag/thread cases
are qualified above; intended production Slack semantics remain outside scope.
