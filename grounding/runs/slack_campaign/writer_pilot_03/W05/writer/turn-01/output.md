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