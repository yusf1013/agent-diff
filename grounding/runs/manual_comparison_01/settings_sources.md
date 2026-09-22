# Model settings and cost sources

Verified on **September 22, 2026**. [Machine-readable metadata](model_metadata.json) records the model IDs, selected AWS price rows, and source URLs. Read-only Bedrock discovery in `us-west-1` confirmed both selected US inference profiles active; no inference calls were needed for this verification.

| Setting | Sonnet 5 | Haiku 4.5 |
| --- | --- | --- |
| Bedrock profile | `us.anthropic.claude-sonnet-5` | `us.anthropic.claude-haiku-4-5-20251001-v1:0` |
| Thinking | Provider-default adaptive thinking; default effort high | Explicit extended thinking, 16,000-token budget, approved by the user |
| Output cap per call | 128,000 | 64,000, including thinking |
| Sampling | Provider default | Temperature 1, explicitly supplied with extended thinking |
| Context window | 1,000,000 | 200,000 |

Sonnet preserves the [native benchmark configuration](../slack_baseline/20260908T161312Z/config.json): no thinking, effort, or sampling override. Omission enables adaptive thinking on Sonnet 5 but leaves Haiku thinking off, so Haiku receives its explicitly approved budget. Haiku does not support adaptive effort or interleaved thinking. See the official [migration guide](https://platform.claude.com/docs/en/models/sonnet-5/migration-guide), [model comparison](https://platform.claude.com/docs/en/models/overview), and [extended-thinking documentation](https://platform.claude.com/docs/en/build-with-claude/extended-thinking).

These **US geographic Standard** rates include the 10% premium over global routing, in dollars per million tokens:

| Token category | Sonnet 5 | Haiku 4.5 |
| --- | ---: | ---: |
| Ordinary input | 2.20 | 1.10 |
| Output, including thinking | 11.00 | 5.50 |
| Five-minute cache write | 2.75 | 1.375 |
| One-hour cache write | 4.40 | 2.20 |
| Cache read | 0.22 | 0.11 |

Prices were resolved from the [AWS pricing page](https://aws.amazon.com/bedrock/pricing/), its geographic inference table, and the [underlying AWS rate data](https://b0.p.awsstatic.com/pricing/2.0/meteredUnitMaps/bedrockfoundationmodels/USD/current/bedrockfoundationmodels.json), published `2026-09-22T16:44:18Z`, under `US West (N. California)`. The metadata preserves only the selected price rows. The old baseline's Sonnet estimates of $3/$15 are superseded: [current pricing](https://platform.claude.com/docs/en/about-claude/pricing) confirms permanent $2/$10 global rates. Historical run artifacts remain unchanged.

Costs are **estimates from provider-reported usage and public list prices**, not AWS invoice figures. They exclude infrastructure, tax, and account-specific discounts. Billed output already includes thinking; do not add thinking tokens a second time.

Explicit five-minute caching is retained. Minimum eligible prefixes are 1,024 tokens for Sonnet and 4,096 for Haiku; both allow four checkpoints. Hits refresh TTL, while cross-region routing can increase writes. Actual returned cache counters establish savings; merely supplying a cache control does not. No padding is added to meet a threshold. [AWS caching documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html)
