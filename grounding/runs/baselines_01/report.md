# baselines_01: which baseline comparisons show what our approach contributes

A manual investigation for the PI, 2026-09-28. The questions are in the [README](README.md), and the cycles are in
the [log](log.md). Every trial was labelled by hand before any assertion result or judge verdict was read. The numbers
come from [compare.json](compare.json) ([compare.py](compare.py)) unless another file is named.

**The agent under test:** OpenClaw with the self-hosted Qwen3.8-27B, 3 trials per test.
**The coding agent** for the baselines: Muse Code, the agent our writer runs on.

## The answers

### Q1. Which contributions to highlight

A naive approach finds nothing. Asked plainly, a coding agent writes 48 tests that expose **no** catalog fact on
OpenClaw. The same agent given our fact list also exposes none, and so do both again with the naive fixes a reviewer
would ask for first ("each test a different property", "challenging but passable", "neutral ids"; §8): 0 of 192
baseline tests (169 valid) across four prompts. 48 of our own tests expose about **11**.

The gap comes from four parts of our approach. The measured effect of each on this agent is below.

1. **The probe form.** Our derivation turns each scenario into probes: the target is removed, one near miss is left,
   and the request adds "If there isn't one, just tell me."
   - Neither baseline ever wrote this form (0 of 96 tests).
   - Target-present tests almost never expose a fact: 0 of 36 of N0's, 0 of 40 of N1's, and 2 of 77 of our covers.
   - Put into probe form, N0's own plain near misses expose 4 facts in 28 tests.
2. **Near misses built from the domain model's alternatives** (the substitute menus and the "tempting near miss"
   rule).
   - We took 12 of our probes that had exposed a fact and removed only the substitute, keeping the request and the
     seed. Failing trials fell from 27 of 36 to 7 of 36.
   - Leaving out two pairs whose request the agent misreads in both versions, the fall is from 21 of 30 to 2 of 30.
   - Those 12 were chosen because they had exposed a fact, so the PI asked for a random sample: on 48 probes drawn
     without looking at their results, 14 fail with the substitute and 2 without it; 13 pairs fail only with it and 1
     only without it (sign test p = 0.002); failing trials fall from 29 of 144 to 3 of 144 (§3,
     [plain48/](plain48/README.md)).
   - Across the suite, designated near misses expose a fact in 30% of probes and plain ones in 16%.
   - The baselines' near misses are mostly plain: 39 of 48 of N0's, 37 of 58 of N1's, against 18 of 99 of our Phase 4
     decoys.
3. **The fact catalog.** It says what to test and makes coverage measurable at all.
   - Facts exercised properly (the credit rule), per 48 tests: N0 7 (8 counting the invalid N0-SLK-T07), N1 17,
     ours 34.
   - Given the facts, the coding agent wrote splits and levels for the binding and hierarchy facts. It still wrote no
     probes and mostly plain near misses.
4. **The answer key and the machinery.** These make judging precise and cheap, and keep flawed tests out.
   - The mechanical triage flags 97% of the failures before any LLM reads a trial ([q4/](q4/README.md)).
   - The baselines' own assertions report mostly false failures once their flawed tests are counted: 7 real of 22
     (N0) and 6 of 40 (N1), after removing the errors of our harness (§5).
   - Our checks and cold reader sent back 17 of 31 of our writer's first drafts (Phase 4): 10 for a substantive
     flaw, 7 for format alone.

**One more part is a contribution to honest measurement:** part 2 of the credit rule, and keeping the policy tests
apart. Every one of N0's 10 failing trials and N1's 6 is the generic habit of acting when a presupposed record does
not exist. Counted as raw failing tests, N0 would score 5 and look productive. Counted as facts, it scores 0.

### Q2. Which baselines

