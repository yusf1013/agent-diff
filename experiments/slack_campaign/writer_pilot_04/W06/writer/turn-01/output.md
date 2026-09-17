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