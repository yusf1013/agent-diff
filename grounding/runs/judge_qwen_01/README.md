# judge_qwen_01: judge v2 on the self-hosted Qwen instead of Muse

Session "judge_qwen", started by the lead ("RoadMap specialist") on 2026-09-30 from the brief
[briefs/judge_qwen.md](../../protocols/briefs/judge_qwen.md).

## Status

- **2026-09-30 00:05 EDT.** Setup. The input check passed on all 2,139 executions (below). The backend and the replay
  driver are being written; no Qwen call has been made yet.
- **Host:** the lead cleared the self-hosted Qwen for the whole replay (message of 2026-09-30, about 00:00 EDT), at
  about 16 judge calls in flight. Purdue's Qwen is not used; the brief's "use Purdue first" step was superseded by
  that message.

## The question

How can we run judge v2 on an open model, the self-hosted Qwen3.8-27B, instead of Muse Spark 1.3 without losing its
accuracy? Concretely: with the same prompt, the same inputs and the same output schema, how often does Qwen's
verdict match Muse's and the blind reference labels, and where Qwen and Muse disagree, which one is right?

The bar, fixed in the brief before any run: Qwen can replace Muse only if, on the labelled executions, it misses at
most 2 of the labelled failures and its failure precision is within 3 points of Muse's. The decision is the lead's.

## Log

| When (EDT) | What changed | What ran | What was learned |
|---|---|---|---|
| 09-30 00:05 | `common.py`, `inputs_check.py` | The input check, no model calls | Muse's 2,139 saved judge prompts are judge_v2.md + the domain's replica notes + the bundle, byte for byte; the kit rebuilds 1,935 bundles exactly and the other 204 up to the order of keys in the diff's UPDATE lines (Python's per-process set order). So the replay sends Muse's saved text, not a rebuild. |
