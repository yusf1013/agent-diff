# Manual Slack exemplars — W01–W10

Manually authored design examples, preserving the [W01–W10 route/mode assignments](../slack_campaign/writer_pilot_04/assignments.json). These are conceptual stories, not compiled or executed tests. Each entry describes a separate environment.

Tables specify current facts after setup. Repeated names or message labels within an entry denote the same records; different message labels denote distinct messages. Names identify one person unless alternatives are explicitly shown. Labels such as M1 are private table labels, not text to put in the messages. Message content should be ordinary and should not hint at the requested action or a row's test role.

The actor can read the scenario's channels and messages. Channels are in the actor's selected workspace; a user's displayed workspace association may differ where explicitly stated. Setup and background activity must preserve the table's matching roots and fixed membership facts. Member counts include the actor where present.

## W01

**Route:** Message → Reaction → User

**Resolution mode:** multiple — two jointly intended messages.

**Request:** Add 🚀 to the messages Priya reacted to with 🙌.

| Referent | Environment facts | Interpretation |
|---|---|---|
| M1 | Priya reacted 🙌. | Match |
| M2 | Priya reacted 🙌; Diego also reacted 👀. | Match with unrelated activity |
| M3 | Priya reacted 👀, with no other reactions. | Wrong emoji only |
| M4 | Diego reacted 🙌, with no other reactions. | Wrong person only |
| M5 | The message has no reactions. | Missing reaction relationship |
| M6 | Priya reacted 👀 and Diego reacted 🙌. These are the only reactions. | Person and emoji occur on different reactions; no single qualifying reaction |

## W02

**Route:** User → Reaction → Message

**Resolution mode:** single — one recipient.

**Request:** DM the person who reacted with 🔥 to the budget-freeze announcement in #finance: “The follow-up meeting is Thursday at 2pm.”

| Referent | Environment facts | Interpretation |
|---|---|---|
| Dana | Reacted 🔥 to budget-freeze announcement M1 in #finance. | Match |
| Wes | Reacted 👍 to M1; has no 🔥 reaction on it. | Wrong emoji only |
| Nora | Reacted 🔥 to office-relocation announcement M2 in #finance; did not react to M1. M2 discusses only the office relocation. | Wrong message topic only |
| Imani | Reacted 🔥 to budget-freeze announcement M3 in #operations; did not react to M1. | Wrong message channel only |
| Priya | Authored M1 but has no reactions. | Author is not a reactor; missing reaction relationship |
| Omar | Reacted 👍 to M1 and 🔥 to M2; has no other reactions. | Requested emoji and requested announcement occur on different reactions |

## W03

**Route:** Conversation → Message → Reaction → User

**Resolution mode:** underspecified — one channel is requested; two singleton alternatives remain.

**Request:** Post “Please send feedback by Friday.” in the channel with the budget-approved message Alex reacted to with 🎉.

| Referent | Environment facts | Interpretation |
|---|---|---|
| #finance-updates | Contains budget-approved message M1, which Alex Rivera reacted to with 🎉. | Alternative through Alex Rivera |
| #planning-sync | Contains a different budget-approved message M2, which Alex Kim reacted to with 🎉. | Alternative through Alex Kim |
| #vendor-updates | Contains budget-approved message M3. Alex Rivera reacted 👍, with no other reactions. | Wrong emoji only |
| #office-updates | Contains office-relocation message M4, which Alex Kim reacted to with 🎉. M4 does not discuss budgets. | Wrong message topic only |
| #procurement-updates | Contains budget-approved message M5, which Morgan reacted to with 🎉. Neither Alex reacted to it. | Wrong reactor name only |
| #delivery-updates | Contains budget-approved message M6. Alex Rivera reacted 👍 and Morgan reacted 🎉; these are its only reactions. | Alex and 🎉 occur on different reactions |
| #purchasing-updates | Contains budget-approved message M7, authored by Alex Rivera. Its only reaction is Morgan's 🎉; neither Alex reacted to it. | Alex is the author, not the reactor |

## W04

**Route:** Message → Reaction → User → Conversation Membership → Conversation

**Resolution mode:** absent — no message satisfies the complete description.

**Request:** Reply to the rollout-checklist message that got a 🚀 reaction from a member of #beta-testers: “Please confirm the final go-ahead timing.”

