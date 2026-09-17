# One-turn self-reflection: repairs, remaining defects and regressions

One generic follow-up improved four of ten sketches: **two now pass the conceptual
review and two remain only partly repaired**. Three previously satisfactory sketches
remain satisfactory. Two defective sketches remain materially unchanged. One call
exhausted its output budget without returning a final sketch.

The conceptual readiness count rises from **3/10 to 5/10**. This is a manual review
of authoring sketches, not a runnable-test validity rate or solver exposure rate.
W09's new conceptual readiness still requires the compiler to confirm realizable
workspace associations and read access. No compiler or solver was invoked.

Read [all nine revised sketches and the incomplete-call record](outputs.md),
[original ten sketches](../outputs.md), and [machine-readable manual comparison](comparison.json).

## Experiment design

- Each original conversation receives the same [six-step follow-up](followup.md).
  It asks the writer to extract actual selection conditions, keep shared facts
  consistent, recompute selection across the whole table, verify mode/counts,
  check the downstream operation and return minimal repairs.
- The original system prompt, user assignment and native assistant response
  (including thinking/signature blocks) are preserved. This is a chat continuation,
  not a new prompt containing a manually corrected version of the case.
- No case-specific diagnoses, manual assessments or other cases' outputs are
  supplied. The existing few-shot examples remain in each original conversation.
- Same Sonnet 5 model, medium effort and 6,000-output-token budget. One review per
  case; no semantic retries, resampling or selection of better attempts.
- All ten cases are reviewed, including the previously good cases, to check for
  regressions. Two sequential substantive calls verify caching; the remaining
  eight run in parallel.
- [Manifest](manifest.json) records hashes of the original artifacts and the
  follow-up. Original hashes and native continuation histories were verified.

The reviewer here is the author itself. The comparative judgments below are manual
Codex work. The model's assertions that its checks passed are not used as labels.

## Results by case

| Case | Before | After one reflection | Assessment |
|---|---|---|---|
| [W01](../W01/writer/turn-02/output.md) | Ready | Ready | Request and table preserved. No material regression. |
| [W02](../W02/writer/turn-02/output.md) | Coherent, missing required negative | Same unresolved defect | Explicitly extracts #launch-prep as a condition but does not add a channel-only negative. Says no defects found. |
| [W03](../W03/writer/turn-02/output.md) | Ready | Ready | Alternatives and request preserved. Adds an unreacted incident-retro message to the topic negative, making it more similar to the existing binding negative. Unnecessary change/redundancy, not a material validity regression. |
| [W04](../W04/writer/turn-02/output.md) | Accidental full match in absent case | Partly repaired | Catches and removes the accidental match and cleans the inline correction. Repeated message descriptions still leave the distinct-root/missing-reaction row unclear. |
| [W05](../W05/writer/turn-02/output.md) | Contradictory current membership facts | Ready | Explicitly gives #support-archive zero current memberships; five names remain only in old message text. Count distinction and supported write preserved. |
| [W06](../W06/writer/turn-02/output.md) | Ready | Ready | Author membership versus message location remains correct. Minor rewording only. |
| [W07](../W07/writer/turn-02/output.md) | Reuses positive roots as negatives | Partly repaired | Correctly replaces those rows with distinct Alexes, but still treats Alex Chen/Diaz as irrelevant negatives for an existence question they can answer with “no.” |
| [W08](../W08/writer/turn-02/summary.json) | Contradictory shared facts; weak answer discrimination | Incomplete | Reaches 6,000 output tokens, 5,999 of them thinking tokens. No final sketch returned. Detection in reasoning is not counted as a repair. |
| [W09](../W09/writer/turn-02/output.md) | Absence insufficiently established | Conceptually ready, compiler qualification retained | Makes #incident-response a single channel with exactly Priya and Sam as members, neither holding workspace membership. This closes the potential extra-match gap. |
| [W10](../W10/writer/turn-02/output.md) | Coherent selection, unsupported role answer | Same unresolved defect | Still claims the requested full role information is observable rather than limiting the answer to supported admin/owner flags. |

| Measure | Result |
|---|---:|
| Assigned reflections | 10 |
| Complete revised outputs | 9 |
| Incomplete outputs | 1 |
| Conceptually ready before | 3/10 (30%) |
| Conceptually ready after | 5/10 (50%) |
| Newly ready cases | 2/7 previously needing revision |
| Materially improved but still incomplete repairs | 2/7 previously needing revision |
| Previously ready cases preserved | 3/3 |
| Observed material validity regressions in returned sketches | 0/9 |

The incomplete call stays in the denominator. The three original good cases are
not a large regression sample, and one pass per case does not establish repeatability.

## What the repairs actually accomplished

