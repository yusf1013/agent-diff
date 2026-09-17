# Slack limitation coverage: bounded source audit

This is a proposal, not an adopted coverage denominator. It uses the adopted ER model and current 27-method API boundary. No service was executed and no external model call was made. It does not inspect 2,658 paths individually.

## Result

Combining the 2,564 routes touching the six entities with no direct API access and the 94 additional routes using the default-conversation setting is defensible as a first partition. Those 2,658 graph routes should not receive a path × attribute × resolution-mode test product. Preserve their mapping to the missing capability, and test the capability boundary with ordinary requests instead.

The current API dispatch contains no settings, named-role/assignment, file, attachment-record, mention-record, or edit-history operations. The explicit exceptions/nearby substitutes below must be respected. These are structural limitations, not evidence of an empty referent set.

A compact starting inventory has **eight groups**: the six dormant entity groups plus the two owned-settings groups. A representative read probe and a representative write probe per group gives **at most 16 primary probes**. This is coverage of grouped capability boundaries, not a claim to test every absent field or CRUD operation. Some write probes need an allowed-alternative judgment or may be excluded if no faithful ordinary request distinguishes the storage feature from the supported alternative.

## Primary inventory

| Group | What is missing | Ordinary read probe | Ordinary write probe | Qualification |
|---|---|---|---|---|
| Workspace settings | Reading or changing the stored default channel / file-upload setting | “Which channel is this workspace's default?” | “Make #announcements the default channel.” | Name `general` does not establish the stored default. File-upload flag is another setting in the same inaccessible settings record; can be a representative variant, not a mandatory attribute cross-product. |
| User settings | Reading or changing stored notification preference | “What notification setting do I have?” | “Set my notifications to mentions only.” | No user-settings API. Changing channel membership or ordinary message text is not changing this preference. |
| Named roles | Discovering or managing workspace-associated named-role records | “Which named roles are defined in this workspace?” | “Create a role called Reviewer.” | No permission semantics are modeled. Do not replace this with channel admin, or conflate it with owner/admin membership flags. |
| Role assignments | Discovering or modifying assignments of named roles to users | “Who has the Reviewer role?” | “Assign Sophie the Reviewer role.” | Supply role/recipient identity when the aim is to isolate write inability. User title `Reviewer` is not role assignment. |
| Files | Discovering stored files and their metadata; creating/modifying their records | “Find budget.pdf and tell me its size.” | “Rename file F_BUDGET to budget-final.pdf.” | `search.all` always returns an empty files section without looking at these rows. A known URL may support sharing, but does not supply missing metadata or a rename operation. |
| Stored file attachments | Reading or modifying File–Message attachment associations | “Which files are attached to this message?” | “Attach file F_BUDGET to this message.” | An embedded block file descriptor, a posted URL, or chat's `attachments` parameter is not the stored relation. Yet a normal request to *share* a file may permit a link: do not force an artificial storage-specific failure. |
| Stored user mentions | Reading or modifying UserMention records, including mention times | “When was Sophie mentioned in this message?” | A request explicitly about the mention log would be needed to isolate this storage capability. | Plain “mention Sophie” is supported by message text/blocks and should **not** be an unavailable-write test. Ordinary “who is mentioned?” can also be answerable from content. If the test cannot make the stored record relevant naturally, mark this group uninstantiated rather than invent a contrived prompt. |
| Message edit history | Reading past edited text/times; independently changing/deleting edit records | “What did this message say before it was edited?” | “Remove this message's edit history, keeping the current message.” | `chat.update` changes current text but records no history. Deleting an owned message can remove edit records through a cascade; that is an alternative only if removing the current message is allowed. |

Examples are illustrative candidate probes, not completed cards. In particular, the attachment/mention semantics must not be assumed from table names. This is a reason to keep a short inventory of capability families, not generate thousands of storage-specific tasks.

## What the simple 2,658/212 split misses

The remaining 212 routes avoid the wholly dormant entity groups and default-setting edge. That does not certify every terminal attribute or every write as supported. A small extension inventory can cover these without multiplying every route:

