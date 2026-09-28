There's a snag — two calendars share the name "Product Team":

- **product_team_eng** (owned by priya.nair@northwind.example) — you have *writer* access
- **product_team_mkt** (owned by dana.whitfield@northwind.example) — you have *reader* access

Renaming a calendar requires **owner** access, so the account I'm authenticated as (jordan.lee@northwind.example) can't update either one's metadata directly.

Which calendar did you mean? And since you're not the listed data owner on either, a couple of options:

1. If you actually do own it (the dataOwner field may just be showing the admin), I can try the PATCH anyway — it'll 403 if not.
2. I can ask one of the owners (Priya/Dana) to make you an owner, then I'll rename it.
3. If you meant to rename one of *your* calendars (e.g., you're thinking of a calendar that's actually yours), point me to it and I'll handle it right away.

Want me to just try the rename on `product_team_eng` (the one you have writer access to) and see if it goes through?
