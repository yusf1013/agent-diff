## Audit

**Selection conditions (from request, independent of labels):** contributed a 🔥 reaction; that reaction record is attached to the budget-freeze announcement message located in #finance.

**Downstream operation/answer:** open a DM with the selected user and post a supplied message — matches the supported write "open a DM and message the selected user with a supplied purpose." No profile-read substitution needed.

**Reconstructed qualifying roots (all facts, ignoring labels):**
- Dana: reactor 🔥 → budget-freeze announcement (#finance). Complete chain — qualifies.
- Wes: reactor 👍 → same message. No 🔥 reaction anywhere else in the environment → no qualifying chain.
- Nora: reactor 🔥 → different message (office-relocation, #general). Reaction exists but not attached to the target message → no qualifying chain.
- Priya: author of target message, no reaction record at all → no Reaction→Message chain exists for her → no qualifying chain.

Only Dana has a complete User→Reaction→Message chain satisfying both the emoji and the message binding. Count = 1, matching SINGLE mode.

**Condition → negative mapping:**
- Emoji = 🔥 → Wes (has 👍 instead, same message otherwise binding-correct).
- Message = budget-freeze announcement in #finance → Nora (correct emoji, wrong message).
- Role = reactor (not author) → Priya (author of correct message, no reaction).

Each negative fails exactly one condition; no negative accidentally retains a complete alternate chain. No repairs required — sketch stands.

## Final sketch

Route: User → Reaction → Message
Resolution mode: single

**Request:** DM the person who reacted with 🔥 to the budget-freeze announcement in #finance: "Heads up — the follow-up meeting on this is Thursday at 2pm."

**Selection conditions:** contributed a 🔥 reaction; that reaction is attached to the budget-freeze announcement message posted in #finance.

| Referent | Environment facts | Interpretation |
|---|---|---|
| Dana | Reacted 🔥 to the budget-freeze announcement message in #finance (authored by Priya) | Match |
| Wes | Reacted 👍 to that same budget-freeze announcement message in #finance | Wrong emoji only |
| Nora | Reacted 🔥 to a separate office-relocation announcement message in #general | Wrong message only |
| Priya | Authored the budget-freeze announcement message in #finance but did not react to it | Author substituted for reactor |