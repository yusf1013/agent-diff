# baselines_02: the naive baselines written by a stronger coding agent (Sonnet 5.5)

Session "values" (second assignment of the day from the lead session "RoadMap specialist"), brief
[baselines_sonnet.md](../../protocols/briefs/baselines_sonnet.md). Branch `exp/values-01`.

## Status

- **2026-09-30, 04:10 EDT. Paused at the lead's request** (the regenerated half's runs have the host). 96 of 267
  trials had finished (SN0M 45 of 132, SN1M 51 of 135) and all but one are labelled; that one timed out under host
  load and waits for a quiet rerun. The 6 trials in flight were stopped (the runner has no drain) and get fresh
  attempts when the runs resume. Interim, from the labels only: one fact exposed on a target-present test
  (SN1M-BOX-T03 trial 1: the owner taken for the uploader, R:File.created_by_id) and two presupposing tests acted on
  (SN1M-BOX-T01 t3, SN0M-BOX-T12 t3); every other finished trial is right. No assertion result or verdict has been
  read.
- **03:15.** Blind review done ([review_pool_01.py](review_pool_01.py), committed before the pool's manifest was read):
  109 of 116 valid, SN0M 44 of 48, SN1M 45 of 48, ours 20 of 20. Answer keys and keyed suites built (`keys.py`);
  blind samples drawn. Runs started at 03:12.
- **02:33.** Generation done: 96 of 96 tests load, every session on its first round (no repair turn needed).

## The question

How can we tell whether the naive baselines' result (no catalog fact exposed in 169 valid tests; the wrong records
they catch come from requests that presuppose a missing record) is a property of the naive approach or of the coding
agent that wrote them? We regenerate the two arms that matter, N0M and N1M
([baselines_01](../baselines_01/report.md) §8), with a stronger coding agent, Sonnet 5.5 through Claude Code, at the
same 48-test budget, and measure them the same way.

## Setup

Set before generation and before the runs; changes made on the way are marked as such.

