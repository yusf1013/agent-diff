Heads up — no change ended up sticking, and here's why:

There's a naming collision. Both the **Mobile** and **Web** teams have a "Cycle 4." I initially found Maya Chen's issue in the Atlas project, "Cycle 4" — but it turned out to be **MOB-1 "Fix push-notification badge count"**, which is in *Mobile's* Cycle 4, not Web's. I set it to High, caught the mismatch, and reverted it back to No priority.

Here's what Maya Chen actually has in Atlas:

- **MOB-1** "Fix push-notification badge count" → Mobile · Cycle 4 (priority: No priority, as before)
- **WEB-7** "Tighten session-refresh logging" → Web · **Cycle 5** (priority: No priority)

There is no Atlas issue assigned to Maya Chen in Web's Cycle 4. Did you mean MOB-1 in Mobile's Cycle 4, or WEB-7 in Web's Cycle 5? Happy to set High on whichever one you intended.
