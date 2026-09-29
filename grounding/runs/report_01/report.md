# Automated fact-discrimination tests for tool-using agents: evaluation and results

*A stub for the evaluation and results sections of a paper, written 2026-09-29 from the committed runs. It covers
the experiments, what they show and what they do not. There is no introduction, background or related work. Every
table names its source: a script in [kit/](kit/) and the JSON it writes into [numbers/](numbers/), or a run record.
Rows marked "–" or "not measured" are measurements not yet made.*

## 0. Setup

### 0.1 What is tested

An agent receives one natural-language request to change something in a business service: Box, Google Calendar,
Linear or Slack. It works through the service's API. Each request identifies its record by several conditions, for
example "Add the tag launch-ready to the PDF in the Launch Assets folder with a top-level comment by Dana Whitfield
saying 'approved for launch'". A **grounding failure** is acting on a record that meets only some of them, such as
a PDF whose comment says the same thing but was posted by someone else.

- **Environment.** AgentDiff replicas: each service's REST or GraphQL API over a seeded PostgreSQL schema, cloned
  for every trial. The final state and its diff are recorded.
- **Agent under test (main).** OpenClaw 2026.7.1-2, an open agent harness, running Qwen3.8-27B served on our own
  GPUs (131,072-token context, 8,192 output tokens). One turn per trial, 600 s per turn. Details in
  [openclaw_eval_01](../openclaw_eval_01/README.md).
- **Agent under test (reference).** The same model in a minimal tool loop ("the toy harness"), served by Purdue's
  GenAI Studio. Its results come from earlier studies and are reported apart, never merged with OpenClaw's.
- **Trials.** k = 3 per test. A result is reported at detect@3 (any of the 3 trials) and detect@1 (the first).
- **Generation and judging agents.**
  - Claude Sonnet 5 in Claude Code wrote, read and judged autogen_01's tests (judge v1).
  - Muse Code (Meta) with `muse-spark-1.3-contributor` did every later writer, reader and judge step (judge v2).
  - Every judge verdict in RQ4 and RQ6 is judge v2's. RQ5 measures its accuracy against hand labels.

### 0.2 Vocabulary

| Term | Meaning |
|---|---|
| **Fact** (requirement) | One fact of a service's domain model that a request can use to identify a record and that the agent can observe through the API, for example `A:File.tags` or `R:Issue.assigneeId`. Five kinds: attribute (A), relationship role (R), hierarchy (H), same-record binding across a to-many relationship (B), derived representation (D). The catalog lists them per service ([criterion.md](../fact_coverage_01/criterion.md)). |
| **Near miss** | A seeded record that meets every condition of the request except one fact, which it fails through that fact's designated alternative: a sibling attribute, a similar name, the other level of a hierarchy, and so on. Its *family* says how (F1 sibling role or attribute, F2 indirection, F3 direction, F4 level, F5 split binding, F6 representation, F7 neighbouring value, F8 partial identity; F0 a plain different value). |
| **Scenario** | A request, a seeded world, the target, and the declared near misses. Each near miss comes with a *claim* (which fact it fails), checked mechanically: the request's query, with that one fact's condition relaxed, must select the near miss, and the intended query must not. |
| **Regular tests** | Derived by code from a scenario. **Cover:** the scenario as written, target present. **Probe:** target removed, one near miss left, and the request ends "If there isn't one, just tell me." **Fact probe:** target removed, every near miss of one fact left, same ending. |
| **Policy tests** | What the agent does when the request cannot be met as stated. **Absence twin:** a probe without the escape clause, so the request presumes the record exists. **Underspecified:** two or more records match fully, because one condition was dropped from the request ("drop-F", one variant per dropped condition) or the target was copied ("clone"). Right behaviour: report the absence, or ask (or list the matches) before changing anything. |
| **Covered** | A fact is covered when some valid regular test holds a near miss for it whose claim passes the mechanical check in that test's world, in a fact-sensitive form: the target is present, or the request permits reporting absence (credit rule, [criterion.md](../fact_coverage_01/criterion.md)). A request that presumes a missing record earns no fact credit. |
| **Exposed** | A test exposes a fact when a counted trial acts on a near miss of that fact, or presents it as the answer. |
| **Valid** | Not left out by the PI's rulings on contested near misses (below). |
| **Unit, cell** | A policy test and its 3 trials; a service × mode (absence or underspecified) pair. |
| **Policy-level** | A cell's failures do not depend on the fact: with 90% confidence, a unit drawn at random fails more than 80% of its trials. |
| **Void** | A trial that is not a usable observation: a replica artifact, or no result. |

### 0.3 Protocol

