# Slack grounding-obligation measurements

Methodology: [Grounding obligations protocol v1.0.1](../card%20extraction.md). The initial v1.0.1 review covers `slack_88`, `slack_98`, `slack_102`, `slack_111`, and `slack_112`. A second pass reviews only the 18 formerly underspecified obligations in `slack_94`, `slack_95`, `slack_96`, `slack_97`, `slack_99`, `slack_100`, `slack_101`, and `slack_103`; the boundary pass additionally reviews `slack_67` O1, `slack_74` O1, `slack_108` O6, `slack_110` O7, and `slack_113` O5. Other cards retain their prior semantic annotations; the overall structural and artifact-consistency checks cover all cards. Protocol versions are recorded outside cards at test or obligation level in `analysis.json` and the rendered documents. No Slack coverage decisions are currently pending because of missing or uninterpretable assertion specifications. Such cases must be raised to the user rather than labeled unchecked.

This directory annotates all **59 Slack tests** in `all_numbered.jsonl` (`slack_57`–`slack_115`). It measures the benchmark's expressed grounding obligations and the extent to which its existing assertions constrain their referents. It does not measure agents, predict their scores, or infer capability.

Start with [the per-test tables and aggregate counts](report.md), then [the cards](cards.md). [CSV measurements](metrics.csv) and [JSON measurements](metrics.json) are available for analysis. [cards.jsonl](cards.jsonl) contains the same cards without document headings.

[Downstream task specifications](task_specs.md) rewrite each prompt into lightly structured, numbered instructions with direct links to the existing obligation cards. Their machine-readable source is the per-test `task_spec` in [analysis.json](analysis.json).

The [focused coverage audit](coverage_audit.md) reviews all 36 initially partial obligations against the outcome-only standard. It promotes two to full coverage and retains 34 as partial, with revised explanations based on final content or final state.

## Fixed evidence boundary

Allowed evidence:

1. The full [test entry](../../datasets/agent-diff-bench/all_numbered.jsonl): prompt, annotations, metadata, and answer assertions.
2. Its referenced [slack_bench_v2 seed](../../examples/slack/seeds/slack_bench_v2.json).
3. The repository's [Slack API definitions](../../examples/slack/testsuites/slack_docs/slack_api_full_docs.json).
4. The explicitly listed API documentation in [sources.json](sources.json), mapped in [source_map.md](source_map.md).

Service implementation, evaluator implementation, live databases, agent runs/audit findings, and the separate conceptual ER model are excluded. Local source hashes are recorded. Public API documentation supports the interface mapping; this is not a claim that Agent-Diff faithfully implements every documented behavior. All entries specify the same seed and acting user, `U01AGENBOT9`.

The prompt defines described subjects. Metadata supplies hints, not counts. Assertions guide coverage and permissive mutation-related boundaries. As agreed for this study, assertions are treated as potentially incomplete requirements; apparent discrepancies are preserved in notes rather than silently substituted for prompt meaning. Source ambiguity remains visible.

## Counting and resolution

