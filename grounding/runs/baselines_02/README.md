# baselines_02: the naive baselines written by a stronger coding agent (Sonnet 5.5)

Session "values" (second assignment of the day from the lead session "RoadMap specialist"), brief
[baselines_sonnet.md](../../protocols/briefs/baselines_sonnet.md). Branch `exp/values-01`.

## Status

- **2026-09-30, 03:15 EDT.** Blind review done ([review_pool_01.py](review_pool_01.py), committed before the pool's
  manifest was read): 109 of 116 valid, SN0M 44 of 48, SN1M 45 of 48, ours 20 of 20. Answer keys and the keyed suites
  built (`keys.py`); blind samples drawn. Next: the runs (started 03:30), then the labels, then the grading.
- **2026-09-30, 02:33 EDT.** Generation done: 96 of 96 tests load, every session on its first round (no repair turn
  needed).

## The question

How can we tell whether the naive baselines' result (no catalog fact exposed in 169 valid tests; the wrong records
they catch come from requests that presuppose a missing record) is a property of the naive approach or of the coding
agent that wrote them? We regenerate the two arms that matter, N0M and N1M
([baselines_01](../baselines_01/report.md) §8), with a stronger coding agent, Sonnet 5.5 through Claude Code, at the
same 48-test budget, and measure them the same way.

## Setup (stated defaults)

