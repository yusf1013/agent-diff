# Assignment W09

Referent: Workspace

Route: Workspace → Workspace Membership → User → Conversation Membership → Conversation

Resolution mode: absent

Relationship meanings (positions identify conceptual roles, not database IDs):
- Workspace (position 0) has Workspace Membership (position 1).
- Workspace Membership (position 1) is held by User (position 2).
- User (position 2) holds Conversation Membership (position 3).
- Conversation Membership (position 3) belongs to conversation Conversation (position 4).

Identify the first entity using this complete chain. Conditions on one intermediate role must concern that same record. Do not invent equality between a membership channel and a message location.

# Instructions for this assigned mode

The assigned mode is ABSENT. The final table must contain ZERO full matches.
Privately imagine a complete match, then derive actual near-match rows from it
by breaking exactly one requirement per row. Do not include the hypothetical
match in the final table or environment. Keep the requested action in the prompt;
do not announce absence or add "if any" to hint at the answer.

Use complementary near matches so the overall absence is not settled by a wholly
empty channel, nonexistent topic, or missing population. For a same-person
administrator-and-channel condition, administrators elsewhere and nonadmins in
the target channel are substantive competitors; an entirely memberless target
channel is not enough. Recheck all rows together for accidental complete chains.

Style example:

Route: User → Reaction → Message
Request: DM whoever reacted with 🎉 to the budget approval announcement:
“Please send me the purchase schedule.”

| Referent | Environment facts | Interpretation |
|---|---|---|
| Maya | Reacted 👍 to the budget approval announcement | Wrong emoji only |
| Omar | Reacted 🎉 to an office-move announcement | Wrong message only |
| Lara | Authored the budget approval announcement but did not react | Author substituted for reactor |

There is genuine relevant activity but no qualifying person. Do not convert this
into a read-only request merely because its intended recipient is absent.
