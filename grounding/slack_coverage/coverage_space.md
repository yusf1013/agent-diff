# Slack coverage-space design

**Status: retired proposal; do not use as the coverage specification.** The existing [Slack conceptual model](../../systematic%20modeling/slack-conceptual-model.md) and its extraction discipline have been adopted instead. Current route-redundancy findings are in [route_redundancy_analysis.md](route_redundancy_analysis.md); those findings are proposals for discussion, not a frozen denominator. The text below preserves the initial 2026-09-15 proposal for provenance. Existing cards and assessment policies are unchanged. Ground-truth run labels are reserved for G4 and are not sources for this space.

The proposed coverage unit is **referent entity × focal identifying attribute/path × resolution mode**. A path identifies the subject; it is not a required API-call sequence. Distinct downstream operations, auxiliary-criterion combinations, and numbers of decoys are not additional coverage axes in this round.

## 1. Sources and admission rule

Derive this space from the benchmark's referenced seed, API definitions, and API documentation. Do not reverse-engineer service handlers, database models, migrations, or seed-loading code. Do not use the separate conceptual ER models or `systematic modeling/` experiment.

| Source | Role |
|---|---|
| [Referenced Slack seed](../../examples/slack/seeds/slack_bench_v2.json) | Native records, field names, explicit values, and relationship endpoints. |
| [Local API definitions](../../examples/slack/testsuites/slack_docs/slack_api_full_docs.json) | Listed operations and request parameters. This file does not provide complete response schemas. |
| [Slack user object](https://docs.slack.dev/reference/objects/user-object/) | Documented identity/profile fields and workspace-role flags. |
| [Slack conversation object](https://docs.slack.dev/reference/objects/conversation-object/) | Documented conversation identity, topic, purpose, and kind/status flags. |
| [Slack thread replies](https://docs.slack.dev/reference/methods/conversations.replies/) | Message identity and root/reply relationship. |
| [Slack reactions](https://docs.slack.dev/reference/methods/reactions.get/) | Reaction names, user attribution, and visibility limitations. |

The four external pages were consulted on 2026-09-15. [Source inventory](source_inventory.json) records local source hashes, every observed seed field, row counts, and the consulted URLs. The existing [source map](../slack_analysis/source_map.md) supplies additional previously documented translations. It is a navigation aid, not an independent authority.

Admit a candidate family when (1) the identifying evidence has a concrete representation in the supplied environment, (2) the documented interface provides a way to observe it, and (3) an ordinary request can use it to identify a subject with a meaningful requested operation or deliverable. Official Slack documentation establishes interface meaning, not implementation parity. Distinguish a source-supported candidate from a runnable, validated generated case.

Build the candidate space before mapping [baseline cards](../slack_analysis/analysis.json). The full test entries later establish baseline selection semantics, actor, and scope. Neither baseline frequency nor solver failures determine which domain paths exist.

## 2. Proposed referent entities

| Coverage entity | Native representation | Interpretation |
|---|---|---|
| User | `users` | A person/bot or a set of accounts. Authors, members, and reactors remain users when they are the described subject. |
| Conversation | `channels` | A channel or DM, or a set of conversations. Conversation kind is a property, not a separate entity family. |
| Message | `messages` | A message, a set of messages, or a root message used to identify a discussion thread. Record thread scope explicitly when the requested subject is the whole discussion. |
| Existing reaction | `message_reactions` | An existing user's reaction on a message. Adding a new reaction ordinarily grounds the message; it does not require an existing reaction referent. |

These are proposals about requested subjects, not a claim that every seed table is a separate obligation type. The seed also has `channel_members`, `user_teams`, and `teams`:

- Channel membership supplies the user–conversation relationship. A request for channel members selects users; removing members need not introduce a separate membership obligation.
- Workspace membership supplies workspace scope and the explicit workspace role. It does not supply an employment title or a department.
- The single supplied workspace is proposed as shared scope for this campaign. Cross-workspace identification remains outside the initial proposal; it is not a missing mode silently called infeasible.

DMs are identified through their documented kind and participants; do not assume a seeded DM's internal `channel_name` is a user-visible name. Existing reactions are identified by message, user, and reaction type; there is no invented reaction-ID field. Preserve the channel alongside a message timestamp in interface operations.

## 3. Direct identifying fields

Each semicolon-separated field below denotes a **separate candidate terminal attribute**, not a compound criterion or a merged cell. Examples illustrate field meaning, not a list of generator-specific task templates.

| Entity | Native terminal attributes | Candidate use and qualifications |
|---|---|---|
| User | `users.real_name`; `users.display_name`; `users.username` | Full/partial name, display-name, or handle descriptions. A first-name predicate can operate on `real_name`; do not invent a stored `first_name`. |
| User | `users.email` | Email identity or a naturally stated address-domain condition. Observation requires email visibility; exact-address uniqueness must be respected. |
| User | `users.timezone` | A timezone-defined person/set. Missing timezone values do not establish another timezone. |
| User | `users.is_bot` | Bot versus human-account selection. |
| Conversation | `channels.channel_name`; `channels.topic_text`; `channels.purpose_text` | Name, explicitly stated topic, or purpose. A vague reference to discussion content is not automatically a topic-field predicate. |
| Conversation | `channels.is_private`; `channels.is_dm`; `channels.is_archived` | Privacy, DM kind, and archive status, subject to field/default qualifications below. |
| Message | `messages.message_text` | Explicit wording or semantic content. Selection predicates remain recorded alongside the path. |
| Message | `messages.ts` / `messages.message_id` | One documented timestamp concept, not two independently covered attributes. Time ranges and first/latest selection need an explicit comparison population and time convention. |
| Existing reaction | `message_reactions.reaction_type` | Existing emoji/reaction type. |

Additional candidates needing an explicit scope decision:

- **Supplied IDs:** `users.user_id`, `channels.channel_id`, and message handles can legitimately identify a subject. Propose tracking direct-ID cases separately as controls until we decide whether to include them in the primary denominator. Handles appearing only in cards are not solver-supplied identifying criteria.
- **Group conversations:** `channels.is_gc` exists but is false in every supplied row. Its mapping to the documented group-DM flag is not established by the local API definitions. Keep pending rather than assuming it.
- **Message subtype:** `messages.type` is only `message` or missing here. Do not invent subtype variation based on full Slack capabilities.
- **Root/reply status and relationship existence/counts:** These are real derived selection predicates, not invented stored fields. Their coverage granularity needs deciding: attach them to a canonical relationship path rather than invent a database column.

## 4. Relationship inventory

The route labels in this table are explanatory notation. Cards must continue to use real native fields and supported predicates. Enumerating both directions avoids losing a family just because the foreign key is stored on the other endpoint.

| Relationship and directions | Native evidence | Documented retrieval basis |
|---|---|---|
| Message → author; User → authored messages | `messages.user_id = users.user_id` | History/search message user plus user information. |
| Message → conversation; Conversation → messages | `messages.channel_id = channels.channel_id` | Conversation-scoped history, search, conversation information. |
| User → joined conversations; Conversation → members | `channel_members.user_id`, `channel_members.channel_id` joined to the endpoint IDs | `conversations.members`, `users.conversations`, and user/conversation information. |
| Reply → root; Root → replies | `messages.parent_id = root.message_id`, retaining the shared channel | `conversations.replies`, `thread_ts`, and message timestamps. Do not impose recursive reply nesting unsupported by this representation. |
| Existing reaction → message; Message → existing reactions | `message_reactions.message_id = messages.message_id` | `reactions.get` on the message. |
| Existing reaction → reactor; User → existing reactions | `message_reactions.user_id = users.user_id` | Reaction user attribution plus user information; enumeration caveat below. |
| User → workspace role | `user_teams.user_id = users.user_id`, scoped by `user_teams.team_id` | Documented user admin/owner flags support the role concept. Exact native-role projection still needs qualification. |

Workspace role is an identifying relationship attribute, not a new User field. The seed has `admin` and `member`; it does not support interpreting these as engineering lead, manager, or other employment roles.

## 5. Identifying-path candidates

Start from the requested referent entity, traverse the relevant relationship(s), and end at the field whose value the request uses. A foreign key used merely to join records does not itself become another focal criterion.

The route groups below are an initial inventory for review. Expand their terminal fields individually before freezing a denominator; they are not single cells. Both source-visible meaning and a natural request must survive expansion.

| Referent | One-relationship routes | Longer routes that must also be considered |
|---|---|---|
| User | Authored message → text/time; joined conversation → name/topic/purpose/kind/status; existing reaction → type; workspace membership → role | Authored message → conversation → name/topic/purpose; existing reaction → message → text/time; authored reply → root → text; joined conversation → other member → name. |
| Conversation | Member → name/handle/email/timezone/bot status; contained message → text/time | Contained message → author → name/timezone; contained message → reaction → type; member → workspace role; contained reply → root → text. |
| Message | Author → name/handle/email/timezone/bot status; conversation → name/topic/purpose/kind/status; root/reply → text/time; existing reaction → type | Existing reaction → reactor → name; author → workspace role; root/reply → author → name; conversation → member → name. |
| Existing reaction | Reactor → name/handle/email/timezone; message → text/time | Message → author → name; message → conversation → name/topic/purpose; message → root → text. |

For example:

- “DM the author of the deployment announcement” selects a **User**, using authored-message text.
- “React to the deployment announcement in #engineering” selects a **Message**, using message text and conversation name; one is designated focal for a generated variant.
- “Find the channel where Alex posted the deployment announcement” selects a **Conversation**, using message author-name and message text on the **same message**.
- “Remove my eyes reaction from the deployment announcement” can describe an **existing reaction**, using reaction type and associated message text within the actor's reaction scope.

These are not `User-via-message` or `Message-via-channel` entity types. They are one entity with different identifying paths. Nor are they mandatory tool sequences.

### Path-space boundary still to settle

Arbitrarily repeated relationship traversal produces an unbounded space, so “all graph walks” is not an appropriate denominator. Conversely, limiting the space to direct fields would repeat the earlier omission of relationships.

Proposed next step: expand direct fields and one-relationship routes systematically, then review longer routes with an ordinary-language example and declared shared scope. Record included, unsupported, redundant, and out-of-campaign routes explicitly. The current longer-route examples are not an exhaustive enumeration and no hop limit has been silently adopted. A meaningful repeated entity type is not automatically a useless cycle: finding users who share a channel with Alex can require User → Conversation → User.

Existence, absence, collection counts, ranking, and set difference can operate on these paths. They should be recorded as selection semantics, not automatically multiplied into extra coverage axes. How to assign a focal path to pure relationship-existence/count requests remains part of this review.

## 6. Resolution and focal construction

| Mode | Meaning |
|---|---|
| Single | One entity is requested, including explicitly delegated choose-one selection from an eligible population. |
| Multiple | One determined collection whose members are jointly intended. |
| Absent | The described reference has no match in the supplied environment. |
| Underspecified | The intended selection is unresolved and the request does not authorize the solver to make that choice. |

These coverage labels do not change the card schema. Cards retain `resolved`, `absent`, or `underspecified`; single/multiple require interpreting the selection, not merely counting the entries in `Referent set`.

Two decisions remain open:

1. **Optional delegated subsets:** A request to acknowledge whichever messages merit it may permit zero, one, or several selections. It is not underspecified merely because judgment is delegated. Keep its mapping pending until agreed; do not silently fold it into multiple or omit it from baseline accounting.
2. **Underspecified focal paths:** Proposed convention, awaiting confirmation: retain identifying information on the focal path but leave the intended selection unresolved, e.g. two people named Alex. If the request instead identifies “the person who congratulated me,” credit that expressed relationship/content path, not a name criterion the request never supplied.

For focal A with auxiliary B and C, a decoy must satisfy B and C and fail A. Multiple mode may have several full matches plus that decoy. Underspecified mode has competing intended selections; a decoy failing A remains a non-match, not one of those competing full matches. Adding a non-match alone does not produce underspecification. Enrichment uses at most three criteria total for this campaign.

Mode feasibility depends on the predicate and selection semantics. Do not generate duplicate unique identifiers or duplicate exact emails to force ambiguity. A broader email-domain condition is a different predicate over the same attribute and must be stated honestly. Do not change the focal path merely to fill its mode cell. Mark cells attempted-but-unrealized separately from genuinely infeasible cells, with evidence for the latter.

## 7. Evidence limits discovered in this pass

- The seed contains 19 users, 12 conversations, 116 messages, one reaction, 62 channel-membership rows, 19 workspace-membership rows, and one workspace. Small or constant populations do not by themselves make a field unusable for generation.
- Eleven conversation rows omit `is_archived`. This pass does not infer an undocumented runtime default. Generated cases targeting archive status should specify it explicitly and receive an interface check before being counted as valid.
- Ten users have null timezone. Null is not evidence for a geographic classification or for absence of the user.
- Ninety-four messages have `ts`; 22 omit it. Every populated `ts` equals `message_id`, and all three supplied parent links resolve within the same conversation. Preserve this consistency when constructing new records; document any normalization rather than consulting implementation defaults.
- The official reactions documentation does not guarantee an exhaustive list of other reactors, although it documents the authenticated user's inclusion. Paths needing complete other-user reaction attribution therefore remain qualified; the seed alone cannot establish their observability. [Source](https://docs.slack.dev/reference/methods/reactions.get/).
- Official Slack user fields exceed this seed's fields. Job title, family relationship, department, and profile status are not admitted merely because they are plausible or available in some Slack interfaces. The local docs' posting parameters for blocks/attachments also do not establish an initial-state file/attachment entity or supported seeded values.
- The proposal establishes documented candidate paths, not seed-import support, permissions, or successful API execution. A later generic construction/setup check must expose those limitations without expanding the evidence boundary for card extraction.

## 8. Next deliverables

1. Settle entity scope, ID controls, path-enumeration boundary, derived relationship predicates, and the two resolution questions.
2. Expand the approved families into a machine-readable catalog with native fields, documented observation route, mode feasibility, and evidence notes. Do not publish a coverage percentage before freezing it.
3. Map baseline obligations into that catalog using the existing cards plus prompt/seed interpretation. Keep every unmapped obligation visible. Do not treat change-computation fields, output handles, or all foreign keys as identifying criteria.
4. Build mutation and clean-generation agents against planned targets. They produce current-format cards/specifications plus private construction evidence; they do not write the old expected-behavior oracle.
5. Track validated coverage, focal-decoy strengthening, attempts, and failures separately. The same campaign supports G2 and G3. No ground-truth run labels enter its selection or generation inputs.