- Count each independently described entity or entity set once, even if it supports several operations. Separately named people and channels are separate obligations.
- A qualifier used to find a subject is not automatically another obligation: “the author of the captcha message” describes one user; a lookup of the qualifying message does not create another requested subject.
- Separate requests for a channel and its member roster can describe two subjects. A broad request to review a channel's discussion can stop at the channel as the source container.
- Contextual people, authentication identity, and names of entities newly created during the task do not automatically require resolving existing entities. Reusing a just-created channel or message does not add an initial-state grounding obligation.
- Count definite requests, including conditional requests relevant to this instance. Do not invent removal targets from tentative remarks such as “we may need to streamline membership.”
- Conditional requests are counted against the supplied seed: include subjects needed to determine which condition holds, then additional subjects required by the applicable branch. Exclude subjects used only in a branch the seed establishes is inactive. If the evidence cannot settle the condition, retain potentially required obligations and explain the uncertainty outside the cards; uncertainty alone does not remove an obligation.
- In `slack_88`, count ElonMusk (absent) and Hubert (notification recipient), but exclude general, which is only the inactive invitation destination. Exclusion does not mean absence: general exists. The assertion forbidding additions to general remains documented but creates no task obligation and contributes no separate covered obligation. In `slack_115`, count the existing conversations and eligible users for creation; the inactive removal branch adds no target set. These rules describe benchmark requirements, not an agent's lookups or execution history.
- `resolved`: the adopted description/boundary yields a justified nonempty referent set.
- `absent`: a sufficiently concrete description has no match in the supplied seed. This does not claim absence from a running service with different data.
- `underspecified`: competing interpretations or selections remain plausible, and the prompt and environment do not distinguish the intended set. Explain the unresolved choice; exhaustive enumeration is unnecessary. In v1.0.1 cards, represent it with `selection`, `partial_constraints`, and `candidate_sets`. Legacy v1 cards use `null`, which is not an empty set.
- Use permissive inclusion boundaries. In reporting, a named containing channel can be sufficient. For subjective mutation targets, supported assertion constraints may guide a permissive boundary, but cannot supply delegation missing from the prompt. A request for the best message delegates a choice; a reference to the user's remembered great message does not.
- For “choose one” tasks, the referent set lists eligible targets and the description explicitly says to choose one. Its cardinality is the number of eligible referents, not the number of required actions. This applies to `slack_112`. `slack_100` O7 delegates acknowledgment judgment without a fixed reaction count. In contrast, `slack_108` O6, `slack_110` O7, and `slack_113` O5 expect one intended target without delegating selection; their competing singleton sets are underspecified.

The analysis establishes one supported identifying alternative per resolved/absent card; it does not claim minimality or exhaustive alternative discovery. Selection rules and semantic explanations live outside the cards in the report and annotation data. Some rules are semantic descriptions, not executable proofs.

## Assertion coverage

Coverage is a property of the assertion predicates relative to the annotated obligation's contribution to the final state or requested output. It does not require a trajectory, intermediate state, evidence of retrieval, source citations, or a record of internal reasoning.

| Value | Meaning |
|---|---|
| `yes` | The assertions constrain the relevant referent(s)/eligible target population in the resulting state, or adequately check the requested source-dependent answer. An output value or derived destination can suffice without exposing source IDs. |
| `partial` | They constrain something relevant but leave a concrete gap in the grounded output or resulting state: an incomplete/incorrect report can pass, a target is only coarsely located, or a required member of a target set can be omitted. |
| `no` | They place no identifiable constraint on this obligation's referents or source-derived result. Generic additions and actor identity alone do not count. |

The user's clarification supersedes the initial convention that treated source-derived words/counts without source-identity checks as automatically partial. A correct count can fully check a count-only result: `slack_114` binds 1 to the requested statement about Nick. In contrast, `slack_110` permits the reported supercomputer count to be 99 with an unrelated 2 later in the text, so its actual predicate remains partial. `Gemini` alone does not check a faithful summary. These distinctions concern final-answer fidelity, never how the answer was obtained.

A source-dependent result need not reproduce its underlying records or IDs unless the prompt requests that information. Different procedures or source selections producing the same correctly checked answer are indistinguishable by design; that is not a coverage defect. Similarly, a reply uses the documented parent-thread handle: checking that final handle can cover the destination without recording which individual question was read.

Requiring a specific channel ID on an added message covers that destination. Requiring any public channel and any message covers none of `slack_98`'s eight described obligations. This is still grounded-contribution coverage, not certification of all task behavior or an exhaustive semantic validator for arbitrary surrounding prose.

Coverage is instance-specific: a content predicate on removed records can identify one seeded message without an explicit ID. Conversely, an aggregate membership count with `user_id in [...]` does not necessarily require every individual in that list. Assertion descriptions are hints; the actual predicate takes precedence when assessing coverage.

Identity coverage does not certify a whole operation or its links to other operations. A predicate can require Hubert's membership without tying it to the conversation receiving the message. A user identity is still constrained, but delivery linkage is not certified. The report states such limits rather than treating full referent coverage as full task correctness.

