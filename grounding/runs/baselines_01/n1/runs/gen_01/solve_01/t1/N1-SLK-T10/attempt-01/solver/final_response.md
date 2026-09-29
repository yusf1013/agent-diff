I checked the workspace — **jordan.lee@example.com isn't a member of this Slack workspace**, so I can't add them to the channel.

What I found:
- `#events2` exists (channel ID `C_EV2`)
- The only members are: Agent Bot, Aisha Khan, Diego Alvarez, Leo Park, Maya Chen, Nina Patel, Omar Haddad, Priya Sharma — no Jordan

`conversations.invite` only works for existing workspace members, and this API setup doesn't have the admin "invite by email to workspace" endpoint.

**To get them in:** a workspace admin would need to invite jordan.lee@example.com to the Slack workspace first (via the Slack UI or an admin token with that scope). Once they're a member, just say the word and I'll drop them into #events2.
