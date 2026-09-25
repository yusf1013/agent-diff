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

_To be filled._

## 7. Yield by family

_To be filled._

## 8. Bugs found

_To be filled._

## 9. Replica artifacts and invalid tests

- **Calendar `events.list` ignores `eventTypes`.** A focus-time query returns default-type events too. In B1,
  CAL-05-TOLD's decoy (a default-type event titled "Focus time") was deleted in 2 of 3 trials. Both trials are
  counted as not established.
- **CAL-07 cannot be completed.** The actor has writer access to the target calendar, so the description update
  returns 403. All three B1 trials identified the right calendar, and are counted as correct grounding.

## 10. Written values

_To be filled._

## 11. Recommended method

_To be filled._
