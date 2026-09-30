# report_01: evaluation and results, a paper stub

[report.md](report.md) is the stub for a paper's evaluation and results sections, written 2026-09-29 over the
studies before it: [fact_coverage_01](../fact_coverage_01/README.md) (the catalog and the credit rule),
[autogen_01](../autogen_01/README.md) and [autogen_02](../autogen_02/overview.md) (the generator, the judge and the
toy harness's runs), [openclaw_eval_01](../openclaw_eval_01/README.md) and [completion_01](../completion_01/README.md)
(roadmap 6a and 6b on OpenClaw), and [judge_baselines_01](../judge_baselines_01/README.md) (6c). Two sections
report studies on other branches: the generator baselines (`exp/baselines-01`) and step 5's extensions
(`exp/automation-01`).

| Path | What |
|---|---|
| [report.md](report.md) | The report |
| [report_concise.md](report_concise.md) | Shorter report: 1,006 methodology cases, final OpenClaw executions, combined writer groups, and estimated solver costs |
| [kit/](kit/) | One script per table group; each reads committed run records and writes one JSON file. No model calls, no agent runs |
| [numbers/](numbers/) | The scripts' outputs, which the report's tables cite |

Run a script from the repository root with the kit's Python (the backend's virtualenv):

```bash
python grounding/runs/fact_coverage_02/launch.py grounding.runs.report_01.kit.coverage   # RQ1, RQ2 (first)
python grounding/runs/fact_coverage_02/launch.py grounding.runs.report_01.kit.generator  # RQ3
python grounding/runs/fact_coverage_02/launch.py grounding.runs.report_01.kit.exposure   # RQ4 (needs coverage)
python grounding/runs/fact_coverage_02/launch.py grounding.runs.report_01.kit.judge      # RQ5
python grounding/runs/fact_coverage_02/launch.py grounding.runs.report_01.kit.policy_space  # RQ6 (needs coverage)
python grounding/runs/fact_coverage_02/launch.py grounding.runs.report_01.kit.beyond     # RQ7
python grounding/runs/fact_coverage_02/launch.py grounding.runs.report_01.kit.mechanisms # §10
python grounding/runs/fact_coverage_02/launch.py grounding.runs.report_01.kit.scale      # §0.4
python grounding/runs/fact_coverage_02/launch.py grounding.runs.report_01.kit.costs      # §12
python -m grounding.runs.report_01.kit.qwen_usage                                    # §0.4: exact Qwen/OpenClaw tokens, including RQ8
python grounding/runs/fact_coverage_02/launch.py grounding.runs.report_01.kit.concise  # concise report: writes only numbers/concise.json
```

`concise.py` selects final executions, combines writers, filters the blind-label and judge-comparison samples,
and recomputes the equal-budget Muse comparison. It reads baseline summaries from `runs/baselines_01` or, if
still unmerged, `.claude/worktrees/baselines-01/grounding/runs/baselines_01`, and includes those summaries in its
output. The concise report's token estimate scales the historical average to 3,018 executions; it is not an
exact usage audit of that subset. Its price table states the rates, sources and calculation separately.

`numbers/awareness_full_03.json` and `numbers/awareness_full_04.json` come from openclaw_eval_01's
`test_awareness.py` on those runs.

`qwen_usage.py` uses only the Python standard library and reads the original proxy metadata, including cached
input and missing usage, without changing run evidence. It separates the main evaluation, RQ8's fresh baseline
and ablation runs, and stopped/smoke runs. If the baseline branch is still separate, pass
`--baselines-root .claude/worktrees/baselines-01/grounding/runs/baselines_01` from the repository root.

## Recount under the 10-minute budget (2026-09-30)

On 2026-09-29 the PI set the solver's budget to 10 minutes, OpenClaw's own turn limit, which every final run used;
the earlier reading of 8 minutes (runs between 8 and 10 minutes counted as timed out) is withdrawn.
`openclaw_eval_01/rulings.py` now counts a run as over budget only when OpenClaw's limit ended it. The scores
(`*.adjudicated.json`, `final_regular*.json`, `policy/decisions_population_*.json`) and the numbers here were rebuilt.

