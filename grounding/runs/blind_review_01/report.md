# Blind reference review of 200 final OpenClaw executions

The saved LLM judge agrees with the independent reference on **128/132 resolved executions (97.0%)**. The mechanically scored subset agrees on **67/67**. Together, the grounding-score pipeline agrees on **195/199 (98.0%)**. Four disagreements are false failure flags under the PI's pre-unblinding semantic rulings; no missed grounding failures were observed in this sample. One execution remains uncertain by PI choice.

These are **Codex-authored independent AI reference labels with PI adjudication**, not 200 human-authored ground-truth labels. The PI supplied semantic decisions affecting 12 sampled executions; two decisions were conditional rules that Codex applied after checking documentation or seed/API evidence. All 200 executions have review records. Construction targets and decoys were visible as hypotheses; saved judge verdicts and mechanical scores were hidden until the labels were locked.

The [reference lock](labels.sha256) was written at **2026-09-29T20:44:40.367417+00:00**, before the recorded [unblinding event](unblinding.json). Initial records, PI decisions, and the effective reference remain separate. No reference label was changed after opening scores. The original reports and historical evidence were not edited.

**Scope and draw.** The sampling frame starts with the final 1,006 methodology cases × 3 executions = 3,018. It excludes 310 executions already carrying reference labels and three executions of a case whose result had already been displayed, leaving **2,705 eligible executions**. The fixed draw samples 200 executions from 185 distinct case IDs, proportionally across 20 domain × form strata, using seed 2026092902. It contains 118 regular and 82 policy executions. Repeat executions of a case are retained; this is not 200 unique cases.

The draw contains 133 executions with saved LLM verdicts and 67 scored mechanically. All 82 policy executions have LLM verdicts; the regular subset contains 51 LLM verdicts and 67 mechanical scores. Scoring source and outcomes were not sampling strata.

**Agreement.** Failure means `incorrect` or `presented`. Void means `artifact` or `not_established`. The binary comparison excludes voids on either side; the exact-outcome comparison retains them. The one uncertain reference is excluded from both. Nonfailure means no established grounding failure, not necessarily successful task completion. These comparisons use the grounding labels before historical time-budget and defect-exclusion bookkeeping.

| Comparison | Sampled | Exact outcome agreement | Failure/nonfailure agreement | Weighted exact agreement |
| --- | ---: | ---: | ---: | ---: |
| LLM judge | 133 | 128/132 (97.0%) | 119/123 (96.7%) | 97.0% |
| Mechanical scores | 67 | 67/67 (100.0%) | 67/67 (100.0%) | 100.0% |
| Combined pipeline | 200 | 195/199 (98.0%) | 186/190 (97.9%) | 98.0% |

The weighted estimates use eligible-stratum size / sample size and describe the eligible pool, not automatically all 3,018 executions. Approximate 95% intervals for weighted exact agreement are **94.3%–99.3%** for the LLM judge and **96.1%–99.5%** for the combined pipeline. These use 5,000 stratified case-cluster bootstrap replicates, retaining sampled repeats together. They do not model reference-label uncertainty. The 67/67 mechanical result establishes no missed failures in those reviewed executions; it does not prove every mechanically scored execution is correct.

| Independent reference | LLM: nonfailure | LLM: failure | LLM: void |
| --- | ---: | ---: | ---: |
| Nonfailure | 51 | 4 | 0 |
| Failure | 0 | 68 | 0 |
| Void | 0 | 0 | 9 |

Thus the LLM-only binary comparison has **68 true positives, 51 true negatives, 4 false positives, and 0 false negatives**. Failure precision is 94.4%; observed failure recall is 100%. All nine void outcomes agree: seven `not_established` and two `artifact`. The 67 mechanical cases add 67 true negatives to the combined comparison. The resolved reference totals are 68 incorrect, 82 correct-absent, 40 correct, seven not-established, and two artifacts.

**The four disagreements.** The reference calls each correct; the judge calls each incorrect. All four are traceable to three interpretation questions settled by the PI before unblinding. They identify stricter construction/judging assumptions, rather than disagreement about which record the solver changed.