**W04: selection reasoning improves, but final-table cleanup is incomplete.**
The writer now recognizes that a marketing message can satisfy the request: the
prompt constrains reactor membership and emoji, not message topic or location.
It replaces the qualifying reactor with Wendy, who belongs to the similarly named
#eng-rollout-archive. The stated facts no longer create that accidental match.
However, two rows still use “New build passed smoke tests,” by Priya in #general.
The first has Sam's reaction; the later row says Priya did not react and labels
the row “no reaction present.” If it is the same message, Sam's reaction remains;
if it is a second otherwise identical message, that distinction must be stated.
The absence result improves, but the claimed distinct missing-reaction negative
is still not cleanly specified.

**W07: the review fixes shared roots but misses the question's meaning.**
Alex Nguyen and Alex Patel now replace the reused Rivera/Kim negative roots.
Those substitutions address the original inconsistency. But Alex Chen reacted
correctly and then left the channel, while Alex Diaz reacted correctly in a channel
where he is not a member. “Is Alex still a member of the channel where they reacted…”
can refer to either; their answer is “no.” Requiring current membership in order
to consider someone an interpretation treats the answer being sought as a
selection prerequisite. The claimed two singleton alternatives are therefore not
established. The response also retains an avoidable read question rather than the
preferred supported write. Its reasoning explicitly accepts identical answers for
the positive alternatives, so answer discrimination has not improved.

**W09: the relevant missing fact is now settled.**
The writer identifies Sam's unstated workspace association and explicitly removes
it. It also gives the target channel a complete two-person membership list, with
neither person holding a workspace membership. This establishes conceptual absence
without making the target channel empty. Workspace members elsewhere and members
of the similarly named channel remain as complementary near matches. Priya's row
is now labeled as providing no workspace candidate; it is useful supporting
information, not an additional root. Compiler confirmation of accessible profile
associations remains necessary. Unavailable workspace-name lookup alone does not
invalidate this absent instance, whose appropriate answer supplies no name.

## W08: detected the problem, failed to produce a repair

[Recorded thinking](../W08/writer/turn-02/thinking.txt) recognizes that Nina cannot
both have and lack the same membership in one environment. It also recognizes
that switching a negative to a different author while removing membership violates
both the fixed-author and membership conditions.

It repeatedly tries to retain the fixed Nina condition, considers dropping the
membership negative, and incorrectly claims the instructions permit that omission.
The original instructions instead say to repair the design when a condition cannot
independently affect selection. The follow-up permits necessary request changes,
but the writer does not finish such a redesign. It consumes 5,999 thinking tokens
within a 6,000-token output limit and returns no final sketch. The exposed thinking
is a provider summary; this diagnosis concerns what was actually recorded, not an
assumption of complete access to every internal step.

This is a new completion failure, even though the starting sketch was already
defective. Increasing the budget might allow an answer, but this experiment does
not establish that it would produce a correct one. No larger-budget retry was made.

## Remaining limitations and implications

- Whole-table consistency checks helped: W04, W05, W07 and W09 contain substantive
  repairs rather than just claims of improvement.
- The checks were not reliable as a final acceptance gate: W02 and W10 confidently
  retain known defects, and W04/W07 remain only partly repaired.
- No material validity regression was observed in the nine completed revisions.
  W03 introduces some redundancy; W08 supplies no revised artifact at all.
- The preservation instruction is helpful for good cases but may interact poorly
  with a scenario that requires a different referring expression. W08 is evidence
  of that difficulty, not proof that a particular wording caused it.
- The next development decision is whether to add a bounded escalation for these
  remaining design failures. This run does not justify broad compilation yet.

## Cost and verification

| Usage | First pass | Added reflection | Combined |
|---|---:|---:|---:|
| Calls | 10 | 10 | 20 |
| Uncached input tokens | 6,417 | 29,076 | 35,493 |
| Output tokens, including thinking | 15,496 | 29,612 | 45,108 |
| Cache creation tokens | 6,794 | 6,794 | 13,588 |
| Cache read tokens | 61,146 | 61,146 | 122,292 |
| Estimated dollars | $0.2955123 | $0.5752293 | $0.8707416 |

These are our historical-rate estimates from native usage, not billed dollar
figures. All twenty calls have usage; W08's incomplete call is included. Reflection
cost roughly 1.95 times the first-pass cost, bringing the combined cost to roughly
2.95 times first-pass authoring alone. Its longer input includes each original
answer/history. Both rounds recorded nine cache-hit calls after one cache creation.

See [incremental usage](usage.json), [combined usage](../usage_summary.json),
[first-pass usage](initial_usage_summary.json), [cache check](cache_check.json),
and [run status](run_status.json). The runner exits nonzero because W08 is incomplete;
the other nine results and all usage were still collected and preserved.

Eleven targeted unit tests passed, including native-history preservation,
unchanged first-turn hashes, no duplicate second calls and no retry of incomplete
responses. All ten actual continuation requests preserve the original messages,
native assistant blocks, system prompt and request settings. No tests or manual
judgments here certify a generated runnable environment.
