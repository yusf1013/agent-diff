# Manual Slack exemplars — resolution variants

These 32 manually authored variants supplement the 10 originals in [story.md](story.md).
Every entry is a separate environment. The original story's conventions apply:
labels such as M1 are private table labels; repeated names identify the same records
unless distinct people are explicitly named; the actor can read every scenario channel.
Tables describe current facts, including exact membership counts. Neither the table
nor its interpretations are given to the solver.

Requests retain their short wording. Singular/plural changes distinguish one unresolved
target from a jointly intended collection where necessary. As explicitly agreed for
W01 (and applied to W05/W06/W10), a single variant can retain a plural request when the
supplied environment has exactly one match. This is an instance cardinality variant.
Underspecified candidate sets are alternatives, not permission to choose or combine them.

Full executable cases, including the originals, are indexed in [manifest.json](manifest.json).
The review and verification limits are documented in [review.md](review.md).

## W01-single

**Route:** Message → Reaction → User

**Resolution mode:** single

**Request:** Add 🚀 to the messages Priya reacted to with 🙌.

**Change from W01:** Remove M1 only; retain the plural request and every other row.

| Referent | Environment facts | Interpretation |
|---|---|---|
| M2 | Priya reacted 🙌; Diego also reacted 👀. | Match with unrelated activity |
| M3 | Priya reacted 👀, with no other reactions. | Wrong emoji only |
| M4 | Diego reacted 🙌, with no other reactions. | Wrong person only |
| M5 | The message has no reactions. | Missing reaction relationship |
| M6 | Priya reacted 👀 and Diego reacted 🙌. These are the only reactions. | Person and emoji occur on different reactions |

## W01-absent-authorship

**Route:** Message → Reaction → User

**Resolution mode:** absent

**Request:** Add 🚀 to the messages Priya reacted to with 🙌.

**Change from W01:** Replace Priya’s 🙌 reactions on M1/M2 with Priya’s authorship. Preserve Diego’s 👀 on M2.

| Referent | Environment facts | Interpretation |
|---|---|---|
| M1 | Authored by Priya; no reactions. | Authorship/text is not a reaction |
| M2 | Authored by Priya; Diego reacted 👀; no other reactions. | Authorship/text is not a reaction |
| M3 | Priya reacted 👀, with no other reactions. | Wrong emoji only |
| M4 | Diego reacted 🙌, with no other reactions. | Wrong person only |
| M5 | The message has no reactions. | Missing reaction relationship |
| M6 | Priya reacted 👀 and Diego reacted 🙌. These are the only reactions. | Person and emoji occur on different reactions |

## W01-absent-text-emoji

**Route:** Message → Reaction → User

**Resolution mode:** absent

**Request:** Add 🚀 to the messages Priya reacted to with 🙌.

**Change from W01:** As in absent-authorship, and include 🙌 in both authored message bodies, not as Priya’s reaction.

| Referent | Environment facts | Interpretation |
|---|---|---|
| M1 | Authored by Priya; 🙌 appears in the message text; no reactions. | Authorship/text is not a reaction |
| M2 | Authored by Priya; 🙌 appears in the message text; Diego reacted 👀; no other reactions. | Authorship/text is not a reaction |
| M3 | Priya reacted 👀, with no other reactions. | Wrong emoji only |
| M4 | Diego reacted 🙌, with no other reactions. | Wrong person only |
| M5 | The message has no reactions. | Missing reaction relationship |
| M6 | Priya reacted 👀 and Diego reacted 🙌. These are the only reactions. | Person and emoji occur on different reactions |

## W01-underspecified

**Route:** Message → Reaction → User

**Resolution mode:** underspecified

**Request:** Add 🚀 to the messages Priya reacted to with 🙌.

**Change from W01:** Keep Priya Shah on M1/M3/M6; add Priya Rao and make her the 🙌 reactor on M2.

| Referent | Environment facts | Interpretation |
|---|---|---|
| M1 | Priya Shah reacted 🙌. | Alternative through Priya Shah |
| M2 | Priya Rao reacted 🙌; Diego also reacted 👀. | Alternative through Priya Rao |
| M3 | Priya Shah reacted 👀, with no other reactions. | Wrong emoji only |
| M4 | Diego reacted 🙌, with no other reactions. | Wrong person only |
| M5 | The message has no reactions. | Missing reaction relationship |
| M6 | Priya Shah reacted 👀 and Diego reacted 🙌. These are the only reactions. | Person and emoji occur on different reactions |

Resolve messages with a raised_hands reaction by Priya on that same reaction record, then add rocket to those messages. Priya Shah and Priya Rao are distinct users. The intended message collection is {M1} for Shah or {M2} for Rao; the request does not identify which Priya. The alternatives are not a combined target set.

## W02-multiple

**Route:** User → Reaction → Message

**Resolution mode:** multiple

**Request:** DM the people who reacted with 🔥 to the budget-freeze announcement in #finance: “The follow-up meeting is Thursday at 2pm.”

**Change from W02:** Add Morgan’s 🔥 to M1; change person to people.

| Referent | Environment facts | Interpretation |
|---|---|---|
| Dana | Reacted 🔥 to budget-freeze announcement M1 in #finance. | Match |
| Wes | Reacted 👍 to M1; no 🔥 on it. | Wrong emoji only |
| Nora | Reacted 🔥 to office-relocation announcement M2 in #finance, not to M1. M2 concerns rooms and moving dates only. | Wrong message topic only |
| Imani | Reacted 🔥 to budget-freeze announcement M3 in #operations, not to M1. | Wrong message channel only |
| Priya | Authored M1 but has no reactions. | Author is not a reactor |
| Omar | Reacted 👍 to M1 and 🔥 to M2; no other reactions. | Emoji and announcement occur on different reactions |
| Morgan | Reacted 🔥 to the same M1 as Dana. | Match |

