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
