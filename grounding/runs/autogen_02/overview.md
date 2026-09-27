# Automated grounding tests for AI agents: the system and what it found

*For a reader new to the project. Written 2026-09-27 from the autogen_02 study's data, after all its runs; every
number below comes from the committed runs ([report.md](report.md) and [tables.md](tables.md) give the details and
sources). A page version with a worked example is [overview_page.html](overview_page.html), published privately at
https://claude.ai/artifact/4gLmexguQrsvYEp2AcuMz5.*

## 1. The problem

AI agents that work in business tools (Box, Google Calendar, Linear, Slack) must act on **exactly the record the
user means**. The common failure is quiet: the agent acts on a record that is *almost* right, such as the budget sync
instead of the budget review, or another Maya's file. We call this a **grounding** failure. This project builds
tests that catch it, automatically, and runs them against an agent in replicas of the four services.

- **The replicas:** AgentDiff, a copy of each service's API over a seeded database, isolated per test.
- **The agent under test:** Qwen 3.8 (27B), through Purdue's GenAI Studio.

## 2. The kinds of test

Every test is a request plus a seeded world. The world holds the **target** (the record the request means) and
**near misses**: records that match all but one condition, each failing on one *fact*.

| Test | The request | The right behaviour | A failure shows |
|---|---|---|---|
| **Cover** | fits exactly one record; near misses around it | act on the target only | the agent cannot tell apart the fact of the near miss it picked |
| **Probe** | the target removed, one near miss left, plus "If there isn't one, just tell me" | say there is none | the same, for that one fact |
| **Fact probe** | the target removed, all near misses of one fact left, plus the escape clause | say there is none | the same |
| **Absence twin** (policy) | a probe **without** the escape clause: the request presumes the record exists | say there is none | the agent acts on something rather than report absence |
| **Underspecified** (policy) | two or more records match fully: one condition dropped ("drop-F"), or the target copied ("clone") | ask which one | the agent picks one, or all, without asking |

The first three are **regular tests**, one per fact. The last two are **policy tests**: they measure what the agent
does when the request cannot be met as stated. The research question for them is whether the agent fails *per fact*
(it depends on what differs) or as a *policy* (it fails whatever the fact). If it is a policy, one test per service
is enough, and testing every fact is redundant.

## 3. The space to cover

| | Box | Calendar | Linear | Slack | All |
|---|---:|---:|---:|---:|---:|
| **Facts in the catalog** | 60 | 40 | 121 | 34 | **255** |
| Left out: the replica cannot serve them | 0 | 6 | 36 | 0 | 42 |
| **Covered by at least one near miss** | 35 | 26 | 47 | 31 | **139 (55%)** |

- **By kind of fact:** attribute 142 (79 covered), relation 65 (32), binding 24 (14), derived 15 (10),
  hierarchy 9 (4).
- **What automation covers:** all 139 covered facts come from automatically generated scenarios. The 36 that
  hand-made scenarios cover are all among them. Of the 213 facts the replicas can serve, that is 65%.
- **The policy space:** 2 policy tests × 4 services = **8 cells**, each sampled over the facts of the generated
  scenarios (below).

## 4. The system

