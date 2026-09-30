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
| Regular tests exposing a fact | 138 of 565 | 143 of 565; 139 of 563 after the two rulings below |
| Facts exposed, detect@3 / detect@1 | 87 / 60 | 88 / 61; 87 / 60 after the two rulings below |
| Policy decisions | 5 not policy-level, 3 undecided | the same 5 and 3, at lower failure rates |
| Box absence rate | 0.79 [0.74, 0.85] | 0.77 [0.71, 0.83] |
| Slack underspecified rate | 0.82 [0.75, 0.89] | 0.77 [0.69, 0.84] |

**The report texts (report.md, report_concise.md) still carry the 8-minute numbers**; their tables are to be
updated from `numbers/` (RQ4, RQ6, §0.4's execution categories, the limits section).

**Two of the PI's blind-review rulings applied to the rulings file (2026-09-30, 01:30):** G4-BOX-11's witness 8201
("Seaport Archive 2024" matches "the Seaport Archive folder") and G4-BOX-02's witness 8112 (a copy in a subfolder
of the named folder) are flawed, group B. Found by the sol_score session; they had never reached
`roadmap_01/known_defects.json`. Two probes leave the suite (563 tests); Box absence has 58 valid units and Box
underspecified 52; every decision stands.

**numbers/ rebuilt in full at 02:00 (2026-09-30)** after the two rulings: `kit/concise.py` now skips the policy
executions of units the rulings exclude and records the counts instead of asserting the old ones. The final manifest
is **998 cases, 2,994 executions** (regular 1,689; absence 726; underspecified 579); 18 policy executions of the 6
excluded units and 6 regular executions of the 2 excluded probes leave it. Studies that used the earlier 3,018
manifest (blind_review_01, judge_qwen_01, values_01) keep their own populations.

## Text changes (2026-09-30)

report.md and report_concise.md brought to the rebuilt numbers (brief:
[report_update.md](../../protocols/briefs/report_update.md); session "values"). Every number is read from a file;
none is recomputed from memory. `numbers/` and `kit/` are unchanged by this work. Format: section, old → new, source;
"old" is the text before these changes.

**Which numbers:** every source is read as of commit a8c046c891 (`numbers/` rebuilt in full after the two PI
rulings above). A first pass (commits 787c4f576b to 1908825239) used the files at 663af2ce1c, before the rulings;
the commits after the merge 3ba8bafe21 re-synced it, and the entries below give the final values. Table 11's
figures are read from the two decision files (`openclaw_eval_01/runs/policy/decisions_population_*.json`), the
sources the table already cites. `numbers/policy.json` has the same rates and intervals, but its `valid` and
`judged` count cases where the decision files count units with each duplicate pair once (Linear underspecified 79
and 76 against 78 and 75, Slack underspecified 32 and 31 against 31 and 30). With these texts updated, the Recount
section's note that they "still carry the 8-minute numbers" no longer holds.

### Setup (§0)

- report.md §0.3, "The 8-minute budget" → "The 10-minute budget": a trial ended by OpenClaw's 600-second turn limit
  (or whose agent time, limiter waits excluded, passes 600 s) is the agent's failure; the 8-minute reading is
  withdrawn. Source: roadmap, "Decisions (2026-09-29)"; `openclaw_eval_01/rulings.py` (`BUDGET_S = 600`,
  `over_budget`); this README, "Recount".
- Both texts' opening note: states the update of 2026-09-30, pins commit a8c046c891 and points here.
- report_concise.md §0.4: 1,006 cases and 3,018 executions → 998 and 2,994; the table's individual probes 189 Muse,
  363 cases, 1,089 executions → 187, 361, 1,083; regular subtotal 294, 565, 1,695 → 292, 563, 1,689; absence 128,
  244, 732 → 126, 242, 726; underspecified 99, 197, 591 → 95, 193, 579; total 521, 1,006, 3,018 → 513, 998, 2,994;
  "363 individual probes" → 361; "465 probes ... 441 policy cases" → 463 and 435; "We used 1,006 cases" → 998. The
  token estimate 371.73M input, 329.41M cached, 9.66M output, 381.39M total, `3,018 / 4,464` → 368.77M, 326.79M,
  9.58M, 378.36M, `2,994 / 4,464` (88.62% cached unchanged). Sources: `numbers/concise.json` (`case_count`,
  `execution_counts`, `writers` → `forms`, `policy_by_scenario_writer`, `token_estimate`, `scope`).
