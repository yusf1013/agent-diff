I found the message, but I'm blocked on adding the reaction.

**Found it:** In #eng-updates, the rollout-timeline message Priya reacted to with 👀 is Leo Park's *"Rollout timeline: shipping to prod Friday 3pm."* (ts `1789916400.000001`) — it currently has 👀 from Priya and 👍 from Diego.

**Blocker:** The Slack API proxy in this setup doesn't expose `reactions.add` — it returns `unknown_method`. The skill only supports reading/removing reactions (`reactions.get`, `reactions.remove`), not adding them, and the endpoint isn't available through any alternate route I tried.

Could you add the 🚀 yourself, or let me know if there's another Slack integration I should use?
