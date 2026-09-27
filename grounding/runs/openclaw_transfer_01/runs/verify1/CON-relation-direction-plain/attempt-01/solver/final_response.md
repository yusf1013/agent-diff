I checked ENG-7 ("Upgrade auth library") and there's no blocking relation on it — neither incoming nor outgoing. Its relations list is completely empty.

For context, the only "blocks" relation in the team is ENG-9 ("Run database migration for the v2 schema") blocking ENG-8 ("Refactor session store") — nothing touches ENG-7. So there's nothing to remove.

If you'd like ENG-7 to be blocked by (or to block) the migration issue, say the word and I'll set that up instead.