| Number | 8 minutes (report text) | 10 minutes (numbers/) |
|---|---:|---:|
| Regular runs over budget | 104 | 52 |
| Regular tests exposing a fact | 138 of 565 | 143 of 565 |
| Facts exposed, detect@3 / detect@1 | 87 / 60 | 88 / 61 |
| Policy decisions | 5 not policy-level, 3 undecided | the same 5 and 3, at lower failure rates |
| Box absence rate | 0.79 [0.74, 0.85] | 0.77 [0.71, 0.83] |
| Slack underspecified rate | 0.82 [0.75, 0.89] | 0.77 [0.69, 0.84] |

**The report texts (report.md, report_concise.md) still carry the 8-minute numbers**; their tables are to be
updated from `numbers/` (RQ4, RQ6, §0.4's execution categories, the limits section).

## Text changes (2026-09-30)

report.md and report_concise.md brought to the rebuilt numbers (brief:
[report_update.md](../../protocols/briefs/report_update.md); session "values"). Every number is read from a file;
none is recomputed from memory. `numbers/` and `kit/` are unchanged. One exception to "numbers/ is current":
`numbers/policy.json` was written (commit 49ce3672dc) before the two duplicate policy pairs were merged (4fec9ec540,
which re-made `openclaw_eval_01/runs/policy/decisions_population_underspecified.json`), so Table 11's figures are
read from the two decision files, the sources the table already cites. Format: section, old → new, source.

### Setup (§0)

- report.md §0.3, "The 8-minute budget" → "The 10-minute budget": a trial ended by OpenClaw's 600-second turn limit
  (or whose agent time, limiter waits excluded, passes 600 s) is the agent's failure; the 8-minute reading is
  withdrawn. Source: roadmap, "Decisions (2026-09-29)"; `openclaw_eval_01/rulings.py` (`BUDGET_S = 600`,
  `over_budget`); this README, "Recount".
- Both texts' opening note: states the update of 2026-09-30 and points here.

### RQ2: the F0 rule

- report.md RQ2 "Near-miss family" and report_concise.md RQ2 (the 37 facts credited only through plain near
  misses): "30 are state attributes ...; the other 7 are 5 text attributes, A:Cycle.number and
  R:IssueRelation.relatedIssueId" / "seven have weaker plain-value evidence" → the F0 rule's split: 30 states; 4 with
  no lure in the domain model (Box A:Hub.description, Linear A:Document.content and A:Team.description, Slack
  A:User.title); 2 whose lure the rulings make flawed (Linear A:Cycle.number, Slack A:Message.message_text); 1 being
  regenerated (Linear R:IssueRelation.relatedIssueId). Sources: `numbers/coverage.json`
  (`credited_only_through_plain_near_misses`, the 37 ids); roadmap, "Decisions (2026-09-29)", "The F0 rule".
  Counts unchanged (37, 167, the per-family figures).

### RQ3: duplicate policy units, a stale reference

- report.md RQ3 "Policy units on OpenClaw": adds that two underspecified pairs are one request each (U-AP-SLK-03,
  U-G4-LIN-14) and count once in RQ6's statistic: 197 → 195 underspecified units there. report_concise.md Table 6:
  a note with the same; the table's executed counts stay (197 valid cases, 441 policy, 591 and 1,323 executions),
  since both cases of each pair ran. Sources: `openclaw_eval_01/rulings.py` (`DUPLICATE_UNITS`);
  `openclaw_eval_01/runs/policy/decisions_population_underspecified.json` (`valid_units` 56 + 30 + 78 + 31 = 195).
- report.md RQ3, "`machinery.json` on branch `exp/baselines-01`" → `grounding/runs/baselines_01/machinery.json`
  (merged into main; file checked).

### RQ4: exposure under the 10-minute budget

Sources: `numbers/exposure.json` (`final`, `by_domain`, `by_form`, `by_writer`, `by_kind`, `probes_by_family`,
`probes_designated_vs_plain`, `trials`); `numbers/concise.json` (`writers` → `exposure`). Percentages recomputed from
those counts.

- Both texts, the budget sentence: "the 8-minute budget" / "over the eight-minute agent-time budget" → the 10-minute
  budget (OpenClaw's own turn limit).
- Table 7: Calendar 32 → 34 tests exposing, 12 → 13 facts at detect@1; Linear 45 → 47 tests, 30 → 31 facts at
  detect@3, share 38% → 39%; Slack 22 → 23 tests; all 138 (24.4%) → 143 (25.3%) tests, 87 → 88 and 60 → 61 facts,
  share 42.6% → 43.1% (report.md: 24% → 25%, 43% unchanged). Box unchanged.
- Table 8, forms: probes 101 (28%) → 105 (29%), facts 79 (55) → 80 (56); fact probes 25 → 26 tests, 25 → 26 facts.
  Covers unchanged.
- Table 8, writers (report.md): Sonnet P 17 (22%) → 18 (23%), 12 → 13 facts; Sonnet P v2 18 (20%) → 19 (21%); Muse
  Phase 4 45 (28%) → 47 (30%), detect@1 19 → 20; Muse 6b 34 (25%) → 35 (26%), 22 → 23 facts. Sonnet R unchanged.
  (report_concise.md): Sonnet 59 (22%) → 61 (23%); Muse 79 (27%) → 82 (28%), 47 → 48 facts, 33 → 34 at detect@1.
- Table 8, kinds: attributes 41 → 42 at detect@1; relationships 19 (40%) → 20 (42%) at detect@3.
- Families: designated 84/282 (30%) → 88/282 (31%); F1 31/98 (32%) → 34/98 (35%); F6 4 → 5 of 16 (report.md);
  "28% of probes" → 29% (report.md).
- Trials: 254 failing (15%) → 267 (16%); 1,310 → 1,348 passing; 104 over the 8-minute budget → 52 ended by the
  10-minute budget; void 13 → 14 (12 artifacts + 2 not established). 14 flawed-only unchanged.
- report.md, opaque ids (same 333 tests): 80 against 65 tests and 48 against 42 facts (Calendar 23 → 25, Linear
  23 → 33, Slack 19 → 22) → 84 against 70 and 48 against 44 (Calendar 23 → 27, Linear 26 → 34, Slack 21 → 23).
  Sources: `openclaw_eval_01/runs/full_02.adjudicated.json` (original ids; Calendar, Linear and Slack rows of `by`)
  and `full_03.adjudicated.json` (`by`, `adjudicated`), both rebuilt with the 10-minute budget; the old source,
  openclaw_eval_01's README, still carries the 8-minute numbers.

### RQ5: blind_review_01, a stale reference

- Both texts: blind_review_01 added as its own paragraph and Table 9 rows (report.md: one row, judge v2 alone;
  report_concise.md: two rows, judge v2 alone and the pipeline), stated as AI reference labels (Codex, with the PI's
  adjudication), not a second human. Figures: pipeline 195 of 199 exact, 186 of 190 non-void (68 TP, 4 FP, 0 FN, 118
  TN); judge v2 alone 128 of 132 exact, 119 of 123 non-void (68, 4, 0, 51), 9 void on both sides; triage 67 of 67;
  exposed facts 68 of 68 on joint failures; 1 uncertain left out; bootstrap 95% intervals for weighted exact agreement
  [0.961, 0.995] (pipeline) and [0.943, 0.993] (judge); 2,705 eligible, 200 drawn, 185 cases, PI decisions affecting 12 executions.
  Sources: `blind_review_01/numbers.json` (`comparators` → `judge`, `mechanical`, `pipeline`: `exact_outcome`,
  `binary`, `binary_diagnostics`, `matrix_rows_reference_columns_comparator`, `exposed_fact_sets_joint_failures`),
  `blind_review_01/uncertainty.json` (`intervals`), `blind_review_01/README.md` and `report.md` (scope, draw, the 12
  PI decisions, the four disagreements).
- report.md RQ5 "Coverage of the check": adds blind_review_01's 200 executions.
- report.md Table 10 source, "baselines_01 on branch `exp/baselines-01`" →
  `grounding/runs/baselines_01/q4/plain_openclaw.score.json` (file checked).