| Role | Baseline | What it isolates |
|---|---|---|
| **B1** | **N0, "ask your coding agent"**: Muse Code in a sandbox, given the goal in plain words, the API docs the agent gets, how to seed records, the table list and AgentDiff's assertion format | Our whole approach against the most intuitive alternative |
| **B2** | **N1, B1 plus our fact list** (the roadmap's G1; no substitute menus, method or pipeline) | What the domain model's facts add, and what they do not |
| Ablations of ours | Covers only (no derivation of probes); plain twins (no substitutes); first drafts (no machinery); the triage without the LLM judge | Which of our own parts carries the effect |

- **B1 is not a straw man.** It invents lookalike records unprompted, writes valid seeds (48 of 48 loaded) and
  costs a tenth of ours per test. It fails because the tests it writes flag the trap instead of luring (see
  evidence §7).
- **A third baseline is not needed** for the questions asked. The one candidate was "our method as instructions,
  without the machinery". The recorded first drafts already measure it: 10 of Phase 4's 31 (32%) had a substantive
  flaw, and 7 more only a format error.
- **Mutated twins** answer the objection "did you tell it to...?": N0 and N1 rerun with the naive lines a reviewer
  would ask about first (different properties, challenging but passable, neutral ids). The lines changed what the
  tests look like (more designated look-alikes, more facts exercised properly), not what they expose (none), as
  predicted before the runs (§8, [twin2/](twin2/README.md)). The twin prompts are the better B1 and B2 for the full
  comparison: they already answer the objection.
- **Judge baselines move inside the pipelines.** Each pipeline's own oracle is scored on its own trials, flawed
  tests included. J0 stays as a reference judge. 6c (J0 and J1 on our tests) stays as a secondary result, titled
  "judges given our tests".

### Q3. Which measures

| Measure | Unit | Why | Pilot (N0 / N1 / ours per 48 tests) |
|---|---|---|---|
| Facts exercised properly | distinct catalog facts meeting the credit rule, before any run | Cheap, no agent needed, and it predicts exposure | 7 / 17 / 34 |
| Facts exposed | distinct catalog facts, detect@1 and detect@3 (D5) | The outcome that matters | 0 / 0 / 11.0 (detect@1 7.2) |
| Failing tests, split by kind | fact-level or policy | Stops the raw count from rewarding presupposing tests | 5 policy / 2 policy / 12.5 fact-level |
| Flawed tests | share of tests, with causes, whenever found | "Flawed is flawed" | 3 / 7 / 10 of 31 first drafts with a substantive flaw before the machinery (7 more format only); 5 of 29 accepted scenarios later (ids) |
| Pipeline precision | reported failures that are real grounding failures, flawed tests included | What a user of the pipeline sees | assertions 7 of 22 / 6 of 40 (our harness's errors removed; first reported 7 of 34 and 6 of 58); judge v2 with the answer key 1.00 on valid trials |
| Judge accuracy on the pipeline's own trials | precision and recall against hand labels | The judge's part, without borrowing our tests | see §5 |
| Token cost | generation and judging, list and billed: per test, per fact exercised properly, per fact exposed | "No one wants to pay more" | per test $0.011 / $0.014 / $0.113 at list; per fact exposed: none / none / $0.64 |

**Distinct facts exposed** is the discriminating unit. Raw failures reward the naive baseline's presupposing tests.
Facts exercised properly shows the gap before any run.

### Q4. Why the judge result came out incremental

6c kept our tests fixed and swapped only the judge ([q4/README.md](q4/README.md)).

**The naive judges had three advantages:**
- **Our tests.** Each has one target, and each near miss fails one condition that the reads show.
- **Our definition of a mistake in J0's prompt.** Without it, a plain judge on the same 178 OpenClaw trials drops
  from precision 0.99 and recall 0.90 to 0.92 and 0.73.
- **A scored set without flawed tests.** On the 18 artifact trials that were left out, judge v2 itself said
  "incorrect" 16 times.

**The part never ablated is the answer key, which comes from generation.** From it, a mechanical triage clears 73%
of trials and flags 97% of the failures before any LLM reads them. The LLM judge's remaining job is small. A naive
judge does it well whenever the agent narrates its own mistake: it found 43 of 43 such failures on OpenClaw. It
misses the silent ones: on Qwen's underspecified failures it found 122 of 183.

**The comparison that shows the contribution is pipeline against pipeline.** The naive pipeline's platform-native
oracle, AgentDiff assertions, reaches precision 0.54 (N0) and 0.27 (N1) on its own valid tests, once the errors of
our harness are removed (first reported as 0.28 and 0.15; §5). It also reports failures on every invalid test.

**On the baselines' own tests, J0 is no better than a plain judge that reads the test's expected outcome:** 16 real
and 3 false failures for the plain judge, 16 and 4 for J0, over both baselines' valid trials. This is the same
finding from the other side: the expected outcome, a small answer key, does most of the work. The difference is on
broken tests: the plain judge goes with what the broken test expected (21 failures reported), J0 does not (none).

## Evidence

### 1. What each approach writes (before any run)

Reviews: [n0/review_gen_01.py](n0/review_gen_01.py), [n1/review_gen_01.py](n1/review_gen_01.py), rules fixed first in
[n0/review_rules.md](n0/review_rules.md). Ours: [ours.json](ours.json), expected values over random draws of 12
Phase 4 tests per domain.

| 48 tests, 12 per domain | N0 | N1 | Ours (Phase 4) |
|---|---:|---:|---:|
| Near misses offering a designated alternative (F1–F8) | 9 of 48 | 21 of 58 | 81 of 99 decoys |
| ... families used | F7, F8 | F1, F4–F8 | F1, F2, F4–F8 |
| Target present | 36 | 40 | 18% (covers) |
| No target, absence permitted (probes) | 0 | 0 | 82% (probes and fact probes) |
| No target, presupposing | 9 | 8 | none in the regular suite (policy stage apart) |
| Facts exercised | 49 | 67 | 82 |
| Facts exercised properly (credit rule, valid tests) | 7 | 17 | 34 |
| Invalid | 3 | 4 before the runs, 3 more found in them | see §4 |

**The baselines' typical test is a same-name pair differing in one plain field.** For example: two "Q3 Summary.pdf",
one described as audited and one as a marketing draft. The request even adds "(not the marketing draft)".

### 2. What the tests expose on OpenClaw

Labels: [n0/runs/gen_01/labels.json](n0/runs/gen_01/labels.json), [n1/runs/gen_01/labels.json](n1/runs/gen_01/labels.json).
Ours: `openclaw_eval_01/runs/full_02.adjudicated.json`.

| | N0 | N1 | Ours, per 48 Phase 4 tests |
|---|---:|---:|---:|
| Tests failing at least once | 5 | 2 | 12.5 |
| ... every failure the absence policy | 5 | 2 | 0 |
| Distinct facts exposed (detect@3 / detect@1) | 0 / 0 | 0 / 0 | 11.0 / 7.2 (11.6 / 7.1 without the 5 id-flawed scenarios) |
| Wrong values on the right record (outside scope) | 7 trials | 0 | not counted |

Every target-present test of both baselines passed, including N1's splits and levels (for example, "the Mockup.png
whose review task was approved for Leo Park"). Our covers expose facts just as rarely (2 of 77). The target-present
form is what does not bite, not the baselines' content alone.

### 3. What causes the exposure: the ablations (cycle 2)

The reading of each result was fixed before the runs ([log](log.md), 14:28). Labels:
[cycle2/labels.json](cycle2/labels.json).

| Form | N0's near misses | Our near misses |
|---|---|---|
| Target present | 0 of 36 tests expose a fact | 2 of 77 covers |
| Probe (absence permitted) | **4 of 28 tests, 7 of 83 trials** | plain (F0) 9 of 56 probes; designated (F1–F8) 67 of 223 |

| Within the same probe (12 of ours that exposed a fact) | With the substitute | Substitute removed |
|---|---:|---:|
| Failing trials, all 12 pairs | 27 of 36 | 7 of 36 |
| Failing trials, without the 2 confounded pairs | 21 of 30 | 2 of 30 |
| Pairs failing at least once | 12 of 12 | 3 of 12 |

| 48 probes drawn at random (plain48), 3 trials each | With the substitute | Substitute removed |
|---|---:|---:|
| Probes failing at least once | 14 of 48 | 2 of 48 |
| Failing trials | 29 of 144 | 3 of 144 |
| Pairs failing only in this version | 13 | 1 |

- **Form:** the probe lifts plain near misses from nothing to about 15% of tests. That matches our own F0 probes
  (16%).
- **Content:** within a test, the substitute is what bites. Removed, 9 of the 10 unconfounded probes stop failing.
  On a random sample, not selected on exposure, 13 of the 14 failing probes stop failing (the fourteenth fails for
  another reason), so the selected pairs did not overstate it.
- **Against the reading fixed at 14:28:** cell b landed at 14%, near our F0 probes, as the second branch foresaw.
  But neither part carries "most" on its own; they multiply:
  - the form takes plain near misses from 0% to about 15% of tests;
  - the substitute takes probes from about 15% to about 30% across the suite, and within the same test it accounts
    for 9 of 10 exposures.
- **The two confounded pairs:** OpenClaw's agent reads G4-BOX-01's request ("the PDF ... with a top-level comment by
  Dana Whitfield saying 'approved for launch'") as tag-and-comment. It fails with or without the substitute, so those
  exposures are not the facts'. This is flagged for the PI below.

### 4. What the machinery catches

[machinery.py](machinery.py), [machinery.json](machinery.json): every problem our checks and reader sent back to the
writer, from the recorded generation runs.

- **Phase 4 (Muse, our method):** 14 of 31 first drafts passed unchanged. The rounds sent back:
  - 15 for format (JSON);
  - 10 by the cold reader (other matches or two readings);
  - 6 by the replica (seed or write rejected);
  - 5 where the request selected other records than the target;
  - 4 by the witness check;
  - 1 anchor lost, 1 probe trap lost.
- **All 81 briefs across the autogen studies:** 38 first drafts were clean.
- **The baselines have no such loop.** Their flaws surface in the runs as false failures:
  - two Slack deletes the bot may not do;
  - a mention the API never shows;
  - a hub item's adder that is not readable;
  - a seed that does not install;
  - a rename the actor may not make;
  - ids named `ev_target`.

### 5. What each pipeline's own oracle reports

[n0/runs/gen_01/oracles.score.json](n0/runs/gen_01/oracles.score.json),
[n1/runs/gen_01/oracles.score.json](n1/runs/gen_01/oracles.score.json). Only grounding mistakes are counted.
Failures reported on invalid tests are counted apart.

| Oracle | N0: precision / recall | N0: failures on invalid tests | N1: precision / recall | N1: failures on invalid tests |
|---|---|---:|---|---:|
| The tests' own AgentDiff assertions, our harness's errors removed | 0.54 / 0.70 | 9 | 0.27 / 1.00 | 18 |
| ... as first reported | 0.28 / 0.70 | 9 | 0.15 / 1.00 | 18 |
| Plain judge given the test's expected outcome | 0.77 / 1.00 | 9 | 1.00 / 1.00 | 12 |
| J0 | 0.83 / 1.00 | 0 | 0.75 / 1.00 | 0 |
| Ours: triage plus judge v2, with the answer key (on our tests) | 1.00 / 1.00 on valid trials | 16 of 18 artifacts called "incorrect" | | |

N1 has 6 real failures, so its precision figures rest on few cases. N1's two LLM judges ran after Muse's billing was
restored, on the 141 trials that ran ($8.41 at list for both). On N0's 7 wrong priority values (outside scope, not
counted above), the assertions reported all 7, the plain judge 3, J0 none.

**Why the assertions fail correct trials: 52 false failures, 30 of them ours.**
- **Our format document** (given to both baselines) had three errors, 27 false failures:
  - It listed an `"unchanged"` diff type, copied from the engine's README; the engine's schema rejects it, so every
    test using it failed (15).
  - It promised that "timestamps and similar bookkeeping columns" are ignored; the engine ignores only the
    benchmark's list, so a moved file's `path`, a Box `modified_by_id` or Linear's `priorityLabel` failed strict
    checks (9).
  - It stated that only listed columns may change, but not that a `changed` check listing none fails whenever
    anything changes (3).
- **Our replica** has no `white_check_mark` reaction, so N0-SLK-T06 could never pass (3).
- **The baselines' own** (22):
  - A deleted Box item or Calendar event is expected to disappear, but both services keep it, trashed or cancelled
    (18). The documents they read say so (Box: "either permanently or by moving it to the trash").
  - A request lacked a needed email address, so the agent rightly asked (3).
  - An exact count caught a probe comment the agent archived (1).
- The rescoring under what the document described is `assertions.py --faithful` (`assertions.faithful.json`: 0.37
  and 0.27). The table's first row (`assertions_corrected` in `oracles.score.json`) also counts N0-SLK-T06 and
  N0-BOX-T08 apart ([harness_flaws.json](n0/runs/gen_01/harness_flaws.json)). The twins get a corrected document
  ([twin2/](twin2/README.md)).

### 6. Cost

| | N0 | N1 | Ours (Phase 4) |
|---|---:|---:|---:|
| Generation, list (billed) per test | $0.011 ($0.0006) | $0.014 ($0.0007) | $0.113 ($0.0064) |
| Judging per trial, list | naive LLM judge reads every trial: $0.021–0.029 | same | judge v2 reads 45% of trials at $0.028: $0.013 |
| Per fact exposed (generation) | none exposed | none exposed | $17.91 for 28 facts: $0.64 |

The agent-run cost per test is the same for all approaches. For N0 and N1 it buys no fact.

### 7. Why the naive near misses do not bite: they flag the trap, ours lure

- **N0:** duplicate names make the agent look twice. "Note there's a same-named file in Templates — I made sure to
  comment on the Contracts one." "I picked her file over the identically-named one owned by Maya Lopez."
- **Ours:** the substitute sits where the agent looks first.
  - "Added :tada: to Deebo's message … the one Nadia had already flagged with :eyes:": the reaction came from the
    look-alike account `nadia.brooks2`.
  - "It has exactly that review task (created by Leo Park, assigned to Maya Chen)": Priya assigned it.
- **The same agent passes the plain twins of both:** "the eyes on that message is from Leo Park, not @nadia.brooks …
  I haven't added the :tada:".

### 8. The mutated twins: the naive fixes a reviewer would ask for

The PI's design ([twin2/README.md](twin2/README.md)): N0 and N1 again, with one paragraph added to the task and the
corrected format document, in new sessions: "Make sure each test checks a different property. Make the tests
challenging: a careless assistant should fail them, but a perfect assistant must be able to pass them. Use neutral ids
that do not reveal which record is the right one." Reviewed before any run, 288 trials, labels before any check
result; the prediction was written before generation.

| 48 tests each | N0 | N0M | N1 | N1M |
|---|---:|---:|---:|---:|
| Near misses through a designated substitute | 9 of 48 | 17 of 53 | 21 of 58 | 19 of 66 |
| Facts exercised properly (valid tests) | 7 | 12 | 17 | 13 |
| Right record present; our probe form | 39; 0 | 44; 0 | 40; 0 | 44; 0 |
| Invalid tests | 3 | 6 | 7 | 7 |
| **Facts exposed** | **0** | **0** | **0** | **0** |
| Tests failing; all the absence policy | 5 | 0 | 2 | 2 |
| Their own assertions: false alarms on valid tests | 6 | 21 | 16 | 32 |

- **The lines changed the tests, not what they expose.** More of the twins' look-alikes offer a designated
  substitute, and more facts are exercised properly, but 44 of 48 tests still leave the right record in the
  workspace, and the agent, seeing both, picks right. Designated look-alikes in the target-present form do not bite
  on this agent, for the baselines as for our covers (2 of 77): the form is the gate, and the substitute works
  through it (§3).
- **"A perfect assistant must be able to pass them" did not stop impossible tests:** the bot deleting or editing
  others' Slack messages, invites of people already in the channel, deleting a calendar the actor does not own.
- **Their own checks got worse:** 51 of the 53 false alarms are tests expecting a cancelled event or a deleted
  calendar to disappear, all flagged in the review before the runs.
- **Protocol deviation:** N0M's Box session wrote tests that did not load after the protocol's one repair turn; it got
  two more turns with the loader's own errors (log), as our writer gets its format errors back.

## Proposal for the full comparison

1. **Arms, all run on the same agents** (OpenClaw with the self-hosted Qwen first; later agents unchanged):
   - **B1 (N0M):** the inputs of [twin2/n0m/inputs](twin2/n0m/inputs) (N0's plus the PI's lines and the corrected
     format document), per domain.
   - **B2 (N1M):** B1 plus the facts of each brief ([n1/make_inputs.py](n1/make_inputs.py)), per brief.
   - **Load feedback:** give the baselines the loader's errors until their tests load (at most three turns), as our
     writer gets its format errors back; the twins needed it once (§8).
   - **Ours (G2):** the frozen pipeline after 6b's regeneration.
2. **Briefs and budget:**
   - **Briefs:** all 51 (Phase 4's and 6b's).
   - **B2:** for each brief, as many tests as our pipeline derives from it (about 5.4).
   - **B1:** per domain, as many tests as ours in that domain.
   - **Repetition:** k = 3 everywhere; report detect@1 and detect@3.
3. **Before any run:** the structural review of §1 on all arms, in one shuffled pool, with the same rules and flaw
   causes. It gives facts exercised properly and the flaw rate. Include about 20 of our tests blind, and compare them
   with their mechanical claims afterwards.
4. **Runs and ground truth:**
   - **The runs:** every valid test of every arm, 3 trials.
   - **Ground truth for the baselines:** the review's intended target per test works as an answer key. Our triage
     plus judge v2 grade their trials with it; the key never goes to their own oracles.
   - **Blind samples:** 60 trials per arm, labelled by hand before any verdict, check that grading.
5. **Oracles scored per pipeline, flawed tests included:** B1 and B2's AgentDiff assertions, the plain judge with the
   expected outcome, J0, and ours.
6. **Measures:** the table under Q3, per arm and per domain, with counts and denominators.
7. **Ablations, reported beside the arms:**
   - **Covers against probes:** from the runs already planned.
   - **Plain twins on a random sample:** done in this pilot (plain48: 14 of 48 probes fail with the substitute, 2
     without); in the full comparison, repeat on the regenerated suite with the same rule and draw.
   - **The machinery:** first drafts, from the generation records.
   - **The judge:** the triage alone against triage plus judge v2.
8. **Size and cost** (estimates from this pilot):
   - **Tests:** about 280 per baseline arm.
   - **Generation:** under $10 at list for both arms.
   - **Solver runs:** about 1,700 trials, about 5 to 7 hours at this session's 12 in flight.
   - **LLM judging:** about $50 at list.
   - **Labelling:** 180 blind trials.

**Decisions for the PI before the full run:**
- **Whether the AgentDiff suite goes in as a status-quo row.** It is not needed to answer Q1–Q3.
- **Whether the same-name-pair pattern is the baseline's right to exploit.** The default people already hold Maya
  Chen and Maya Lopez; recorded as infrastructure.
- **Whether B2's fact list keeps the kinds' definitions.** They hint at the split and level alternatives. This pilot
  kept them, as part of "the facts".

## Limits of this pilot

- **One agent, and small samples.**
  - 48 tests per baseline.
  - Cycle 2's 12 plain-twin pairs were chosen from probes that had exposed a fact; the random sample of 48 (plain48)
    gives the average effect, with the same answer.
- **Our side is the recorded full_02 run, not a same-day rerun.** The Phase 4 numbers include 5 scenarios now judged
  flawed for their ids (G4-CAL-01, -02, -06, -07, G4-LIN-06). Without them, per 48 tests: 11.6 facts exposed at
  detect@3 (7.1 at detect@1), and 31.7 exercised properly.
- **I am the only labeller,** and I wrote the reviews. The rules were fixed before generation; the calibration
  against our own tests' mechanical claims is left to the full comparison.
- **The coding agent had no shell** (the kit's sandbox), so it could not try its tests. One repair turn for load
  errors was allowed; none was needed.
- **The twins are one generation each,** with no unchanged same-day repeat; the pre-registered rule required one only
  if a twin exposed 3 or more facts, and neither exposed any.
- **Our format document for the baselines had errors** (§5). They changed the baselines' assertion results only,
  not what their tests expose; the corrected figures are given.

## For the PI, outside the question

- **Muse billing:** Muse answered HTTP 402 ("Billing verification failed") from 16:13 until the PI's recharge;
  N1's judges reran afterwards.
- **G4-BOX-01's wording:** OpenClaw reads the comment clause as a second instruction in both arms of the ablation (12
  of 12 trials). Its two probes' exposures in full_02 then belong to the reading, not to H:Comment.item_id:comment or
  B:Comment.file_id. N1-BOX-T12 shows the same reading ("with a review task assigned by Omar").
- **Replica behaviour met here:**
  - Slack's reaction whitelist has no `white_check_mark`.
  - Calendar's `events.list` hides cancelled events.
  - Slack's `chat.delete` is author-only, as in Slack.
  - Box has no readable hub-item adder, and removing a hub item returns 501.
  - Slack history omits reactions (known).

## Files

| Path | What |
|---|---|
| [q4/](q4/README.md) | Question 4, from existing data plus the plain judge |
| [n0/](n0/) | N0: inputs, generator, converter, review rules, review, runs, labels, oracles |
| [n1/](n1/) | N1: inputs, review, runs, labels, flaws found at run time |
| [cycle2/](cycle2/) | The form and content ablations: cases, run, labels |
| [twin2/](twin2/README.md) | The mutated twins: the naive fixes a reviewer would ask for, run and scored |
| [plain48/](plain48/README.md) | The substitute's effect on 48 randomly drawn probes |
| [plain_twins.py](plain_twins.py), [plain_pick.json](plain_pick.json), `ablation/` | The plain twins and their sample |
| [ours.py](ours.py), [machinery.py](machinery.py), [compare.py](compare.py) | Our side, the machinery, the tables |
| [judges.py](judges.py), [assertions.py](assertions.py), [score_oracles.py](score_oracles.py) | The baselines' oracles |
| [label_view.py](label_view.py), [add_labels.py](add_labels.py), [summarize_labels.py](summarize_labels.py) | Labelling |
