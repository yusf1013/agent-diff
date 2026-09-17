# Assignment W10

Referent: Workspace Membership

Route: Workspace Membership → User → Reaction → Message → Conversation → Conversation Membership

Resolution mode: multiple

Relationship meanings (positions identify conceptual roles, not database IDs):
- Workspace Membership (position 0) is held by User (position 1).
- User (position 1) contributes Reaction (position 2).
- Reaction (position 2) is attached to Message (position 3).
- Message (position 3) is located in Conversation (position 4).
- Conversation (position 4) has Conversation Membership (position 5).

Identify the first entity using this complete chain. Conditions on one intermediate role must concern that same record. Do not invent equality between a membership channel and a message location.

Downstream operation menu for this referent:
No supported write. Read the administrator/owner flags or workspace identifier on the selected discoverable user's profile association. Ordinary-member versus guest classification is unavailable; ask about the specific exposed flag, not a full role label. Restrict the population to those displayed profile associations.

# Instructions for this assigned mode

The assigned mode is MULTIPLE. The final table must contain exactly 2
distinct intended root referents, jointly requested through ordinary plural
wording. Make useful positive variants: a simple complete match and a match with
additional unrelated activity. Both must remain complete matches. Then derive
one-requirement negatives; do not count several witnesses for one root as several
matches. This requested design count does not redefine the benchmark's mode.

Style example:

Route: Message → Reaction → User
Request: Add a heart to messages Tom reacted to with a thumbs up.

| Referent | Environment facts | Interpretation |
|---|---|---|
| A | Tom 👍 | Match |
| B | Tom 👍 and Maya 👀 | Match with unrelated activity |
| C | Tom 👀 | Wrong emoji only |
| D | Tim 👍 | Wrong person only |
| E | No reactions; other message facts unchanged | Missing reaction relationship |
| F | Tom 👀 and Tim 👍 | Person and emoji occur on different reactions |

Longer-route example showing distinct roots with shared records:

Route: User → Reaction → Message → Conversation
Request: DM the people who reacted with 🎉 to the office-move announcement in
#facilities: “Can you help with the move on Friday?”
Selection: emoji 🎉; announcement about the office move; location #facilities.

| Referent | Environment facts | Interpretation |
|---|---|---|
| Maya | 🎉 on the office-move announcement M in #facilities | Match |
| Theo | 🎉 on that same M; also 👀 on an unrelated lunch message | Match with extra activity |
| Omar | Only 👍 on M | Wrong emoji only |
| Lara | 🎉 on a parking-policy notice in #facilities; no reaction to M | Wrong topic only |
| Tim | 🎉 on an office-move announcement in #general; no reaction in #facilities | Wrong location only |
| Rina | 🎉 on the parking notice and 👍 on M, both in #facilities | Emoji and topic are on different reacted-to messages |

M is one shared message. Maya's and Theo's qualifying reactions cannot make Omar
or Rina qualify: users are the roots, and each needs their own complete chain.
Omar's 👍 is not another negative row for Maya. All rows coexist. No other reactions
by these users complete the chain. Adapt counts to the assignment, not this example.
