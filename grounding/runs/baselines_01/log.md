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
