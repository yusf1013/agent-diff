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
