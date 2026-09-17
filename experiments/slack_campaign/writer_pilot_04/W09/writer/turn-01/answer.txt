Route: Workspace → Workspace Membership → User → Conversation Membership → Conversation
Resolution mode: absent

**Request:** "What workspace is shown on the profile of the bot that belongs to the #incident-response channel?"

**Selection conditions:** the target is the workspace membership (and its workspace) held by the user who (a) is classified as a bot, and (b) holds a conversation membership belonging to the #incident-response channel.

| Referent | Environment facts | Interpretation |
|---|---|---|
| Cascade Systems (via WatcherBot) | WatcherBot is bot-flagged, holds workspace membership in Cascade Systems, and is a member of #project-launch | Wrong conversation membership only |
| Nimbus Robotics (via Dana Reyes) | Dana Reyes is a non-bot user holding workspace membership in Nimbus Robotics and is a member of #incident-response | User is not bot-flagged (bot condition fails) |
| — (via PulseBot) | PulseBot is bot-flagged and is a member of #incident-response, but holds no workspace membership record | Missing required workspace membership (position 1 absent) |