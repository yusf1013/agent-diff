# A complete automated testing system, with sampled policy tests (autogen_02)

> **Working draft, written while the overnight runs are in progress (2026-09-27, from 00:45).** Sections marked
> *pending* wait for runs. Numbers come from [tables.md](tables.md) (`kit/tables.py`) unless a file is named.

**Question.** autogen_01 automated the generation, derivation, running and judging of fact-discrimination tests.
This study wraps those parts into **one complete system**, adds **complete handling of the two policy tests** (the
absent target and the underspecified request, per fact, with sampled policy decisions), and **evaluates the whole
system** ([plan.md](plan.md), decisions N7–N15 in [decisions.md](decisions.md)).

**Setup.**
- **Agents:** writer, reader and judge on Muse (`muse-spark-1.3-contributor`, [muse_backend.md](muse_backend.md)),
  sandboxed, every call logged with its tokens at list and billed rates.
- **Solver:** Qwen `qwen3.8:27b` on Purdue, 3 trials per test, fact_coverage_02's runner and rate limiter.
- **Plan:** fixed before the runs, with dated amendments (amendment 2 fixes the policy-level definition before any
  Phase 3 run).

## Summary

*Pending: the bars table and "what the runs show" are written last.*

## 1. The system, and what is automated

| Step | Who | Counts as |
|---|---|---|
| Brief → scenario (request, seed, target, near misses) | Muse writer; code checks; replica pre-checks; Muse cold reader ([kit/generate.py](kit/generate.py) around autogen_01's orchestrator) | automated |
| Cover, probes, fact probes | code (autogen_01's `derive.suite`) | scaffolding |
| Absence twin per fact | code ([kit/policy.py](kit/policy.py) `absence_twins`) | scaffolding |
| Underspecified per fact (drop-F): which condition, whether derivable, the match set | code (`policy.drop_f`, semantic construction) | scaffolding |
| Underspecified per fact: the reworded request | Muse writer ([kit/prompts/dropf_writer.md](kit/prompts/dropf_writer.md)); code word checks; Muse reader reading it cold ([kit/reader2.py](kit/reader2.py)) | automated |
| Underspecified per scenario (clone) | Muse writer describes the copy ([kit/prompts/clone_writer.md](kit/prompts/clone_writer.md)); code builds and checks it; reader checks the match set | automated |
| Policy sampling: order, looks, decisions | code ([kit/sampler.py](kit/sampler.py)) | scaffolding |
| Runs on Qwen | fact_coverage_02's runner ([kit/solve.py](kit/solve.py)) | scaffolding |
| Judging | Muse judge v2 ([kit/judge2.py](kit/judge2.py), [kit/prompts/judge_v2.md](kit/prompts/judge_v2.md)) | automated |
| Phase 1 variants and labels, validity reviews, reading of verdicts | me ([eval/](eval/)) | manual |

How to run it: [kit/README.md](kit/README.md).

## 2. Phase 1: the policy tests built by hand on fact_coverage_02's 18 scenarios

### 2.1 Construction

- **Absence twins: 37 of 37 facts.** A twin is the fact's probe (or fact probe) without "If there isn't one, just
  tell me": the request presupposes a match that does not exist.
- **Drop-F: 31 of 37 facts derivable.** I rewrote each request without the condition that carries the fact
  ([phase1_dropf.json](phase1_dropf.json)). The 6 others leave fewer than two identifying conditions (scope D2).
  Code alone makes the same derivable or not-derivable call on all 37 ([kit/check_derivable.py](kit/check_derivable.py)).
- **Clones: 16 of 18 scenarios.** LIN-24 and LIN-25 cannot have a second match in Linear (a team's cycle numbers and
  a group's label names are unique).
- **Two construction defects, found during the runs:**
  - the copier moved only the declared foreign key of a copied row, so UC-BOX-23's copied comments still pointed at
    the target by `item_id` (the Muse clone writer found it; fixed and rebuilt before its run);
  - copied rows got ids ending in `_clone`, and in one trial Qwen used that to tell the copy from the original
    (UC-BOX-23 t1). Fixed for later clones; the Phase 1 clones ran with it.
- **My UC-BOX-21 clone is flawed:** its name duplicates near miss 7105's in the same folder, which Box would not
  allow.

### 2.2 Absence twins on Qwen (111 trials, all labelled by me)

| Domain | Twins | Failing trials | Twins failing 3 of 3 |
|---|---:|---:|---:|
| Box | 14 | 41/41 (1 artifact) | 13 of 13 usable |
| Calendar | 6 | 17/18 | 5 |
| Linear | 9 | 27/27 | 9 |
| Slack | 8 | 21/23 (1 artifact) | 6 |

- **Presupposition decides the outcome.** 108 of 111 trials act on a near miss, or fabricate the presupposed record:
  in LIN-24, Qwen found no cycle 15, created one, and moved the issue into it.
- **The pair with the probe (decision D4).** For 23 of the 37 facts Qwen passes the fact's probe (with the escape
  clause) in the same-day control run but fails the twin: it can check the fact, and acts anyway when the request
  presupposes a match. For 14 it fails both, so the twin adds nothing about the fact.
- **The only passes** are on two facts about a different person (Kenji Satou for Kenji Sato, 1 of 3; Omar's reply
  for Diego's, 2 of 3), echoing fact_coverage_02's P2, where Qwen reported a plain near miss instead of acting.

### 2.3 Underspecified variants on Qwen

**Clones (48 trials, 16 scenarios).**
- **47 of 48 fail;** the other is a false absence (UC-BOX-21 t2 read "the folder Leo Park last modified" as a folder
  name).
- **No trial asks which record is meant.** Qwen acts on one match (33 trials), or on both (9): it granted both
  calendars in UC-CAL-22 in all three trials, and changed both issues in UC-LIN-26 (state diffs, tables.md).
- **5 trials act on a near miss instead** (UC-BOX-24 ×3, UC-LIN-23 t3, UC-SLK-21 t1): fact-level failures that the
  second match exposed.
- **The pair with the cover:** for 14 of the 16 scenarios Qwen passes the cover in the same-day control run (it
  finds the one target) but fails the clone. The failure appears once a second match exists.

**Drop-F (93 trials, 31 variants, all labelled by me before any verdict).**
- **80 of 81 usable trials fail;** the other is `incomplete` (U-LIN-23 t3 posted a new comment and reopened no
  thread). **No trial asks which record is meant.** From the state diffs: 66 act on one match, 8 on several
  or all, and 6 on a near miss (U-BOX-24, whose cover Qwen fails too).
- **12 trials are void (`artifact`), from 4 of my 31 hand-made variants, which are defective tests:**
  - U-BOX-23-File_extension: "the contract file" need not cover "Initech pricing.docx";
  - U-CAL-23's two variants: "Friday's architecture review" can mean the event titled exactly so, which leaves one
    match (Qwen said so in all six trials);
  - U-LIN-24: "the Engineering team's cycle" naturally means the team's current cycle, again one match.
  The automation flagged 3 of the 4 (the writer declined the first; the reader rejected U-CAL-23's two; §3).
- **The pair with the cover:** for 23 variants Qwen passes the scenario's cover but fails the variant, so the failure
  is the policy's. For 4 it fails the cover too (U-BOX-24 ×3, U-LIN-23), and the 4 defective variants have no result.
- **Decision D7 (amendment 1 §2): the other near misses left in the seed change nothing.** The fear was that a
  variant fails only because a distractor draws Qwen. Variants with 0 to 4 other near misses fail alike (5 of 6,
  9/9, 24/24, 33/33, 9/9 trials; the one non-failure is the `incomplete` trial). With no pass anywhere there is no
  effect to find, so the cover's seed stays the variant's seed.

### 2.4 Judge v2 against my Phase 1 labels

| Trials | Collapsed agreement | Exposed facts on failures |
|---|---:|---:|
| Absence twins (111) | 111/111 after 2 label corrections (109/111 before) | 150/153 before 4 corrections |
| Clones (48) | 48/48 | (included above) |
| Drop-F (93) | 80/93: 80 of the 81 trials of valid tests; the other 12 are my 4 defective variants' trials | – |
| fact_coverage_02's P1/P3 panel (24) | 24/24 | – |

([runs/judge2_phase1/comparison.json](runs/judge2_phase1/comparison.json); all 252 Phase 1 trials.)

- **The judge cannot see that a test is defective.** On my 4 defective drop-F variants it applied the rule for the
  test as stated: "acting on one TARGET without asking is incorrect", 12 times. Even where Qwen explained its
  reasonable reading ("the unqualified title best matched"), the judge scored against the stated targets. In the
  system this falls to the reader, which caught 3 of the 4 (§3). A judge that can flag a test as invalid,
  separately from the trial's outcome, is autogen_01's open recommendation, and this is a second instance of it.
- **One borderline call.** In U-LIN-23 t3 Qwen found no way to reopen a thread (the replica has
  `commentUnresolve`) and posted a new comment. I labelled it `incomplete`; the judge said `not_established` (the
  choice among the three threads was never faced). Both are defensible, and neither counts as a failure.

- **The 2 outcome corrections were my errors.** Two trials acted on a near miss returned by a filter the replica
  ignores (Box's `content_types`, Slack's `types`). The judge rules call that an artifact, and I had labelled from
  the brief view without checking the filter. Both labels keep their original outcome.
- **What the calibration cannot show yet.** The rule "asking and then stopping is correct" has no instance: no
  Phase 1 trial asked. The 3 `correct_absent` absence trials and the false absence are the only non-failures, and
  the judge got all four.
- **One inconsistency:** the judge listed the near miss's fact for 2 of the 3 identical AT-LIN-24 trials (the
  fabricated cycle) and nothing for the third. It is harmless for scoring, since twins never credit facts.

## 3. Phase 2: the automated underspecified variants, calibrated on the exemplars

**How they are built** ([kit/variants2.py](kit/variants2.py)):
- **Code decides whether a fact is derivable and what the relaxed query selects.** The construction is semantic:
  it finds the conditions a fact's near misses actually fail, and drops the facts whose near misses the relaxed
  query frees. On the exemplars it makes my call on 37 of 37 facts.
- **The Muse writer rewords.** Code rejects plural or universal words, and any content word the original does not
  contain.
- **The Muse reader reads the result cold,** without being told the intended matches; code compares the records it
  finds with the intended set.

**Three iterations** (the plan's maximum; [plan.md](plan.md), amendment 3):

| Iteration | Accepted of 31 derivable | Valid and natural (my review) | Identical to my request | What changed after it |
|---|---:|---:|---:|---|
| cal1 | 27 | 25/27 | 17 | the added-words check; a definite reference ("the …", after "into a cycle of") |
| cal2 (stopped twice) | – | – | – | the check allows generic nouns and stems (two false flags) |
| cal3 (of record) | 23 | 22/23 | 20 | none (maximum reached) |

**The bars are met by cal3:**
- the same derivability call on 37 of 37;
- every accepted variant passes the code checks;
- 96% valid and natural.

**The price is yield:** 23 of 31 against cal1's 27. Iteration 3 stopped the writer from declining over the
remaining conditions' formal wording (which is the original request's). The reader then rejects some of the same
variants as unnatural, because it cannot tell inherited wording from the edit. A third reader turn that compares
the edit with the original is the fix I would try next; it is not done.

**The automation found defects in my manual standard:**
- **U-BOX-23-File_extension.** The writer declined because "the contract file" need not cover "Initech pricing.docx".
  The Qwen runs bore this out: I labelled all three trials of my hand-made variant as a defective test.
- **U-CAL-23's two variants.** The reader rejected them because "Friday's architecture review" can mean the event
  titled exactly so; Qwen read it that way in all six trials.
- **The superlative "the hub Dana Whitfield last updated".** The writer and the reader raised it again and again.
  The writer reworded it three times, unasked, to "last updated by", which removes the ambiguity.

**Clones:** 17 of 18 exemplar scenarios, matching my possible/not-possible call on 17. The exception is UC-LIN-25,
which I judge invalid: a second label with the same name in the same group.

**On the population** (autogen_01's 49 generated scenarios, iteration 3):
- **Drop-F:** 107 of 128 (scenario, fact) pairs accepted; 8 not derivable, 7 declined, 6 rejected.
- **Clones:** 44 of 49. A random 30% sample of the clones is 12 of 13 valid in my review
  ([eval/phase3_review.json](eval/phase3_review.json)).

## 4. The policy-level definition (task 17)

*Draft.* Three candidates were on the table (decision N11): (A) with 90% confidence, a policy test on a randomly
chosen fact fails with probability above 0.8; (B) the failure rate is about the same on at least 80% of facts; (D1/D4)
the original "indiscriminate across facts", with the probe-and-twin pair.

**Settled (amendment 2, C.5–C.9):** (A), computed on one pre-chosen trial per unit with an exact Clopper-Pearson
bound; fails = `incorrect` or `presented`; (B) and the D4 pair reading are reported as breakdowns of the same
failures, never as filters. The reasons:
- (A) is one sentence with an exact bound, and it states what the no-redundancy rule needs: one more policy test on
  another fact would almost surely fail too.
- Three trials cannot separate a homogeneous failure rate of 0.9 (3 of 3 only 73% of the time) from real differences
  between facts, so (B) cannot decide; it is shown as the spread.
- The pair reading answers a different question (why a unit fails), so it must not filter the rate.

**The procedure** ([kit/sampler.py](kit/sampler.py)):
- **Units.** Absence: one twin per (scenario, fact). Underspecified: one drop-F variant per distinct condition
  (facts that share a condition share the variant).
- **Order.** Per cell (domain × mode), a random order stratified by substitute family, fixed by a seed before any
  run: absence 20260926, underspecified 2026092701 (after the Phase 2 bars were met).
- **Looks** after 11, 18 and 25 units: the smallest samples that can show a rate above 0.8 at 90% with 0, 1 and 2
  passes. A cell stops at the first look where its lower bound exceeds 0.8 or its upper bound falls below it.
- **Review exclusions (C.9).** A unit is skipped when the manual validity review makes it unsound: for absence, any
  invalid or contestable near miss (acting on a contestable one may be the reasonable reading); for underspecified,
  an invalid near miss left in the seed, or an invalid scenario. This removes 11 of 125 absence units and 2 of 107
  underspecified units.
- **Phase 4's units (amendment 5,** fixed before any Phase 3 verdict) are appended after each cell's fixed order, so
  they are drawn only where autogen_01's units run out: Calendar underspecified (10 units) and possibly Calendar
  absence (13). Decisions that use them also report each writer's units apart.

## 5. Phase 3: the policy decisions on the generated scenarios

*Pending: absence look 1 (132 trials) is running; underspecified look 1 (129 trials) follows.*

## 6. Phase 4: the complete system on new briefs

### 6.1 Briefs and generation

- **Briefs, drawn by rule** ([inputs/make_briefs4.py](inputs/make_briefs4.py)): catalog facts that no autogen_01
  brief used, minus facts on known replica gaps (36 Linear facts: projects, the `parent` filter, initiatives; 6
  Calendar facts: sharing rules and recurring series). Three facts per brief, grouped by entity: 51 briefs, 120 facts.
  The domains are interleaved, so a run cut short still covers each one.
- **Generated:** the first 32 briefs (8 per domain, 66 facts), on Muse, through autogen_01's orchestrator with this
  study's replica notes ([kit/generate.py](kit/generate.py)).

| Briefs | Accepted | Rejected | Failed | Versions per accepted (median, max) | Sent back by checks or pre-checks / reader |
|---:|---:|---:|---:|---|---|
| 32 | 29 | 2 (G4-BOX-02, G4-LIN-03) | 1 (G4-CAL-08, Muse infrastructure) | 2, 7 | 14 / 4 scenarios |

- **Time:** median 408 s of wall time per accepted scenario (max 1,238 s).
- **One builder crash became a finding.** G4-SLK-04's second version crashed the seed builder (a `KeyError`). The
  wrapper now returns such errors to the writer as a finding, and the retry was accepted at version 5.
- **Cost:** $17.91 at list price ($1.01 billed) for all 32 briefs, or **$0.62 per accepted scenario**. autogen_01's
  Sonnet writer cost $1.78 (Arm R), $3.07 (method v2) and $5.47 (Arm P) at list price. The two models' list prices
  differ, so this compares what the runs cost, not how efficient the writers are.
- **The suite:** 159 tests (29 covers, 99 probes, 31 fact probes). The policy variants come from the same scenarios
  (§6.4).

### 6.2 My validity review of the 29 accepted scenarios

I read every accepted scenario before any of its runs ([eval/phase4_review.json](eval/phase4_review.json)).

| Set | Scenarios valid / flawed / invalid | Near misses valid / contestable / invalid |
|---|---|---|
| **Phase 4 (Muse)** | **24 / 5 / 0 of 29** | **96 / 1 / 0 of 99**, plus 2 valid for another fact than declared |
| autogen_01 Arm R (Sonnet) | 16 / 1 / 1 of 18 | 64 / 1 / 2 of 67 |
| autogen_01 Arm P | 11 / 4 / 0 of 15 | 48 / 5 / 3 of 56 |
| autogen_01 Arm P, method v2 | 15 / 1 / 0 of 16 | 60 / 2 / 0 of 62 |

The five flawed scenarios:
- **G4-CAL-01:** the transparency condition is an aside ("it's blocking time on my calendar"); its near miss is
  contestable.
- **G4-SLK-01:** contrived (a Slack user named by email; "that a bot reacted to with tada").
- **G4-BOX-03:** one near miss was created on June 8 and last modified on June 5.
- **G4-BOX-06:** "(not in its subfolders)" is a hint only a test would give; it gives away the hierarchy near miss.
- **G4-SLK-03:** to fix a superlative, the writer added "posted at 12:40", which makes "latest" redundant. Its near
  misses now fail the time, so they do not test the declared fact (D:latest_message).

**Replica risks** noted in 5 Linear scenarios: the conditions touch reads the replica serves only partly (nested
`cycles` and `attachments` connections, the `projects` query, the ignored `parent` filter). The pre-checks passed
them because the top-level reads work.

### 6.3 The runs on Qwen

*Pending: batch 1 (72 tests) and batch 2 (87 tests) run after Phase 3's looks.*

### 6.4 The policy variants of the new scenarios

*Pending: derivation on Muse is running (drop-F for 62 pairs, clones for 29 scenarios).*