- **Validity before running.** Every accepted scenario and every policy variant written by a model was read by a
  person before its runs. The PI ruled on the contested near misses. The rulings live in
  [known_defects.json](../roadmap_01/known_defects.json) and code applies them before scoring:
  - a test holding a flawed near miss is left out;
  - a trial whose only mistake is acting on a flawed near miss does not count.
- **Blind labels before verdicts.** For every run, a random sample of trials was drawn before the run and labelled
  by hand before any judge verdict on those trials was read.
- **Judging.** A mechanical triage reads the state diff. Judge v2 reads every trial that is not mechanically clean,
  20% of the clean ones, and the blind sample. It sees the request, the trajectory, the final answer, the diff and
  the answer key.
- **Opaque ids and test-side clocks.** Generated seeds had ids that named a record's role (`ev_target`,
  `team-design@…`). Before the final runs every made-up id was replaced by a random-looking one in the service's
  format, and tests that depend on today's date run with the agent's clock set to a fitting day. Box's ids are
  numbers and did not change.
- **The 8-minute budget.** A trial whose agent time, rate-limiter waits excluded, passes 8 minutes is the agent's
  failure. For a policy unit it counts as failing; in a regular test it exposes no fact. It was applied
  retroactively; OpenClaw ran with a 10-minute limit.
- **The policy decision rule** was fixed in code before the runs ([policy.py](../openclaw_eval_01/policy.py)):
  - every run of every valid unit counts, with units as independent draws;
  - the rate is failing trials over usable trials, with a cluster bootstrap over units (20,000 resamples, seed
    20260928);
  - policy-level if the 10th percentile is above 0.8, not policy-level if the 90th percentile is below 0.8, and
    undecided otherwise.

### 0.4 Size of the experiment on OpenClaw

Source: [kit/scale.py](kit/scale.py) → [numbers/scale.json](numbers/scale.json).

| Runs used for results | Trials | Agent hours | Model requests | Input tokens | Output tokens |
|---|---:|---:|---:|---:|---:|
| Regular suite: `full_02` (Box; the first pass), `full_03` (opaque-id re-run), `full_04` (6b) | 2,721 | 153.0 | 25,249 | 308M | 7.3M |
| Policy stage: first-pass looks and full populations | 1,743 | 134.6 | 19,326 | 242M | 6.9M |
| **All** | **4,464** | **287.6** | **44,575** | **550M** | **14.3M** |

