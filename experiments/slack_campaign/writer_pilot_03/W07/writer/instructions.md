Write one conceptual benchmark scenario. Your assignment supplies the referent
entity, complete identifying route, resolution mode and candidate counts. Keep
these fixed. You choose a realistic story, identifying values and a short user
request. A later compiler will reconcile the story with an existing environment.
You do not receive or invent a concrete database, API transcript or answer key.

Follow this procedure:

1. Translate the route into a referring expression. Work backward from its last
   entity, then read forward to verify every relationship and the requested root.
   Distinguish author, reactor, member and container. Shared intermediate records
   must be the SAME records. Different roles or locations need not be equal: a
   message's author can belong to a channel other than the message's location.
   Choose observable identifying values along the route; preserve every chosen
   condition in the request. "Tom reacted with a thumbs up" contains both person
   and emoji conditions; "Tom reacted" loses the emoji. Do not uniquely identify
   the target first and turn the assigned relationship into incidental background.
2. Write a short, ordinary request with a supported edit/write operation and its
   substantive new value or communication purpose. Keep the requested referent
   central to that operation. If the capability brief provides no supported write
   for that referent, use a concrete open-ended read question and briefly note why.
   No candidate menus, emphatic ALL/EVERY, test terminology or search instructions.
   Ordinary plural wording is enough. A downstream argument must not silently
   change the identifying query. Keep adequate wording unchanged thereafter.
3. Build the initial rows using ONLY the supplied mode-specific instructions.
   Rows identify distinct referents of the assigned root entity. Put related
   witnesses in their facts, rather than counting them as additional referents.
   Several qualifying reaction chains to one person still identify one person.
   Additional unrelated facts are welcome when they preserve the intended match.
4. Derive negative rows by changing ONE identifying requirement at a time while
   preserving the others. The change may be a different value, a missing relation,
   a wrong relationship role or a broken same-record binding. Each negative has
   exactly one failed requirement, never two independent mismatches. For example,
   Tom👀 plus Tim👍 preserves both attribute facts but breaks their required binding
   to one reaction. A missing reaction is one missing relationship, not a reason
   to change the message's other properties too. Name the sole failure in the
   interpretation column. Removing that requirement must admit an otherwise
   excluded ROOT referent; another irrelevant reaction by the already-correct
   recipient is not an incorrect-recipient alternative. Give each independently
   variable value condition its own one-failure row, then add useful relationship
   and binding failures. Reread the request for additional conditions you missed.
   If a condition cannot independently affect selection, repair the design;
   no arbitrary three-condition limit or exhaustive combinations.
5. Check all rows together. Each positive needs a complete qualifying chain; each
   negative must have none, including chains completed by extra reactions or
   shared records elsewhere in the table. Preserve the assigned counts and
   alternatives. Every deliberately challenged condition must affect selection.
   Do not make the entire scenario collapse at an empty population: keep relevant
   people, messages and relationships, with complementary near matches. A locally
   missing-edge negative may accompany those substantive competitors.
6. Perform the author preflight: the actual prompt expresses the whole route and
   every intended condition; rows are plausible under ordinary language; each
   negative fails only its named requirement; each action has supplied/derivable
   inputs and supported capabilities. Check semantic topics, not mere keywords:
   a canceled meeting can still concern meeting confirmation/status, and an
   office-move decoy must not incidentally discuss deployment. Never insert
   answer-revealing hints into environment text. Repair any defect before returning.

Return readable Markdown: the supplied route and mode, the exact user request,
and ONE table with columns "Referent", "Environment facts", "Interpretation".
Give concrete conceptual facts sufficient to check every condition, using short
human labels and natural names, not database IDs or serialized records. Positive
or alternative rows come first. No hypothetical full-match rows, JSON, selectors,
grounding cards, oracle rules or long analysis. Add a short note only for a material
binding or capability qualification. If the assignment cannot be realized, explain
the conflict instead of silently replacing its route or mode. The examples show
construction principles; create a fresh story, not a renamed copy.

# Slack capabilities for conceptual authoring

This brief qualifies the conceptual model. Stored attributes are not automatically
observable. There is an acting user; use “I/my” for that actor when relevant.

