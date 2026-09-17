**Audit**

Selection conditions from the request: a message that received a reaction with emoji 🚀, where the reactor holds conversation membership in #eng-rollout (the membership's conversation, not necessarily the message's own channel).

Defects found in the prior draft:
- One row conflated two contradictory descriptions of the same message/reactor pair (garbled "adjust" text) — not a clean single-failure row.
- A "wrong message" row (Marco reacting 🚀 while a genuine #eng-rollout member) was actually a **complete qualifying chain** for that message, since the route never requires the message's own channel to match the membership channel — this accidentally produced a full match, violating the ABSENT mode. Fixed by making that reactor's membership channel wrong instead of the message's channel.
- Ensured every negative changes exactly one condition (emoji, membership-channel identity, missing reaction, or missing membership) while leaving the others intact, and that #eng-rollout retains genuine members (Dana, Priya) so absence isn't due to an empty channel.

Recomputed: no row now has a reactor who is simultaneously (a) a member of #eng-rollout and (b) reacting with 🚀 to the message in that row. All five negatives fail exactly one requirement.

---

**Route:** Message → Reaction → User → Conversation Membership → Conversation
**Mode:** absent

**Request:** "Reply to the message that someone from #eng-rollout reacted to with 🚀, letting them know the rollout window has been pushed to Friday."

| Referent | Environment facts | Interpretation |
|---|---|---|
| "New build passed smoke tests" (posted by Priya in #general) | Reacted 🚀 by Sam; Sam is a member of #general only, not #eng-rollout | Wrong conversation membership only (reactor not in #eng-rollout) |
| "Rollback plan finalized" (posted by Priya in #general) | Reacted 👍 by Dana; Dana is a member of #eng-rollout | Wrong emoji only |
| "Marketing banner draft" (posted by Priya in #marketing) | Reacted 🚀 by Wendy; Wendy is a member of #eng-rollout-archive, a distinct channel from #eng-rollout | Wrong conversation identity only (similarly-named but different channel) |
| "New build passed smoke tests" (posted by Priya in #general) | Priya authored it and is a member of #eng-rollout, but has not reacted to it or any other message | Author's membership substituted for reactor's; no reaction present |
| "Deploy checklist updated" (posted by Priya in #general) | Reacted 🚀 by Alex; Alex's #eng-rollout membership was removed and no longer exists | Missing membership relationship only |

*Note: Dana and Priya remain genuine current members of #eng-rollout so the channel's population is real; each row breaks a different single link in the chain (emoji, membership-channel identity, missing reaction, or missing membership) rather than the whole chain being vacuous.*