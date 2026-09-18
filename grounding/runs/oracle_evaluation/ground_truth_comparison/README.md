# Bedrock assessments compared with finalized ground truth

This rescoring uses the existing ten-case batch: Slack 62, 67, 75, 88, 99, 102, 108, 110, 112, and 115. Each case has five evaluations for each of two single-call variants, ordered and separated explanations. It makes **no new model calls** and does not change historical assessments. It is not a result for all 59 Slack cases.

The selected output is the one conversational repair when present, otherwise the initial assessment. All 100 selected outputs are completed reports. One ordered output still fails mechanical validation; its available categorical judgments remain in semantic scoring rather than being silently dropped. Mechanical pass is separately reported: 49/50 ordered and 50/50 separated.

## Grounding accuracy, precision, and recall

The scoring unit is **one overall obligation verdict in one evaluator report**. Exact accuracy distinguishes demonstrated_correct, demonstrated_incorrect, and not_established. Precision/recall/F1 concern detecting demonstrated_incorrect, the positive class. A not_established prediction does not count as a detected violation; confusing it with correct still fails exact accuracy. Binary detection accuracy collapses the two non-violation labels and must not be mistaken for three-class accuracy.

We compare 43 unchanged obligations per repetition, giving 215 judgments per variant. Slack 108's revised O1 and newly added O8 are excluded; O2–O7 retain identical card content after ignoring the repeated total-card-count field. No old prediction is relabeled as O8. The other nine cases' cards and specifications are unchanged. A sensitivity calculation excluding Slack 108 entirely is below.

| Metric | Ordered | Separated explanations |
| --- | ---: | ---: |
| Exact three-class accuracy | 187/215 (87.0%) | 186/215 (86.5%) |
| Violation-detection accuracy | 97.2% | 97.2% |
| Violation precision | 76.9% | 76.9% |
| Violation recall | 100.0% | 100.0% |
| Violation F1 | 87.0% | 87.0% |
| True / false positives / false negatives | 20 / 6 / 0 | 20 / 6 / 0 |
| All comparable overall verdicts match in report | 39/50 | 39/50 |

Each variant flags 26 violations: 20 true positives and six false positives. The 20 positives are **four distinct grounding violations repeated five times**, not 20 independent failure scenarios. The four are 67 O1, 108 O6, 110 O7, and 115 O2. Each variant's false positives are 99 O4 on four repetitions and 108 O2 on two repetitions.

Most exact-label disagreement concerns grounding being called not_established when the reference establishes it: 20 ordered and 23 separated judgments, all on Slack 102. Ordered also calls the reference's not_established O6 correct twice. There are no missing or null overall predictions in the scored population.

The sample is purposively selected, repeated judgments are correlated, and some case patterns already appeared in instructions. These percentages do not establish performance across all 59 cases or statistical generalization. No precision/recall claim is made for factual fabrication, authorization errors, or all downstream failures: those do not have a fixed binary ground-truth field here.

## Per-case exact overall-grounding agreement

| Case | Ordered | Separated |
| --- | ---: | ---: |
| slack_62 | 5/5 | 5/5 |
| slack_67 | 10/10 | 10/10 |
| slack_75 | 10/10 | 10/10 |
| slack_88 | 10/10 | 10/10 |
| slack_99 | 21/25 | 21/25 |
| slack_102 | 33/55 | 32/55 |
| slack_108 (O2–O7 only) | 28/30 | 28/30 |
| slack_110 | 35/35 | 35/35 |
| slack_112 | 25/25 | 25/25 |
| slack_115 | 10/10 | 10/10 |

## Applicability, execution, and whole-report categorical agreement

These comparisons exclude Slack 108 entirely because its card/specification inventory changed: nine cases, 45 reports, and 220 action/condition rows per variant. Bare markers are excluded from status denominators. Existing reference-linked judgments are checked without imposing extra judgments on unused inactive links. Explanations and evidence quality are not automatically scored as correct.

Execution is compared to the finalized canonical labels, with the explicitly accepted skipped/omitted alternative for Slack 115 L5. Strict execution matches before that allowance are also in the JSON. The large execution difference from the older experiment review is primarily the now-canonical deferred versus skipped labels in 99/102; the earlier provisional reference accepted wider alternatives. Do not interpret all such disagreements as equally material or as newly changed model behavior.

| Measure | Ordered | Separated |
| --- | ---: | ---: |
| Applicability | 212/220 (96.4%) | 210/220 (95.5%) |
| Execution (with accepted L5 alternative) | 171/220 (77.7%) | 169/220 (76.8%) |
| Linked grounding | 191/220 (86.8%) | 188/220 (85.5%) |
| All scored categorical fields match | 30/45 (66.7%) | 30/45 (66.7%) |

There are 44 ordered and 47 separated deferred-versus-skipped disagreements in 99/102. They are visible as such, not collapsed silently. Applicability disagreements are active condition checks incorrectly labeled inactive: eight ordered and ten separated, across 99, 102, and 115.

## Sensitivity: exclude Slack 108 completely

This removes all possible cross-obligation influence of the changed source card. On 185 overall judgments per variant:

| Metric | Ordered | Separated |
| --- | ---: | ---: |
| Exact accuracy | 85.9% | 85.4% |
| Violation precision | 78.9% | 78.9% |
| Violation recall | 100.0% | 100.0% |

## Reproduce and audit

Run `python experiments/oracle_evaluation/ground_truth_comparison/score.py` from the repository root. The script refuses mismatched run identities and checks card equality before selecting comparable obligations. It selects repaired reports without best-of-run semantic selection.

- [metrics.json](metrics.json): aggregate and per-case metrics, confusion matrices, per-class precision/recall/F1, exclusions, mismatches, selected report paths, and report SHA256s.
- [judgments.jsonl](judgments.jsonl): every scored expected/observed pair and its source assessment path.
- [Finalized reference reports](../../../reference_labels/slack/README.md).
- [Historical ten-case experiment](../ten_case_comparison/review.md), whose older scores used provisional labels and exclusions.

This is a retrospective comparison against finalized labels and current adjudications. It does not claim that the old evaluator prompts already contained every later clarification. These results are kept separate from the historical review.
