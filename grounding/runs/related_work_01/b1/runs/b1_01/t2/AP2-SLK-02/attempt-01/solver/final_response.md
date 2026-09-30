I identified the right target and Aisha, but I can't complete the invite with the available API. Here's the breakdown:

**Channel identified:** `incident-response` (CHDGJMA7UI1)
- ✅ Name contains "incident", not archived
- ✅ Topic: "Postmortems and outage retros for live incidents"
- The other matches were filtered out: `incident-comms` (no postmortem topic), and `incident-response-archive` / `incident-2019-retro` (both archived)

**User identified:** Aisha Khan — `UWUIS8ZJWB4` (aisha.khan)

**The blocker:** This Slack proxy only exposes a limited set of API methods, and none of them can add *another user* to a channel:
- `conversations.invite` → `unknown_method`
- `channels.invite`, `users.invite`, `users.admin.invite`, `users.admin.conversations.invite` → `unsupported_endpoint`
- `conversations.join` (with `users` param) → returned `already_in_channel`, but that only joined the bot itself — verified via `conversations.members` that Aisha is **not** in the channel (members are still U01AGENBOT9, UD4FRIJ21TY, UO9107V7UZI)

To finish this, either invite Aisha manually in Slack (channel menu → Invite people), or enable the `conversations:invite` scope on the bot token so the invite endpoint works through the proxy. Want me to retry anything else in the meantime?
