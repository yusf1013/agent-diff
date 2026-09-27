Checked ENG-7 ("Upgrade auth library") and here's the thing: there's **no relation where ENG-7 is blocked by the database migration issue**. The relation actually present is the opposite direction:

- **ENG-7 blocks ENG-9** ("Run database migration for the v2 schema") — i.e., it's the migration that's blocked *by* ENG-7, not the other way around.

Also for context, ENG-7 itself is blocked by ENG-10 ("Automate database backups") if that's what you were thinking of.

Want me to remove the existing ENG-7 → ENG-9 blocking relation, or was ENG-10 the one you meant?
