# Conceptual writer pilot: all first outputs

These are the ten original Sonnet 5 outputs, without repairs. See [manual review](review.md) for validity and challenge assessments. [Shared input](system.md) is combined with each case input below.

[W01](#w01) · [W02](#w02) · [W03](#w03) · [W04](#w04) · [W05](#w05) · [W06](#w06) · [W07](#w07) · [W08](#w08) · [W09](#w09) · [W10](#w10)


## W01

[Case input](W01/input.md) · [Original output](W01/writer/turn-01/output.md) · [Recorded thinking](W01/writer/turn-01/thinking.txt)

# Assignment W01

**Route:** Message → Reaction → User
**Resolution mode:** multiple

**Request:** "Add a ✅ to the messages Priya reacted to with a 🚀 in #product-launch."

| Referent | Environment facts | Interpretation |
|---|---|---|
| A | Message "Shipping build 4.2 to prod tonight" in #product-launch; Priya 🚀 | Match |
| B | Message "Landing page copy finalized" in #product-launch; Priya 🚀, and also Dan 👀 on the same message | Match with unrelated activity |
| C | Message "Rollback plan drafted" in #product-launch; Priya 👀 (no 🚀 from her) | Wrong emoji only |
| D | Message "QA sign-off received" in #product-launch; Wen 🚀 (Priya did not react) | Wrong person only |
| E | Message "Marketing embargo lifted" in #product-launch; no reactions at all | Missing reaction relationship |
| F | Message "Launch retro scheduled" in #product-launch; Priya 👀 and Wen 🚀 (Priya's reaction and the 🚀 reaction are different reactions) | Person and emoji occur on different reactions |
| G | Message "Beta invite list finalized" in #eng-internal (not #product-launch); Priya 🚀 | Right person/emoji, wrong container location |

## W02

[Case input](W02/input.md) · [Original output](W02/writer/turn-01/output.md) · [Recorded thinking](W02/writer/turn-01/thinking.txt)

# Assignment W02

**Route:** User → Reaction → Message
**Resolution mode:** single

**Request:** "DM the person who reacted with 🚀 to the billing rollout announcement in #launch-prep, and ask if they're free for a quick sync call this afternoon."

| Referent | Environment facts | Interpretation |
|---|---|---|
| Priya | Reacted 🚀 to the message in #launch-prep reading "We're rolling out the new billing system Monday morning." | Match — correct reactor, emoji, and message |
| Devon | Reacted 👍 to the same billing rollout announcement in #launch-prep | Wrong emoji only |
| Lana | Reacted 🚀 to a different message in #launch-prep announcing "The office wifi will be down for maintenance tonight." | Wrong message only |
| Marcus | Authored the billing rollout announcement in #launch-prep; did not react to it | Author substituted for reactor |
| Sofia | Member of #launch-prep and reacted 🚀 to a teammate's comment reply underneath the billing rollout announcement, not to the announcement message itself | Wrong message only (reacted to a reply, not the identified root message) |

## W03

[Case input](W03/input.md) · [Original output](W03/writer/turn-01/output.md) · [Recorded thinking](W03/writer/turn-01/thinking.txt)

Route: Conversation → Message → Reaction → User
Request: Set the topic of the channel with the incident retro message that Sam reacted to with 🎉 to "Postmortem scheduled for Thursday".

| Referent | Environment facts | Interpretation |
|---|---|---|
| sre-oncall | Sam Wozniak reacted 🎉 to its incident retro message | Alternative through Sam Wozniak |
| platform-reliability | Sam Ibarra reacted 🎉 to its incident retro message | Alternative through Sam Ibarra |
| sre-oncall-archive | Sam Wozniak reacted 👀 to its incident retro message | Wrong emoji only |
| infra-updates | Sam Wozniak reacted 🎉 to its capacity-planning message | Wrong message topic only |
| release-notes | Contains an incident retro message; Sam Wozniak reacted 🎉 to a different message in the same channel | Reaction not bound to the identified message |
| escalations | Contains an incident retro message with a 🎉 reaction from Priya Shah, and Sam Wozniak is a member of the channel but did not react to it | Wrong reactor role (member, not reactor)

## W04

[Case input](W04/input.md) · [Original output](W04/writer/turn-01/output.md) · [Recorded thinking](W04/writer/turn-01/thinking.txt)

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

## W05

[Case input](W05/input.md) · [Original output](W05/writer/turn-01/output.md) · [Recorded thinking](W05/writer/turn-01/thinking.txt)

# Assignment W05

**Route:** Conversation → Conversation Membership (position 0 → position 1)
**Resolution mode:** multiple (2 intended referents)

**Request:** "Post a reminder message in the channels that have exactly 5 members, letting everyone know Friday's stand-up moved to 10am."

| Referent | Environment facts | Interpretation |
|---|---|---|
| #launch-team | Conversation members: Ana, Ben, Cara, Dev, Eli — exactly 5 conversation memberships | Match: simple complete match, member count = 5 |
| #ops-sync | Conversation members: Fay, Gus, Hal, Ivy, Jax — exactly 5 conversation memberships; channel also has an unrelated pinned topic "Sprint planning" and an older message with a 🎉 reaction | Match with unrelated activity: count still = 5 |
| #design-crew | Conversation members: Kai, Lea, Mia, Nia — only 4 conversation memberships | Wrong count only (4, not 5) |
| #eng-all | Conversation members: Oli, Pia, Quin, Ravi, Sam, Tia — 6 conversation memberships | Wrong count only (6, not 5) |
| #product | 5 users (Nora, Omar, Pat, Quinn, Ray) hold workspace membership in the same workspace as #product, but only 3 of them (Nora, Omar, Pat) hold conversation membership in #product itself | Wrong relation role: workspace-membership count substituted for conversation-membership count; actual conversation membership count = 3 |
| #support | Conversation members: Sasha, Tariq, Uzo, Val, Wren — exactly 5 conversation memberships, but the conversation is archived and its membership records list these 5 users as removed (no active membership rows remain, only historical mentions in messages) | Missing relationship: no current conversation membership records despite prior/mentioned association, so no qualifying count |

**Note:** Member count is computed strictly from `Conversation Membership` records tied to the same conversation (including the actor if the actor holds membership there); workspace-level membership or message mentions are not substitutes for that relationship.

## W06

[Case input](W06/input.md) · [Original output](W06/writer/turn-01/output.md) · [Recorded thinking](W06/writer/turn-01/thinking.txt)

**Route:** Message → User → Conversation Membership → Conversation
**Resolution mode:** multiple

**User request:** "Add a 🚀 reaction to the messages posted by members of our #product-launch channel."

| Referent | Environment facts | Interpretation |
|---|---|---|
| A | Message "Timeline looks good" authored by Dana; Dana is a member of #product-launch | Match |
| B | Message "Assets are ready" authored by Eli; Eli is a member of #product-launch; message also has a reply from Farah and an unrelated 👍 from Priya | Match with unrelated activity |
| C | Message "Can we push the date?" authored by Farah; Farah is a member of #design, not #product-launch | Wrong conversation only (author's membership points elsewhere) |
| D | Message "Draft copy attached" authored by Gil; Gil's only membership is to #product-launch-archive, a distinct conversation despite the similar name | Wrong conversation only (name similarity, different record) |
| E | Message "Almost done" authored by Priya; Priya has no conversation membership records at all | Missing membership relationship |
| F | Message "Let's ship it" posted in the #product-launch channel itself, authored by Farah, who is a member of #design only; Farah is not a member of #product-launch | Message location is #product-launch but author's membership is to a different conversation — location must not be treated as author's membership |

*Note:* Reaction-add is a supported write; the channel condition is satisfied strictly through the author's own conversation-membership record, not through where the message happens to be posted.

## W07

[Case input](W07/input.md) · [Original output](W07/writer/turn-01/output.md) · [Recorded thinking](W07/writer/turn-01/thinking.txt)

Route: Conversation Membership → User → Reaction → Message → Conversation

Request: Is Alex still a member of the channel where they reacted 🚀 to the message announcing the new deployment pipeline?

| Referent | Environment facts | Interpretation |
|---|---|---|
| Alex Rivera's membership in #infra-updates | Alex Rivera reacted 🚀 to the message "New deployment pipeline is live" posted in #infra-updates, and Alex Rivera is a current member of #infra-updates | Alternative through Alex Rivera |
| Alex Kim's membership in #platform-eng | Alex Kim reacted 🚀 to the message "New deployment pipeline is live" posted in #platform-eng, and Alex Kim is a current member of #platform-eng | Alternative through Alex Kim |
| Alex Rivera's membership in #infra-updates (wrong emoji) | Alex Rivera reacted 👍 (not 🚀) to the deployment pipeline message in #infra-updates, and is a member of #infra-updates | Wrong emoji only |
| Alex Kim's membership in #platform-eng (wrong topic) | Alex Kim reacted 🚀 to a message announcing an office relocation, not the deployment pipeline, in #platform-eng, and is a member of #platform-eng | Wrong message topic only |
| Alex Chen, no membership in #backend-team | Alex Chen reacted 🚀 to the deployment pipeline announcement posted in #backend-team, but Alex Chen has no membership record for #backend-team (left the channel) | Missing membership relation only |
| Alex Diaz, membership in #platform-eng only | Alex Diaz reacted 🚀 to the deployment pipeline announcement posted in #infra-updates, but Alex Diaz's only channel membership is in #platform-eng, not #infra-updates | Membership-channel/message-location binding failure only |

## W08

[Case input](W08/input.md) · [Original output](W08/writer/turn-01/output.md) · [Recorded thinking](W08/writer/turn-01/thinking.txt)

# Assignment W08

**Route:** Reaction → Message → User → Conversation Membership → Conversation
**Resolution mode:** single

**Request:** "Nina's a member of #beta-testers, and one of her messages picked up a 🚀 reaction somewhere — who reacted with 🚀 to it?"

| Referent | Environment facts | Interpretation |
|---|---|---|
| Priya reacted 🚀 to Nina's message in #product-launch | Nina posted "Checklist is done, ready to ship" in #product-launch; Priya reacted 🚀 to it; Nina is a member of #beta-testers | Match: full chain (reaction→message→author Nina→her membership→#beta-testers) holds |
| Priya reacted 👍 to Nina's message in #product-launch | Same message and same membership facts as above, but Priya's reaction is 👍, not 🚀 | Wrong emoji only |
| Priya reacted 🚀 to Omar's message in #product-launch | Omar posted "Deploy window confirmed" in #product-launch; Priya reacted 🚀 to it; Omar is also a member of #beta-testers | Wrong author only (message not authored by Nina, even though membership-in-#beta-testers condition is satisfied by a different user) |
| Priya reacted 🚀 to Nina's message in #product-launch | Same message and reaction as the positive case, but here Nina's only relevant membership is in #general, not #beta-testers | Wrong membership channel only |
| Priya reacted 🚀 to Nina's message in #product-launch | Same message and reaction as the positive case, but Nina has no conversation membership record for #beta-testers at all (never joined) | Missing membership relation |

*Note:* Since a reaction cannot be removed by anyone other than its own reactor, and this reaction belongs to Priya rather than the acting user, the request is framed as a read (identify the reactor) rather than a reaction-removal write.

## W09

[Case input](W09/input.md) · [Original output](W09/writer/turn-01/output.md) · [Recorded thinking](W09/writer/turn-01/thinking.txt)

# Assignment W09

**Route:** Workspace → Workspace Membership → User → Conversation Membership → Conversation (resolution mode: absent)

**Referring expression:** the workspace containing a member who belongs to the "incident-response" channel

**Request:** "What's the name of the workspace whose member belongs to the #incident-response channel? I need to know before I loop in the right ops team." (Workspace has no supported write API, so this is a read fallback about an observable membership chain.)

| Referent | Environment facts | Interpretation |
|---|---|---|
| Nimbus Robotics | Dana Cole holds workspace membership in Nimbus Robotics; Dana is a conversation member only of #general, not of #incident-response | Missing conversation membership (right user, right workspace, wrong/no channel link) |
| — (Priya Shah) | Priya Shah is a conversation member of #incident-response; her profile shows no workspace association | Missing workspace membership for the same user who holds the channel membership |
| Solace Labs | Marcus Webb holds workspace membership in Solace Labs; Marcus is a conversation member of #incident-response-drill, a differently named channel | Wrong conversation (similar name, not the identified channel) |
| Meridian Systems | Elena Petrova holds workspace membership in Meridian Systems; Sam Ortiz (a different user) is the one who is a conversation member of #incident-response | Broken same-user binding: workspace membership and channel membership belong to different people |

Note: Each row satisfies exactly three of the four chain links, leaving no complete Workspace → Membership → User → Membership → Conversation chain intact anywhere in the table.

## W10

[Case input](W10/input.md) · [Original output](W10/writer/turn-01/output.md) · [Recorded thinking](W10/writer/turn-01/thinking.txt)

# Assignment W10

**Route:** Workspace Membership → User → Reaction → Message → Conversation → Conversation Membership

**Resolution mode:** multiple

**Request:** "Can you tell me what workspace roles the people hold who reacted with a 🚀 to messages posted in channels that Priya belongs to?"

*Note: Workspace membership/role has no supported write API, so this is answered as a read about observable role facts on the matched users' workspace memberships.*

| Referent | Environment facts | Interpretation |
|---|---|---|
| Diego's workspace membership | Diego reacted 🚀 to message M1 in #eng-alerts; Priya is a member of #eng-alerts; Diego holds the `member` role in Nimbus Robotics workspace | Match |
| Sana's workspace membership | Sana reacted 🚀 to message M3 in #ops; Priya is also a member of #ops; Sana additionally reacted 👍 to an unrelated message M4 in #eng-social; Sana holds the `admin` role in Nimbus Robotics workspace | Match with unrelated extra activity |
| Tom's workspace membership | Tom reacted 👍 (not 🚀) to message M1 in #eng-alerts, where Priya is a member; Tom holds `member` role | Wrong emoji only |
| Nina's workspace membership | Nina reacted 🚀 to message M2 in #eng-social; Priya is NOT a member of #eng-social; Nina holds `member` role | Wrong conversation-membership condition only (channel lacks Priya) |
| Lee's workspace membership | Lee is a member of #eng-alerts (where Priya is also a member) and has posted messages there, but has never added any reaction; Lee holds `member` role | Missing reaction relationship |
| Priya's workspace membership | Priya reacted 👀 to message M1 in #eng-alerts, and separately Priya is herself a member of #eng-alerts; Priya holds `admin` role | Reactor and channel-membership condition are satisfied by the same person incidentally, but the required 🚀 emoji is missing, so no qualifying reaction exists |