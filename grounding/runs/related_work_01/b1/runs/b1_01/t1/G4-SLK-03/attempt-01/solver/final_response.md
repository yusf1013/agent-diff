Found the right message — Diego's latest in #deployments: *"Gateway rollback complete, traffic is recovering."* (12:40).

But I can't add the reaction: the Slack API access here only supports `reactions.get` and `reactions.remove` — there's no `reactions.add` (the proxy rejected it with `unknown_method`).

Two ways forward:
1. **You add it manually** — it's the top message in #deployments, or this permalink: https://example.slack.com/archives/CUOTU572SNZ/p1789994400000006
2. **Enable the `reactions:write` scope** for the Slack integration, and I'll be able to add/remove reactions going forward (I could then add it to this message too).

Want me to set anything else up on the Slack side?
