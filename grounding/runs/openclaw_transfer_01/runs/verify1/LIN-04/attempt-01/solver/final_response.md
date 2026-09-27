Before making the change, I checked ENG-7's actual relations in Linear, and the direction doesn't match what you described:

**What I found:**
- **ENG-7** "Upgrade auth library" has one blocking relation: it **blocks ENG-9** ("Run database migration for the v2 schema")
- ENG-7 itself is **not blocked by** the database migration issue — it's the other way around: the migration (ENG-9) is blocked by ENG-7
- There are no other block/blocked-by relations on ENG-7 (just one "related" relation)

So removing the relation I found wouldn't unblock ENG-7 — it would unblock ENG-9 instead.

How would you like to proceed?

1. **Delete the relation anyway** (ENG-7 no longer blocks ENG-9)
2. **Flip it** — remove ENG-7 → ENG-9 and instead make ENG-9 block ENG-7
3. **Something else** — maybe you meant a different issue

I haven't changed anything yet.
