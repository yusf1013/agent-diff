Done — the blocking relation is removed.

One wrinkle worth knowing: the relation in Linear was stored backwards from how you described it. It said **ENG-7 blocks ENG-9** ("Run database migration for the v2 schema"), rather than ENG-7 being blocked by it. Since ENG-7 has no other relations, that was unambiguously the one you meant, so I removed it. Verified: ENG-7 now has no relations at all.

If you actually wanted to express "the migration issue blocks ENG-7" (rather than remove the relation entirely), let me know and I'll create it with the correct direction.
