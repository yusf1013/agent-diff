I located the channel — Diego Alvarez's rollback message ("Gateway rollback finished on prod…") is in the private channel **release-ops** (`CCP7RZLRCM1`) — but I can't set the topic from here.

The Slack proxy in this setup only exposes a limited set of API endpoints, and none of them support updating a channel topic:
- `conversations.update` → `unsupported_endpoint`
- `channels.update` / `groups.update` (legacy) → `unsupported_endpoint`

So the topic change has to be done in Slack directly: in #release-ops, click the channel name → **About → Edit** → set Topic to `Post-release monitoring`. (As a workaround, I *can* rename the channel via `conversations.rename` if you'd like, but that changes the name, not the topic.)
