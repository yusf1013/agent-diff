I checked — but there's a direction mismatch, so I didn't make any change.

What actually exists in Linear is the **opposite** relation:

- **ENG-7 "Upgrade auth library" blocks ENG-9 "Run database migration for the v2 schema"** (relation id `r-1`)

There is no relation where the migration issue blocks ENG-7 — in fact, no "blocks" relation points at ENG-7 at all (its `inverseRelations` is empty).

Since the relation you described doesn't exist (the one that does exists in the reverse direction), I left everything as-is. If you actually want to remove **ENG-7 → blocks → ENG-9**, say the word and I'll delete it.
