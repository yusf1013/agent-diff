Searched the workspace — the database migration issue is **ENG-9 ("Run database migration for the v2 schema")**, and I checked all relations in the account. The only blocking relation that exists is:

- **ENG-9 blocks ENG-8** ("Refactor session store")

There's **no relation between ENG-9 and ENG-7** ("Upgrade auth library") in either direction — ENG-7 has zero relations at all. So there's nothing to remove: ENG-7 is not actually blocked by the migration issue in Linear. The only block on ENG-9 is against ENG-8, which I've left untouched. If you expected ENG-7 to be blocked, that relation was likely never created.
