Done. ENG-7 (Upgrade auth library) no longer has a blocking relation with the migration issue — confirmed via verification that its relations list is now empty.

One note: there were actually two blocking relations between these issues, and I removed both:
- **ENG-9 (Run database migration for the v2 schema) → blocks → ENG-7** — the one you described
- **ENG-7 → blocks → ENG-9** — the reverse direction, which was also set up (contradictory with the above)

Remaining relations on ENG-7: a "related to" link with ENG-9 (kept), and ENG-10 (Automate database backups) still blocks ENG-7 — untouched. If you wanted to restore the ENG-7→ENG-9 "blocks" relation, let me know.
