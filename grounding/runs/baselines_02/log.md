# baselines_02: log

## 2026-09-30, 02:05: set-up

- Brief: [baselines_sonnet.md](../../protocols/briefs/baselines_sonnet.md). The question and the stated defaults are
  in the [README](README.md); nothing had run when they were written.
- `generate.py` wraps baselines_01's pieces (`n0/generate.py`: the repair prompt, the loader, the snapshots;
  `n0/cases.py`: the case builder) with the Claude Code backend of the generation kit. Changes from the Muse arms'
  procedure: the writer (Sonnet 5.5 at effort high, as the Muse arms ran at Muse's effort high) and up to three
  repair turns from the start (the Muse twins had one, then two more for N0M's Box).
- Case ids: `SN0M-<SVC>-<id>` and `SN1M-<SVC>-<id>`, apart from the Muse arms' `N0M-` and `N1M-`.

## 2026-09-30, 02:09–02:33: generation (cycle 1)

- **Smoke:** N0M's Box session alone (`runs/gen_n0m_01`): 12 of 12 tests loaded at the first round, 8 turns, 144 s.
- **The rest,** one session at a time: N0M's Calendar, Linear, Slack, then N1M's four services (`runs/gen_n1m_01`).
  No refusal, no failed call.

| Arm | Sessions | Tests loaded (first round) | Repair turns | Turns per session | Output tokens | List-price equivalent | Billed |
|---|---:|---:|---:|---|---:|---:|---:|
| SN0M | 4 | 48 of 48 | 0 | 8, 8, 8, 9 | 79,323 | $1.39 | $0 (plan) |
| SN1M | 4 | 48 of 48 | 0 | 9, 9, 9, 9 | 109,481 | $1.81 | $0 (plan) |

  Against the Muse twins: N0M $1.20 and N1M $1.14 at list ($0.06 billed each); the Muse N0M Box session needed three
  extra repair turns. Claude Code's list price is its own estimate (`total_cost_usd`), from Sonnet 5.5's rates.
- I have not opened any test: the loader's counts are all I read, so the review stays blind to the arm.

## 2026-09-30, 02:35–03:15: the blind review

- One pool, `runs/pool_01` (`pool.py build`): the 96 Sonnet tests and 20 of our Muse tests (5 per service, seeded
  draw from the 292 of the final score), shuffled under anonymous ids. The view shows each test's request, acting
  user, seeded rows and, for the baselines, their own expected outcome and assertions.
- Reviewed by hand in `review_pool_01.py`, in pool order, with the catalog's facts (`pool.py facts`) and the replica's
  code where a request depends on what the API shows or does. Committed at 116 of 116 (4ee8151996) before
  `keys.py` read the manifest.
- **Mid-review correction:** I had given six near misses a family the catalog does not list for their fact (F8 on a
  message text, a user's title, a location; F7 on a message text). baselines_01's reviews never did (checked over
  all their non-F0 near misses), so those became F0 or, where the near miss is the fact's listed substitute, the
  listed family (R060: F6 for D:primary). Proper credit moved accordingly (R039, R053, R068).
- **Precedents followed:** unsound own-oracles stay valid (baselines_01 kept N0M's cancelled-event tests valid);
  sets get no proper credit (rule 6); an edited recurring occurrence is keyed as its exception row.
- **Replica behaviour checked for validity:** Slack's history returns blocks and the calendar list returns
  summaryOverride (readable); Box adds hub items (only removal answers 501); Slack's reaction list has heart and
  thumbsup, not white_check_mark; `chat.delete` is author-only.
- Result: 109 of 116 valid; the numbers and findings are in the README.

## 2026-09-30, 03:11–03:45: runs started at the lead's load; the reviewer cross-check

- **Runs:** started at 24 in flight (12 per arm) at 03:11; the lead asked for 6 in all (the self-host is shared with
  regen's 12 and related_work's 8, and overloaded an hour earlier), so I stopped both within a minute: 12
  attempts per arm had started, all still in `preflight` (no agent turn). A second start ran in the tool's background,
  whose limit is two hours against about three needed, so I stopped it at once too (3 more attempts per arm, also in
  `preflight`). Relaunched detached (`setsid nohup`) at 03:12, 3 per arm, with `--retry-infrastructure`, which gives the
  interrupted attempts a fresh attempt and keeps the old ones on disk.
- **Cross-check** (the lead's yes to my offer): 15 baselines_01 tests re-reviewed under my hand, then compared with
  the other session's calls; the agreement is in the README. Not fully blind for the 10 twin tests (see there).

## 2026-09-30, 03:12–04:10: runs and labels; paused

- **Labels as the trials finished**, in batches, each before any assertion result or verdict (none has been read).
  96 trials finished by 04:07; 95 labelled.
- **One timeout under host load** (SN0M-BOX-T08 t2): 11 requests, 51 s mean, one of 224 s, 2.6 to 15 tokens a second
  (the proxy's request records). It had grounded on the right file and kept retrying a remove form the replica
  ignores. Kept apart in `runs/host_load.json`, unlabelled until its quiet rerun; `rerun.py` written for that.
- **Paused at 04:07** at the lead's request (the regenerated half's runs time out under host load). The lead asked
  to let the in-flight trials finish; the runner cannot drain (its only per-attempt skip is roadmap_01's
  known-defects file, not mine to edit, and stopping the process with SIGSTOP would have stamped the in-flight
  trials as hard-deadline timeouts), so I stopped both runners and their 6 OpenClaw processes (0.5 to 2 minutes into
  their turns). Left as `solver_running`: SN0M-CAL-T04 t1–t3 and SN1M-CAL-T08 t1–t3, for `--retry-infrastructure`.
- **Interim, labels only:** SN1M-BOX-T03 t1 acted on the file Leo owns instead of the one he uploaded, after one
  search that showed both fields (a misread; R:File.created_by_id, a target-present exposure the Muse arms never
  had); SN1M-BOX-T01 t3 and SN0M-BOX-T12 t3 acted on a near miss when nothing matched (policy). The rest are right.

## 2026-09-30, 11:50–12:10: resumed; a key correction and a replica gap

- **Resumed at 11:50** at the lead's word, 3 per arm, `--retry-infrastructure`: the 6 stopped attempts got fresh ones.
- **SN0M-CAL-T05's answer key corrected** (the only test keyed to an occurrence id): the replica writes an edited
  occurrence as `<series>_<local start digits>Z` (`ev_r9x_20180619T093000Z`), not Google's UTC form I had keyed
  (`...T163000Z`), seen in trials 1 and 3 and confirmed in the replica's code. Fixed in `review_pool_01.py`; the
  suites are regenerated after the runs (rewriting case files the runner reads could break an attempt), and
  [judge.py](judge.py) grades every attempt with the suites' final keys. No verdict or assertion had been read.
- **A known replica gap voids one trial:** SN0M-CAL-T05 t2 got empty lists for three valid queries (a keyword search,
  a June 17-26 window with `singleEvents=true`, an unbounded listing) because the replica lists a recurring series
  only when the window covers its first start (autogen_02's replica notes); it reported an empty calendar. Labelled
  `artifact`. Trials 1 and 3 found the series (a `showDeleted` listing, then `instances`) and edited the right
  occurrence, so the test stays valid.
- **Replica finding (report only):** the occurrence ids use local wall-clock digits with a "Z", unlike Google's UTC.
- **Replica finding (report only):** `teams { projects { nodes { ... } } }` fails with "Cannot return null for
  non-nullable field ProjectConnection.nodes" (SN1M-LIN-T05 t2, step 9); it did not decide the trial.

## 2026-09-30, 12:10–12:55: labels, and a second replica gap

- **Replica gap voids two trials:** the replica's `conversations.history` and `conversations.replies` return messages
  without their `reactions` (Slack includes them; the replica code serializes reactions only in `reactions.get`).
  SN1M-SLK-T05 t1 and t3 read the reactions from those listings, saw none, and said nothing matched: labelled
  `artifact`. Trial 2 used `reactions.get` and acted right, so the test stays valid. autogen_02's replica notes for
  the judge say messages "carry their reactions", which is not what the replica does: judge v2 may call these two
  trials the agent's failures (report only; noted for the comparison).
- **Labels beyond baselines_01's vocabulary, kept inside it:** a false absence on a target-present test is
  `incomplete` with `false_absence: true` (SN0M-LIN-T12 t2); a self-corrected write on a decoy is `incorrect` with
  `self_corrected: true` (SN0M-LIN-T11 t2), as judge v2's rules count any write on a decoy.