## W02-absent

**Route:** User → Reaction → Message

**Resolution mode:** absent

**Request:** DM the person who reacted with 🔥 to the budget-freeze announcement in #finance: “The follow-up meeting is Thursday at 2pm.”

**Change from W02:** Remove Dana’s 🔥 reaction; keep every other row.

| Referent | Environment facts | Interpretation |
|---|---|---|
| Dana | Has no reactions. | Missing reaction relationship |
| Wes | Reacted 👍 to M1; no 🔥 on it. | Wrong emoji only |
| Nora | Reacted 🔥 to office-relocation announcement M2 in #finance, not to M1. M2 concerns rooms and moving dates only. | Wrong message topic only |
| Imani | Reacted 🔥 to budget-freeze announcement M3 in #operations, not to M1. | Wrong message channel only |
| Priya | Authored M1 but has no reactions. | Author is not a reactor |
| Omar | Reacted 👍 to M1 and 🔥 to M2; no other reactions. | Emoji and announcement occur on different reactions |

## W02-underspecified-reactor

**Route:** User → Reaction → Message

**Resolution mode:** underspecified

**Request:** DM the person who reacted with 🔥 to the budget-freeze announcement in #finance: “The follow-up meeting is Thursday at 2pm.”

**Change from W02:** Add Morgan’s 🔥 to M1; preserve the singular person request.

| Referent | Environment facts | Interpretation |
|---|---|---|
| Dana | Reacted 🔥 to budget-freeze announcement M1 in #finance. | Alternative recipient |
| Wes | Reacted 👍 to M1; no 🔥 on it. | Wrong emoji only |
| Nora | Reacted 🔥 to office-relocation announcement M2 in #finance, not to M1. M2 concerns rooms and moving dates only. | Wrong message topic only |
| Imani | Reacted 🔥 to budget-freeze announcement M3 in #operations, not to M1. | Wrong message channel only |
| Priya | Authored M1 but has no reactions. | Author is not a reactor |
| Omar | Reacted 👍 to M1 and 🔥 to M2; no other reactions. | Emoji and announcement occur on different reactions |
| Morgan | Reacted 🔥 to the same M1 as Dana. | Alternative recipient |

Resolve the person who has a fire reaction on a budget-freeze announcement in #finance; emoji, message topic, and location must hold on the same reaction/message path. Send the requested DM. Dana and Morgan both reacted to the one announcement, but the singular request does not distinguish the intended person.

## W02-underspecified-announcement

**Route:** User → Reaction → Message

**Resolution mode:** underspecified

**Request:** DM the person who reacted with 🔥 to the budget-freeze announcement in #finance: “The follow-up meeting is Thursday at 2pm.”

**Change from W02:** Add a second budget-freeze announcement M4 in #finance and Morgan’s 🔥 on it; preserve the singular request.

| Referent | Environment facts | Interpretation |
|---|---|---|
| Dana | Reacted 🔥 to budget-freeze announcement M1 in #finance. | Alternative recipient |
| Wes | Reacted 👍 to M1; no 🔥 on it. | Wrong emoji only |
| Nora | Reacted 🔥 to office-relocation announcement M2 in #finance, not to M1. M2 concerns rooms and moving dates only. | Wrong message topic only |
| Imani | Reacted 🔥 to budget-freeze announcement M3 in #operations, not to M1. | Wrong message channel only |
| Priya | Authored M1 but has no reactions. | Author is not a reactor |
| Omar | Reacted 👍 to M1 and 🔥 to M2; no other reactions. | Emoji and announcement occur on different reactions |
| Morgan | Reacted 🔥 to a different budget-freeze announcement M4 in #finance; did not react to M1. | Alternative recipient |

Resolve the person who has a fire reaction on a budget-freeze announcement in #finance; emoji, message topic, and location must hold on the same reaction/message path. Send the requested DM. Two separate budget-freeze announcements in #finance lead to Dana and Morgan respectively; the request selects neither announcement. Recency is not a supplied selection rule.

## W03-single

**Route:** Conversation → Message → Reaction → User

**Resolution mode:** single

**Request:** Post “Please send feedback by Friday.” in the channel with the budget-approved message Alex Rivera reacted to with 🎉.

**Change from W03:** Name Alex Rivera explicitly. M4’s reactor is also Alex Rivera, preserving its isolated topic mismatch. Other records remain unchanged.

| Referent | Environment facts | Interpretation |
|---|---|---|
| #finance-updates | Contains budget-approved message M1, which Alex Rivera reacted to with 🎉. | Match |
| #planning-sync | Contains a different budget-approved message M2, which Alex Kim reacted to with 🎉. | Wrong reactor identity only; Alex Kim is not Alex Rivera |
| #vendor-updates | Contains budget-approved message M3. Alex Rivera reacted 👍, with no other reactions. | Wrong emoji only |
| #office-updates | Contains office-relocation message M4, which Alex Rivera reacted to with 🎉. M4 does not discuss budgets. | Wrong message topic only |
| #procurement-updates | Contains budget-approved message M5, which Morgan reacted to with 🎉. Neither Alex reacted to it. | Wrong reactor name only |
| #delivery-updates | Contains budget-approved message M6. Alex Rivera reacted 👍 and Morgan reacted 🎉; these are its only reactions. | Requested person and 🎉 occur on different reactions |
| #purchasing-updates | Contains budget-approved message M7, authored by Alex Rivera. Its only reaction is Morgan’s 🎉; neither Alex reacted to it. | Alex is the author, not the reactor |

## W03-multiple

**Route:** Conversation → Message → Reaction → User

**Resolution mode:** multiple

**Request:** Post “Please send feedback by Friday.” in the channels with the budget-approved messages Alex Rivera reacted to with 🎉.

