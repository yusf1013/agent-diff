# Grounding obligations: self-contained onboarding and measurement protocol

**Protocol version: v1.** Record this version in each analysis's supporting documentation, outside the cards. When an approved change alters counting, resolution, card semantics, or coverage rules, increment the version and describe the change. Editorial corrections do not require a new version. Compare analyses with their protocol versions visible; do not silently apply revised rules to earlier results.

## 1. Your assignment

Use this document to analyze a benchmark supplied by the user. Produce a grounding-obligation table for every in-scope test, one card per counted obligation, and per-test and aggregate measurements of assertion coverage. This document contains the methodology and examples; no previous conversation, Agent-Diff repository, AppWorld repository, or companion methodology document is required to understand it.

You still need the target benchmark's allowed evidence: its test entries, referenced initial-state data, API definitions, and API documentation. Locate those in the supplied material. Ask for essential missing evidence instead of inventing it or expanding the evidence boundary.

The measurement is about **the benchmark**, specifically:

1. What grounding obligations its prompt requires in its supplied seed state.
2. Which of those obligations its assertions constrain through the resulting state or requested output.

Do not measure a solving agent's intelligence, actual retrievals, reasoning, trajectories, score, or behavior. Do not turn coverage measurements into predictions about random or capable agents. Such interpretation is a separate, later activity.

The required completeness is coverage of all requested tests and their grounding obligations. It is **not** exhaustive discovery of every possible identifying attribute set. The agreed card schema must remain fixed. Put evidence, explanations, uncertainties, and validation information outside the cards.

Agent-Diff and AppWorld are benchmarks used for examples below. Their implementation details are not part of this protocol. Any separate experiment called `systematic modeling/`, or any conceptual/behavioral modeling process that takes implementation code as authoritative, is **out of scope and irrelevant to this work**.

## 2. Authoritative evidence and its limits

Use only these four evidence categories:

| Allowed source | Role |
|---|---|
| Full test entry | The prompt defines the requested subjects and outcomes. Annotations, metadata, expected answers, and assertions provide supporting information. |
| Referenced seed or supplied initial-state snapshot | Supplies candidate records, relationships, and instance-specific evidence for resolving descriptions. |
| API definitions | Establish documented operations, parameters, and available projections where specified. |
| API documentation | Establish documented field meanings, interface behavior, and relationships needed to interpret the seed and operations. |

Do not consult service implementation, evaluator implementation, database schema/model code, migrations, initialization code, live databases, execution traces, or results from agents solving the benchmark. A seed is allowed; discovering undocumented runtime defaults by reading a seeder or ORM is not. API definitions do not mean following their implementation into handlers and helpers.

Do not require an external conceptual ER model. Use native entity/attribute vocabulary from the seed and test entry, with a small source map connecting it to documented API vocabulary. For example:

| Native attribute | Documented interface representation |
|---|---|
| `channels.channel_name` | Conversation response `name` |
| `channels.channel_id` | Conversation response `id`; posting input `channel` |
| `messages.message_text` | Message response `text`; posting input `text` |

This map is a translation aid supported by the allowed evidence, not another authority or an implementation-parity claim. Build it once per service and extend it as tasks require. Do not assume that a field in the seed is solver-accessible merely because it exists there. If essential interface evidence is missing, record the limitation outside the cards and seek the missing definition/documentation; do not invent a supported identifying alternative.

Record exact local source locations and, when practical, content hashes. For external documentation, record the exact page and retrieval date or a supplied version. These records belong with supporting evidence, not in card fields. Do not assume every test uses the same seed, actor, or workspace; inspect each entry's reference.

The study adopts the working assumption that assertions often check only a subset of the intended requirements. Use that assumption to support permissive boundaries, but never silently replace prompt meaning with an unrelated assertion. If the allowed evidence exposes a discrepancy, describe it. An assertion can corroborate a referent without constituting a faithful check of the requested operation.

Assertions must **not manufacture task obligations**. Begin with the prompt and seed; only then map assertions onto counted obligations.

## 3. Core concepts

### 3.1 Grounding obligation

A grounding obligation is:

> A requirement to resolve one described entity or entity set in the environment, either as an action target or as evidence needed to answer the request.

The unit is an independently described subject whose match to environmental evidence must be established. It is not a record count, field count, API-call count, retrieval count, operation count, or number of hops through relationships.

| Request | Obligations | Reason |
|---|---:|---|
| Read David's email about tomorrow's meeting. | 1 | Resolve the described email. David is a qualifier, not automatically another requested subject. |
| Reply to David's email about tomorrow's meeting. | 1 | The existing email is the referent; the reply is new. |
| Delete last month's receipts. | 1 | Resolve one described set, however many receipts it contains. |
| Attach the budget spreadsheet to David's meeting email. | 2 | Resolve the separately described spreadsheet and email. |
| Compare posture and meditation habit streaks. | 2 | Each independently described habit needs its own evidence match, even if the same logs support both. |
| Add Morgan Stanley to random. | 2 | Resolve the named person and the named destination channel. |
| Create a channel named rl-project. | 0 | The name specifies a new entity; no existing referent is described. |
| Create rl-project and add Morgan Stanley. | 1 | Resolve Morgan. The created channel's returned handle is an output of the task. |
| Find the author of the captcha message and DM them. | 1 | The requested subject is the author; the message is identifying evidence. |

