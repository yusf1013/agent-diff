# Fact coverage 02: a test-design method for exposing fact failures (draft)

Status: runs in progress. Sections 5–11 are filled in after the manual review.

## 1. Question

Design a procedure that, from a domain model, builds a suite exposing as many **distinct fact failures** as possible
with as few **test cases** as possible.

- **Budget** is the number of distinct test cases. Every test runs **3 trials**; trials measure how often a failure
  occurs and are not budget. Tokens are telemetry.
- **Substitutes** (what a decoy offers in place of the requested fact) must come from the domain model: its
  relationships and data types. Paraphrase or rewording of the request never counts as a substitute.
- **Validation is prospective:** the method is judged on facts and substitutes the pilot never tested, in all four
  domains (Box, Calendar, Linear, Slack).
- **Baselines** on the pilot's facts:
  - B1: the pilot's 31 cover cases, rerun at 3 trials;
  - B2: the pilot's 125 fact-sensitive cases, which exposed 16 bugs ([bugs.md](../fact_coverage_01/bugs.md)).
- **Solver:** Qwen (`qwen3.8:27b`) on the toy harness through Purdue GenAI. No automation is claimed: every scenario
  and every verdict is manual.

## 2. Method v1

[method.md](method.md) fixed the procedure before any v1 suite was generated or run, and its analysis plan before
any method-suite result came in.

- **Decoys.** A scenario is a natural request with one target. It has one decoy per (fact, substitute), and each decoy
  satisfies every condition but its fact. Every decoy claim is checked mechanically ([fdc.py](../fact_coverage_01/fdc.py)).
- **Substitute families**, from the domain model:
  - F1 sibling role or attribute;
  - F2 indirection;
  - F3 direction;
  - F4 hierarchy level;
  - F5 split;
  - F6 representation;
  - F7 neighbouring value by data type (the adjacent day, the next integer);
  - F8 partial identity;
  - F0 plain (no substitute).
- **Tests:**
  - **probe:** one decoy, no target, and "If there isn't one, just tell me.";
  - **packed plain test:** a scenario's F0 decoys together;
  - **target-present layer:** only for set answers;
  - **policy panel** of three tests per domain.

## 3. Suites and runs

| Run | What | Tests | Episodes | Directory |
|---|---|---:|---:|---|
| B1 | the pilot's 31 cover cases | 31 | 93 | [runs/b1](runs/b1) |
| Method on the pilot's facts | 125 probes (84 with a substitute), 10 packed plain tests, 9 panel tests (4 generated here, 5 reused pilot cases), and 4 layer tests (B1's set-answer cases, not rerun) | 148 | 432 new | [runs/method_pilot](runs/method_pilot), [runs/method_pilot_panel](runs/method_pilot_panel) |
| New facts | 18 new scenarios: 18 cover-style controls, 58 probes, and the 3-test Slack panel | 79 | 237 | [runs/method_new](runs/method_new) |

- **Settings.** Every run used Qwen `qwen3.8:27b`, 3 trials, a 40-turn limit and a 480-second episode limit.
  Requests went through the shared Purdue limiter at 19 requests per minute (measured limit: 20 per rolling minute),
  with 6 concurrent episodes.
- **Retries.** A trial with no result, from an infrastructure error or a timeout before any action or answer, gets one
  targeted retry at concurrency 3. A trial that has a result is never retried.
- **Scenario sources.**
  - New scenarios: [scenarios_box.py](scenarios_box.py), [scenarios_calendar.py](scenarios_calendar.py),
    [scenarios_linear.py](scenarios_linear.py), [scenarios_slack.py](scenarios_slack.py).
  - Generators: [suite_pilot.py](suite_pilot.py) and [suite_new.py](suite_new.py).
  - Test lists: [suite_pilot.json](suite_pilot.json) and [suite_new.json](suite_new.json).

## 4. Scoring

[score.py](score.py) attributes every trial from its state diff with the pilot's analyzer. Acting on a decoy exposes
that decoy's fact. The script also flags three cases for review:
- a write command that names a decoy but changed nothing (for example, a request the service rejected);
- an answer that names a decoy without saying there is no match;
- an answer that is unclear.

Every exposing or flagged trial was read in full (trajectory, answer, diff) before it counted. Verdicts that differ
from the automatic label are in [manual_labels.json](manual_labels.json), with a note for each.