| Step | Done by | Checked by | Measured quality |
|---|---|---|---|
| Brief → scenario (request, seed, target, near misses) | an LLM writer (Muse) | code checks; the replica runs the seed; a second LLM reads it cold and must find the target | 29 of 32 accepted; 24 of 29 valid in a human review (0 invalid) |
| Scenario → regular tests (covers, probes, fact probes) | code | code (each near miss must fail exactly its fact) | a probe can lose its trap when the target is removed: 1 of 62 fact pairs |
| Absence twins | code | the same code check | 61 of 62 pairs |
| Underspecified, drop-F | code chooses the condition and computes the matches; the LLM rewords the request | code word checks; the reader must find exactly the intended matches | 52 of 59 accepted; valid in human review: 22 of 23 (calibration), 42 of 43 and 28 of 28 (later); 3 of all 159 degenerate |
| Underspecified, clone | the LLM describes a copy of the target; code builds it | code; the reader | 25 of 29 accepted; 11 of 11 valid in review |
| Sampling and decisions | code: a random order fixed by a seed, looks at 11/18/25 tests | pre-registered before any run | – |
| Running the agent | Qwen on Purdue, 3 trials per test | – | 90 to 170 trials an hour (limit: ~20 requests a minute) |
| Judging | an LLM judge (Muse, "judge v2") | a human grades random trials blind, before seeing the judge | agreement 95% on the first 252 trials; on later blind samples 87/93 (90/93 after a ruling on one contested test), then 110/110 |
| People | review scenarios and variants before their runs; grade blind samples; rule on contested tests | – | 455 trials graded by hand |

**Cost:**
- **One scenario:** $0.62 at list price ($0.035 billed).
- **All LLM work in the study** (writer, reader, judge, including development): $148 at list price, $9.47 billed,
  over 3,093 calls.
- **The agent runs:** 1,356 trial attempts, 10,802 requests, about 10 hours of Purdue time.

## 5. How much ran

| | Scenarios | Tests | Trials on Qwen |
|---|---:|---:|---:|
| Hand-made (earlier study), policy tests built per fact | 18 | 84 | 252 |
| autogen_01's generated scenarios (Sonnet), policy tests sampled | 49 | 125 twins, 107 drop-F, 44 clones available | 195 absence, 183 underspecified |
| New scenarios (Muse), regular tests | 29 | 159 | 477 |
| New scenarios, policy tests (the first 14) | 14 | 67 | 201 |

## 6. Results

### 6.1 Policy tests: Qwen fails as a policy, in every service

| Cell | Absence: tests failing | Decision | Underspecified: tests failing | Decision |
|---|---:|---|---:|---|
| Box | 11/11 | policy-level | 11/11 | policy-level |
| Calendar | 11/11 | policy-level | 11/11 (robust: 17/17) | policy-level |
| Linear | 11/11 | policy-level | 17/18 | policy-level |
| Slack | 23/25 (29/32 over all run) | policy-level | 11/11 (robust: 17/17) | policy-level |

- **The rule, fixed before any run:** a cell is policy-level when we are 90% confident that a test on a random
  fact fails more than 80% of the time. 11 of 11 is the least that shows it.
- **Checks:**
  - Three decisions rested on a test found flawed or contested. A robustness run, declared in advance, confirmed
    two; a ruling settled the third (the acting bot counts as a Slack channel member).
  - The new scenarios' own policy tests confirm all eight: 88 of 90 absence trials and 106 of 108 underspecified
    trials fail.
- **So:** for this agent, one absence test and one underspecified test per service carry the whole result.

### 6.2 Regular tests: the new scenarios catch the agent

| Suite | Tests | Facts exposed (failed in at least one trial) | Facts per test |
|---|---:|---:|---:|
| New scenarios, batch 1 (Muse) | 72 | 19 of 29 | 0.26 |
| New scenarios, batch 2 (Muse) | 87 | 5 of 30 | 0.06 |
| **New scenarios, both** | **159** | **24 of 58** | **0.15** |
| autogen_01, three arms (Sonnet) | 108 / 84 / 93 | 11 / 19 / 13 | 0.10 / 0.23 / 0.14 |

- **The comparison is rough:** the suites test different facts and were graded by different judge versions.
- **Difficulty varies widely by scenario:** batch 2's scenarios came from the same process as batch 1's, yet Qwen
  passes nearly all of them (no Slack test in batch 2 exposes anything).

### 6.3 What the agent does

- **It almost never asks.** Qwen asked "which one?" once in 435 underspecified trials. Given several matches, it acts
  on the first it finds (93 of 129) or on all of them (30), and often says nothing about the others.
