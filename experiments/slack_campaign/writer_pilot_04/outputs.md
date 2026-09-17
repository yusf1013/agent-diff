# All ten initial v4 sketches

Model output is reproduced verbatim below; Interpretation labels and audits are author claims. See the [manual comparison](review.md). No compiler or solver ran.

## W01 — R083 — multiple

[Assignment](W01/input.md) · [Native request](W01/writer/turn-01/request.json) · [Raw output](W01/writer/turn-01/output.md) · [Recorded thinking](W01/writer/turn-01/thinking.txt)

Route: Message → Reaction → User
Resolution mode: multiple

**Request:** "Add a 🚀 to the messages that Priya reacted to with raised_hands."

**Selection conditions:** message received a reaction with emoji raised_hands, and that reaction's reactor is Priya.

| Referent | Environment facts | Interpretation |
|---|---|---|
| "Rocket specs draft" (M1) | Priya 🙌 (raised_hands) | Match |
| "Budget review" (M2) | Priya 🙌 (raised_hands); also Diego 👀 (unrelated) | Match with unrelated activity |
| "Vendor contract" (M3) | Priya 👀 only | Wrong emoji only |
| "Timeline update" (M4) | Diego 🙌 (raised_hands) | Wrong person only |
| "Design mockup" (M5) | No reactions; other message facts unchanged | Missing reaction relationship |
| "Marketing plan" (M6) | Priya 👀 and Diego 🙌 (raised_hands) | Person and emoji occur on different reactions |

---

## W02 — R146 — single

[Assignment](W02/input.md) · [Native request](W02/writer/turn-01/request.json) · [Raw output](W02/writer/turn-01/output.md) · [Recorded thinking](W02/writer/turn-01/thinking.txt)

# W02 — User → Reaction → Message (single)

**Request:** DM the person who reacted with 🔥 to the budget-freeze announcement in #finance: "Heads up — the follow-up meeting on this is Thursday at 2pm."

**Selection conditions:** contributed a 🔥 reaction; that reaction is attached to the budget-freeze announcement message posted in #finance.

| Referent | Environment facts | Interpretation |
|---|---|---|
| Dana | Reacted 🔥 to the budget-freeze announcement message in #finance (authored by Priya) | Match |
| Wes | Reacted 👍 to that same budget-freeze announcement message in #finance | Wrong emoji only |
| Nora | Reacted 🔥 to a separate office-relocation announcement message in #general | Wrong message only |
| Priya | Authored the budget-freeze announcement message in #finance but did not react to it | Author substituted for reactor |

---

## W03 — R024 — underspecified

[Assignment](W03/input.md) · [Native request](W03/writer/turn-01/request.json) · [Raw output](W03/writer/turn-01/output.md) · [Recorded thinking](W03/writer/turn-01/thinking.txt)

Route: Conversation → Message → Reaction → User
Resolution mode: underspecified

**Request:** Post "Kickoff meeting moved to Monday" in the channel with the budget-approved message that Alex reacted to with 🎉.

**Selection conditions:** conversation contains a message whose text concerns a budget being approved, that message received a 🎉 reaction from a user whose first name is Alex.

| Referent | Environment facts | Interpretation |
|---|---|---|
| finance-updates | Alex Rivera reacted 🎉 to its "Q3 budget approved" message | Alternative through Alex Rivera |
| planning-sync | Alex Kim reacted 🎉 to its "marketing budget approved" message | Alternative through Alex Kim |
| vendor-notes | Alex Rivera reacted 👍 to its "budget approved" message | Wrong emoji only |
| team-social | Alex Kim reacted 🎉 to its "office party announcement" message | Wrong message topic only |

Note: the two alternatives are distinguished only by the reactor's surname (Alex Rivera vs. Alex Kim), a detail the request omits; no choice between them is authorized.

---

## W04 — R089 — absent

[Assignment](W04/input.md) · [Native request](W04/writer/turn-01/request.json) · [Raw output](W04/writer/turn-01/output.md) · [Recorded thinking](W04/writer/turn-01/thinking.txt)

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

---

## W05 — R009 — multiple

