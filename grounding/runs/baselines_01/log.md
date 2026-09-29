# Cycle log

Times are US Eastern, from `date`.

## 2026-09-28 14:02: set-up

- The questions and constraints are in the [README](README.md).
- Plan, reviewed with the advisor:
  - **Q4 first**, from existing data only.
  - **N0, "ask your coding agent":** Muse Code, one sandboxed session per domain. It gets only the goal in plain
    words, the API docs the agent under test gets (`api.md`), how to seed data (`seed_ops.md`) and a neutral test
    format. It gets no domain model, facts, substitute menus, method, worked examples, replica profile, checks or
    feedback.
  - **Before any agent run:** review N0's tests by hand for facts exercised, the credit rule, validity (with the
    cause of each flaw) and the oracle. The mapping rules are written down before the review.
  - **Runs:** label every trial by hand before any verdict. Then grade with N0's own assertions, a plain LLM judge
    and J0.
  - **After N0:** decide the next cycle from what N0 shows. That is either N1 (N0 plus the facts, no menus) or
    hand-built ablations of our own tests.

## 2026-09-28 14:05–14:26: cycle 1, N0 ("ask your coding agent")

- **Q4 done** from existing data ([q4/README.md](q4/README.md)). A plain judge (told nothing about grounding) now
  runs on OpenClaw's 178 labelled trials, to measure what J0's prompt adds.
- **N0 generated** ([n0/](n0/)): four Muse Code sessions wrote 48 tests for $0.51 at list ($0.027 billed); all loaded
  at the first try, so no repair turn was needed.
- **My review, before any run** ([n0/review_gen_01.py](n0/review_gen_01.py)):
  - near misses: 39 plain (F0), 8 partial names (F8), 1 neighbouring value (F7); no F1 to F6;
  - forms: 36 target present, 9 absence presupposing a match, 3 sets; none permits absence, none underspecified;
  - facts exercised 49, exercised properly (credit rule) 8, against about 34 for 48 of our Phase 4 tests
    ([ours.py](ours.py));
  - invalid 3: two Slack deletes the service refuses (the bot is not the author), one Slack mention the API never
    shows; 2 oracles unsound (a Box delete expected as a removed row; one emoji name).
- **Runs:** N0's 48 tests × 3 trials on OpenClaw, 12 in flight (`n0/runs/gen_01/solve_01`). Labels are written as
  trials end (`labels.json`), before any assertion or judge verdict.

## Cycle 2, planned from cycle 1 (built while cycle 1 runs)

The two parts most likely to carry our exposure, both suggested by existing OpenClaw data (covers expose 2 of 77,
probes 76 of 279; F1-F8 probes 67/223, F0 probes 9/56):
- **Form ablation:** N0's own target-present tests turned into probes (target removed, "If there isn't one, just tell
  me."): 28 tests ([n0/probe_form.py](n0/probe_form.py)). Does the probe form alone make N0's plain near misses expose
  failures?
- **Content ablation:** plain twins of 12 of our probes that exposed a fact on OpenClaw, same request and seed, the
  substitute removed ([plain_twins.py](plain_twins.py), [plain_pick.json](plain_pick.json)), run beside the
  unchanged originals the same day. Of the facts our probes expose, how many would a plain near miss expose too?

### Cycle 2's reading, fixed before any of its results (2026-09-28, 14:28, commit c38417474)

(Corrected: an earlier version of this heading said 15:05, a time I had not read from the clock.)

Five cells, all on OpenClaw with the self-hosted Qwen, 3 trials per test:

| Cell | Content | Form | Source |
|---|---|---|---|
| a | N0's (mostly plain) | target present | `n0/runs/gen_01/solve_01` |
| b | N0's | probe (target removed, absence permitted) | `n0/runs/gen_01/probe_form` |
| c | ours, with the substitute | probe | `ablation` run, the unchanged originals |
| d | ours, made plain | probe | `ablation` run, the twins |
| e | ours: covers against probes | both | existing: 2 of 77 covers and 76 of 279 probes expose a fact; F0 probes 9 of 56 |

