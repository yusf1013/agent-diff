I checked Linear and there's a mismatch I don't want to paper over: **no high-priority webhook issue about rate limiting exists.**

The rate-limiting webhook issues in your workspace are all at **Medium** priority (Linear's 3 = High isn't set on any of them):

- **WEB-1** — Back off webhook deliveries past the rate limit
- **WEB-2** — Replay missed webhook events under the rate limit
- **WEB-3** — Slow webhook retries to stay under the rate limit
- **WEB-4** — Alert when webhook traffic nears the rate limit

The only high/urgent-priority issues are WEB-5 (billing page redesign) and WEB-6 (staging DB credentials) — neither is webhook/rate-limit related.

Two options:
1. Tell me which of WEB-1–4 you meant and I'll set its estimate to 8.
2. Or, if you'd like, I can bump one of them to High priority *and* set the estimate — just say which.

My guess would be **WEB-1** (the 429 backoff one reads most like "the rate limiting issue"), but I didn't want to update the wrong issue without checking.
