I found the exact target but hit a blocker on the last step.

**What I did:**
1. Located #incidents (`C7KWDBX02L7`) and #payments-oncall (`CNKAA28WL2K`)
2. #payments-oncall members: `U01AGENBOT9`, `UCSQXSCO8QP`, `U2VXWM7OP2O`
3. Five messages in #incidents mention "payment gateway timeout" — but only **one** was posted by a #payments-oncall member:
   - `UCSQXSCO8QP` (1790258400.000001): *"Seeing 504s tied to a payment gateway timeout on checkout after the last deploy."*

**The blocker:** The Slack API proxy in this setup only exposes `reactions.get` and `reactions.remove` — `reactions.add` returns `unknown_method`, so I can't add the eyes emoji (or any reaction) through it.

If you can enable `reactions.add` on the proxy/token, I'll add it immediately. Otherwise you'd need to add 👀 manually to that message.