How the results will be read:
- **If b exposes near zero** (as a does), the form alone does not make N0's near misses bite: the substitute carries
  the exposure.
- **If b lands near our F0 probes' rate (about 16%)**, the form carries most of it, and the substitute adds the rest
  (F1-F8 probes expose about 30%).
- **c against d** is the within-test effect of the substitute on facts our probes already exposed. The sample is 12
  pairs × 3 trials, so only a large gap counts (for example, c failing at least three times as often as d). A smaller
  gap is reported as inconclusive, not as "no effect".

## 2026-09-28 14:19–15:34: cycle 1 and cycle 2 results

**Cycle 1, N0 on OpenClaw** (`n0/runs/gen_01`, all 144 trials labelled before any verdict):
- 5 of 48 tests fail (10 of 144 trials), every one the generic absence policy: the request presupposes a record that
  does not exist, and the agent acts on something anyway (or creates the missing channel). **No fact is exposed.**
- 7 trials wrote a wrong value to the right record (Linear priority scale, a duplicate membership), outside the
  grounding scope.
- The naive pipeline's own oracles, against the labels ([oracles.score.json](n0/runs/gen_01/oracles.score.json)):
  - assertions (AgentDiff's): precision 0.28, recall 0.70 on grounding mistakes, plus 9 failures reported on the 3
    invalid tests;
  - a plain judge given the test's `expected`: precision 0.77, recall 1.00, plus the same 9;
  - J0: 0.83 and 1.00, none on the invalid tests.
- Found at run time, not in my review: the Slack replica has no `white_check_mark` reaction (N0-SLK-T06's assertion
  can never pass); strict assertions fail correct trials whenever a bookkeeping column also changes (a file's
  `path` on a move, Linear's `priorityLabel`).

**Cycle 2** (`cycle2/solve_01`, 156 trials, labelled before any verdict), read as fixed at 14:28:
- **Form (cell b):** N0's own near misses in probe form: 7 of 83 trials fail; 4 of 28 tests expose a fact
  (A:Hub.description, A:EventAttendee.email, A:Calendar.summary, R:issue_label_issue_association). In cover form
  (cell a) none of 36 did. 4 of 28 is 14%, near our F0 probes' 16%: **the probe form carries a large part.**
- **Content (cells c and d):** 12 of our exposing probes against plain twins: ALT 27/36 failing trials, PLAIN 7/36;
  12 pairs fail at least once with the substitute, 3 without it. **The gap passes the fixed bar (3×).**
  - Two pairs (G4-BOX-01-I11, I12) fail in both arms for another reason: OpenClaw's agent reads "the PDF ... with a
    top-level comment by Dana Whitfield saying 'approved for launch'" as tag-and-comment, tags the only PDF and
    sometimes posts the comment itself. Without them: ALT 21/30, PLAIN 2/30.
  - **For the PI:** the frozen suite's exposures on these two probes are then not the facts' (H and B); a natural
    reading changes the task. This looks like the "natural reading" flaw (group B) and is not decided here.

## 2026-09-28 15:34–16:16: N1 on OpenClaw, and the report

- **N1** (`n1/runs/gen_01`, 144 trials, labelled before any verdict): 2 of 48 tests fail (6 trials), both the absence
  policy; **no fact exposed**. Every target-present test passed, including its splits and levels. 3 more flaws surfaced
  at run time (a seed that does not install, an unreadable hub-item adder with a removal the replica does not support,
  a rename the actor may not make): [runtime_flaws.json](n1/runs/gen_01/runtime_flaws.json).
- **N1's assertions:** precision 0.15, recall 1.00, plus 18 failures reported on invalid tests.
- **Muse billing:** from 16:13 every Muse call returns HTTP 402 "Billing verification failed". N1's plain and J0
  judges were stopped after 41 failed calls (no cost); kept as `judged_*.failed-402-billing`.
- **The report:** [report.md](report.md). Total Muse spend of the study: $14.13 at list, $1.02 billed (every `calls.jsonl` under the study).

## 2026-09-28 21:29–21:45: N1's judges, and two errors in my format document

- **N1's LLM judges** reran after the PI recharged Muse, on the 141 trials that ran (finished 21:29 and 21:30,
  $8.41 at list for both). Plain judge given `expected`: precision 1.00, recall 1.00 (6 real failures); J0: 0.75
  and 1.00. On the 7 invalid tests (21 trials): the plain judge reported 12 failures, J0 none.
- **My error:** `n0/inputs/*/format.md`, which both baselines got, lists an `"unchanged"` diff type (copied from the
  engine's README), and the engine's schema rejects it. It also says "timestamps and similar bookkeeping columns"
  are ignored, but the engine ignores only the benchmark's list, which misses `path` and `modified_by_id` (Box) and
  `priorityLabel` (Linear). 27 of N1's 34 false alarms had an `"unchanged"` assertion, and 6 of N0's 18 and 3 more of
  N1's came from the bookkeeping columns.
- **Rescored as the document described** (`assertions.py --faithful`: `"unchanged"` becomes `changed` with a count
  of 0; the missing bookkeeping columns ignored): N0 18 false alarms become 12 (precision 0.28 → 0.37); N1 34
  become 16 (0.15 → 0.27). True failures caught are unchanged (N0 7 of 10, N1 6 of 6). The originals are kept in
  `assertions.json`; the report's precision figures need this correction.
- **The 28 false alarms left**, by cause: 18 expect a deleted record to disappear, but Box moves it to the trash and
  Calendar marks the event cancelled; 3 have a request that lacks an email address, so the assistant asked; 3
  expect the `white_check_mark` reaction, which the replica lacks; 3 have a `changed` assertion without
  `expected_changes`, which strict mode fails whenever anything changes (my format document states the rule, not
  this consequence); 1 counts a probe comment the assistant archived.
- **Spend:** the study's Muse total is now $22.55 at list, $1.66 billed.

## 2026-09-28 22:15–22:20: the mutated twins prepared; report corrected

- **The PI's twin design** (2026-09-28): N0 and N1 rerun with one added paragraph, "Make sure each test checks a
  different property. Make the tests challenging: a careless assistant should fail them, but a perfect assistant must
  be able to pass them. Use neutral ids that do not reveal which record is the right one." The PI dropped my
  "documentation" line: the documents are given and Muse read every one in full in all 8 round-1 sessions (its
  `read_file` calls).
- **Round 1's sessions:** one Muse session per service wrote all 12 tests together into one file; N1's sessions were
  separate from N0's; no repair turn was used. Whether the twins start new sessions (recommended) or resume round
  1's is the PI's choice, pending; nothing is generated until then.
- **Prepared:** [twin2/](twin2/README.md) (inputs, with only `task.md` and `format.md` changed; the corrected format
  document), `assertions.py --twin`, [variety.py](variety.py), and the prediction, written at 22:16 before any
  generation.
- **Report corrected** ([report.md](report.md)): the baselines' assertion precision with our harness's errors removed
  (N0 0.54, N1 0.27; `assertions_corrected`, which also counts N0-SLK-T06 and N0-BOX-T08 apart via
  `harness_flaws.json`), N1's judges (plain 1.00/1.00, J0 0.75/1.00), and the first-draft split, now recorded by
  [machinery.py](machinery.py): Phase 4's 31 first drafts, 14 clean, 7 sent back for format only, 10 for substance.

## 2026-09-28 22:34–23:02: the mutated twins generated and reviewed before any run

- **Sessions (PI's choice (a)):** a new Muse session per service, all 12 tests written together, as in round 1.
  Generation ran 22:34–23:01; $2.34 at list, $0.12 billed. The study is at $24.89 at list, $1.78 billed.
- **Loading:** three sessions wrote invalid JSON at first (N0M Box, N1M Box, N1M Linear; round 1 had none). N1M's two
  loaded after the protocol's one repair turn. N0M Box did not: the repair fixed one bracket and left another. I
  gave it further turns with the loader's own errors ([twin2/repair_more.py](twin2/repair_more.py)), a deviation from
  round 1's protocol, checked with the advisor: our writer gets load feedback until its drafts load, and the cap of
  one was ours, not a property of the baseline. Round 3 parsed but 11 seeds lacked a file's `parent`; round 4
  loaded all 12. Funnel: N0M Box "loaded after three repairs"; every other service at first or after one.
- **My review** ([twin2/n0m/review_gen_01.py](twin2/n0m/review_gen_01.py),
  [twin2/n1m/review_gen_01.py](twin2/n1m/review_gen_01.py)), by the fixed rules, before any run:

  | 48 tests | N0 | N0M | N1 | N1M |
  |---|---:|---:|---:|---:|
  | Right record present (incl. sets) | 39 | 44 | 40 | 44 |
  | No right record, absence permitted (our probe form) | 0 | 0 | 0 | 0 |
  | Near misses through a designated substitute | 9 of 48 | 17 of 53 | 21 of 58 | 19 of 66 |
  | Facts exercised | 49 | 55 | 67 | 76 |
  | Facts exercised properly (valid tests) | 7 | 12 | 17 | 13 |
  | Distinct deciding details; tests only reusing one | 32; 20 | 38; 17 | 46; 9 | 51; 13 |
  | Invalid | 3 | 6 | 7 | 7 |

  - **Invalid, N0M:** five Slack tests ask the bot to delete, edit or un-react other people's messages (Slack
    allows none of these), one needs `white_check_mark` (the replica lacks it; counted apart). **N1M:** three Slack
    deletes of others' messages, two invites of people the seed already made members, one delete of a calendar the
    actor does not own, one `white_check_mark`. The "perfect assistant must be able to pass" line did not prevent
    them.
  - **Their own assertions:** the Calendar ones expect a deleted event or calendar to disappear (the replica cancels
    or flags it): 7 N0M and 11 N1M tests are unsound before any run. Not comparable with round 1's review, which had
    not flagged N1's (the scored measure is unaffected).
  - N0M-LIN-T05's active cycle ended on 2026-09-14 (Linear runs on the real clock): a quality note, not a flaw,
    after the advisor's reading (no reading picks the past cycle).
- **Two credits withdrawn before any run** (advisor, precision-first): N0M-LIN-T08's competitor has "Login" in its
  title, but so does every issue, so it lures toward none (F0); N1M-BOX-T08's split is of a binding the catalog does
  not name (two assignees on one task), recorded outside the catalog. The table above has the final counts.
- **Offline check:** all 96 twin assertion specs compile under `--twin`, and an empty `where` and an `exists` check
  mean "any row" (tested on a synthetic diff).
- **The structural predictions, scored before any trial** ([twin2/README.md](twin2/README.md)):
  - P2 held: the right record is present in 44 and 44 tests; neither twin wrote our probe form.
  - P3 missed for N0M: 17 of 53 near misses (32%) go through a designated substitute, against a predicted 25% at
    most (N0: 19%). "Make the tests challenging" moved Muse toward partial names (F8), neighbouring values (F7) and
    sibling fields (F1). N1M, 29%, is inside its predicted 25% to 50%. So P1, exposure, is the live question.
  - P4 half met: N0M uses 38 distinct deciding details (the predicted floor) but 17 tests only reuse one (predicted
    12 at most). N1M: 51 and 13, near N1's 46 and 9.
  - P5 missed for both: 6 invalid N0M tests and 7 N1M (predicted 3 and 4 at most), all from Slack's and Calendar's
    permission rules, pre-seeded memberships and the replica's missing emoji. The "perfect assistant" line did not
    reach them.

## 2026-09-28 23:06 to 2026-09-29 00:40: the twins run, labelled, and scored

- **Runs:** 288 trials (N0M and N1M, 3 each) on OpenClaw with the self-hosted Qwen, two runners at 6 in flight each,
  23:06–00:31. Every trial was labelled by hand as it ended, before any assertion result was read; labels committed
  at bb951e4f2d before scoring.
- **Result** ([twin2/README.md](twin2/README.md#result-runs-2026-09-28-2306-to-2026-09-29-0031-labels-before-any-check-result)):
  neither twin exposes a fact (0 and 0, as N0 and N1). N0M has no failing test; N1M's 2 are both the absence
  policy. P1 and P6 held; the control-repeat rule did not trigger. Across the four naive prompts, 0 of 192 tests
  (169 valid) exposed a fact.
- **Labelling decisions:** 5 timeouts labelled `incomplete` with `"timeout": true` and counted as failures of the agent
  that expose no fact (the PI's rule of 2026-09-28). Round 1 labelled three timed-out trials `not_established`
  (N0-SLK-T12 twice, N1-BOX-T11), all on tests counted invalid, so no count changes; its fourth (N1-BOX-T12) acted
  before timing out and is `incorrect`. N1M-BOX-T12's three attempted removals of the wrong hub item are labelled `incorrect`
  (absence policy) although the replica's 501 kept them out of the diff; that test is listed in
  `twin2/n1m/runs/gen_01/harness_flaws.json` for the assertions, as its review note foresaw.
- **Their own checks** (`assertions.py --twin`): 21 (N0M) and 32 (N1M) false alarms on valid tests, 51 of the 53
  from tests expecting a cancelled event or deleted calendar to disappear, all flagged in the review; 19 N0M trials
  wrote "urgent" on the wrong Linear priority scale, and the assertions caught all 19.
- `summarize_labels.py` now counts timeouts; `compare.py` includes the twins and the variety measure.

## 2026-09-29 00:40–00:47: the random plain twins designed (plain48/)

- The PI chose 48 random plain twins, 12 per service (2026-09-28). [plain48/](plain48/README.md): the seeded draw
  (from this worktree's suite, the version cycle 2 used; exclusions from cycle 2, G4-BOX-01, and the lead's current
  known-defects list on exp/roadmap-02), two replacements by a rule fixed before any twin was built, 48 hand edits
  (4 reused from cycle 2), and the prediction, written before any run.

## 2026-09-29 00:48–02:15: plain48 run, labelled and scored

- 288 trials (48 random probes and their plain twins, 3 each) on OpenClaw with the self-hosted Qwen, 12 in flight,
  00:48–02:11; every trial labelled by hand as it ended, labels committed (a5ae6a3976) before any summary.
- **Result** ([plain48/](plain48/README.md#result-runs-2026-09-29-0048-to-0211-every-trial-labelled-by-hand-before-any-summary)):
  14 of 48 probes fail with the substitute, 2 without; 13 pairs fail only with it, 1 only without (sign test
  p = 0.002); failing trials 29 against 3 of 144. Prediction 1 held on probes and on the originals' trials; the
  plain twins' 3 failing trials came in below the predicted floor of 5 (a miss, in our favour). Predictions 2 and 3
  held. Cycle 2's selected result was not a selection effect.
- Labelling decisions: an attempted wrong action that the service refused (a reaction that returned
  message_not_found) is labelled `incorrect`, as for N1M-BOX-T12; a write followed by a timeout is `incorrect` with
  `"timeout": true`; the one archive of a 5-member channel read as "four humans and a bot" is `incorrect`
  (D:member_count's designated confusion; a reader could call "four members" ambiguous about bots).
- P-AR-BOX-24-I14 fails both ways (3 of 3, 2 of 3): the agent takes the only pricing-table task of that person
  whatever its date, which looks like the absence policy rather than a misread fact; it is counted as an exposure of
  A:Task.created_at in both arms and does not change the discordant count.
- 7 plain twins also rename an id that carried the removed lure (for example U_ANATORRES to U_BELLA), beyond the
  near miss's own value; they are listed in build.py.