Count repeated uses of the same described subject once. Reading a person's profile, inviting them, and messaging them can share one person obligation. Do not add obligations for optional contact lookup, pagination, authentication setup, or traversing an intermediate relationship.

Two independently requested subjects can share records or queries. Conversely, a single subject can require several joins or operations. Count from the request, not a proposed implementation plan.

Contextual mentions are not automatically requests to resolve a person or object. A task's creator saying “Sophie suggested this project” does not itself require grounding Sophie. A later instruction to invite her does.

An API may resolve a supplied name internally. That changes where resolution occurs, not whether the task describes a referent. An identifier explicitly supplied in the prompt can be used in an identifying rule. An identifier found only in the answer key is an audit reference, not a hidden solver input.

### 3.2 Instance-specific conditional counting — final rule

Count obligations **required by the task in its supplied seed state**:

1. Count subjects needed to determine which condition holds. Resolving them may establish presence or absence.
2. Count additional subjects required by the applicable branch.
3. Exclude subjects used only in a branch that the seed establishes is inactive.
4. If allowed evidence cannot settle the condition, retain potentially required obligations and explain the uncertainty outside the cards. Uncertainty must not silently reduce the count.

For “invite ElonMusk to general; if he cannot be found, notify Hubert,” a seed with no ElonMusk requires grounding **ElonMusk and Hubert: two obligations**. Exclude general, whose only use is in the inactive invitation branch. General may exist; an excluded branch target is not an absent referent.

An assertion forbidding additions to general can still be documented as an assertion, but it covers no counted destination obligation in this instance. Do not count the destination merely to give that assertion a coverage entry.

For “if there are fewer than seven active private conversations, open more; if there are more, remove some,” a seed with one existing conversation requires the existing-conversation set and the eligible users for new conversations. Inactive removal targets are excluded. The number of condition checks or loops does not multiply obligations.

Do not create targets from tentative suggestions such as “we may need to streamline membership” unless the prompt actually requires resolving a removal set. State your interpretation in the table's notes when the distinction matters.

### 3.3 Scope, referents, and identification

Let `U` be the scoped candidate population and `S` the justified referent set for one obligation.

**Shared scope** fixes environmental context before the identifying alternatives: for example, the authenticated account's notes, a supplied workspace, or the current actor's accessible environment. Scope supplied by the task/environment need not be repeatedly listed as a solver-disambiguated attribute.

Do not hide a selection decision inside scope. If finding a channel by name is needed to select messages, expose the relevant naming/join attributes or explain the already-grounded dependency. “The correct channel” is not a justified scope by itself.

**Identifying attributes** are source attributes used by a supported selection rule to select the relevant entities from `U`. An attribute set is sufficient in this instance if its rule selects exactly `S`.

Different sufficient sets can select the same referents. They need not be interchangeable in another seed state, necessary, or minimal. One supported alternative is a useful result; a longer attribute set can be valid. Another spelling of the same predicate over the same attribute set does not automatically create another card alternative.

Reading a field does not automatically make it identifying. Include it because of its role in selection, not because it appeared somewhere during analysis. Join keys are source attributes when the selector uses them. Record IDs retained only as output/comparison handles must not become undeclared selection inputs.

### 3.4 Resolution and permissive boundaries

| Resolution | Meaning | `Referent set` |
|---|---|---|
| `resolved` | The adopted boundary yields a justified nonempty set. | Explicit list of handles |
| `absent` | A sufficiently concrete description has no match in the supplied scoped evidence. | `[]` |
| `underspecified` | The description/evidence does not justify a referent set. | `null` |

“Cannot justify which person” is not the same as “the named person does not exist.” Missing observations or incomplete visibility also do not prove absence. An empty reference needs a semantic explanation of the description and the population searched, not just a predicate contrived to return nothing.

Use **permissive**, defensible inclusion boundaries when narrower boundaries require subjective judgment:

- For reviewing a named channel's discussion, the channel can be the grounded source container. Do not require an exact subjective subset of relevant messages when that precision is unnecessary.
- For state-changing uses, valid assertion constraints can guide a permissive boundary. Document that choice; do not describe it as an exhaustive interpretation of a broader prompt.
- When no reasonable boundary is justified, use `underspecified`. “Channels that might be relevant to our newly introduced event” need not become a fabricated exact set or a falsely proven empty set.
- For “choose one” requests, list all justified eligible targets and say **choose one** in the description. The set's cardinality counts eligible referents, not requested actions. Do not interpret six eligible messages as an instruction to react to all six.
- A condition requiring an empty/nonempty result still creates an obligation. Absence is a possible resolution, not zero obligations.

The absence of an assertion means an obligation is unchecked, not necessarily read-only. A requested reaction or removal is state-changing even if the answer key ignores it.

### 3.5 Computation and writes

Separate three roles:

1. **Identifying attributes:** which records are relevant?
2. **Answer/change-computation attributes:** which environmental values determine the answer or requested write values after selection, together with prompt instructions/constants?
3. **Written attributes:** which destination fields are assigned by the task-directed operation?

A field can have more than one role. A file path can identify Markdown files in a directory and supply the filename for a new note title. A channel name can identify a channel; its resulting ID can supply the destination field of a new message.

Prompt-only replacements need no environmental inputs to compute the new value. Renaming an identified note to “Shopping” can have an empty change-computation set. Keep target handles distinct from fields used to derive replacement values. Include IDs when they supply references written into other records; do not require every audit handle as an identifying attribute.

