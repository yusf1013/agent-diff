There's no such blocking relation on ENG-7. I checked its relations and the only one is:

- **ENG-7 → blocks → ENG-9** ("Run database migration for the v2 schema")

So the direction is reversed from what you described — ENG-7 is *blocking* the database migration issue, not blocked by it. There's no "blocked by" relation on ENG-7 to remove, so I left everything as-is. Let me know if you actually want me to remove that ENG-7 → ENG-9 blocks relation instead.
