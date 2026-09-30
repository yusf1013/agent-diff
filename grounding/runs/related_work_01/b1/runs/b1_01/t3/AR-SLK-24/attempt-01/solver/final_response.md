I've hit a dead end: the Slack integration here only exposes **`reactions.get`** and **`reactions.remove`** — there's no `reactions.add` available (the proxy rejects it with `unknown_method`).

Here's what I confirmed before that:

- **5 payment-gateway-timeout messages** in #incidents
- **Exactly one** author of those messages is a member of #payments-oncall: **UCSQXSCO8QP**, who posted *"Seeing 504s tied to a payment gateway timeout on checkout after the last deploy."* (ts `1790258400.000001`)
- I verified the #payments-oncall member list contains only that user from the timeout posters

So the target message is identified and I'm ready — but I can't add the 👀 reaction through the available API. If the proxy gets `reactions.add` enabled (or you have a token with that scope I can use directly), I can fire it off immediately.
