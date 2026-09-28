No dedicated incidents channel for the checkout outage exists in your workspace. Here's what I found:

- **incidents-billing** — *archived*, topic is "Billing reconciliation queue and invoice retries," but its purpose notes it "also holds the checkout outage postmortem thread for reference."
- **incidents-auth** — active (not archived), explicitly about a login rate-limiting incident, "unrelated to checkout."
- A message search for "checkout outage" turned up nothing else.

So the only checkout-outage material lives inside the archived **incidents-billing** channel as a postmortem thread — that channel itself is a billing channel, not a checkout one. I didn't unarchive anything since it's not clearly "the" checkout channel.

Want me to unarchive **incidents-billing** anyway, or create a new `incidents-checkout` channel instead?
