I found the message — Leo Park's "standup moved to 10:00" (ts `1789992300.000002` in #standup) — but I can't delete it. I'm authenticated as a bot (AgentBot), and Slack only allows bots to delete messages they posted themselves, so `chat.delete` returns `cant_delete_message`.

To get it removed, you'd need to delete it from your own account (right-click → Delete in the Slack client), or give the bot a user-token with `chat:delete` acting as a member — which isn't something I should wire up unilaterally. Diego's copy of the same message is untouched.