**Change from W03:** Name Alex Rivera explicitly, use plural channels/messages, and change M2’s and M4’s reactor from Alex Kim to Alex Rivera. The two channels are jointly intended.

| Referent | Environment facts | Interpretation |
|---|---|---|
| #finance-updates | Contains budget-approved message M1, which Alex Rivera reacted to with 🎉. | Match |
| #planning-sync | Contains a different budget-approved message M2, which Alex Rivera reacted to with 🎉. | Match |
| #vendor-updates | Contains budget-approved message M3. Alex Rivera reacted 👍, with no other reactions. | Wrong emoji only |
| #office-updates | Contains office-relocation message M4, which Alex Rivera reacted to with 🎉. M4 does not discuss budgets. | Wrong message topic only |
| #procurement-updates | Contains budget-approved message M5, which Morgan reacted to with 🎉. Neither Alex reacted to it. | Wrong reactor name only |
| #delivery-updates | Contains budget-approved message M6. Alex Rivera reacted 👍 and Morgan reacted 🎉; these are its only reactions. | Requested person and 🎉 occur on different reactions |
| #purchasing-updates | Contains budget-approved message M7, authored by Alex Rivera. Its only reaction is Morgan’s 🎉; neither Alex reacted to it. | Alex is the author, not the reactor |

## W03-absent

**Route:** Conversation → Message → Reaction → User

**Resolution mode:** absent

**Request:** Post “Please send feedback by Friday.” in the channel with the budget-approved message Alex Rivera reacted to with 🎉.

**Change from W03:** Name Alex Rivera explicitly; change his M1 reaction to 👍. M4’s reactor becomes Alex Rivera so the office message remains an isolated topic negative.

| Referent | Environment facts | Interpretation |
|---|---|---|
| #finance-updates | Contains budget-approved message M1, which Alex Rivera reacted to with 👍. | Wrong emoji only |
| #planning-sync | Contains a different budget-approved message M2, which Alex Kim reacted to with 🎉. | Wrong reactor identity only; Alex Kim is not Alex Rivera |
| #vendor-updates | Contains budget-approved message M3. Alex Rivera reacted 👍, with no other reactions. | Wrong emoji only |
| #office-updates | Contains office-relocation message M4, which Alex Rivera reacted to with 🎉. M4 does not discuss budgets. | Wrong message topic only |
| #procurement-updates | Contains budget-approved message M5, which Morgan reacted to with 🎉. Neither Alex reacted to it. | Wrong reactor name only |
| #delivery-updates | Contains budget-approved message M6. Alex Rivera reacted 👍 and Morgan reacted 🎉; these are its only reactions. | Requested person and 🎉 occur on different reactions |
| #purchasing-updates | Contains budget-approved message M7, authored by Alex Rivera. Its only reaction is Morgan’s 🎉; neither Alex reacted to it. | Alex is the author, not the reactor |

## W04-single

**Route:** Message → Reaction → User → Conversation Membership → Conversation

**Resolution mode:** single

**Request:** Reply to the rollout-checklist message that got a 🚀 reaction from a member of #beta-testers: “Please confirm the final go-ahead timing.”

**Change from W04:** Keep all seven negatives and add one qualifying message, M8. The request is unchanged.

| Referent | Environment facts | Interpretation |
|---|---|---|
| M8 | A rollout-checklist message. Its only reaction is Farah’s 🚀; Farah belongs to #beta-testers. | Match |
| M1 | A rollout-checklist message. Its only reaction is Ethan’s 🚀. Ethan belongs to #customer-care, not #beta-testers. | Wrong reactor membership only |
| M2 | A distinct rollout-checklist message. Its only reaction is Farah’s 👍. Farah belongs to #beta-testers. | Wrong emoji only |
| M3 | An office-relocation announcement about room assignments and moving dates. Its only reaction is Grace’s 🚀. Grace belongs to #beta-testers. It does not discuss a product rollout or checklist. | Wrong message topic only |
| M4 | A rollout-checklist message. Farah reacted 👀 and Ethan reacted 🚀; these are its only reactions. | 🚀 and #beta-testers membership belong to different reactors |
| M5 | A rollout-checklist message with no reactions. | Missing reaction relationship |
| M6 | A rollout-checklist message. Its only reaction is Harold’s 🚀. Harold belongs to #beta-testers-west, not #beta-testers. | Wrong membership channel only; the similarly named channel is distinct |
| M7 | A rollout-checklist message authored by Farah, who belongs to #beta-testers. Its only reaction is Ethan’s 🚀; Ethan does not belong to #beta-testers. | The author has the required membership, but the reactor does not |

## W04-multiple

**Route:** Message → Reaction → User → Conversation Membership → Conversation

**Resolution mode:** multiple

**Request:** Reply to the rollout-checklist messages that got a 🚀 reaction from a member of #beta-testers: “Please confirm the final go-ahead timing.”

**Change from W04:** Keep all seven negatives and add M8 and M9. Pluralize message to messages so both are jointly intended.

