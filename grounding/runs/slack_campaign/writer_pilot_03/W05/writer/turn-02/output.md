## Audit

**Selection conditions from the request:** "the channels that have exactly 5 members" → root entity is Conversation; the sole identifying condition is a Conversation Membership count of exactly 5 for that conversation (all current conversation-membership records, actor included if present). Nothing about archived status, topic, or workspace membership is part of the request.

**Defects found:**
1. **#support contradicted itself** — it claimed "exactly 5 conversation memberships" while also saying those users were removed and only appear in message text. A row can't assert the qualifying count and then negate it. Fixed by making the count explicitly 0 active conversation memberships (a genuine missing-relationship negative), with the 5 names surviving only as message-text mentions (a plausible near-miss, not a stored membership).
2. **#product** was slightly ambiguous about which count is "official" — clarified that its true conversation-membership count is 3; the 5-person workspace-membership figure is a decoy for the wrong relationship role, not a competing true value.
3. Everything else (route, mode = 2 distinct roots, one-condition negatives, downstream write capability) checked out: posting a message to a channel is a supported write, and the two positive channels give distinguishable, observable answers (they are different channels receiving the same reminder).

No other defects found.

## Final sketch

**Route:** Conversation → Conversation Membership (position 0 → position 1)
**Resolution mode:** multiple (2 intended referents)

**Request:** "Post a reminder message in the channels that have exactly 5 members, letting everyone know Friday's stand-up moved to 10am."

| Referent | Environment facts | Interpretation |
|---|---|---|
| #launch-team | Conversation members: Ana, Ben, Cara, Dev, Eli — exactly 5 conversation memberships | Match: simple complete match, member count = 5 |
| #ops-sync | Conversation members: Fay, Gus, Hal, Ivy, Jax — exactly 5 conversation memberships; channel also has an unrelated pinned topic "Sprint planning" and an older message with a 🎉 reaction | Match with unrelated activity: count still = 5 |
| #design-crew | Conversation members: Kai, Lea, Mia, Nia — only 4 conversation memberships | Wrong count only (4, not 5) |
| #eng-all | Conversation members: Oli, Pia, Quin, Ravi, Sam, Tia — 6 conversation memberships | Wrong count only (6, not 5) |
| #product | Nora, Omar, Pat, Quinn, and Ray all hold workspace membership in the workspace containing #product (5 people), but only Nora, Omar, and Pat hold conversation membership in #product itself | Wrong relation role: workspace-membership count substituted for conversation-membership count; true conversation membership count = 3 |
| #support-archive | Channel is archived; no current conversation membership rows exist. Old messages in the channel mention "welcome Sasha, Tariq, Uzo, Val, Wren to the team," but none of the five hold an active conversation membership record | Missing relationship: 0 current conversation memberships despite five names appearing only in message text, not as memberships |

**Note:** Member count is computed strictly from current `Conversation Membership` records tied to the same conversation (including the actor if the actor holds membership there); workspace-level membership or names appearing only in message text are not substitutes for that relationship.