# The denominator: the tests the methodology prescribes

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
| **A. The Muse pipeline, one attempt, plus one retry after a failed attempt** (Muse for every brief; Sonnet's attempts become the writer comparison) | 86 | 4: the Linear team brief, the Linear issue-count brief, the Box task brief, the Linear label brief | 195 | 187 | 161 | 90 | **633** |
| A without the retry | 83 | 6 (the four, the Box file-location brief, the Calendar event-visibility brief) | 185 | 179 | 154 | 89 | 607 |
| B. The earliest attempt, plus one retry (Sonnet v1 for the 34 hand-grouped briefs, Muse for the rest) | 86 | 4: the label-parent brief (invalid at review), the Linear issue-count brief, the Box task brief, the Linear label brief | 198 | 191 | 164 | 90 | 643 |
| B without the retry | 83 | 7 | 188 | 182 | 156 | 89 | 615 |
| Every attempt on record (production, redundant) | 135 | — | 202 | 197 | 178 | 90 | 667 |

The PI has not yet chosen the rule (2026-10-01). Under either rule the uniformity gap is the same: the two
completion_01 briefs rejected and never retried (the Box task brief, the Linear label brief) get the retry every
other failed brief got, or are declared failed without one; the outcome-driven round-2 rewordings of ten boundary
requests do not count (only the one whose round-1 request was invalid is a retry), so boundary results come from
round 1 for the other nine.

**One test per item.** Where the designated attempts leave two or more valid tests for one item (a fact claimed in
two scenarios, or two units of one fact), the test from the scenario of the fact's own brief counts; failing that,
the earliest-generated scenario's. The rest are spares (rule A: 10 probes, 10 absence, 26 underspecified). One
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
