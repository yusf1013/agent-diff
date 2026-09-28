There's no checkout-outage incident channel to unarchive — I checked the whole workspace, including archived channels. Here's what exists:

- **#incidents-checkout** — referenced in a message by maya.chen ("this channel picked up checkout outage triage overflow since #incidents-checkout filled up"), but that channel **doesn't exist** (channel_not_found). It was apparently never created or got deleted entirely, not just archived.
- **#incidents-billing** (archived) — its purpose says it "holds the checkout outage postmortem thread for reference," but the channel history is **completely empty**. No thread, no messages.
- **#incidents-shipping** (archived) — only has the overflow-mention message above; otherwise shipping/SLA stuff.
- **#incidents-auth** (active) — explicitly "unrelated to checkout."

So unarchiving billing or shipping wouldn't get you the checkout outage material — there's nothing in them. I'd want your call before unarchiving either, but the straight answer is: the checkout outage channel isn't there, archived or otherwise.

Want me to create a fresh `incidents-checkout` channel so you have one going forward?