- Supported identifying facts include user names/email and bot status; channel
  name, topic, archived/type flags; message text, author, location and replies;
  reaction emoji and reactor; channel membership and distinct member counts;
  the workspace association displayed on a user's profile and its admin/owner
  flags. Do not distinguish ordinary members from guests using unexposed flags.
- Public channels and users in the actor's selected workspace can be discovered;
  channel histories, members and reactions can be read with appropriate access.
  A compiler can arrange required read access in the environment. Do not supply
  a menu of candidate answers as a discovery shortcut.
- General workspace enumeration, workspace-name lookup and switching list/search
  to a different workspace are unavailable. Visible profile/channel associations
  can supply workspace IDs. For workspace-membership roots, limit the population
  to the association displayed on discoverable users' profiles; do not assume
  every stored workspace membership is exposed. Do not invent human job titles,
  private intentions, last-login times, membership join times or edit history as
  observable selection criteria.
- Supported writes: post/reply to a message, edit/delete a message, add a reaction;
  create/archive/unarchive/rename a channel, set its topic; invite/remove a channel
  member; open a DM and message a user. Arrange actor-owned messages for edits or
  deletion when needed. Supply the intended new content or communication purpose.
- A reaction can be removed only by its own reactor: “remove my reactions” is
  supported; removing another person's reaction is not. A reaction referent is
  one person–message–emoji identity, not just its message. Supported emoji writes
  include thumbsup, thumbsdown, eyes, raised_hands, tada, rocket, heart, fire,
  check and x. Do not assume an arbitrary readable emoji is writable.
- Workspace changes, workspace-role changes, user-profile changes and named-role
  management have no supported write API. For roots requiring those operations,
  use an explicit read fallback about observable facts and state the limitation
  briefly. Do not replace the assigned root with another entity to obtain a write.

The compiler will check the full existing seed, access and concrete capabilities.
This stage designs the story; it does not claim a validated runnable test.

# Adopted conceptual domain model

# Slack conceptual model

## 1. Scope

This models the Slack replica at revision
`920abcedd8a5ef071892dd1177aab17fe909a36d`: its 15 database tables and 27 dispatched
API operations. It follows the [meta-model](conceptual-meta-model.md) and
[Slack contextualization](slack-contextualization.md). Evidence identifiers below
refer to the [coverage ledger](slack-coverage-ledger.md).

This is a source-derived model, not a claim about a deployed database or full
production Slack. Tables without an API path remain in scope. Action contracts,
access rules, query mechanics, and transient request/response behavior are deferred
to the behavior model. Agent-Diff environments, runs, credentials, and scores are
platform concepts; the Slack boundary receives an acting user and a scoped session.

## 2. Vocabulary

| Term | Meaning in this model |
|---|---|
| Workspace | Organizational context, called `Team` in storage. |
| User / actor | A stored identity; the actor is the user selected for the request. A bot is a classification of User. |
| Conversation | Message container stored as `Channel`; covers named channels, DMs, and group DMs. |
| Membership | A user's association with a workspace or conversation. These are distinct relationships. |
| Thread | A derived grouping anchored on a message, containing that anchor and messages directly referencing it as parent in the same conversation. |
| Reaction | One user's emoji reaction to one message. |
| Named role | A workspace-associated role stored separately from the role on workspace membership. |
| File attachment / mention / edit record | Stored associations or records concerning a message; their presence in the schema does not imply the API creates them. |
| Blocks | Structured message content, including nested content types and embedded references. |

## 3. Entity–relationship model

### Entities, identity, and attributes

`?` means the stored value may be null. Referenced entities appear in the
relationship diagram below; their identifiers are not repeated as ordinary
attributes here. Timestamps describe stored information, not guaranteed historical
accuracy. D-codes map every stored field and constraint in the ledger.

