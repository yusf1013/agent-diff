# The denominator: the tests the methodology prescribes

*The three summary tables (the denominator filled of prescribed; OpenClaw runs and failures on the filled items; the attempts) are in [../denominator_tables.md](../denominator_tables.md), built by `runs/denominator_01/kit/tables.py`.*

*The PI's decisions of 2026-10-01 (the discussion is logged in [overnight_2026-09-30.md](overnight_2026-09-30.md)
and the roadmap's "Decisions (2026-10-01)"). Every reported number is read against the counts here. They come from
the domain model and the replicas alone; no generation attempt, writer, retry or run changes them. The kit that
measures how the denominator is filled is [runs/denominator_01](../runs/denominator_01/README.md).*

## The principle

The methodology prescribes a fixed number of tests per service: one item per servable fact in each of three forms
(a regular probe, an absence test, an underspecified test), and one per faithful capability boundary. Cover cases
are the sampling vehicle through which the facts are reached; they are not counted. Several-match tests are a
separate addition whose coverage space is still to be settled by its own investigation; they are not in the
denominator. **Without several-match the denominator is 732 cases.**

## Facts: 255 in the catalog, 213 servable

| Service | Catalog facts | Unservable | Servable | Why unservable |
|---|---:|---:|---:|---|
| Box | 60 | 0 | 60 | — |
| Calendar | 40 | 6 | 34 | a calendar's sharing rules (the rule's role, scope type, scope value and calendar) can be listed only with the owner role; a recurring series (the occurrence's series, the derived occurrence) is listed only when the window covers its first start |
| Linear | 121 | 36 | 85 | every `projects` query errors and a project's lead cannot be read (15 facts: the project, project-status, project-relation and initiative-to-project facts); the `parent` filter is ignored (2: an issue's parent, as hierarchy and as binding); initiatives, notifications and organization invites exist "with varying completeness" (19 facts) |
| Slack | 34 | 0 | 34 | — |
| **All** | **255** | **42** | **213** | |

Source: `runs/fact_coverage_01/catalog/<service>.json` (the facts); `runs/autogen_02/inputs/briefs_phase4.excluded.json`
(the unservable list, as the replica notes record it). A fact is one requirement of the domain model, counted
once, never multiplied by routes or combinations. Kinds: attribute 142, relationship 65, hierarchy 9, binding 24,
derived 15.

## Capability boundaries: 152 elements, 93 faithful

For each attribute and relation of the catalog, the write the actor cannot make — through which operation, under
which precondition: permission 59, read-only field 40, no operation 26, state precondition 21, value limit 6. The
152 are an addition to the domain-model input, derived from the catalog (`runs/boundary_02/catalog.py`), then each
probed on the replica (`runs/boundary_02/space.json`).

| Service | Elements | Faithful | Unfaithful (the replica performs what the service refuses) | Not a boundary | Replica gap (the endpoint is missing) | Uncertain |
|---|---:|---:|---:|---:|---:|---:|
| Box | 35 | 21 | 3 | 8 | 2 | 1 |
| Calendar | 28 | 24 | 1 | 0 | 0 | 3 |
| Linear | 47 | 20 | 22 | 3 | 0 | 2 |
| Slack | 42 | 28 | 1 | 3 | 10 | 0 |
| **All** | **152** | **93** | **27** | **14** | **12** | **6** |

Linear's 22 unfaithful elements are its permission checks, which the replica does not enforce. The faithful 93 by
class: read-only field 32, permission 31, no operation 15, state precondition 13, value limit 2.

## The prescribed tests: 732

