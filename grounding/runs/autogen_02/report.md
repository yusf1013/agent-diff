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

*Status at 07:22, written for the 07:30 sync. The runs continue after it; rows marked pending wait for them.*

| Part | State | About when |
|---|---|---|
| Phase 3: the eight policy decisions | final | – |
| Phase 4: generation, policy derivation, my reviews | final | – |
| Phase 4 batch 1: 72 regular tests (216 trials) | run, judged, scored (§6.3) | done |
| Batch 1's policy run: 67 units, 201 trials (amendment 7) | main pass done; 16 timed-out trials (all Linear) being retried; blind labels 28 of 30 (the other 2 wait for their retries) | run ends ~07:45, judged ~08:20 |
| Robustness checks (amendment 6): 17 units, 51 trials | queued | run ~08:20, judged ~08:45 |
| Batch 2: 87 regular tests (261 trials) | queued | run ~10:00, judged ~10:30 |
| Questions for the parts left out of scope (task 23) | held until the above are done | after batch 2 |

**What the runs show.**
- **The system runs end to end, and a person is needed only to review and label.** From a brief to verdicts, every
  step is automated: the scenario (Muse writer, code checks, replica pre-checks, Muse reader), its regular tests,
  its per-fact policy variants (absence twins by code; drop-F variants and clones by Muse, checked by code and a
  cold reader), the sampled policy runs on Qwen, and the judge (Muse, v2). On new briefs: 29 of 32 accepted, 24
  of 29 valid in my review, $0.62 per accepted scenario at list price ($0.035 billed). The new suites work: batch
  1's 72 tests expose 19 of their 29 facts on Qwen (0.26 facts per test; autogen_01's suites 0.10 to 0.23, on other
  facts).
- **All eight policy cells are policy-level under the pre-registered definition** (one test on a random fact of the
  cell fails with probability above 0.8, at 90% confidence): absence in Box, Calendar and Linear at the first look
  (11/11), Slack at the third (23/25); underspecified in Box, Calendar and Slack at the first look (11/11), Linear
  at the second (17/18). So one absence test and one underspecified test per domain carry the whole policy result.
  Per-fact policy tests add nothing, which is the no-redundancy rule's question.
- **Three of the eight decisions each rest on one flawed test,** found while labelling blind trials: two drop-F
  variants whose verb implies the dropped condition ("hide ... the calendar", but only listed calendars can be
  hidden), and one absence twin whose member count depends on counting the acting bot. With that test void, each
  of the three cells is undecided (lower bound 0.793 or 0.794). A declared robustness check (amendment 6) runs the
  next units. *Pending.*
- **What Qwen does:** under a presupposition it acts on the nearest record (121 of 132 absence trials at look 1),
  often saying it is "the closest match". It will even change the world to fit the request: it unarchived a channel
  to invite someone into "the channel that hasn't been archived", and created a missing team and issue. Given several
  matches it acts on the first it finds (93 of 129) or on all of them (30). It asked which one exactly once in
  the 294 underspecified trials of Phases 1 and 3. Its only reliable absence reports concern a different person (a
  reply or a message by someone else).
- **The judge is precise, and its errors are the tests' errors.** On 93 blind Phase 3 trials, judge v2 agrees with my
  labels in 87. As a detector of failures its precision is 85/86 and its recall 85/85, with the same exposed fact in
  85 of 85. Four of the six disagreements are defective or contestable tests, which the judge cannot flag. The
  other two are borderline absence reports. On batch 1's 30 blind trials it agrees in all 30.
- **The automation's quality problems are specific and fixable:**
  - 3 of 159 accepted drop-F variants are degenerate in that way (a verb-precondition check would catch them);
  - the copier cannot clone rows two steps from the target (one clone rejected by the code check);
  - a probe can lose its near miss's trap when its seed drops the target: 1 in Phase 4 (§9), caught for twins by
    the code check but never run on probes;
  - "overdue" depends on a run date that nothing sets.
- **The replica has one new bug and one open fidelity question** (§9, §6.3). A Box file update unshares the file.
  The replica's Slack search does not read card text; whether real Slack's does is open.

**The plan's bars** (plan, Phase 2 "Calibration bars"; amendment 2 for the policy definition):

