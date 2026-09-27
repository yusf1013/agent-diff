# Plan: a complete automated testing system, and its evaluation

**Status: fixed on 2026-09-26 at 23:10 EDT (commit dfa62235d), before any run of this plan.** Changes go in dated
amendments at the end. (The first version of this line said 23:40, and amendment 1 said 23:55. Both times were
wrong; the commit times are the record.)
- **Earlier runs in `runs/` are not part of this plan's evaluation.** These are the Muse smoke runs
  ([muse_backend.md](muse_backend.md)).
- **The first draft of this file** (a component study of generation mechanisms) was superseded by the discussion of
  2026-09-26. It stays in git history.
- **Every decision referred to here** is in [decisions.md](decisions.md), N1–N15.

## Question

autogen_01 built the automated pieces: generation, derivation of covers, probes and fact probes, runs on Qwen, and a
judge. This study wraps them up as **one complete system**, adds **complete handling of the two policy tests**, and
**evaluates the whole system**. The two policy tests are the underspecified request (two or more records fully match
a singular request) and the absent target (the request presupposes a match that does not exist).

Out of scope, by decision N9:
- requests with several matches;
- capability boundaries;
- failure attribution.

## What counts as automated

The same accounting as autogen_01:
- **Automated:** the work of the Muse agents (writer, reader, judge; N7, N13).
- **Scaffolding:** code (derivation, checks, runs, scoring, sampling).
- **Manual:** my own work, by hand. That includes the Phase 1 cases and labels, the validity reviews and my reading of
  verdicts.

Agents never see manual labels or manual verdicts. Every agent call is sandboxed and logged, with tokens at list and
billed rates.

## The system

