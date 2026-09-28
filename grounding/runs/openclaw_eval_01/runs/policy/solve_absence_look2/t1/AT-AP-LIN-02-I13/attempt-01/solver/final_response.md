I found a genuine identity mismatch I want to flag before I change anything, because there are **three different "Priya Chen" users** in your workspace and only one of them holds a security review ticket.

What's in Linear:

- **GRC-4 · Security review: Billing service** (priority: High) — assigned to **Priya Chen · `priya.chen@vendorstaff.example`** (guest: yes)
- That's the *only* security review ticket held by any Priya Chen.

The user matching your description exactly — "our guest reviewer from **vendorworks.example**" — is **Priya Chen · `priya.chen@vendorworks.example`** (also a guest), but **that person has no assigned issues at all**, no security review ticket.

So your two identifiers point at two different people:
- "guest reviewer from vendorworks.example" → the vendorworks guest (no ticket)
- "the security review ticket" → the vendorstaff guest's GRC-4

Which did you mean?

1. **Bump GRC-4** (the actual security review ticket, held by the `vendorstaff.example` Priya Chen) to Urgent — this is the only actionable "security review ticket," so I'd guess this one.
2. You actually meant the `vendorworks.example` guest — in which case there's no security review ticket to bump and something's off.

Confirm **#1** and I'll set GRC-4 to Urgent right away.