| Referent | Environment facts | Interpretation |
|---|---|---|
| M1 | A rollout-checklist message. Its only reaction is Ethan's 🚀. Ethan belongs to #customer-care, not #beta-testers. | Wrong reactor membership only |
| M2 | A distinct rollout-checklist message. Its only reaction is Farah's 👍. Farah belongs to #beta-testers. | Wrong emoji only |
| M3 | An office-relocation announcement about room assignments and moving dates. Its only reaction is Grace's 🚀. Grace belongs to #beta-testers. It does not discuss a product rollout or checklist. | Wrong message topic only |
| M4 | A rollout-checklist message. Farah reacted 👀 and Ethan reacted 🚀; these are its only reactions. | 🚀 and #beta-testers membership belong to different reactors |
| M5 | A rollout-checklist message with no reactions. | Missing reaction relationship |
| M6 | A rollout-checklist message. Its only reaction is Harold's 🚀. Harold belongs to #beta-testers-west, not #beta-testers. | Wrong membership channel only; the similarly named channel is distinct |
| M7 | A rollout-checklist message authored by Farah, who belongs to #beta-testers. Its only reaction is Ethan's 🚀; Ethan does not belong to #beta-testers. | The author has the required membership, but the reactor does not |

## W05

**Route:** Conversation → Conversation Membership

**Resolution mode:** multiple — two jointly intended channels.

**Request:** Post “Please complete the compliance training module by Friday.” to the onboarding channels with exactly six members.

| Referent | Environment facts | Interpretation |
|---|---|---|
| #onboarding-fall | Public channel for new-hire onboarding; exactly six current members, including the actor. | Match |
| #onboarding-spring | Private channel for new-hire onboarding; exactly six current members, including the actor. One member also belongs to unrelated channels. | Match; privacy and unrelated memberships do not exclude it |
| #onboarding-winter | New-hire onboarding channel; exactly five current members, including the actor. | Wrong member count only — below six |
| #onboarding-summer | New-hire onboarding channel; exactly seven current members, including the actor. | Wrong member count only — above six |
| #office-move | Channel for office-relocation logistics; exactly six current members, including the actor. Its content does not concern onboarding. | Wrong channel purpose/topic only |

## W06

**Route:** Message → User → Conversation Membership → Conversation

**Resolution mode:** multiple — two jointly intended messages.

**Request:** Add 👀 to the messages from people who are members of #mentorship-hub.

| Referent | Environment facts | Interpretation |
|---|---|---|
| M1 | Dana authored this message in #general. Dana currently belongs to #general and #mentorship-hub. | Match |
| M2 | Farid authored this message in #random. Farid currently belongs to #random and #mentorship-hub. Priya also reacted 👍 to M2. | Match with unrelated activity |
| M3 | Priya authored this message in #general. Priya currently belongs only to #general. | Wrong author membership channel only |
| M4 | Owen authored this message in #general. Owen currently belongs to #general and #mentors-lounge, not #mentorship-hub. | Wrong author membership channel only; the similarly named channel is distinct |
| M5 | Lucia authored this message in #general before leaving her channels. Lucia retains workspace membership but currently has no channel memberships. | Missing author-to-channel membership relationship |
| M6 | Theo authored this message in #mentorship-hub before leaving that channel. Theo currently belongs only to #general. | Message location does not establish the author's current membership |

## W07

**Route:** Conversation Membership → User → Reaction → Message → Conversation

**Resolution mode:** underspecified — one membership is requested; two singleton alternatives remain.

**Request:** Remove from #team-hub the member named Jordan who reacted with 👍 to the security-audit message in #announcements.

| Referent | Environment facts | Interpretation |
|---|---|---|
| Jordan Lee's #team-hub membership | Jordan Lee reacted 👍 to security-audit message M1 in #announcements. | Alternative through Jordan Lee |
| Jordan Kim's #team-hub membership | Jordan Kim reacted 👍 to the same M1. | Alternative through Jordan Kim |
| Jordan Patel's #team-hub membership | Jordan Patel reacted 👀 to M1 and has no 👍 reaction on it. | Wrong emoji only |
| Jordan Nguyen's #team-hub membership | Jordan Nguyen reacted 👍 to office-relocation message M2 in #announcements, not to M1. M2 does not discuss security audits. | Wrong message topic only |
| Jordan Ahmed's #team-hub membership | Jordan Ahmed reacted 👍 to security-audit message M3 in #security-team, not to M1. | Wrong message channel only |
| Jordan Diaz's #random membership | Jordan Diaz reacted 👍 to M1 but has no #team-hub membership. | Wrong membership channel only |
| Morgan Lee's #team-hub membership | Morgan Lee reacted 👍 to M1. Morgan is not named Jordan. | Wrong person's first name only |
| Jordan Park's #team-hub membership | Jordan Park reacted 👀 to M1 and 👍 to M2; has no other reactions. | Requested emoji and requested message occur on different reactions |