| Referent | Environment facts | Interpretation |
|---|---|---|
| M8 | A rollout-checklist message. Its only reaction is Farah’s 🚀; Farah belongs to #beta-testers. | Match |
| M9 | A different rollout-checklist message. Grace reacted 🚀 and Ethan reacted 👀. Grace belongs to #beta-testers; Ethan does not. | Match with unrelated activity |
| M1 | A rollout-checklist message. Its only reaction is Ethan’s 🚀. Ethan belongs to #customer-care, not #beta-testers. | Wrong reactor membership only |
| M2 | A distinct rollout-checklist message. Its only reaction is Farah’s 👍. Farah belongs to #beta-testers. | Wrong emoji only |
| M3 | An office-relocation announcement about room assignments and moving dates. Its only reaction is Grace’s 🚀. Grace belongs to #beta-testers. It does not discuss a product rollout or checklist. | Wrong message topic only |
| M4 | A rollout-checklist message. Farah reacted 👀 and Ethan reacted 🚀; these are its only reactions. | 🚀 and #beta-testers membership belong to different reactors |
| M5 | A rollout-checklist message with no reactions. | Missing reaction relationship |
| M6 | A rollout-checklist message. Its only reaction is Harold’s 🚀. Harold belongs to #beta-testers-west, not #beta-testers. | Wrong membership channel only; the similarly named channel is distinct |
| M7 | A rollout-checklist message authored by Farah, who belongs to #beta-testers. Its only reaction is Ethan’s 🚀; Ethan does not belong to #beta-testers. | The author has the required membership, but the reactor does not |

## W04-underspecified

**Route:** Message → Reaction → User → Conversation Membership → Conversation

**Resolution mode:** underspecified

**Request:** Reply to the rollout-checklist message that got a 🚀 reaction from a member of #beta-testers: “Please confirm the final go-ahead timing.”

**Change from W04:** Use the same two qualifying messages as the multiple variant, with the original singular request. No condition distinguishes the intended message.

| Referent | Environment facts | Interpretation |
|---|---|---|
| M8 | A rollout-checklist message. Its only reaction is Farah’s 🚀; Farah belongs to #beta-testers. | Alternative through M8 |
| M9 | A different rollout-checklist message. Grace reacted 🚀 and Ethan reacted 👀. Grace belongs to #beta-testers; Ethan does not. | Alternative through M9 |
| M1 | A rollout-checklist message. Its only reaction is Ethan’s 🚀. Ethan belongs to #customer-care, not #beta-testers. | Wrong reactor membership only |
| M2 | A distinct rollout-checklist message. Its only reaction is Farah’s 👍. Farah belongs to #beta-testers. | Wrong emoji only |
| M3 | An office-relocation announcement about room assignments and moving dates. Its only reaction is Grace’s 🚀. Grace belongs to #beta-testers. It does not discuss a product rollout or checklist. | Wrong message topic only |
| M4 | A rollout-checklist message. Farah reacted 👀 and Ethan reacted 🚀; these are its only reactions. | 🚀 and #beta-testers membership belong to different reactors |
| M5 | A rollout-checklist message with no reactions. | Missing reaction relationship |
| M6 | A rollout-checklist message. Its only reaction is Harold’s 🚀. Harold belongs to #beta-testers-west, not #beta-testers. | Wrong membership channel only; the similarly named channel is distinct |
| M7 | A rollout-checklist message authored by Farah, who belongs to #beta-testers. Its only reaction is Ethan’s 🚀; Ethan does not belong to #beta-testers. | The author has the required membership, but the reactor does not |

Rollout-checklist messages with a 🚀 reaction whose reactor currently belongs to #beta-testers. The emoji and membership must bind the same reactor. One message is intended, but M8 and M9 remain competing alternatives.

## W05-single

**Route:** Conversation → Conversation Membership

**Resolution mode:** single

**Request:** Post “Please complete the compliance training module by Friday.” to the onboarding channels with exactly six members.

**Change from W05:** Remove #onboarding-fall. The private #onboarding-spring is the sole match; retain the original plural request.

| Referent | Environment facts | Interpretation |
|---|---|---|
| #onboarding-spring | Private channel for new-hire onboarding; exactly 6 current members, including the actor. One member also belongs to unrelated channels. | Match; privacy and unrelated memberships do not exclude it |
| #onboarding-winter | Public channel for new-hire onboarding; exactly 5 current members, including the actor. | Wrong member count only — below six |
| #onboarding-summer | Public channel for new-hire onboarding; exactly 7 current members, including the actor. | Wrong member count only — above six |
| #office-move | Public channel for office-relocation logistics; exactly 6 current members, including the actor. Its content does not concern onboarding. | Wrong channel purpose/topic only |

## W05-absent

**Route:** Conversation → Conversation Membership

**Resolution mode:** absent

**Request:** Post “Please complete the compliance training module by Friday.” to the onboarding channels with exactly six members.

**Change from W05:** Change #onboarding-fall to five members and #onboarding-spring to seven. The request and all other channel facts remain unchanged.

| Referent | Environment facts | Interpretation |
|---|---|---|
| #onboarding-fall | Public channel for new-hire onboarding; exactly 5 current members, including the actor. | Wrong member count only — below six |
| #onboarding-spring | Private channel for new-hire onboarding; exactly 7 current members, including the actor. One member also belongs to unrelated channels. | Wrong member count only — above six |
| #onboarding-winter | Public channel for new-hire onboarding; exactly 5 current members, including the actor. | Wrong member count only — below six |
| #onboarding-summer | Public channel for new-hire onboarding; exactly 7 current members, including the actor. | Wrong member count only — above six |
| #office-move | Public channel for office-relocation logistics; exactly 6 current members, including the actor. Its content does not concern onboarding. | Wrong channel purpose/topic only |

## W05-underspecified

**Route:** Conversation → Conversation Membership

**Resolution mode:** underspecified

**Request:** Post “Please complete the compliance training module by Friday.” to the onboarding channel with exactly six members.

**Change from W05:** Keep the original environment and change channels to channel. Both six-member onboarding channels remain alternatives; no choice is delegated.

