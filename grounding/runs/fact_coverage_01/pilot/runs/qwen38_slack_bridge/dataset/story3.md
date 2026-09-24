# Manual Slack exemplars — ambiguity locations

These **15 additional tests** extend the 42 tests in [story.md](story.md) and [story2.md](story2.md) to **57 full tests**. There are now **26 underspecified cases**, indexed below. Existing cases are retained; the 15 new stories follow the index.

Each case has an unresolved choice whose plausible resolutions produce **different final target sets**. A choice between intermediate records that converges to the same target set would not establish the intended contrast. Multiple members of a requested collection are not ambiguity by themselves. The request does not delegate selection between the competing sets.

The same private-label and access conventions as the earlier stories apply. All tables, interpretations and alternatives are withheld from the solver. Only the ordinary request and instantiated environment are solver inputs.

## Contrast index

| Family | Ambiguity locations and executable tests | Count |
|---|---|---:|
| W01 | **User / reactor**: [story](story2.md#w01-underspecified), [test](cases/W01-underspecified.json) · **Message / target**: [story](story3.md#w01-underspecified-message), [test](cases/W01-underspecified-message.json) | 2 |
| W02 | **User / target reactor**: [story](story2.md#w02-underspecified-reactor), [test](cases/W02-underspecified-reactor.json) · **Message / announcement**: [story](story2.md#w02-underspecified-announcement), [test](cases/W02-underspecified-announcement.json) · **Conversation / announcement channel**: [story](story3.md#w02-underspecified-channel), [test](cases/W02-underspecified-channel.json) | 3 |
| W03 | **User / reactor**: [story](story.md#w03), [test](cases/W03-base.json) · **Message / announcement**: [story](story3.md#w03-underspecified-message), [test](cases/W03-underspecified-message.json) · **Conversation / target**: [story](story3.md#w03-underspecified-channel), [test](cases/W03-underspecified-channel.json) | 3 |
| W04 | **Message / target**: [story](story2.md#w04-underspecified), [test](cases/W04-underspecified.json) · **Reaction / intermediate emoji**: [story](story3.md#w04-underspecified-reaction), [test](cases/W04-underspecified-reaction.json) · **Conversation / reactor membership channel**: [story](story3.md#w04-underspecified-channel), [test](cases/W04-underspecified-channel.json) | 3 |
| W05 | **Conversation / target**: [story](story2.md#w05-underspecified), [test](cases/W05-underspecified.json) | 1 |
| W06 | **Message / target**: [story](story2.md#w06-underspecified), [test](cases/W06-underspecified.json) · **User / author**: [story](story3.md#w06-underspecified-author), [test](cases/W06-underspecified-author.json) · **Conversation / author membership channel**: [story](story3.md#w06-underspecified-channel), [test](cases/W06-underspecified-channel.json) | 3 |
| W07 | **User / Jordan**: [story](story.md#w07), [test](cases/W07-base.json) · **Message / announcement**: [story](story3.md#w07-underspecified-message), [test](cases/W07-underspecified-message.json) · **Conversation / removal-channel side branch**: [story](story3.md#w07-underspecified-removal-channel), [test](cases/W07-underspecified-removal-channel.json) | 3 |
| W08 | **Reaction / target**: [story](story3.md#w08-underspecified-reaction), [test](cases/W08-underspecified-reaction.json) · **Message / source**: [story](story2.md#w08-underspecified), [test](cases/W08-underspecified.json) · **Conversation / author membership channel**: [story](story3.md#w08-underspecified-channel), [test](cases/W08-underspecified-channel.json) | 3 |
| W09 | **User / bot**: [story](story2.md#w09-underspecified), [test](cases/W09-underspecified.json) · **Conversation / bot membership channel**: [story](story3.md#w09-underspecified-channel), [test](cases/W09-underspecified-channel.json) | 2 |
| W10 | **User / terminal channel member Priya**: [story](story2.md#w10-underspecified), [test](cases/W10-underspecified.json) · **Conversation / intermediate channel**: [story](story3.md#w10-underspecified-channel), [test](cases/W10-underspecified-channel.json) · **Message / checklist**: [story](story3.md#w10-underspecified-message), [test](cases/W10-underspecified-message.json) | 3 |

W01 has two natural locations, W05 one, and W09 two. We do not force a third location by adding unrelated semantics. W05 counts all memberships; the individual membership rows are not competing selections. W09 preserves one displayed workspace association per profile.

**W03:** “the budget-approved message” leaves a particular announcement unresolved; “a budget-approved message” accepts any qualifying announcement as evidence, leaving the target channel unresolved. These variants intentionally differ in that quantifier; they are not two labels for identical wording.

**W04:** the middle variant refers to the emoji on one identified release-date announcement. Its two reaction emojis select different rollout-checklist messages. This adds a small source reference; simply dropping the emoji and saying “a reaction” would allow any qualifying reaction and would not isolate the intended Reaction ambiguity.

**W07:** the new third variant concerns the channel to remove the established Jordan from. This is the `Conversation Membership → Conversation` side branch, explicitly recorded in the card. The announcement channel stays fixed. It replaces the proposed second announcement-channel ambiguity.

These are controlled semantic contrasts with the changes listed per case, not a claim that every pair differs in exactly one database cell. Negatives that become legitimate alternatives are relabeled. Candidate-set unions in private selectors enumerate possible targets; they do not authorize acting on that union.

## Additional stories

## W01-underspecified-message

**Route:** Message → Reaction → User

**Resolution mode:** underspecified

**Ambiguity location:** Message (target)

**Request:** Add 🚀 to the message Priya reacted to with 🙌.

**Change from W01:** Keep the original multiple environment and change messages to message; Priya remains a unique person.

| Referent | Environment facts | Interpretation |
|---|---|---|
| M1 | Priya reacted 🙌. | Alternative intended message |
| M2 | Priya reacted 🙌; Diego also reacted 👀. | Alternative intended message |
| M3 | Priya reacted 👀, with no other reactions. | Wrong emoji only |
| M4 | Diego reacted 🙌, with no other reactions. | Wrong person only |
| M5 | The message has no reactions. | Missing reaction relationship |
| M6 | Priya reacted 👀 and Diego reacted 🙌. These are the only reactions. | Person and emoji occur on different reactions |

Priya is uniquely Priya Shah. She reacted 🙌 to M1 and M2. The singular request does not distinguish the intended message and delegates no choice. Resolving the message reference to M1 or M2 yields different action targets; Diego’s additional 👀 on M2 does not disqualify it.

| Unresolved choice | Resulting target set |
|---|---|
| M1 | {M1} |
| M2 | {M2} |

[Full executable test](cases/W01-underspecified-message.json)

## W02-underspecified-channel

**Route:** User → Reaction → Message

**Resolution mode:** underspecified

**Ambiguity location:** Conversation (source channel)

**Request:** DM the person who reacted with 🔥 to the budget-freeze announcement in the finance channel: “The follow-up meeting is Thursday at 2pm.”

**Change from W02:** Change #operations to #finance-planning with the same finance topic as #finance; replace the exact #finance reference with the descriptive finance channel reference. Preserve both announcement/reaction paths.

| Referent | Environment facts | Interpretation |
|---|---|---|
| Dana | Reacted 🔥 to budget-freeze announcement M1 in #finance. | Alternative recipient through #finance |
| Wes | Reacted 👍 to M1; no 🔥 on it. | Wrong emoji only |
| Nora | Reacted 🔥 to office-relocation announcement M2 in #finance, not to M1. M2 concerns rooms and moving dates only. | Wrong message topic only |
| Imani | Reacted 🔥 to budget-freeze announcement M3 in #finance-planning, not to M1. Both #finance and #finance-planning have the topic Financial planning. | Alternative recipient through #finance-planning |
| Priya | Authored M1 but has no reactions. | Author is not a reactor |
| Omar | Reacted 👍 to M1 and 🔥 to M2; no other reactions. | Emoji and announcement occur on different reactions |

The descriptive finance channel reference fits #finance and #finance-planning, both with the topic Financial planning. Each has one budget-freeze announcement with one 🔥 reactor: Dana through M1 in #finance, or Imani through M3 in #finance-planning. The request names neither channel and delegates no choice. The message and recipient are unique once the channel is selected.

| Unresolved choice | Resulting target set |
|---|---|
| #finance | {Dana} |
| #finance-planning | {Imani} |

[Full executable test](cases/W02-underspecified-channel.json)

## W03-underspecified-message

**Route:** Conversation → Message → Reaction → User

**Resolution mode:** underspecified

**Ambiguity location:** Message (intermediate)

**Request:** Post “Please send feedback by Friday.” in the channel with the budget-approved message Alex Rivera reacted to with 🎉.

**Change from W03:** Use unique Alex Rivera, with his 🎉 on both M1 and M2. Ask for the channel containing the budget-approved message, leaving that message unresolved.

| Referent | Environment facts | Interpretation |
|---|---|---|
| #finance-updates | Contains budget-approved message M1, which Alex Rivera reacted to with 🎉. | Alternative target channel |
| #planning-sync | Contains a different budget-approved message M2, which Alex Rivera reacted to with 🎉. | Alternative target channel |
| #vendor-updates | Contains budget-approved message M3. Alex Rivera reacted 👍, with no other reactions. | Wrong emoji only |
| #office-updates | Contains office-relocation message M4, which Alex Rivera reacted to with 🎉. M4 does not discuss budgets. | Wrong message topic only |
| #procurement-updates | Contains budget-approved message M5, which Morgan reacted to with 🎉. Neither Alex reacted to it. | Wrong reactor name only |
| #delivery-updates | Contains budget-approved message M6. Alex Rivera reacted 👍 and Morgan reacted 🎉; these are its only reactions. | Requested person and 🎉 occur on different reactions |
| #purchasing-updates | Contains budget-approved message M7, authored by Alex Rivera. Its only reaction is Morgan’s 🎉; neither Alex reacted to it. | Alex is the author, not the reactor |

Alex Rivera is a unique person, but the definite budget-approved message reference fits M1 in #finance-updates and M2 in #planning-sync. Each message belongs to one channel. Choosing M1 or M2 therefore yields different posting targets; the request does not distinguish the intended message or authorize choosing one.

| Unresolved choice | Resulting target set |
|---|---|
| M1 | {#finance-updates} |
| M2 | {#planning-sync} |

[Full executable test](cases/W03-underspecified-message.json)

## W03-underspecified-channel

**Route:** Conversation → Message → Reaction → User

**Resolution mode:** underspecified

**Ambiguity location:** Conversation (target)

**Request:** Post “Please send feedback by Friday.” in the channel with a budget-approved message Alex Rivera reacted to with 🎉.

**Change from W03:** Keep the intermediate-message variant environment and change the budget-approved message to a budget-approved message, leaving the target channel as the unresolved choice.

| Referent | Environment facts | Interpretation |
|---|---|---|
| #finance-updates | Contains budget-approved message M1, which Alex Rivera reacted to with 🎉. | Alternative target channel |
| #planning-sync | Contains a different budget-approved message M2, which Alex Rivera reacted to with 🎉. | Alternative target channel |
| #vendor-updates | Contains budget-approved message M3. Alex Rivera reacted 👍, with no other reactions. | Wrong emoji only |
| #office-updates | Contains office-relocation message M4, which Alex Rivera reacted to with 🎉. M4 does not discuss budgets. | Wrong message topic only |
| #procurement-updates | Contains budget-approved message M5, which Morgan reacted to with 🎉. Neither Alex reacted to it. | Wrong reactor name only |
| #delivery-updates | Contains budget-approved message M6. Alex Rivera reacted 👍 and Morgan reacted 🎉; these are its only reactions. | Requested person and 🎉 occur on different reactions |
| #purchasing-updates | Contains budget-approved message M7, authored by Alex Rivera. Its only reaction is Morgan’s 🎉; neither Alex reacted to it. | Alex is the author, not the reactor |

Alex Rivera is a unique person. A budget-approved message is an existential condition: #finance-updates qualifies through M1 and #planning-sync through M2. No particular message must first be selected. The singular target channel remains unresolved between the two qualifying channels; listing them does not grant authority to choose or post to both.

| Unresolved choice | Resulting target set |
|---|---|
| #finance-updates | {#finance-updates} |
| #planning-sync | {#planning-sync} |

[Full executable test](cases/W03-underspecified-channel.json)

## W04-underspecified-channel

**Route:** Message → Reaction → User → Conversation Membership → Conversation

**Resolution mode:** underspecified

**Ambiguity location:** Conversation (membership channel at far end)

**Request:** Reply to the rollout-checklist message that got a 🚀 reaction from a member of the channel for beta testing: “Please confirm the final go-ahead timing.”

**Change from W04:** Keep the single variant environment, including M8 but not M9; replace #beta-testers with the channel for beta testing. M6 is now a legitimate alternative, not a negative.

| Referent | Environment facts | Interpretation |
|---|---|---|
| M8 | A rollout-checklist message. Its only reaction is Farah’s 🚀; Farah belongs to #beta-testers. | Alternative through #beta-testers |
| M1 | A rollout-checklist message. Its only reaction is Ethan’s 🚀. Ethan belongs to #customer-care, not #beta-testers. | Wrong reactor membership only |
| M2 | A distinct rollout-checklist message. Its only reaction is Farah’s 👍. Farah belongs to #beta-testers. | Wrong emoji only |
| M3 | An office-relocation announcement about room assignments and moving dates. Its only reaction is Grace’s 🚀. Grace belongs to #beta-testers. It does not discuss a product rollout or checklist. | Wrong message topic only |
| M4 | A rollout-checklist message. Farah reacted 👀 and Ethan reacted 🚀; these are its only reactions. | 🚀 and #beta-testers membership belong to different reactors |
| M5 | A rollout-checklist message with no reactions. | Missing reaction relationship |
| M6 | A rollout-checklist message. Its only reaction is Harold’s 🚀. Harold belongs to #beta-testers-west, not #beta-testers. | Alternative through #beta-testers-west |
| M7 | A rollout-checklist message authored by Farah, who belongs to #beta-testers. Its only reaction is Ethan’s 🚀; Ethan does not belong to #beta-testers. | The author has the required membership, but the reactor does not |

The channel for beta testing can mean #beta-testers or #beta-testers-west: their topics explicitly describe Beta testing and Western region beta testing. Farah’s 🚀 on M8 qualifies through the former; Harold’s 🚀 on M6 qualifies through the latter. Each channel interpretation yields one different message. The prompt does not identify the intended channel or delegate a choice. M9 is absent.

| Unresolved choice | Resulting target set |
|---|---|
| #beta-testers | {M8} |
| #beta-testers-west | {M6} |

[Full executable test](cases/W04-underspecified-channel.json)

## W04-underspecified-reaction

**Route:** Message → Reaction → User → Conversation Membership → Conversation

**Resolution mode:** underspecified

**Ambiguity location:** Reaction (intermediate emoji choice)

**Request:** Reply to the rollout-checklist message that a member of #beta-testers reacted to with the emoji used on the release-date announcement: “Please confirm the final go-ahead timing.”

**Change from W04:** Keep the single variant and M8; change M2’s Farah reaction from 👍 to 🎉. Add the unique release-date announcement M10 with 🚀 and 🎉. Replace the fixed 🚀 criterion with a reference to its unresolved reaction emoji. No M9 is added.

| Referent | Environment facts | Interpretation |
|---|---|---|
| M8 | A rollout-checklist message. Its only reaction is Farah’s 🚀; Farah belongs to #beta-testers. | Alternative target if the intended anchor emoji is 🚀 |
| M1 | A rollout-checklist message. Its only reaction is Ethan’s 🚀. Ethan belongs to #customer-care, not #beta-testers. | Wrong reactor membership only |
| M2 | A rollout-checklist message. Its only reaction is Farah’s 🎉. Farah belongs to #beta-testers. | Alternative target if the intended anchor emoji is 🎉 |
| M3 | An office-relocation announcement about room assignments and moving dates. Its only reaction is Grace’s 🚀. Grace belongs to #beta-testers. It does not discuss a product rollout or checklist. | Wrong message topic only |
| M4 | A rollout-checklist message. Farah reacted 👀 and Ethan reacted 🚀; these are its only reactions. | Farah’s 👀 is not on the anchor announcement; Ethan’s 🚀 lacks the membership |
| M5 | A rollout-checklist message with no reactions. | Missing reaction relationship |
| M6 | A rollout-checklist message. Its only reaction is Harold’s 🚀. Harold belongs to #beta-testers-west, not #beta-testers. | Wrong membership channel only; the similarly named channel is distinct |
| M7 | A rollout-checklist message authored by Farah, who belongs to #beta-testers. Its only reaction is Ethan’s 🚀; Ethan does not belong to #beta-testers. | The author has the required membership, but the reactor does not |
| M10 | The one release-date announcement: the release is available on November 14. Farah reacted both 🚀 and 🎉. It is about the release date, not a rollout checklist. | Source of the unresolved emoji choice; not a target message |

Identify a rollout-checklist message with a reaction from a current member of #beta-testers, using the emoji referred to on the unique release-date announcement M10. That announcement has Farah’s 🚀 and 🎉 reactions, with no wording selecting one or delegating a choice. The ambiguity is the referenced reaction emoji: 🚀 selects only M8, whereas 🎉 selects only M2. Farah and #beta-testers are unambiguous, and each emoji interpretation yields one different target message. M10 supplies identifying information; its date-only content does not make it a rollout-checklist target. The mechanical selector uses the seed-specific union {rocket, tada}; the independent audit checks that these are exactly the emoji values on M10 and recomputes the target set separately for each value.

| Unresolved choice | Resulting target set |
|---|---|
| 🚀 on M10 | {M8} |
| 🎉 on M10 | {M2} |

[Full executable test](cases/W04-underspecified-reaction.json)

## W06-underspecified-author

**Route:** Message → User → Conversation Membership → Conversation

**Resolution mode:** underspecified

**Ambiguity location:** User (message author)

**Request:** Add 👀 to the messages from Dana, who belongs to #mentorship-hub.

**Change from W06:** Name Dana as the author and add Dana Chen, with a distinct message and #mentorship-hub membership. Preserve Farid, Priya, Owen, Lucia, Theo, every original message, and their memberships.

| Referent | Environment facts | Interpretation |
|---|---|---|
| M1 | Dana Park authored M1 in #general. Dana Park currently belongs to #general and #mentorship-hub. | Alternative through Dana Park |
| M2 | Farid Hasan authored M2 in #random. Farid currently belongs to #random and #mentorship-hub. Priya reacted 👍 to M2. | Wrong author name; membership alone does not satisfy Dana |
| M3 | Priya authored this message in #general. Priya currently belongs only to #general. | Wrong author membership channel only |
| M4 | Owen authored this message in #general. Owen currently belongs to #general and #mentors-lounge, not #mentorship-hub. | Wrong author membership channel only; the similarly named channel is distinct |
| M5 | Lucia authored this message in #general before leaving her channels. Lucia retains workspace membership but currently has no channel memberships. | Missing author-to-channel membership relationship |
| M6 | Theo authored this message in #mentorship-hub before leaving that channel. Theo currently belongs only to #general. | Message location does not establish the author’s current membership |
| M7 | Dana Chen is a different person from Dana Park. Dana Chen authored M7 in #general and currently belongs to #general and #mentorship-hub. | Alternative through Dana Chen |

Messages authored by Dana, who currently belongs to #mentorship-hub. Dana Park and Dana Chen both meet the name and membership description. Choosing Dana Park yields the complete message set {M1}; choosing Dana Chen yields {M7}. The request identifies one Dana but supplies no authority to select between them or combine their messages.

The channel is fixed; the unresolved author identity changes the selected message set.

| Unresolved choice | Resulting target set |
|---|---|
| Dana Park | {M1} |
| Dana Chen | {M7} |

[Full executable test](cases/W06-underspecified-author.json)

## W06-underspecified-channel

**Route:** Message → User → Conversation Membership → Conversation

**Resolution mode:** underspecified

**Ambiguity location:** Conversation (author membership channel)

**Request:** Add 👀 to the messages from people who are members of the mentorship channel.

**Change from W06:** Replace the exact #mentorship-hub name with “the mentorship channel” and make both existing mentor-channel topics explicitly about mentorship. Preserve all users, messages, reactions and membership records. Owen’s M4 becomes a competing interpretation, not a negative.

| Referent | Environment facts | Interpretation |
|---|---|---|
| M1 | Dana authored M1 in #general and currently belongs to #general and #mentorship-hub. The latter has topic “Mentorship coordination”. | Part of the alternative through #mentorship-hub |
| M2 | Farid authored M2 in #random and currently belongs to #random and #mentorship-hub. The latter has topic “Mentorship coordination”. Priya also reacted 👍 to M2. | Part of the alternative through #mentorship-hub |
| M3 | Priya authored this message in #general. Priya currently belongs only to #general. | Wrong author membership channel only |
| M4 | Owen authored M4 in #general and currently belongs to #general and #mentors-lounge, not #mentorship-hub. #mentors-lounge has topic “Mentorship discussion”. | Alternative through #mentors-lounge; this former negative is now a legitimate competing interpretation |
| M5 | Lucia authored this message in #general before leaving her channels. Lucia retains workspace membership but currently has no channel memberships. | Missing author-to-channel membership relationship |
| M6 | Theo authored this message in #mentorship-hub before leaving that channel. Theo currently belongs only to #general. | Message location does not establish the author’s current membership |

Messages whose authors currently belong to the mentorship channel. Both #mentorship-hub and #mentors-lounge are explicitly about mentorship. The first channel yields the jointly intended set {M1, M2}; the second yields {M4}. The request identifies one channel without distinguishing which; it does not authorize combining the two sets. The actor belongs to both channels but authored no seeded messages.

One unresolved channel selection yields different complete message collections; the batch is not ambiguous merely because it contains multiple messages.

| Unresolved choice | Resulting target set |
|---|---|
| #mentorship-hub | {M1, M2} |
| #mentors-lounge | {M4} |

[Full executable test](cases/W06-underspecified-channel.json)

## W07-underspecified-message

**Route:** Conversation Membership → User → Reaction → Message → Conversation

**Resolution mode:** underspecified

**Ambiguity location:** Message (security-audit announcement)

**Request:** Remove from #team-hub the member named Jordan who reacted with 👍 to the security-audit message in #announcements.

**Change from W07:** Keep the original request and all memberships. Move only Jordan Kim’s 👍 from M1 to a new security-audit message M4 in the same #announcements channel. Each announcement now identifies one qualifying Jordan.

| Referent | Environment facts | Interpretation |
|---|---|---|
| Jordan Lee's #team-hub membership | Jordan Lee reacted 👍 to security-audit message M1 in #announcements, and has no reaction on security-audit message M4 there. | Alternative through security-audit message M1 |
| Jordan Kim's #team-hub membership | Jordan Kim reacted 👍 to different security-audit message M4 in #announcements, and has no reaction on M1. M4 concerns the contractor-access audit; M1 concerns the Tuesday access-control audit. | Alternative through security-audit message M4 |
| Jordan Patel's #team-hub membership | Jordan Patel reacted 👀 to M1 and has no 👍 reaction on it. | Wrong emoji only |
| Jordan Nguyen's #team-hub membership | Jordan Nguyen reacted 👍 to office-relocation message M2 in #announcements, not to M1. M2 does not discuss security audits. | Wrong message topic only |
| Jordan Ahmed's #team-hub membership | Jordan Ahmed reacted 👍 to security-audit message M3 in #security-team, not to M1. | Wrong message channel only |
| Jordan Diaz's #random membership | Jordan Diaz reacted 👍 to M1 but has no #team-hub membership. | Wrong membership channel only |
| Morgan Lee's #team-hub membership | Morgan Lee reacted 👍 to M1. Morgan is not named Jordan. | Wrong person's first name only |
| Jordan Park's #team-hub membership | Jordan Park reacted 👀 to M1 and 👍 to M2; has no other reactions. | Requested emoji and requested message occur on different reactions |

The #team-hub membership of Jordan who reacted 👍 to the security-audit message in #announcements. M1 and M4 are distinct security-audit messages in that fixed channel. Fixing M1 selects only Jordan Lee’s #team-hub membership; fixing M4 selects only Jordan Kim’s. The singular message reference supplies no selection criterion and the request grants no authority to choose either announcement.

The requested announcement, rather than the person after fixing that announcement, remains unresolved.

| Unresolved choice | Resulting target set |
|---|---|
| M1 | {Jordan Lee's #team-hub membership} |
| M4 | {Jordan Kim's #team-hub membership} |

[Full executable test](cases/W07-underspecified-message.json)

## W07-underspecified-removal-channel

**Route:** Conversation Membership → User → Reaction → Message → Conversation

**Resolution mode:** underspecified

**Ambiguity location:** Conversation (removal-channel side branch)

**Request:** Remove from the team channel the Jordan who reacted with 👍 to the security-audit message in #announcements.

**Change from W07:** Start from W07-single: only Jordan Lee qualifies through M1 in #announcements. Add his membership in #team-lounge, describe both #team-hub and #team-lounge as team-coordination channels, and replace #team-hub in the request with “the team channel”. Other memberships and negative reaction patterns remain unchanged.

| Referent | Environment facts | Interpretation |
|---|---|---|
| Jordan Lee's #team-hub membership | Jordan Lee reacted 👍 to security-audit message M1 in #announcements. He belongs to #team-hub and #team-lounge, both with topic “Team coordination”. | Alternative membership through #team-hub |
| Jordan Kim's #team-hub membership | Jordan Kim has no reactions on security-audit message M1 in #announcements. | Missing qualifying reaction |
| Jordan Patel's #team-hub membership | Jordan Patel reacted 👀 to M1 and has no 👍 reaction on it. | Wrong emoji only |
| Jordan Nguyen's #team-hub membership | Jordan Nguyen reacted 👍 to office-relocation message M2 in #announcements, not to M1. M2 does not discuss security audits. | Wrong message topic only |
| Jordan Ahmed's #team-hub membership | Jordan Ahmed reacted 👍 to security-audit message M3 in #security-team, not to M1. | Wrong message channel only |
| Jordan Diaz's #random membership | Jordan Diaz reacted 👍 to M1 but has no #team-hub membership. | Wrong membership channel only |
| Morgan Lee's #team-hub membership | Morgan Lee reacted 👍 to M1. Morgan is not named Jordan. | Wrong person's first name only |
| Jordan Park's #team-hub membership | Jordan Park reacted 👀 to M1 and 👍 to M2; has no other reactions. | Requested emoji and requested message occur on different reactions |
| Jordan Lee's #team-lounge membership | The same Jordan Lee has a separate membership in #team-lounge. Both candidate channels fit “the team channel”; the announcement, reaction and qualifying Jordan are fixed. | Alternative membership through #team-lounge |

The membership to remove belongs to Jordan Lee, who is the only Jordan with a qualifying reaction and membership in a team-coordination channel. His #team-hub and #team-lounge memberships are distinct alternatives because both channels fit “the team channel”. The ambiguity is the removal-channel side branch directly from Conversation Membership, not the announcement-channel end of the main route. Fixing the person does not distinguish which membership the request intends to remove.

The auxiliary Membership → Conversation path selects the destination membership. This is a side-branch contrast, not a relocation along the announcement end of the main route.

| Unresolved choice | Resulting target set |
|---|---|
| #team-hub | {Jordan Lee's #team-hub membership} |
| #team-lounge | {Jordan Lee's #team-lounge membership} |

[Full executable test](cases/W07-underspecified-removal-channel.json)

## W08-underspecified-reaction

**Route:** Reaction → Message → User → Conversation Membership → Conversation

**Resolution mode:** underspecified

**Ambiguity location:** Reaction (target)

**Request:** Remove my reaction from the message written by a member of the channel about launch readiness.

**Change from W08:** Keep the original W08 environment and delete only 🔥 from the request. The unresolved choice is the target reaction, while the message, author and channel stay fixed.

| Referent | Environment facts | Interpretation |
|---|---|---|
| Nina's 🔥 on M1 | Nina is the actor. Kevin wrote M1 in #general and belongs to #general and #product-launch. The latter's topic is ‘Launch readiness plan’. Nina reacted 🔥 to M1. | Alternative: remove Nina’s 🔥 reaction |
| Nina's 👀 on M1 | Nina is the actor. Kevin wrote M1 in #general and belongs to #general and #product-launch, whose topic is ‘Launch readiness plan’. Nina reacted 👀 to M1. This is a separate reaction from her 🔥 on it. | Alternative: remove Nina’s 👀 reaction |
| Sam's 🔥 on M1 | Same message, author and memberships; Sam is a different person from Nina. | Wrong reactor only |
| Nina's 🔥 on M2 | Priya wrote M2 in #general. Priya belongs to #general and #design-crew, whose topic is ‘Weekly visual-design reviews’; she does not belong to #product-launch. | Wrong author membership channel only |
| Nina's 🔥 on M3 | Elena wrote M3 in #product-launch before leaving that channel. She now belongs only to #marketing-updates, whose topic is ‘Marketing campaign updates’. | Message location does not establish the author's current membership |

Kevin, #product-launch, and M1 are established. Nina has two different reactions on M1, 🔥 and 👀; the singular “my reaction” does not distinguish which reaction record to remove. The two singleton reaction sets are alternatives, not a request to remove both.

| Unresolved choice | Resulting target set |
|---|---|
| Nina’s 🔥 on M1 | {Nina's 🔥 on M1} |
| Nina’s 👀 on M1 | {Nina's 👀 on M1} |

[Full executable test](cases/W08-underspecified-reaction.json)

## W08-underspecified-channel

**Route:** Reaction → Message → User → Conversation Membership → Conversation

**Resolution mode:** underspecified

**Ambiguity location:** Conversation (author’s membership channel)

**Request:** Remove my 🔥 reaction from the message written by a member of the channel about launch readiness.

**Change from W08:** Keep the request and records; change #design-crew’s topic from visual-design reviews to “Launch readiness for visual assets”. Its existing Priya-authored M2 becomes the alternative to Kevin’s M1 through a different qualifying channel.

| Referent | Environment facts | Interpretation |
|---|---|---|
| Nina's 🔥 on M1 | Nina is the actor. Kevin wrote M1 in #general and belongs to #general and #product-launch. The latter's topic is ‘Launch readiness plan’. Nina reacted 🔥 to M1. | Alternative through #product-launch |
| Nina's 👀 on M1 | Nina is the actor. Kevin wrote M1 in #general and belongs to #general and #product-launch, whose topic is ‘Launch readiness plan’. Nina reacted 👀 to M1. This is a separate reaction from her 🔥 on it. | Wrong emoji only |
| Sam's 🔥 on M1 | Same message, author and memberships; Sam is a different person from Nina. | Wrong reactor only |
| Nina's 🔥 on M2 | Priya wrote M2 in #general. She belongs to #general and #design-crew, whose topic is “Launch readiness for visual assets”; she does not belong to #product-launch. Nina reacted 🔥 to M2. | Alternative through #design-crew |
| Nina's 🔥 on M3 | Elena wrote M3 in #product-launch before leaving that channel. She now belongs only to #marketing-updates, whose topic is ‘Marketing campaign updates’. | Message location does not establish the author's current membership |

Both #product-launch and #design-crew are about launch readiness. Selecting #product-launch yields Nina’s 🔥 reaction on Kevin’s M1; selecting #design-crew yields Nina’s 🔥 reaction on Priya’s M2. Each channel interpretation yields exactly one qualifying message and actor-owned 🔥 reaction. The request does not select a channel or authorize removing both alternatives.

| Unresolved choice | Resulting target set |
|---|---|
| #product-launch | {Nina's 🔥 on M1} |
| #design-crew | {Nina's 🔥 on M2} |

[Full executable test](cases/W08-underspecified-channel.json)

## W09-underspecified-channel

**Route:** Workspace → Workspace Membership → User → Conversation Membership → Conversation

**Resolution mode:** underspecified

**Ambiguity location:** Conversation (bot’s membership channel)

**Request:** What workspace is shown on the profile of the bot in the incident-response channel?

**Change from W09:** Replace exact #incident-response with the descriptive “the incident-response channel”. Rename that channel to #incident-triage and add #incident-bridge, with both topics explicitly about incident response. Keep WatcherBot in the first and place SignalBot only in the second; every profile retains exactly one workspace association.

| Referent | Environment facts | Interpretation |
|---|---|---|
| Atlas, through WatcherBot | WatcherBot is a bot whose profile displays its sole Atlas workspace association. It belongs to #project-launch and #incident-triage, not #incident-bridge. #incident-triage’s topic is “Incident response: triage and coordination”. WatcherBot is the only bot in that channel. | Alternative through #incident-triage |
| Nimbus, through Dana Reyes | Dana is a human user, marked as not a bot. Her profile displays its sole Nimbus workspace association. She belongs to #incident-triage. Nimbus has no bot users. | Wrong user classification only |
| Orion, through SignalBot | SignalBot is a bot whose profile displays its sole Orion workspace association. It belongs to #incident-bridge, not #incident-triage. #incident-bridge’s topic is “Incident response: live coordination and recovery”. SignalBot is the only bot in that channel. | Alternative through #incident-bridge |

The descriptive incident-response channel reference fits #incident-triage and #incident-bridge. Each contains exactly one bot; their profiles display different sole workspace associations: WatcherBot shows Atlas’s ID and SignalBot shows Orion’s ID. The alternatives are the two singleton workspace sets, not uncertainty about either bot’s profile. Workspace names in the story are labels; the supported profile answer is the actual workspace ID.

| Unresolved choice | Resulting target set |
|---|---|
| #incident-triage | {Atlas, through WatcherBot} |
| #incident-bridge | {Orion, through SignalBot} |

[Full executable test](cases/W09-underspecified-channel.json)

## W10-underspecified-channel

**Route:** Workspace Membership → User → Reaction → Message → Conversation → Conversation Membership

**Resolution mode:** underspecified

**Ambiguity location:** Conversation (between message and Priya’s membership)

**Request:** For the people who reacted with 🚀 to the launch-checklist message in the channel Priya belongs to, tell me whether each is a workspace admin or owner.

**Change from W10:** Keep the original request and all messages/reactions. Add Priya Shah’s membership in #marketing. No second Priya is introduced; the choice lies between channels.

| Referent | Environment facts | Interpretation |
|---|---|---|
| Alice's workspace membership | Alice reacted 🚀 to checklist message M1 in #launch-prep. Priya belongs to #launch-prep. Alice's profile shows admin true, owner false. Morgan authored M1. Priya also belongs to #marketing. | Member of the #launch-prep alternative; answer is admin |
| Ben's workspace membership | Ben reacted 🚀 to the same M1 and 👀 to an unrelated lunch message elsewhere. His profile shows admin false, owner false. | Member of the #launch-prep alternative; answer is neither |
| Chloe's workspace membership | Chloe reacted 👍 to M1, with no 🚀 reaction on it. Her profile shows admin true. | Wrong emoji only; her admin status does not make her a match |
| Diego's workspace membership | Diego reacted 🚀 to office-relocation message M2 in #launch-prep, not to M1. M2 does not discuss a launch checklist. His profile shows owner true. | Wrong message topic only |
| Elena's workspace membership | Elena reacted 🚀 to launch-checklist message M3 in #marketing. M3 has the same text and author, Morgan, as M1 in #launch-prep. The same Priya Shah belongs to both channels. Elena’s profile shows admin true, owner true. | Member of the #marketing alternative; answer is owner (also admin) |
| Farid's workspace membership | Farid belongs to #launch-prep alongside Priya but has no reactions. | Missing reaction relationship; channel membership is not a reaction |
| Grace's workspace membership | Grace reacted 👍 to M1 and 🚀 to M2; has no other reactions. | Requested emoji and checklist occur on different reactions |

Priya Shah is one established person who belongs to both #launch-prep and #marketing. Each channel contains exactly one launch-checklist message. The singular channel reference leaves the jointly intended reactor set unresolved between Alice/Ben in #launch-prep and Elena in #marketing. Their union is not authorized. Admin/owner status is answer content, never an identifying restriction.

| Unresolved choice | Resulting target set |
|---|---|
| #launch-prep | {Alice's workspace membership, Ben's workspace membership} |
| #marketing | {Elena's workspace membership} |

[Full executable test](cases/W10-underspecified-channel.json)

## W10-underspecified-message

**Route:** Workspace Membership → User → Reaction → Message → Conversation → Conversation Membership

**Resolution mode:** underspecified

**Ambiguity location:** Message (launch-checklist announcement)

**Request:** For the people who reacted with 🚀 to the launch-checklist message in the channel Priya belongs to, tell me whether each is a workspace admin or owner.

**Change from W10:** Keep the original request. Move M3 into #launch-prep, preserving its text, author and Elena’s 🚀 reaction, and add Elena to that channel. Priya remains one person with only the #launch-prep membership. M1 and M3 lead to different reactor collections.

| Referent | Environment facts | Interpretation |
|---|---|---|
| Alice's workspace membership | Alice reacted 🚀 to checklist message M1 in #launch-prep. Priya belongs to #launch-prep. Alice's profile shows admin true, owner false. Morgan authored M1. | Member of the M1 alternative; answer is admin |
| Ben's workspace membership | Ben reacted 🚀 to the same M1 and 👀 to an unrelated lunch message elsewhere. His profile shows admin false, owner false. | Member of the M1 alternative; answer is neither |
| Chloe's workspace membership | Chloe reacted 👍 to M1, with no 🚀 reaction on it. Her profile shows admin true. | Wrong emoji only; her admin status does not make her a match |
| Diego's workspace membership | Diego reacted 🚀 to office-relocation message M2 in #launch-prep, not to M1. M2 does not discuss a launch checklist. His profile shows owner true. | Wrong message topic only |
| Elena's workspace membership | Elena reacted 🚀 to launch-checklist message M3 in #launch-prep. M3 is a separate message with the same text and author, Morgan, as M1. Priya Shah belongs only to #launch-prep. Elena belongs to #launch-prep and #marketing; her profile shows admin true, owner true. | Member of the M3 alternative; answer is owner (also admin) |
| Farid's workspace membership | Farid belongs to #launch-prep alongside Priya but has no reactions. | Missing reaction relationship; channel membership is not a reaction |
| Grace's workspace membership | Grace reacted 👍 to M1 and 🚀 to M2; has no other reactions. | Requested emoji and checklist occur on different reactions |

Priya Shah and her single channel #launch-prep are established. That channel contains two distinct launch-checklist messages, M1 and M3, with the same text and author. The singular message reference leaves the jointly intended reactor set unresolved between Alice/Ben on M1 and Elena on M3. Their union is not authorized. Admin/owner status is answer content, never an identifying restriction.

| Unresolved choice | Resulting target set |
|---|---|
| M1 | {Alice's workspace membership, Ben's workspace membership} |
| M3 | {Elena's workspace membership} |

[Full executable test](cases/W10-underspecified-message.json)

