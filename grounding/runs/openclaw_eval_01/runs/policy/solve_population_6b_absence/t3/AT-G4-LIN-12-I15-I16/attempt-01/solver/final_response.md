I can't cleanly resolve that, so I paused before changing anything. Here's what I found in Linear:

**No user named "Rae Ellison" exists.** Close matches:
- **Rae Quinn** — America/Chicago, status "Reviewing support queue" ✓ (but assigned to zero issues)
- **Raquel Ellison** — America/Chicago, status "Reviewing support queue" ✓ (also assigned to zero issues)

**Apex (APX) team has two offline sync issues**, but neither is assigned to either of those people:
- **APX-6** — "Offline sync timeout handling" (estimate 1) → **Raquel Ibarra**, America/**Denver**
- **APX-7** — "Offline sync delta download" (estimate 1) → **Raquel Okafor**, Europe/**Berlin**

So the "Chicago time + Reviewing support queue" clue matches Rae Quinn and Raquel Ellison, but neither owns an offline sync issue — and the two actual offline sync issues are owned by people in Denver and Berlin (who, coincidentally, also have the same status label).

Which one did you mean? For example:
1. APX-6 (Ibarra) → set estimate to 3
2. APX-7 (Okafor) → set estimate to 3
3. A different issue if it was reassigned recently or has a different title

Tell me which and I'll make the change.
