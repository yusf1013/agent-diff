Done. The blocking relation tied to the database migration issue has been removed from ENG-7 ("Upgrade auth library") and the change is verified — ENG-7 has no relations now.

One note: in Linear the relation was actually recorded as **ENG-7 blocks ENG-9** ("Run database migration for the v2 schema") rather than ENG-7 being blocked by ENG-9. If you expected the opposite direction, that may be worth double-checking on your side.