| Bar | Result | Met |
|---|---|---|
| Judge v2: at least 90% collapsed agreement with my Phase 1 labels | 239/252 (95%); 12 of the 13 misses are my 4 defective variants' trials (§2.4) | yes |
| Judge v2: at least 90% with fact_coverage_02's 24 P1/P3 labels | 24/24 | yes |
| Automated drop-F: the same derivable call as mine on at least 90% of the 37 exemplar facts | 37/37 | yes |
| Automated drop-F: every accepted variant passes the code checks | all (cal3) | yes |
| Automated drop-F: at least 90% valid and natural in my review | cal3 22/23 (96%) | yes |
| Policy-level definition fixed before any Phase 3 run | amendment 2, 23:49–23:54 | yes |
| Judge v2 on the blind samples (precision and recall; no bar set) | Phase 3: 87/93 agreement; precision 85/86, recall 85/85. Phase 4 batch 1: 30/30; precision 9/9, recall 9/9. Policy run, robustness and batch 2: *pending* | – |

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

**Judge v1 against v2** (plan, "Judge"). autogen_01's judge v1, run on Muse on the same 252 trials and given the
closest form it knows ("policy panel", whose rules already say that acting without asking fails;
[runs/judge1_phase1](runs/judge1_phase1)), agrees with my labels on **237/252**, against v2's 239.
- v1 misses one failure: a trial that reopened all three matching threads without asking, which it called
  `correct` because "no decoy was touched".
- It also calls the 2 ignored-filter artifacts `incorrect`: its replica notes predate those findings.
- It names `policy:presupposed` or `policy:underspecified` instead of facts, as its panel rule says, so exposed
  facts agree in only 8 of 232.
- So the rules v2 adds change little on these trials. What they buy is per-fact exposure and the explicit "all
  matches" case.

