I checked: the `new logo draft is up` message in #design (ts 1789992180.000001) has an 👀 reaction from Priya (U_PRIYA), plus her 👍. But I'm authenticated as **AgentBot**, not Priya — Slack's `reactions.remove` can only remove the authenticated user's own reaction, so the API returned `no_reaction` when I tried to remove eyes.

There's no public API way for me to remove *her* reaction while acting as the bot. Two options:

1. **Priya removes it herself** — easiest, one tap in Slack.
2. **Re-authenticate as Priya** (or with a token bearing her identity/scopes), and I'll remove it immediately.

Want to go with one of those?