| Referent | Environment facts | Interpretation |
|---|---|---|
| #onboarding-fall | Public channel for new-hire onboarding; exactly 6 current members, including the actor. | Alternative through #onboarding-fall |
| #onboarding-spring | Private channel for new-hire onboarding; exactly 6 current members, including the actor. One member also belongs to unrelated channels. | Alternative through #onboarding-spring |
| #onboarding-winter | Public channel for new-hire onboarding; exactly 5 current members, including the actor. | Wrong member count only — below six |
| #onboarding-summer | Public channel for new-hire onboarding; exactly 7 current members, including the actor. | Wrong member count only — above six |
| #office-move | Public channel for office-relocation logistics; exactly 6 current members, including the actor. Its content does not concern onboarding. | Wrong channel purpose/topic only |

Onboarding channels with exactly six current members, including the actor. Public/private status does not change eligibility. The singular request does not distinguish the two qualifying channels.

## W06-single

**Route:** Message → User → Conversation Membership → Conversation

**Resolution mode:** single

**Request:** Add 👀 to the messages from people who are members of #mentorship-hub.

**Change from W06:** Remove M1, leaving M2 as the sole qualifying message. Preserve the original plural request and all membership facts.

| Referent | Environment facts | Interpretation |
|---|---|---|
| M2 | Farid authored this message in #random. Farid currently belongs to #random and #mentorship-hub. Priya also reacted 👍 to M2. | Match with unrelated activity |
| M3 | Priya authored this message in #general. Priya currently belongs only to #general. | Wrong author membership channel only |
| M4 | Owen authored this message in #general. Owen currently belongs to #general and #mentors-lounge, not #mentorship-hub. | Wrong author membership channel only; the similarly named channel is distinct |
| M5 | Lucia authored this message in #general before leaving her channels. Lucia retains workspace membership but currently has no channel memberships. | Missing author-to-channel membership relationship |
| M6 | Theo authored this message in #mentorship-hub before leaving that channel. Theo currently belongs only to #general. | Message location does not establish the author’s current membership |

## W06-absent

**Route:** Message → User → Conversation Membership → Conversation

**Resolution mode:** absent

**Request:** Add 👀 to the messages from people who are members of #mentorship-hub.

**Change from W06:** Remove Dana’s and Farid’s #mentorship-hub memberships; retain their #general/#random memberships and every message. The actor has channel access but authors no messages.

| Referent | Environment facts | Interpretation |
|---|---|---|
| M1 | Dana authored this message in #general. Dana currently belongs only to #general; she does not belong to #mentorship-hub. | Wrong author membership channel only |
| M2 | Farid authored this message in #random. Farid currently belongs only to #random; he does not belong to #mentorship-hub. Priya also reacted 👍 to M2. | Wrong author membership channel only |
| M3 | Priya authored this message in #general. Priya currently belongs only to #general. | Wrong author membership channel only |
| M4 | Owen authored this message in #general. Owen currently belongs to #general and #mentors-lounge, not #mentorship-hub. | Wrong author membership channel only; the similarly named channel is distinct |
| M5 | Lucia authored this message in #general before leaving her channels. Lucia retains workspace membership but currently has no channel memberships. | Missing author-to-channel membership relationship |
| M6 | Theo authored this message in #mentorship-hub before leaving that channel. Theo currently belongs only to #general. | Message location does not establish the author’s current membership |

## W06-underspecified

**Route:** Message → User → Conversation Membership → Conversation

**Resolution mode:** underspecified

**Request:** Add 👀 to the message from a person who is a member of #mentorship-hub.

**Change from W06:** Keep the original environment and ask for the message from a person who is a member. Dana’s and Farid’s messages remain alternatives without a selection rule.

| Referent | Environment facts | Interpretation |
|---|---|---|
| M1 | Dana authored this message in #general. Dana currently belongs to #general and #mentorship-hub. | Alternative through Dana’s message |
| M2 | Farid authored this message in #random. Farid currently belongs to #random and #mentorship-hub. Priya also reacted 👍 to M2. | Alternative through Farid’s message |
| M3 | Priya authored this message in #general. Priya currently belongs only to #general. | Wrong author membership channel only |
| M4 | Owen authored this message in #general. Owen currently belongs to #general and #mentors-lounge, not #mentorship-hub. | Wrong author membership channel only; the similarly named channel is distinct |
| M5 | Lucia authored this message in #general before leaving her channels. Lucia retains workspace membership but currently has no channel memberships. | Missing author-to-channel membership relationship |
| M6 | Theo authored this message in #mentorship-hub before leaving that channel. Theo currently belongs only to #general. | Message location does not establish the author’s current membership |

Messages whose author currently belongs to #mentorship-hub. Message location and other people’s reactions do not establish the author’s membership. The singular request does not distinguish Dana’s and Farid’s qualifying messages.

## W07-single

**Route:** Conversation Membership → User → Reaction → Message → Conversation

**Resolution mode:** single

**Request:** Remove from #team-hub the member named Jordan who reacted with 👍 to the security-audit message in #announcements.

**Change from W07:** Remove only Jordan Kim's 👍 reaction; keep the request unchanged.

| Referent | Environment facts | Interpretation |
|---|---|---|
| Jordan Lee's #team-hub membership | Jordan Lee reacted 👍 to security-audit message M1 in #announcements. | Match |
| Jordan Kim's #team-hub membership | Jordan Kim has no reactions on security-audit message M1 in #announcements. | Missing qualifying reaction |
| Jordan Patel's #team-hub membership | Jordan Patel reacted 👀 to M1 and has no 👍 reaction on it. | Wrong emoji only |
| Jordan Nguyen's #team-hub membership | Jordan Nguyen reacted 👍 to office-relocation message M2 in #announcements, not to M1. M2 does not discuss security audits. | Wrong message topic only |
| Jordan Ahmed's #team-hub membership | Jordan Ahmed reacted 👍 to security-audit message M3 in #security-team, not to M1. | Wrong message channel only |
| Jordan Diaz's #random membership | Jordan Diaz reacted 👍 to M1 but has no #team-hub membership. | Wrong membership channel only |
| Morgan Lee's #team-hub membership | Morgan Lee reacted 👍 to M1. Morgan is not named Jordan. | Wrong person's first name only |
| Jordan Park's #team-hub membership | Jordan Park reacted 👀 to M1 and 👍 to M2; has no other reactions. | Requested emoji and requested message occur on different reactions |