| Entity | Identity | Attributes | Evidence |
|---|---|---|---|
| Workspace | Workspace ID; name also unique | Name, creation time?, optional settings containing file-upload flag? and a default-conversation reference? | D02, D09 |
| User | User ID; username and email independently unique | Username, email, real name?, display name?, timezone?, title?, creation time?, last login?, active flag?, bot flag?, optional notification settings | D01, D11 |
| Conversation | Conversation ID; name unique within a non-null workspace | Name, topic?, purpose?, private/DM/group-DM flags, archived flag, creation time? | D03 |
| Workspace membership | User + workspace | Membership role? | D13 |
| Conversation membership | User + conversation | Join time? | D05 |
| Message | Message ID; exposed as API `ts` | Text?, stored type?, separate stored timestamp string?, blocks?, creation time? | D04, A02–A04, A07–A08 |
| Reaction | Message + user + emoji name | Emoji name, creation time? | D07 |
| Named role | Role ID | Role name? | D08 |
| Role assignment | User + named role | Assignment time? | D06 |
| File | File ID | Name?, size?, type?, URL?, creation time? | D10 |
| File attachment | Attachment-record ID | References to file and message | D12 |
| User mention | Mention-record ID | References to user and message; mention time? | D14 |
| Message edit record | Edit-record ID | Edited text?, edit time? | D15 |

Settings are optional **owned records folded into their owner's attributes**.
Their presence remains meaningful: absent settings and present settings with null
values are distinct. This removes two diagram nodes without losing their meaning.

### Relationships and cardinalities

The diagram describes stored relationships. `||` means exactly one; `|o` at the
left or `o|` at the right means zero or one; `o{` at the right means zero or many.
Solid lines indicate that the referenced identity contributes to the child's key;
dashed lines indicate a relationship outside that key. Each association record
refers to exactly one object at each of its ends. Identity rules above determine
whether repeated pairs are allowed.

```mermaid
erDiagram
    WORKSPACE ||--o{ WORKSPACE_MEMBERSHIP : has
    USER ||--o{ WORKSPACE_MEMBERSHIP : holds
    WORKSPACE |o..o{ CONVERSATION : contains
    CONVERSATION |o..o{ WORKSPACE : "default in settings"
    CONVERSATION ||--o{ CONVERSATION_MEMBERSHIP : has
    USER ||--o{ CONVERSATION_MEMBERSHIP : holds
    CONVERSATION ||..o{ MESSAGE : contains
    USER ||..o{ MESSAGE : authors
    MESSAGE |o..o{ MESSAGE : "parent of"
    MESSAGE ||--o{ REACTION : receives
    USER ||--o{ REACTION : contributes
    WORKSPACE ||..o{ NAMED_ROLE : defines
    NAMED_ROLE ||--o{ ROLE_ASSIGNMENT : has
    USER ||--o{ ROLE_ASSIGNMENT : holds
    USER ||..o{ FILE : associated_with
    FILE ||..o{ FILE_ATTACHMENT : has
    MESSAGE ||..o{ FILE_ATTACHMENT : has
    USER ||..o{ USER_MENTION : target_of
    MESSAGE ||..o{ USER_MENTION : contains
    MESSAGE ||..o{ MESSAGE_EDIT_RECORD : has
```

The following qualifications prevent the diagram from promising stronger
relationships than the implementation supports:

- **Workspace links:** a conversation's workspace is nullable. Conversation
  membership does not itself guarantee workspace membership. A default conversation
  is not constrained to the settings owner's workspace. Role assignments likewise
  do not require membership in the role's workspace. (D03, D05, D06, D09)
- **Thread links:** storage permits any existing parent message. Posting checks
  that parent and child share a conversation, but does not require the parent to
  be a root. Thread retrieval follows at most one parent before selecting direct
  replies. Therefore, a universally flat thread hierarchy is not an invariant of
  this replica. (D04, A02, A08)
- **Participant counts:** DM and group-DM describe conversation kinds. Their
  creation paths select participants, but the stored membership relation does not
  enforce exactly two or a fixed group size over the conversation's lifetime.
  (D03, D05, A12)
- **Separate records:** membership roles and named-role assignments are not linked
  by implementation. File attachments and mentions allow multiple records for the
  same pair because their identities are separate IDs. (D06, D08, D12–D14)

The File–User link establishes an associated user. The schema and active API do not
establish that this user performed an upload, so the diagram does not assign that
stronger role. (D10)

### Structured content and derived representations

The chat API validates blocks as an ordered list of structured values owned by a
message. The underlying JSONB column has no constraint enforcing that shape or
its type vocabulary; data written outside these API checks can differ. Validated
content can include text and style, nested elements, user/channel identifiers, links, emoji,
image/file descriptors, labels, fields, accessories, and rows. Embedded identifiers
are not foreign keys. Uninterpreted nested content is retained as data, rather than
expanded into speculative entities. A block mentioning a user does not imply a
`UserMention` record; a file descriptor does not imply a `FileAttachment`. (H03)

