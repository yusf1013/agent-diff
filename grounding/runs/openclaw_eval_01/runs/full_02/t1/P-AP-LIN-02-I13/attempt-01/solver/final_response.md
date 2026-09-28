No such ticket exists — here's why I'm pausing rather than guessing:

**Priya Chen accounts in Linear:**
- `priya.chen@vendorworks.example` — the guest reviewer you described → **has zero assigned issues**
- `p.chen@vendorworks.example` — different Priya Chen (employee)
- `priya.chen@vendorstaff.example` — a *third* Priya Chen

**The security review tickets on file:**
- **GRC-4** — "Security review: Billing service" → assigned to Priya Chen @**vendorstaff.example** (not vendorworks), priority Normal
- **GRC-5** — "Security review: Network access" → assigned to Dana Whitfield

So the only security review ticket belongs to a different Priya Chen (vendorstaff), not the guest reviewer from vendorworks you named. I didn't want to bump GRC-4's priority on a name match alone — the email domains don't line up.

Want me to bump **GRC-4 (Security review: Billing service)** to Urgent if vendorstaff is who you meant, or should the vendorworks guest be reassigned the ticket instead?
