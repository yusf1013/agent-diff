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

**Which numbers:** every source below is read as of commit 663af2ce1c (after the 10-minute rebuild 49ce3672dc and
the duplicate merge 4fec9ec540). The later commit 3405221d90 (two PI rulings from blind_review_01: 563 regular
tests, Box absence 58 and Box underspecified 52 valid units) rebuilt `numbers/exposure.json`, `numbers/policy.json`
and the decision files, but not `numbers/concise.json` or `numbers/coverage.json`; its numbers are not applied here.
A reader of a later `numbers/` file will find other values than the ones logged below. Once these texts are updated,
the Recount section's note that they "still carry the 8-minute numbers" no longer holds.

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

### RQ6: the policy cells and the per-fact space

Table 11 in both texts is read from `openclaw_eval_01/runs/policy/decisions_population_absence.json` and
`decisions_population_underspecified.json` (`valid_units`, `failing_trials`, `usable_trials`, `rate`, `p10`, `p90`,
`decision`, `readings.spread`, the writers' parts), rounded half up. `numbers/policy.json` agrees for the six cells the
merge did not touch; for Linear and Slack underspecified it predates the merge (79 and 32 valid units, p10/p90 0.343
/ 0.469 and 0.69 / 0.844).

- Table 11: Box absence 142/179, 0.79 [0.74, 0.85], spread 6/4/11/38 → 132/171, 0.77 [0.71, 0.83], 6/4/10/33;
  Calendar absence 104/126, 0.83 [0.77, 0.88], 3/2/9/28 → 101/124, 0.82 [0.75, 0.87], 4/1/8/27; Linear absence
  202/294, 0.69 [0.64, 0.74], 17/13/14/52 → 160/263, 0.61 [0.55, 0.67], 21/12/9/35; Slack absence 80/129, 0.62
  [0.54, 0.70], 10/5/9/19 → 75/125, 0.60 [0.52, 0.68], 10/5/5/19; Box underspecified 97/167, 0.58 [0.52, 0.65],
  10/15/9/21 → 71/145, 0.49 [0.42, 0.56], 11/12/6/13; Calendar underspecified 52/90, 0.58 [0.49, 0.67], 6/7/6/11 →
  37/81, 0.46 [0.36, 0.56], 8/5/3/8; Linear underspecified 79 units, 120/236, 0.51 [0.45, 0.57], 25/10/19/24 → 78,
  83/205, 0.41 [0.34, 0.47], 25/10/5/17; Slack underspecified 32 units, 79/96, 0.82 [0.75, 0.89], 2/3/5/22 → 31,
  63/82, 0.77 [0.69, 0.84], 2/3/4/12. Decisions unchanged. (report_concise.md shows no spread.) report.md adds a note
  on the merge, the spread (units with exactly 3 usable trials, `autogen_02/kit/sampler.py`, `cell_stats`) and the
  first-pass column (the first pass's own record, not recomputed).
- The budget bullet (report.md) and sentence (report_concise.md), "With over-budget trials left as the judge called
  them, the rates are 0.77, 0.82, 0.61, 0.60 and 0.49, 0.46, 0.41, 0.77" / "Removing the eight-minute budget rule
  changes rates but none of these decisions" → the 10-minute rates are those above; under the withdrawn 8-minute
  reading they were 0.79, 0.83, 0.69, 0.62 and 0.58, 0.58, 0.51, 0.82, with the same decisions. Source for the old
  rates: `numbers/policy.json` at 49ce3672dc^ (the previous Table 11).
- report.md, writers in the Calendar cells: absence 0.90 (Phase 4), 0.96 (6b) against 0.64 → 0.88, 0.96 against
  0.64; underspecified 0.71 and 0.53 against 0.37 → 0.64 and 0.27 against 0.23. Source: the decision files,
  `phase3_only`, `phase4_only`, `6b_only`.
- Table 12 (both): facts failing detect@3 169 / 140 / 309 → 159 / 113 / 272; detect@1 145 / 111 / 256 → 131 / 81 /
  212; both 82 / 62 → 79 / 54; policy only 87 / 78 → 80 / 59; regular only 2 / 12 → 6 / 21; neither 26 / 21 → 32 /
  39. Source: `numbers/policy.json` (`totals`, `regular_vs_policy_facts`); these count facts, which the merge does not
  change. report.md's units row, "Valid units, all run and judged 244 / 197 / 441" → "all run" 244 / 197 (195 with
  each duplicate pair once) / 441 (439), plus "with a usable trial" 240 / 189 / 429 (the decision files' `units`,
  summed over the four cells; `policy.json`'s `judged`, 240 / 191, predates the merge). report_concise.md keeps "Valid
  executable cases" 244 / 197 / 441 (both cases of a pair ran).
- Prose: report.md "Of the 84 facts ... 82 also fail it. Another 87 facts" → 85, 79, 80; report_concise.md "Another
  87 facts ... and 78" → 80 and 59; report.md "Muse's Phase 4 scenarios alone ... 45 failing; ... 41 failing" → 43
  and 32 (`policy.json`, `by_source` → `phase4`; the duplicate pairs are in 6b and Phase 3, so Phase 4's units are
  unchanged); report.md's answer "169 facts ... 140 (309 ..., 256 ...)" → 159, 113 (272, 212).
- Not changed: the first-pass column, the readings bullet (any-of-runs: Box absence, Calendar absence and Slack
  underspecified policy-level, the others undecided or not; all-runs: none policy-level; checked in the decision
  files).

### RQ7: corrections from values_01, and a pointer to it

- Restore row (both texts), "Wrote, then restored a record | 6 | 3 | 4" → "6 | 0 | 2", with two new rows: "Wrote a
  value already there, or a field the record lacks | 0 | 3 | 2" and "Posted a comment, then deleted it (no trace in
  the diff) | 1 | 1 | 0". The original 13 are the executions whose diff shows a record touched and left unchanged;
  read with their trajectories, 8 are restorations and 5 no-ops; the 2 deleted comments are found only in the
  transcripts. Source: `values_01/report.md` §2.5 (the restore table); `values_01/eval/labels.jsonl` (stratum
  `restore`, one label per execution).
- The harmful-change row (both texts), "moved it from 10:00 to 17:00 (a time-zone error) and reset the attendees'
  replies, then reported the old time" / "Changed meeting time and attendees' replies" → the full update reset both
  attendees' accepted replies; the time did not move (the replica stores API-written times in UTC and seeded times as
  local; the API still shows 10:00; the reply's time was right). Source: `values_01/report.md` §2.4 and §5;
  `values_01/eval/labels.jsonl`, key `solve_population_absence/t3/AT-G4-CAL-01-I11-I12`.
- report_concise.md's provenance note: the two corrected rows and values_01's itemized record named.
- A short paragraph (report_concise.md) or bullet (report.md) pointing to values_01, with its headline numbers:
  1,275 of 1,399 value writes right; 105 of 149 priority writes wrong; 179 executions with a finding, 52 of them
  passing grounding; 96 replies (R3), 60 (R4); 9 of 15 undone or no-op writes undisclosed. Source:
  `values_01/report.md`, "The answer in brief", §2.2, §2.3, §2.5. It replaces the "not measured" line (report.md) and
  "have not received a systematic value audit" (report_concise.md).
- Unchanged: Table 13 and the other rows (values_01 agrees with them: 4 outside the candidate set, 2 changed to fit,
  2 other fields disclosed, 32 Box replica effects).
