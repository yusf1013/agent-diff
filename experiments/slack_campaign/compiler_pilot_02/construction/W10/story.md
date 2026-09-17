**Route:** Workspace Membership → User → Reaction → Message → Conversation → Conversation Membership
**Mode:** multiple

**Request:**
"Are the people who reacted with a rocket to the launch-checklist message, in the channel that has Priya as a member, workspace admins or owners?"

**Selection conditions:** emoji 🚀; message is the launch-checklist message; the reacted-to message's channel has Priya as a conversation member.

| Referent | Environment facts | Interpretation |
|---|---|---|
| Alice | 🚀 on "Launch checklist ready for review" (M) in #launch-prep; #launch-prep has Priya as a member; Alice's profile shows workspace-admin flag | Match |
| Ben | 🚀 on M in #launch-prep (same channel, same Priya membership); also 👀 on an unrelated "lunch order" message elsewhere; profile shows admin/owner flags false | Match with unrelated activity |
| Chloe | 👍 (not 🚀) on M in #launch-prep | Wrong emoji only |
| Diego | 🚀 on a different message "Launch party invite" (N) in #launch-prep | Wrong message only |
| Elena | 🚀 on a same-text message "Launch checklist ready for review" (M2) posted in #marketing; Priya is not a member of #marketing | Conversation lacks required membership |
| Farid | Member of #launch-prep alongside Priya; no reactions on any message | Missing reaction relationship |

Note: M is one shared message referenced identically by Alice and Ben; their qualifying reactions do not extend to Chloe, Diego, Elena, or Farid, each of whom needs an independent complete chain.
