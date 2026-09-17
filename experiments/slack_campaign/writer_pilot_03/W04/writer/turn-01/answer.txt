# Assignment W04

Route: Message → Reaction → User → Conversation Membership → Conversation
Resolution mode: absent

**User request:** "Reply to the message that someone from #eng-rollout reacted to with 🚀, letting them know the rollout window has been pushed to Friday."

| Referent | Environment facts | Interpretation |
|---|---|---|
| "New build passed smoke tests" (posted in #general by Priya) | Reacted 🚀 by Sam; Sam is a member of #general, not #eng-rollout | Wrong conversation membership only (reactor's membership channel doesn't match) |
| "Rollback plan finalized" (posted in #general by Priya) | Reacted 👍 by Dana; Dana is a member of #eng-rollout | Wrong emoji only |
| "New build passed smoke tests" (posted in #general by Priya) | Reacted 🚀 by Wendy; Wendy is a member of #eng-rollout | This is the message that would qualify but for the missing reactor-membership binding elsewhere — actually satisfies the chain; adjust: reacted 🚀 by Wendy, but Wendy's membership is in #eng-rollout-archive, a differently named channel | Wrong conversation identity only |
| "Marketing banner draft" (posted in #marketing by Priya) | Reacted 🚀 by Marco; Marco is a member of #eng-rollout | Wrong message only |
| "New build passed smoke tests" (posted in #general by Priya) | Authored by Priya, who is a member of #eng-rollout; message has no reactions | Author's membership substituted for reactor's membership; no reaction present |
| "Deploy checklist updated" (posted in #general by Priya) | Reacted 🚀 by Alex; Alex was removed from #eng-rollout and now has no membership record there | Missing membership relationship only |

*Note: rows keep the reaction (person, emoji, message) and the conversation-membership condition each independently broken exactly once, so no row completes the full Message→Reaction→User→Membership→Conversation chain to #eng-rollout with 🚀.*