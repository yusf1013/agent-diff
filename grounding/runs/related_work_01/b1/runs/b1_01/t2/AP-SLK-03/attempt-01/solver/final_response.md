I found the exact message — but hit a wall adding the reaction.

**Target identified:**
- Channel: `#eng-updates`
- Message: "Rollout timeline: shipping to prod Friday 3pm." (ts `1789916400.000001`) — the one Priya Sharma (UDQOKTF5IKJ) reacted to with 👀
- Note: there's a second eyes reaction in that channel, but it was from someone else (UI4KCKXRY5Z) on "Rollout timeline slipped by one day," so the first one is the unambiguous match.

**The problem:** this Slack integration's API proxy doesn't support `reactions.add` — it returns `unknown_method` (only `reactions.get`/`reactions.remove` are exposed). Auth is working fine, so it's just a missing endpoint on the proxy side, not a permissions issue.

So I can't add 🚀 programmatically from here. Options:
1. You add the rocket reaction manually in Slack (message is from Friday per the channel history, about "shipping to prod Friday 3pm").
2. If you can enable `reactions.add` on the Slack proxy, I'll do it immediately.

Want me to retry anything, or is there another way you'd like to handle it?
