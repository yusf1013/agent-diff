## Audit

**Selection conditions extracted (independent of the asked answer):** emoji = 🚀; reacted-to message is the "launch checklist" message; that message's conversation record has a conversation-membership entry for Priya. The admin/owner flag is the *answer*, not a filter — so Ben legitimately qualifies even though his flag reads negative.

**Capability match:** downstream read = admin/owner flag on the qualifying user's discoverable workspace-membership profile association. This is exactly the supported read in the menu (no write exists for workspace membership). Alice/Ben are the User(1) position in the route, so reading their profile flags is the correct terminal operation — not a substitution of referent.

**Recomputed roots:** Only Alice and Ben have a complete chain (🚀 → correct message → #launch-prep → Priya's membership in #launch-prep). Chloe, Diego, Elena, Farid each break exactly one link and have no alternate qualifying chain elsewhere in the shared environment (checked: Elena's message differs only in channel, not text, so re-adding Priya to #marketing's membership — and only that — would make her qualify, confirming a single-point failure). Count matches assigned mode (multiple, 2 intended roots).

**Condition → negative mapping:**
- emoji condition → Chloe (👍 instead of 🚀)
- message-identity condition → Diego (right channel/emoji, wrong message)
- conversation-membership condition → Elena (right message text/emoji, wrong channel lacking Priya)
- missing-edge (no reaction at all) → Farid

No equality was invented between an unrelated membership channel and the message's location channel: Priya's membership is checked on the *same* conversation record where the qualifying message sits, per route.

**Repairs made:** none required; original sketch is coherent under audit. Wording kept unchanged.

## Final sketch

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