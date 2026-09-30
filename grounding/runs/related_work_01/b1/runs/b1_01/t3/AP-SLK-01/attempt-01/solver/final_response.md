I found the exact message you meant, but I can't add the reaction — the Slack integration here doesn't expose `reactions.add` (the proxy rejects it as `unknown_method`; only `reactions.get`/`reactions.remove` are available).

For reference, this is the message I identified:

- **Channel:** #launch-planning
- **User:** Farhan Malik (farhan.malik, "Deebo")
- **Text:** "Confirmed: the launch date is set for March 3."
- **ts:** `1772377200.000001`
- **Existing reaction:** :eyes: from nadia.brooks — matches your description exactly (his other confirmation messages didn't have Nadia's :eyes:, and a user named "Farhan (Ops)" sent a separate confirmation without it)

You can add the :tada: yourself on that message, or if you can enable `reactions.add` on the Slack proxy, I'll fire it off in one shot.
