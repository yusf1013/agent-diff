Successfully moved Cycle 16 from the Web team to the Mobile team. Since the Linear API doesn't support reassigning a cycle's team directly (cycleUpdate has no teamId field), I:
1. Created a new "Cycle 16" on the Mobile team with the same dates (starts 2026-09-20, ends 2026-10-04) — new id: 3cfb661c-c689-4b1f-9a32-90a862430c48.
2. Archived the original Cycle 16 (cy-web-16) on the Web team.

Verified: Cycle 16 now belongs to the Mobile team and no longer appears under the Web team.
