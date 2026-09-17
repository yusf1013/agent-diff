**Route:** Message → Reaction → User → Conversation Membership → Conversation
**Mode:** absent

**Request:** "Reply to the message about the rollout checklist that got a 🚀 reaction from a member of the #beta-testers channel: 'Please confirm the final go-ahead timing.'"

**Selection conditions:** the message concerns the rollout checklist; it received a 🚀 reaction; the reactor holds a conversation membership in #beta-testers.

| Referent | Environment facts | Interpretation |
|---|---|---|
| "Rollout checklist finalized for Tuesday" (#product-launch, authored by Dana) reacted 🚀 by Ethan | Ethan is a member of #general only, not #beta-testers | Wrong membership only |
| "Rollout checklist finalized for Tuesday" (#product-launch, authored by Dana) reacted 👍 by Farah | Farah is a member of #beta-testers | Wrong emoji only |
| "Office relocation announcement" (#office-updates, authored by Grace) reacted 🚀 by Grace | Grace is a member of #beta-testers | Wrong message (unrelated topic) only |
| "Launch checklist for marketing site copy" (#marketing-launch, authored by Iris) reacted 🚀 by Harold | Harold is a member of #beta-testers | Wrong message (different conversation, superficially similar topic) only |