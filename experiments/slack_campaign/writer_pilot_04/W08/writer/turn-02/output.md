## Audit

**Qualifying roots (recomputed from all facts):** Only Nina's 🔥 reaction on Kevin's message satisfies the full chain — actor-owned reaction (Nina), emoji 🔥, message authored by Kevin, and Kevin holding an actual Conversation Membership row in #product-launch (topic "Launch readiness plan"). Exactly one qualifying root — matches assigned SINGLE mode.

**Condition → negative mapping:**
- Emoji = 🔥 → Row 2 (Nina/👀 on Kevin's message): same author, same membership, only emoji differs.
- Reactor = actor → Row 3 (Sam/🔥 on Kevin's message): same author, same membership, only reactor differs from actor — correctly unremovable since removal is restricted to the reactor's own reaction.
- Author's membership in the launch-readiness channel → Row 4 (Priya/🔥): Priya's real membership is in #design-crew, not #product-launch — fails membership-conversation condition only.
- Membership must be an actual Conversation Membership record, not message co-location → Row 5 (Elena/🔥): message physically posted inside #product-launch, but Elena has no membership row there (only #marketing-updates) — isolates the binding failure from message location.

**Capability check:** Downstream operation is "remove a reaction," restricted to reactions owned by the acting user (Nina). This directly rules out Row 3 (Sam's reaction) via the stated restriction, not via an invented eligibility rule. Rows 1–5 all use only supported/observable facts (author, reaction emoji/reactor, membership existence, conversation topic).

**Repairs:** None required — single qualifying root confirmed, each negative isolates exactly one failed condition, and the write capability/restriction is correctly exercised. Wording preserved unchanged.

---

# Final Sketch — Assignment W08

**Route:** Reaction → Message → User → Conversation Membership → Conversation
**Mode:** single

**Exact user request:**
"Remove my fire reaction from the message posted by the member of the channel about launch readiness."

**Selection conditions:** the reaction is my own 🔥 reaction, on a message authored by a user, where that author holds membership in the conversation whose topic concerns launch readiness (an actual membership record, not merely posting location, in that conversation).

| Referent | Environment facts | Interpretation |
|---|---|---|
| Nina's 🔥 on Kevin's message in #general | Kevin authored the message; Kevin holds membership in #product-launch, topic "Launch readiness plan"; I (Nina) reacted 🔥 to Kevin's message | Match |
| Nina's 👀 on Kevin's message in #general | Same Kevin, same #product-launch membership, but I reacted 👀 instead of 🔥 | Wrong emoji only |
| Sam's 🔥 on Kevin's message in #general | Same Kevin, same #product-launch membership, message reacted 🔥 by Sam, not by me | Wrong reactor (not actor-owned) |
| Nina's 🔥 on Priya's message in #general | Priya authored the message; Priya holds membership only in #design-crew (topic "Design crit queue"), not #product-launch; I reacted 🔥 | Wrong author's conversation membership |
| Nina's 🔥 on Elena's message posted in #product-launch | Elena authored and posted the message directly inside #product-launch, but holds no membership record there — she is only a member of #marketing-updates; I reacted 🔥 | Message location mistaken for membership (binding missing) |

**Note:** Row 5 keeps the message's posting location inside #product-launch to show that channel presence of the message is not equivalent to the author holding a membership record in that conversation; the membership condition must be satisfied by an actual Conversation Membership row, not by co-location.