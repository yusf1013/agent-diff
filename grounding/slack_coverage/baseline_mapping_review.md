# Baseline Slack identifying-path review

This is a manual annotation of the 59 task designs and their 198 existing cards,
not automated extraction or a measurement of solver behavior. No trajectories,
oracle verdicts, or ground-truth run labels were consulted. The only card change
is the authorized `Identifying paths` field; all previous annotations, referent
sets, task specifications, and assertion-coverage labels remain unchanged.

[baseline_mapping.json](baseline_mapping.json) contains the per-obligation mode,
predicate attributes, complete route IDs, source-selection rule, and review note.
[annotate_baseline_paths.py](annotate_baseline_paths.py) records the manual
decisions as a reproducible projection. It is not a general-purpose extractor.

| Annotation | Count |
|---|---:|
| Requested single | 129 |
| Requested determined collection | 34 |
| Absent | 11 |
| Underspecified | 20 |
| Delegated optional subset, outside four-mode cells | 4 |
| Distinct complete retained routes used | 12 / 174 |
| Distinct native identifying predicate fields recorded | 18 |

The 18 field names are the native-field inventory, not automatically 18 cells in
the conceptual attribute catalog. Some express identity, population scope, or
timestamp ordering and need that catalog's normal mapping. Four-mode coverage
also requires the referent-entity dimension; these obligation counts are not
counts of distinct coverage cells.

## Path interpretation

Paths begin with the referent table and preserve native foreign-key roles and
ordered direction. A local predicate is represented by a singleton path. A
message's named author and its named channel are separate paths; they are not
combined into a walk that changes the requested referent. Internal path
conditions remain in the card's description/selection rule. These small path
objects do not duplicate a full Boolean query language.

Only an entire annotated route earns its corresponding route cell. A longer
route does not automatically earn its prefixes, suffixes, or edges. Mere joins
used to compute a response, a new-message destination, and shared workspace
scope do not create identifying routes. Actor IDs supplied by the environment
can constrain a message or membership directly without inventing a user lookup.

All paths are native-table paths. The conceptual correspondence is conversation
= channels, user = users, message = messages, reaction = message_reactions,
conversation membership = channel_members, workspace membership = user_teams,
workspace = teams.

## Decisions worth inspecting

- **Slack 66 O1:** “MCP deployment questions” is plural in the original request
  and task specification. It is mapped as a requested collection even though
  the seed supplies just one matching message. The existing card is unchanged.
- **Slack 89 O1:** the literal “Test Workspace” supports the full
  users → user_teams → teams route. Its name is present in the seed. This
  records the designed reference; it does not assert that every identifying
  field is exposed by the current API.
- **Slack 92 O1:** the agreed card's boundary is the containing history. The
  path is messages → channels; Gemini in the requested summary does not add an
  exact source-message predicate that the card deliberately omits.
- **Slack 94/95/101/103 relevance ambiguities:** where the card does not settle
  a relationship-based interpretation, the annotation leaves a root-only path
  with no invented identifying field. Speculative discussion-based routes do
  not earn coverage. Slack 98 O4 differs: both interpretations explicitly ask
  for channels discussing a topic, so channels → messages is stable even though
  the topic and resulting set are unresolved.
- **Slack 105:** Robert's named authorship is retained from the original
  request. Sophie's DM source has both an author path and a conversation
  membership path, referring to the same person. These do not create new
  obligations or alter existing referents.
- **Slack 107 O5 and 113 O4:** actual reply-parent traversal repeats the messages
  table. It is preserved, marked outside the current no-repeated-type catalog,
  and earns no substituted shorter route. The former also allows explicit
  circuit-tracer mentions as an alternative to thread membership; its path list
  does not turn that OR into an AND.
- **Slack 78 O1 and 113 O6:** merely checking that a message is a reply/root uses
  its parent_id field. No second message record is traversed solely for that
  check.
- **Slack 100 O7, 107 O4/O5, and 108 O8:** delegated optional source/target
  subsets are recorded with a null four-mode value and an explicit selection
  policy. This does not make every summary source optional: Slack 92's history
  and Slack 109's broad source-channel collection remain collective referents.
- **Slack 112 O3:** choosing one of six eligible messages is single mode.
- **Slack 115 O2:** the path through memberships to existing DMs is an exclusion
  condition. Listing its path does not mean those existing counterparts are the
  users selected for new DMs. The prior card's sort and exclusion rule controls.

## Verification

The card projector validates every path's root, native table names, foreign-key
endpoints, and field existence, then regenerates the cards. Its `--check` passes
for all 59 tests / 198 cards. Removing only `Identifying paths` from the updated
analysis reproduces the prior Git version exactly. This establishes preservation
and structural consistency, not a formal proof of the manual semantic choices.
