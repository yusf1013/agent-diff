# Known limitations of the pre-correction evidence in this directory

The 57 scored trials, trajectories, judgments, and metrics in this directory
are preserved as recorded. The adapter corrections committed after the
checkpoint do not change those bytes. When reusing this evidence, apply the
following annotations:

- **Provider reasoning is missing from saved steps.** The pre-correction
  adapter created `thinking` content blocks but dropped their text during
  serialization, and did not preserve the raw provider response. The absence
  of reasoning text in `runs/qwen36/*/attempt-*/solver/*.json` is a logging
  gap, not proof the provider returned none. Do not treat those steps as
  complete response records.
- **Thinking-token counts are unavailable, not zero.** `costs.json`,
  `usage_summary.json`, and per-attempt summaries record `thinking_tokens`
  as 0. The provider does not report thinking-token counts; read 0 as
  "unavailable" in every file written before the correction.
- **Retry descriptions are stale in `plan.json`.** The plan says "(3
  attempts, backoff)". The client actually used up to 6 attempts per call
  with longer waits for rate-limit and transient-server 400s. Attempt and
  retry counts in `costs.json` (679 successful calls, 220 absorbed
  retries) are unaffected.
- **Output-limit precedence.** The pre-correction client resolved the
  per-call limit and the client-level cap with `max()`, which would have
  ignored the cap had one been set. No recorded run set a client-level
  cap, so every recorded call used the per-call value (16384) and the
  saved requests remain accurate.
- **Rate limiting was reactive.** Recorded runs relied on per-process
  concurrency plus backoff after 400s. Later runs use a shared
  cross-process limiter; retry counts are therefore not comparable
  across the two regimes.
