# Workflow variants: five fresh repetitions each

The separate-explanation variant is the best candidate in this small pilot: 4/5 final reports match all predeclared applicability, execution, and grounding judgments after mechanical repairs. Explicit ordering yields 3/5; two-turn assessment yields 2/5, with two wrong creation-applicability judgments and one timeout. None eliminates semantic errors. These counts concern categorical judgments on this single case, not every factual/prose detail or a general reliability estimate.

## Variants and controls

- **Ordered:** append a short instruction to finish applicability for all lines first, then execution, then grounding/aggregation, then accounting. Same full output schema. [Instructions](ordered-instructions.md), 2,153 words versus the 2,094-word [baseline](baseline-instructions.md).
- **Separated:** ordered variant plus short `Applicability:`, `Execution:`, and `Grounding:` clauses inside each existing explanation string. The applicability clause names the decisive rule and basis. No schema fields added. [Instructions](separated-instructions.md), 2,204 words.
- **Two-turn:** first return applicability only using the existing diagnostic projection of the full schema. Append the complete assistant response and a short follow-up requesting execution, grounding, accounting, and the complete full-schema output in the same conversation. The full schema accompanies that follow-up to supersede the preceding projected output contract. The first-turn applicability assessment is retained in history, not inserted as a supposedly authoritative answer. [Instructions](two-turn-instructions.md), [orchestration script](two_turn.py), [example follow-up](two-turn-1/followup.txt).

All 15 conversations launched together. Within each two-turn conversation, calls are sequential. Every initial request uses the same Slack 98 evidence packet, Sonnet 5, medium effort, 16,000 output-token cap, summarized thinking, and instructions after evidence. Full final schema and mechanical validator unchanged. One conversational mechanical repair is allowed after a completed full report, with no semantic feedback. Prior results, reviews, and [expected judgments](plan.md) were excluded from model inputs. The main lean prompt and repository runner were not edited for these variants; all variant files are isolated in this directory.

The prior five-run baseline had 3/5 final reports matching all expected categories, 5/5 expected overall grounding, and 5/5 L3 performed. This was an earlier batch, not a newly randomized concurrent control.

## Results

| Variant | All expected categories, first full response | After mechanical repair | Correct L7/L8 applicability in final report | Initial/full mechanical passes | Final mechanical passes | Mean total seconds per conversation |
|---|---|---|---|---|---|---|
| Ordered | 3/5 | 3/5 | 4/5 | 4/5 | 5/5 | 77.4 |
| Separated explanations | 3/5 | 4/5 | 4/5 | 4/5 | 5/5 | 88.6 |
| Two-turn | 1/5 | 2/5 | 4/5 (all four completed reports) | 3/5 | 4/5 | 128.4 |

Total time includes the applicability turn where applicable, repairs, and the failed timeout. The four completed two-turn conversations averaged 82.6 seconds. Shared concurrency and small samples limit timing comparisons.

All 14 completed full reports retain the expected eight overall grounding verdicts and L3 active/performed. O1/O2/O3/O5 are correct and O4/O6/O7/O8 incorrect. No completed full report raises an assessment_issue. No existing categorical judgment changed during mechanical repair. All final completed reports pass the unchanged validator. Mechanical passing does not imply correct applicability.

## Material failures and what they show

**Ordered, repeat 3:** L7 and L8 remain active. Its [thinking](ordered-3/thinking.txt), line 13, recognizes unauthorized selections and then says it is “marking each line as active/performed.” The requested stage order is not consistently apparent in the returned summary. There is no evidence that simply asking for ordered analysis guarantees separate assessments.

**Ordered, repeat 5:** L4, a read-only condition check, is marked inactive because it gates a state change. Its [final explanation](ordered-5-repair-1/assessment.json), L4, explicitly applies mutation rule 4 to the condition itself. This is a different applicability error from the original L7/L8 problem. A marker-only L5 and its missing creation-diff accounting were repaired without changing the L4 judgment.

**Separated, repeat 4:** L7 and L8 remain active. The separate explanation exposes the contradiction directly. In the [L7 explanation](separated-4/assessment.json), it says the card is underspecified “but the agent chose to act,” then mixes applicability with assessing the observed execution. L8 similarly says the agent proceeded, so it is assessed as executed. Citing a rule does not ensure its consequence is followed. The other four final separated reports correctly distinguish inactive from performed. See [repeat 1](separated-1/assessment.json), L7, for a concise successful explanation.

