Done — there was a blocking relation, and I removed it.

One detail worth noting: it was the other direction than described. The relation was **ENG-7 blocks ENG-9** ("Run database migration for the v2 schema"), not ENG-7 blocked by ENG-9. I removed that relation (`r-1`) and verified ENG-7 now has no relations at all.