Per-test and aggregate counts separately report full, partial, and unchecked obligations. `not_fully_covered = partially_covered + unchecked`. Full coverage fraction is `fully_covered / obligations`; zero-obligation tests have `null`, not 0 or 1. The denominator includes resolved, absent, and underspecified obligations. Resolution/coverage cross-counts are included in JSON. No assertion-count weighting or agent-performance inference is applied.

## Locked card schema

Every card has exactly these common fields:

```text
Test ID
Task type
Grounding obligations
Grounding obligation name
Grounding obligation description
Resolution
Shared scope
Referent set
Alternative sufficient identifying sets
```

Read-only cards add `Answer-computation attributes`. State-changing cards add `Change-computation attributes` and `Written attributes`. No prompt, seed-template, validation, witness, coverage, or source fields are inserted into cards.

`Grounding obligations` repeats the parent test's total on each card; do not sum this field across cards. Card position within its test supplies the table association. `Task type` describes this obligation's use: evidence requested for reporting or an input/target of a state change. Mixed requests can therefore contain both types. Computation fields record the local contribution of a grounded subject, not a claim that each card alone completes the whole multi-obligation task. Cards can combine through the test's other grounded subjects, documented relationships, prompt constants, and newly created output handles.

Attribute names follow seed/test-entry vocabulary, with documented API mappings. `[[]]` is one empty identifying/computation alternative, for example selecting the entire scoped population. `null` means no alternative is established for an underspecified obligation. Source-container cards may compute using related records in the container's documented history or membership projection. Missing job-title/role details are outside the grounding measurement; profile cards record the accessible profile contribution without certifying a full role answer.

For migrated underspecified cards, `Referent set` has exactly `selection` (`one(entity)` or `set(entity)`), `partial_constraints` (predicates over real fields, or `[]`), and `candidate_sets` (concrete competing sets, or `null` if unenumerated). User intent and unrecorded facts stay in the description; do not invent departure or relationship fields. An empty inner candidate set is a possible absence alongside another interpretation, not an established absent resolution. Competing sets do not authorize arbitrary choice. Partial predicates are not sufficient identifying alternatives.

Current totals: **197 obligations: 166 resolved, 11 absent, 20 underspecified; 74 fully covered, 37 partially covered, 86 unchecked**.

The v1.0.1 reviews preserve obligation counts while distinguishing empty necessary populations from unresolved intent and explicitly delegated choice. All underspecified cards now use the structured referent representation. This does not claim that all prior semantic annotations have been re-derived.

For `slack_67` O1, all four lunch-question targets are required except the pizza-combo message, whose specific thumbs-down instruction is an agreed exception to the general thumbs-up request. Its coverage is partial because only two lunch targets are checked. `slack_74` O1 contains all eight question-bearing messages, including a confirmation tag question, independently of the four assertion keywords; coverage remains partial. Neither set is labeled permissive. Obligation overlap is allowed generally; the `slack_67` exception is task-specific.

`slack_108` O6, `slack_110` O7, and `slack_113` O5 preserve channel/topic constraints and competing singleton targets, with partial coverage. Contextual references can establish a topic match without an exact keyword. The user-approved delegated choices in `slack_112` and `slack_100` O7 remain unchanged.

`Written attributes: []` on a deletion/removal means no destination field is assigned; the described referent or relationship is removed. Generated IDs, authentication-supplied actor fields, and automatic timestamps are omitted. Changes driven by prompt constants can have empty computation inputs; routing/reference inputs are included when used to construct other records.

## Downstream task specifications

These specifications describe the task before execution. They support later assessment of grounding, requested operations and deliverables, and workflow; they contain no execution verdicts or new reward policy. The prompt supplies the request, with existing cards guiding reference interpretations. Weak assertions do not weaken the requested actions.

Each test has one `task_spec` list alongside its existing `obligations` and `notes`. Each line has exactly:

```json
{"line": 1, "text": "Send a 'hello' message to #general.", "obligations": [1]}
```

`line` is a consecutive, one-based identifier local to the test. `text` is one physical line of informal pseudocode; leading spaces express branch indentation. `obligations` lists the directly relevant, one-based positions in that test's existing obligation list. Together, test ID and line number identify a specification line. Conditions and branch markers also have line numbers, so counting lines does not count actions. Renumbering lines or reordering cards requires updating consumers of those identifiers.