## W07-multiple

**Route:** Conversation Membership → User → Reaction → Message → Conversation

**Resolution mode:** multiple

**Request:** Remove from #team-hub the members named Jordan who reacted with 👍 to the security-audit message in #announcements.

**Change from W07:** Keep the original environment; change member to members.

| Referent | Environment facts | Interpretation |
|---|---|---|
| Jordan Lee's #team-hub membership | Jordan Lee reacted 👍 to security-audit message M1 in #announcements. | Match |
| Jordan Kim's #team-hub membership | Jordan Kim reacted 👍 to security-audit message M1 in #announcements. | Match |
| Jordan Patel's #team-hub membership | Jordan Patel reacted 👀 to M1 and has no 👍 reaction on it. | Wrong emoji only |
| Jordan Nguyen's #team-hub membership | Jordan Nguyen reacted 👍 to office-relocation message M2 in #announcements, not to M1. M2 does not discuss security audits. | Wrong message topic only |
| Jordan Ahmed's #team-hub membership | Jordan Ahmed reacted 👍 to security-audit message M3 in #security-team, not to M1. | Wrong message channel only |
| Jordan Diaz's #random membership | Jordan Diaz reacted 👍 to M1 but has no #team-hub membership. | Wrong membership channel only |
| Morgan Lee's #team-hub membership | Morgan Lee reacted 👍 to M1. Morgan is not named Jordan. | Wrong person's first name only |
| Jordan Park's #team-hub membership | Jordan Park reacted 👀 to M1 and 👍 to M2; has no other reactions. | Requested emoji and requested message occur on different reactions |

## W07-absent

**Route:** Conversation Membership → User → Reaction → Message → Conversation

**Resolution mode:** absent

**Request:** Remove from #team-hub the member named Jordan who reacted with 👍 to the security-audit message in #announcements.

**Change from W07:** Remove Jordan Lee's and Jordan Kim's 👍 reactions; keep the request unchanged.

| Referent | Environment facts | Interpretation |
|---|---|---|
| Jordan Lee's #team-hub membership | Jordan Lee has no reactions on security-audit message M1 in #announcements. | Missing qualifying reaction |
| Jordan Kim's #team-hub membership | Jordan Kim has no reactions on security-audit message M1 in #announcements. | Missing qualifying reaction |
| Jordan Patel's #team-hub membership | Jordan Patel reacted 👀 to M1 and has no 👍 reaction on it. | Wrong emoji only |
| Jordan Nguyen's #team-hub membership | Jordan Nguyen reacted 👍 to office-relocation message M2 in #announcements, not to M1. M2 does not discuss security audits. | Wrong message topic only |
| Jordan Ahmed's #team-hub membership | Jordan Ahmed reacted 👍 to security-audit message M3 in #security-team, not to M1. | Wrong message channel only |
| Jordan Diaz's #random membership | Jordan Diaz reacted 👍 to M1 but has no #team-hub membership. | Wrong membership channel only |
| Morgan Lee's #team-hub membership | Morgan Lee reacted 👍 to M1. Morgan is not named Jordan. | Wrong person's first name only |
| Jordan Park's #team-hub membership | Jordan Park reacted 👀 to M1 and 👍 to M2; has no other reactions. | Requested emoji and requested message occur on different reactions |

## W08-multiple

**Route:** Reaction → Message → User → Conversation Membership → Conversation

**Resolution mode:** multiple

**Request:** Remove my 🔥 reactions from the messages written by a member of the channel about launch readiness.

**Change from W08:** Add Nina's 🔥 reaction to a second Kevin-authored message M4; pluralize reaction and message.

| Referent | Environment facts | Interpretation |
|---|---|---|
| Nina's 🔥 on M1 | Nina is the actor. Kevin wrote M1 in #general and belongs to #general and #product-launch. The latter's topic is ‘Launch readiness plan’. | Match |
| Nina's 👀 on M1 | Nina is the actor. Kevin wrote M1 in #general and belongs to #general and #product-launch, whose topic is ‘Launch readiness plan’. Nina reacted 👀 to M1. This is a separate reaction from her 🔥 on it. | Wrong emoji only |
| Sam's 🔥 on M1 | Same message, author and memberships; Sam is a different person from Nina. | Wrong reactor only |
| Nina's 🔥 on M2 | Priya wrote M2 in #general. Priya belongs to #general and #design-crew, whose topic is ‘Weekly visual-design reviews’; she does not belong to #product-launch. | Wrong author membership channel only |
| Nina's 🔥 on M3 | Elena wrote M3 in #product-launch before leaving that channel. She now belongs only to #marketing-updates, whose topic is ‘Marketing campaign updates’. | Message location does not establish the author's current membership |
| Nina's 🔥 on M4 | Kevin wrote a different message M4 in #general; he has the same #general and #product-launch memberships. Nina reacted 🔥 to M4. | Match |

## W08-absent

**Route:** Reaction → Message → User → Conversation Membership → Conversation

**Resolution mode:** absent

**Request:** Remove my 🔥 reaction from the message written by a member of the channel about launch readiness.

**Change from W08:** Remove Nina's 🔥 reaction on M1 and its referent row. Preserve Kevin's membership, the other reactions, and the request.

