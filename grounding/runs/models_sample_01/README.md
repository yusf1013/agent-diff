# models_sample_01: a sample of the suite on more models and harnesses

## The PI's questions (2026-10-04)

1. How does performance vary across models?
2. How does it vary across harnesses for the same model?
3. How large is the jump between versions of one model (Sonnet 5 to 5.5, GPT-6 Sol to 6.1 Sol)?
4. Which models should get the full-scale evaluation? (A recommendation after the results.)

## What runs (decided by the PI, 2026-10-04)

Ten sets, a set being one model on one harness, each running the sample's 150 tests three times (450 runs):

| Harness | Models | Login |
|---|---|---|
| OpenClaw (2026.7.1-2, the version the earlier rounds used) | self-hosted Qwen3.8-27B, GPT-6 Sol, GPT-6.1 Sol | OpenClaw's ChatGPT login of 2026-09-29 |
| OpenHands (software-agent-sdk 1.51.0) | the same three | OpenHands's ChatGPT login (2026-10-04) |
| Claude Code | Sonnet 5, Sonnet 5.5 | the machine's Claude login, read only |
| Codex | GPT-6 Sol, GPT-6.1 Sol | the machine's Codex login, read only |

4,500 runs: 2,700 on the ChatGPT plan, 900 on the Claude plan, 900 on our Qwen; nothing billed per token. Sonnet on
OpenClaw and OpenHands is left out: both reach a Claude subscription only by running Claude Code inside them, and
their own agents would need a paid API key (about $100 for the four sets); the PI chose to skip them.

Every model runs at reasoning effort "medium", with the 10-minute limit, no follow-up turn, and the tests' dates filled
in for the day of the run ([dates_02](../dates_02/README.md)). The judge is judge v2 on the self-hosted Qwen; the
boundary tests are graded by code (the change made to the data, then the reply), as in boundary_auto_01.

## The sample

[kit/draw.py](kit/draw.py) → [sample.json](sample.json), seed 20261004, drawn without reading any result: 30 tests in
each of five forms (packed probes, single-decoy probes, absence, underspecified, boundary; covers skipped by the PI),
from the designated tests behind [denominator_tables.md](../../denominator_tables.md), services in proportion
(Box 40, Calendar 29, Linear 54, Slack 27), at most one test per fact within a form, the boundary tests spread over
their five limit classes.

## Hand checks (the PI asked for more than 200)

About 45 runs per set labelled blind before any verdict (450), to measure the Qwen judge per set; about a quarter of
each set's boundary runs read by hand, plus every run the grading code flags (about 230).

## Status

- 2026-10-04: sample drawn; OpenHands installed and checked on our Qwen (`grounding/integrations/openhands/smoke.py`);
  logins in place (`grounding/integrations/harness_auth/`). Next: the boundary tests on real harnesses, the OpenHands
  and Codex runners, one check call per subscription route, then the runs, GPT first (the ChatGPT plan lapses around
  2026-10-06).