Rewriting rules:

- Retain the original language where practical, including relevant context, scope, quantities, literal message text, formatting requirements, and unresolved descriptions. Preserve exact requested output strings even when they contain typos.
- An action is a requested operation or deliverable. Split different operations, such as setting a topic and posting an announcement. Keep a batch operation over a collection together. A single report can retain several required components.
- Use `then`, `after`, conditions, and indentation for requested sequences and dependencies on newly created objects. Other list order alone does not impose execution order. Keep alternative branches conditional and separate, including branches inactive in the supplied seed.
- Do not promote search, resolution, reading, computation, or preparation into extra actions unless their results are independently requested. Preserve an expressly requested review or count; integrate a lookup used only to supply a reply into that reply instruction. Tentative future work does not become a definite action.
- Link each line's direct targets and source-dependent content to existing cards. A line may link several obligations, and one obligation may link several lines. Resolve pronouns from the local task context, but do not propagate obligation links through control flow or merely because an earlier action had them. Contextual names alone do not require links: creating a channel for named people differs from inviting those people.
- Empty links are valid for branch markers, creation-only actions, and uses of newly created output handles. They do not mean an action is optional or completed. Do not invent obligations for inactive branch targets, intermediate lookups, or generated objects.
- Retain absent and underspecified references without supplying missing facts, selecting an arbitrary candidate, adding fallback behavior, or deleting the request. Preserve explicitly delegated choice and its permitted cardinality.

Examples and interpretation notes:

- [Slack 67](task_specs.md#slack_67) retains the agreed pizza-combo exception to the otherwise complete lunch-question set. [Slack 74](task_specs.md#slack_74) requires posting every question separately.
- [Slack 88](task_specs.md#slack_88) links the ElonMusk condition and invitation to O1, and the notification to Hubert to O2. The notification does not inherit O1 from its condition. The inactive #general destination does not gain a new card.
- [Slack 60](task_specs.md#slack_60) has a creation action and no obligation links. [Slack 111](task_specs.md#slack_111) similarly gives the reaction to the newly created schedule post no existing-referent link; the schedule content and invitations do link the named participants.
- [Slack 100](task_specs.md#slack_100) links the summary of gathered context to its channel/profile sources and its posting destination. Its acknowledgment choice retains the agreed discretion and has no fixed reaction count.
- [Slack 109](task_specs.md#slack_109) preserves join → inspect → leave, and asks the matching incognito user to change their nickname. It does not replace the requested ping with the assertion's membership addition.
- [Slack 115](task_specs.md#slack_115) preserves both branches. The creation branch's stopping point of seven follows the existing card's six eligible new users and the task's target of seven conversations. The removal line links the already-counted conversation set directly; it introduces no inactive removal-target card or link to the creation users.

The builder checks exact line fields, numbering, nonempty single-line text, valid nonduplicated obligation links, and that every existing obligation has at least one link. It does not parse workflow semantics or infer links. Prompt fidelity, appropriate granularity, and direct mappings require manual review. The specifications do not alter the locked grounding-card schema or the grounding/coverage counts.

## Reproducibility and review

[analysis.json](analysis.json) is the editable annotation source. It associates each locked card with its referent entity, semantic justification, selection description, assertion indices (one-based within the entry), and coverage explanation. These supporting fields are not card fields. All generated artifacts derive from this file.

```bash
python grounding/slack_analysis/build.py
python grounding/slack_analysis/build.py --check
```

The second command verifies schema keys, resolution/null conventions, referenced seed IDs, attribute names, assertion-index bounds, aggregate counts, known examples, task-spec line structure and obligation links, and generated-file freshness. It does not assess semantic correctness, execute API operations, interpret the full evaluator, or constitute a formal proof checker. No proof-author/checker security claim is made for this rendering/consistency utility.

The tables cover the complete Slack subset, with the initial coverage labels revised by the focused audit. Their semantic boundaries and coverage explanations are reviewable measurements, not a claim that interpretation has been eliminated. The audit changes no card fields, referent sets, resolution labels, or obligation counts. The original annotation is preserved in commit `2ec3342`.
