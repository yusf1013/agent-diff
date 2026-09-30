All done — sprint cleanup is set up in Linear:

- **BE-1** — "Complete PostgreSQL database migration to Aurora" (existing, In Progress) — used as the dependency
- **BE-2** — "Q1 Infrastructure Overhaul" created in Backend, assigned to **Olga Petrova** with **High** priority
- **BE-3** — "Upgrade Redis cluster to v7" created under BE-2 (parent set), assigned to **Jamal Abdullah**, and blocked by BE-1 (BE-1 → blocks → BE-3)
- Standup comment was created on BE-3, then **deleted** as you asked — BE-3 now has zero comments, and the migration ticket (BE-1) was never touched

Verified: BE-3's parent is BE-2, comments list is empty, and both assignees/priority are in place.

One heads-up: the directory has **two** users named Jamal Abdullah (`jamal.abdullah@backend.org` and `jamal.abdullah2@backend.org`). The assignment landed on `jamal.abdullah2@backend.org` (the other ID was rejected by the API when I tried it). If that's the wrong Jamal, say the word and I'll flip it.
