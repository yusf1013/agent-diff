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