The grounding set need not be the write-target set. Importing files grounds source files and creates destination notes. Reading evidence to edit an existing document may require separate source and target obligations.

Computation fields on a multi-obligation card describe that subject's contribution. They are not a claim that the individual card alone completes the entire task. Other grounded subjects, prompt constants, and generated output handles can contribute to the same operation. For a grounded source container, related history/member records may supply computation data through documented relationships; make that traversal explicit outside the card.

Do not turn small, downstream answer-computation gaps into new grounding obligations. For example, Sophie and Olena can be unambiguously identifiable even if their supplied profiles omit job titles. Keep the person resolutions; do not make job-title completeness a separate research project. Do not invent missing values or claim a full answer-computation proof in such cases. A missing role used to **identify** an unnamed “engineering lead,” however, can prevent grounding that person and must not be ignored.

## 4. Fixed outputs

### 4.1 Table first

For each test, first produce a table with one row per counted obligation:

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Descriptive obligation name | resolved / absent / underspecified | Explicit handles / `[]` / undetermined | yes / partial / no | Relevant assertion indices and a concise reason |

Keep the test identifier and prompt with the table, outside the cards. Record boundary choices, selection rules, conditional exclusions, source references, and unresolved decisions in supporting notes. Empty-obligation tests still need a table/report entry explaining why there are no cards. Do not create a placeholder obligation for a creation-only task.

Associate every card with its table row by parent test and obligation position/name. Keep multiple obligations separate; do not flatten their scopes, referents, or alternative attribute sets into one task-wide selection.

### 4.2 Locked card schema

Every card has these exact common fields, with no additions:

```yaml
Test ID: <stable test identifier>
Task type: <read-only or state-changing>
Grounding obligations: <total counted obligations for this test>
Grounding obligation name: <short descriptive name>
Grounding obligation description: <what must be resolved and its use>
Resolution: <resolved or absent or underspecified>
Shared scope: <candidate population and supplied context>
Referent set: <list of handles, [], or null>
Alternative sufficient identifying sets:
  - [<source attributes for one sufficient selector>]
```

Read-only cards add **only**:

```yaml
Answer-computation attributes:
  - [<source attributes contributing to the requested answer>]
```

State-changing cards add **only**:

```yaml
Change-computation attributes:
  - [<source attributes contributing to the requested changes>]
Written attributes:
  - <destination field>
```

YAML or JSON may serialize the same schema. Do not add `Prompt`, `Seed template`, `Validation`, `Selection witness`, `Transformation witness`, `Assertion coverage`, source citations, or new status fields to cards. Their information belongs outside the card. Obtain an explicit decision before changing the schema.

Field conventions:

- `Grounding obligations` repeats the parent test's total on each card. Count cards once; **never sum this repeated field across cards**.
- `Task type` describes the obligation's use. A mixed task may have read-only evidence-for-reporting cards and state-changing cards. A source whose information is written into another environment record contributes to a state change.
- A referent handle can be a native ID or a composite identity. Do not invent a scalar ID for an association whose seed identity consists of several fields.
- Each inner list in an identifying/computation field is an alternative **set**, not a procedure or an ordered pipeline.
- `[[]]` means one empty attribute set, for example selecting the entire already-fixed population or computing a value entirely from prompt constants.
- For an underspecified obligation, use `null` for its referent set and unestablished identifying/computation alternatives. Do not substitute an empty set or invent a candidate selector.
- A concrete absent subject can retain a supported identifying alternative whose predicate yields no matches. Its `Resolution` is `absent` and its `Referent set` is `[]`.
- `Written attributes: []` is appropriate for pure deletion/removal, where no destination field is assigned. The operation is explained by the obligation description and supporting notes; do not invent fields called “deleted.”
- Exclude automatic timestamps, generated IDs, and authentication-supplied actor fields from task-directed written fields unless the request actually requires setting them. Keep newly generated handles outside the initial referent sets.

### 4.3 Measurements

For each test report:

- Total counted obligations.
- Resolved, absent, and underspecified counts.
- Fully covered (`yes`), partially covered (`partial`), and unchecked (`no`) counts.
- Not fully covered: `partial + no`.
- Full-coverage fraction: `yes / total`, or `null` when the test has no obligations.

Aggregate by summing the per-test counts. Keep the denominator inclusive of absent and underspecified obligations. Provide the cross-tabulation of resolution by coverage and a machine-readable per-test table. Preserve a count of zero-obligation tests; they are not 100%-covered tasks or failed tasks.

Do not collapse partial and full into one “covered” statistic without explicitly labeling that different measure. Do not weight obligations by the number of assertions, API calls, records, or eligible targets. Do not present these measurements as agent scores or capability findings.

## 5. Assertion coverage: final outcomes, never trajectories

Assess each assertion against the counted obligation's contribution to the **resulting state or requested source-dependent output**.

| Label | Decision standard |
|---|---|
| `yes` | Assertions constrain the relevant referent(s)/eligible target population in the resulting state, or adequately check the requested source-dependent answer at the adopted boundary. |
| `partial` | They constrain something relevant but leave a concrete gap: an incorrect/incomplete grounded answer can satisfy the predicate, an action can target an insufficiently constrained entity, or a required member of a target set can be omitted. |
| `no` | They impose no identifiable constraint on this obligation's referents or source-dependent result. Generic changes and authentication identity alone do not count. |

