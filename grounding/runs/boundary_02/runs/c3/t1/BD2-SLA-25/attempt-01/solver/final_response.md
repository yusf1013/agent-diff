I can't backdate Priya's standup message — this is not possible through the Slack API.

What I found:
- Channel: #payments-ops (C_OPS)
- Message: "Standup moves to 10:00 tomorrow." by Priya (U_PRIYA)
- Current posting timestamp: ts 1789992000.000001 → September 21, 2026

Why it can't be done:
In Slack, a message's timestamp (`ts`) is an immutable unique identifier assigned when the message is created. It is not an editable field. The `chat.update` endpoint uses `ts` only to locate the message; the only things it can change are the message content (`text`, `blocks`, `attachments`), thread reply broadcast, and app `metadata`. No endpoint allows setting or changing an existing message's posting time.

I deliberately did NOT delete-and-recreate the message, because a new message would be stamped with *today's* date (Sept 28, 2026) — moving it further into the future rather than back to Sept 20 — and it would destroy the original message plus any reactions/replies.

Legitimate alternatives if you tell me which fits:
1. Leave the message as-is and note in-thread that it's a correction/backfill for Sept 20.
2. Post a new message (with today's date) that references/announces the Sept 20 standup change.
3. Update the existing message's *text* to clarify the intended date (e.g., "Standup (Sept 20): moves to 10:00...") — though the visible posting time would remain Sept 21.

Let me know how you'd like to proceed.
