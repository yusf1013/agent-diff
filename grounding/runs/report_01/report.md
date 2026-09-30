# Automated fact-discrimination tests for tool-using agents: evaluation and results

*A stub for the evaluation and results sections of a paper, written 2026-09-29 from the committed runs and brought
to the rebuilt numbers on 2026-09-30 (the 10-minute budget, duplicate policy units, blind_review_01; every change is
logged in [README.md](README.md), "Text changes"). It covers the experiments, what they show and what they do not.
There is no introduction, background or related work. Every table names its source: a script in [kit/](kit/) and the
JSON it writes into [numbers/](numbers/), or a run record. Rows marked "–" or "not measured" are measurements not yet
made.*

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
- **The 10-minute budget.** A trial that OpenClaw's own 600-second turn limit ends, or whose agent time,
  rate-limiter waits excluded, passes 600 s, is the agent's failure. For a policy unit it counts as failing; in a
  regular test it exposes no fact. Every final run used that limit; an earlier reading of 8 minutes (trials past 8
  minutes counted as timed out) was withdrawn on 2026-09-29.
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
| **Main evaluation subtotal** | **4,464** | **287.6** | **44,575** | **550M** | **14.3M** |

- Agent hours add up each trial's agent time; trials ran 24 to 48 at a time.
- Median trial: 152 to 282 s depending on the run.
- **Kept apart:** `full_01` (578 trials, stopped when the harness was found to leak the test's identity, §10) and
  three smoke runs (17 trials).
- **The toy harness** (earlier studies, reference only): 1,356 trial attempts and 10,802 requests
  ([autogen_02 overview](../autogen_02/overview.md) §4).

**Self-hosted Qwen token accounting across this report (audited 2026-09-29).** The subtotal above omits
RQ8's fresh baseline and ablation runs. [kit/qwen_usage.py](kit/qwen_usage.py) →
[numbers/qwen_usage.json](numbers/qwen_usage.json) reads the original proxy request metadata, checks the
self-hosted Qwen/OpenClaw configuration, and reconciles it with each execution summary. No new model calls.

| Scope | Trial attempts | Model requests | Input tokens | Output tokens | Combined tokens |
|---|---:|---:|---:|---:|---:|
| Main regular and policy evaluation (opening table) | 4,464 | 44,575 | 549,836,059 | 14,285,364 | 564,121,423 |
| RQ8: N0, N1, N0M, N1M, cycle2 and plain48 | 1,020 | 7,488 | 89,314,308 | 1,792,608 | 91,106,916 |
| **All reported OpenClaw result runs** | **5,484** | **52,063** | **639,150,367** | **16,077,972** | **655,228,339** |
| Stopped `full_01` and the three smoke runs, kept apart | 595 | 3,601 | 44,405,460 | 1,298,576 | 45,704,036 |
| Including stopped and smoke runs | 6,079 | 55,664 | 683,555,827 | 17,376,548 | 700,932,375 |

- Input counts the prompt and accumulated context on every request, including **564,216,576 cached input
  tokens** in the reported result runs (88.3% of input). The provider also reports 55,297,088 cache-creation
  tokens. These are input details, not extra tokens to add. Output includes 9,613,752 reasoning tokens.
- **Recorded lower bounds:** 247 of the 52,063 result-run requests have no returned usage (232 main, 15 RQ8).
  Three baseline trial attempts have no model request metadata. The stopped/smoke group has another 19 requests
  without usage and six attempts without request metadata; their consumption is not estimated.
- The result-run metadata agrees exactly with the saved usage summaries. The stopped run has 18 unfinished
  summaries whose surviving request metadata adds 1,190,158 input and 37,904 output tokens absent from `scale.json`.
- Reused trials in judge comparisons and ablations count once; fresh reruns count again. Generation and judging
  models are excluded, as are all toy-harness runs, including step 5's self-hosted Qwen runs in RQ9.

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
  credited only through plain near misses (F0). Under the F0 rule (roadmap, 2026-09-29), a plain difference is the
  designated alternative where the domain model names no other, which covers 36 of the 37:
  - 30 state attributes, where another value is the alternative;
  - 4 facts for which the domain model names no lure: Box `A:Hub.description`, Linear `A:Document.content` and
    `A:Team.description`, Slack `A:User.title`;
  - 2 whose lure the 2026-09-28 rulings make flawed, so a plain near miss is their only valid form: Linear
    `A:Cycle.number` (a cycle *named* "Cycle 4" can be what a user means) and Slack `A:Message.message_text` (Slack
    shows a message's blocks).

  The 37th, Linear `R:IssueRelation.relatedIssueId` (the related issue's direction), has only a plain near miss
  although the domain model names a lure; it is being regenerated with its lure (regen_01). Plain near misses expose
  less often than designated ones (RQ4, RQ8).
- **Facts per family** (a fact counted once per family it has): F1 81, F0 71, F8 41, F7 38, F2 30, F5 22, F6 13,
  F4 5, F3 1.

## RQ3. How well does the generator perform?

**Table 5. From briefs to valid regular tests, per writer.** Sources: briefs to acceptance and the manual review,
[autogen_01 report](../autogen_01/report.md) §4, [autogen_02 report](../autogen_02/report.md) §6.1–6.2 and
[completion_01](../completion_01/README.md); from scenarios on, [kit/generator.py](kit/generator.py) →
[numbers/generator.json](numbers/generator.json).

| | Sonnet R | Sonnet P | Sonnet P v2 | Muse Phase 4 | Muse 6b | **All runs** |
|---|---:|---:|---:|---:|---:|---:|
| Briefs run | 18 | 16 | 16 | 32 | 26 | **108** |
| Accepted scenarios | 18 | 15 | 16 | 29 | 23 | **101** |
| Rejected (no version accepted) | 0 | 1 | 0 | 2 | 3 | **6** |
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

- **Acceptance:** 101 of 108 brief runs (94%) gave an accepted scenario. The runs overlap: P v2 reran P's 16 briefs
  and 6b reran 3 of Phase 4's (G4-BOX-02, G4-CAL-08, G4-LIN-03). Of the 89 distinct briefs, 86 have an accepted
  scenario and 3 never did (G4-BOX-10, G4-LIN-18, G4-LIN-03). A brief is rejected when no version passes every check
  within the round limit; in the cases whose record gives the reason, the cold reader kept finding a problem.
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
  `grounding/runs/baselines_01/machinery.json`).
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

- **Policy units on OpenClaw** (RQ6): 255 absence units, 244 valid; 209 underspecified units, 197 valid. Two
  underspecified pairs are one request each (U-AP-SLK-03 and U-G4-LIN-14, `openclaw_eval_01/rulings.py`,
  `DUPLICATE_UNITS`): both of each pair ran, and RQ6's statistic counts each pair once, so its underspecified
  denominator is 195 units.
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
v2's (RQ5 measures it), under the PI's rulings and the 10-minute budget.

**Table 7. Exposure by service.** Source: [final_regular_with_6b.json](../openclaw_eval_01/runs/final_regular_with_6b.json);
[kit/exposure.py](kit/exposure.py) → [numbers/exposure.json](numbers/exposure.json).

| Service | Tests | Tests exposing a fact | Facts exposed, detect@3 | detect@1 | Facts covered | Share of covered facts exposed (detect@3) |
|---|---:|---:|---:|---:|---:|---:|
| Box | 139 | 39 | 27 | 21 | 56 | 48% |
| Calendar | 103 | 34 | 17 | 13 | 34 | 50% |
| Linear | 213 | 47 | 31 | 19 | 80 | 39% |
| Slack | 110 | 23 | 13 | 8 | 34 | 38% |
| **All** | **565** | **143 (25%)** | **88** | **61** | **204** | **43%** |

**Table 8. Exposure by test form, writer and kind of fact.** Same source.

| | Tests | Exposing | Facts, detect@3 (detect@1) |
|---|---:|---:|---:|
| Cover (target present) | 100 | 12 (12%) | 12 (6) |
| Probe (one near miss, absence permitted) | 363 | 105 (29%) | 80 (56) |
| Fact probe (all near misses of a fact) | 102 | 26 (25%) | 26 (14) |
| Sonnet R | 104 | 24 (23%) | 19 of 37 covered (13) |
| Sonnet P | 78 | 18 (23%) | 13 of 40 (7) |
| Sonnet P v2 | 89 | 19 (21%) | 15 of 44 (10) |
| Muse Phase 4 | 158 | 47 (30%) | 26 of 58 (20) |
| Muse 6b | 136 | 35 (26%) | 23 of 69 (14) |

| Kind of fact | Covered | Exposed, detect@3 | detect@1 |
|---|---:|---:|---:|
| A attribute | 117 | 59 (50%) | 42 |
| R relationship | 48 | 20 (42%) | 13 |
| H hierarchy | 5 | 1 | 1 |
| B binding | 22 | 4 (18%) | 2 |
| D derived | 12 | 4 (33%) | 3 |

- **Probes carry the exposure.** With the target present, the agent picks the right record far more often: 12% of
  covers expose a fact against 29% of probes. Covers are still needed for credit on 2 facts (RQ2) and test the
  write itself.
- **By near-miss family** (probes): designated substitutes 88 of 282 (31%) against plain F0 near misses 17 of 81
  (21%). F8 partial identity (a similar name, a shared prefix) exposes most: 25 of 52 probes (48%); then F1 sibling
  role or attribute 34 of 98 (35%), F7 neighbouring value 13 of 50 (26%), F6 representation 5 of 16, F2 indirection
  6 of 32 (19%), F5 split binding 4 of 28 (14%).
- **Trials:** of 1,695, 267 fail and count (16%), 1,348 pass, 52 were ended by the 10-minute budget (no exposure),
  14 failed only on flawed near misses (not counted) and 14 are void.

**Opaque ids matter.** Before the final runs, the Calendar, Linear and Slack tests had seed ids that could name a
record's role. On the same 333 tests, with the same rules and judge, the opaque-id re-run exposes more: 84 tests
against 70 and 48 facts against 44 (Calendar 23 → 27 tests, Linear 26 → 34, Slack 21 → 23). The two runs are a day
apart, not interleaved. Source: [full_02.adjudicated.json](../openclaw_eval_01/runs/full_02.adjudicated.json) (the
original ids) and [full_03.adjudicated.json](../openclaw_eval_01/runs/full_03.adjudicated.json), `by`.

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
| *OpenClaw, AI reference labels (blind_review_01)* | all forms, final runs | 132 | 128 | 68 | 4 | 0 | 51 | 9 | 0 | 0 | 68 / 68 |

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
  agrees on 239 (95%), and 12 of the 13 misses are trials of 4 hand-built policy variants with defects.
- **A second reference review (blind_review_01, the last row).** Codex labelled 200 of the 2,705 final executions
  that had no earlier label (seeded, stratified by service and form; 185 distinct cases), with PI decisions affecting 12
  of them, and locked the labels before seeing any verdict or mechanical score. These are **AI
  reference labels, not a second human annotator.** The pipeline (judge v2 where it read the execution, mechanical
  triage otherwise) agrees on 186 of 190 executions both call non-void (68 TP, 4 FP, 0 FN, 118 TN); judge v2 alone on
  119 of 123; triage alone on 67 of 67 (all passes). Exposed facts agree on all 68 joint failures. The 4 false
  positives follow from three interpretation questions the PI settled before unblinding, where the judge read the
  request more strictly. Case-cluster bootstrap 95% intervals for exact agreement, weighted to the eligible pool:
  96.1% to 99.5% (pipeline) and 94.3% to 99.3% (judge). One execution stays uncertain by the PI's choice. Sources:
  [blind_review_01](../blind_review_01/README.md), `numbers.json`, `uncertainty.json`, `report.md`.
- **Coverage of the check:** 658 blind trials in all, against 3,033 judge v2 verdicts on OpenClaw and about 1,000
  on the toy harness, plus blind_review_01's 200 final executions. The trials the judge did not read are ones the mechanical triage found clean. In `full_02`,
  the judge read 227 such clean trials (its 20% sample and the blind ones) and changed the triage's call on 2
  (baselines_01, ablation 7).

**Table 10. Judges given the same trials.** Source: [judge_baselines_01](../judge_baselines_01/README.md)
(`score.json`); the plain judge from baselines_01 (`grounding/runs/baselines_01/q4/plain_openclaw.score.json`).

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
| Box, absence | 60 | 132 / 171 | 0.77 [0.71, 0.83] | 6 / 4 / 10 / 33 | **undecided** | undecided (0.75) | policy-level |
| Calendar, absence | 42 | 101 / 124 | 0.82 [0.75, 0.87] | 4 / 1 / 8 / 27 | **undecided** | not policy-level | policy-level |
| Linear, absence | 99 | 160 / 263 | 0.61 [0.55, 0.67] | 21 / 12 / 9 / 35 | **not policy-level** | not policy-level | policy-level |
| Slack, absence | 43 | 75 / 125 | 0.60 [0.52, 0.68] | 10 / 5 / 5 / 19 | **not policy-level** | not policy-level | policy-level |
| Box, underspecified | 56 | 71 / 145 | 0.49 [0.42, 0.56] | 11 / 12 / 6 / 13 | **not policy-level** | not policy-level | policy-level |
| Calendar, underspecified | 30 | 37 / 81 | 0.46 [0.36, 0.56] | 8 / 5 / 3 / 8 | **not policy-level** | not policy-level | policy-level |
| Linear, underspecified | 78 | 83 / 205 | 0.41 [0.34, 0.47] | 25 / 10 / 5 / 17 | **not policy-level** | not policy-level | policy-level |
| Slack, underspecified | 31 | 63 / 82 | 0.77 [0.69, 0.84] | 2 / 3 / 4 / 12 | **undecided** | undecided (0.80) | policy-level |

Two underspecified pairs are one request each (RQ3), so each pair counts once: Linear 79 → 78 and Slack 32 → 31
valid units, the pair's trials pooled. The spread counts units with exactly 3 usable trials. The first-pass column
is the first pass's own record, not recomputed.

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
- **The budget reading changes no decision.** Under the withdrawn 8-minute reading the rates were 0.79, 0.83, 0.69,
  0.62 (absence) and 0.58, 0.58, 0.51, 0.82 (underspecified), with the same eight decisions.
- **Writers differ.** In both Calendar cells, units from Muse's scenarios fail more often than units from Sonnet's:
  absence 0.88 (Phase 4) and 0.96 (6b) against 0.64; underspecified 0.64 and 0.27 against 0.23.

**Table 12. The per-fact policy space.** Same source (`totals`, `regular_vs_policy_facts`, `by_source`).

| | Absence | Underspecified | Both |
|---|---:|---:|---:|
| Requirements (one per covered fact) | 204 | 204 | 408 |
| Units derived (every fact of every scenario) | 255 | 209 | 464 |
| Valid units, all run | 244 | 197 (195 with each duplicate pair once) | 441 (439) |
| … with a usable trial | 240 | 189 | 429 |
| Facts with a valid unit | 197 | 173 | 370 (91% of 408) |
| Facts failing at least one trial (detect@3) | 159 | 113 | 272 |
| Facts failing the first trial (detect@1) | 131 | 81 | 212 |
| … of those with a unit: also exposed by a regular test | 79 | 54 | |
| … failing the policy unit only | 80 | 59 | |
| … exposed by a regular test only | 6 | 21 | |
| … neither | 32 | 39 | |

- **Units exceed requirements** because a fact can have near misses in several scenarios; the unit is the scenario's
  fact. Some facts have no valid unit (a derivation not possible, a variant declined or ruled invalid).
- **The same facts show up in both kinds of test.** Of the 85 facts that a regular test exposes and that have an
  absence unit, 79 also fail it. Another 80 facts pass every regular test but fail when the request presumes the
  record: the agent can check the fact when it may report absence, and does not when the request presumes a match.
- **Per-fact counting of policy failures.** A policy failure is attributed to the fact of the near miss acted on
  (absence) or of the condition dropped (underspecified), exactly as in regular tests. The totals above count facts,
  not failing tests.
- **Muse's Phase 4 scenarios alone** (for comparison with the baselines, RQ8): 60 absence units over 56 facts, 43
  failing; 50 underspecified units over 52 facts, 32 failing.

**Answer to RQ6.** For Qwen in the toy harness the policy tests collapse to 8. For the same model in OpenClaw they
do not: failures depend on the fact, and a per-fact policy space of about 400 tests is what finds them. On this
agent it found absence failures on 159 facts and underspecified failures on 113 (272 fact and mode pairs at
detect@3, 212 at detect@1).

## RQ7. What do the trials show outside the grounding criterion?

The criterion and judge v2 grade one thing: which record the agent acted on. A trial can pick the right record and
still do harm: write a wrong value, change fields or records the request never mentioned, or create what the
request presumed. None of this counts in RQ4 or RQ6. We measured it mechanically from each trial's state diff and
read every flagged trial by hand. Source: [kit/beyond.py](kit/beyond.py) → [numbers/beyond.json](numbers/beyond.json)
(its `examples` list the trials). Trials: the 1,695 of the regular suite's final score and the 1,323 of the policy
populations (the first pass's looks for Box's units).

**Table 13. Values written, against the value the request states.** Checked where the value can be read off the
request without interpretation.

| Field (the request says) | Regular: writes checked | Wrong | Policy runs: writes checked | Wrong |
|---|---:|---:|---:|---:|
| Linear priority ("…to Urgent") | 58 (31 on the target) | **42 (23 on the target)** | 91 | **63** |
| Linear estimate ("estimate to 5") | 58 | 0 | 75 | 0 |
| Box tag ("Add the tag X") | 105 | 0 | 198 | 0 |
| Slack reaction ("a :tada: reaction") | 45 | 0 | 74 | 0 (1 ambiguous: asked for a "check" reaction, which names no exact emoji; wrote "done") |
| Slack archive or unarchive | 14 | 0 | 15 | 0 |
| Calendar hide | 21 | 0 | 17 | 0 |

- **One systematic value error: Linear's priority scale, read upside down.** Linear stores Urgent as 1 and Low as 4.
  Asked for Urgent, the agent wrote 4 (Low) in 37 of the regular suite's 42 wrong writes, 0 (no priority) in 2, and
  3 (Medium) for High in 2. Over all runs, 105 of 149 priority writes (70%) are wrong. The step-5 study found the
  same on its own tests (31 of 39 passed Linear priority trials), and so did fact_coverage_02 (7 of 14).
- **The right record with the wrong value passes.** 23 cover trials set the priority of the right issue to the wrong
  value, and 22 of them count as correct: the triage cleared 16 without the judge, and the judge graded 6 correct,
  with notes such as "The written priority 4 is Low not Urgent, but a wrong value on the target does not change the
  outcome". The 23rd is incorrect because it also wrote a near miss.
- **Judge v2's notes** mention a wrong value or scale in 76 of its 3,033 OpenClaw verdicts (13 graded correct), a side
  effect in 2 and a false claim to the user in 2. It reports what it sees but, as instructed, grades grounding only.

**Writes the request did not ask for** (each flagged trial read by hand):

| What the agent did | Regular | Absence | Underspecified | Example |
|---|---:|---:|---:|---|
| Created the record the request presumed | 3 | 10 | 2 | Asked to tag "the PDF … with a top-level comment by Dana Whitfield saying 'approved for launch'", it tagged a PDF and posted that comment itself (Box, 14 trials); created the attachment it was asked to rename (Linear, 1) |
| Changed the record to fit the request | – | 2 | – | Asked for "the issue assigned to the active human admin", it reassigned a bot's issue to the admin, then set the estimate, and said so |
| Changed other fields on the record, disclosed | 2 | – | – | Hid a calendar and also unchecked it |
| Changed other fields, harmful | – | 1 | – | Moving a meeting to Room 5B, it also moved it from 10:00 to 17:00 (a time-zone error) and reset the attendees' replies, then reported the old time |
| Other small writes | 2 | – | – | Opened a Slack DM; set a document icon |
| Acted on a record outside the test's declared set | 0 | 4 | 0 | Hid "Team Calendar", a calendar that is not one of the near misses |
| Wrote a record, then restored it | 6 | 3 | 4 | Renamed the wrong team, noticed, renamed it back |
| **Trials writing anything** | **547 of 1,695** | **466 of 732** | **251 of 591** | |

- **The presumption habit shows here too.** In RQ6 the agent acts on a near miss when the request presumes a record;
  here it sometimes makes the presumption true instead (17 trials), by posting the comment, creating the attachment
  or reassigning the issue.
- **Replica effects, not the agent's:** Box's replica clears a file's shared link and lock when an update omits
  them. 32 trials show such a change; it is a replica defect, recorded, not scored.
- **Not measured:** values whose request needs interpretation (dates, free text, colours, time zones), except where a
  flagged trial showed one; a check of disclosure (whether the final reply reports what was written).

## RQ8. Baselines and ablations

A separate study, baselines_01 (branch `exp/baselines-01`, `grounding/runs/baselines_01/report.md` and
`compare.json`), compares our tests with what a coding agent writes when asked directly, and removes parts of our
system one at a time. Everything below ran on the same agent (OpenClaw, Qwen3.8-27B, k = 3). Each baseline trial was
labelled by hand before any assertion result or judge verdict was read; one person labelled.

### 8.1 Two baselines

- **B1, "ask your coding agent" (N0):** Muse Code in a sandbox, given the goal in plain words, the API docs the agent
  under test gets, how to seed records, the table list and AgentDiff's assertion format. 48 tests, 12 per service.
- **B2, B1 plus our fact catalog (N1).**
- **Mutated twins (N0M, N1M):** B1 and B2 again with the fixes a reviewer would ask for first ("each test a different
  property", "challenging but passable", "neutral ids").
- **Ours:** Muse's Phase 4 tests, as expected values over random draws of 12 per service from its 158 tests, on the
  first pass (`full_02`). Phase 4's final score is close: 45 tests exposing and 26 facts, against 41 and 28 in the
  first pass.

**Table 14. Baselines against ours, per 48 tests.** Source: baselines_01 `compare.json`, `policy_facts.json`,
`oracles.score.json`; our policy row from [numbers/policy.json](numbers/policy.json) (`by_source`).

| | B1: N0 | B1 + fixes: N0M | B2: N1 | B2 + fixes: N1M | Ours (Phase 4) |
|---|---:|---:|---:|---:|---:|
| Tests / valid | 48 / 45 | 48 / 42 | 48 / 41 | 48 / 41 | 48 of 158, all valid |
| Near misses through a designated substitute (F1–F8) | 9 of 48 | 17 of 53 | 21 of 58 | 19 of 66 | 81 of 99 |
| Facts exercised properly (credit rule), valid tests | 7 | 12 | 17 | 13 | 34.0 |
| **Facts exposed, fact-sensitive tests (detect@3 / detect@1)** | **0 / 0** | **0 / 0** | **0 / 0** | **0 / 0** | **11.0 / 7.2** |
| Failing tests (detect@3), and their kind | 5, all presupposing | 0 | 2, presupposing | 3: 2 presupposing, 1 a timeout without a write | 12.5, all fact-level |
| Policy-level facts, designated near misses only (baselines_01's count) | 0 / 0 | 0 / 0 | 1 / 1 | 0 / 0 | – |
| Policy-level facts, any near miss failing one fact (our rule) | 4 / 3 | 0 / 0 | 2 / 2 | 1 / 0 | – |
| Own oracle on its valid trials: precision / recall | 0.54 / 0.70 (assertions) | 0 real, 21 false | 0.27 / 1.00 | 0.03 / 1.00 | 1.00 / 1.00 (judge v2) |
| Generation cost per 48 tests, list (billed) | $0.51 ($0.03) | $1.20 ($0.06) | $0.67 ($0.03) | $1.14 ($0.06) | $5.44 ($0.31) |

- **Asked plainly, a coding agent writes tests that expose no fact,** with or without our catalog, with or without
  the reviewer's fixes: 0 facts from 169 valid baseline tests. 48 of ours expose about 11.
- **Its failing tests are policy failures.** Every failing baseline trial that wrote something acted on a request that
  presupposes a record that does not exist; the one other failing test (N1M) is a timeout without a write. Counted
  as raw failing tests, B1 (5) would look productive; counted as facts, it is not.
- **Policy-level failures counted by fact.** Our policy tests count the fact of the near miss acted on (RQ6), so the
  baselines' presupposing tests should too. Our own Phase 4 policy units, with every one run: 60 absence units over
  56 facts, 45 failing (39 through designated near misses); 50 underspecified units over 52 facts, 41 failing (38).
  These are not per 48 tests: our regular suite has no presupposing tests, and the policy units are generated
  apart.
- **A counting difference we found in the baseline study.** It counts a plain near miss (F0) as exposing its fact in
  probe form (ablation 3 below), but as "no fact" in presupposing form. Our pipeline credits any near miss that fails
  exactly one fact, whatever its family (RQ2: 37 facts are credited through plain near misses alone). Counting the
  baselines' failures on plain near misses by the facts their labels name gives the second policy row: B1 4 facts
  (A:File.tags, A:Issue.title, A:Event.start, R:Event.calendar_id), B2 2 (D:overdue,
  R:TaskAssignment.assigned_by_id), N1M 1. Either way the baselines' fact-sensitive exposure stays 0.
- **Their oracles:** AgentDiff assertions written by the coding agent report mostly false failures (7 real of 22 for
  N0, 6 of 40 for N1, after removing our harness's errors), and report failures on every invalid test.
- **Value errors** (outside scope, as in RQ7): N0's assertions caught 7 wrong-value trials on the right record, mostly
  Linear's priority scale; the plain judge caught 3 and J0 none.

### 8.2 Six ablations of our system

**Table 15.** Source: baselines_01 (`cycle2/labels.json`, `plain48/score.json`, `machinery.json`,
`q4/numbers.json`, `q4/plain_openclaw.score.json`); judge_baselines_01 `score.json`.

| # | What is removed or swapped | Result |
|---|---|---|
| 3 | **The probe form** (target present instead) | N0's own near misses: 0 of 36 tests expose a fact as covers; as probes, 4 of 28 tests (4 facts at detect@3, 3 at detect@1), 7 of 83 trials |
| 4a | **The designated substitute** (only the lure removed, same probe), 12 probes that had exposed a fact | Failing trials 27/36 against 7/36 (21/30 against 2/30 without 2 confounded pairs); pairs failing 12/12 against 3/12; facts at detect@3 10 against 1 |
| 4b | The same, on 48 probes drawn at random (plain48) | Probes failing 14/48 against 2/48; failing trials 29/144 against 3/144; pairs failing in one version only 13 against 1, sign test p = 0.002; facts 14 against 2 (detect@1 10 against 1). Counting 3 timeouts as failures: 15 against 4 probes, p = 0.007 |
| 5 | **Probes in our own suite** (first pass, 436 tests) | Covers 2 of 77 tests expose a fact; probes 76 of 279; fact probes 16 of 80. Within probes, designated near misses 67 of 223, plain 9 of 56. The final score shows the same (RQ4) |
| 6 | **The machinery** (checks, replica pre-checks, cold reader): first drafts against accepted | Phase 4: 14 of 31 first drafts clean; 17 sent back, 10 for a substantive flaw and 7 for format; all 81 autogen briefs: 38 first drafts clean |
| 7 | **The LLM judge** (mechanical triage alone), `full_02`'s 1,314 trials | Triage clears 957 (73%) and flags 184 of the 189 final failures (97%). The judge voided 11 of triage's failures as artifacts, resolved 143 uncertain trials as correct, and changed 2 of 227 sampled clean ones |
| 8 | **The judge's inputs**: plain judge, J0, J1 against judge v2, on 178 hand-labelled OpenClaw trials | Precision / recall: plain 0.92 / 0.73; J0 0.99 / 0.90; J1 0.98 / 0.91; judge v2 1.00 / 1.00 (0.98 counting its 2 voids). On regular tests alone, judge v2 and J0 6 of 8, the plain judge 2 of 8 |

- **Form and content multiply.** The probe form lifts plain near misses from nothing to about 15% of tests; the
  designated substitute doubles that across the suite, and within one test it carries 9 of 10 exposures.
- **The machinery keeps flawed tests out:** a third of first drafts had a substantive flaw.
- **The answer key does most of the judging.** Triage alone flags 97% of failures; the LLM judge settles the rest
  and removes artifacts.
- **Not measured:** baselines for the policy tests (the baselines wrote no underspecified test); baselines for the
  extensions in RQ9; a second agent under test.

## RQ9. Two extensions: several matches, and requests beyond the agent's capabilities

Two studies from branch `exp/automation-01` (source commit 5b87399356, now merged into main) automate methods first worked out by hand:
`grounding/runs/several_match_auto_01/` and `grounding/runs/boundary_auto_01/`, each with `summary.py` →
`summary.json` and `report.md`. **They ran on the self-hosted Qwen3.8-27B in the toy harness, not in OpenClaw,**
3 trials per test, with timeouts counted as failures.

**Neither adds a coverage dimension.** Several-match tests are one more test form over the same catalog facts, and
their traps (a copy of the target in a hidden calendar, past a page, in another folder) are construction choices,
like near-miss families. Capability boundaries are a separate requirement space, linked to the catalog the way the
policy panel is.

### 9.1 Several matches: plural requests

- **The form.** A plural request ("tag every PDF that…") over a cover's world with the target and extra full matches.
  *Easy:* the copies are in plain view. *Hard:* one copy sits where a lazy route misses it (another folder, a hidden
  calendar, a private channel, past the first page). The cover's near misses stay and are checked again.
- **Generated:** 91 single-target covers in; the Muse writer judged 65 worth a plural request; 131 tests (101 first
  builds, 17 repairs, 13 from later rounds). **Valid: 103** (63 easy, 40 hard): the cold reader picks exactly the
  targets, the fact check still holds, the thorough route finds every target, the trap is practical, and the seed
  installs.
- **In FDC terms:** the 103 valid tests exercise 99 catalog facts (Box 29, Calendar 21, Linear 30, Slack 19), all
  servable and all already covered by single-target covers. They add no coverage, and 13 facts are exposed through
  near misses acted on (10 firm; 3 rest on near misses the reader or the upstream wording makes contestable).
- **Trials:** 309, 8 voided on review, 23 timeouts counted as failures.

**Table 16. Targets found, by where the extra match was placed** (valid tests; timeouts and voided trials out).

| Placement | Found |
|---|---:|
| Plain view | 708 / 731 |
| One folder down | 5 / 5 |
| Another folder | 2 / 2 |
| Another calendar the user owns | 7 / 21 |
| Hidden calendar or private channel | 2 / 26 |
| Past the first page | 58 / 65 |
| Text lacking the search words | 10 / 10 |

- **This is a policy, not a fact.** The misses follow the route, whatever the facts: with no calendar named, the
  agent reads the primary calendar only, in all 7 calendar covers: a copy in a hidden calendar was found 0 of 21
  times. Slack's default channel list missed a private channel's copy 3 of 5 times, and Linear sometimes reads one
  page (5 covers). Box walks folders and pages. There was no clear
  case of stopping early and no filter failure. We report it like the policy panel's collection request
  ([criterion.md](../fact_coverage_01/criterion.md)), once per service, not per fact.
- **The judge against review:** 84 failures reported on valid tests, 76 true and 8 false (3 replica artifacts, 5
  near misses the reader itself doubted); no false negative in 225 passes. This is not a blind comparison: 13 were
  read by hand, and the others follow from construction or the timeout rule. The judge does not check values: in 31
  of 39 passed Linear trials that name a priority, the agent wrote the wrong one (RQ7).
- **Manual phase before it** (`several_match_02`): 4 covers, trap reach 12 of 23; the automation reaches 11 of 23 on
  the same covers and reproduces the findings. Plural probes (no target) exposed nothing in 41 trials and were
  dropped.
- **Cost:** 144 Muse calls, $7.26 at list price ($0.52 billed).

### 9.2 Capability boundaries: requests the actor cannot carry out

- **The requirement space.** From the catalog: for each of the 255 facts, can the acting user change it, through which
  operation and under what precondition, plus preconditions of operations not tied to a field. This gives 152
  elements; checked on the replicas, **93 are faithful** (27 unfaithful, 12 replica gaps, 6 uncertain, 14 not a
  boundary). 88 of the 93 come from a catalog fact (80 distinct facts); 5 are operation-level. By class: read-only
  field 32, permission 31, no such operation 15, state precondition 13, value limit 2.
- **The test.** A natural request that needs the missing capability, naming the record, with no hint of the limit.
  Right behaviour: report the limit. Failures: substituting another change, re-creating the record, or claiming
  success.
- **Generated:** 93 tests, 89 valid (the cold reader: the named record, no hint, natural wording); 10 reworded in a
  second round, all valid: **90 of 93 boundaries** have a valid test.
- **Results:** 49 of 89 boundaries fail at least once; 116 of 261 graded trials fail (44%). Wording matters: round 1's
  "Show X as…" requests read as display requests; reworded as "Make X…", the same 10 boundaries fail 23 of 30 trials
  against 15 of 30.
- **The judge against hand labels** (a seeded random quarter of the trials, drawn before the verdicts, plus every
  flagged trial): failures 21 true, 1 false; passes 42 true, 1 false negative, and 2 more pending a PI ruling on
  undone writes. The generated oracle specs agree with the hand-written ones on 272 of 275 manual-phase trials.
- **Not an FDC exposure.** A boundary failure is the answer to an impossible request, not a confusion between facts.
  It is keyed to its source fact ("80 catalog facts carry a faithful write limit") and counted in its own space.
- **The 42 unservable facts are a different axis:** only 4 of the 152 elements touch them (the Calendar sharing-rule
  limit).
- **Cost:** 179 Muse calls, $5.42 at list price ($0.38 billed).

**Caveats for both** (from the studies): one agent, and the toy harness; the self-hosted model was shared with other
sessions (13 to 38 s per turn); replica gaps voided some trials (Linear's null connections, Box folder listings that
ignore `fields`); two upstream covers are contestable (AR-LIN-24's "Cycle 4", G4-CAL-06's "Leo Park's calendar").
**Not measured:** either extension on OpenClaw, and baselines for either.

## 10. Lessons

### 10.1 How the agent fails

**Table 17. Failure mechanisms in the hand labels** (OpenClaw's blind samples). Source:
[kit/mechanisms.py](kit/mechanisms.py) → [numbers/mechanisms.json](numbers/mechanisms.json). Judge v2 records the same
mechanisms on every failing trial it reads ([numbers/exposure.json](numbers/exposure.json)).

| Mechanism | Regular (22 failures) | Absence (95) | Judge v2, all 254 counted regular failures |
|---|---:|---:|---:|
| Saw the mismatch and acted anyway | 13 | 74 (78%) | 156 (61%) |
| Never checked the deciding field | 5 | 12 | 63 (25%) |
| Checked it and misread it | 4 | 9 | 35 (14%) |

- **Seeing is not stopping.** OpenClaw's agent usually inspects the deciding field, reports the difference, and acts
  on the closest record anyway ("likely a typo", "the only match"). The same model in the toy harness failed
  differently (169 hand-graded failures on a missing target): misread 37%, saw and acted 34%, never checked 22%.
- **Underspecified requests:** in 58 of 138 usable blind trials (42%) the agent asked which match was meant, which is
  right. Otherwise it acted on one match or on all of them, usually disclosing the others afterwards. In the toy
  harness it asked once in 435 trials.
- **What bites:** near misses by partial identity (a similar name, a shared prefix) expose in 48% of their probes;
  sibling roles or attributes 32%; neighbouring values 26%; plain near misses 21% (RQ4). Attributes are exposed more
  often than bindings (50% against 18% of covered facts).
- **Habits beyond grounding** (RQ7): Linear's priority scale read upside down in 70% of priority writes; making a
  presumed record true (posting the comment the request describes, reassigning an issue to the named person);
  occasional harmful side effects.
- **Time:** 104 of 1,695 regular trials ran past the 8-minute budget, as did 188 of 1,170 policy-population trials;
  some agents debug a replica error until the limit (§10.4).

### 10.2 What the harness does to the measurement

- **The harness changes the answer more than the tests do.** The same model is policy-level in all eight cells in
  the toy harness and in none in OpenClaw (RQ6).
- **Harnesses can leak the test.** OpenClaw wrote its state folder's path, which held the case id and the benchmark's
  name, into every system prompt. In the stopped `full_01`, 43% of trials remarked on being tested, some reading the
  test's form from its id. An anonymous state folder and a guard on every attempt's first request fixed it.
- **The agent still notices tests.** Remarks on a trap, a decoy or a test appear in 25.6% of `full_02`'s trials,
  19.9% of `full_03`'s (opaque ids) and 22.8% of `full_04`'s ([numbers/awareness_full_03.json](numbers/awareness_full_03.json),
  [awareness_full_04.json](numbers/awareness_full_04.json)); in the toy harness, 11 of 221 and 1 of 261 trials.
- **Ids that name roles hand over the answer.** Opaque ids raised exposure on the same 333 tests from 65 to 80 tests
  (RQ4).
- **Some tests are right only on some days.** "On Tuesday", "overdue" and "the next milestone" need the agent's clock
  set; the date check first missed one of them.

### 10.3 What building the tests taught

- **Enforce every check.** The witness check ran from the start, but its result was ignored until the frozen
  version: 7 tests would have run with no trap.
- **Automated checks do not replace a reader.** Domain semantics, fields the actor cannot read and contrived wording
  reached the manual review; 8 near misses and 1 scenario were ruled out by the PI.
- **Covers rarely expose; probes do.** A generator that writes only target-present tests finds almost nothing on
  this agent (RQ8).
- **Identifiers need a collision check.** The drop-F derivation silently lost 7 variants to a naming collision.

### 10.4 Replica defects found (reported, not fixed)

- Linear: `documentUpdate` and `attachmentUpdate` apply the change but answer with an error, and agents then debug
  until the time limit; several nested connections return null (projects, comment children, team cycles, cycle
  issues, attachments).
- Box: an update that omits the shared link or the lock clears it; folder listings ignore `fields`; search ignores
  `ancestor_folder_ids` and `file_extensions`; `DELETE /tasks` fails and `/task_assignments` is missing.
- 38 catalog facts are replica gaps (RQ1).

## 11. Threats to validity

- **One model.** Qwen3.8-27B, in two harnesses. No second model ran the final suite.
- **One labeller.** The same person wrote the blind labels, the validity reviews and the variant reads. Labels were
  written before the verdicts, but there is no second annotator and no inter-rater agreement.
- **Judge validation is a sample.** 455 of about 3,000 OpenClaw verdicts have a blind label. The bounds in RQ5 hold for
  the sampled runs.
- **Rulings made by the team.** The PI ruled on contested near misses after the first pass had been seen; the rulings
  are recorded and applied by code, and change coverage by 1 fact.
- **The 8-minute budget was applied after the runs,** which ran with a 10-minute limit. No policy decision changes
  without it.
- **The opaque-id comparison is not same-day.** The two runs are a day apart on the same self-hosted server.
- **Replicas are not the services.** 42 facts cannot be served, and replica artifacts void some trials.
- **Writers are confounded.** Sonnet and Muse differ in briefs, method version and judge; comparisons are descriptive.
- **Coverage includes weak credit.** 37 facts are credited through plain near misses only, and 2 through a cover
  only.
- **Test awareness** at about 20% of trials may change the agent's behaviour in either direction.
- **Baselines** are 48 tests per arm with one labeller and one agent.
- **The extensions** ran on the toy harness only.

## 12. Cost

**Table 18. Model spend by component** (list price; billed in brackets). Source: [kit/costs.py](kit/costs.py) →
[numbers/costs.json](numbers/costs.json), from every `calls.jsonl` on this branch; other branches from their reports.

| Component | Calls | List | Billed |
|---|---:|---:|---:|
| Muse: scenario generation (writer and cold reader) | 331 | $36.74 | $2.08 |
| Muse: policy variants (drop-F wording and reader, clones) | 1,291 | $54.42 | $3.44 |
| Muse: drop-F and clone calibration | 446 | $21.23 | $1.36 |
| Muse: judge v2 on OpenClaw trials | 3,037 | $89.53 | $6.21 |
| Muse: judge v2 on the toy harness's trials | 1,067 | $46.23 | $3.12 |
| Muse: development (smoke tests, judge v1 on Muse, settings checks) | 450 | $20.09 | $1.34 |
| Muse: judge baselines J0 and J1 | 1,228 | $34.50 | $2.41 |
| **Muse, this branch** | **7,850** | **$302.74** | **$19.96** |
| Muse: baselines_01 (generation $3.53, judges $21.36) | 814 | $24.89 | $1.78 |
| Muse: step 5's automation (several matches $7.26, boundaries $5.42) | 323 | $12.68 | $0.90 |
| Sonnet 5 on the Claude Code subscription (autogen_01, all runs) | 1,421 | $208.02, plus $13.61 in failed calls | $0 |
| Agent under test: self-hosted Qwen (main evaluation only; full token accounting in §0.4) | 44,575 requests | no per-call charge | 287.6 agent-hours |

**Unit costs (Muse, list price; billed in brackets):**

| Unit | Cost |
|---|---:|
| Accepted scenario (writer and reader) | $0.62 (Phase 4), $0.82 (6b); ($0.035, $0.046) |
| Valid regular test | $0.125 ($0.007) |
| Judge v2 verdict on an OpenClaw trial | $0.029 ($0.002) |
| Judging per OpenClaw trial run (4,464) | $0.020 ($0.0014) |
| Baseline test (B1, B2), for comparison | $0.011 to $0.014 at list |

- **Muse is billed at about 6.6% of its list price.** Muse's part of the OpenClaw evaluation (its scenarios, all
  policy variants, and judging) comes to $181 at list price and $11.73 billed.
- **Not measured:** GPU cost of the self-hosted agent; the people's time for reviews and labels.

## 13. Not yet measured

| Measurement | Status |
|---|---|
| A second model and harness on the final suite | – |
| Baselines for the policy tests (neither baseline wrote an underspecified test) | – |
| The several-match and boundary extensions on OpenClaw | – |
| Baselines for the extensions | – |
| A second annotator on the blind samples | – |
| Value checks for dates, free text and time zones (RQ7) | – |
| Disclosure: does the final reply report what was written? | – |
| The 9 servable facts left uncovered (label groups, Box tasks) | – |
| Phase 4's 2 drop-F variants lost to the naming bug | – |
| The full baseline comparison proposed in baselines_01 | – |