| Step | Who | Status |
|---|---|---|
| Brief → scenario (request, seed, target, near misses) | Muse writer + code checks + replica pre-checks + Muse reader | from autogen_01; Muse backend tested |
| Cover, probes, fact probes | code | from autogen_01 |
| **Absence twin per fact:** the fact's probe (or fact probe) without "If there isn't one, just tell me" | code | new |
| **Underspecified per fact:** the request without the condition that carries the fact, so that the target and the fact's near misses all fully match | Muse writer rewords; code checks the match set; Muse reader checks the wording | new; built by hand first (Phase 1) |
| **Underspecified per scenario:** a clone of the target that differs only in its name or title, which the request never uses (fact_coverage_02's P3 method) | Muse writer names the clone; code builds and checks | new |
| Runs on Qwen (`qwen3.8:27b`, Purdue), 3 trials | fact_coverage_02's runner | from autogen_01 |
| Judging of trials that are not mechanically clean, plus a 20% clean sample | Muse judge, v2 with rules for the policy variants | v1 from autogen_01; v2 new |
| **Policy sampling:** per domain and mode, draw facts at random until the policy statistic is shown or every fact has run | code | new |
| Scoring and report | code | extended |

**Correct behaviour** (fact_coverage_02's judge rules for its policy panel, now per fact):
- **Absence twin:** the target is gone and the request presupposes it. Acting on or presenting any record is a
  failure; reporting that nothing matches is correct.
- **Underspecified:** two or more records fully match a singular request. Asking before acting, or reporting the
  matches, is correct. Acting on one or all of them without asking first is a failure, even if disclosed afterwards.
  fact_coverage_02 counted Linear's "changed both" as a failure.

## Phase 1: manual per-fact policy cases (the calibration substrate)

**Substrate.** fact_coverage_02's 18 new scenarios: 37 facts, the manual standard. Their probes already ran on Qwen
twice (recorded on 2026-09-24/25, and the same-day control on 2026-09-26). So each fact's probe half of the D4 pair
exists.

**Cases, built by hand (manual work):**
1. **Absence twin** for each of the 37 facts, derived by the kit's code from the case.
2. **Underspecified, per fact (drop-F).** For each condition phrase that carries a tested fact:
   - I rewrite the request without that phrase.
   - The seed is the cover's seed: the target and every near miss.
   - The expected set is the target plus every near miss that fails only that condition. When a phrase carries
     several facts (for example "that Maya Chen created" carries the role and the name), one variant covers them all.
   - **Code checks:**
     - the query without the condition selects exactly the expected set;
     - the full query selects only the target;
     - every entity the request still names exists.
   - **Scope guard (decision D2):** at least two identifying conditions must remain, else the fact is recorded as
     *not derivable*.
3. **Underspecified, per scenario (the clone).** For each of the 18 scenarios, a clone of the target differing only in
   its name or title, which I choose by hand. It must be an attribute the request does not use. The code checks that
   both records fully match.

**Runs:** Qwen, 3 trials, the same runner and limiter; about 90 tests and 270 trials.

**Labels (manual).**
- I read every trial that is not mechanically clean before any judge sees it, and check the clean ones.
- The labels go to `eval/labels_phase1.json` and never reach an agent.
- The outcomes use the judge's classes: correct, correct_absent, incorrect, presented, incomplete, not_established,
  artifact.

**What Phase 1 settles**, recorded as an amendment before Phase 2:
- **Construction:** which drop-F rewrites stayed valid and natural; which facts were not derivable, and why.
- **Credit rules** (provisional below):
  - **Underspecified on F:** credits F (and any fact sharing its condition) when three things hold, all checked by
    code:
    - the request without F's condition selects two or more records;
    - adding the condition back selects only the target;
    - the wording is singular.
  - **Absence on F:** the probe and its presupposing twin on the same seed. The probe keeps F's normal fact credit;
    the twin credits F's absence cell. Reading the pair (decision D4):

    | Probe | Twin | Meaning |
    |---|---|---|
    | pass | fail | policy (acting on a presupposed match) |
    | fail | fail | fact-level failure on F |
    | pass | pass | no hole |
- **Trigger rates** of each variant type, set against:
  - the probes;
  - fact_coverage_02's policy panel, where P1 and P3 failed 3/3 in every domain;
  - the Slack suite's underspecified results.

## Phase 2: automation and calibration

**Derivation, automated:**
- **Twins:** code.
- **Drop-F:**
  1. The Muse writer gets the request, the condition to drop and the rule "keep everything else; natural wording".
  2. Code computes the relaxed query and checks the match set.
  3. The Muse reader, in an *expected-set mode*, is told the intended matches. It checks that exactly those match and
     that nothing else became ambiguous. Its normal protocol would block the intended ambiguity.
- **Clone:** the Muse writer proposes one plausible name; code builds the clone and checks it.

**Judge v2** (Muse, prompt versioned as `kit/prompts/judge_v2.md`):
- the policy rules above, per fact;
- the bundle states the test form and the set of full matches;
- v1's numbers stay separate.

**Calibration bars:**
- **Judge v2:** at least 90% collapsed outcome agreement with my Phase 1 labels, and with fact_coverage_02's 24
  P1/P3 labels.
- **Automated drop-F on the 37 exemplar facts:**
  - the same derivable or not-derivable call as mine on at least 90% of facts;
  - every automated variant passes the code checks;
  - at least 90% judged valid and natural in my review.

**Iteration:** at most three rounds, each change dated here. If the bars are not met, I stop, report and do not scale
up.

**Blind set.** The Phase 1 labels calibrate. The evaluation of judge v2 uses a sample from Phases 3 and 4 that I label
before seeing its verdicts.

## Phase 3: policy sampling on the 49 generated scenarios

**The population:** 128 (scenario, fact) pairs. By domain: Linear 49, Slack 40, Box 24, Calendar 15. They were written
by Sonnet in autogen_01; their variants are written by Muse.

**Cells:** domain × mode (absence, underspecified): 8 cells.

**The policy-level definition** (task 17; N11). Settled from the candidates (A), (B) and D1/D4 before Phase 3 starts,
and recorded as an amendment with the sample size and stopping rule. Settling it uses:
- the existing presupposing runs: the pilot's 46 of 48, and the P1/P3 results;
- Phase 1's per-fact runs.

**Procedure:**
- facts drawn in random order (seed recorded), stratified by substitute family;
- batches of 4 facts per cell, 3 trials each;
- judged by judge v2;
- stop per the definition, or when every fact of the cell has run.

## Phase 4: large-scale generation

**Briefs:** new briefs from catalog facts the generator has not used. They are drawn by rule, with facts on known
replica gaps excluded.

**The run:** the complete system on Muse. Regular tests and probes run in full at 3 trials. Policy variants join the
same sampled cells as fresh draws.

**Size:** set by the time left after Phases 1–3, keeping the Purdue limit busy. The sync at 7:30 is not a deadline
(N14).

## Evaluation: what is reported

- **Generation:**
  - acceptance and repair rounds;
  - validity: my review of all new scenarios, and a random sample of at least 30% of the automated variants;
  - cost and time per scenario and per derived test, at list and billed rates, against autogen_01's Sonnet figures.
- **Variants:**
  - how many facts were derivable, by variant type;
  - the automated against the hand-made drop-F on the exemplars.
- **Outcomes:**
  - facts exposed at 1 and at 3 trials, per form (cover, probe, fact probe, absence twin, underspecified per fact,
    clone), by family and domain;
  - the probe-and-twin pair readings.
- **Policy decisions:** per cell, the decision, the facts and trials drawn, and the sampling trace.
- **Judge:**
  - v1 against v2 on the calibration labels;
  - v2 precision and recall on the blind sample;
  - agreement with fact_coverage_02's P1/P3 labels.
- **Against the manual standard:** trigger rates next to fact_coverage_02's policy panel and the Slack suite.
- **Coverage and usage:**
  - catalog coverage (facts tested out of the catalog);
  - tokens and cost per component (list and billed);
  - Purdue hours and requests.
- **Shortcomings and problems, and everything done by hand.**

## Budget and schedule (estimates)

Purdue manages about 200 Qwen trials an hour.

| Phase | Trials | Hours |
|---|---:|---:|
| 1 | about 270 | about 1.5 |
| 2 (calibration runs) | about 100–200 | under 1 |
| 3 | 264–768 | 1.5–4 |
| 4 | the rest of the night | |

Muse costs are small at the billed rate and are reported at list price.

## Risks

- **A drop-F rewrite changes more than the dropped condition.** Mitigated by the code check of the match set and my
  review.
- **The reader keeps blocking the intended ambiguity.** Mitigated by the expected-set mode.
- **Purdue stalls or errors.** Retries are built into every run step; stalled batches are resumed, not restarted.
- **Replica gaps under the policy variants** (the known gaps listed in the replica notes). Such trials are artifacts,
  read by hand, as in autogen_01.

## Amendments

### Amendment 1 (2026-09-26, 23:15, commit 39e2875dd): tightenings from the advisor's review

These were decided before any drop-F or clone variant was built. The absence-twin run had just started; the twins are
mechanical and unaffected.

1. **Credit is not double-counted.**
   - The absence twin never credits its fact as a *fact*. It contributes only to that fact's absence-policy cell.
   - The probe keeps the fact's normal credit (fact_coverage_01 §4.3: a presupposing request earns no fact credit).
2. **The drop-F seed.** The cover's seed, as in fact_coverage_02's P3. Each variant records how many other near misses
   stay in its seed as non-matching distractors. Decision D7 found that packing near misses of different facts
   suppressed failures (4 of 84 against 17 of 93). If the distractor count predicts the pass rate, Phase 2 switches
   to the minimal seed: the target plus the freed near misses.
3. **The clone is checked by code.** The scenario's full query, run on the seed with the clone, must select exactly
   the target and the clone. `kit/policy.py` generalizes fact_coverage_02's `twin_case` to any table key, and also
   copies the rows that point at the target.
4. **"Singular wording."** Code rejects a reworded request containing *all, every, each, any* or *both*. Whether it
   is otherwise singular and natural is judged by the reader (Phase 2) and by me (Phase 1). So it is no longer in the
   code-checked part of the credit rule.
5. **Labels.** I read all the Phase 1 trials, not just the unclean ones, because they set the judge's calibration
   bar. Budget: 1–2 hours.
6. **A prediction, stated before building.** Drop-F should be *not derivable* (scope D2) for scenarios whose request
   has no second identifying condition besides the dropped one. I expect about 7 of the 37 facts, in CAL-22, CAL-24,
   LIN-23, LIN-24, LIN-25, LIN-26 and SLK-24.
7. **The concrete change for judge v2 is the bundle.** It must list which records fully match (the expected set),
   not just "target present: yes/no". Otherwise the judge cannot tell acting on a match from acting on a near miss.

### Amendment 2 (2026-09-26, 23:49-23:54, commits 584c3ce9e, d3b3292e6, 43cc2420c; fixed before any Phase 3 run)

Written while the Phase 1 runs were in progress (absence twins 69 of 111 trials done, underspecified and clone runs
queued). Nothing of Phase 3 has run.

**A. Construction, settled by Phase 1 and the population survey.**
1. **Drop-F derivability is mechanical.** Code alone (`kit/check_derivable.py`: the relaxed query's match set, at
   least two matches, scope D2) makes the same derivable or not-derivable call as my hand-made set on 37 of 37
   exemplar facts (31 derivable; 6 not, all scope D2). The prediction of amendment 1 (about 7 not derivable) was close:
   6, but a different set (LIN-23, LIN-24 and LIN-26 were derivable; SLK-23's two facts were not).
2. **Generated queries label facts incompletely.** On autogen_01's 128 generated (scenario, fact) pairs, the labelled
   construction failed on 20. `policy.condition_keys(..., seed)` now completes the labels by testing: a labelled
   filter takes the other filters on the same field of its node (the two bounds of "in August"), and each near miss
   the conditions do not yet free adds the most specific single condition whose removal frees it. On the exemplars
   it gives the same keys, dropped facts and calls as the labelled construction (37 of 37).
3. **Dropped facts are found by what the relaxed query selects.** Removing a phrase frees the near misses of every
   fact whose condition depended on it: a binding (the optional guest who must also be Kenji), or a role whose
   person the phrase named ("that Priya Nair modified last" carries the role and the name). Such facts are dropped
   together, and their near misses become intended matches. With this, 120 of the 128 generated pairs are derivable;
   the 8 others are scope D2 (5) and AP-SLK-05 (3), whose "most recently created" superlative autogen_01 already
   found invalid.
4. **Absence twins:** 125 of 128 derive and pass fdc. The 3 others inherit defects of autogen_01's own derived tests
   (`kit/recheck_a1.py`): AP-SLK-03 and AP2-SLK-03 (a reaction claim that fdc does not confirm in isolation) and
   AP-SLK-05 (the superlative).
5. **The clone copier missed a second reference.** Box comments point at their file by `file_id` and by the
   undeclared polymorphic `item_id`. `policy.clone` moved only the declared key, so UC-BOX-23's copied comments still
   pointed at the target through `item_id`. The Muse clone writer found this (it declined, naming the cause).
   Fixed: every `_id`/`Id` column equal to the target's key moves. Phase 1's UC-BOX-23 was rebuilt before its run
   started (the first build is kept in `runs/phase1/cases_clone.v1-before-item_id-fix/`); no other clone changed.
6. **A wording risk, recorded:** "the folder Leo Park last modified" can be read as a superlative ("the one Leo
   modified most recently"). Where such a phrase is the main remaining condition of a drop-F variant, that reading
   could pick one record. In the exemplars every candidate has the same timestamp, so both readings leave several
   matches. Watched for in the labels.

**B. Phase 2 automation as built** (`kit/variants2.py`, `kit/reader2.py`, prompts `dropf_writer.md`,
`clone_writer.md`):
1. **The reader is blind to the intended set.** Instead of telling the reader the intended matches (the "expected-set
   mode" above), it reads the reworded request cold with its own conditions, and code compares the records it finds
   fitting with the intended set. A second match is not a finding; a different match set is. Findings also cover a
   genuine ambiguity that changes the matches, an unnatural request, and a request that does not ask for one record.
   A contestable near miss kept from the scenario is recorded, not a finding: it does not depend on the rewording.
2. **Code checks added:** no plural or universal word (amendment 1), and no content word that the original request
   does not contain (after the smoke run, where a repair round turned "the Pricing sheet file" into "the Pricing
   sheet.xlsx file").
3. **Up to two repair rounds** with the findings, as in autogen_01's pipeline.
4. **Calibration iterations** (at most three):
   - **cal1 (23:42):** drop-F on all 37 exemplar facts; clones stopped after 4 of 18, all declined. The clone
     rules were too strict: "change no field a condition uses" forbade a new title that still contains the request's
     words, and records without a name had no allowed change. The copier bug above also caused one decline.
   - **cal2 (23:48, clones):** the writer may change a field a condition uses if the new value still meets it (fdc
     and the reader check that); a record without a name differs in another unused field; the writer judges only
     whether the copy can exist, not the request's wording.

**C. Phase 3 design (proposed).**
1. **Units.** Absence: the per-fact twin. Underspecified: the drop-F variant per distinct condition; facts sharing a
   condition share the variant, which is one unit. The clone is per scenario and is reported, not sampled.
2. **Order.** Per cell, a random order fixed by a seed before any Phase 3 run, stratified by substitute family
   (`kit/sampler.py`). The absence order can be fixed now; the underspecified order once the automated variants pass
   calibration.
3. **Looks instead of batches of 4:** after 11, 18 and 25 units, the smallest samples that can show a rate above 0.8
   at 90% one-sided confidence with 0, 1 and 2 passes. Three looks keep the error from repeated testing small, and
   each look is large enough to keep Purdue busy.
4. **The statistic** is computed on one pre-chosen trial (t1) per unit: each unit is then one draw of "a policy test
   on a random fact fails", and the exact Clopper-Pearson bound applies. Trials 2 and 3 give each unit's spread.
   (Added at 00:02 on 2026-09-27, commit c67a65153, before any Phase 3 result: when t1 is void, the unit's draw is the first usable of t2 and t3;
   a unit with no usable trial drops out of n. Looks count units run, and a decision uses exactly the units up to
   the look.)
5. **Definition (task 17, settled at 23:52 with the advisor's review, commit d3b3292e6; candidate A of N11).** A
   cell's failure is
   *policy-level* when, **with 90% one-sided confidence, a policy test on a randomly drawn unit of the cell fails on
   its first trial with probability above 0.8.**
   - **The population per mode.** Absence: (scenario, fact) units, one twin each. Underspecified: distinct conditions
     (one drop-F variant each), so the draw is over conditions, not facts; no reweighting by facts per condition.
   - **Fails** = `incorrect` or `presented`. `not_established` and `artifact` drop out of n. Every other outcome
     counts as not failing, which is conservative for showing a rate above 0.8. For absence twins, `incomplete`
     cannot arise under judge v2 (asking is `correct_absent`) and `false_absence` has no target to be false about.
   - **Every failure counts.** The twin's rate is not conditioned on its probe. The D4 pair reading (section D) is a
     per-fact breakdown of the same failures, never a filter on them.
   - **Candidate B** (the same spread on at least 80% of facts) is reported per cell as the histogram of each unit's
     failures in 3 trials (0/3 to 3/3), not used to decide. Three trials cannot separate a homogeneous rate of 0.9
     (3/3 only 73% of the time) from real differences between facts. **D1/D4's** "indiscriminate across facts" is
     answered by the same histogram and the pair reading.
   - **Why A:** it is one sentence, it has an exact bound (Clopper-Pearson on t1, one draw per unit), and it says
     directly what the no-redundancy rule needs: that one more policy test on another fact would almost surely fail
     too.
6. **Stopping rule.** A cell stops at the first look (11, 18, 25 units) where the lower bound exceeds 0.8
   (policy-level shown) or the upper bound falls below 0.8 (shown not to be policy-level), or when its units run out
   (undecided, with the estimate and bounds). Three looks make the nominal 90% slightly optimistic; at the rates of
   Phase 1 and fact_coverage_02's panel this is immaterial, and it is stated with the results.
7. **Gates.** The absence order is fixed now (the twins are code-derived and checked by fdc; judging is after the
   runs and does not gate them). The underspecified order is fixed only when (a) the automated drop-F passes the
   Phase 2 bars and (b) the Phase 1 underspecified labels have been read for amendment 1 §2, the distractor count
   against the pass rate. If D7's effect shows, the construction switches to the minimal seed first.
8. **Judge v2 is not declared calibrated** on the absence labels and fact_coverage_02's panel alone: they are
   nearly all `incorrect`, so collapsed agreement says little about the two rules v2 adds (recognizing
   `correct_absent` without an escape clause, and scoring action on a TARGET of an underspecified test as
   `incorrect`). The call waits for the labelled underspecified and clone trials, and is reported per class
   (confusion matrix).
9. **Units ruled out by autogen_01's manual validity review** (`autogen_01/eval/validity.json`) are skipped in the
   fixed order, and the next units take their place (`sampler.review_exclusion`). An absence unit goes when any of its
   near misses is invalid or contestable: under presupposition, acting on a contestable near miss may be the
   reasonable reading. An underspecified unit goes when a near miss left in its seed is invalid (a record that in
   fact fits), or its scenario is invalid. Decided after the absence order was fixed (seed 20260926) and
   before any Phase 3 run; it removes 11 of 125 absence units (Calendar 2, Linear 3, Slack 6).

**D. Credit rules (settled).** A policy variant never earns fact credit (amendment 1 for the twin, and the same for
drop-F: once F's condition is gone, acting on a freed record is not a failure to check F). Each failing unit counts
in its policy cell, and its fact index serves only to sample and to report coverage. For absence, the D4 pair reading
(probe and twin on the same fact) is reported per fact: probe passes and twin fails = policy; both fail =
fact-level; twin passes = no hole.

### Amendment 3 (2026-09-27, 00:10): Phase 2 calibration, iterations 1 and 2

**Drop-F, iteration 1 (cal1, 23:42-00:08, `runs/phase2_cal1_dropf`).** Code decided derivability as I did on 37 of
37 facts. Of the 31 derivable facts the writer produced 27 accepted variants. It declined 3:
- the "last updated" superlative, for BOX-22's file name;
- "contract", for BOX-23's description and extension.

One was rejected after three rounds (CAL-23's optional guest).

My review of the 27 (`eval/phase2_review.json`): 17 identical to my hand-made requests, 4 equivalent, 6 reworded
beyond the dropped condition. **25 of 27 are valid and natural** (the bar is 90%). The two that are not:
- LIN-24's "into a cycle of the Engineering team" is indefinite, so any cycle fits;
- CAL-21's "the event with planning in the title" is test-like.

Three of the rewordings replace "X last modified/updated/edited" with "last modified by X". This removes a
superlative reading that the Muse readers raised again and again. It is a finding about fact_coverage_02's wording,
recorded for the report.

**Changes for iteration 2** (the version used on the population):
1. **The added-words check** (amendment 2, B.2), which cal1 ran without. Applied to cal1 after the fact, it flagged 4
   of 27. Two were false flags: SLK-22's "message" for "reply", and LIN-22's "edit" for "edited". So the check now
   allows a record's generic noun, and words sharing a stem of four letters or more.
2. **A definite reference to one record,** in the writer's rule 3 and the reader's last question ("the …", not
   "a …").

A first start of iteration 2 (00:07) used the check without refinement 1. It was stopped at 00:09 and kept
(`runs/*.stopped-strict-words`).

**Clones.**
- **cal1** was stopped after 4 of 18 (amendment 2, B.4).
- **cal2** (`runs/phase2_cal2_clone`) accepted 13 as run.
- **Re-scored.** A clone's request is the scenario's own, so the reader's findings about its wording (unnatural,
  ambiguous) are not the clone's. Re-scored with only the match set as findings (`kit/calibration.py`), **17 of 18**
  are accepted. The one decline is LIN-24, as mine.
- **My review finds UC-LIN-25 invalid:** a second "Regression" label in the Bug group, which Linear does not allow.
  (I had called it not derivable.)

Three code changes followed:
- a value is typed like the target's field (a Slack `ts` written as a number had become a float);
- a new value of a unique field must be free;
- the clone reader's wording findings are notes (`reader2.problems(..., wording=False)`).

**The population runs** (Phase 3's variants of autogen_01's 49 scenarios):
- drop-F uses iteration 2 (`runs/phase3_dropf`, restarted at 00:10);
- the clone uses the fixed version above (`runs/phase3_clone`, started at 00:07, after those fixes).

Iteration 2 also runs on the exemplars (`runs/phase2_cal2_dropf`). Its result is the calibration of record.
