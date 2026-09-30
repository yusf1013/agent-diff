I checked Linear, and there's no issue that matches "high-priority webhook issue about rate limiting." Here's what's actually in the workspace:

**High priority (3):**
- WEB-6 — "Rotate staging database credentials" (not webhook / rate-limiting)

**Urgent (4):**
- WEB-5 — "Redesign billing settings page" (not webhook / rate-limiting)

**Medium priority (2) — all webhook + rate-limiting:**
- WEB-1 — "Back off webhook deliveries past the rate limit"
- WEB-2 — "Replay missed webhook events under the rate limit"
- WEB-3 — "Slow webhook retries to stay under the rate limit"
- WEB-4 — "Alert when webhook traffic nears the rate limit"

So there's a mismatch: the only high-priority issue isn't about webhooks, and all four webhook rate-limiting issues are Medium, not High.

Which one do you want me to set the estimate to 8 on? Options:
1. You meant a specific webhook issue (tell me which — WEB-1 through WEB-4).
2. You want me to treat "high priority" loosely and pick one of the Medium webhook issues (but I'd rather not guess among four).
3. Something else — e.g., the high-priority WEB-6, if that's actually what you meant.

Let me know and I'll update the estimate right away.
