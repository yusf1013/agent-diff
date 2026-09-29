# twin2: the mutated twins of N0 and N1

**Question (PI, 2026-09-28):** do the naive fixes a reviewer would ask about first close the gap between the
baselines and our approach? "Did you tell it to test different properties? To make the tests challenging? To make
them passable?" A mutated twin is a baseline rerun with those lines added to its prompt and nothing else changed.

## Design

- **Arms:** N0M is N0 ("ask your coding agent") plus the lines; N1M is N1 (N0 plus our facts document) plus the same
  lines. 12 tests per service, 48 per arm, as in round 1.
- **The added paragraph** (the PI's lines, verbatim in both arms, after the request for 12 tests):

  > Make sure each test checks a different property. Make the tests challenging: a careless assistant should fail
  > them, but a perfect assistant must be able to pass them. Use neutral ids that do not reveal which record is the
  > right one.

- **The corrected format document.** Round 1's had three errors of ours (log, 21:29–21:45): an `"unchanged"` diff
  type the engine rejects, a promise that "similar bookkeeping columns" are ignored, and no word that a changed
  column left out of `expected_changes` fails the assertion. The twins' version names the engine's diff types, lists
  the ignored columns, and states the rule. It is a correction of our harness, not advice on test design; round 1 is
  compared through its rescoring under what its document said (`assertions.faithful.json`), so the fix is not
  credited to the lines.
- **Sessions:** as in round 1, one Muse session per service writes all 12 tests together (**pending the PI's
  choice:** (a) a new session, recommended, or (b) the round-1 session resumed, with the lines as a follow-up and a
  request to revise).
- **Everything else as round 1:** OpenClaw with the self-hosted Qwen, 3 trials, 12 or fewer in flight; my review
  under the fixed rules ([n0/review_rules.md](../n0/review_rules.md)) before any run; hand labels before any
  assertion result; the tests' own assertions evaluated with `assertions.py --twin`. No LLM judges: they do not bear
  on this question.

Inputs: `python grounding/runs/fact_coverage_02/launch.py grounding.runs.baselines_01.twin2.make_inputs` writes
`n0m/inputs/` and `n1m/inputs/`; they differ from round 1's only in `task.md` (the paragraph) and `format.md` (the
fixes).

## Prediction (written 2026-09-28 at 22:16, before any generation)

Round 1's values are in brackets (N0, N1).

1. **Exposure, the main one.** Each twin exposes at most 2 distinct facts at detect@3 in its 48 tests [0, 0]; ours
   expose about 11 per 48. Most failing tests remain the absence policy.
2. **The reason.** Each twin keeps the right record present in at least 34 of 48 tests [39, 40], and writes at most
   3 tests with no right record and absence permitted, our probe form [0, 0].
3. **Look-alikes.** The share of near misses through a designated substitute: N0M at most 25% [19%]; N1M between
   25% and 50% [36%].
4. **Variety** (`variety.py`). N0M: at least 38 distinct deciding details [32] and at most 12 tests only reusing
   one [20 of 42]. N1M: about N1's [46; 9].
5. **Validity.** Invalid tests: N0M at most 3 [3], N1M at most 4 [7]. The "perfect assistant" line removes the
   impossible requests; details the API does not show and replica gaps can remain.
6. **Their own checks.** The false alarm that expects a deleted Box item or Calendar event to disappear (both
   services keep it, trashed or cancelled) recurs wherever a twin writes such a test; a request that lacks a needed
   detail falls to at most 1 test.

**Fixed now:** if a twin exposes 3 or more facts, an unchanged fresh repeat of that baseline runs before any
conclusion, to separate the lines from session luck. The lines are not tuned on the results; each arm is generated
once (with the generator's one repair turn for tests that do not load, as in round 1).

## Result (runs 2026-09-28 23:06 to 2026-09-29 00:31; labels before any check result)

288 trials on OpenClaw with the self-hosted Qwen, all labelled by hand ([n0m labels](n0m/runs/gen_01/labels.json),
[n1m labels](n1m/runs/gen_01/labels.json)); numbers from [compare.json](../compare.json).

| 48 tests each | N0 | N0M | N1 | N1M |
|---|---:|---:|---:|---:|
| Near misses through a designated substitute | 9 of 48 | 17 of 53 | 21 of 58 | 19 of 66 |
| Facts exercised properly (valid tests) | 7 | 12 | 17 | 13 |
| Distinct deciding details; tests only reusing one | 32; 20 | 38; 17 | 46; 9 | 51; 13 |
| Right record present; our probe form | 39; 0 | 44; 0 | 40; 0 | 44; 0 |
| Invalid tests | 3 | 6 | 7 | 7 |
| **Facts exposed (detect@3)** | **0** | **0** | **0** | **0** |
| Tests failing at least once; of them the absence policy | 5; 5 | 0; 0 | 2; 2 | 2; 2 |
| Trials with a wrong written value (Linear priority) | 7 | 19 | 0 | 1 |
| Their own assertions on valid tests: real failures caught; false alarms | 7 of 10; 6 | none to catch; 21 | 6 of 6; 16 | 1 of 1 visible; 32 |
| Generation cost at list (billed) | $0.51 ($0.03) | $1.20 ($0.06) | $0.67 ($0.03) | $1.14 ($0.06) |

(N1's 7 invalid tests include 3 found at run time. N0 and N1's assertion figures are the corrected ones.)

**The predictions:**
- **P1 held.** Neither twin exposes a fact. N0M has no failing test at all: its 4 absence tests (N0 had 9) were all
  answered by saying nothing fits. N1M's 2 failing tests are both the absence policy: asked to remove a "Datasets
  folder" that is not in the hub, the agent tried to remove the file named Datasets instead (3 of 3 trials; the
  replica refuses hub removals, so only the transcripts show it); asked to cancel a budget sync "with Kenji", it once
  cancelled the one with Sam.
- P2 held; P3 missed for N0M; P4 half met; P5 missed (scored before the runs, [log](../log.md)).
- **P6 held.** 51 of the twins' 53 false alarms are tests expecting a cancelled event or a deleted calendar to
  disappear, all marked unsound in the review before the runs; the other 2 are trials where the agent rightly asked
  or timed out. No request lacked a needed detail.
- The rule for a control repeat (3 or more facts exposed) did not trigger.

**What it says:** the naive lines changed what the tests look like, not what they expose. "Different property" and
"challenging" raised the designated look-alikes (N0: 19% of near misses, N0M: 32%) and the facts exercised properly
(7 to 12), but 44 of 48 tests in each twin still leave the right record in the workspace, and the agent, seeing both,
picks right ("There were two files named ..., so I checked ... on each"). Across the four naive prompts, 0 of 192
tests exposed a fact (at most about 1.6% per test at 95%). The line "a perfect assistant must be able to pass them"
did not prevent impossible requests (the bot deleting others' Slack messages, invites of existing members, deleting
a calendar the actor does not own), and the twins' own checks got worse, because more of their tests cancel events.

**Also seen:** 5 timeouts (4 on invalid N0M Slack tests, 1 on N1M-BOX-T03), counted as failures of the agent that
expose no fact; two trials probed destructively to test a permission (a delete tried on an older copy, a scratch
channel created).
