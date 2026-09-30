Sprint cleanup complete in Linear ✅

**What happened, in order:**
1. **Migration issue found** — heads up: there are *two* identical "Complete PostgreSQL database migration to Aurora" issues in Backend (BE-1 and BE-2, same description, both assigned to Olga). I used **BE-1** (`de456789...`) as the canonical one — you may want to archive the duplicate.
2. **Epic created** — **BE-3 "Q1 Infrastructure Overhaul"** in Backend.
3. **Sub-issue created** — **BE-4 "Upgrade Redis cluster to v7"**, parent = BE-3.
4. **Dependency set** — BE-1 *blocks* BE-4 (Redis can't start until migration is done).
5. **Comment added to BE-4**, then **deleted** per your correction — verified BE-4 now has zero comments, so nothing is stranded on the wrong ticket.
6. **Assignments** — BE-4 → **Jamal Abdullah**; BE-3 → **Olga Petrova** with priority **High**.

Final verified state:
- BE-3: assigned Olga, priority 2 (High), epic
- BE-4: assigned Jamal, parent BE-3, blocked by BE-1, no comments
