# Model settings and cost sources (Purdue run)

Verified on **September 22, 2026**. [Machine-readable metadata](model_metadata.json) records the model ID, endpoint, and source URLs. A read-only `GET /api/models` confirmed `qwen3.6:27b` accessible to this account.

| Setting | Qwen 3.6 27B |
| --- | --- |
| Endpoint | `https://genai.rcac.purdue.edu/api/chat/completions` (OpenAI-compatible) |
| Model ID | `qwen3.6:27b` (vLLM, Recommended tier) |
| Thinking | Provider default; no override |
| Output cap per call | 16,384 (within the 65,536 deployed context) |
| Sampling | Provider default; no temperature override |
| Context window | 65,536 deployed (not the larger native limit) |
| Prompt caching | None; same prompt bytes as the Claude comparison |

The system prompt is byte-identical to `manual_comparison_01` (sha256 `a7b31b4f…8547e1`). The episode loop is unchanged: first `<action>` block per turn executed in the same `agent-diff-slack-executor` sandbox, 40-turn / 480-second limits, same environment prepare/diff/cleanup. Only the model endpoint differs.

Costs are **zero by account terms**: Purdue GenAI Studio has no per-token charge to this account. Provider-reported token counts (4,704,258 input / 186,508 output across scored trials) are recorded in [costs](costs.json); dollar cost is recorded as 0, not an invoice. Infrastructure and manual review are excluded.

Rate limits are 60 requests/minute/user with ~10 concurrent calls supported. The first attempt at concurrency 10 hit 400 rate limits; the run was retried at concurrency 3 with backoff (220 absorbed retry attempts, zero failed calls). One case needed a third attempt after a transient `Open WebUI: Server Connection Error` 400. Prior failed attempts are retained and excluded from scored metrics.