- **Writer:** Sonnet 5.5 (`claude-sonnet-5-5`) through Claude Code 2.1.285 (`claude -p`, on the PI's plan), with the
  generation kit's settings (`autogen_01/kit/agent.py`, its Claude Code backend): a clean workspace outside the
  repository, restricted mode, the file tools only (Read, Write, Edit, Glob, Grep; no shell, no web), no MCP servers,
  user and project settings ignored, effort `high` (the Muse arms ran at Muse's `high`). [generate.py](generate.py).
- **Inputs:** baselines_01's, unchanged: `twin2/n0m/inputs/<domain>/` for SN0M (the task, the corrected format
  document, the API notes, the seed operations, the schema, and the PI's reviewer paragraph) and
  `twin2/n1m/inputs/<domain>/` for SN1M (the same plus the fact list). The prompts are not tuned.
- **Sessions:** one session per service writes its 12 tests, one session at a time (the plan's window is shared by
  five sessions). The loader's errors go back in the same session, at most three repair turns (baselines_01's rule
  for the full comparison); none was needed. Every round and transcript is kept under `runs/gen_<arm>_01/`.
- **Review:** by hand, under baselines_01's rules ([n0/review_rules.md](../baselines_01/n0/review_rules.md)), in one
  shuffled pool with anonymous ids and 20 of our Muse tests (5 per service, a seeded draw from the 292 of the final
  score). Blind to the arm; not blind to ours against theirs (our probes' wording gives them away, and our tests have
  no oracle to show). The review also writes each test's intended target and effect: the answer key for grading.
- **Runs:** every valid test (SN0M 44, SN1M 45) on OpenClaw with the self-hosted Qwen3.8-27B through the proxy on
  18778, 3 trials, the 600-second budget (`openclaw_eval_01/run.py`, `SOLVER_BACKEND=selfhost`). Only valid tests
  run: baselines_01 also ran its invalid ones, so its count of failures its assertions report on invalid tests has no
  counterpart here; the per-valid-trial measures stay comparable.
  - *Load (changed on the way):* 3 in flight per arm, 6 in all, the lead's cap for a host shared with two other
    studies (the first start, at 24, was stopped within a minute, before any agent turn).
  - *Timeouts:* the agent's failures, except a timeout with few requests at over 30 s each, which is a "timeout under
    host load" (the lead's rule): kept apart in `runs/host_load.json` with the proxy's timings, and rerun as a new
    attempt when the host is quiet ([rerun.py](rerun.py); the old attempt stays).
  - *Pause (changed on the way):* at 04:07 the lead asked for the host back. The runner cannot drain, so both runners
    and their 6 in-flight solvers were stopped; those attempts stay as `solver_running` and get fresh attempts from
    the runner's `--retry-infrastructure` on resume.
- **Labels:** every trial is labelled by hand (`baselines_01/label_view.py`, `add_labels.py`, baselines_01's
  vocabulary) after it ends and before any assertion result or judge verdict is read, as in baselines_01. The blind
  samples, drawn before the runs from the cases folders alone (30 per arm: `eval/blind_solve_sn0m_01.json`, seed
  2026093021; `eval/blind_solve_sn1m_01.json`, seed 2026093022), are the trials judge v2 is scored on.
- **Grading:** the tests' own AgentDiff assertions (`baselines_01/assertions.py --twin`), and our triage plus judge
  v2 with the review's answer key ([grade.py](grade.py)); baselines_01's label-based measures (policy facts, oracle
  scores, label summaries) through [tables.py](tables.py). Two-choice tests (SN0M-BOX-T05, SN0M-LIN-T05,
  SN0M-LIN-T11) carry two references, and judge v2 reads the first only, so their second choice is checked in the
  labels and their own assertions. A trial of SN0M-LIN-T10 that leaves out only the Backlog issue is a reading
  dispute ("open"), not a near-miss failure. Muse cap $5 billed.

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
- **Reviewer cross-check** (the lead's request; [rereview.py](rereview.py), [rereview_01.py](rereview_01.py),
  `runs/rereview_01/compare.json`): I re-reviewed a seeded draw of 15 baselines_01 tests (5 N0M, 5 N1M, 5 N1) before
  reading the other session's calls on them. Agreement: validity and flaw cause 15 of 15, form 15 of 15, the
  near-miss records 16 of 16, designated or plain 16 of 16 (the family itself too), proper credit on the valid tests
  14 of 14 (the one difference is on a test both call invalid); the fact named differs on 2 of 16, both plain near
  misses (R:Issue.stateId against my A:WorkflowState.name; R:EventAttendee.event_id against my
  A:EventAttendee.email). The twin part is not fully blind: an audit an hour earlier had printed the other
  session's non-F0 near misses for every twin test; the 5 N1 tests are the clean control and agree fully. So the
  gap between the Sonnet and the Muse arms is not the reviewer's.

## Layout

| Path | What |
|---|---|
| [generate.py](generate.py) | One Claude Code session per service writes 12 tests from baselines_01's inputs, with load feedback |
| [pool.py](pool.py) | The blind pool (96 Sonnet tests and 20 of ours under anonymous ids), its view, the catalog's facts |
| [review_pool_01.py](review_pool_01.py) | My review of the pool, with each test's answer key |
| [keys.py](keys.py) | From the review to per-arm review records, keyed cases (valid tests only) and the calibration on ours |
| [rereview.py](rereview.py), [rereview_01.py](rereview_01.py) | The reviewer cross-check on 15 baselines_01 tests |
| [blind_sample.py](blind_sample.py) | The blind samples, drawn before the runs |
| [rerun.py](rerun.py) | The quiet rerun of timeouts under host load, as new attempts |
| [grade.py](grade.py), [tables.py](tables.py) | Judge v2's trial list and the scores; baselines_01's label-based measures on these arms |
| `runs/gen_<arm>_01/` | Generation (per service: prompts, transcripts, results, workspace per round, `load.json`, `cases/`), the arm's `review.json` and `labels.json` |
| `runs/pool_01/`, `runs/rereview_01/` | The pool (items, manifest, review, calibration) and the cross-check draw |
| `runs/suite_sn0m_01/`, `runs/suite_sn1m_01/` | The keyed valid cases the solver runs |
| `runs/solve_sn0m_01/`, `runs/solve_sn1m_01/` | The runs (hidden from ripgrep by `.ignore`); `runs/host_load.json` |
| `eval/` | The blind samples |
| [log.md](log.md) | The cycle log |
