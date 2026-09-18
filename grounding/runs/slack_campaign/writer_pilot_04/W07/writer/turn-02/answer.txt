## Audit

**Extracted conditions (independent of operation):** membership conversation = #general; user's reaction emoji = 👍; reacted message located in #announcements; message topic = security audit; user's first name = Jordan (surname omitted).

**Qualifying roots:** Two — Jordan Lee's membership in #general and Jordan Kim's membership in #general — each satisfies all four fixed conditions identically; only the omitted surname distinguishes them, matching the assigned 2-alternative undespecified pilot. Route roles stay distinct: the membership's conversation (#general) is never equated with the reacted message's location (#announcements), per the route/mode constraint.

**Condition → negative mapping:**
- membership conversation (#general) → Jordan Diaz (member of #random instead)
- emoji (👍) → Jordan Patel (reacted 👀 instead)
- message location (#announcements) → Jordan Ahmed (message located in #security-team)
- message topic (security audit) → Jordan Nguyen (message about budget planning)

Each negative breaks exactly one condition while holding the others (including being named "Jordan" and, where applicable, membership in #general) constant, so no negative admits a qualifying chain elsewhere.

**Capability used:** Supported write "remove a channel member" applied to #general, targeting the user resolved through the reaction/message/location chain — a genuine supported downstream operation, not merely a read.

**Repairs made:** Removed stray corrupted emoji text ("👀ipa" → 👀) in the emoji negative. Clarified that the Jordan Ahmed negative message is a distinct record sharing only the topic, not the same message row as the positive one, avoiding a location contradiction on a shared record. No other defects found; alternatives remain equally supported and differently consequential (removes a different user), and all four negatives map to distinct, independently-variable conditions.

---

## Final Sketch

**Route:** Conversation Membership → User → Reaction → Message → Conversation
**Mode:** underspecified

**Request:** "Remove from #general the member named Jordan who reacted with 👍 to the message in #announcements about the security audit."

**Selection conditions:** the removed membership's conversation is #general; its user reacted 👍 to a message located in #announcements whose text concerns the security audit; the user's first name is Jordan (surname not given).

| Referent | Environment facts | Interpretation |
|---|---|---|
| Jordan Lee's membership in #general | Jordan Lee is a member of #general; reacted 👍 to the #announcements message about the security audit | Alternative through Jordan Lee |
| Jordan Kim's membership in #general | Jordan Kim is a member of #general; reacted 👍 to the #announcements message about the security audit | Alternative through Jordan Kim |
| Jordan Patel's membership in #general | Jordan Patel is a member of #general; reacted 👀 (not 👍) to the #announcements message about the security audit | Wrong emoji only |
| Jordan Nguyen's membership in #general | Jordan Nguyen is a member of #general; reacted 👍 to a different #announcements message about budget planning | Wrong message topic only |
| Jordan Ahmed's membership in #general | Jordan Ahmed is a member of #general; reacted 👍 to a message about the security audit, but that message is located in #security-team, not #announcements | Wrong message location only |
| Jordan Diaz's membership in #random | Jordan Diaz reacted 👍 to the #announcements message about the security audit, but Jordan Diaz's membership is in #random, not #general | Wrong membership conversation only |

No choice between Jordan Lee and Jordan Kim is authorized by the request.