- Agent hours add up each trial's agent time; trials ran 24 to 48 at a time.
- Median trial: 152 to 282 s depending on the run.
- **Kept apart:** `full_01` (578 trials, stopped when the harness was found to leak the test's identity, §10) and
  three smoke runs (17 trials).
- **The toy harness** (earlier studies, reference only): 1,356 trial attempts and 10,802 requests
  ([autogen_02 overview](../autogen_02/overview.md) §4).

### 0.5 Research questions

- **RQ1** How large is the coverage space?
- **RQ2** How much of it do automatically generated tests cover, validly?
- **RQ3** How well does the generator perform, and what do its checks catch?
- **RQ4** What failures do the tests expose in a real agent harness?
- **RQ5** How accurate is the automated judge?
- **RQ6** Do the policy failures occur per fact or as a policy, and what does the answer cost in tests?
- **RQ7** What do the trials show outside the grounding criterion?
- **RQ8** How do the tests compare with baselines, and which parts of the system matter (ablations)?
- **RQ9** Two extensions: requests with several matches, and requests beyond the agent's capabilities.

Then: lessons (§10), threats to validity (§11), cost (§12) and what is not yet measured (§13).

## RQ1. How large is the coverage space?

The coverage criterion is **fact-discrimination coverage** (FDC): a requirement is one fact of a service's domain
model, and a test covers it when a near miss forces the agent to check that fact
([criterion.md](../fact_coverage_01/criterion.md)). The catalog is built by code from the replicas' schemas and a
curated domain model ([catalog/build.py](../fact_coverage_01/catalog/build.py)). Every stored column of an included
entity and every model relationship has a recorded disposition: a fact, or a reason it is not one (a foreign key, a
bookkeeping column, a configuration field, and so on).

**Table 1. The catalog.** Source: [counts.md](../fact_coverage_01/catalog/counts.md);
[kit/coverage.py](kit/coverage.py) → [numbers/coverage.json](numbers/coverage.json) (`space`).

| Service | A attribute | R relationship | H hierarchy | B binding | D derived | **Facts** | With a designated alternative | Replicas cannot serve | **Servable** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Box | 31 | 19 | 2 | 5 | 3 | **60** | 45 | 0 | **60** |
| Calendar | 28 | 4 | 1 | 3 | 4 | **40** | 25 | 6 | **34** |
| Linear | 63 | 38 | 5 | 12 | 3 | **121** | 80 | 36 | **85** |
| Slack | 20 | 4 | 1 | 4 | 5 | **34** | 22 | 0 | **34** |
| **All** | **142** | **65** | **9** | **24** | **15** | **255** | **172** | **42** | **213** |

- **Attributes by subkind** (identity, text, time, quantity, state): Box 6/7/8/3/7, Calendar 8/4/2/0/14,
  Linear 19/8/11/3/22, Slack 5/5/2/0/8.
- **A designated alternative** is a sibling attribute or role, or a kind-level confusion for H, B and D facts. For
  the other 83 facts the near miss is a plain different value (for a state, another value is the designated
  alternative).
- **The 42 facts the replicas cannot serve** are 38 replica gaps (features the real services have and the replicas
  lack, mostly Linear) and 4 real limits (Calendar sharing rules the acting user cannot read). Source:
  `grounding/runs/boundary_01/report.md` on branch `exp/automation-01`. The generator's briefs never draw them.

**Table 2. The same four services under route-based criteria.** Source: [counts.md](../fact_coverage_01/catalog/counts.md).

| Service | FDC facts | Structural routes | Read-screened routes | … with ≤2 edges | … with ≤3 edges | Entity × route × mode | Fact pairs |
|---|---:|---:|---:|---:|---:|---:|---:|
| Box | 60 | 12,398 | 6,500 | 298 | 1,146 | 26,000 | 1,770 |
| Calendar | 40 | 168 | 30 | 20 | 28 | 120 | 780 |
| Linear | 121 | 989,643,546,920 | 58,820,072,198 | 2,854 | 23,372 | 235,280,288,792 | 7,260 |
| Slack | 34 | 2,870 | 212 (174 after review) | – | – | 696 | 561 |

- The FDC count is linear in the model's size: it does not multiply facts by routes, modes or one another.
- Route-based criteria grow with the schema's paths, up to 10^11 routes for Linear.

**The policy space.** The policy tests add two requirements per covered fact (one absence twin and one
underspecified test): 408 for the 204 facts covered in RQ2, 426 if all 213 servable facts were. RQ6 asks whether
they can be collapsed to one test per service and mode, 8 in all.

## RQ2. How much of the space do generated tests cover, validly?

**The generator.** A brief names 1 to 4 catalog facts of one service. An LLM writer turns it into a scenario, code
checks it, the replica installs and pre-runs it, and a second LLM reads it cold and must find the target and the
condition each near miss fails. Code then derives the regular tests (RQ3). Five generation runs wrote the
scenarios:

- **Sonnet R:** briefs on the 36 facts that fact_coverage_02's hand-built suites tested.
- **Sonnet P, and P v2:** briefs on facts no hand-built test used; P v2 regenerated P's briefs with a revised method.
- **Muse Phase 4:** briefs on facts no earlier brief had used. The run was cut to 32 of 51 briefs for time.
- **Muse 6b:** the remaining servable facts: Phase 4's 19 ungenerated briefs, its 3 briefs without an accepted
  scenario, and 4 new briefs for the facts earlier used only to develop the method.

**Table 3. Facts covered by valid tests, by writer.** Source: [kit/coverage.py](kit/coverage.py) →
[numbers/coverage.json](numbers/coverage.json) (`achieved`). Writers overlap (P and P v2 share their briefs), so the
columns do not add up.

| Service | Servable | Sonnet R | Sonnet P | Sonnet P v2 | Muse Phase 4 | Muse 6b | Covered before 6b | **Covered** | Share of servable |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Box | 60 | 14 | 5 | 5 | 16 | 21 | 35 | **56** | 93% |
| Calendar | 34 | 7 | 3 | 4 | 16 | 10 | 26 | **34** | 100% |
| Linear | 85 | 9 | 18 | 21 | 17 | 35 | 46 | **80** | 94% |
| Slack | 34 | 7 | 14 | 14 | 9 | 3 | 31 | **34** | 100% |
| **All** | **213** | 37 | 40 | 44 | 58 | 69 | 138 | **204** | **95.8%** |

- **Of the whole catalog,** 204 of 255 facts (80%) are covered; the other 42 cannot be served (RQ1).
- **Every covered fact comes from generated scenarios.** Of the 36 facts the hand-built suites tested, 35 are
  covered; the 36th is `H:IssueLabel.parentId` (below).
- **6b** was aimed at 74 uncovered facts and covered 66 of them.
- **Validity costs one fact.** Before the PI's rulings the suites claim 205 facts. `H:IssueLabel.parentId` had
  its only near miss in AR-LIN-25, a scenario the validity review found invalid (the target itself carries the
  label group that the near miss was meant to differ on).

**Table 4. Coverage by kind of fact.** Same source (`by_kind`).

| Kind | Facts | Servable | Covered | Share of servable |
|---|---:|---:|---:|---:|
| A attribute | 142 | 119 | 117 | 98% |
| R relationship | 65 | 51 | 48 | 94% |
| H hierarchy | 9 | 6 | 5 | 83% |
| B binding | 24 | 23 | 22 | 96% |
| D derived | 15 | 14 | 12 | 86% |

**The 9 servable facts left uncovered,** and why:

| Facts | Cause |
|---|---|
| Box `R:Task.item_id`, `R:Task.created_by_id`, `B:Task.item_id`, `D:Task.assignment_count` | Brief G4-BOX-10: the cold reader rejected all 3 rounds |
| Linear `A:IssueLabel.isGroup`, `A:IssueLabel.name`, `R:IssueLabel.teamId`, `D:issue_count` | Briefs G4-LIN-03 (rejected twice, after 7 versions in 6b) and G4-LIN-18 (rejected after 3 rounds) |
| Linear `H:IssueLabel.parentId` | Its only near miss is in the invalid AR-LIN-25 (above) |

Label groups and Box tasks recur: the writer could not build scenarios on them that the reader accepted.

**How the credit is earned.** Same source (`facts_credited_through_form`, `credited_only_through_plain_near_misses`,
`facts_per_family`).

- **Form.** All 204 facts have a near miss in some cover; 202 also in a probe and 94 in a fact probe. For 2 facts
  (`R:Comment.file_id` in G4-BOX-13, `R:ProjectMilestone.projectId` in G4-LIN-01) the credit rests on a cover
  alone. Their probes were dropped because the near miss lost its trap once the target was removed, while the claim
  still passes the check in the cover. All 101 covers pass the reference check again here.
- **Near-miss family.** 167 facts have at least one near miss through a designated substitute (F1–F8). 37 are
  credited only through plain near misses (F0). 30 of those are state attributes, where another value is the
  designated alternative; the other 7 are 5 text attributes, `A:Cycle.number` and `R:IssueRelation.relatedIssueId`.
  Plain near misses expose less often than designated ones (RQ4, RQ8), so these 37 are covered by the rule but
  tested more weakly.
- **Facts per family** (a fact counted once per family it has): F1 81, F0 71, F8 41, F7 38, F2 30, F5 22, F6 13,
  F4 5, F3 1.

## RQ3. How well does the generator perform?

**Table 5. From briefs to valid regular tests, per writer.** Sources: briefs to acceptance and the manual review,
[autogen_01 report](../autogen_01/report.md) §4, [autogen_02 report](../autogen_02/report.md) §6.1–6.2 and
[completion_01](../completion_01/README.md); from scenarios on, [kit/generator.py](kit/generator.py) →
[numbers/generator.json](numbers/generator.json).

| | Sonnet R | Sonnet P | Sonnet P v2 | Muse Phase 4 | Muse 6b | **All** |
|---|---:|---:|---:|---:|---:|---:|
| Briefs | 18 | 16 | 16 | 32 | 26 | **108** |
| Accepted scenarios | 18 | 15 | 16 | 29 | 23 | **101** |
| Rejected (the cold reader never accepted a version) | 0 | 1 | 0 | 2 | 3 | **6** |
| Failed (infrastructure) | 0 | 0 | 0 | 1 | 0 | **1** |
| Versions per accepted scenario, median (max) | 1 (5) | 2 (5) | 2 (6) | 2 (7) | – | |
| Manual review: scenarios valid / flawed but usable / invalid | 16 / 1 / 1 | 11 / 4 / 0 | 15 / 1 / 0 | 24 / 5 / 0 | 21 / 2 / 0 | **87 / 13 / 1** |
| Near misses declared | 67 | 56 | 62 | 99 | 93 | **377** |
| … ruled flawed by the PI (rulings) | 2 | 3 | 2 | 0 | 1 | **8** |
| Regular tests derived (cover, probe, fact probe) | 108 | 84 | 93 | 159 | 138 | **582** |
| … dropped by the witness check | 0 | 3 | 2 | 1 | 1 | **7** |
| … left out by the rulings | 4 | 3 | 2 | 0 | 1 | **10** |
| **Valid regular tests** | **104** | **78** | **89** | **158** | **136** | **565** |
| Facts covered (RQ2) | 37 | 40 | 44 | 58 | 69 | **204** |

- **Acceptance:** 101 of 108 briefs (94%) gave an accepted scenario. A brief is rejected when no version passes
  every check within the round limit; in the recorded cases the cold reader kept finding a problem.
- **Validity:** 100 of 101 accepted scenarios are usable; 1 is invalid (AR-LIN-25). Of all derived tests, 565 of
  582 (97%) are valid. "Flawed but usable" means a contestable near miss or contrived wording; the PI's rulings
  decide what is left out.
- **Sonnet versus Muse** is descriptive only: different briefs, facts, method versions and judges. Muse's scenarios
  had fewer flawed near misses in review (Phase 4: 1 contestable of 99, against 2 to 8 contestable or invalid per
  Sonnet arm).
- **The witness check** drops a probe whose near miss no longer fails its fact once the target is removed. It
  always ran, but its result was ignored until the frozen version of 2026-09-27; the 7 dropped tests would otherwise
  have been run and scored.

**What the automated checks caught before any agent ran.**

- **Per version** (autogen_01's Sonnet arms): 50 versions sent back. Code checks 14 (near misses failing two
  conditions, missing seed arguments, anchors that vanish with the target), replica pre-checks 18 (seeds the
  replica refuses, values no read returns, writes that do not land), the cold reader 18 (undeclared near misses,
  genuine ambiguity such as "my calendar list", unnatural requests).
- **Per scenario** (Muse Phase 4): 14 of 32 sent back by the code checks or pre-checks, 4 by the reader. Of 31
  first drafts, 14 were clean and 17 were sent back, 10 of them for a substantive flaw (baselines_01,
  `machinery.json` on branch `exp/baselines-01`).
- **What no check caught** (found by the manual review or in runs): domain semantics (a Linear label group used as a
  label), fields the acting user cannot read (a calendar's sharing rules), and contrived or ambiguous wording.

**Table 6. Policy variants, written by code and Muse.** Sources: [autogen_02 report](../autogen_02/report.md) §3
and §6.4, [completion_01](../completion_01/README.md).

| Variant | Attempted | Accepted | Declined by the writer | Rejected | Not derivable | Valid in manual read |
|---|---:|---:|---:|---:|---:|---|
| Absence twin (code), Phase 4 | 62 pairs | 61 | – | 1 (code check) | – | – |
| Drop-F, Phase 2 calibration (cal3, on the hand-built scenarios) | 31 derivable | 23 | – | – | – | 22 / 23; 37 / 37 same derivable call as the hand-made variants |
| Drop-F, Phase 4 | 59 | 52 | 4 | 1 (reader) | 2 | – |
| Drop-F, 6b | 70 | 53 | 11 | 5 | 1 | 51 / 53 |
| Clone, Phase 4 | 29 | 25 | 3 | 1 (code check) | – | 11 / 11 reviewed |

- **Policy units on OpenClaw** (RQ6): 255 absence units, 244 valid; 209 underspecified units, 197 valid.
- **A bug the checks missed:** the drop-F derivation named a variant by table and field without the fact's kind, so
  two facts of one column overwrote each other's records. It cost 6b five jobs, derived again, and Phase 4 two
  variants, not recovered because 6a's population had been fixed. Found while assembling 6b; now fixed
  (`variants2.dropf_id`).

**Cost of generation** (Muse, [numbers/costs.json](numbers/costs.json)): writer and reader together, $0.62 per
accepted scenario at list price in Phase 4 and $0.82 in 6b ($0.035 and $0.046 billed); $0.125 per valid regular test
($0.007 billed). Sonnet on the subscription: $1.78 to $5.47 per accepted scenario at list price. §12 has the rest.

## RQ4. What failures do the tests expose in a real agent harness?

The 565 valid regular tests ran on OpenClaw with the self-hosted Qwen3.8-27B, 3 trials each: Box's tests from
`full_02`, the other services' from the opaque-id re-run `full_03`, and 6b's from `full_04`. Every verdict is judge
v2's (RQ5 measures it), under the PI's rulings and the 8-minute budget.

**Table 7. Exposure by service.** Source: [final_regular_with_6b.json](../openclaw_eval_01/runs/final_regular_with_6b.json);
[kit/exposure.py](kit/exposure.py) → [numbers/exposure.json](numbers/exposure.json).

| Service | Tests | Tests exposing a fact | Facts exposed, detect@3 | detect@1 | Facts covered | Share of covered facts exposed (detect@3) |
|---|---:|---:|---:|---:|---:|---:|
| Box | 139 | 39 | 27 | 21 | 56 | 48% |
| Calendar | 103 | 32 | 17 | 12 | 34 | 50% |
| Linear | 213 | 45 | 30 | 19 | 80 | 38% |
| Slack | 110 | 22 | 13 | 8 | 34 | 38% |
| **All** | **565** | **138 (24%)** | **87** | **60** | **204** | **43%** |

**Table 8. Exposure by test form, writer and kind of fact.** Same source.

| | Tests | Exposing | Facts, detect@3 (detect@1) |
|---|---:|---:|---:|
| Cover (target present) | 100 | 12 (12%) | 12 (6) |
| Probe (one near miss, absence permitted) | 363 | 101 (28%) | 79 (55) |
| Fact probe (all near misses of a fact) | 102 | 25 (25%) | 25 (14) |
| Sonnet R | 104 | 24 (23%) | 19 of 37 covered (13) |
| Sonnet P | 78 | 17 (22%) | 12 of 40 (7) |
| Sonnet P v2 | 89 | 18 (20%) | 15 of 44 (10) |
| Muse Phase 4 | 158 | 45 (28%) | 26 of 58 (19) |
| Muse 6b | 136 | 34 (25%) | 22 of 69 (14) |

| Kind of fact | Covered | Exposed, detect@3 | detect@1 |
|---|---:|---:|---:|
| A attribute | 117 | 59 (50%) | 41 |
| R relationship | 48 | 19 (40%) | 13 |
| H hierarchy | 5 | 1 | 1 |
| B binding | 22 | 4 (18%) | 2 |
| D derived | 12 | 4 (33%) | 3 |

- **Probes carry the exposure.** With the target present, the agent picks the right record far more often: 12% of
  covers expose a fact against 28% of probes. Covers are still needed for credit on 2 facts (RQ2) and test the
  write itself.
- **By near-miss family** (probes): designated substitutes 84 of 282 (30%) against plain F0 near misses 17 of 81
  (21%). F8 partial identity (a similar name, a shared prefix) exposes most: 25 of 52 probes (48%); then F1 sibling
  role or attribute 31 of 98 (32%), F7 neighbouring value 13 of 50 (26%), F6 representation 4 of 16, F2 indirection
  6 of 32 (19%), F5 split binding 4 of 28 (14%).
- **Trials:** of 1,695, 254 fail and count (15%), 1,310 pass, 104 ran over the 8-minute budget (no exposure), 14
  failed only on flawed near misses (not counted) and 13 are void.

**Opaque ids matter.** Before the final runs, the Calendar, Linear and Slack tests had seed ids that could name a
record's role. On the same 333 tests, with the same rules and judge, the opaque-id re-run exposes more: 80 tests
against 65 and 48 facts against 42 (Calendar 23 → 25 tests, Linear 23 → 33, Slack 19 → 22). The two runs are a day
apart, not interleaved. Source: [openclaw_eval_01](../openclaw_eval_01/README.md), "Results: the regular suite".

**Reference: the same model in the toy harness.** Qwen on Purdue ran 332 of these tests earlier, with the original
ids, before the rulings; autogen_01's arms were judged by judge v1 (Sonnet), Phase 4 by judge v2. Not comparable
row for row with Table 7. Source: [autogen_02 report](../autogen_02/report.md) §6.3.

| Suite (toy harness) | Tests | Exposing | Facts, detect@3 (detect@1) |
|---|---:|---:|---:|
| Muse Phase 4 (judge v2) | 159 | 37 | 24 of 58 declared (15) |
| Sonnet R (judge v1) | 108 | 18 | 11 (7) |
| Sonnet P (judge v1) | 84 | 25 | 19 (12) |
| Sonnet P v2 (judge v1) | 93 | 14 | 13 (9) |

- **Not measured:** a second model or harness under the same final suite and rules.

## RQ5. How accurate is the automated judge?

Every run had a blind sample: trials drawn at random before the run and labelled by hand before any verdict on them
was read. Outcomes collapse to fail (acted on a wrong record, or presented one as the answer), pass (correct, or
correctly reported absence) and void. TP, FP, FN and TN are counted on trials both call usable; void disagreements
are counted apart.

**Table 9. Judge v2 against the blind labels.** Source: each run's `comparison_blind.json`;
[kit/judge.py](kit/judge.py) → [numbers/judge.json](numbers/judge.json).

| Agent | Tests | Trials | Agree | TP | FP | FN | TN | Void (both) | Judge void only | Label void only | Same facts on TP |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| OpenClaw | regular | 150 | 148 | 20 | 0 | 0 | 127 | 1 | 2 | 0 | 20 / 20 |
| OpenClaw | absence | 155 | 154 | 95 | 0 | 0 | 48 | 11 | 0 | 1 | 95 / 95 |
| OpenClaw | underspecified | 150 | 150 | 80 | 0 | 0 | 58 | 12 | 0 | 0 | 79 / 80 |
| **OpenClaw** | **all** | **455** | **452** | **195** | **0** | **0** | **233** | **24** | **2** | **1** | **194 / 195** |
| Toy harness | regular | 60 | 60 | 10 | 0 | 0 | 50 | 0 | 0 | 0 | 10 / 10 |
| Toy harness | absence | 60 | 55 | 50 | 1 | 0 | 4 | 1 | 0 | 4 | 50 / 50 |
| Toy harness | underspecified | 53 | 52 | 52 | 0 | 0 | 0 | 0 | 0 | 1 | 52 / 52 |
| Toy harness | policy, mixed (Phase 4) | 30 | 30 | 29 | 0 | 0 | 1 | 0 | 0 | 0 | 29 / 29 |
| **Toy harness** | **all** | **203** | **197** | **141** | **1** | **0** | **55** | **1** | **0** | **5** | **141 / 141** |

- **On OpenClaw, no false positive and no false negative** in 428 trials both call usable. With a random sample,
  these are estimates: 0 misses in 195 labelled failures bounds the miss rate below 1.5% (95%, rule of three), and
  0 false alarms in 233 labelled passes bounds that rate below 1.3%.
- **The void disagreements.**
  - Judge void only (2, both regular, the first pass): the judge voided two labelled failures as artifacts. In one,
    the replica reports a group DM as private, which the label missed; the other rests on a near miss the validity
    review marks contestable. Counting both as misses gives recall 195 / 197.
  - Label void only (1): a timed-out trial that changed nothing; the budget makes it a failure either way.
- **Toy harness.** The one false positive is a contested Slack test; the PI ruled for the judge (the acting bot
  counts as a channel member). Every trial of Phase 1 was also labelled by hand (252 trials, not blind): judge v2
  agrees on 239 (95%), and 12 of the 13 misses are trials of 4 policy variants I built with defects.
- **Coverage of the check:** 658 blind trials in all, against 3,033 judge v2 verdicts on OpenClaw and about 1,000
  on the toy harness. The trials the judge did not read are ones the mechanical triage found clean. In `full_02`,
  the judge read 227 such clean trials (its 20% sample and the blind ones) and changed the triage's call on 2
  (baselines_01, ablation 7).

**Table 10. Judges given the same trials.** Source: [judge_baselines_01](../judge_baselines_01/README.md)
(`score.json`); the plain judge from baselines_01 on branch `exp/baselines-01` (`q4/plain_openclaw.score.json`).

| Judge | What it reads | OpenClaw, 178 trials (94 mistakes): precision / recall | Toy harness, 191 blind trials (139 mistakes) |
|---|---|---|---|
| Plain LLM judge | the trial only, no definition of a mistake | 69/75 = 0.92 / 69/94 = 0.73 | not run |
| J0 | the trial and the definition of a mistake | 85/86 = 0.99 / 85/94 = 0.90 | 100/101 = 0.99 / 100/139 = 0.72 |
| J1 | J0 plus the service's domain model | 86/88 = 0.98 / 86/94 = 0.91 | 104/104 = 1.00 / 104/139 = 0.75 |
| **Judge v2** | the test's candidates, a mechanical attribution, policy rules, replica notes | **92/92 = 1.00 / 92/92 = 1.00** (92/94 = 0.98 counting its 2 voids) | **139/140 = 0.99 / 139/139 = 1.00** |

- **The naive judges miss silent failures.** On the toy harness they miss 30% of underspecified failures: the agent
  acted on one of several full matches and said nothing, and without the test's candidates the trial looks right.
  OpenClaw's agent usually discloses the mismatch, which lifts the naive judges' recall to 0.90.
- **Only judge v2 attributes facts.** Exposure (RQ4) needs the fact, not just a mistake.
- **Pipeline cost of judging:** judge v2 reads a trial for $0.03 at list price (§12).

## RQ6. Do policy failures occur per fact or as a policy?

**Why it matters.** A policy test asks what the agent does when the request cannot be met as stated: the record it
presumes is missing (absence), or several records match (underspecified). If the agent fails such requests whatever
the fact at stake, one test per service and mode measures it: 8 tests. If it fails for some facts and not others,
finding which takes a test per fact: up to 408 for the 204 covered facts (RQ1). The decision rule was fixed before
the runs (§0.3). Every valid unit of the generated scenarios ran, 3 trials each.

**Table 11. The eight cells on OpenClaw.** Sources: [decisions_population_absence.json](../openclaw_eval_01/runs/policy/decisions_population_absence.json),
[decisions_population_underspecified.json](../openclaw_eval_01/runs/policy/decisions_population_underspecified.json);
[kit/policy_space.py](kit/policy_space.py) → [numbers/policy.json](numbers/policy.json). The toy harness column is
[autogen_02](../autogen_02/report.md) §5.

| Cell | Valid units | Failing / usable trials | Rate [p10, p90] | Units failing 0 / 1 / 2 / 3 of 3 | **Decision** | First pass (fewer units) | Same model, toy harness |
|---|---:|---:|---|---|---|---|---|
| Box, absence | 60 | 142 / 179 | 0.79 [0.74, 0.85] | 6 / 4 / 11 / 38 | **undecided** | undecided (0.75) | policy-level |
| Calendar, absence | 42 | 104 / 126 | 0.83 [0.77, 0.88] | 3 / 2 / 9 / 28 | **undecided** | not policy-level | policy-level |
| Linear, absence | 99 | 202 / 294 | 0.69 [0.64, 0.74] | 17 / 13 / 14 / 52 | **not policy-level** | not policy-level | policy-level |
| Slack, absence | 43 | 80 / 129 | 0.62 [0.54, 0.70] | 10 / 5 / 9 / 19 | **not policy-level** | not policy-level | policy-level |
| Box, underspecified | 56 | 97 / 167 | 0.58 [0.52, 0.65] | 10 / 15 / 9 / 21 | **not policy-level** | not policy-level | policy-level |
| Calendar, underspecified | 30 | 52 / 90 | 0.58 [0.49, 0.67] | 6 / 7 / 6 / 11 | **not policy-level** | not policy-level | policy-level |
| Linear, underspecified | 79 | 120 / 236 | 0.51 [0.45, 0.57] | 25 / 10 / 19 / 24 | **not policy-level** | not policy-level | policy-level |
| Slack, underspecified | 32 | 79 / 96 | 0.82 [0.75, 0.89] | 2 / 3 / 5 / 22 | **undecided** | undecided (0.80) | policy-level |

- **The same model is policy-level in all eight cells in the toy harness, and in none on OpenClaw:** five cells are
  shown not policy-level and three are undecided with every unit used. The harness changes the answer.
- **In the toy harness** Qwen almost never stopped: it acted on a near miss in about 95% of absence trials, and it
  asked or listed the matches without acting once in 435 underspecified trials. One absence test and one
  underspecified test per service carried the whole result there.
- **On OpenClaw** the failure rate depends on the unit: every cell has units that fail 3 of 3 and units that never
  fail.
- **Readings other than the fixed one** (the same file, `readings`): if a unit counts as failing when any of its 3
  trials fails, Box absence, Calendar absence and Slack underspecified become policy-level and the others stay
  undecided or not; if a unit must fail all 3, every cell is not policy-level.
- **The 8-minute budget changes no decision.** With over-budget trials left as the judge called them, the rates are
  0.77, 0.82, 0.61, 0.60 (absence) and 0.49, 0.46, 0.41, 0.77 (underspecified).
- **Writers differ.** In both Calendar cells, units from Muse's scenarios fail more often than units from Sonnet's:
  absence 0.90 (Phase 4) and 0.96 (6b) against 0.64; underspecified 0.71 and 0.53 against 0.37.

**Table 12. The per-fact policy space.** Same source (`totals`, `regular_vs_policy_facts`, `by_source`).

| | Absence | Underspecified | Both |
|---|---:|---:|---:|
| Requirements (one per covered fact) | 204 | 204 | 408 |
| Units derived (every fact of every scenario) | 255 | 209 | 464 |
| Valid units, all run and judged | 244 | 197 | 441 |
| Facts with a valid unit | 197 | 173 | 370 (91% of 408) |
| Facts failing at least one trial (detect@3) | 169 | 140 | 309 |
| Facts failing the first trial (detect@1) | 145 | 111 | 256 |
| … of those with a unit: also exposed by a regular test | 82 | 62 | |
| … failing the policy unit only | 87 | 78 | |
| … exposed by a regular test only | 2 | 12 | |
| … neither | 26 | 21 | |

- **Units exceed requirements** because a fact can have near misses in several scenarios; the unit is the scenario's
  fact. Some facts have no valid unit (a derivation not possible, a variant declined or ruled invalid).
- **The same facts show up in both kinds of test.** Of the facts a regular test exposes, almost all also fail their
  absence twin (82 of 84). Another 87 facts pass every regular test but fail when the request presumes the record:
  the agent can check the fact when it may report absence, and does not when the request presumes a match.
- **Per-fact counting of policy failures.** A policy failure is attributed to the fact of the near miss acted on
  (absence) or of the condition dropped (underspecified), exactly as in regular tests. The totals above count facts,
  not failing tests.
- **Muse's Phase 4 scenarios alone** (for comparison with the baselines, RQ8): 60 absence units over 56 facts, 45
  failing; 50 underspecified units over 52 facts, 41 failing.

**Answer to RQ6.** For Qwen in the toy harness the policy tests collapse to 8. For the same model in OpenClaw they
do not: failures depend on the fact, and a per-fact policy space of about 400 tests is what finds them. On this
agent it found absence failures on 169 facts and underspecified failures on 140 (309 fact and mode pairs at
detect@3, 256 at detect@1).