- Both texts §0.4, new paragraph (report_concise.md) or bullet (report.md), as the lead asked: the two blind-review
  rulings applied on 2026-09-30 made two Box near misses flawed and removed 2 probes and 6 policy units (2 absence, 4
  underspecified; 6 regular and 18 policy executions); blind_review_01, judge_qwen_01 and values_01 used the earlier
  3,018 manifest. report.md adds that the removed units' trials stay in its opening table (`numbers/scale.json`
  counts every trial run). Sources: this README (the rulings and the full rebuild, above); `numbers/concise.json`
  (`excluded_policy_trials`: 6 and 12); `numbers/generator.json` (`left_out`: P-G4-BOX-02-I11, P-G4-BOX-11-I11).

### RQ1: a stale reference

- report.md RQ1, "`grounding/runs/boundary_01/report.md` on branch `exp/automation-01`" → a link to
  `../boundary_01/report.md`, merged into main (file checked).

### RQ2: the F0 rule

- report.md RQ2 "Near-miss family" and report_concise.md RQ2 (the 37 facts credited only through plain near
  misses): "30 are state attributes ...; the other 7 are 5 text attributes, A:Cycle.number and
  R:IssueRelation.relatedIssueId" / "seven have weaker plain-value evidence" → the F0 rule's split: 30 states; 4 with
  no lure in the domain model (Box A:Hub.description, Linear A:Document.content and A:Team.description, Slack
  A:User.title); 2 whose lure the rulings make flawed (Linear A:Cycle.number, Slack A:Message.message_text); 1 being
  regenerated (Linear R:IssueRelation.relatedIssueId). Sources: `numbers/coverage.json`
  (`credited_only_through_plain_near_misses`, the 37 ids); roadmap, "Decisions (2026-09-29)", "The F0 rule".
  Counts unchanged (37, 167).
- Both texts, facts per family: F8 41 → 40 (the two rulings left one fact without a valid F8 near miss); the others
  unchanged. Source: `numbers/coverage.json` (`facts_per_family`).

### RQ3: the two rulings, duplicate policy units, a stale reference

- Table 5 (both), after the two rulings: near misses ruled flawed 8 → 10 (Muse 6b 1 → 3); tests left out by the
  rulings 10 → 12 (6b 1 → 3); valid regular tests 565 → 563 (6b 136 → 134; report_concise.md's Muse 294 → 292);
  report.md "565 of 582 (97%)" → 563 (97% unchanged); report_concise.md "565/582 (97.1%)" → "563/582 (96.7%)".
  Source: `numbers/generator.json` (`flawed_near_misses`, `left_out_by_rulings`, `valid_total`, `valid`).
- report.md "Policy units on OpenClaw": 244 → 242 absence and 197 → 193 underspecified valid units, naming the two
  rulings (2 and 4 Box units left out); adds that two underspecified pairs are one request each (U-AP-SLK-03,
  U-G4-LIN-14) and count once in RQ6's statistic, 191 units there. Sources: `numbers/policy.json` (`totals`:
  `units`, `valid`); `openclaw_eval_01/rulings.py` (`DUPLICATE_UNITS`); the decision files (`valid_units`,
  52 + 30 + 78 + 31 = 191).
- report_concise.md Table 6: excluded 11 and 12 → 13 and 16; valid 244 and 197 → 242 and 193; Muse parents 128 and
  99 → 126 and 95; executions 732 and 591 → 726 and 579; totals 23, 441, 227, 1,323 → 29, 435, 221, 1,305. A new note
  on the duplicate pairs: both cases of each pair ran and count here; RQ6's statistic counts each pair once (191
  underspecified cases, 433 policy cases in all). Sources: `numbers/policy.json` (`totals`), `numbers/concise.json`
  (`policy_by_scenario_writer`, `execution_counts`); the decision files.