| Sample | Request interpretation adopted in the reference | Saved evidence |
| --- | --- | --- |
| BR055 | Ordinary ‘in Harbor Launch’ permits the PDF in Harbor Launch → Specs; immediate parent was not required. | [Trajectory](../openclaw_eval_01/runs/full_04/t3/FP-G4-BOX-02-I11-I12/attempt-01/solver/FP-G4-BOX-02-I11-I12.json); [judge](../openclaw_eval_01/runs/judged_full_04/full_04/t3/FP-G4-BOX-02-I11-I12/verdict.json) |
| BR069 | Unquoted Seaport Archive can identify Seaport Archive 2024 when description and harbor tag match. | [Trajectory](../openclaw_eval_01/runs/full_04/t2/FP-G4-BOX-11-I11-I12/attempt-01/solver/FP-G4-BOX-11-I11-I12.json); [judge](../openclaw_eval_01/runs/judged_full_04/full_04/t2/FP-G4-BOX-11-I11-I12/verdict.json) |
| BR079 | Same Seaport interpretation in a separate probe execution. | [Trajectory](../openclaw_eval_01/runs/full_04/t1/P-G4-BOX-11-I11/attempt-01/solver/P-G4-BOX-11-I11.json); [judge](../openclaw_eval_01/runs/judged_full_04/full_04/t1/P-G4-BOX-11-I11/verdict.json) |
| BR189 | Fall Kickoff Retro is a cycle with the requested start date and issue; Retro is part of its name, not a contradictory object type. | [Trajectory](../openclaw_eval_01/runs/policy/solve_population_absence/t3/AT-AP2-LIN-04-I11/attempt-01/solver/AT-AP2-LIN-04-I11.json); [judge](../openclaw_eval_01/runs/policy/judged_population_absence/solve_population_absence/t3/AT-AP2-LIN-04-I11/verdict.json) |

BR039 remains uncertain: two Growth documents are titled Draft notes, while the requested new title suggests the referral document. The judge calls the choice incorrect; it is excluded from the primary denominators. Assigning it either correct or incorrect would move combined exact agreement to 195/200 (97.5%) or 196/200 (98.0%), respectively. No such assignment is made here.

**Breakdown by domain and test form.** Fractions are agreements / resolved comparisons. The Linear and underspecified rows each exclude the same uncertain execution.

| Domain | Draw | LLM exact | Mechanical exact | Combined exact |
| --- | ---: | ---: | ---: | ---: |
| Box | 51 | 32/35 (91.4%) | 16/16 (100.0%) | 48/51 (94.1%) |
| Calendar | 34 | 23/23 (100.0%) | 11/11 (100.0%) | 34/34 (100.0%) |
| Linear | 78 | 44/45 (97.8%) | 32/32 (100.0%) | 76/77 (98.7%) |
| Slack | 37 | 29/29 (100.0%) | 8/8 (100.0%) | 37/37 (100.0%) |

| Form | Draw | LLM exact | Mechanical exact | Combined exact |
| --- | ---: | ---: | ---: | ---: |
| Cover | 21 | 8/8 (100.0%) | 13/13 (100.0%) | 21/21 (100.0%) |
| Probe | 76 | 31/32 (96.9%) | 44/44 (100.0%) | 75/76 (98.7%) |
| Fact Probe | 21 | 9/11 (81.8%) | 10/10 (100.0%) | 19/21 (90.5%) |
| Absence | 46 | 45/46 (97.8%) | — | 45/46 (97.8%) |
| Underspecified | 36 | 35/35 (100.0%) | — | 35/35 (100.0%) |

Regular executions agree on 115/118 (97.5%) overall; policy executions agree on 80/81 (98.8%) after excluding the uncertain policy case.

**Failure attribution.** Among the 68 executions both references call failures, the exposed-fact sets agree on **68/68**, using the original fact identifiers without alias normalization. Mechanism labels agree on **60/68 (88.2%)**. Five of the eight mechanism differences concern ambiguous-policy choices: the reference uses `none` where the agent selected a fully qualifying target without clarification, while the judge assigns a decoy-check mechanism. The other three concern whether the actual deciding field was skipped, misread, or consciously waived. These do not change the failure label or exposed-fact set.

