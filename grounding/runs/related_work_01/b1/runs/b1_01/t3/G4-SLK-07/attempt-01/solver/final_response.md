I found the right channel, but I'm blocked on the actual change:

- **Channel:** `release-ops` (private) — Diego Alvarez's message "Gateway rollback finished on prod, the error rate is back to baseline."
- **Problem:** Setting a channel topic requires Slack's `conversations.update` endpoint, and this workspace's Slack proxy doesn't expose it (`unsupported_endpoint` on both POST and GET). The proxy only supports the endpoints in the skill doc — `conversations.rename` (name only, no topic) is the closest, and I didn't want to rename your channel when you asked for a topic.

Quick options:
1. You set it in the Slack UI: open `release-ops` → ⋯ → Edit channel → Topic: `Post-release monitoring` (takes 2 seconds).
2. If you'd rather I do it, the proxy config would need `conversations.update` allowed for the Slack service — happy to walk through that.