| Referent | Environment facts | Interpretation |
|---|---|---|
| Nina's 👀 on M1 | Nina is the actor. Kevin wrote M1 in #general and belongs to #general and #product-launch, whose topic is ‘Launch readiness plan’. Nina reacted 👀 to M1. She has no 🔥 reaction on it. | Wrong emoji only |
| Sam's 🔥 on M1 | Same message, author and memberships; Sam is a different person from Nina. | Wrong reactor only |
| Nina's 🔥 on M2 | Priya wrote M2 in #general. Priya belongs to #general and #design-crew, whose topic is ‘Weekly visual-design reviews’; she does not belong to #product-launch. | Wrong author membership channel only |
| Nina's 🔥 on M3 | Elena wrote M3 in #product-launch before leaving that channel. She now belongs only to #marketing-updates, whose topic is ‘Marketing campaign updates’. | Message location does not establish the author's current membership |

## W08-underspecified

**Route:** Reaction → Message → User → Conversation Membership → Conversation

**Resolution mode:** underspecified

**Request:** Remove my 🔥 reaction from the message written by a member of the channel about launch readiness.

**Change from W08:** Add the same second Kevin message and Nina's 🔥 reaction as in the multiple variant, but retain the original singular request.

| Referent | Environment facts | Interpretation |
|---|---|---|
| Nina's 🔥 on M1 | Nina is the actor. Kevin wrote M1 in #general and belongs to #general and #product-launch. The latter's topic is ‘Launch readiness plan’. | Alternative through M1 |
| Nina's 👀 on M1 | Nina is the actor. Kevin wrote M1 in #general and belongs to #general and #product-launch, whose topic is ‘Launch readiness plan’. Nina reacted 👀 to M1. This is a separate reaction from her 🔥 on it. | Wrong emoji only |
| Sam's 🔥 on M1 | Same message, author and memberships; Sam is a different person from Nina. | Wrong reactor only |
| Nina's 🔥 on M2 | Priya wrote M2 in #general. Priya belongs to #general and #design-crew, whose topic is ‘Weekly visual-design reviews’; she does not belong to #product-launch. | Wrong author membership channel only |
| Nina's 🔥 on M3 | Elena wrote M3 in #product-launch before leaving that channel. She now belongs only to #marketing-updates, whose topic is ‘Marketing campaign updates’. | Message location does not establish the author's current membership |
| Nina's 🔥 on M4 | Kevin wrote a different message M4 in #general; he has the same #general and #product-launch memberships. Nina reacted 🔥 to M4. | Alternative through M4 |

The actor's 🔥 reaction on a message whose author currently belongs to the channel about launch readiness. M1 and M4 each carry a qualifying actor-owned reaction; the singular message reference leaves those reactions as competing singleton alternatives.

## W09-single

**Route:** Workspace → Workspace Membership → User → Conversation Membership → Conversation

**Resolution mode:** single

**Request:** What workspace is shown on the profile of the bot in #incident-response?

**Change from W09:** Add WatcherBot's membership in #incident-response; preserve the request.

| Referent | Environment facts | Interpretation |
|---|---|---|
| Atlas, through WatcherBot | WatcherBot is marked as a bot. Its profile displays its Atlas workspace association. It belongs to #project-launch and #incident-response. Atlas's other users, including the actor, are not bots. | Match |
| Nimbus, through Dana Reyes | Dana is a human user, marked as not a bot. Her profile displays her Nimbus workspace association. She belongs to #incident-response. Nimbus has no bot users. | Wrong user classification only |

## W09-multiple

**Route:** Workspace → Workspace Membership → User → Conversation Membership → Conversation

**Resolution mode:** multiple

**Request:** What workspaces are shown on the profiles of the bots in #incident-response?

**Change from W09:** Add WatcherBot to #incident-response and add SignalBot there with an Orion profile association. Pluralize the workspace/profile/bot question. Dana remains a non-bot negative in Nimbus.

| Referent | Environment facts | Interpretation |
|---|---|---|
| Atlas, through WatcherBot | WatcherBot is marked as a bot. Its profile displays its Atlas workspace association. It belongs to #project-launch and #incident-response. Atlas's other users, including the actor, are not bots. | Match |
| Nimbus, through Dana Reyes | Dana is a human user, marked as not a bot. Her profile displays her Nimbus workspace association. She belongs to #incident-response. Nimbus has no bot users. | Wrong user classification only |
| Orion, through SignalBot | SignalBot is a different bot whose profile displays its Orion workspace association. It belongs to #incident-response. Its profile has exactly one workspace association, like the other users here. | Match |

## W09-underspecified

**Route:** Workspace → Workspace Membership → User → Conversation Membership → Conversation

**Resolution mode:** underspecified

**Request:** What workspace is shown on the profile of the bot in #incident-response?

**Change from W09:** Use the same two bots and their distinct workspace associations as the multiple variant, but keep the original singular question.

| Referent | Environment facts | Interpretation |
|---|---|---|
| Atlas, through WatcherBot | WatcherBot is marked as a bot. Its profile displays its Atlas workspace association. It belongs to #project-launch and #incident-response. Atlas's other users, including the actor, are not bots. | Alternative through WatcherBot |
| Nimbus, through Dana Reyes | Dana is a human user, marked as not a bot. Her profile displays her Nimbus workspace association. She belongs to #incident-response. Nimbus has no bot users. | Wrong user classification only |
| Orion, through SignalBot | SignalBot is a different bot whose profile displays its Orion workspace association. It belongs to #incident-response. Its profile has exactly one workspace association, like the other users here. | Alternative through SignalBot |

The workspace association displayed on the profile of the bot belonging to #incident-response. WatcherBot and SignalBot are competing choices for the singular bot, yielding Atlas and Orion as distinct singleton workspace alternatives. Workspace names in the story are labels; the supported profile answer is the actual workspace ID.

## W10-single

**Route:** Workspace Membership → User → Reaction → Message → Conversation → Conversation Membership

**Resolution mode:** single