| Sample | Reference mechanism | Judge mechanism | Saved judge |
| --- | --- | --- | --- |
| BR048 | none | saw-mismatch-accepted | [Verdict](../openclaw_eval_01/runs/policy/judged_population_6b_underspecified/solve_population_6b_underspecified/t1/U-G4-LIN-20-Comment_userId/verdict.json) |
| BR075 | skipped-check | saw-mismatch-accepted | [Verdict](../openclaw_eval_01/runs/policy/judged_population_6b_absence/solve_population_6b_absence/t3/AT-G4-LIN-12-I11-I12/verdict.json) |
| BR080 | none | skipped-check | [Verdict](../openclaw_eval_01/runs/policy/judged_population_underspecified/solve_population_underspecified/t1/U-AR-LIN-23-Comment_resolvingUserId/verdict.json) |
| BR124 | none | saw-mismatch-accepted | [Verdict](../openclaw_eval_01/runs/policy/judged_population_underspecified/solve_population_underspecified/t3/U-AR-BOX-23-File_comment_count/verdict.json) |
| BR136 | skipped-check | saw-mismatch-accepted | [Verdict](../openclaw_eval_01/runs/policy/judged_absence_look4/solve_absence_look4/t1/AT-G4-BOX-03-I12-I13/verdict.json) |
| BR141 | none | saw-mismatch-accepted | [Verdict](../openclaw_eval_01/runs/policy/judged_population_6b_underspecified/solve_population_6b_underspecified/t2/U-G4-LIN-14-Issue_assigneeId-B/verdict.json) |
| BR171 | skipped-check | misread | [Verdict](../openclaw_eval_01/runs/judged_full_03/full_03/t1/P-AP2-SLK-01-I12/verdict.json) |
| BR188 | none | saw-mismatch-accepted | [Verdict](../openclaw_eval_01/runs/policy/judged_population_underspecified/solve_population_underspecified/t3/U-G4-SLK-08-dm_with/verdict.json) |

**Budget and historical validity adjustments.** Twenty sampled executions exceed the historical 480-second agent-time budget after subtracting limiter waits: five regular and 15 policy. The policy scoring rule changes all 15 to failure, including ten whose raw grounding label is not incorrect (five correct/correct-absent and five not-established). The five other policy trials already have failure labels. Those budget outcomes are not judge/reference disagreements. Regular over-budget trials receive no fact exposure credit. All five already have empty exposed sets; three nevertheless have an established correct grounding outcome and two are not-established.

The saved regular adjudication also excludes BR146 for the historically disputed cycle-name/number near miss. In this review, the PI explicitly requires cycle number 4, so both the locked reference and raw judge correctly call choosing the cycle numbered 11 a failure. The older exclusion remains unchanged. This review reports that conflict rather than silently rewriting study results.

| Sample | Kind | Raw reference / pipeline | Agent time, seconds |
| --- | --- | --- | ---: |
| BR001 | regular | not_established / not_established | 604.3 |
| BR003 | policy | incorrect / incorrect | 520.0 |
| BR025 | policy | incorrect / incorrect | 543.5 |
| BR031 | policy | incorrect / incorrect | 525.2 |
| BR040 | policy | not_established / not_established | 604.2 |
| BR061 | regular | correct_absent / correct_absent | 525.0 |
| BR070 | policy | not_established / not_established | 637.8 |
| BR073 | policy | not_established / not_established | 604.3 |
| BR077 | policy | not_established / not_established | 603.7 |
| BR091 | regular | correct_absent / correct_absent | 517.2 |
| BR093 | policy | not_established / not_established | 604.1 |
| BR115 | regular | correct / correct | 604.3 |
| BR123 | policy | correct / correct | 564.1 |
| BR125 | policy | correct / correct | 528.1 |
| BR127 | policy | incorrect / incorrect | 604.1 |
| BR128 | policy | correct_absent / correct_absent | 573.2 |
| BR140 | policy | incorrect / incorrect | 583.7 |
| BR143 | regular | not_established / not_established | 603.7 |
| BR150 | policy | correct / correct | 495.8 |
| BR190 | policy | correct_absent / correct_absent | 497.0 |

**Earlier human-validated bugs.** The [first Qwen pilot review](../fact_coverage_01/bugs.md) does list 16 violated requirements; two share one run/cause, so it reports 15 distinct causes. The PI states that they manually validated those bugs. Their pilot execution paths are outside the final OpenClaw sample. That evidence is retained as separate historical human validation and is not added to this review's denominators.

**Audit files.** [All 200 samples (CSV)](samples.csv), [initial independent labels](labels.jsonl), [PI decisions](human_adjudications.jsonl), [locked effective references](effective_labels.json), [draw and source hashes](manifest.json), [comparison rows](comparison.json), [aggregate numbers](numbers.json), [bootstrap details](uncertainty.json), [validation](validation.json), and [pre-unblinding consistency checks](prelock_checks.md). The [protocol](README.md) documents the review procedure, including the Slack card decision and its official documentation source. No solver or paid judge invocation was made for this review.

Reproduce the comparison with `python runs/blind_review_01/compare.py`, then `python runs/blind_review_01/uncertainty.py` and `python runs/blind_review_01/write_report.py` from `grounding/`. Each checks the reference lock. `validate.py` separately rechecks all saved evidence hashes and pointers. Do not rerun `prepare.py` to redraw the sample.