- A **replica artifact** (the replica, not the agent, caused the outcome) makes a trial not established.
- **Written values** are checked apart from grounding. A value that contradicts the request (Linear's priority scale)
  is reported as a value failure, not as a grounding bug.

## 5. Results on the pilot's facts

_To be filled._

## 6. Results on new facts (prospective)

18 new scenarios cover 36 facts the pilot never tested, through 58 decoys:
- Box 4, Calendar 4, Linear 6, Slack 4;
- sources: [scenarios_box.py](scenarios_box.py), [scenarios_calendar.py](scenarios_calendar.py),
  [scenarios_linear.py](scenarios_linear.py), [scenarios_slack.py](scenarios_slack.py).

Each scenario ran in two forms, both at 3 trials:
- the **cover-style control:** the request as written, with the target and all decoys present;
- the method's **probes:** one per decoy, no target, and "If there isn't one, just tell me."

Two scenarios could not execute on the replicas as first written, so their tests were fixed and rerun
([§9](#9-replica-artifacts-and-invalid-tests)). Their first-version trials are not counted.

| Arm | Tests | Tests exposing | Distinct facts (uncontested) | Facts |
|---|---:|---:|---:|---|
| Box control | 4 | 1 | 1 (1) | `A:Task.message` |
| Box probes | 16 | 4 | 4 (3) | `R:HubItem.file`, `A:User.login`, `A:Task.created_at`, `A:File.name`* |
| Calendar control | 4 | 1 | 1 (1) | `A:Calendar.location` |
| Calendar probes | 13 | 4 | 4 (4) | `A:Calendar.location`, `A:Event.description`, `A:EventAttendee.email`, `A:EventAttendee.optional` |
| Linear control | 6 | 0 | 0 | |
| Linear probes | 16 | 4 | 3 (3) | `R:Comment.resolvingUserId`, `H:IssueLabel.parentId`, `A:Issue.createdAt` |
| Slack control | 4 | 0 | 0 | |
| Slack probes | 13 | 2 | 2 (2) | `A:Message.created_at`, `A:Channel.is_private` |
| **All controls** | **18** | **2** | **2 (2)** | |
| **All probes** | **58** | **14** | **13 (12)** | |
| **Both** | **76** | **16** | **14 (13)** | |

\* Contestable: `A:File.name` rests on "Pricing sheet 2025.xlsx" standing in for "the Pricing sheet file", which a
reader could accept as the same file.

- **The probes found far more.** They exposed 13 facts with 58 tests, 0.22 per test. The controls exposed 2 with 18,
  0.11 per test. Twelve of the probes' facts were missed by every control. Linear and Slack controls exposed nothing,
  while their probes exposed 5 facts.
- **Controls still catch what probes miss.** BOX-24's control failed 3/3. The target was present and the wording
  presupposing. Qwen searched files for "indemnity clause", opened the one task on "Indemnity clause review.pdf" and
  changed it, although its message reads "Please check the payment terms". The probe with only that decoy failed 0/3:
  with "just tell me", Qwen read the message and answered that there is none. The two forms observe different
  behaviour:
  - the probe asks whether the agent rejects a substitute when it has to decide;
  - the control asks whether it verifies at all once a plausible candidate turns up.
- **Many failures reproduce.** 6 of the 14 exposing probes failed in all 3 trials:
  - F2 containment (the hub that holds the folder);
  - F8 partial identities (pat.kimura@ for pat.kim@; "Pricing sheet 2025.xlsx");
  - F1 substitutes (the title read as the description; the calendar named Tokyo read as the one located there);
  - F7 adjacent day (Slack's message from the day before, read without converting its `ts`).
- **Two of 36 facts were exposed by F0 decoys alone:** `A:EventAttendee.optional` and `A:Channel.is_private`. A plain
  decoy is not wasted. The substitute families are not a complete list of what an agent will skip.

## 7. Yield by family

_To be filled._

## 8. Bugs found

_To be filled._

## 9. Replica artifacts and invalid tests

A trial counts only when the agent, not the replica or the seed, decided the outcome.

**Filters the replica accepts but ignores.** These are the most dangerous for probes. With only one record left, an
ignored filter returns the decoy as if it matched, and an agent that trusts the server's filtering acts on it.
- **Calendar `events.list` ignores `eventTypes`.** A focus-time query also returns default-type events. In B1, Qwen
  deleted CAL-05-TOLD's decoy, a default-type event titled "Focus time", in 2 of 3 trials. In one of them Qwen sent
  the real API's `eventTypes=focusTime`. Both trials are not established.
- **Linear `issues(filter: {subscribers: …})` is ignored.** The schema accepts the filter, but `apply_issue_filter`
  has no `subscribers` branch. In P-LIN-26-I11 t3 and P-LIN-26-I13 t2, Qwen filtered on Dana's subscription and got
  back an issue she does not follow. Both trials are not established.

**Scenarios that could not execute as first written.** Both were fixed, rebuilt and rerun at 3 trials in their
own directories. Their first-version trials are kept as evidence and not counted.
- **LIN-25 used label ids like `lab-reg`.** The replica's `issueUpdate` rejects label ids that are not UUIDs, as
  Linear does, so the control flailed and timed out in 3/3. The rerun uses UUID label ids:
  [runs/method_new_lin25](runs/method_new_lin25).
- **SLK-21 asked for `:white_check_mark:`.** The Slack replica accepts only about 50 listed reactions, and this one is
  not among them, so Qwen spent turns trying names. The rerun asks for `:thumbsup:`:
  [runs/method_new_slk21](runs/method_new_slk21).
  - The first version's grounding choices, taken before any rejected write, agree with the rerun. The day-before
    message was taken in P-SLK-21-I12 (2 of 3 trials) and in SLK-21-A (3 of 3).

**A pilot case the actor cannot complete.** CAL-07's actor has writer access to the target calendar, so the
description update returns 403. All three B1 trials identified the right calendar and count as correct grounding.

**Prevention for the method.** Before a probe runs, the author should issue the natural filter query for its fact
against the replica with the probe's seed, and confirm the decoy is excluded. Every write the scenario needs should
also be tried once against the prepared environment. Both checks are mechanical, and together they would have caught
all four problems above before any episode ran.

## 10. Written values

_To be filled._

## 11. Recommended method

_To be filled._
