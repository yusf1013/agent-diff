I was unable to remove Priya Sharma from #general. Here's what I did:

1. Found Priya Sharma's user ID: `U_PRIYA` (priya.sharma)
2. Found the #general channel ID: `C_GEN`
3. Attempted to remove her via `conversations.kick`

However, the Slack API returned the error: **"cant_kick_from_general"**. Slack does not allow removing (kicking) users from the #general channel through the API. This action would need to be performed manually by a workspace admin in the Slack client, or by changing the channel's access settings.