- Cost per valid regular test (both) $0.125 → $0.126 ($0.007 billed unchanged), and report_concise.md's "294 valid
  regular cases" → 292: `numbers/costs.json`, $36.74 list and $2.08 billed, over Muse's 292 valid regular tests (the
  old figure reproduces with 294). report_concise.md "the 1,006-case evaluation" → 998.
- report.md RQ3, "`machinery.json` on branch `exp/baselines-01`" → `grounding/runs/baselines_01/machinery.json`
  (merged into main; file checked).

### RQ4: exposure under the 10-minute budget and the two rulings

Sources: `numbers/exposure.json` (`final`, `by_domain`, `by_form`, `by_writer`, `by_kind`, `probes_by_family`,
`probes_designated_vs_plain`, `trials`); `numbers/concise.json` (`writers` → `exposure`). Percentages recomputed from
those counts.

- Both texts, the budget sentence: "the 8-minute budget" / "over the eight-minute agent-time budget" → the 10-minute
  budget (OpenClaw's own turn limit). The regular tests 565 → 563.
- Table 7: Box 139 tests, 39 exposing, 27 and 21 facts, 48% → 137, 35, 26 and 20, 46%; Calendar 32 → 34 tests
  exposing, 12 → 13 facts at detect@1; Linear 45 → 47 tests, 30 → 31 facts at detect@3, 38% → 39%; Slack 22 → 23
  tests; all 565 tests, 138 exposing (24.4%) → 563, 139 (24.7%) (report.md: 24% → 25%); facts 87 and 60 and the
  share (42.6%; report.md 43%) come out unchanged.
- Table 8, forms: probes 363 tests, 101 exposing (28%) → 361, 103 (29%), facts 79 (55) unchanged; fact probes 25
  (25%) → 24 (24%), facts 25 (14) → 24 (12). Covers unchanged.
- Table 8, writers (report.md): Sonnet P 17 (22%) → 18 (23%), 12 → 13 facts; Sonnet P v2 18 (20%) → 19 (21%); Muse
  Phase 4 45 (28%) → 47 (30%), detect@1 19 → 20; Muse 6b 136 tests, 34 (25%), 22 of 69 (14) → 134, 31 (23%), 22 of
  69 (13). Sonnet R unchanged. (report_concise.md): Sonnet 59 (22%) → 61 (23%); Muse 294 cases, 79 (27%) → 292, 78
  (27%), facts 47 and 33 unchanged.
- Table 8, kinds: attributes 41 → 42 at detect@1; relationships 13 → 12 at detect@1 (19 at detect@3 unchanged).
- Families: designated 84 of 282 (30%) → 86 of 280 (31%); F8 25 of 52 (48%) → 24 of 51 (47%); F1 31 of 98 (32%) →
  34 of 98 (35%); report.md F6 4 → 5 of 16, F2 6 of 32 (19%) → 5 of 31 (16%), "28% of probes" → 29%.
- Trials: of 1,695, 254 failing (15%), 1,310 passing, 104 over the 8-minute budget, 14 flawed-only, 13 void → of
  1,689, 255 (15%), 1,348, 52 ended by the 10-minute budget, 20 flawed-only, 14 void (12 artifacts, 2 not
  established).
- report.md, opaque ids (same 333 tests): 80 against 65 tests and 48 against 42 facts (Calendar 23 → 25, Linear
  23 → 33, Slack 19 → 22) → 84 against 70 and 48 against 44 (Calendar 23 → 27, Linear 26 → 34, Slack 21 → 23).
  Sources: `openclaw_eval_01/runs/full_02.adjudicated.json` (original ids; Calendar, Linear and Slack rows of `by`)
  and `full_03.adjudicated.json` (`by`, `adjudicated`), both rebuilt with the 10-minute budget (the two rulings
  touch only Box, which is not in this comparison); the old source, openclaw_eval_01's README, still carries the
  8-minute numbers.

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

### RQ8: the baselines on main, the Muse expectation, one coverage rule

- Intro (both): report_concise.md "The baseline evidence remains on the existing baseline branch" → "The baseline
  study is baselines_01 (link), now on main"; "outside the 1,006-case methodology count" → 998
  (`numbers/concise.json`, `case_count`). report.md "(branch `exp/baselines-01`, ...)" → a link to
  `../baselines_01/report.md`, now on main (file checked).
- report_concise.md Table 14, the Muse column: "all 294 Muse regular cases" and "sampled from 294 valid" → 292;
  facts exposed @1 7.9 → 7.7; covered facts counting every plain decoy 47.7 → 47.8; exposed @3 (12.2), exposing tests
  (14.0) and F1–F8 coverage (38.3) come out unchanged. Source: `numbers/concise.json` (`equal_budget_muse_final`;
  `writers` → `Muse` → `exposure`, 292 tests). Writer cost $6.00 ($0.34) → $6.04 ($0.34), recomputed as the text
  describes it: `numbers/costs.json`, "Muse: scenario generation (writer and cold reader)", $36.74 list and $2.08
  billed, × 48 / 292 (the old figure reproduces with 294).
- report_concise.md, the coverage-row note: "uses the baseline study's narrower F1–F8 rule on both sides. Under the
  main report's rule, including F0, ..." → one rule on both sides, F1–F8 ("designated" means F1–F8 in this table);
  the F0 rule would also credit plain decoys for states and the six facts without a usable lure, on neither side
  here; counting every plain decoy 47.8; the baseline summaries give only the F1–F8 count. Sources: roadmap, "The F0
  rule" ("The baseline comparison uses the same rule on both sides"); `kit/concise.py` (`designated_facts_covered`
  leaves out F0); `baselines_01/n0/review_gen_01.py` ("proper": an F1–F8 near miss in a fact-sensitive form);
  `numbers/concise.json` (`baseline_comparison`, no any-family count for the baselines).
