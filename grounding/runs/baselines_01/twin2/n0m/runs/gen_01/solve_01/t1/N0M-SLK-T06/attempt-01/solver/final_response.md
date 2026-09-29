I couldn't do it — and it's not a mistake in my approach. Here's what I found:

- **Message:** "new logo draft is up" by Diego in #design (ts `1789992180.000001`)
- **Reactions on it:** 👀 eyes (Priya) and 👍 thumbsup (Priya)
- **The blocker:** I'm authenticated to Slack as **AgentBot**, and the Slack API only lets a caller remove *their own* reactions. `reactions.remove` returned `no_reaction` because AgentBot never reacted with 👀.

Slack has no API to remove another user's reaction — that's by design. To get rid of it, Priya (or you, if you have her account on a client) would need to click the 👀 off in Slack directly. If you'd like, I can message Priya in #design or a DM asking her to remove it.
