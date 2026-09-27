There's no blocking relation to remove — I checked.

What actually exists: **ENG-7 (Upgrade auth library)** has one relation, and it's the *reverse* of what you described: ENG-7 **blocks** ENG-9 (Run database migration for the v2 schema). ENG-9's side has no relations at all, confirming nothing is blocking ENG-7.

So nothing was deleted. If you actually want ENG-7 to be blocked by ENG-9 (or to remove the existing ENG-7 → ENG-9 blocks relation), say the word and I'll flip or delete it.