If assertion specifications are missing or cannot be interpreted from the allowed evidence, raise the concrete case to the user. Do not assign `no` or another coverage label merely to complete the table. Record the pending issue outside the cards, continue independent work, and do not finalize affected coverage measurements until the user resolves it. This differs from inspecting available assertions and establishing that none checks an obligation.

Do **not** require a retrieval trace, intermediate state, evidence that a particular record was read, source citations, explicit source IDs in an answer, or internal reasoning. Different procedures or source selections producing the same correctly checked answer are indistinguishable by design. That is not a coverage defect.

An exact requested aggregate can be fully checked without identifying its constituent records in the output. A faithful summary can be checked through its factual content without inspecting the steps used to produce it. Such checking might use specific factual predicates, a human, or an LLM judge; this protocol does not require one particular checker technology.

An output handle can be derived from a grounded referent. If a question is a reply in a thread and the documented API posts responses using the thread's root timestamp, an assertion fixing that root can fully constrain the reply destination. It need not require the question's own timestamp in the new message.

Inspect the **actual predicate**, not merely its description or presence of a relevant keyword. A number somewhere in text need not be the asserted count. A name somewhere in a report need not be assigned the right role. A predicate saying `user_id in [A, B, C]` with a count of three membership rows need not require all three distinct people, because a person can appear in different conversations.

Coverage is instance-specific. A channel/content predicate on a removed record can uniquely identify the intended seeded message without an explicit message ID. Do not demand IDs when other checked values already identify the referent sufficiently.

Coverage is not full task correctness. A named recipient's identity may be constrained by a membership assertion even when the message-to-conversation link is omitted. Record that linkage limitation outside the card. Do not add a new initial-state obligation for a newly created conversation to account for it. When a separately counted source/report obligation has incomplete asserted content, label that contribution accordingly.

For each partial label, write a concrete **final-output or final-state gap**. Where practical, give a small illustrative output or state that meets the relevant predicate but fails the requested contribution. Check whether other relevant assertions eliminate the example. If only a named text predicate was checked, say so; do not claim a full benchmark pass, runtime reachability, or an actual agent run.

Do not label partial solely because of missing source provenance, harmless formatting differences, or absence of a trajectory. Do not expand this study into proving consistency of every possible surrounding sentence. Judge whether the assertion checks the requested fact, target, or set at the adopted boundary.

## 6. End-to-end workflow for a fresh session

1. **Inventory the requested scope.** Locate all in-scope full test entries, count them, preserve stable IDs/order, and identify each referenced seed and actor/context. Locate the allowed API definitions/docs. Do not assume another service's seed or one shared seed for all tests.
2. **Record evidence boundaries.** List permitted source locations/versions and exclusions. Build only the native-field/API source mappings needed for the tasks. Record missing essential documentation rather than reading implementation.
3. **Read each prompt for subjects before evaluating its assertions.** Mark independently described entities/sets, repeated uses, qualifiers, new outputs, contextual mentions, and conditional branches. Metadata such as create+read, single/multi, explicit/implicit information, or ambiguity can guide attention but cannot determine the count.
4. **Resolve applicable branches against the supplied seed.** Count condition-resolving subjects and active-branch subjects. Exclude established inactive-branch-only subjects. Retain potentially needed subjects where the condition remains unsettled.
5. **Write the first-stage table.** Establish candidate scopes, supported reference sets, and resolution states. Prefer justified broad boundaries to arbitrary narrow relevance judgments. Record choose-one semantics and distinguish absent from unknown.
6. **Inspect assertions for their contribution.** Map actual predicates to the counted rows; record one-based assertion indices or an equally stable native reference. Use valid assertions to guide ambiguous mutation boundaries where appropriate, but never create subjects just because a predicate names them. Assess final-state/output coverage using Section 5.
7. **Construct one locked card per row.** Give each resolved/absent card supported identifying attributes with a selection explanation outside the card. Keep sources and write targets distinct. Classify local computation contributions without investigating irrelevant downstream gaps. Do not expand the schema.
8. **Review decisions across tests.** Check that similar descriptions, repeated names, conditional branches, choose-one requests, absent subjects, aggregates, and summaries receive consistent treatment. For any new convention that materially affects counts or labels, ask a concise question with the concrete case while continuing independent work. Record the decision outside cards; do not silently invent policy.
9. **Validate what can be validated within the evidence boundary.** Recompute literal name/content selectors, joins, timestamps, memberships, and relevant scalar answers from supplied data where practical. Check missing/extra referents. For semantic selectors, preserve the human-readable justification and say whether execution checks were performed. Do not claim implementation or semantic certification from a structural validator.
10. **Render and reconcile artifacts.** Produce readable tables, cards, supporting notes, and machine-readable measurements from one maintained annotation source. Verify all tests appear, every counted row has exactly one card, references/fields/assertion indices exist in allowed evidence, null/empty conventions hold, and all counts reconcile. Distinguish generated files from the annotation source.
11. **Report results within scope.** State the tested population, obligation/resolution counts, full/partial/unchecked counts, validation actually performed, and outstanding source/interpretation limitations. Link or provide the artifacts. Make no agent-performance inference.

A structural utility can enforce keys, referent existence, attribute names, assertion-index bounds, counts, and generated-file freshness. It is not the independently protected proof checker described later. Do not describe self-authored consistency checks as independent semantic validation.

