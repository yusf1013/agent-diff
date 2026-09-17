# Slack construction pilot selection

The [assignment manifest](pilot_assignments.json) fixes 14 initial construction
jobs: two mutations and twelve clean generations. Each of the seven referent
entities receives two jobs. The modes are three single, five multiple, three
absent and three underspecified. These are manual design assignments, not
generated tests or achieved coverage. The separate Sonnet construction agent must
write the actual requests, concrete seeds and cards.

There are **no newly created easy controls**. Existing baseline runs can support
comparisons where applicable. An enriched request is reported as an adapted
variant; comparing it against the original does not isolate an environment-only
intervention. For the single-criterion mutation, the enriched case is itself a
campaign stage. A subsequent near-miss stage uses the same enriched request only
if the valid enriched case did not demonstrate a grounding failure. That optional
job is additional to the 14 initial jobs.

| Assignment | Referent | Route | Mode | Construction / main feasibility risk |
| --- | --- | --- | --- | --- |
| P01 | User | Direct `users.real_name`; no relationship-route ID | Single | Enrich slack_58 O1 while retaining its original name predicate. |
| P02 | Message | R061: Message → Conversation | Multiple | Add a channel-name focal negative to slack_66 O1; retain its content condition, original prompt and existing singleton match set. |
| P03 | User | R145: User → Reaction | Absent | Preserve plausible users and reactions while establishing no match for the focal emoji. |
| P04 | Message | R089: Message → Reaction → User → Conversation membership → Conversation | Multiple | Preserve the same reactor/membership binding and distinct-message collection. |
| P05 | Conversation | R009: Conversation → Conversation membership | Multiple | Count distinct membership records per channel, including the actor if present. |
| P06 | Conversation | R024: Conversation → Message → Reaction → User | Underspecified | Partial name information must induce competing conversation selections. |
| P07 | Conversation membership | R045: Conversation membership → User | Single | A membership is a user–channel pair, not just a person. |
| P08 | Conversation membership | R031: Conversation membership → Conversation → Workspace → Workspace membership → User | Absent | Use the bounded profile-displayed association and establish the missing focal person. |
| P09 | Reaction | R111: Reaction → User | Underspecified | Competing user identities must imply distinct reaction selections. |
| P10 | Reaction | R108: Reaction → Message → User → Conversation membership → Conversation | Multiple | The author, not the reactor, must hold the qualifying membership. |
| P11 | Workspace | R165: Workspace → Conversation | Absent | Use actual workspace IDs exposed on bounded non-DM channels. |
| P12 | Workspace | R179: Workspace → Conversation → Message → Reaction → User | Single | Deduplicate by workspace identity rather than relationship witnesses. |
| P13 | Workspace membership | R195: Workspace membership → Workspace → Conversation → Message → Reaction → User | Underspecified | Long internal-workspace route, profile scope and distinct candidate membership sets. |
| P14 | Workspace membership | R203: Workspace membership → User → Message | Multiple | Preserve the membership pair and its user's authorship. |

This is a purposive feasibility pilot, not a representative estimate of all 174
routes. It includes one-, two-, three-, four- and five-edge routes, both membership
referents, same-person bindings, a relation count and workspace visibility.
Twelve clean-generation routes and the mutation's R061 are distinct retained
routes. P01 deliberately does not manufacture a route label for a direct
attribute. The pilot does not exercise all 28 entity–mode requirements; both
Message assignments are multiple. Modes follow the requested selection semantics,
not raw match count. Slack 66's plural request jointly intends its matching
questions, although its seed contains one such question. The mode remains
multiple without adding new positive targets just to increase cardinality.

Only the focal entity/path, endpoint field or count operation, and assigned mode
are fixed. The author chooses up to two auxiliary criteria, concrete values,
ordinary request wording and seed details. Existing catalog request fragments are
provided as feasibility illustrations, not as authored pilot requests. No solver
ground-truth labels, native scores or solver outcomes informed this selection.

The count pilot uses R009, where membership counting is local to the root
conversation. Nested counts over an intermediate route node are deliberately
outside this first implementation; this is a construction-tool limitation, not
an exclusion from the agreed coverage catalog.

The two mutation inputs were checked in the full test entries and existing
cards. Slack 58 names one recipient, John, resolved by `users.real_name`.
Slack 66 combines a channel-name condition with the MCP deployment message
content. Its focal path is R061 and a suitable negative preserves the content
condition while violating the channel-name condition. No claims about either
solver's existing success were needed to select them.

Run `python grounding/slack_campaign/build_assignments.py --check` to verify the
manifest against its builder and hashed source files. This validates assignment
structure and retained-route membership; concrete semantic, seed, API visibility
and generated-card validation must still occur before a case earns coverage.
