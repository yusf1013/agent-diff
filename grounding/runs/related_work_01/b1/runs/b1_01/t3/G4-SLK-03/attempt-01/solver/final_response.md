I found the message and tried to add the reaction, but I'm stuck:

- **Message found**: Diego Alvarez (diego.alvarez) in #deployments, 08:40 EDT — "Gateway rollback complete, traffic is recovering."
- **Blocker**: the Slack integration in this environment doesn't expose the `reactions.add` endpoint (it returns `unknown_method`). Only `reactions.get` and `reactions.remove` are available, so I can read or remove reactions but not add one.

You'd need to add 👀 manually, or the Slack integration's proxy would need `reactions.add` enabled for me to do it.
