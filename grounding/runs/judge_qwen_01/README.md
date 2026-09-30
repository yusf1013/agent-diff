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

## Setup

**What stays the same as the Muse runs:**
- **The prompt:** judge v2's `autogen_02/kit/prompts/judge_v2.md` plus the domain's replica notes
  (`autogen_02/inputs/<domain>/replica.md`), unchanged.
- **The inputs:** each execution's saved Muse input, byte for byte. [inputs_check.py](inputs_check.py) shows, for
  all 2,139 executions with a Muse verdict ([inputs_check.json](inputs_check.json)):
  - every saved prompt is `judge.system.md`, a "---" line, and the user text;
  - every `judge.system.md` equals today's judge_v2.md plus the replica notes;
  - the kit rebuilds every user text from the attempt folder (`judge2.triage`, `bundle.build`, with the form Muse was
    given), 1,935 exactly and the other 204 up to the order of keys inside the diff's UPDATE lines. `bundle.diff_text`
    builds that dict from a set of field names, whose order follows Python's per-process string hashing. So the
    replay sends the saved text, not a rebuild.
  - every judged attempt is the execution's latest attempt, the one in the final manifest.
- **The output schema:** autogen_01's `judge.SCHEMA`, made strict as agent.py makes it for Muse, sent as the
  request's `response_format` (json_schema).

**What differs:**
- **The model:** Qwen3.8-27B (BF16), self-hosted, served by vLLM 0.30.0 as `qwen3.8-27b` at
  `http://127.0.0.1:18000/v1`. The lead described the host as two copies on trojai4 without NVLink; the model's root
  is `/data4/user/ahmed298/qwen/models/Qwen3.8-27B`, and every response carries the fingerprint
  `vllm-0.30.0-tp2-d555b196` (each copy on two GPUs).
- **The wrapper:** Qwen gets the judge prompt as the system message and the bundle as the user message, and nothing
  else. Muse got the two joined by the "---" line as one user message, inside Muse Code's own harness: its base
  instructions (about 25 KB), about 23 KB of developer context blocks, and reasoning effort "high". The judge's own
  text is the same; the harness around it is not reproducible, and it is a confound for any "does the judge need a
  strong model" reading.
- **Settings:** the provider's defaults for sampling (the model's generation config) and for thinking (on; vLLM's
  qwen3 reasoning parser returns the reasoning apart, and the schema applies to the answer after it);
  `max_tokens` 16,384; up to 1,800 s per request.
- **Calls:** [backend.py](backend.py), a drop-in for `autogen_01.kit.agent.run` on calls without tools, through the
  launcher (`SOLVER_BACKEND=selfhost`: the key file, the endpoint, the model name and the limiter shared by every
  session on this machine, 110 requests a minute) and the toy harness's `PurdueClient` (non-streaming). autogen_01's
  agent.py is not changed. A failed attempt (an HTTP error, an answer cut at max_tokens, or an answer that does not
  fit the schema) is kept as `NN-judge.failed.json` and the call is made again, up to 2 more times, as agent.py does.
- **Concurrency:** 16 calls in flight, as the lead asked.

**Recorded per call** (`runs/<run>/<run>/<trial>/<case_id>/`): `judge.system.md`, `NN-judge.prompt.md` (the user
message), `NN-judge.request.json` (the request body, without the auth header), `NN-judge.result.json` (usage, the
raw response with its reasoning, the fingerprint, cost 0) and `verdict.json` (the answer, plus the fields judge2
adds, copied from Muse's verdict). Each run folder has `plan.json` (settings and schema) and `calls.jsonl` (a usage
row per attempt).

**Reference labels** (read only by [compare.py](compare.py)): the lead's 310 retained blind labels on final
executions (`openclaw_eval_01/eval/labels_*/*_blind.json`), and blind_review_01's 200 effective labels, of which the
133 with a Muse verdict enter the comparison. So 443 labelled executions, 442 with a resolved label (BR039 stays
uncertain, as in blind_review_01).

**Outcome groups,** as blind_review_01: failure (incorrect, presented), nonfailure (correct, correct_absent,
false_absence, incomplete), void (artifact, not_established). report_01's RQ5 puts incomplete and false_absence with
the voids instead, so Muse's numbers here can differ slightly from its Table 9.

## Log

| When (EDT) | What changed | What ran | What was learned |
|---|---|---|---|
| 09-30 00:05 | `common.py`, `inputs_check.py` | The input check, no model calls | Muse's 2,139 saved judge prompts are judge_v2.md + the domain's replica notes + the bundle, byte for byte; the kit rebuilds 1,935 bundles exactly and the other 204 up to the order of keys in the diff's UPDATE lines (Python's per-process set order). So the replay sends Muse's saved text, not a rebuild. |
