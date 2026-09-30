I found the right message but hit a wall:

**Target identified:** In `#incidents`, the only payment-gateway-timeout message from a `#payments-oncall` member is:
- *"Seeing 504s tied to a payment gateway timeout on checkout after the last deploy."* — posted by `UCSQXSCO8QP` (the one oncall-channel member who posted a timeout message; the other timeout posters aren't in #payments-oncall)

**Blocker:** The Slack API proxy in this environment doesn't implement `reactions.add`. It's whitelisted but returns `unknown_method` for every variant I tried (JSON body, form POST, GET, auth header, alternate spellings), while `reactions.remove` and `reactions.get` on the same proxy work fine. I'm not going to try to route around the proxy's method allowlist.

So I can't add the 👀 reaction as things stand — if the proxy admin enables `reactions.add`, I can retry in one command. Alternatively, if you'd like, I can leave a short message or thread reply in #incidents instead — just say the word.