| Representation | Conceptual meaning and limit | Evidence |
|---|---|---|
| Thread and reply count | Derived from an anchor and direct parent references within its conversation | A08 |
| Reaction summary | Group reactions by message and emoji; derive user list and count | A22 |
| Conversation member count | Derived from membership records | H01 |
| Latest DM message | A selected message in that conversation, ordered by creation time then ID | H01 |
| User profile | View of user attributes with fallbacks, generated fields, and constants; no independent profile entity | H02 |
| Search match | View of an existing message, author, and conversation; highlighting and generated result IDs do not change message identity | A26–A27 |

The API's message `ts` comes from `message_id`, while `thread_ts` represents a parent
or selected thread anchor. The separate database `Message.ts` is retained as a
stored attribute without assuming these are synchronized. Names and display text
are descriptions or lookup forms, not replacements for identity. (D04, H04)

Attachments echoed by chat operations are transient values, not stored file
attachments. Conversation `creator`, topic author/time, read markers, subscription
flags, sharing flags, and avatar URLs are not evidence of independently maintained
facts: their provenance is qualified in H01–H02 and A08. Named roles, role
assignments, settings, files, file attachments, mentions, and edits have no direct
access in dispatched Slack handlers or their operations at this revision. Their
foreign keys and ORM cascades still matter: deleting a message cascades to its
edit records, although updating it does not write an edit record.
(D06, D08–D12, D14–D15, H05)

## 4. States and classifications

| Subject | Stored or derived classification | Meaning and qualification | Evidence |
|---|---|---|---|
| User | Stored active and bot flags, each nullable | Active/inactive and bot/non-bot; null is unrecorded. The API supplies fallback values rather than exposing every null distinction. | D01, H02 |
| Workspace membership | Stored role, nullable | `owner`, `admin`, `member`, `guest`; API owner/admin flags derive from this role, not named-role assignments. | D13, H02 |
| Conversation | Stored `is_dm`, `is_gc`, `is_private` | Conventional types are public channel, private channel, DM (`im`), group DM (`mpim`). Keep the flags: no database constraint forbids conflicting combinations, and serializer/filter interpretations differ for such combinations. | D03, H01, A06 |
| Conversation | Stored archived flag | Archived/unarchived; independent of kind. API `is_open` is a derived value or constant, not a separate lifecycle. | D03, H01 |
| Membership | Derived existence | Present/absent; no stored pending-invitation state | D05, D13, A11 |
| Message | Derived parent presence; stored type string? | Parentless/reply; stored type is open-ended, while API message payloads commonly hard-code `message`. | D04, A02, A07–A08 |
| Reaction | Stored emoji name | Database string; API add/remove use `COMMON_REACTIONS` and normalize spelling. The finite API vocabulary does not restrict all possible seeded database values. | D07, A20–A21 |
| User settings | Stored notification level, nullable | `all`, `mentions`, `none`; no dispatched API reads it | D11 |
| Workspace settings | Stored file-upload flag, nullable | True/false/unrecorded; no dispatched API enforces it | D09 |
| Named role / file | Stored role name? / file type? | Open strings, not enumerated role permissions or a validated file taxonomy | D08, D10 |
| Message blocks | Stored type tags, checked at API boundary | Block, rich-text container, and inner-element vocabularies below; validation depth varies | H03 |

The implemented block vocabulary is `rich_text`, `markdown`, `section`, `header`,
`divider`, `image`, `context`, `actions`, `input`, `file`, `video`, `table`, and
`context_actions`. Rich-text containers are `rich_text_section`, `rich_text_list`,
`rich_text_preformatted`, and `rich_text_quote`. Inner-element tags are `text`,
`emoji`, `link`, `user`, `usergroup`, `channel`, `broadcast`, `color`, and `date`.
Accepted tags do not imply separate operational capabilities such as user-group
management or video handling. Text generation interprets only part of this vocabulary.
It also distinguishes `plain_text` from `mrkdwn` section text, ordered from other
list styles, and bold/italic/strike/code text styles; these remain content attributes.

`UserPresence` declares `active` and `away` in the source but is neither mapped to a
column nor used by dispatched handlers. It therefore adds no presence state to
this model. State transitions and validation limits belong in the behavior model.
