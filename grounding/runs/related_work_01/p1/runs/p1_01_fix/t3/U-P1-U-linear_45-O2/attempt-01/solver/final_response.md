All done and verified. Summary:

1. **Migration issue found:** BE-1 — "Complete PostgreSQL database migration to Aurora" (In Progress, Olga). ⚠️ Note: BE-2 is an exact duplicate of BE-1 (same title, description, state, assignee). I used BE-1 (the original) for the dependency — worth cleaning up that duplicate at some point.
2. **Epic created:** BE-3 — "Q1 Infrastructure Overhaul" in the Backend team.
3. **Sub-issue created:** BE-4 — "Upgrade Redis cluster to v7", parent set to BE-3 (confirmed).
4. **Dependency set:** BE-1 → blocks → BE-4 (verified via relations).
5. **Standup note:** Created on BE-4 as instructed, then deleted after your correction — BE-4 now has zero comments. The note did *not* end up on the migration ticket either, per your instruction to just delete.
6. **Assignments:** BE-4 → Jamal Abdullah; BE-3 → Olga Petrova with priority 3 (High). Both confirmed.

Final state: BE-3 (Olga, High) ← BE-4 (Jamal), blocked by BE-1.