- **Writer:** Sonnet 5.5 (`claude-sonnet-5-5`) through Claude Code 2.1.285 (`claude -p`, on the PI's plan), with the
  generation kit's settings (`autogen_01/kit/agent.py`, the Claude Code backend): a clean workspace outside the
  repository, restricted mode, the file tools only (Read, Write, Edit, Glob, Grep; no shell, no web), no MCP servers,
  user and project settings ignored. Effort `high`, the Muse arms' setting (`MUSE_EFFORT=high`).
- **Inputs:** baselines_01's, unchanged: `twin2/n0m/inputs/<domain>/` (N0M) and `twin2/n1m/inputs/<domain>/` (N1M).
  The prompts are not tuned.
- **Sessions:** one session per service writes its 12 tests, one session at a time (the plan's window is shared).
- **Load feedback:** the loader's errors go back in the same session until the tests load, at most three repair
  turns (baselines_01's rule for the full comparison). Every round is snapshotted.
- **Refusals:** a refused or failed call is kept (`*.failed.json`); the domain is run again later under a new run
  name, and both are recorded.
- **Review:** by hand, under baselines_01's rules ([n0/review_rules.md](../baselines_01/n0/review_rules.md)), in one
  shuffled pool with anonymous ids and about 20 of our Muse tests (5 per service, a seeded draw). The review is blind
  to the arm; it cannot be blind to ours against theirs, since our probes' wording gives them away. It adds each
  test's intended target and effect, the answer key for grading.
- **Runs:** every valid test on OpenClaw with the self-hosted Qwen3.8-27B, 3 trials, the 10-minute budget, at most
  24 in flight. Timeouts are the agent's failures; only infrastructure errors are re-run.
- **Grading:** the tests' own AgentDiff assertions (`baselines_01/assertions.py --twin`), and our triage plus judge
  v2 with the review's answer key. A blind sample of 30 trials per arm, drawn before the runs and labelled by hand
  before any assertion result or verdict. Muse cap $5 billed.

## The review (before any run)

Under baselines_01's rules ([n0/review_rules.md](../baselines_01/n0/review_rules.md)), by hand, in one shuffled pool
(`runs/pool_01`: 96 Sonnet tests and 20 of ours, anonymous ids R001–R116). The per-arm records are
`runs/gen_<arm>_01/review.json`; `compare.py`'s `structure` and `variety.py` read them unchanged.

| 48 tests each | N0 (Muse) | N0M (Muse) | **SN0M (Sonnet)** | N1 (Muse) | N1M (Muse) | **SN1M (Sonnet)** | Ours per 48 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Valid before the runs | 45 | 42 | **44** | 44 | 41 | **45** | all |
| Near misses through a designated substitute (F1–F8) | 9 of 48 | 17 of 53 | **57 of 113** | 21 of 58 | 19 of 66 | **75 of 130** | 81 of 99 |
| ... families used | F7, F8 | F1, F6–F8 | **F1, F3, F4, F6–F8** | F1, F4–F8 | F1, F4–F8 | **F1, F4–F8** | F1, F2, F4–F8 |
| Facts exercised | 49 | 55 | **61** | 67 | 76 | **92** | 82.1 |
| Facts exercised properly (valid tests) | 7 | 12 | **22** | 17 | 13 | **37** | 34.0 |
| Distinct deciding details | 32 | 38 | **49** | 46 | 51 | **68** | – |
| Right record present (sets included); probe form (no target, absence permitted) | 39; 0 | 44; 0 | **40; 0** | 40; 0 | 44; 0 | **43; 0** | 18%; 82% |
| Presupposing; underspecified; sets | 9; 0; 3 | 4; 0; 4 | **6; 2; 4** | 8; 0; 0 | 4; 0; 0 | **5; 0; 1** | none in the regular suite |
| Generation, list-price equivalent (billed) | $0.51 ($0.03) | $1.20 ($0.06) | **$1.39 ($0)** | $0.67 ($0.03) | $1.14 ($0.06) | **$1.81 ($0)** | $5.44 ($0.31) |

Sources: baselines_01 `compare.json` for the Muse arms (valid before the runs: 48 less `invalid_before_runs`;
report_01's Table 14 counts N1 as 41 valid, after 3 more flaws found in its runs) and `ours.json` for ours (the
expectation over draws of 12 Phase 4 tests per domain); the Sonnet arms from this review. Sonnet's cost is Claude
Code's own list-price estimate; the plan bills $0.

- **Sonnet seeds about twice as many look-alikes per test** (2.4 and 2.7 near misses per test against 1.1 to 1.4),
  and three to four times as many of them offer a designated substitute. SN1M, which has the fact list, exercises 37
  facts properly, at the level of our 34.0 per 48 tests; SN0M, without it, 22.
- **The form did not change:** 40 and 43 of 48 tests still leave the right record in the workspace, and no test is
  a probe (no target, absence permitted). That is the form that did not bite for the Muse arms (baselines_01 §3, §8).
  The runs will say whether the richer look-alikes bite anyway.
- **Fewer invalid tests** (4 and 3 against 6 and 7), and the same kinds: the bot deleting others' Slack messages
  (cause a, SN0M-SLK-T03, T08, T12), Slack's `white_check_mark` missing from the replica's reaction list (b,
  SN0M-SLK-T05, SN1M-SLK-T08), the replica's 501 on removing a hub item (b, SN1M-BOX-T11), and who added a hub item,
  which the API does not show (f, SN1M-BOX-T12). One valid test's own oracle cannot fail a wrong outcome
  (SN0M-CAL-T05: every count allows 0); as in baselines_01, it stays valid and its oracle is scored apart.
- **Calibration on our 20 tests** (rule 8, compared after the review): the same target in 20 of 20, the same
  near-miss records in 20 of 20, the same fact on 23 of 26 shared near misses, and the same designated-or-plain call
  on 23 of 26 (the family itself on 19).
- **Two readings of the rules I applied** (no precedent in baselines_01's reviews): a near miss gets a family only
  when the catalog lists that family for its fact, otherwise F0 (baselines_01 never used an unlisted one); and a
  request for a set gets no proper credit (rule 6 names the target-present and absence-permitted forms). Crediting
  sets would add one fact to each Sonnet arm (SN0M 23 with R:File.parent_id, SN1M 38 with D:overdue); no Muse set
  test had a designated near miss.
- **Reviewer:** this review is mine; baselines_01's Muse arms were reviewed by another session with the same rules.
  The near-miss counts are counts of seeded records failing exactly one condition and depend little on the reviewer;
  the family and proper calls depend more on judgment.

## The runs and the grading (stated defaults, set before the runs)

- **Runs:** `runs/solve_sn0m_01` (44 valid SN0M tests) and `runs/solve_sn1m_01` (45 valid SN1M tests), 3 trials each
  (267 trials), OpenClaw with the self-hosted Qwen through the proxy on 18778, the 600-second budget, 12 in flight
  per arm (24 in all, the lead's cap). The runner's own selection leaves none of them out (checked without running).
  Only valid tests run: baselines_01 also ran its invalid tests, so its count of failures its assertions report on
  invalid tests has no counterpart here; the per-valid-trial oracle measures stay comparable.
- **Blind samples,** drawn before the runs from the cases folders alone (`eval/blind_solve_sn0m_01.json`, seed
  2026093021, 30 of 132 trials; `eval/blind_solve_sn1m_01.json`, seed 2026093022, 30 of 135), labelled by hand with
  `baselines_01/label_view.py` before any assertion result or verdict is read.
- **Labels, all trials:** as in baselines_01, every trial gets a hand label before its assertions or judge verdict are
  read; the blind samples are the part the judge is scored on.
- **Two-choice tests** (SN0M-BOX-T05, SN0M-LIN-T05, SN0M-LIN-T11: a relation's two ends, an assignee and an issue, a
  folder and its destination) carry two references; judge v2 reads the first only (`judge_one`,
  `references[0]`), so their second choice is checked by hand in the labels and by their own assertions.
- **A reading dispute is not a near-miss failure:** SN0M-LIN-T10 reads "open" as not completed or canceled (Backlog
  included); a trial that leaves out only the Backlog issue is labelled a reading dispute, not a failure.

## Layout

| Path | What |
|---|---|
| [generate.py](generate.py) | One Claude Code session per service writes 12 tests from baselines_01's inputs, with load feedback |
| `runs/` | Generation runs (`gen_<arm>_NN/<domain>/`: prompts, transcripts, results, workspace per round, `load.json`, `cases/`), and later the solver runs |
| [log.md](log.md) | The cycle log |
