Route: Conversation → Message → Reaction → User
Resolution mode: underspecified

**Request:** Post "Kickoff meeting moved to Monday" in the channel with the budget-approved message that Alex reacted to with 🎉.

**Selection conditions:** conversation contains a message whose text concerns a budget being approved, that message received a 🎉 reaction from a user whose first name is Alex.

| Referent | Environment facts | Interpretation |
|---|---|---|
| finance-updates | Alex Rivera reacted 🎉 to its "Q3 budget approved" message | Alternative through Alex Rivera |
| planning-sync | Alex Kim reacted 🎉 to its "marketing budget approved" message | Alternative through Alex Kim |
| vendor-notes | Alex Rivera reacted 👍 to its "budget approved" message | Wrong emoji only |
| team-social | Alex Kim reacted 🎉 to its "office party announcement" message | Wrong message topic only |

Note: the two alternatives are distinguished only by the reactor's surname (Alex Rivera vs. Alex Kim), a detail the request omits; no choice between them is authorized.