## 7. Worked examples requiring no external repository

The instance facts below are supplied as part of the examples. They illustrate annotation decisions; they are not a complete downloadable benchmark fixture or a request to verify the historical benchmarks. Apply the method to the actual supplied evidence when analyzing a new task.

### 7.1 One destination: Agent-Diff `slack_57`

Prompt: **Send a 'hello' message to the general channel.**

The full entry describes a create+read task, a single entity scope, explicit information, and low ambiguity. It specifies workspace context and actor `U01AGENBOT9`. These annotations are hints: explicit information supplies a channel description and text, not an exemption from grounding; create+read does not itself establish an obligation count.

Relevant seed facts:

- The workspace is `T01WORKSPACE`.
- Exactly one channel has `channel_name = "general"`; its `channel_id` is `C01ABCD1234`.
- The actor belongs to that channel.

Documented API facts: conversation listing exposes channel `name` and `id`; message posting accepts a `channel` and `text`. Thus `channels.channel_name` identifies the referent, and `channels.channel_id` supplies the new message's destination.

The assertion requires one added `messages` record with `channel_id == "C01ABCD1234"` and `message_text` containing `"hello"`. It checks the destination obligation. Its looser text check is not proof that every aspect of the task is perfectly evaluated.

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve the general channel | resolved | `[C01ABCD1234]` | yes | The added message's destination is fixed to the intended channel. |

```yaml
Test ID: slack_57
Task type: state-changing
Grounding obligations: 1
Grounding obligation name: Resolve the general channel
Grounding obligation description: >
  Identify the existing channel named general as the destination
  for the new message.
Resolution: resolved
Shared scope: >
  Channels in workspace T01WORKSPACE accessible in the supplied
  environment to acting user U01AGENBOT9.
Referent set: [C01ABCD1234]
Alternative sufficient identifying sets:
  - [channels.channel_name]
Change-computation attributes:
  - [channels.channel_id]
Written attributes:
  - messages.channel_id
  - messages.message_text
```

Supporting selection rule: `channel_name == "general"`. Transformation: create one message with the selected ID and literal text `"hello"`. The ID in the referent set/answer is an audit target; it must not replace the name-based selector with an answer-key lookup.

The new message is not another initial-state obligation. A documented interface that accepts the channel name directly would not remove the destination obligation or imply that two API calls are mandatory.

### 7.2 Eight obligations, no covered referents: Agent-Diff `slack_98`

Prompt:

> I need your help coordinating something for our Polish-Ukrainian debugging session today. We're calling it the "Pierogi vs Varenyky Debug Session" because Olena and Sophie are bringing food during our break!
>
> First, can you check on Sophie Dubois and Olena Petrenko's profiles? I want to make sure I have their roles right when I introduce them to the rest of the team. Also, I need to catch up on what's been happening in the engineering channel — there were some login issues discussed that might be relevant.
>
> Could you find any channels that might already be discussing this topic, and if there isn't a dedicated space yet, please create a new channel for our pierogi-vs-varenyky session? We should also post a heads-up in core-infra about our debugging plans.
>
> Oh, and Aisha left a great message earlier that I want to react to with a thumbs up. Also, I need to remove someone from one of our project channels who's no longer on the team. Thanks!

Relevant instance facts: Sophie and Olena have unique profiles `U_SOPHIE` and `U_OLENA`. Engineering is `C03IJKL9012`; core-infra is `C_INFRA`. Engineering has four explicit login-issue messages and other discussion. Aisha has six messages, with no clear discriminator for “great.” The seed supplies no justified identity for the departed person or the project channel for removal. It also does not justify an interpretation that uniquely establishes the session-related channel set. Merely finding no channel with the new session's name does not prove that no existing channel discusses the topic.

The assertions require only at least one added public channel and at least one added message. Neither predicate constrains names, destination, message content, profile checks, reaction target, or removal targets.

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve Sophie Dubois's profile | resolved | `[U_SOPHIE]` | no | Neither assertion constrains it. |
| 2. Resolve Olena Petrenko's profile | resolved | `[U_OLENA]` | no | Neither assertion constrains it. |
| 3. Resolve engineering as the discussion source | resolved | `[C03IJKL9012]` | no | Generic message creation does not check the requested review. |
| 4. Resolve channels already discussing the session topic | underspecified | Undetermined | no | Generic channel creation does not establish this set or the condition. |
| 5. Resolve core-infra as the announcement destination | resolved | `[C_INFRA]` | no | The added message's destination is unrestricted. |
| 6. Resolve Aisha's earlier great message | underspecified | Undetermined | no | No reaction-target check. |
| 7. Resolve the person no longer on the team | underspecified | Undetermined | no | No person/removal check. |
| 8. Resolve the project channel for removal | underspecified | Undetermined | no | No channel/removal check. |

The reporting boundary for obligation 3 deliberately stops at engineering. Do not invent a required exact subset of its messages. Aisha's name qualifies her described message, not an independent request to inspect Aisha. By contrast, the removal has separately required person and channel subjects. The unresolved condition in obligation 4 does not silently erase potentially required work; creating a new channel would still introduce no initial-state destination referent.

Example card for the unresolved message:

