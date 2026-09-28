I checked Linear and there's a domain mismatch I want to flag before changing anything:

**No security review ticket is assigned to a Priya Chen from vendorworks.example.** There are actually two accounts under that name at vendorworks (`priya.chen@vendorworks.example` and `p.chen@vendorworks.example`) — both have zero assigned issues.

What I *did* find: **GRC-4 — "Security review: Billing service"** (priority: High, currently 3.0), assigned to a *different* Priya Chen: `priya.chen@vendorstaff.example` (note: vendor**staff**, not vendor**works**).

Since vendorworks and vendorstaff look like different organizations, I didn't want to bump the wrong person's ticket. Want me to set GRC-4 to Urgent, or should I leave it?
