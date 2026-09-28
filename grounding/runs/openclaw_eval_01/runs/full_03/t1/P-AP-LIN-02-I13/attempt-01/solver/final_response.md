I checked Linear and there's a catch I want to flag before changing anything.

There is **no security review ticket assigned to a Priya Chen from vendorworks.example**.

Here's what I found:

- There are **three** "Priya Chen" accounts in your workspace, plus a "Priyanka Chen":
  - `priya.chen@vendorworks.example` — has **no** assigned issues
  - `p.chen@vendorworks.example` — has **no** assigned issues
  - `priya.chen@vendorstaff.example` — this one **does** have a security review ticket
- The only security review tickets that exist are:
  - **GRC-4 — "Security review: Billing service"** → assigned to Priya Chen **@vendorstaff.example**
  - **GRC-5 — "Security review: Network access"** → assigned to Dana Whitfield

So the only security review ticket going to a "Priya Chen" belongs to a **vendorstaff.example** account, not **vendorworks.example**. Since you specifically scoped this to the vendorworks guest reviewer, I did **not** bump anything — I didn't want to change priority on what may be a different person's ticket without confirming.

If you actually meant the **vendorstaff.example** Priya Chen (GRC-4 "Security review: Billing service"), just say the word and I'll set it to Urgent.