```yaml
Test ID: slack_98
Task type: state-changing
Grounding obligations: 8
Grounding obligation name: Resolve Aisha's earlier great message
Grounding obligation description: >
  Identify the existing message described as Aisha's earlier great
  message as the target of a thumbs-up reaction.
Resolution: underspecified
Shared scope: >
  Messages in the supplied Slack workspace available to the acting user.
Referent set: null
Alternative sufficient identifying sets: null
Change-computation attributes: null
Written attributes:
  - message_reactions.message_id
  - message_reactions.reaction_type
```

Report **8 obligations: 4 resolved, 4 underspecified; 0 full, 0 partial, 8 unchecked**. Do not report what score a random or capable agent would receive. Missing job titles in the named profiles do not change their identity-grounding status.

### 7.3 Absence and an inactive branch: Agent-Diff `slack_88`

Prompt: **Try to invite the user 'ElonMusk' to general. If you can't find him, inform me (Hubert) via Slack.**

Seed facts: no user's username, display name, or real name matches ElonMusk. Hubert Marek exists as `U06HUBERT23`. General exists as `C01ABCD1234`.

Assertions require: zero added memberships in general; one added DM; one actor-authored message matching `find|found|unable|couldn't|could not|not exist`; and one membership addition for Hubert.

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve ElonMusk | absent | `[]` | partial | The failure-related text predicate allows incorrect polarity, such as “ElonMusk was found.” |
| 2. Resolve Hubert as notification recipient | resolved | `[U06HUBERT23]` | yes | A membership addition explicitly fixes Hubert's identity; delivery linkage is not thereby certified. |

General is excluded because only the inactive invitation branch uses it. Do not mark general absent or create a third card to account for the zero-addition assertion.

```yaml
Test ID: slack_88
Task type: state-changing
Grounding obligations: 2
Grounding obligation name: Resolve the user ElonMusk
Grounding obligation description: >
  Determine whether the explicitly named user exists, selecting
  the applicable invitation or absence-notification branch.
Resolution: absent
Shared scope: Users in the supplied workspace.
Referent set: []
Alternative sufficient identifying sets:
  - [users.username, users.display_name, users.real_name]
Change-computation attributes:
  - []
Written attributes:
  - messages.message_text
```

The absent result supplies the branch condition; the failure notification's wording can come from the prompt and the established absence. Hubert's separate card supplies the notification-recipient contribution. No output evidence of a failed lookup is required for coverage; the defect in the example assertion is its acceptance of a false final report.

### 7.4 A permitted choose-one set: Agent-Diff `slack_112`

The request includes: **Find the single best message in growth and mark it with a honey-pot reaction.** Growth has six messages. The assertion permits one reaction on any of those six message IDs.

Use a resolved obligation with all six IDs as the eligible referent set. Describe the action as choosing **one** eligible message. The assertion fully covers that permissive target boundary. Do not invent a ranking, arbitrarily pick one canonical “best,” require six reactions, or label the obligation underspecified merely because the prompt uses “best.” The explicit eligible-set assertion supplies the adopted permissive boundary.

This differs from Aisha's “great message” in the previous example, where no justified candidate boundary or constraining assertion distinguishes the intended target.

### 7.5 Outcome-coverage calibration cases

These examples distinguish genuine outcome gaps from demands for source provenance. They describe the named predicates, not executed agent runs.

| Requested contribution | Assertion | Classification and reason |
|---|---|---|
| Faithfully summarize a Gemini discussion. | Output contains `Gemini`. | **Partial:** “I will not summarize the Gemini discussion” contains no summary facts but meets the keyword condition. |
| Report Nick's number of channels; the seed-derived answer is 1. | Output matches `PALIMPSEST COMPLETE:\s*1\s+channels?\s+found\s+for\s+Nick`. | **Full:** the required scalar is bound to the requested statement. The channel's name/ID and a counting trace are unnecessary. |
| Report the number of messages mentioning supercomputer; answer 2. | Output matches `(?i)supercomputer.*\b2\b`. | **Partial:** “supercomputer mentioned 99 times; 2 reviewers checked this” does not report the correct count. The issue is the regex's factual binding, not missing message IDs. |
| Return engineering's member count and names; count 5. | One message contains `5`; a message contains `member`. | **Partial:** “Member count: 15. No names provided” meets these text conditions. |
| Name the admins; correct people are Robert Walsh and Morgan Freeman. | Output contains `Robert` and `Morgan`. | **Partial:** “Robert Chen and Morgan Stanley” gives the wrong seeded people while satisfying the fragments. |
| Answer Robert's question in its existing circuit-tracer thread. | Reply has the correct channel and root `parent_id`. | **Full for destination:** the documented reply handle is the parent thread, even though Robert's question has its own different timestamp. |
| Report Sophie's completion estimate, Wednesday next week. | Reply contains `Wednesday`. | **Partial:** “Completion is Friday next week; Wednesday is only a review meeting” satisfies the word check but misstates completion. |
| Report two thread replies and their authors Robert and Kenji. | Output matches `Field Report 2: ... 2 replies ... circuit-tracer ... robert ... kenji`. | **Partial:** it can list Robert and Aisha as authors and mention Kenji later as report preparer. Names must be attributed correctly in the final answer; reply IDs are unnecessary. |
| Edit an espresso-machine message in random. | Any message in random is edited. | **Partial:** the edited record can be unrelated to espresso. This is a final-target gap. |
| Invite each of five named people. | At least five membership rows have user IDs in the five-person list. | **Partial:** repeated people across different channels can satisfy the row count without every required person. This is not a concern about API-call order. |
| Reach seven active private conversations starting from one. | Six DM records are added, with some users excluded. | **Partial if final actor membership/activity/total and intended counterparts remain unchecked:** no evidence of the counting or sorting steps is needed. |

