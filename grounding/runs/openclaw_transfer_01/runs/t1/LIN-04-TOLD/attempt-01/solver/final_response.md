Done — the blocking relation existed and is removed.

- **ENG-7** (Upgrade auth library) was blocked by **ENG-9** (Run database migration for the v2 schema)
- Deleted that blocking relation (`r-3`) and verified: ENG-7 now only has a "related" link to ENG-9 (and still blocks nothing). It's no longer blocked.
