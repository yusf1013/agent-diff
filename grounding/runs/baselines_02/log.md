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
