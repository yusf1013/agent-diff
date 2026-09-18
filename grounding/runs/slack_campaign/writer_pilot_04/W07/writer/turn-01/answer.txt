**Route:** Conversation Membership → User → Reaction → Message → Conversation
**Mode:** underspecified

**Request:** "Remove from #general the member named Jordan who reacted with 👍 to the message in #announcements about the security audit."

**Selection conditions:** the removed membership's conversation is #general; its user reacted 👍 to a message located in #announcements whose text concerns the security audit; the user's first name is Jordan (surname not given).

| Referent | Environment facts | Interpretation |
|---|---|---|
| Jordan Lee's membership in #general | Jordan Lee is a member of #general; reacted 👍 to the #announcements message about the security audit | Alternative through Jordan Lee |
| Jordan Kim's membership in #general | Jordan Kim is a member of #general; reacted 👍 to the #announcements message about the security audit | Alternative through Jordan Kim |
| Jordan Patel's membership in #general | Jordan Patel is a member of #general; reacted 👀 (not 👍) to the #announcements message about the security audit | Wrong emoji only |
| Jordan Nguyen's membership in #general | Jordan Nguyen is a member of #general; reacted 👍 to a #announcements message about budget planning | Wrong message topic only |
| Jordan Ahmed's membership in #general | Jordan Ahmed is a member of #general; reacted 👍 to the security-audit message, but that message is located in #security-team, not #announcements | Wrong message location only |
| Jordan Diaz's membership in #random | Jordan Diaz reacted 👍 to the #announcements message about the security audit, but Jordan Diaz's membership is in #random, not #general | Wrong membership conversation only |

No choice between Jordan Lee and Jordan Kim is authorized by the request.