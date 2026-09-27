Removed it. ENG-7 ("Upgrade auth library") had a **blocks** relation to ENG-9 ("Run database migration for the v2 schema") — I deleted that relation, and ENG-7 now has no relations left.

One note: in Linear's data it was ENG-7 *blocking* the migration issue, not the other way around, but I went ahead and removed the relation as you asked. Let me know if that wasn't what you intended.
