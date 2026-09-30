I found five rate-limit issues assigned to Leo Park, and all have comments about retry logic. Which should I set to **5**?

- **API-1** — Rate limit blocks legitimate retry bursts — exponential backoff with jitter proposal
- **API-2** — Rate limit throttles retries during traffic peaks — review notes before sign-off
- **API-3** — Rate limit rejects valid burst retries — backoff schedule draft
- **API-4** — Rate limit drops retries from mobile clients — idempotency-key edge cases
- **API-5** — Rate limit drops retries on edge nodes — rough retry-logic sketch

No changes made yet. Memory search was unavailable, so I checked Linear directly.