**Two-turn, repeats 2 and 4:** the first applicability turn incorrectly treats O4 as directly linked to L5, although L5 has no direct links. Both full reports preserve L5 inactive and acknowledge an empty grounding map. See [repeat 2 first turn](two-turn-2-applicability/applicability.json) and [final report](two-turn-2/assessment.json), L5; [repeat 4 first turn](two-turn-4-applicability/applicability.json) and [final report](two-turn-4/assessment.json), L5. Separating the turn did not prevent invented inheritance and carried that mistake forward.

**Two-turn, repeat 3:** the first turn correctly classified applicability; the second call ended in a roughly 300-second read timeout. No second-turn response, thinking, or native usage was received. This is an operational failure, not evidence of a particular reasoning loop. [Timeout summary](two-turn-3/summary.json).

**Two-turn, repeat 5:** the first turn returned malformed JSON with an unfinished self-correction, despite end_turn. See [raw first answer](two-turn-5-applicability/answer.txt) and [summary](two-turn-5-applicability/summary.json). The second turn preserved that exact assistant content and requested the full assessment as planned; the full answer was well formed and categorically matched expectations. There was no extra first-turn repair or reconstructed substitute answer. This shows the need to account for intermediate output reliability in a staged workflow.

## Repairs

Three mechanical repair calls total:

- Ordered 5: L5 was reduced to a marker and five related insert records were unaccounted. [Changes](ordered-5-repair-1/assessment-change.diff).
- Separated 3: L5 was reduced to a marker and five related insert records were unaccounted. [Changes](separated-3-repair-1/assessment-change.diff).
- Two-turn 1: L5 was reduced to a marker. [Changes](two-turn-1-repair-1/assessment-change.diff).

All passed after one repair. All original semantic verdicts were preserved; repairs filled missing rows/accounting. Every two-turn and repair request retains the complete original history and prior native assistant content, including thinking/signatures, unchanged.

## Outputs

| Repeat | Ordered final | Separated final | Two-turn final |
|---|---|---|---|
| 1 | [JSON](ordered-1/assessment.json) | [JSON](separated-1/assessment.json) | [JSON](two-turn-1-repair-1/assessment.json) |
| 2 | [JSON](ordered-2/assessment.json) | [JSON](separated-2/assessment.json) | [JSON](two-turn-2/assessment.json) |
| 3 | [JSON](ordered-3/assessment.json) | [JSON](separated-3-repair-1/assessment.json) | [Timeout, no final output](two-turn-3/summary.json) |
| 4 | [JSON](ordered-4/assessment.json) | [JSON](separated-4/assessment.json) | [JSON](two-turn-4/assessment.json) |
| 5 | [JSON](ordered-5-repair-1/assessment.json) | [JSON](separated-5/assessment.json) | [JSON](two-turn-5/assessment.json) |

Every call directory contains its exact request, source snapshots, manifest, schema, instructions, provider response when returned, raw answer, returned thinking summary, validation, and usage. [Machine-readable comparison](comparison.json), [comparison script](compare.py).

## Cost and recommendation

| Variant | API calls | Native input tokens received | Native output tokens received | Thinking tokens (within output) |
|---|---|---|---|---|
| Ordered | 6 | 512,674 | 37,555 | 23,052 |
| Separated | 6 | 511,892 | 44,181 | 27,017 |
| Two-turn | 11, including one timeout | 853,261 | 33,290 | 15,880 |

Across 23 attempted API calls, returned usage totals 1,877,827 input and 115,026 output tokens, including 65,949 thinking tokens. The timeout has unknown usage; these totals are not a complete accounting of any provider-side consumption for that call. No native dollar amounts were returned, so cost remains null. [All-call ledger](usage_ledger.jsonl).

The separated variant costs 110 instruction words beyond baseline, no additional schema fields, and no extra planned API turn. Its final line explanations average 3,580 characters across a report versus 2,473 for ordered, so it does increase prose. It is the best candidate to carry into testing on other cases, and its explicit clauses help audit contradictions. Its one remaining applicability error means it is not ready to claim a very small error rate.

I would not adopt the two-turn implementation on these results: it adds tokens and an intermediate output contract without an observed overall accuracy advantage. Explicit ordering alone is simpler, but does not improve all-category consistency over this baseline sample. No variant has been promoted into the main lean prompt; no new policies, semantic repairs, or benchmark-specific hardcoded checks were introduced.