- report_concise.md Table 15: the paired-probe link `../../../.claude/worktrees/baselines-01/...` →
  `../baselines_01/plain48/README.md` (file checked); forms 101/363 and 25/102 → 103/361 and 24/102 (covers 12/100
  unchanged; `numbers/exposure.json`, `by_form`); triage "879/3,018 ... the other 2,139" → "879/2,994 ... the other
  2,115" (`numbers/concise.json`, `judge_verdicts_on_final_executions`, `execution_counts`).
- report.md: "Phase 4's final score is close: 45 tests exposing and 26 facts, against 41 and 28 in the first pass"
  → 47 and 26 under the 10-minute budget, the first pass's 41 and 28 "as baselines_01 counted it, before the budget
  changed" (`numbers/exposure.json`, `by_writer` → `Muse Phase 4`; baselines_01 `ours.json`).
- report.md Table 14: the source note adds that the coverage rows count F1–F8 on both sides (the F0 rule on neither),
  that the Ours column is Phase 4's first pass as baselines_01 computed it, not recomputed, and the final-outcome
  expectation for all 292 Muse regular tests: 12.2 facts at detect@3, 7.7 at detect@1, 14.0 tests exposing
  (`numbers/concise.json`, `equal_budget_muse_final`). Row label "(credit rule)" → "(F1–F8)".
- report.md, Phase 4's policy units: 45 failing (39 through designated near misses) and 41 (38) → 43 (37) and 32 (29);
  units and facts unchanged (60 over 56, 50 over 52). Source: `numbers/policy.json`, `by_source` → `phase4`.
- **Not changed, no source in `numbers/`:** report.md Table 14's Ours column (34.0, 81 of 99, 11.0 / 7.2, 12.5,
  $5.44) and "48 of ours expose about 11": baselines_01 `ours.json` and `compare.json`, computed from
  `full_02.adjudicated.json` before the 10-minute rebuild. That file, as rebuilt, gives Phase 4's first pass 42 tests
  exposing and 29 facts (28 at detect@3 → 29, 20 → 21 at detect@1), so the column would move a little if recomputed.
  report.md Table 15 row 5 (first pass: covers 2 of 77, probes 76 of 279, fact probes 16 of 80; designated 67 of 223,
  plain 9 of 56): baselines_01 `log.md`, from `full_02` before the rebuild. Row 7 (triage against judge v2 on
  `full_02`'s 1,314 trials): baselines_01 `q4/numbers.json`, from the judge's verdicts, which the budget does not
  change. The baselines' own numbers are unaffected: baselines_01 counts a timeout only when the harness's turn limit
  ended the trial (`summarize_labels.py`, `plain48/score.py`).
