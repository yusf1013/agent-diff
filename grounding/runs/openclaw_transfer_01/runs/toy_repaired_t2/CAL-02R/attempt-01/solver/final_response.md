Successfully cancelled just this Tuesday's (June 19, 2018) instance of the weekly "Platform sync" event organized by Omar Haddad. I did this by:

1. **Found** the recurring "Platform sync" event (id: `ev_psync`, `RRULE:FREQ=WEEKLY;BYDAY=TU`) organized by Omar Haddad at 10:00 AM PT.
2. **Retrieved** the specific June 19 instance (id: `ev_psync_20180619T100000Z`).
3. **Deleted** that single instance with `sendUpdates=all`, which cancels only that occurrence as an exception.

Verified the result: the June 19 instance is now **cancelled**, while the next occurrence on June 26 and all other recurring instances remain **confirmed**. The rest of the series is untouched.
