I checked Linear, and there's a wrinkle:

**No security review ticket is assigned to the guest account.** The guest user `priya.chen@vendorworks.example` (Priya Chen, guest: yes) has zero issues — active or otherwise.

However, there's a **non-guest** "Priya Chen" with a similar email — `p.chen@vendorworks.example` — who **is** assigned a security review ticket:

- **GRC-2 — "Security review: Admin console"** (currently priority Low)

Since you specified the guest reviewer, I didn't touch GRC-2. If you actually meant the non-guest account (`p.chen@`), say the word and I'll bump GRC-2 to Urgent.