| Service | Regular probes (one per fact, all of the fact's decoys in it) | Absence (one per fact) | Underspecified (one per fact) | Boundary (one per faithful element) | **Total** |
|---|---:|---:|---:|---:|---:|
| Box | 60 | 60 | 60 | 21 | **201** |
| Calendar | 34 | 34 | 34 | 24 | **126** |
| Linear | 85 | 85 | 85 | 20 | **275** |
| Slack | 34 | 34 | 34 | 28 | **130** |
| **All** | **213** | **213** | **213** | **93** | **732** |

Trials (three per test) are metadata, not budget.

## What is not in the denominator

- **Cover cases.** A cover is the scenario as written (target and every near miss present): the vehicle that
  supplies the natural request, its conditions and its near misses, from which the probes and the policy tests
  derive. The number of covers is a sampling choice. The 89 briefs on record are kept as generated (the PI,
  2026-10-01), with their shortcomings on record: two grouping rules (38 briefs grouped by hand, size free; 51 by a
  script, one entity's facts in catalog order, three per brief, a fixed size never put to the PI); 22 single-fact
  briefs, whose requests meet the scope rule only where the writer added conditions; the 18 reproduction briefs generated twice (Sonnet, then Muse) and the 16 prospective briefs three times (Sonnet
  v1, v2, then Muse), 3 briefs regenerated after a failed attempt and 2 given a second draw (see "How it is filled"); 12 facts claimed by writers beyond their briefs, so 8 facts earn credit in
  two or three scenarios; one Slack fact (who posted a message) in two briefs.
- **Single-decoy probes of a multi-decoy fact.** The derivation also makes one probe per decoy; where a fact has
  two or more decoys those are spares beside the packed probe, reported apart (204 in the frozen pipeline's output).
- **Clones** (a copy of the target that differs only in unused fields, one per scenario): they isolate no fact.
- **Several-match tests**: a separate addition, pending.
- **Generation-side matters** that do not change a count: the scope rule for underspecified tests (dropping the
  fact's condition must leave a multi-condition request), two facts carried by one condition (one test fills two
  items), a writer declining a rewording, a probe dropped because its near miss loses its trap without the target,
  and the rulings.

## How it is filled: the attempts on record

The PI's rule (2026-10-01): one generation attempt per item, with internal retries inside the pipeline's stages;
no item may hold redundant copies, and no item may get more attempts than another. Production counts (998 cases,
1,000+ runs, 254 cover–fact slots, 204 covered facts) are not denominators.

**The attempts on record, by brief set:**

| Brief set | Attempt 1 | Attempt 2 | Attempt 3 |
|---|---|---|---|
| 18 reproduction briefs (the design study's hand-written scenarios' fact sets) | Sonnet, method v1 (autogen_01 arm R, 2026-09-26): 18 accepted, 1 invalid at review | Muse, the frozen pipeline (regen_01, 2026-09-30): 18 accepted | — |
| 16 prospective briefs (chosen by hand) | Sonnet, method v1 (arm P): 15 accepted; the Linear team brief (key, description, privacy) rejected | Sonnet, method v2 (arm P v2): 16 accepted | Muse, the frozen pipeline (regen_01): 14 accepted at the first draw; the Slack channel brief (member count, creation date, workspace role) accepted at a second draw; the Linear team brief rejected twice |
| 32 briefs drawn by rule, orders 1–32 | Muse, the frozen pipeline (autogen_02 Phase 4, 2026-09-27): 29 accepted; the Box file-location brief (parent folder, collections) and the Linear issue-count brief rejected, the Calendar event-visibility brief lost to a Muse outage | Muse (completion_01, 2026-09-28), the three generated again: the Box and Calendar briefs accepted, the Linear issue-count brief rejected again | — |
| 19 briefs drawn by rule, orders 33–51, and 4 briefs for the development briefs' 12 facts (those 12 facts had been generated twice before, in autogen_01's development rounds under the unfrozen method, never counted) | Muse (completion_01): 21 accepted; the Box task brief (item, creator, binding, assignment count) and the Linear label brief (group flag, name, team) rejected, never retried | — | — |
| 1 new brief (the related issue's direction) | Muse (regen_01): accepted | — | — |

Inside an attempt the writer may answer the code checks up to 6 times and the cold reader twice (the orchestrator's
limits, unchanged since 2026-09-25; autogen_01's plan text said 4); a Muse outage retry is the same attempt. The
Sonnet arms ran under method v1 and v2 of the same orchestrator. **The three Muse runs are not one frozen pipeline:**
they share the orchestrator, the derivation and the checks frozen at tag `grounding-freeze-01` (2026-09-27; Phase
4's suite was rebuilt from its recorded scenarios with the frozen kit), but Phase 4's writer ran on 2026-09-27
00:05–01:27 EDT, before that day's writer-prompt fix ("the writer matches the examples' standard, not their
content; the Box example loses its test-only hint", 20:24), and completion_01 (09-28) and the regeneration (09-30)
after it: the Muse pipeline at two dated versions of the writer prompt.

**The one-attempt rules compared** (the kit's `numbers/filling.json`; "filled" = items with a test valid under the
rulings as they stand, whenever the ruling was made):

| Rule | Scenarios | Briefs with no usable scenario | Probe items of 213 | Absence of 213 | Underspecified of 213 | Boundary of 93 | **Filled of 732** |
|---|---:|---|---:|---:|---:|---:|---:|
| **A (adopted). The Muse pipeline, one attempt, plus one retry after a failed attempt** (Muse for every brief; Sonnet's attempts become the writer comparison) | 86 | 4: the Linear team brief, the Linear issue-count brief, the Box task brief, the Linear label brief | 195 | 187 | 161 | 90 | **633** |
| A without the retry | 83 | 6 (the four, the Box file-location brief, the Calendar event-visibility brief) | 185 | 179 | 154 | 89 | 607 |
| B (not adopted). The earliest attempt, plus one retry (Sonnet v1 for the 34 hand-grouped briefs, Muse for the rest) | 86 | 4: the label-parent brief (invalid at review), the Linear issue-count brief, the Box task brief, the Linear label brief | 198 | 191 | 164 | 90 | 643 |
| B without the retry | 83 | 7 | 188 | 182 | 156 | 89 | 615 |
| Every attempt on record (production, redundant) | 135 | — | 202 | 197 | 178 | 90 | 667 |

**The PI's decision (2026-10-01, afternoon): Muse is the writer of the main suite; other writers only in a separate
comparison. So rule A is adopted: the adopted set is 86 Muse scenarios, one test per item, 633 of 732 items
filled.** The uniformity gap: the two
completion_01 briefs rejected and never retried (the Box task brief, the Linear label brief) get the retry every
other failed brief got, or are declared failed without one; the outcome-driven round-2 rewordings of ten boundary
requests do not count (only the one whose round-1 request was invalid is a retry), so boundary results come from
round 1 for the other nine.

**One test per item.** Where the designated attempts leave two or more valid tests for one item (a fact claimed in
two scenarios, or two units of one fact), the test from the scenario of the fact's own brief counts; among those, a
scenario whose near miss realizes a catalog alternative outranks one with only a plain decoy (the PI, 2026-10-01
evening: the repeat made for a fact's lure is the one kept); then the earliest-generated scenario's. Every rule is
about construction, never about a solver's outcome. The rest are spares (rule A: 10 probes, 10 absence, 26 underspecified). One
underspecified test can fill two items when its dropped condition carries two facts (rule A: 152 valid units fill
161 items).

**Rule A per service** (items filled of the prescribed):

| Service | Probes | Absence | Underspecified | Boundary | Filled of total |
|---|---:|---:|---:|---:|---:|
| Box | 54 of 60 | 52 of 60 | 46 of 60 | 20 of 21 | 172 of 201 |
| Calendar | 33 of 34 | 30 of 34 | 26 of 34 | 23 of 24 | 112 of 126 |
| Linear | 77 of 85 | 76 of 85 | 68 of 85 | 20 of 20 | 241 of 275 |
| Slack | 31 of 34 | 29 of 34 | 21 of 34 | 27 of 28 | 108 of 130 |
| **All** | **195** | **187** | **161** | **90** | **633 of 732** |

(Boundary per service: the four invalid round-1 requests are one each in Slack, Calendar, Box and Linear; Linear's
is the one restored by the retry.) The 99 unfilled items (`numbers/filling.json`, `unfilled_reasons`): 33 in the four failed briefs (11 facts × 3
forms); 25 with a test on record that the rulings leave out (a flawed near miss or a variant read as invalid: 3
probes, 11 absence, 11 underspecified); 36 with no test of that form derived for the fact (4 probes: a comment's
file and a milestone's project lose their trap without the target, a calendar-list entry's selected flag and a
message's text got no packed probe; 4 absence twins; 30 underspecified: the condition could not be dropped under the
scope rule, the writer declined, or code found it not derivable); 2 probes whose only valid form is a single-decoy
probe of a two-decoy fact (a hub item's file, a message's reactions); and 3 boundaries whose request the cold reader
rejected.

**The funnel under rule A** (brief attempts to valid tests to items; the regular columns from report_01's
`numbers/generator.json` and regen_01's `eval/funnel.json`, the units from this kit):

| Stage | Phase 4 (2026-09-27) | completion_01 (2026-09-28) | regeneration (2026-09-30) | All |
|---|---:|---:|---:|---:|
| Briefs, first attempts | 32 | 23 | 35 | 90 |
| Retries after a failed attempt | — | 3 (Phase 4's failures) | 2 (second draws) | 5 (2 owed) |
| Writer versions per accepted scenario, median and max | 2, 7 | 2, 3 (the outage retry batch 2, 7) | 2, 9 | |
| Accepted scenarios | 29 | 21 + 2 retried | 33 + 1 retried | 86 |
| Without a scenario | 2 rejected, 1 outage (all three retried) | 2 rejected, never retried; 1 retry rejected | 2 rejected; 1 retry rejected | 4 briefs |
| Reviewed usable | 29 | 23 | 34 | 86 |
| Derived regular candidates (cover / probe / fact probe) | 29 / 99 / 31 | 23 / 93 / 22 | 34 / 135 / 47 | 513 |
| Dropped by the witness check | 1 | 1 | 4 | 6 |
| Left out by the rulings, before the runs / after judgment | 0 / 0 | 1 / 2 | 7 / 0 | 10 |
| Valid regular tests | 158 | 134 | 205 | 497 = 86 covers + 205 packed probes + 204 single-decoy spares + 2 unpacked |
| Absence units built → valid | 61 → 60 | 69 → 66 | 78 → 71 | 208 → 197 |
| Underspecified units built → valid | 51 → 50 | 51 → 44 | 64 → 58 | 166 → 152 |
| Boundary requests → valid | | | | 93 → 89, + 1 retry = 90 |
| **Items filled, one test per item** | | | | **195 probes + 187 absence + 161 underspecified + 90 boundaries = 633 of 732** |

Two of the rulings after judgment came from the blind review of 2026-09-30 (two Box near misses, in completion_01's
scenarios); under the PI's rule an invalid test is invalid whenever it shows.

## The agents under test, on the filled items (as of 2026-10-01)

| Agent | Harness | Probe, absence and underspecified items | Boundary items |
|---|---|---|---|
| Qwen3.8-27B (BF16), self-hosted on vLLM 0.30.0, served as `qwen3.8-27b` | OpenClaw, 10-minute budget, 3 trials | every item on record, both rules | the 93 ran only on the bare toy loop (8-minute budget, 40 turns), 3 trials: not yet on the agent under test |
| GPT-6.1 Sol (`gpt-6.1-sol`, thinking medium, the ChatGPT plan) | OpenClaw, 10-minute budget, 3 trials | rule A's items except one Linear brief's three facts (due date, estimate, identifier: 9 items; its scenario's clock lies past the login's expiry); none of rule B's Sonnet-written scenarios | none |
| Sonnet 5.5 (effort medium, the Max plan) | Claude Code 2.1.285 headless, 10-minute budget | a 32-test pilot on the Muse half, one trial | none |

Judge: judge v2 on Muse Spark 1.3 (list prices reported); the self-hosted Qwen replays all 2,115 Muse verdicts at
98.6% agreement (judge_qwen_01), whether it becomes the judge is the PI's open decision.

## The adopted set against the runs on record (2026-10-01; `runs/denominator_01/kit/outcomes.py` → `numbers/outcomes.json`)

**One attempt, and what a retry is.** One attempt is one writer session on a brief: the writer drafts the scenario,
code checks it, the replica pre-checks run it, the cold reader reads it; every finding goes back to the same writer
session (up to 6 check rounds and 2 reader rounds). Those are the internal retries, inside one attempt. A retry in
the denominator's sense is a fresh writer session on the same brief after an attempt ended without an accepted
scenario. Five happened (the three failures of the Sept 27 batch, regenerated on Sept 28; two second draws on
Sept 30), two are owed (the Box task brief and the Linear label brief, rejected on Sept 28 and never retried).

**Redundancy inside the 633.** None by construction: one designated test per item (the 46 spare tests beyond one
per item are reported apart, with the 86 covers and the 206 single-decoy or unpacked probes). Every designated test
has three trials on disk for each agent. Attempts replaced for infrastructure reasons, never for the agent's
result: Qwen, 6 tests (Box tests of the regenerated half whose first attempt failed the environment preflight;
16 trial-attempts); Sol, 18 tests (a provider error, 14; a provider stall, 4). Trials voided after judging because
the agent acted only on a near miss later ruled flawed: Qwen 18 trials, Sol 13. Trials ended by the ten-minute
budget count as failures without exposure (Qwen 25 among the designated probes; Sol none).

**Do the numbers drop?** Yes, and the drop has a cause worth the PI's attention.

| Regular exposure, facts at detect@3 (detect@1) | Qwen | Sol |
|---|---:|---:|
| Everything on record, Sonnet's tests included (768 valid tests) | 106 (78) | not run |
| Every Muse-written valid test (497: covers, packed probes, single-decoy probes) | 88 (62) | 13 (12) |
| **The designated packed probe per item (195)** | **61 (35)** | **10 (10)** |

Qwen's 27 facts lost between "every Muse test" and the designated probes: 22 were exposed only by a single-decoy
probe beside the packed one (with all of the fact's decoys present Qwen picks the best match and passes; shown a
single decoy it acts on it), 3 only by another Muse scenario's test (a tie-break spare), 2 only by a cover. Sol's
3: two by single-decoy probes, one by a tie-break spare. **So the packed-probe definition costs about a quarter of
the regular exposures the single-decoy form finds.** The policy cells do not move: on the designated units every
decision is as published (Qwen: Calendar absence policy-level at 0.889, Box absence 0.781 and Slack underspecified
0.719 undecided, the five others not policy-level; Sol: all eight not policy-level, rates 0.00–0.17), rates within
0.03 of the all-units reading.

**The 99 unfilled items, by what happened:**

| What happened | Probe | Absence | Underspecified | Boundary | Items |
|---|---:|---:|---:|---:|---:|
| The brief produced no scenario (4 briefs, 11 facts) | 11 | 11 | 11 | — | 33 |
| A test was built, then a ruling left it out (a near miss ruled flawed, or the variant read as invalid) | 1 | 11 | 11 | — | 23 |
| No test of the form could be derived from the scenario | 4 | 4 | 30 | — | 38 |
| Only a single-decoy probe exists for a two-decoy fact (the packed form lost its trap) | 2 | — | — | — | 2 |
| The cold reader rejected the request | — | — | — | 3 | 3 |
| **All** | **18** | **26** | **52** | **3** | **99** |

The facts: the four failed briefs are the Linear team (key, description, privacy), the Linear issue count, the Box
task (item, creator, their binding, assignment count) and the Linear label (group flag, name, team). The rulings
touch the folder name, the file's parent folder and collections, the folder's description and tags (Box); the
calendar's title, the list entry's selected and hidden flags and calendar, the event's video link, status, transparency
and attendee resource (Calendar); the cycle number (Linear); the channel name, the message text, the user's real name
and username, the member count, the reply count and the workspace role (Slack). No underspecified variant could be
derived for 30 facts whose condition cannot be dropped and leave a request for one record (the Linear user's flags
and names, the workflow state's name and type, the Box file's name, extension and tags, the Slack conversation's
flags and topic, the thread parent, among others). No probe for a comment's file and a milestone's project (their
near miss loses its trap once the target is gone), a calendar-list entry's selected flag and a message's text.

**The funnel, in plain stages** (Batch 1: Sept 27, the first 32 briefs drawn by rule; Batch 2: Sept 28, the 19
remaining drawn briefs, the 4 development-fact briefs and the 3 retries of Batch 1's failures; Batch 3: Sept 30, the
34 hand-grouped briefs regenerated with Muse and 1 new brief, with 2 retries):

| Briefs to scenarios | Batch 1 | Batch 2 | Batch 3 | All |
|---|---:|---:|---:|---:|
| Briefs attempted (first attempt) | 32 | 23 | 35 | 90 |
| Accepted at the first attempt | 29 | 21 | 33 | 83 |
| Failed at the first attempt | 3 | 2 | 2 | 7 |
| Retries run (in this batch) | 0 | 3 | 2 | 5 |
| Accepted at the retry | 0 | 2 | 1 | 3 |
| Briefs still without a scenario | 0 | 3 | 1 | 4 |
| Usable after manual review | 29 | 23 | 34 | 86 |
| Writer versions per accepted scenario, median | 2 | 2 | 2 | 2 |
| Writer versions per accepted scenario, maximum | 7 | 7 | 9 | 9 |

| Scenarios to tests | Batch 1 | Batch 2 | Batch 3 | All |
|---|---:|---:|---:|---:|
| Regular tests derived | 159 | 138 | 216 | 513 |
| Dropped: the near miss loses its trap without the target | 1 | 1 | 4 | 6 |
| Left out by a ruling before the runs | 0 | 1 | 7 | 8 |
| Left out by a ruling after judgment | 0 | 2 | 0 | 2 |
| Valid regular tests | 158 | 134 | 205 | 497 |
| Absence tests derived | 61 | 69 | 78 | 208 |
| Absence tests valid | 60 | 66 | 71 | 197 |
| Underspecified tests derived | 51 | 51 | 64 | 166 |
| Underspecified tests valid | 50 | 44 | 58 | 152 |

| Tests to items | Probes | Absence | Underspecified | Boundary | All |
|---|---:|---:|---:|---:|---:|
| Prescribed items | 213 | 213 | 213 | 93 | 732 |
| Valid tests of the form | 205 | 197 | 152 | 90 | 644 |
| Spare tests beyond one per item | 10 | 10 | 26 | 0 | 46 |
| Covers and single-decoy probes, reported apart | 292 | — | — | — | 292 |
| **Items filled** | **195** | **187** | **161** | **90** | **633** |

## Two more denominators, tracked beside the 732 (the PI's proposal, 2026-10-01 afternoon)

- **Covers: one per brief, 90 prescribed** (the 89 briefs plus the new related-issue brief), **86 filled**. For
  tracking only: the brief set is a sampling choice.
- **Single-decoy probes: one per (fact, designated alternative), 286 prescribed.** The catalog names each fact's
  designated alternatives (a sibling field, an indirection, a direction, ...); a fact with none gets one
  plain-difference probe; a hierarchy, binding or derived fact carries its one lure in its kind. Per service: Box
  80, Calendar 48, Linear 112, Slack 46. Against it, the adopted set's valid single-decoy probes in each fact's
  designated scenario, counted per fact and capped at the fact's prescribed number (a built decoy is not labelled
  with the catalog alternative it realizes): **227 filled** (Box 60, Calendar 40, Linear 93, Slack 34), from 297
  built. Kit: `runs/denominator_01/kit/single_decoy.py` → `numbers/single_decoy.json`.

**The denominator with the two tracked forms, per service, filled of prescribed (2026-10-01):**

| Service | Covers | Packed probes | Single-decoy probes | Absence | Underspecified | Boundary | Total |
|---|---:|---:|---:|---:|---:|---:|---:|
| Box | 20 of 21 | 54 of 60 | 61 of 80 | 52 of 60 | 46 of 60 | 20 of 21 | 253 of 302 |
| Calendar | 16 of 16 | 33 of 34 | 40 of 48 | 30 of 34 | 26 of 34 | 23 of 24 | 168 of 190 |
| Linear | 32 of 35 | 77 of 85 | 93 of 112 | 76 of 85 | 68 of 85 | 20 of 20 | 366 of 422 |
| Slack | 18 of 18 | 31 of 34 | 35 of 46 | 29 of 34 | 21 of 34 | 27 of 28 | 161 of 194 |
| **All** | **86 of 90** | **195 of 213** | **229 of 286** | **187 of 213** | **161 of 213** | **90 of 93** | **948 of 1,108** |

The 732 of the main denominator are the four right-hand columns' 213 + 213 + 213 + 93; covers and single-decoy
probes are tracked beside them. One test can fill a packed-probe item and a single-decoy item at once (a fact with
one decoy: its single probe is its packed form): of the 229 counted single-decoy probes, 130 stand beside a packed
probe and the other 99 are it. The single-decoy count is per fact, capped at the catalog's prescribed number
(300 valid single-decoy probes built in the designated scenarios).

**What leaving out the rest costs, with the tracked forms counted** (`numbers/outcomes.json`, "tracked_denominators_set":
the chosen scenarios' covers, the designated packed probes, and per fact its single-decoy probes in claim order up to
the catalog's prescribed number):

| Set of tests | Tests | Qwen, facts exposed in any of 3 trials | Qwen, first trial | Sol, any of 3 | Sol, first trial |
|---|---:|---:|---:|---:|---:|
| Everything on record, Sonnet's tests included | 768 | 106 | 78 | — | — |
| Every Muse-written valid test | 497 | 88 | 62 | 13 | 12 |
| The tracked denominators: covers, packed probes, counted single-decoy probes | 411 | 83 | 56 | 11 | 11 |
| The packed probes alone | 195 | 61 | 35 | 10 | 10 |

Between the first two rows Qwen loses 18 facts exposed only by Sonnet-written tests (the writer comparison, outside
the suite). Between the second and third, 5 for Qwen (a folder's creation date and item count, an event's start,
a user's status label, who posted a message: exposed only by a single-decoy probe beyond the catalog's prescribed
number for the fact, or by another scenario's test) and 2 for Sol (a cycle's name, the related issue's direction).
Between the third and fourth, 22 for Qwen and 1 for Sol: the covers' and single-decoy probes' exposures. Policy
cells are unchanged by any of this (they have no tracked spares).

**Every valid test on record, retained or excluded, with each agent's failures** (`runs/denominator_01/kit/retained.py`
→ `numbers/retained.json`; a regular test "with a failure" exposed a fact in some trial; a policy test with a failing
trial; boundary: the automated study's round 1 on the bare toy loop). 142 underspecified tests fill 161 items (a
dropped condition can carry two facts).

| Tests | On record | Qwen: run | Qwen: with a failure | Sol: run | Sol: with a failure |
|---|---:|---:|---:|---:|---:|
| **In the denominator** | | | | | |
| Covers | 86 | 86 | 10 | 85 | 2 |
| Packed probes | 195 | 195 | 61 | 192 | 10 |
| Single-decoy probes, counted | 130 | 130 | 44 | 126 | 4 |
| Absence tests | 187 | 187 | 154 | 184 | 31 |
| Underspecified tests | 142 | 142 | 111 | 138 | 8 |
| Boundary tests (bare toy loop, Qwen only) | 90 | 89 | 49 | 0 | 0 |
| **Retained** | **830** | **829** | **429** | **725** | **55** |
| **Remaining, outside the denominator** | | | | | |
| Sonnet-written covers | 48 | 48 | 4 | 0 | 0 |
| Sonnet-written packed probes | 49 | 49 | 10 | 0 | 0 |
| Sonnet-written single-decoy probes | 174 | 174 | 47 | 0 | 0 |
| Muse packed probes of a fact already filled (another scenario) | 2 | 2 | 1 | 2 | 0 |
| Muse single-decoy probes beyond the counted ones | 84 | 84 | 23 | 82 | 4 |
| Sonnet-written absence tests | 116 | 116 | 101 | 0 | 0 |
| Sonnet-written underspecified tests | 97 | 97 | 72 | 0 | 0 |
| Muse absence tests of a fact already filled | 10 | 10 | 9 | 10 | 2 |
| Muse underspecified tests of a fact already filled | 10 | 10 | 6 | 10 | 0 |
| Duplicate underspecified tests (same request as another) | 3 | 2 | 2 | 1 | 0 |
| **Excluded** | **593** | **592** | **275** | **105** | **6** |

Sol's "run" falls short of "on record" by the clocked Linear brief's tests (its login's expiry). Facts exposed at
detect@3 by the retained regular tests: Qwen 83, Sol 11; by the excluded Muse regular tests: Qwen 22, of which
5 are not among the retained; Sol 4, of which 2 not among the retained; the Sonnet-written tests expose
18 facts for Qwen that no Muse test exposes. Policy failing trials over usable trials, retained: Qwen
639/983, Sol 86/964.

**The Muse single-decoy probes beyond the counted ones (84):** 71 are further decoys of a fact in its own
scenario — the writer's method notes ask for them ("one decoy per (fact, substitute) ... use a plain decoy for a
fact with no substitute, or in addition ... include the nearest value on the wrong side ... two or three decoys on
one fact are good when they are different substitutes"), while the single-decoy denominator counts one per
alternative the catalog names; 13 sit in another scenario than the one counted for the fact: 8 where a
writer gave a decoy to a condition on a fact outside its brief (allowed by the method notes, not asked), 5 where
the fact sits in two briefs (the related issue's direction, which got a second brief to realize its lure; who
posted a message, in two reproduction briefs) and the tie-break chose the other scenario. Correction of 2026-10-01
(evening): the kits had keyed facts by id alone, and a user's email, name and timezone exist in Linear and in Slack;
keyed by service and fact, and with the single-decoy credit extended to facts without a packed probe, the counts
above replace the afternoon's (packed probes 195 tests, counted single-decoy probes 130, beyond 84).

**The excluded tests by origin (the PI's distinction, 2026-10-01 evening).** Two different things: a test that
arose as a by-product of a legitimate attempt (a scenario built for its own brief, whose items were unfilled, in which
the writer or a builder produced more than the one test per item), and a test from a decision to generate or run
something again for an item already filled.

| Origin | Tests | What they are |
|---|---:|---|
| By-product: the writer built more decoys for its own facts than the catalog names | 73 | single-decoy probes |
| By-product: the writer gave a decoy to a condition on a fact outside its brief (four scenarios) | 20 | 8 single-decoy probes, 8 absence twins, 4 underspecified variants |
| By-product: the variant builder makes one variant per fact, and some conditions carry several facts | 6 | 4 underspecified variants of facts filled by another variant, 2 duplicate variants |
| The outdated first version of a fact given a second brief (the related issue's direction: its first scenario had only a plain decoy where the catalog names the reversed relation; the second brief, decided by the lead on 2026-09-30, realized it, and is the one kept) | 2 | the first scenario's plain probe and its absence twin (its underspecified variant stays, since it also carries the relation's source fact) |
| A fact in two briefs by the brief set's design (who posted a message, in two of the design study's fact sets) | 5 | 2 single-decoy probes, 1 packed probe, 1 twin, 1 variant |
| Another writer's attempt at the same items (Sonnet, kept as the writer comparison by the PI's decision) | 485 | 48 covers, 223 probes, 116 absence, 98 underspecified |
| **All excluded** | **591** | |

No test was run more than its three trials by decision; attempts were replaced only for infrastructure failures.

## The 99 unfilled items, in full (2026-10-01 afternoon)

**Four briefs produced no scenario (33 items).** Each attempt ran the writer, the code checks, the replica
pre-checks and the cold reader, with findings going back to the same writer session.
- *The Linear team brief* (a team's key, description and privacy flag), two attempts, three reader rounds each.
  Last wording of the first: "Set the priority of the issue on the private team with MOB in its key, described in
  its team profile as owning offline sync, to High." Of the second: "Please set the 'Login fails on checkout'
  issue to High priority. It is in the private PAY* team that handles checkout billing." The reader rejected every
  version as unnatural: a real user names the team; stacking a privacy flag, a key fragment and the description's
  wording "reads as constructed to force a lookup". The same brief failed the same way with Sonnet. The three
  facts have no natural single-record request in this pipeline's hands.
- *The Linear issue-count brief* (the number of open issues of a project or cycle), two attempts, 4 and 7
  versions. Last wording: "Set the priority of the Done issue assigned to Maya Chen in the Harbor Launch project in
  the cycle with only two open issues left to High." The checks first caught probes that removed the named project
  with the target; then the reader rejected every version: identifying a cycle by its exact count of open issues
  "is a puzzle-like hint that only a test would contain".
- *The Box task brief* (which item a task is on, who created it, their binding, the number of assignees), one
  attempt, three reader rounds. Last wording: "Add the tag launch-ready to the board pack draft PDF in the Launch
  folder with the review task Omar Haddad created about proofreading the launch summary, the one with two
  assignees." The reader: a real user would name the file; task creator, task wording and assignee count read as
  constructed disambiguation. Never retried.
- *The Linear label brief* (a label's group flag, name and team), one attempt, three reader rounds. Wording: "Set
  the priority to High for the issue with the Refund label group of the Mobile team." The reader found the
  near miss for the label's team failing two conditions at once (the Refund group was workspace-level, so it was
  neither the Mobile team's group nor a Refund label of that team) and two undeclared near misses (issues with a
  Bug label only). Never retried.

**A test was built, then a ruling left it out (23 items).** All 23 had passed every automated stage (the writer's
checks, the replica pre-checks, the cold reader, the derivation and its witness check); what left them out is manual
review, by the PI or by a session (a Claude agent's review counts as manual, the PI's rule). 5 of them ran and were
judged before the ruling (the two blind-review rulings; their trials are voided); 18 were left out before they ran
(the regeneration's cut, the completion and Muse studies' pre-run reviews, and three tests the runner left out at
run time when the "Marcus Webb Jr" ruling arrived after the cut). By origin: 5 the PI's own rulings, 9 the PI's
rulings of 2026-09-28 applied by agents to later scenarios of the same kind, 9 agents' own reviews. A ruling is a decision, recorded in
`runs/roadmap_01/known_defects.json`, that a near miss does not differ from the request the way the writer
claimed, or that a variant is invalid; the scoring then leaves out every test holding that near miss and voids any
trial that acted only on it. The rulings here, by who made them:
- *The PI, in the blind review of 2026-09-30:* "Add the tag 'seaport-final' to the Seaport Archive folder whose
  description mentions the lighthouse and that is tagged 'harbor'": a folder named "Seaport Archive 2024" is a
  match when the other conditions hold (a natural reading includes it), so the folder-name near miss is no near
  miss; its absence twin and the drop-F variants of the same scenario's description and tags go with it (3
  items). "Add the tag harbor-final to the favorited copy of Harbor launch plan.pdf in the Harbor Launch folder
  that also has the Harbor budget spreadsheet": a copy in a subfolder of the named folder counts as "in the
  folder", so the parent-folder near miss is no near miss; its twin and the collections variant go (2 items).
- *The PI, 2026-09-28, applied by the lead to later scenarios of the same kind:* a cycle named "Cycle 7" but
  numbered 9 is what a user saying "cycle 7" may mean (the cycle-number twin, 1 item); a message whose displayed
  blocks say what its plain text does not is about that topic (the message-text twin and the reply-count variant
  of "Invite the user whose post about the lattice outage in #outages drew two replies", 2 items); "the active
  launch channel whose topic is ..." does not name a channel, so a channel whose purpose is launch coordination is
  such a channel (the channel-name twin, 1 item); "Marcus Webb", unquoted, includes Marcus Webb Jr (the real-name
  probe, its twin and the username variant, 3 items); "the small 5-person release channel" counts people, not the
  bot, so a channel with five people and the bot is a match (the member-count twin and the role variant, 2 items).
- *The regeneration session's review (2026-09-30):* "Move the kickoff review on my Editorial Calendar on Thursday
  to Room 5B": the calendar the user's own list shows as "Editorial Calendar" and a second calendar titled
  "Editorial Calendar" that is merely not selected for display are both what "my Editorial Calendar" means (the
  calendar-title twin, the selected-flag twin and variant, 3 items); "the Garden Workshop calendar on my calendar
  list shared with Sam Rivera" without "on my calendar list" has intended matches the agent cannot list (1 item).
- *The completion session's review (2026-09-28):* "the confirmed sprint review with a video link": an event whose
  description holds a Meet link naturally has a video link (the video-link twin, the status and attendee-resource
  variants, 3 items).
- *The Muse study's pre-run review (2026-09-27):* "Hide the calendar I call Team Travel": dropping "hidden" frees
  a calendar that is already hidden, which "hide" excludes (1 item); the event-transparency near miss of "Move
  the Budget Review ... it's blocking time on my calendar" is contestable (the aside carries the condition) and
  its twin stays out (1 item).

**No test of the form could be derived from the scenario (38 items): generation-side, every one.** None
subtracts from the denominator: each fact can carry the test; this scenario could not. The derivation and its
checks are code; the writer's part is a Muse call with a recorded reason.
- *30 underspecified variants.* The construction drops the condition carrying the fact and asks the Muse writer
  for a deletion-only rewording; code checks the relaxed query selects exactly the target and the freed near
  misses, and a cold reader must read the new request the same way. Outcomes: the writer declined 16 (no
  deletion-only edit keeps the intended matches: "Removing 'Data Analyst' leaves 'posted by our in Chicago', which
  is ungrammatical, and repairing it requires inserting a generic noun not in the original"; "Removing 'active'
  leaves 'the human admin', which still naturally implies a current active user"); the reader rejected 12 (the
  reworded request does not fit exactly the intended set, or reads as test-constructed, or the writer added a
  word); code found 3 not derivable (fewer than two identifying conditions would remain, the scope rule; or the
  relaxed query selects more than the intended records).
- *4 probes and 4 absence twins.* The derivation removes the target and the rows only it used, then runs the
  witness check: the request must select nothing, and the request with the fact's condition relaxed must select
  the near miss (that is what makes it a trap). Where the only instance of an entity the request names was
  attached to the target, the relaxed request finds nothing, and the near miss is no trap. Example: "Add a fire
  reaction to the message in #launch about the release checklist that Priya Sharma reacted to with eyes" — the
  near miss for the reaction relation is a checklist message that someone else reacted to with eyes; once the
  target is removed, no message anywhere carries an eyes reaction by Priya, so an agent looking for her reaction
  correctly finds none, and the probe cannot expose the fact. The same for a hub's file items when the only files
  of the named hub were the target's neighbours, for a comment's file and for a milestone's project. Code drops
  these ("claim not killed by witness: original=False, mutant=False"), with no manual step; the generation-time
  check that named entities must survive the target's removal does not yet cover relationship rows (a reaction, a
  membership), which is why these reached the derivation.
- *2 probes with only a single-decoy form* (a hub item's file, a message's reactions): the same check dropped
  their packed form (the two-decoy probe), since one of the two decoys loses its trap as above; the other decoy's
  single probe is valid and ran, but it is not the packed form the denominator prescribes.
- *3 boundary requests the cold reader rejected* (one each in Slack, Calendar and Box): the request did not name
  the record, hinted at the limit, or read as unnatural.

**The decided repeat, clarified (2026-10-01 evening).** The decision of 2026-09-30 was to give the related issue's
direction a brief of its own because its only scenario — *"Set the estimate to 5 for the Web team issue assigned to
Maya Chen that blocks the Checkout crash on Safari issue"* — had a plain decoy for it (a relation to another issue)
where the catalog names the reversed relation as the lure; nothing was said then about the first version, and both
stayed in the suite. The repeat — *"Set the estimate to 5 for the Todo issue assigned to Maya Chen with the Bug label
that is blocked by the Checkout rollout issue"* — realized the lure (an issue that blocks the anchor instead of being
blocked by it) and added a partial-identity and an indirection decoy. Under the denominator the repeat is the version
kept for this fact and the first version's plain probe and twin are the outdated spares; the tie-break now says so.
Failures: on Qwen the first version's probe exposed nothing, its twin failed 2 of 3 trials and its variant 1 of 3;
the repeat's packed probe and three probes exposed nothing, its twin failed 3 of 3 and its variant 1 of 3. On Sol the
first version exposed nothing anywhere; the repeat's partial-identity probe exposed the fact in one trial — Sol's
only exposure of it, and the one fact Sol exposed that Qwen did not. The suite's totals do not move (Table 2 is
unchanged), since the fact's designated packed probe exposed nothing for either agent before or after.
