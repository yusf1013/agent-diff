# Slack grounding-obligation measurements

This directory annotates all **59 Slack tests** in `all_numbered.jsonl` (`slack_57`–`slack_115`). It measures the benchmark's expressed grounding obligations and the extent to which its existing assertions constrain their referents. It does not measure agents, predict their scores, or infer capability.

Start with [the per-test tables and aggregate counts](report.md), then [the cards](cards.md). [CSV measurements](metrics.csv) and [JSON measurements](metrics.json) are available for analysis. [cards.jsonl](cards.jsonl) contains the same cards without document headings.

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
- Provisional conditional convention for `slack_88`: retain an explicitly named destination in the task-expressed count even when its branch is inactive in the seed. Thus ElonMusk, general, and Hubert are three obligations. This optional clarification is recorded in the test notes; excluding the inactive destination would reduce overall obligations and full coverage by one each. No claim about necessary execution steps follows from including it.
- `resolved`: the adopted description/boundary yields a justified nonempty referent set.
- `absent`: a sufficiently concrete description has no match in the supplied seed. This does not claim absence from a running service with different data.
- `underspecified`: the available description/evidence does not justify a referent set. `null` is not an empty set.
- Use permissive inclusion boundaries. In reporting, a named containing channel can be sufficient. For subjective mutation targets, use supported assertion constraints rather than inventing precise relevance rankings.
- For “choose one” tasks, the referent set lists eligible targets and the description explicitly says to choose one. Its cardinality is the number of eligible referents, not the number of required actions. The user approved this convention for `slack_112`; it also applies to `slack_108`, `slack_110`, and `slack_113`.

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

`Written attributes: []` on a deletion/removal means no destination field is assigned; the described referent or relationship is removed. Generated IDs, authentication-supplied actor fields, and automatic timestamps are omitted. Changes driven by prompt constants can have empty computation inputs; routing/reference inputs are included when used to construct other records.

## Reproducibility and review

[analysis.json](analysis.json) is the editable annotation source. It associates each locked card with its referent entity, semantic justification, selection description, assertion indices (one-based within the entry), and coverage explanation. These supporting fields are not card fields. All generated artifacts derive from this file.

```bash
python grounding/slack_analysis/build.py
python grounding/slack_analysis/build.py --check
```

The second command verifies schema keys, resolution/null conventions, referenced seed IDs, attribute names, assertion-index bounds, aggregate counts, known examples, and generated-file freshness. It does not assess semantic correctness, execute API operations, interpret the full evaluator, or provide the independent proof checker discussed earlier. No proof-author/checker security claim is made for this rendering/consistency utility.

The tables cover the complete Slack subset, with the initial coverage labels revised by the focused audit. Their semantic boundaries and coverage explanations are reviewable measurements, not a claim that interpretation has been eliminated. The audit changes no card fields, referent sets, resolution labels, or obligation counts. The original annotation is preserved in commit `2ec3342`.
