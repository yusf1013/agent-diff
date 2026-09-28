No checkout incident channel exists in the workspace — I can't unarchive one. Here's what's actually there:

- **incidents-auth** (active) — login rate-limiting incident, explicitly "unrelated to checkout"
- **incidents-shipping** (archived) — topic says "Shipping carrier delays and SLA tracking," but a message in it notes it "picked up checkout outage triage overflow since #incidents-checkout filled up"

There's no channel named `incidents-checkout` or anything checkout-specific in the list (including archived ones). It may have been deleted or unlinked, or it's a private channel you're not in — I can't see it either way.

If you want, I can unarchive **incidents-shipping** since that's the one channel where the checkout outage triage actually landed — just confirm and I'll do it.