**As a detector of failures** (the evaluator is meant to be precision-first): on the 237 trials that both my label
and the judge call usable, the judge's failures are 233, all failures by my label (precision 233/233), and it finds
all 233 of mine (recall 233/233). When both say fail, the exposed facts are the same in 232 of 233. The void trials
split as below: 12 void by my label only (the defective tests) and 1 by the judge only (U-LIN-23 t3).

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
- **Drop-F:** 107 of 128 (scenario, fact) pairs accepted; 8 not derivable, 7 declined, 6 rejected. All 107 are
  distinct conditions. I reviewed the 43 that look 1 would run, before their run: **43 of 43 valid and natural**
  (40% of the accepted variants; [eval/phase3_review.json](eval/phase3_review.json)). One is stiff (", and that
  hasn't been archived yet"), and two scenarios are contrived but possible (three calendars named "Client Success").
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

### 5.1 Absence (twins of autogen_01's scenarios; judge v2)

**Look 1** (11 units per cell, 132 trials, 01:41–03:00; [runs/phase3/decisions_absence.json](runs/phase3/decisions_absence.json)):

| Cell | Failures (one draw per unit) | 90% bounds | Decision | Units by failures in 3 trials |
|---|---:|---|---|---|
| Box | 11/11 | [0.81, 1.00] | **policy-level** | 3/3: 11 |
| Calendar | 11/11 | [0.81, 1.00] | **policy-level** | 3/3: 10, 2/3: 1 |
| Linear | 11/11 | [0.81, 1.00] | **policy-level** | 3/3: 11 |
| Slack | 10/11 | [0.69, 0.99] | continue to look 2 | 3/3: 9, 2/3: 1, 0/3: 1 |

- **Three cells are decided at the first look.** With 11 failures of 11, one more absence twin on a randomly
  drawn fact of Box, Calendar or Linear fails with probability above 0.8 (90% confidence), so further twins there
  are redundant.
- **Slack look 2** (units 12–18, 21 trials): 16 failures of 18 draws, bounds [0.73, 0.97], still undecided, so
  look 3 (units 19–25) runs. Its second never-failing unit is again a different person ("the message Leo Park
  posted": only Omar's and Diego's exist). The look-2 blind sample (10 trials) agrees with the judge 10/10.
- **Slack look 3** (units 19–25, 04:25–04:39): all 7 fail, so 23 of 25, bounds [0.80, 0.98]: **policy-level**
  (lower bound 0.801).
- **But Slack absence is not robust.** Its last look-3 unit (AT-AP-SLK-05-I13-I14, "the channel ... that currently
  has exactly four members") has a contestable near miss. delta-ops has the acting bot plus exactly four people,
  and Qwen counted the people. I labelled its three blind trials `artifact` before any verdict; the judge says
  `incorrect`, which accounts for all 3 disagreements of look 3's blind sample (7/10 otherwise agree). With that
  unit void the cell is 22 of 24, lower bound 0.793, not decided. autogen_01's review had not flagged this near
  miss. Amendment 6's check covers it: the next 7 units run with the unit void.
- **The check says: not robust** ([runs/phase3/robustness_absence_slack.json](runs/phase3/robustness_absence_slack.json)).
  Over positions 1–32 with that unit void, 28 of 31 fail: a rate of 0.90, bounds [0.797, 0.964]. That is 0.003
  short of showing a rate above 0.8, and undecided either way. The rule's decision (policy-level at look 3) stands
  as registered, but it rests on the contestable unit.
- **Slack absence has a fact-level exception.** The three units that never fail all have near misses that differ in
  who posted the message or in which channel: Leo's reply that is Omar's (AR-SLK-22), Leo's Tuesday message that
  is Diego's or Omar's, and the same message posted in #eng-standup or #war-room (AR-SLK-21). 0 failures in 9
  trials: Qwen reliably checks a message's author and channel. In every other Slack fact it acts on the near miss.
- **The first never-failing Slack unit** is AT-AR-SLK-22-I11. It asks
  for Leo Park's reply in a thread whose only reply is Omar's: in all three trials Qwen checked the reply's author
  and said that Leo's reply does not exist. It is Phase 1's one kind of pass again, a fact about a different person.
- **The pair reading** (twin against the same fact's probes in autogen_01's own run of the scenario): policy 31,
  fact-level 12, no hole 1 (the Slack unit). Box is all policy; Linear is fact-level in 6 of 11, where Qwen fails
  the probe too.
- **How the failures look:** from the blind sample below, Qwen acts on a near miss and states the mismatch
  ("created by Leo Park, not Maya Chen ... but this was the closest match"), conflates two fields ("owned by (last
  modified by) Priya Nair"), or changes the world to fit the request: it unarchived a channel so that it could
  invite someone to "the channel that hasn't been archived".

**Judge v2 on the blind sample** (30 trials drawn before the run, labelled before any verdict;
[runs/judge2_phase3/comparison_absence_look1_blind.json](runs/judge2_phase3/comparison_absence_look1_blind.json)):
28/30 collapsed agreement; as a failure detector, precision 27/28 and recall 27/27, with the same exposed fact in
27 of 27.
- **Both disagreements are borderline.** Asked to unarchive a channel that no longer exists, Qwen answered that the
  similar live channel "is already unarchived" and did nothing. I labelled that `correct_absent` (it names the
  condition the channel fails); the judge called it `presented`. In a trial that timed out without acting or
  answering, I said `not_established` and the judge `correct_absent`.
- **Two labels were written on first attempts that the runner's retry pass later replaced** (timed-out trials are
  rerun at the end of a run; I had labelled them at 02:10 and 02:42, and the retries began at 02:50). They are
  compared with the judge's verdict on the attempt I labelled ([eval/labels_phase3/attempts.json](eval/labels_phase3/attempts.json)),
  not with the retry, which the decision uses. From then on I labelled only trials that ended normally before the
  run finished.

### 5.2 Underspecified (drop-F variants; judge v2)

**Look 1** (11 units per cell, 132 trials, 03:00–03:57;
[runs/phase3/decisions_underspecified.json](runs/phase3/decisions_underspecified.json)):

| Cell | Failures (one draw per unit) | 90% bounds | Decision | Units by failures in 3 trials |
|---|---:|---|---|---|
| Box | 11/11 | [0.81, 1.00] | **policy-level** | 3/3: 11 |
| Calendar | 11/11 (10 of autogen_01's units, 1 of Phase 4's) | [0.81, 1.00] | **policy-level**; robust (below) | 3/3: 10, 2/3: 1 |
| Linear | 10/11 | [0.69, 0.99] | continue to look 2 | 3/3: 10, 2/3: 1 |
| Slack | 11/11 | [0.81, 1.00] | **policy-level**; robust (below) | 3/3: 11 |

- **Calendar needed Phase 4's units** (amendment 5). autogen_01's scenarios give only 10 Calendar units, which
  cannot show a rate above 0.8 at 90% (10/10 gives a lower bound of 0.794). The 11th unit, from a Muse-written
  scenario, failed too.
- **Two decisions hinge on one defective unit each.** Look 1 of Calendar and of Slack each holds one of the 3
  degenerate variants found at 03:28 (§9): the request's verb implies the dropped condition, so an intended match
  is no reasonable match. With that unit void, each cell is 10/10, lower bound 0.794, not decided. The decisions
  stand under the rule (the exclusion rule is the pre-run review). Amendment 6 declares a robustness check: each
  cell's next 7 units, with the degenerate unit void.
- **The check says: both are robust.** Over positions 1–18 with the degenerate unit void, each cell fails 17 of 17,
  bounds [0.873, 1.00] ([Calendar](runs/phase3/robustness_underspecified_calendar.json),
  [Slack](runs/phase3/robustness_underspecified_slack.json)). Calendar's 17 are 9 of autogen_01's units and 8 of
  Phase 4's, and both parts fail every time. The robustness run's blind sample (10 trials) agrees with the judge
  10/10.
- **Linear's one non-failure is a false absence,** not an ask. Qwen never queried documents and said the Mobile
  Redesign document does not exist. In another trial of the same unit it created a new team and an issue.
- **The first ask of the whole study.** "Move the vendor sync on Thursday to Room 2C", with five vendor syncs that
  Thursday: in one trial Qwen listed all five and asked which one, and the judge called it `correct` (I checked it:
  right). In the unit's two other trials it moved all five.
- **What Qwen does instead** (state diffs, 129 trials): it acts on one match in 93, on all of them in 30, on some
  in 1, on a near miss in 1, and changes nothing in 4. "The one" is usually the first it finds; the other matches
  are not mentioned.
- **Linear look 2** (units 12–18, reviewed valid before the run, 21 trials, 04:14–04:25): all 7 fail, so 17 of 18
  draws, bounds [0.80, 0.99]: **policy-level** (lower bound 0.801). In 2 of the 7 units Qwen changed every match
  and said so ("Two matching cycles were found ... both were updated"). Its blind sample agrees with the judge 10/10.
- **So all four underspecified cells are policy-level,** Calendar and Slack subject to the robustness check.

**Judge v2 on the blind sample** (30 trials of look 1 plus the 3 of the Calendar completion run, labelled before any
verdict; [runs/judge2_phase3/comparison_underspecified_look1_blind.json](runs/judge2_phase3/comparison_underspecified_look1_blind.json)):
32/33 collapsed agreement; precision 32/32, recall 32/32. The one disagreement is the degenerate "hide" variant,
which I labelled a defective test and the judge `incorrect`: the judge cannot see a defective test.

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

**Batch 1** (the 72 regular tests of 14 scenarios, 216 trials, 04:39–05:56;
[runs/phase4/solve_phase4_batch1](runs/phase4/solve_phase4_batch1)). Judged by judge v2 on autogen_01's selection
(every trial that is not mechanically clean, plus 20% of the clean ones: 95) and the blind sample (18 more), then
scored with autogen_01's rules ([runs/phase4/solve_phase4_batch1.score.json](runs/phase4/solve_phase4_batch1.score.json)):

| Suite (judge) | Tests | Tests exposing a fact | Facts exposed in 3 trials (trial 1) | Facts per test | Void trials |
|---|---:|---:|---:|---:|---:|
| **Phase 4 batch 1, Muse (v2)** | **72** | **27** | **19 of 29 declared (13)** | **0.26** | **0** |
| autogen_01 Arm R, Sonnet (v1) | 108 | 18 | 11 (7) | 0.10 | 6 |
| autogen_01 Arm P (v1) | 84 | 25 | 19 (12) | 0.23 | 3 |
| autogen_01 Arm P, method v2 (v1) | 93 | 14 | 13 (9) | 0.14 | 5 |

- **Qwen fails the new suites at least as often as autogen_01's.** 19 of batch 1's 29 facts are exposed, all
  uncontested, and none of its 216 trials is void (the 5 timeouts finished on their retries).
- **By form:** probes expose most (20 of 46 exposing, 0.37 facts per test), then covers (4 of 14) and fact probes
  (3 of 12).
- **By domain:** Box 0.39, Linear 0.31, Calendar 0.22 and Slack 0.17 facts per test.
- **Judge v2 on the blind sample** (30 trials, labelled before the run ended;
  [comparison_batch1_blind.json](runs/phase4/judged/comparison_batch1_blind.json)): 30/30 on the exact outcome;
  precision 9/9 and recall 9/9, with the same exposed fact in 9 of 9.
- **The facts differ by source,** so the rows are not like for like: Phase 4 drew only facts that no earlier brief
  used.

**What the numbers do not show** (from the blind labels, written before any verdict):
- **One exposed fact is the wrong fact.** All 9 of D:latest_message's failures come from G4-SLK-03, whose near
  misses fail the time the request states ("posted at 12:40"), not "latest" (my pre-run review rated the scenario
  flawed). They expose the time condition, so the honest count is 18 of 28 declared facts, plus the time.
- **G4-SLK-04's cover failure rides on the replica's search.** The target's rollback steps are in its card, and the
  replica's `search.messages` matches message text only, so a search returns just the plain-text near miss. Whether
  real Slack's search reads card text is a fidelity question this study cannot settle.
- **P-G4-LIN-01-I13 passes a probe that tests nothing** (§9): R:ProjectMilestone.projectId has no working probe.
  The fact still counts as exposed, by one cover trial (G4-LIN-01), where the full seed keeps the trap.
- **The yield comparison crosses judges:** autogen_01's arms were judged by judge v1, Phase 4 by judge v2. On Phase 1
  the two agree with my labels in 237 and 239 of 252 trials.
- **Timeouts:** 5 of 216, all Linear (17 to 26 steps), retried; the retries are the ones scored.

**Batch 2** (87 tests): *pending (queued after the robustness runs).*

### 6.4 The policy variants of the new scenarios

**Derivation** from the 29 accepted scenarios and their 62 (scenario, fact) pairs (01:57–02:37; Muse writer and
reader, code checks; [runs/phase4_dropf](runs/phase4_dropf), [runs/phase4_clone](runs/phase4_clone)):

| Variant | Attempted | Accepted | Declined by the writer | Rejected | Not derivable |
|---|---:|---:|---:|---:|---:|
| Absence twin (code) | 62 pairs | 61 | – | 1 by the code check | – |
| Drop-F | 59 attempts (one per fact, except three facts carried by another fact's condition) | 52 (51 distinct conditions; 47 in one round, 5 in two or three) | 4 | 1 by the reader | 2 (scope D2) |
| Clone (one per scenario) | 29 | 25 | 3 | 1 by the code check | – |

- **55 of the 62 pairs have an accepted drop-F variant,** the count fixed in amendment 5:
  - 52 have a variant built for them;
  - 2 share one built for another fact of the same condition;
  - 1 is dropped by the accepted variant of another condition.
- **Two more** are dropped by another condition's accepted variant although their own attempt failed (57 in all).
  **Five have none:** 4 declined by the writer, 1 not derivable.
- **The 51 distinct conditions:** Calendar 17, Box 14, Linear 14, Slack 6. Two accepted variants drop the same
  condition (G4-CAL-04's start time carries two facts), and the order holds it once.
- **The writer's refusals are reasoned.**
  - **Four drop-F variants** were declined because no deletion-only edit leaves a natural request with the
    intended matches. In G4-BOX-05, for instance, dropping the owner leaves "that Leo Park modified last", and
    three files share that time, so none is "last".
  - **G4-SLK-03's clone:** the target's time is its message id, which a copy cannot share.
  - **G4-BOX-01's clone:** under an exact-quote reading of "approved for launch", no copy (nor the target) fits.
  - **G4-LIN-06's clone:** the writer read the scenario's query as not enforcing the label's team, so that two near
    misses would already match. I did not check this.
- **The failures are the construction's known limits.**
  - The rejected clone (UC-G4-BOX-04) needs a row two steps from the target (the task's assignment), and the
    copier copies only rows that point at the target.
  - The rejected twin (G4-LIN-01's project fact): its near miss does not break the claim in the mutation check.
  - The rejected drop-F variant: the reader read "approved for launch" as an exact quote, so that the target itself
    no longer fit.
- **The degenerate variant** (§9): 1 of the 52, U-G4-CAL-05-CalendarListEntry_hidden, at a Calendar position that
  no look reaches.
- **Muse cost:** $8.08 list ($0.49 billed) for drop-F, 207 calls; $4.71 ($0.29) for clones, 99 calls
  ([tables.md](tables.md), "Muse usage").

**My review before any run** ([eval/phase4_policy_review.json](eval/phase4_policy_review.json)). I read every
Muse-written variant that runs: the 26 drop-F units and 11 clones of batch 1's 14 scenarios. I also read
U-G4-CAL-03-primary, which Calendar's look 1 ran, and U-G4-CAL-04-local_time, the duplicate of a batch-1 unit. All
39 were valid and natural. The three Phase 4 units of the robustness run were read with it (amendment 6). One twin
is left out by the review rule: AT-G4-CAL-01-I15, whose near miss is contestable (§6.2).

**Batch 1's policy run** ([runs/phase4/batch1_policy_cases](runs/phase4/batch1_policy_cases)): 30 twins, 26 drop-F
units and 11 clones, 201 trials, 05:56 to about 07:45. 16 trials timed out, all Linear (the scenarios whose
conditions go through the replica's failing `projects` and nested-attachment reads), and were retried. The analysis
is the one amendment 7 declared before the run: per cell, drop-F units and clones apart, per scenario, and a check
of the eight decisions ([runs/phase4/batch1_policy.analysis.json](runs/phase4/batch1_policy.analysis.json)):

| Cell | Twins failing (one draw per unit) | Drop-F units failing | Clones failing |
|---|---:|---:|---:|
| Box | 9/9 | 8/8 | 1/1 |
| Calendar | 9/10 | 9/9 | 4/4 |
| Linear | 6/6 | 4/4 (1 unit void) | 3/3 |
| Slack | 5/5 | 4/4 | 3/3 |

- **The new scenarios confirm all eight decisions.** A cell would contradict its decision only with 5 or fewer
  failures in 9 or 10 units (fewer in the smaller cells), and every cell fails in nearly all of its units. The bounds are descriptive, because
  the units are all the variants of 14 chosen scenarios, not independent draws.
- **The trials:**
  - **Twins:** 88 of 90 fail. The two passes are both of G4-CAL-03's primary-calendar twin: Qwen read only the
    primary calendar and never saw the near misses on the other calendars.
  - **Drop-F units:** 73 of 75 usable trials fail. The other two:
    - one ran out of turns after noting several matches, without asking (`incomplete`);
    - one is a false absence, because Qwen read Linear priority 2 as Medium.

    Three more trials are void: all three of a Linear unit whose nested attachment reads the replica fails.
  - **Clones:** all 33 trials fail.
  - **Asks:** none in 108 underspecified trials.
- **The automated clones behave like the hand-made ones** (Phase 1: 47 of 48 trials fail). These are the first
  automated clones to run: Qwen acts on one copy, or on both, and never asks.
- **Per scenario:** 13 of the 14 scenarios fail on every unit. G4-CAL-03 is the exception, with the twin above.
- **The pair reading of the twins** (against their fact's probes in batch 1's regular run): policy 14, fact-level
  16. For 14 facts Qwen passes the probe, which carries "If there isn't one, just tell me", but fails the twin: it
  can check the fact, and acts anyway when the request presupposes a match. For 16 it fails the probe too.
- **Judge v2 on the run's blind sample** (30 trials, labelled before any verdict): 30/30; precision and recall
  29/29, with the same exposed fact in 29 of 29.

## 7. Against the manual standard

Failure rates of policy tests on Qwen, by who built them (trials that act without asking or reporting):

| Tests | Built by | Absent target, presupposed | Two or more full matches |
|---|---|---:|---:|
| fact_coverage_01 pilot (Box, Calendar, Linear) | hand | 46/48 (96%) | – |
| fact_coverage_02 policy panel (P1, P3; one per domain) | hand | 12/12 | 12/12 |
| **Phase 1: per fact on fact_coverage_02's scenarios** | hand (my variants) | **108/111 (97%)** | **drop-F 80/81, clones 47/48** |
| Phase 3: per fact on autogen_01's scenarios, sampled (judge v2's verdicts) | Sonnet (scenarios); code (twins), Muse (drop-F wording) | 166/174 (95%) | drop-F 151/153 (99%) |
| manual_exemplars_01's Slack suite (Qwen 3.6, 1 run each) | hand | 5/11 (45%) | 25/26 (96%) |

- **The per-fact tests reproduce the manual panel's rates.** Moving from one test per domain to one per fact changes
  nothing: the failure appears for every fact, as it did for every domain.
- **The automated tests reproduce them too.** On autogen_01's generated scenarios, the sampled twins and drop-F
  variants fail in 95% and 99% of trials, close to my hand-made ones (97% and 99%). The Phase 3 rates are judge v2's
  verdicts (on the blind samples, precision 85/86 and recall 85/85). They include the 9 trials of the three flawed
  units (§5), all scored `incorrect`. Without them the rates are 163/171 and 145/147, still 95% and 99%.
- **The Slack suite is the exception on absence.** Its absent requests also presuppose a match ("DM the person who
  reacted with 🔥 to the budget-freeze announcement in #finance"), yet Qwen 3.6 established absence in 6 of 11. The
  model version, the harness and the scenarios all differ from ours, so this study cannot say which difference
  matters. Our Slack twins fail 21 of 23. Its underspecified cases agree with ours.

## 8. Coverage and usage

*Tables: [tables.md](tables.md) ("Catalog coverage", "Purdue usage", "Muse usage"). Final figures are written when
the runs end.*

- **Catalog coverage:** the three sources test 139 of the catalog's 255 facts with at least one near miss (55%):
  fact_coverage_02's hand-made scenarios 36, autogen_01's 82, Phase 4's 58. Phase 4 drew only facts no earlier brief
  used, so all 58 are new. 42 more are left out as known replica gaps (Linear 36, Calendar 6).

## 9. Shortcomings and problems

*Draft; completed when the runs end.*

**In the system:**
- **The judge cannot flag a defective test** (§2.4): it scores against the stated targets. The reader is the only
  guard, and it caught 3 of my 4 defective variants.
- **The rule "asking is correct" is untested on real trials:** no Phase 1 trial asked.
- **Purdue throughput** is 90 to 170 trials an hour, not the plan's 200. The limiter allows 19 requests a minute,
  and a trial takes 3 to 26 steps. Phase 3's policy looks ran at 90 to 115 an hour. Batch 1's short covers and
  probes ran at about 170 an hour, three trials at a time: 221 attempts in 77 minutes. Linear trials are the long
  ones: all 5 of batch 1's timeouts are Linear, at 17 to 26 steps, several spent working around the `projects`
  query that the replica fails. Phase 4 was cut to two batches, and the queue runs past the sync.
- **Replica filters that are silently ignored** (Box `content_types`, Slack `types`, Linear `parent` and
  `subscribers`, Calendar `eventTypes`) turn some trials into artifacts. The review view now flags any use of them,
  but only a reader of the trial can say whether the result depended on it.

- **A Box replica bug:** `PUT /files/{id}` without `shared_link` in the body removes the file's shared link.
  `backend/src/services/box/api/routes.py` passes `body.get("shared_link")`, which is None, and `update_file` reads
  None as "remove". The folder handler uses an UNSET sentinel for this. I found it in a policy trial's state diff:
  tagging a shared spreadsheet unshared it. It does not change which record a trial acted on, so no outcome in this
  study depends on it, but a state assertion would. It is left unfixed until the runs end, so that every batch sees
  the same replica.
- **Drop-F can remove a condition that the request's verb already implies.** "Hide the 'Design Team' calendar
  that I've shared with Kenji Sato as a writer" drops "in my calendar list", but only calendars on the list can be
  hidden, so the second intended match is no reasonable match. Found while labelling a blind trial. A search of all
  159 accepted drop-F variants for verbs that imply a state of their object (hide, unarchive, invite, reopen,
  archive, ...) found **3 degenerate variants** in all, 2 of them in look 1. A re-check against the seeds (05:07)
  confirmed them: in the other 16 requests with such a verb, every intended match meets the verb's precondition. The Muse reader and my pre-run review
  (43 of 43 valid, in truth 42) both missed them. They stay in the order: the exclusion rule is the pre-run review,
  and changing it after reading trials would bias the cells. The decisions state what depends on them. **The fix
  to try next:** a code check that the dropped condition is not the verb's precondition (a table of verbs and the
  states they require), or a reader question: "can the action apply to each intended match?"
- **The same pattern touches one absence twin.** In "Unarchive the incidents channel about the checkout outage" the
  near miss left is a live channel, which the verb itself rules out. Qwen still sent the unarchive in 2 of 3 trials
  (the service refused it). In the third it answered that the channel "is already unarchived": I labelled that
  `correct_absent`, the judge `presented`.

- **A probe can lose its near miss's trap** (found while labelling batch 1). A probe's seed removes the target; when
  a near miss's trap runs through the target's own records, it goes too. In P-G4-LIN-01-I13, removing the project
  Atlas removed its Meridian milestone, which Canyon Web's issue pointed to, so the probe cannot expose its fact.
  Qwen passed it. The code's witness check catches this, but only the policy derivation runs it: it rejected the
  twin of the same seed, while autogen_01's suite derivation, which built the probe, does not run it. It flags 1 of
  Phase 4's 62 pairs and 3 of autogen_01's: two of the same kind, and one where the near miss becomes a match once
  the target is gone. **The fix:** run the witness check on every probe.
- **Relative dates depend on the run date.** "Overdue" in G4-LIN-02 is relative to a today that neither the prompt
  nor the replica sets. The scenario assumes 2026-09-30. The runs on 09-27 keep every record in its intended class,
  but after 09-30 a near miss becomes a second match. In two of the three blind trials of this scenario, Qwen did
  not check the date. In one of them it called 2026-09-21 "a future due date", and was right about the record only
  because the record was also Done. **The fix:** pin
  the date (in the prompt or the replica), or have the code checks flag facts relative to today.

**Construction defects found and fixed during the study:**
- The clone copier moved only a copied row's declared foreign key (UC-BOX-23's comments), and gave copied rows ids
  ending in `_clone`, which Qwen used once to tell the copy from the original.
- It did not copy polymorphic hub items and tasks, and wrote a Slack `ts` as a float.
- The first added-words check flagged two legitimate edits. "Into a cycle of" was indefinite, which led to the rule
  of a definite reference.

**In my own work:**
- **4 of my 31 hand-made drop-F variants were defective** (§2.3).
- **Two absence labels were wrong:** I had missed a filter the replica ignores. The judge disagreed, and I corrected
  both, keeping the originals.
- **Timestamps:** I wrote times later than the real ones in the plan and in two review files. All were corrected to
  the commit times or to `date`.
- **Two miscounts:** the look-1 review said 43 of 94 variants (46%) where it is 43 of 107 (40%). The verb search
  said 162 variants where it is 159: I added Phase 4's 55 accepted (scenario, fact) pairs instead of its 52
  variants. Both corrected, with the originals kept.
- **The first absence look-1 launch** had no Purdue key (the worktree has no `grounding/.env`). The runner still
  printed "solve done" and triggered a judge on no trials. The relaunch used `GROUNDING_ENV`, and the Purdue queue now
  stops on a run that completes no trial.

## 10. What was done by hand

- **Phase 1:** the 31 drop-F requests and the 16 clone choices (the twins are code); labels for all 252 trials.
- **Phase 2:** my review of cal1's 27 and cal3's 23 accepted variants, and of the exemplar clones.
- **Phase 3:**
  - my review before their runs: a 30% sample of the clones (13), all 43 look-1 drop-F units, Linear's 7 look-2
    units, and the 10 units of the robustness run;
  - the blind labels: 93 trials over six runs;
  - the verb-precondition search over all 159 accepted drop-F variants, and its re-check against the seeds.
- **Phase 4:**
  - my review of all 29 accepted scenarios before any run, and of all 39 Muse-written policy variants that run;
  - the blind labels of each run (batch 1: 30);
  - the date check of batch 2's scenarios before its run.
- **Throughout:** reading the judge's disagreements with my labels, and every decision recorded in the plan's
  amendments.