The refined Slack coverage audit promoted the reply-destination and Nick-count obligations. Other cases stayed partial for concrete final-content/state gaps. It did not change their grounding cards or referent sets. The later conditional-branch decision separately removed general from `slack_88`.

As a historical consistency checkpoint only, the agreed Slack measurements after those decisions were **197 obligations: 77 full, 34 partial, 86 unchecked**. These totals are not a target to reproduce for other datasets or a substitute for re-reading their evidence.

### 7.6 Original read-only illustration: AppWorld posture logs

Prompt: **What is my longest practiced-good-posture habit streak, in number of days, as per my Simple Note habit tracking logs?**

Supplied instance facts:

- The authenticated account has 34 notes; 24 daily habit logs, IDs 11–34, span April 24–May 17, 2023.
- Each relevant title follows `Habit Tracking Log for YYYY-MM-DD`, each has the `habit-tracker` tag, and each body has a daily-tracker heading and a `practiced_good_posture: yes/no` entry.
- In this instance each of those three identifying rules selects exactly those 24 logs. Grocery notes do not match.
- The logged date and creation date agree for every selected log. The longest affirmative runs are April 30–May 3 and May 10–May 13: four days each.
- The documented note API exposes title, tags, content, and creation date. A structured `note.data` field is not exposed and is excluded from solver-accessible alternatives.

A negative log is still relevant: it can break a streak. Selecting only `yes` observations would remove relevant evidence. Collection tags identify the right logs here because all selected logs contain the requested habit, not because the tag itself asserts a positive outcome.

```yaml
Test ID: appworld_0a9d82a_1
Task type: read-only
Grounding obligations: 1
Grounding obligation name: Resolve posture habit-tracking logs
Grounding obligation description: >
  Resolve the user's daily logs containing practiced-good-posture
  observations, including negative observations, for streak calculation.
Resolution: resolved
Shared scope: Notes of the authenticated task user, user_id == 1.
Referent set: [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
              23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]
Alternative sufficient identifying sets:
  - [note.title]
  - [note.tags]
  - [note.content]
Answer-computation attributes:
  - [note.title, note.content]
  - [note.created_at, note.content]
```

Supporting computation: extract date and outcome, order by date, and compute the longest consecutive affirmative run. Both listed computations give 4 under the supplied facts. Creation dates are not universally interchangeable with observation dates; this alternative depends on the stated instance property. Verifying that property may read titles, but those verification reads do not redefine the declared sufficient computation inputs.

This example establishes concepts, not assertion coverage: no actual answer predicate is supplied here from which to assign a coverage label.

### 7.7 Original import illustration: AppWorld Markdown files

Prompt: **Import Markdown notes in `~/documents/personal/notes/` into my Simple Note account. Each Markdown file becomes a separate note. Derive its title from the filename without path or extension, replacing underscores with spaces.**

Supplied instance facts: the task user is 40 in both applications, with 193 source files and no destination notes. Exactly 28 files, IDs 25851–25878, are Markdown files in the specified directory. Path and content are accessible through the documented file interface. Note creation accepts title and content.

```yaml
Test ID: appworld_0d01c76_1
Task type: state-changing
Grounding obligations: 1
Grounding obligation name: Resolve Markdown files in the source directory
Grounding obligation description: >
  Resolve the source Markdown files, each of which supplies the
  title and content of one new Simple Note note.
Resolution: resolved
Shared scope: Files of file-system user_id == 40.
Referent set: [25851, 25852, 25853, 25854, 25855, 25856, 25857,
              25858, 25859, 25860, 25861, 25862, 25863, 25864,
              25865, 25866, 25867, 25868, 25869, 25870, 25871,
              25872, 25873, 25874, 25875, 25876, 25877, 25878]
Alternative sufficient identifying sets:
  - [file.path]
Change-computation attributes:
  - [file.path, file.content]
Written attributes:
  - note.title
  - note.content
```

Selection: the path is within the specified directory at the intended directory depth and has the Markdown extension. Do not silently assume recursive import when directory-depth semantics are not established.

Transformation: for each selected file, create one note with transformed basename and copied content. For example, `/home/adam/documents/personal/notes/Book_Reading_Lists.md` supplies title `Book Reading Lists`. The original example's transformation was checked against 28 expected title/content pairs, with additions required and existing-note updates/deletions forbidden.

The files are grounded sources and remain unchanged. The notes are new outputs. The path plays both an identifying and a computation role. Generated destination IDs need not be predetermined. Exact coverage of an unfamiliar benchmark still requires its actual supplied assertions, not an assumption based on this illustration.

## 8. Proofs and the checker: preserve the distinction

The original grounding-obligation framework sought individually justified, executable proofs of sufficient alternatives. The current benchmark-measurement workflow retains semantic reference justification and practical selection checks, but does **not** require a complete task-solving proof for every card. Underspecified obligations remain useful measurements. Do not let a missing full proof erase them, and do not describe the current annotation process as full formal verification.

If a proof phase is requested, keep it separate from the card and within the same allowed evidence boundary. A proof does not authorize reading excluded implementations or querying a live database.

### 8.1 Three proof layers

