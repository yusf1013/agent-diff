# All ten reflected v4 sketches

Model output is reproduced verbatim below; Interpretation labels and audits are author claims. See the [manual comparison](../review.md). No compiler or solver ran.

## W01 — R083 — multiple

[Assignment](../W01/input.md) · [Native request](../W01/writer/turn-02/request.json) · [Raw output](../W01/writer/turn-02/output.md) · [Recorded thinking](../W01/writer/turn-02/thinking.txt)

**Audit**

- Selection conditions (independent of the write): a message must have received a reaction whose emoji is raised_hands AND whose reactor is Priya (same reaction record, not just same message).
- Downstream operation: add 🚀 (rocket) reaction — both raised_hands (read) and rocket (write) are in the supported emoji list, so this is a valid capability match. No restriction (e.g. "own reactor only") applies to reading raised_hands or to adding a new rocket reaction.
- Qualifying roots recomputed from all facts:
  - M1: Priya 🙌 → qualifies.
  - M2: Priya 🙌 (+ unrelated Diego 👀) → qualifies, extra activity doesn't disqualify.
  - M3: Priya 👀 only → fails emoji condition (no raised_hands reaction at all).
  - M4: Diego 🙌 → fails person condition (reactor isn't Priya).
  - M5: no reactions → fails relationship existence.
  - M6: Priya 👀 and Diego 🙌 → person and emoji present but on two different reaction records, so no single reaction satisfies both → fails the joint binding.
- Condition-to-negative mapping: emoji→M3, person→M4, existence→M5, joint binding→M6. All four distinct failure types covered; no negative accidentally has a second qualifying chain elsewhere (records aren't shared across rows).
- Count check: exactly 2 qualifying roots (M1, M2), matching assigned MULTIPLE count with one plain match and one match-with-extra-activity, as required.
- No discrepancies found; original sketch stands unchanged.

**Final sketch**

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

[Assignment](../W02/input.md) · [Native request](../W02/writer/turn-02/request.json) · [Raw output](../W02/writer/turn-02/output.md) · [Recorded thinking](../W02/writer/turn-02/thinking.txt)

## Audit

**Selection conditions (from request, independent of labels):** contributed a 🔥 reaction; that reaction record is attached to the budget-freeze announcement message located in #finance.

**Downstream operation/answer:** open a DM with the selected user and post a supplied message — matches the supported write "open a DM and message the selected user with a supplied purpose." No profile-read substitution needed.

**Reconstructed qualifying roots (all facts, ignoring labels):**
- Dana: reactor 🔥 → budget-freeze announcement (#finance). Complete chain — qualifies.
- Wes: reactor 👍 → same message. No 🔥 reaction anywhere else in the environment → no qualifying chain.
- Nora: reactor 🔥 → different message (office-relocation, #general). Reaction exists but not attached to the target message → no qualifying chain.
- Priya: author of target message, no reaction record at all → no Reaction→Message chain exists for her → no qualifying chain.

Only Dana has a complete User→Reaction→Message chain satisfying both the emoji and the message binding. Count = 1, matching SINGLE mode.

**Condition → negative mapping:**
- Emoji = 🔥 → Wes (has 👍 instead, same message otherwise binding-correct).
- Message = budget-freeze announcement in #finance → Nora (correct emoji, wrong message).
- Role = reactor (not author) → Priya (author of correct message, no reaction).

Each negative fails exactly one condition; no negative accidentally retains a complete alternate chain. No repairs required — sketch stands.

## Final sketch

Route: User → Reaction → Message
Resolution mode: single

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

[Assignment](../W03/input.md) · [Native request](../W03/writer/turn-02/request.json) · [Raw output](../W03/writer/turn-02/output.md) · [Recorded thinking](../W03/writer/turn-02/thinking.txt)

**Audit**

- Qualifying roots: exactly two, matching the intended alternatives — finance-updates (via Alex Rivera) and planning-sync (via Alex Kim). Both channels contain a message concerning a budget being approved that received a 🎉 reaction from a user first-named Alex; nothing disqualifies either.
- Condition inventory from the request: (1) message concerns "budget approved", (2) reaction emoji is 🎉, (3) reactor's first name is Alex. The surname distinguishing Rivera/Kim is the deliberately omitted detail, not a condition negatives may fail.
- Negative mapping found only two of three conditions covered (emoji, topic). Missing: a negative for the reactor-name condition itself (someone not named Alex reacting 🎉 to a qualifying "budget approved" message). Added row (mktg-notes / Jordan Lee) to fill that gap; it fails only the name condition, keeping topic and emoji correct.
- Rechecked no negative row supplies a second, hidden qualifying chain (e.g., Alex Rivera's other channel activity in vendor-notes stays in that channel only, doesn't leak into finance-updates).
- Capability: "post a supplied message" is a supported write for the selected conversation, matching the menu; distinguishable outcome (different channel receives the post) confirms the alternatives are consequential.
- Repair made: added the missing reactor-name negative row; no other changes needed.

**Final sketch**

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
| mktg-notes | Jordan Lee reacted 🎉 to its "budget approved" message | Wrong reactor name only |

Note: the two alternatives are distinguished only by the reactor's surname (Alex Rivera vs. Alex Kim), a detail the request omits; no choice between them is authorized.

---

## W04 — R089 — absent

[Assignment](../W04/input.md) · [Native request](../W04/writer/turn-02/request.json) · [Raw output](../W04/writer/turn-02/output.md) · [Recorded thinking](../W04/writer/turn-02/thinking.txt)

## Audit

**Selection conditions (independent of the requested reply):**
1. The message's topic is the rollout checklist.
2. The message received a 🚀 reaction.
3. The reactor holds a conversation membership specifically in #beta-testers.

**Qualifying roots reconstructed from stated facts:**
- No row satisfies all three conditions simultaneously — confirmed by re-checking each row against all three independently (not by trusting labels).
- Row A: message ✓, reaction ✓, membership ✗ (Ethan → #general only).
- Row B: message ✓, membership ✓ (Farah → #beta-testers), reaction ✗ (👍 not 🚀).
- Row C: reaction ✓, membership ✓ (Grace → #beta-testers), message ✗ (office relocation, unrelated topic).
- Row D: reaction ✓, membership ✓ (Harold → #beta-testers), message ✗ (different conversation/topic — marketing checklist, not rollout).

No cross-row combination produces an accidental full chain: each row's reaction, reactor, and membership are self-contained records: Ethan/general, Farah/👍, Grace/office-relocation, Harold/marketing-launch don't combine with each other's messages since Reaction is a message-user pair, not separable.

**Condition → negative row mapping:**
- Membership failure → Row A (real reaction to the right message, wrong channel membership).
- Emoji failure → Row B (right message, right membership, wrong emoji).
- Topic failure (unrelated) → Row C.
- Topic failure (superficially similar decoy) → Row D.

Population is not vacuous: #beta-testers has three distinct members (Farah, Grace, Harold) appearing across rows, so absence isn't due to an empty channel.

**Capability check:** downstream operation is "reply to a message with a supplied purpose," a supported write. The target message is identified purely by topic/reaction/membership chain, not by channel name in the request — consistent with route conditions. Since no message satisfies all three conditions, the reply has no valid target, matching absent mode without stating so.

No discrepancies found requiring repair; sketch retained as-is.

## Final sketch

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

[Assignment](../W05/input.md) · [Native request](../W05/writer/turn-02/request.json) · [Raw output](../W05/writer/turn-02/output.md) · [Recorded thinking](../W05/writer/turn-02/thinking.txt)

## Audit

**Roots reconstructed from all facts:**
- #onboarding-fall — onboarding topic, 6 members → qualifies.
- #onboarding-spring — onboarding topic, 6 members (extra unrelated member activity elsewhere doesn't disqualify) → qualifies.
- #onboarding-winter — onboarding topic, only 4 members → excluded, count fails.
- #marketing-launch — 6 members but topic unrelated to onboarding → excluded, topic fails.
- #onboarding-legacy — onboarding topic, 6 members, but private and actor not a member → outside discoverable population, excluded.
- Former row 6 was defective: a "conversation membership record" cannot actually be a workspace-membership record — these are separate relations/tables, so the construction was incoherent and admitted no real chain at all (neither a true negative nor a coherent match). Replaced with a genuine scope-based negative: an identically-purposed channel in a *different* workspace than the actor's selected one, which is excluded because discovery is limited to the actor's selected workspace, not because of any membership miscount.

**Condition → negative mapping:**
- Member count = 6 → #onboarding-winter (4 members).
- Topic concerns onboarding → #marketing-launch (unrelated topic).
- Discoverability (public, accessible) → #onboarding-legacy (private, non-member).
- Workspace scope (actor's selected workspace) → #onboarding-uk (right topic/count, wrong workspace).

**Capability check:** Member count is derived from conversation-membership records (H01) — a specific supported read. Topic is a directly stored/readable attribute. The downstream action, posting a supplied message, is a supported write requiring no extra capability beyond channel access, consistent with the two positive roots. Both negatives relying on access (private / other workspace) are excluded per the discovery rule limiting population to public channels in the actor's selected workspace.

**Repair:** Removed the incoherent membership-binding negative and replaced it with a workspace-scope negative that is structurally sound and does not conflate membership types.

## Final Sketch

**Route:** Conversation → Conversation Membership
**Resolution mode:** multiple

**Request:** "Post 'Please complete the compliance training module by end of this week.' to the onboarding channels that have exactly 6 members."

**Selection conditions:** public channel, in the actor's selected workspace, whose name/topic concerns new-hire onboarding; exactly 6 conversation members (actor included if a member).

| Referent | Environment facts | Interpretation |
|---|---|---|
| #onboarding-fall | Public channel in actor's workspace, topic "New hire onboarding cohort", 6 conversation members | Match |
| #onboarding-spring | Public channel in actor's workspace, topic "New hire onboarding cohort", 6 conversation members; one member also belongs to several unrelated channels and has posted unrelated messages elsewhere | Match with unrelated activity |
| #onboarding-winter | Public channel in actor's workspace, topic "New hire onboarding cohort", but only 4 conversation members | Wrong member count only |
| #marketing-launch | Public channel in actor's workspace, topic "Q3 product launch planning", 6 conversation members | Wrong topic/name (not onboarding) only |
| #onboarding-legacy | Private channel, topic "New hire onboarding cohort", 6 conversation members, actor not a member | Not publicly discoverable — access fails |
| #onboarding-uk | Public channel, topic "New hire onboarding cohort", 6 conversation members, but located in a different workspace than the actor's selected one | Outside actor's workspace scope — discovery fails |

---

## W06 — R078 — multiple

[Assignment](../W06/input.md) · [Native request](../W06/writer/turn-02/request.json) · [Raw output](../W06/writer/turn-02/output.md) · [Recorded thinking](../W06/writer/turn-02/thinking.txt)

**Audit**

- Qualifying roots (message referents whose author holds membership in #mentorship-hub): M1 (Dana), M2 (Farid). Exactly 2, matching assigned MULTIPLE count. M2's extra unrelated reaction from Priya does not disqualify it — Farid's own membership chain is complete.
- Condition extracted from request, independent of downstream action: author's User record must hold a Conversation-Membership record whose Conversation is #mentorship-hub. The reaction-add operation itself imposes no eligibility filter (any message can receive a reaction), so it cannot be used to exclude candidates — confirmed no property-as-eligibility error.
- Condition→negative mapping:
  - "author lacks membership in #mentorship-hub, holds an unrelated channel" → M3 (Priya, #general only).
  - "author holds membership in a similarly-named but distinct channel" (near-name decoy, tests topic/name precision) → M4 (Owen, #mentors-lounge).
  - "author holds no conversation membership at all" (missing-edge) → M5 (Lucia).
  - "message posted inside #mentorship-hub but author not a member of it" (binding confusion between message location and membership channel) → M6 (Theo).
  All four negatives fail the sole condition (membership-in-#mentorship-hub) while otherwise reading as plausible candidates; none accidentally re-qualifies through another record.
- Capability check: downstream operation is "add a supported reaction" (👀/eyes), which is in the supported emoji list and requires no authorship restriction on the target message — matches the menu's preferred write exactly. No read-only fallback needed.
- No discrepancies found; no repairs required. Wording, roots, and negatives are internally consistent and preserved.

---

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

[Assignment](../W07/input.md) · [Native request](../W07/writer/turn-02/request.json) · [Raw output](../W07/writer/turn-02/output.md) · [Recorded thinking](../W07/writer/turn-02/thinking.txt)

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

---

## W08 — R108 — single

[Assignment](../W08/input.md) · [Native request](../W08/writer/turn-02/request.json) · [Raw output](../W08/writer/turn-02/output.md) · [Recorded thinking](../W08/writer/turn-02/thinking.txt)

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

---

## W09 — R154 — absent

[Assignment](../W09/input.md) · [Native request](../W09/writer/turn-02/request.json) · [Raw output](../W09/writer/turn-02/output.md) · [Recorded thinking](../W09/writer/turn-02/thinking.txt)

**Audit**

- Extracted conditions (independent of the requested answer): user must be (a) bot-flagged, (b) hold a conversation membership belonging to #incident-response, (c) hold a workspace membership (whose workspace is the reported answer). The answer itself ("which workspace") is not usable to exclude candidates — a candidate lacking workspace membership legitimately yields "no workspace shown," not disqualification.
- Qualifying-root recomputation across all facts: no row satisfies bot + #incident-response membership + workspace membership simultaneously. WatcherBot satisfies bot+workspace membership but wrong channel (#project-launch). Dana Reyes satisfies channel+workspace membership but is not bot-flagged. PulseBot satisfies bot+channel but has no workspace membership. No hidden overlap (e.g., no second bot, no other #incident-response member with a workspace) creates an accidental full chain. Count of full matches = 0, as assigned.
- Condition→negative mapping:
  - Bot-flag condition → Dana Reyes (fails only this).
  - Conversation-membership-in-#incident-response condition → WatcherBot (fails only this).
  - Workspace-membership-existence condition → PulseBot (fails only this).
  All three independently variable conditions each have a dedicated negative; no condition is left unchallenged, and each negative satisfies the other two conditions under ordinary reading.
- Capability check: the downstream operation is the supported read "workspace identifier exposed by discoverable users' profiles." For WatcherBot/Dana Reyes, a workspace value (Cascade Systems / Nimbus Robotics) would be readable and distinguishable from any other candidate's workspace — so a wrong candidate produces a distinguishable, non-revealing answer. For PulseBot, absence of workspace membership means no workspace is exposed on profile — a legitimate observable outcome, not an invented restriction. No write capability applies to Workspace per the menu; the read fallback is correctly used.
- No discrepancies found requiring repair to names, chain bindings, or wording; the sketch already avoids an empty-channel or fully-vacant-population defect (channel has a real, non-bot member; bots exist elsewhere and with missing workspace ties).

**Final sketch**

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

[Assignment](../W10/input.md) · [Native request](../W10/writer/turn-02/request.json) · [Raw output](../W10/writer/turn-02/output.md) · [Recorded thinking](../W10/writer/turn-02/thinking.txt)

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

---
