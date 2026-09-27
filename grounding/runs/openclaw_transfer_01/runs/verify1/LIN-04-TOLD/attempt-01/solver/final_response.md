I checked ENG-7's relations in Linear, and there's no blocking relation from the database migration issue to remove. Here's what actually exists:

- **ENG-9** ("Run database migration for the v2 schema") — only a **related** relation to ENG-7, and in fact ENG-7 *blocks* ENG-9, not the other way around.
- **ENG-10** ("Automate database backups") — this one does *block* ENG-7, but it's a backups issue, not the migration.

So no change was made. If you actually wanted to unblock ENG-7 from ENG-10, or remove the ENG-7→ENG-9 blocking relation, let me know and I'll do it.
