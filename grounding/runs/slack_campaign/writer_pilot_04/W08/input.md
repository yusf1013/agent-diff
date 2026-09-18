# Assignment W08

Referent: Reaction

Route: Reaction → Message → User → Conversation Membership → Conversation

Resolution mode: single

Relationship meanings (positions identify conceptual roles, not database IDs):
- Reaction (position 0) is attached to Message (position 1).
- Message (position 1) is authored by User (position 2).
- User (position 2) holds Conversation Membership (position 3).
- Conversation Membership (position 3) belongs to conversation Conversation (position 4).

Identify the first entity using this complete chain. Conditions on one intermediate role must concern that same record. Do not invent equality between a membership channel and a message location.

Downstream operation menu for this referent:
Prefer removing the actor's own selected reaction: choose actor-owned reactions when constructing the story. Other people's reactions cannot be removed. A read can report the reactor or emoji, but the answer should distinguish competing reactions.

# Instructions for this assigned mode

The assigned mode is SINGLE. The final table must contain exactly 1
intended root referent. Construct its complete qualifying facts first. Extra
unrelated activity may coexist, but no other root may satisfy the full request.
Then derive the one-requirement negatives. Do not delegate a choice among matches.

Style example (one recipient; facts about related messages stay within user rows):

Route: User → Reaction → Message
Request: DM the person who reacted with ✅ to the deployment announcement:
“Ready for the review?”

| Referent | Environment facts | Interpretation |
|---|---|---|
| Maya | Reacted ✅ to the deployment announcement | Match |
| Omar | Reacted 👍 to that announcement | Wrong emoji only |
| Lara | Reacted ✅ to an office-move announcement | Wrong message only |
| Tim | Authored the deployment announcement but did not react | Author substituted for reactor |

All planned message topics and relationships must preserve those interpretations.