## W08

**Route:** Reaction → Message → User → Conversation Membership → Conversation

**Resolution mode:** single — one actor-owned reaction.

**Request:** Remove my 🔥 reaction from the message written by a member of the channel about launch readiness.

| Referent | Environment facts | Interpretation |
|---|---|---|
| Nina's 🔥 on M1 | Nina is the actor. Kevin wrote M1 in #general and belongs to #general and #product-launch. The latter's topic is “Launch readiness plan.” | Match |
| Nina's 👀 on M1 | Same actor, message, author and memberships; a separate 👀 reaction. | Wrong emoji only |
| Sam's 🔥 on M1 | Same message, author and memberships; Sam is a different person from Nina. | Wrong reactor only |
| Nina's 🔥 on M2 | Priya wrote M2 in #general. Priya belongs to #general and #design-crew, whose topic is “Weekly visual-design reviews”; she does not belong to #product-launch. | Wrong author membership channel only |
| Nina's 🔥 on M3 | Elena wrote M3 in #product-launch before leaving that channel. She now belongs only to #marketing-updates, whose topic is “Marketing campaign updates.” | Message location does not establish the author's current membership |

## W09

**Route:** Workspace → Workspace Membership → User → Conversation Membership → Conversation

**Resolution mode:** absent — no workspace has a user satisfying both bot and channel-membership conditions.

**Request:** What workspace is shown on the profile of the bot in #incident-response?

| Referent | Environment facts | Interpretation |
|---|---|---|
| Atlas, through WatcherBot | WatcherBot is marked as a bot. Its profile displays its Atlas workspace association. It belongs to #project-launch, not #incident-response. Atlas's other users, including the actor, are not bots. | Wrong channel membership only |
| Nimbus, through Dana Reyes | Dana is a human user, marked as not a bot. Her profile displays her Nimbus workspace association. She belongs to #incident-response. Nimbus has no bot users. | Wrong user classification only |

## W10

**Route:** Workspace Membership → User → Reaction → Message → Conversation → Conversation Membership

**Resolution mode:** multiple — two jointly intended workspace memberships.

**Request:** For the people who reacted with 🚀 to the launch-checklist message in the channel Priya belongs to, tell me whether each is a workspace admin or owner.

| Referent | Environment facts | Interpretation |
|---|---|---|
| Alice's workspace membership | Alice reacted 🚀 to checklist message M1 in #launch-prep. Priya belongs to #launch-prep. Alice's profile shows admin true, owner false. Morgan authored M1. | Match; answer is admin |
| Ben's workspace membership | Ben reacted 🚀 to the same M1 and 👀 to an unrelated lunch message elsewhere. His profile shows admin false, owner false. | Match with unrelated activity; answer is neither |
| Chloe's workspace membership | Chloe reacted 👍 to M1, with no 🚀 reaction on it. Her profile shows admin true. | Wrong emoji only; her admin status does not make her a match |
| Diego's workspace membership | Diego reacted 🚀 to office-relocation message M2 in #launch-prep, not to M1. M2 does not discuss a launch checklist. His profile shows owner true. | Wrong message topic only |
| Elena's workspace membership | Elena reacted 🚀 to checklist message M3 in #marketing. M3 has the same text and author, Morgan, as M1. Priya does not belong to #marketing. | Wrong channel membership only; message text and authorship do not distinguish the two channels |
| Farid's workspace membership | Farid belongs to #launch-prep alongside Priya but has no reactions. | Missing reaction relationship; channel membership is not a reaction |
| Grace's workspace membership | Grace reacted 👍 to M1 and 🚀 to M2; has no other reactions. | Requested emoji and checklist occur on different reactions |