- **It acts under presumption.** Without the escape clause, it acts on a near miss in about 95% of absence trials.
  With the clause, it often reports the absence. For 14 of 30 new facts, it passes the probe and fails the twin:
  it can check the fact, and does not when the request presumes a match.
- **When it fails a missing target** (169 failures graded by hand):
  - it misread the deciding field in 37%;
  - it **saw the mismatch and acted anyway** in 34% ("likely a typo", "the closest match", "clearly the one you
    meant");
  - it never checked the field in 22%.
- **It changes the world to fit the request:**
  - it unarchived a channel so that it could invite someone to "the channel that hasn't been archived";
  - it created a missing team and issue;
  - it posted the "approved for launch" comment the request described as already there.
- **Its one reliable check:** who posted a Slack message, and where. Those absence tests pass 9 of 9.
- **Recurring slips:**
  - it misreads Linear's priority numbers: it writes 4 (Low) for Urgent and reads 2 (High) as Medium;
  - it trusts a text search that cannot see message cards;
  - it assumes a date instead of checking it.

### 6.4 The judge

On random trials a person graded before seeing its verdicts, the LLM judge agrees in 87 of 93 on the first policy
runs, then in 110 of 110.
- **The disagreements:** in 3 of the 93, the project lead later ruled the judge right and the person wrong: the
  Slack bot does count as a channel member. That makes 90 of 93.
- **As a failure detector:** when it says "fail" it is right 88 of 89 times, and it finds every failure the person
  found.
- **Its one weakness:** it cannot tell a flawed test from a failing agent.

## 7. What the automation gets wrong, and the fixes

| Defect | How often | Found by | Fix |
|---|---|---|---|
| A drop-F variant whose verb implies the dropped condition ("hide" a calendar not in the list) | 3 of 159 | a person, while grading | derive action preconditions from each service's API, or try the action on each intended match in a replica copy |
| A probe loses its trap when the target is removed | 1 of 62 new pairs; in autogen_01's, the same check finds 2 more of this kind, and 1 where the near miss becomes a full match | a person, while grading | run the existing witness check on every probe |
| A fact relative to "today" (overdue) with no date set | 1 scenario | a person | pin the date, or flag such facts |
| A count that changes with the acting bot ("exactly four members") | 1 test | a person | flag counts the acting account can change |
| Seed fields that contradict the request (events in LA time on a New-York-time calendar) | 1 scenario | a person | check the seed's other fields against the conditions |
| A request that parses two ways ("the folder owned by ...") | 1 scenario | a person | a reader question about attachment |
| The clone copier cannot copy rows two steps from the target | 1 of 29 | code | copy along two-step links |

Every defect but the last slipped past both the automated checks and the human pre-run review. A person found each
of them while grading trials by hand: human grading is still the system's safety net.

## 8. The replicas

11 issues are documented in [replica_issues.md](replica_issues.md), 4 of them new:
- a Box bug: updating a file unshares it;
- Slack's history returns thread replies;
- Slack's search ignores card text;
- only Calendar has a fixed "today".

Linear's failing `projects` query and nested reads cause every timeout in the new scenarios' runs (21 of 21).

## 9. What these results do not cover

- **One agent.** Every result is for Qwen 3.8 (27B). Another agent may fail differently, or not as a policy.
- **Three kinds of test left out of scope:**
  - requests meant to reach several records ("tag all of Maya's PDFs");
  - requests the service cannot do;
  - attributing *why* a failure happened. The judge assigns a mechanism, but this is not validated.
- **42 of the 255 facts** cannot be tested until the replicas serve them (36 in Linear, 6 in Calendar).
- **The judge cannot tell a flawed test from a failing agent,** so the system still needs a person to review and
  grade samples.
- **Scenario difficulty varies widely.** Two batches from the same process exposed 0.26 and 0.06 facts per test.
  One batch is not enough to rate a writer.
