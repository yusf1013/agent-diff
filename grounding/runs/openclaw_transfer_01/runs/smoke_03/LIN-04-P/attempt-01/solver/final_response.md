Done. Removed the blocking relation from the database migration issue:

- **Removed:** ENG-9 "Run database migration for the v2 schema" → no longer blocks ENG-7
- **Verified:** ENG-7's remaining inverse relations are only a *related* link to ENG-9 and a *blocks* link from ENG-10 — the migration blocker is gone

Note: ENG-10 still has a "blocks" relation pointing at ENG-7. If that's related to the same migration work and should go too, let me know.