**Request:** For the people who reacted with 🚀 to the launch-checklist message in the channel Priya belongs to, tell me whether each is a workspace admin or owner.

**Change from W10:** Remove Ben's 🚀 reaction on M1; keep his unrelated 👀 and the plural request.

| Referent | Environment facts | Interpretation |
|---|---|---|
| Alice's workspace membership | Alice reacted 🚀 to checklist message M1 in #launch-prep. Priya belongs to #launch-prep. Alice's profile shows admin true, owner false. Morgan authored M1. | Match; answer is admin |
| Ben's workspace membership | Ben has no reaction on M1 but reacted 👀 to an unrelated lunch message elsewhere. His profile shows admin false, owner false. | Missing qualifying reaction on M1 |
| Chloe's workspace membership | Chloe reacted 👍 to M1, with no 🚀 reaction on it. Her profile shows admin true. | Wrong emoji only; her admin status does not make her a match |
| Diego's workspace membership | Diego reacted 🚀 to office-relocation message M2 in #launch-prep, not to M1. M2 does not discuss a launch checklist. His profile shows owner true. | Wrong message topic only |
| Elena's workspace membership | Elena reacted 🚀 to checklist message M3 in #marketing. M3 has the same text and author, Morgan, as M1. Priya does not belong to #marketing. | Wrong channel membership only; message text and authorship do not distinguish the two channels |
| Farid's workspace membership | Farid belongs to #launch-prep alongside Priya but has no reactions. | Missing reaction relationship; channel membership is not a reaction |
| Grace's workspace membership | Grace reacted 👍 to M1 and 🚀 to M2; has no other reactions. | Requested emoji and checklist occur on different reactions |

## W10-absent

**Route:** Workspace Membership → User → Reaction → Message → Conversation → Conversation Membership

**Resolution mode:** absent

**Request:** For the people who reacted with 🚀 to the launch-checklist message in the channel Priya belongs to, tell me whether each is a workspace admin or owner.

**Change from W10:** Remove Alice's and Ben's 🚀 reactions on M1; preserve the request and all negative patterns.

| Referent | Environment facts | Interpretation |
|---|---|---|
| Alice's workspace membership | Alice has no reactions on checklist message M1 in #launch-prep. Priya belongs to #launch-prep. Alice's profile shows admin true, owner false. Morgan authored M1. | Missing qualifying reaction |
| Ben's workspace membership | Ben has no reaction on M1 but reacted 👀 to an unrelated lunch message elsewhere. His profile shows admin false, owner false. | Missing qualifying reaction on M1 |
| Chloe's workspace membership | Chloe reacted 👍 to M1, with no 🚀 reaction on it. Her profile shows admin true. | Wrong emoji only; her admin status does not make her a match |
| Diego's workspace membership | Diego reacted 🚀 to office-relocation message M2 in #launch-prep, not to M1. M2 does not discuss a launch checklist. His profile shows owner true. | Wrong message topic only |
| Elena's workspace membership | Elena reacted 🚀 to checklist message M3 in #marketing. M3 has the same text and author, Morgan, as M1. Priya does not belong to #marketing. | Wrong channel membership only; message text and authorship do not distinguish the two channels |
| Farid's workspace membership | Farid belongs to #launch-prep alongside Priya but has no reactions. | Missing reaction relationship; channel membership is not a reaction |
| Grace's workspace membership | Grace reacted 👍 to M1 and 🚀 to M2; has no other reactions. | Requested emoji and checklist occur on different reactions |

## W10-underspecified

**Route:** Workspace Membership → User → Reaction → Message → Conversation → Conversation Membership

**Resolution mode:** underspecified

**Request:** For the people who reacted with 🚀 to the launch-checklist message in the channel Priya belongs to, tell me whether each is a workspace admin or owner.

**Change from W10:** Keep Priya Shah in #launch-prep and add a distinct Priya Rao in #marketing. The original plural request leaves a choice between the Alice/Ben collection and the Elena collection.

| Referent | Environment facts | Interpretation |
|---|---|---|
| Alice's workspace membership | Alice reacted 🚀 to checklist message M1 in #launch-prep. Priya Shah belongs to #launch-prep. Alice's profile shows admin true, owner false. Morgan authored M1. | Member of the alternative through Priya Shah; answer is admin |
| Ben's workspace membership | Ben reacted 🚀 to the same M1 and 👀 to an unrelated lunch message elsewhere. His profile shows admin false, owner false. | Member of the alternative through Priya Shah; answer is neither |
| Chloe's workspace membership | Chloe reacted 👍 to M1, with no 🚀 reaction on it. Her profile shows admin true. | Wrong emoji only; her admin status does not make her a match |
| Diego's workspace membership | Diego reacted 🚀 to office-relocation message M2 in #launch-prep, not to M1. M2 does not discuss a launch checklist. His profile shows owner true. | Wrong message topic only |
| Elena's workspace membership | Elena reacted 🚀 to checklist message M3 in #marketing. M3 has the same text and author, Morgan, as M1. Priya Rao belongs to #marketing; Priya Shah does not. These are two different people. Elena's profile shows admin true, owner true. | Member of the alternative through Priya Rao; answer is owner (also admin) |
| Farid's workspace membership | Farid belongs to #launch-prep alongside Priya Shah but has no reactions. | Missing reaction relationship; channel membership is not a reaction |
| Grace's workspace membership | Grace reacted 👍 to M1 and 🚀 to M2; has no other reactions. | Requested emoji and checklist occur on different reactions |

Workspace memberships of the 🚀 reactors on the launch checklist in the channel containing Priya. The jointly intended set is unresolved between Alice/Ben through Priya Shah and Elena through Priya Rao; their union is not authorized. Admin/owner status is answer content, never an identifying restriction.
