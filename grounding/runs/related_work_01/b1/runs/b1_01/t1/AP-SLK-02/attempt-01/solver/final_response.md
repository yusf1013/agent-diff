I can't complete this one through the Slack proxy: I located the channel — **`incidents-checkout`** (`#incidents-checkout`, ID `CYFXSMDHK8C`, topic: "Checkout outage: 502s during payment retries, resolved and archived for reference") — and called `conversations.unarchive`, but the proxy rejects it with `unknown_method` (it only exposes the documented method set, which oddly includes `conversations.archive` but not `unarchive`).

To unarchive it manually: in Slack, hover the channel → **•••** (or right-click) → **Restore**.

If you'd like, I can check back later in case the proxy gets updated to allow unarchive.
