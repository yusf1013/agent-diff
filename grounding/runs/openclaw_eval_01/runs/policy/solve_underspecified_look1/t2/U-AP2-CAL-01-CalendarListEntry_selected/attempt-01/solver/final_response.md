I hit a blocker and need to flag both issues:

**1. Two calendars are named "Product Team":**
- `product_team_eng` (owned by priya.nair@northwind.example)
- `product_team_mkt` (owned by dana.whitfield@northwind.example)

There's also a "Product Team Offsite" calendar, but the target name "Eng Product Sync" points clearly at the **eng** one.

**2. I can't rename it:** the PATCH returned `403 — You do not have permission to update this calendar`. Your account is not the data owner of either calendar (they're owned by Priya Nair and Dana Whitfield respectively), and even reading their ACLs is forbidden — so your access is likely read-only or limited.

**To unblock this, one of:**
- Priya (owner) renames it herself, or
- She adds you as owner on the calendar (Settings → product_team_eng → Share → add as owner), after which I can do the rename.

Want me to try renaming the *mkt* calendar instead (in case that was the intended one), or shall we wait on access to the eng one?