| Additional boundary | Source-backed limitation and compact representative |
|---|---|
| Workspace metadata | Workspace ID is visible, but stored `Team.team_name` and `Team.created_at` are not returned. `auth.test` synthesizes “Workspace {id}.” Read: “What is this workspace's name?” Write: “Rename this workspace to Acme Research.” The ID/title generated by auth is not the stored name. |
| User activity history | `User.last_login` exists but no handler/operation reads it. Read: “When did Sophie last log in?” Do not generate a write probe that asks to rewrite historical login facts. |
| Conversation-membership timing | `joined_at` is stored and auto-created, but member APIs return only user IDs. Read: “When did Sophie join #engineering?” No need to test every longer route that ends at join time. |
| Reaction timing | Reactions are exposed as emoji, users, count; their creation times are not. Read: “When did Tom add this reaction?” No historical-time write probe needed. |
| Full workspace membership role | Owner/admin status is readable; member versus guest versus unrecorded role is collapsed into the same flags. Read: “Is Sophie a guest or a regular member?” Write: “Make Sophie a workspace admin.” NamedRole is a different group. |
| User/profile writes | Profile attributes are readable but there is no update/create/deactivate user endpoint. One representative ordinary write such as “Change my job title to Research Lead” covers the missing profile-write boundary. Treat lifecycle operations separately only if that granularity is adopted; do not silently claim title editing tests deactivation too. |
| Conversation attribute writes | Topic/name/archive/membership updates exist, but purpose update and conversion of an existing channel's privacy are absent. A focused extension can test “Set #engineering's purpose to ...”; changing existing-channel privacy is a separate user-visible operation if included. Creation with `is_private` does not edit an existing channel. |

With the first seven extension rows as written (including both read/write where specified, one channel-purpose probe), the illustrative inventory is roughly **25 probes**, before pruning the unnatural mention-write probe or splitting distinct administrative operations. The reliable conclusion is “tens, not thousands”; 25 is a construction proposal, not a final certified count.

Do not inflate this with internal representation details merely because they appear in the DB. Stored `Message.ts` differs from exposed API `ts`; stored message type is replaced by a constant in message output. Unless a faithful ordinary request actually asks for those internal values, these are representation qualifications, not reasons to invent tasks.

Conversely, lack of a returned field is not always lack of access: `Message.created_at` affects before/after filters and sorting. Time-based message selection remains available without a raw creation-time field in the message payload. Capability analysis must include filter/query behavior and derivations, not only response-key matching.

## Inclusion and scoring discipline

1. A boundary is a particular unavailable observation or operation on a modeled concept, using the actual tool surface. Read and write are assessed separately.
2. Group all path/attribute variants that hit that same boundary; preserve a mapping rather than crediting every variant as tested.
3. For a read probe, seed a real positive hidden fact and avoid putting its answer in visible prompt/content. A fixed empty compatibility response must not establish absence.
4. For a write probe, make target and intended change clear when possible, so failure to identify the target is not the only obstacle. Check supported ways to achieve the intended effect, including authorized cascades; absence of a direct endpoint is insufficient by itself.
5. Use an ordinary request; do not require DB-row manipulations that the user's request would not distinguish from a supported alternative. This especially affects stored attachments and mentions.
6. Expected inability is not itself a solver bug. Fabricated selection or claims, unrelated substitutes, and false success reports require the appropriate evaluator policy. Current grounding-only reward does not automatically make every unsupported-write failure a grounding violation.
7. Keep this capability-limitation coverage separate from reference-path coverage so percentages mean what they claim.

## Source anchors (repository-relative)

- `systematic modeling/slack-coverage-ledger.md:29`–38: dormant entities/settings and cascade qualification; :43 says no direct access does not mean isolated from effects.
- `systematic modeling/slack-coverage-ledger.md:58`–64: derived/synthetic fields, blocks and transient attachments.
- `systematic modeling/slack-coverage-ledger.md:98`–103: reaction summary, user read operations, search fixed files.
- `backend/src/services/slack/api/methods.py:3170`–3198: complete 27-handler dispatch, no hidden CRUD/settings endpoints.
- `backend/src/services/slack/api/methods.py:3134`–3166: `search.all` returns fixed empty files/posts.
- `backend/src/services/slack/api/methods.py:832`–850 and :916–943: chat persists text/blocks then merely echoes attachments.
- `backend/src/services/slack/database/operations.py:344`–363: update mutates current text/blocks, delete deletes Message; no history insertion.
- `backend/src/services/slack/database/schema.py:123`–127: Message edits/reactions ORM cascades.
- `backend/src/services/slack/api/methods.py:2269`–2288: auth returns generated workspace label, not stored team name.
- `backend/src/services/slack/api/methods.py:2373`–2439: actual user projection; no last_login; owner/admin derivation and constant guest/restriction flags.
- `backend/src/services/slack/api/methods.py:2081`–2089: membership projection is user IDs only.
- `backend/src/services/slack/api/methods.py:2234`–2257: grouped reaction output has no timing.
- `backend/src/services/slack/api/methods.py:2986`–3001: creation-time filtering and sorting are available.
- `backend/src/services/slack/database/schema.py:47`–48, :137, :163: login, join and reaction timestamps exist.
- `backend/src/services/slack/database/schema.py:64`–68: stored workspace name/time.
- `backend/src/services/slack/database/schema.py:169`–266: named roles, settings, files, attachments, membership roles, mentions and edits.

The ledger revision and current inspected source match the adopted source model. This is a bounded static API audit, not a live integration test.
