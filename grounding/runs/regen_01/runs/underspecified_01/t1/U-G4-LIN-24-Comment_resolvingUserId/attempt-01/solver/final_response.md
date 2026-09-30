I dug into this and hit a genuine ambiguity — here's what I found in Linear:

**Leo Park's open rate-limit issues (all in API team, all currently unestimated):**

- **API-1** — Rate limit blocks legitimate retry bursts → thread: *"Retry logic proposal: exponential backoff with jitter for the new rate limiter. Flagging for review."* (Omar Haddad)
- **API-2** — Rate limit throttles retries during traffic peaks → thread: *"Retry logic looks good to me; leaving my notes inline before sign-off."* (Maya Chen)
- **API-3** — Rate limit rejects valid burst retries → thread: *"Retry logic draft is ready; walking through the backoff schedule below."* (Sam Rivera)
- **API-4** — Rate limit drops retries from mobile clients → thread: *"Retry logic edge cases: idempotency keys on repeated attempts."* (Omar Haddad)
- **API-5** — Rate limit drops retries on edge nodes → thread: *"Retry logic sketch for edge nodes, still rough."* (Omar Haddad)

Every one of Leo's rate-limit issues has a comment about retry logic, so the description matches all five (no memory of a prior discussion to disambiguate either). The closest to "the thread about retry logic" in the literal sense is **API-1**, where the comment is the retry-logic *proposal* itself — but I'd rather not guess on a field that affects planning.

Which one did you mean? (API-1 through API-5 — I'll set the estimate to 5 on it right away.)

⚠️ 🛠️ Exec failed: `list files in ~/.openclaw-state/c87ba79b42ee4be2/workspace-assistant/memory/ → search "retry|linear|API-1" in 2>/dev/null` (exit 2)