[Assignment](W05/input.md) · [Native request](W05/writer/turn-01/request.json) · [Raw output](W05/writer/turn-01/output.md) · [Recorded thinking](W05/writer/turn-01/thinking.txt)

**Route:** Conversation → Conversation Membership
**Resolution mode:** multiple

**Request:** "Post 'Please complete the compliance training module by end of this week.' to the onboarding channels that have exactly 6 members."

**Selection conditions:** public channel whose name/topic concerns new-hire onboarding; exactly 6 conversation members (actor included if a member).

| Referent | Environment facts | Interpretation |
|---|---|---|
| #onboarding-fall | Public channel, topic "New hire onboarding cohort", 6 conversation members | Match |
| #onboarding-spring | Public channel, topic "New hire onboarding cohort", 6 conversation members; one member also belongs to several unrelated channels and has posted unrelated messages elsewhere | Match with unrelated activity |
| #onboarding-winter | Public channel, topic "New hire onboarding cohort", but only 4 conversation members | Wrong member count only |
| #marketing-launch | Public channel, topic "Q3 product launch planning", 6 conversation members | Wrong topic/name (not onboarding) only |
| #onboarding-legacy | Private channel, topic "New hire onboarding cohort", 6 conversation members, actor not a member | Not discoverable/public — fails container access |
| #onboarding-eu | Public channel, topic "New hire onboarding cohort", 6 conversation memberships recorded but one is a workspace membership rather than a conversation membership for this channel | Miscounted membership binding — true conversation-member count is 5 |

---

## W06 — R078 — multiple

[Assignment](W06/input.md) · [Native request](W06/writer/turn-01/request.json) · [Raw output](W06/writer/turn-01/output.md) · [Recorded thinking](W06/writer/turn-01/thinking.txt)

**Route:** Message → User → Conversation Membership → Conversation
**Resolution mode:** multiple

**Request:** "Add 👀 to the messages from people who are members of #mentorship-hub."

**Selection conditions:** the message's author holds a conversation-membership record in the conversation named #mentorship-hub (the message itself may be posted anywhere).

| Referent | Environment facts | Interpretation |
|---|---|---|
| M1 (Dana) | Dana authored M1 in #general; Dana holds membership in #mentorship-hub | Match |
| M2 (Farid) | Farid authored M2 in #random; Farid holds membership in #mentorship-hub; M2 also carries an unrelated 👍 from Priya | Match with unrelated activity |
| M3 (Priya) | Priya authored M3 in #general; Priya's only conversation membership is #general | Wrong conversation only |
| M4 (Owen) | Owen authored M4 in #general; Owen holds membership in #mentors-lounge (similarly named, distinct channel) | Wrong conversation only (near-name decoy) |
| M5 (Lucia) | Lucia authored M5 in #general; Lucia holds no conversation memberships (only workspace membership) | Missing membership relationship |
| M6 (Theo) | Theo authored M6 posted directly in #mentorship-hub; Theo holds no membership in #mentorship-hub (posted while not a member) | Message location mistaken for membership; membership condition fails |

---

## W07 — R058 — underspecified

[Assignment](W07/input.md) · [Native request](W07/writer/turn-01/request.json) · [Raw output](W07/writer/turn-01/output.md) · [Recorded thinking](W07/writer/turn-01/thinking.txt)

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

---

## W08 — R108 — single

[Assignment](W08/input.md) · [Native request](W08/writer/turn-01/request.json) · [Raw output](W08/writer/turn-01/output.md) · [Recorded thinking](W08/writer/turn-01/thinking.txt)

# Assignment W08 — Reaction removal

**Route:** Reaction → Message → User → Conversation Membership → Conversation
**Mode:** single

**Exact user request:**
"Remove my fire reaction from the message posted by the member of the channel about launch readiness."

**Selection conditions:** the reaction is my own 🔥 reaction, on a message authored by a user, where that author holds membership in the conversation whose topic concerns launch readiness (membership record, not merely posting location, in that conversation).