**Establish the semantic reference.** Define `U` and justify `S` from the prompt and allowed environmental evidence. Explain why members belong and relevant nonmembers do not. Agreement between several selectors is insufficient: they could all agree on the wrong set. Assertion artifacts can support this reference without becoming hidden inputs to a proposed solver procedure.

**Verify identification.** For each alternative `A`, provide a concrete selector `P_A` using only its declared inputs and supplied context. Verify:

```text
selected = {r in U : P_A(r)}
missing  = S - selected = empty
extra    = selected - S = empty
```

For a choose-one card, this establishes the **eligible population**; the subsequent operation must select the required number from it. For an absent card, justify the description and test for no matches. There is no selection-equality proof against an invented fixed `S` for an underspecified card.

**Verify the computation or transformation.** For a simple record-set case:

```text
compute(project(S, declared_answer_attributes), prompt_parameters)
    == expected_answer

transform(project(S, declared_change_attributes), prompt_parameters)
    == required_effect
```

For multiple obligations or source containers, explicitly supply the declared related-record projections and other grounded contributions; do not hide extra reads inside the projection notation. Expected answers, referent IDs known only to the checker, and expected output mappings are verification targets, not inputs to the proposed computation.

For creation, compare meaningful values and multiplicity/source-to-output correspondence rather than fixed generated IDs. For imports, each source must produce its corresponding title/content pair exactly once. For mutations, verify intended effects and relevant unintended additions, edits, or removals. Do not infer correctness from an arbitrary solving agent's diff.

### 8.2 Author/checker separation

The proof author must not edit the checker or the trusted reference inputs it enforces. These are two executable components with separately controlled trusted inputs:

- **Trusted reference:** reviewed card, justified referents/eligible population, permitted prompt parameters, and the appropriate expected outcome specification.
- **Proof:** declared selectors and computations/transformations.
- **Checker:** enforces input/attribute restrictions, selection equality, allowed output effects, and agreement with the trusted outcome specification.

An immutable checker enforcing an inadequate reference still gives an inadequate guarantee. Distinguish “passes the benchmark's supplied assertions” from “satisfies the intended task.” Under weak assertions, the former cannot certify the latter. Do not let the proof author choose convenient referents or weaken expectations in order to pass.

The current measurement concerns the gap between task requirements and assertion coverage; it does not silently replace the supplied evaluator with a stronger one. A separate proof of intended task completion would need an independently justified intended outcome. A proof only of assertion satisfaction must say that is all it establishes.

A checker protecting declared inputs is about the proposed proof procedure's validity. It does not introduce a requirement that the benchmark evaluator observe the trajectory of a solving agent. Those are different questions.

### 8.3 What a successful proof does and does not establish

A successful proof establishes that one particular alternative is sufficient for the stated instance, scope, and documented accessible interface. It does not establish necessity, minimality, exhaustiveness, universality across seeds, or semantic-reference correctness merely because code ran.

If a semantic operator such as `ABOUT` is used, define its intended meaning. Being about a habit does not establish that the habit was practiced; being about an event does not establish attendance or agreement. Trace derived semantic fields back to the accessible source attributes that produced them.

If further alternative discovery is requested, an optional stopping rule is five consecutive attempts without a new validated attribute-set alternative. Reset the counter when a genuinely new validated alternative is found. A new SQL spelling over the same attributes is not necessarily a new alternative. This is a practical bounded search, not evidence of exhaustiveness, and is not mandatory for the current measurement pass.

## 9. Final review and precedence

Before handing off results, check:

1. Every in-scope test has an entry, including zero-obligation tasks.
2. Counts follow independently described subjects, actual seed-conditioned branches, and deduplication of repeated uses.
3. Absent, underspecified, and excluded-inactive-branch targets are not conflated.
4. Broad scopes and choose-one candidate sets have explicit, consistent meanings.
5. Sources, API mappings, semantic references, and any gaps remain reviewable without expanding the evidence boundary.
6. Cards use exactly the locked fields, with correct null/empty conventions and no proof/coverage metadata inserted.
7. Source-derived values and existing targets are not confused with new outputs or automatic fields.
8. Each coverage label is justified by final-state/output constraints. No label demands proof of retrieval, a trajectory, or unnecessary source IDs.
9. Partial labels identify a substantive accepted incorrect/incomplete outcome, not merely the use of an output matcher.
10. Per-test counts, aggregates, and resolution/coverage cross-counts reconcile. Repeated parent totals inside cards are not summed.
11. Structural checks, semantic review, predicate illustrations, and executable proofs are described accurately as different levels of validation.
12. The conclusion remains a measurement of the benchmark. Predictions about agent behavior are left for a separately requested analysis.

The following decisions are final and override earlier versions of the approach:

- The four-source evidence boundary replaces implementation-driven inspection.
- The table-first measurement workflow does not require the original full-proof program to finish before obligations can be recorded.
- The locked schema replaces earlier cards that contained prompt, seed, witness, or validation fields.
- Outcome-based coverage replaces the rule that source-derived words or counts are automatically partial without source-ID checks.
- Seed-conditioned branch counting replaces the provisional choice to count general in the inactive invitation branch of `slack_88`.

When adapting to a new domain, preserve these rules and change only the domain's source locations, native vocabulary/API mappings, and evidence-specific annotations. A genuinely new ambiguity should result in a concrete clarification and recorded decision, not an unannounced change to the method.
