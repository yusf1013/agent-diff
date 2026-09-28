Done — with one caveat worth knowing.

**What I found:** There was no calendar named exactly "Product Team" — the only checked one matching that description was **"Product Team Offsite"** (owned by `maya.chen@northwind.example`, shared with you as a writer).

**What happened:** I couldn't rename the calendar itself — that requires owner access, and the API returned 403. So I applied a **per-user display name override** instead. Your calendar list now shows it as **"Eng Product Sync"** (verified, HTTP 200).

The difference: the calendar's real title is still "Product Team Offsite" for Maya and everyone else on it. If you want it renamed for everyone, Maya would need to do it or grant you owner access. Want me to keep it this way?