| Referent | Environment facts | Interpretation |
|---|---|---|
| Nina's 🔥 on Kevin's message in #general | Kevin authored the message; Kevin holds membership in #product-launch, topic "Launch readiness plan"; I (Nina) reacted 🔥 to Kevin's message | Match |
| Nina's 👀 on Kevin's message in #general | Same Kevin, same #product-launch membership, but I reacted 👀 instead of 🔥 | Wrong emoji only |
| Sam's 🔥 on Kevin's message in #general | Same Kevin, same #product-launch membership, message reacted 🔥 by Sam, not by me | Wrong reactor (not actor-owned) |
| Nina's 🔥 on Priya's message in #general | Priya authored the message; Priya holds membership only in #design-crew (topic "Design crit queue"), not #product-launch; I reacted 🔥 | Wrong author's conversation membership |
| Nina's 🔥 on Elena's message posted in #product-launch | Elena authored and posted the message directly inside #product-launch, but holds no membership record there — she is only a member of #marketing-updates; I reacted 🔥 | Message location mistaken for membership (binding missing) |

**Note:** Row 5 keeps the message's posting location inside #product-launch to show that channel presence of the message is not equivalent to the author holding a membership record in that conversation; the membership condition must be satisfied by an actual Conversation Membership row, not by co-location.

---

## W09 — R154 — absent

[Assignment](W09/input.md) · [Native request](W09/writer/turn-01/request.json) · [Raw output](W09/writer/turn-01/output.md) · [Recorded thinking](W09/writer/turn-01/thinking.txt)

Route: Workspace → Workspace Membership → User → Conversation Membership → Conversation
Resolution mode: absent

**Request:** "What workspace is shown on the profile of the bot that belongs to the #incident-response channel?"

**Selection conditions:** the target is the workspace membership (and its workspace) held by the user who (a) is classified as a bot, and (b) holds a conversation membership belonging to the #incident-response channel.

| Referent | Environment facts | Interpretation |
|---|---|---|
| Cascade Systems (via WatcherBot) | WatcherBot is bot-flagged, holds workspace membership in Cascade Systems, and is a member of #project-launch | Wrong conversation membership only |
| Nimbus Robotics (via Dana Reyes) | Dana Reyes is a non-bot user holding workspace membership in Nimbus Robotics and is a member of #incident-response | User is not bot-flagged (bot condition fails) |
| — (via PulseBot) | PulseBot is bot-flagged and is a member of #incident-response, but holds no workspace membership record | Missing required workspace membership (position 1 absent) |

---

## W10 — R212 — multiple

[Assignment](W10/input.md) · [Native request](W10/writer/turn-01/request.json) · [Raw output](W10/writer/turn-01/output.md) · [Recorded thinking](W10/writer/turn-01/thinking.txt)

# Assignment W10 — Workspace Membership benchmark

**Route:** Workspace Membership → User → Reaction → Message → Conversation → Conversation Membership
**Mode:** multiple

**Request:**
"Are the people who reacted with a rocket to the launch-checklist message, in the channel that has Priya as a member, workspace admins or owners?"

**Selection conditions:** emoji 🚀; message is the launch-checklist message; the reacted-to message's channel has Priya as a conversation member. (The downstream read is the admin/owner flag on each qualifying user's discoverable workspace-membership profile.)

| Referent | Environment facts | Interpretation |
|---|---|---|
| Alice | 🚀 on "Launch checklist ready for review" (M) in #launch-prep; #launch-prep has Priya as a member; Alice's profile shows workspace-admin flag | Match |
| Ben | 🚀 on M in #launch-prep (same channel, same Priya membership); also 👀 on an unrelated "lunch order" message elsewhere; profile shows owner flag false/admin false | Match with unrelated activity |
| Chloe | 👍 (not 🚀) on M in #launch-prep | Wrong emoji only |
| Diego | 🚀 on a different message "Launch party invite" (N) in #launch-prep | Wrong message only |
| Elena | 🚀 on a same-text message "Launch checklist ready for review" (M2) posted in #marketing; Priya is not a member of #marketing | Conversation lacks required membership |
| Farid | Member of #launch-prep alongside Priya; no reactions on any message | Missing reaction relationship |

Note: M is one shared message referenced identically by Alice and Ben; their qualifying reactions do not extend to Chloe, Diego, Elena, or Farid, each of whom needs an independent complete chain.

---
