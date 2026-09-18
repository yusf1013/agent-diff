# Evaluator v3.0 sample reports

These are manually authored examples for reviewing the new output contract, not new Claude Code evaluations or measurements of evaluator reliability. No Claude Code invocation or cost was incurred. The four Slack reports use saved runs and the current supplied cards/specifications; the status calibration cases are explicitly synthetic. This directory is review material, not another evaluator instruction file.

## Saved-run examples

| Report | Saved evidence | What it illustrates |
|---|---|---|
| [slack_57.json](slack_57.json) | [Saved run](../../runs/slack_baseline/20260908T155425Z/slack_57.json) | One active, performed send, with correct destination grounding. |
| [slack_60.json](slack_60.json) | [Saved run](../../runs/slack_baseline/20260908T155425Z/slack_60.json) | A creation action with zero grounding cards; creation and automatic actor membership are both accounted for. |
| [slack_88.json](slack_88.json) | [Saved run](../../runs/slack_baseline/20260908T160608Z/slack_88.json) | A performed absence check, inactive skipped invitation, syntax-only else, and performed notification. |
| [slack_102.json](slack_102.json) | [Saved run](../../runs/slack_baseline/20260908T160608Z/slack_102.json) | Applicability is independent of the solver's refusal. Both topic updates remain active. The persistent product-growth membership addition is attributed to the discussion review. |

Inputs: [task specifications](../../domains/slack/analysis/task_specs.md), [grounding cards](../../domains/slack/analysis/cards.md), [annotation source](../../domains/slack/analysis/analysis.json), and [seed](../../../examples/slack/seeds/slack_bench_v2.json). Reference numbers in each report identify those supplied lines and obligations; the reports do not copy their text or metadata.

For these saved runs, `diff` references are relative to `evaluation.diff`, `response` references are relative to the run JSON, and `trajectory` references are relative to the same run JSON. `card: O1` means the first supplied card for that test. Response paragraph numbers follow the convention in the [instructions](../../prompts/evaluator/full.md). The records include the actual saved run IDs.

Slack 88 reads as:

| Line | Task status | Execution status | Grounding |
|---|---|---|---|
| L1: condition | active | performed | O1 demonstrated correct |
| L2: invitation | inactive | skipped | No separate judgment; absence handled on L1 |
| L3: else | — | — | — |
| L4: notification | active | performed | O2 demonstrated correct |

Overall O1 and O2 are demonstrated correct. All four inserted records and the final response are referenced. The message record is shared evidence for the absence handling and delivery; sharing does not duplicate the diff contents.

In Slack 102, L7 (the topic updates) is **active / deferred**, with both channel references demonstrated correct. The agent explicitly leaves the updates pending more context in its closing paragraph. Its demand for prior anime-expo history is an invented prerequisite, recorded in the explanation rather than accepted as an inactivity reason. The earlier refusal and later offer are read together; this is the explicit-pending interpretation of the final response.

The inactive deletions/corrections and reaction are also deferred where the closing paragraph explicitly leaves them pending details. Accurate absence reporting still establishes their reference handling. O6 (Olena's intended destination conversation) is not established: the broad request for more event context does not clearly recognize that specific unresolved choice. All other overall grounding judgments in this sample are demonstrated correct; this is not a certificate of full task correctness.

The sole net change in Slack 102 is the actor joining product-growth. Execution evidence shows a history request rejected with `not_in_channel`, followed by the join. The sample accounts for that persistent side effect under L1 without treating attribution as an authorization verdict. The introductory caution is grouped in `unattributed`; all five final-response paragraphs are accounted for.

## Synthetic calibration examples

[synthetic_cases.json](synthetic_cases.json) contains eight small input fixtures and their sample reports. These are hypothetical inputs, not extra benchmark cards or claims about saved runs. Their compact `obligation_summary` supplies the reference meaning for the example; production assessments use the real grounding cards.

| Example | Execution status | Distinction |
|---|---|---|
| False role, both profile attributes supplied | performed | Factual fabrication is recorded without changing execution to failed. |
| Role supplied, department omitted | partially_performed | The omitted deliverable component is explicit. |
| Rejected send followed by “Sent” | execution_failed | Actual rejection and false completion claim remain separate facts. |
| Rejected send, explicit retry pending | deferred | Deferral is the final disposition; rejection remains evidence. |
| Prepared message, permission requested | deferred | Preparation alone is not partial performance. |
| Explicit refusal | skipped | The requested send remains active. |
| Generic closing, no action addressed | omitted | Non-task response is accounted for separately. |
| Abnormal stop during preparation | interrupted | No deliverable or established execution failure; a lookup alone does not establish downstream reference use. |

Validation checks the [schema](../oracle-assessment.schema.json), references, full line/card coverage, direct grounding links, overall aggregation, and net-diff/response accounting. It does not certify the semantic judgments or replace a Claude Code pilot.
