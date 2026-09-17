# Assignment W06

Referent: Message

Route: Message → User → Conversation Membership → Conversation

Resolution mode: multiple

Relationship meanings (positions identify conceptual roles, not database IDs):
- Message (position 0) is authored by User (position 1).
- User (position 1) holds Conversation Membership (position 2).
- Conversation Membership (position 2) belongs to conversation Conversation (position 3).

Identify the first entity using this complete chain. Conditions on one intermediate role must concern that same record. Do not invent equality between a membership channel and a message location.

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
