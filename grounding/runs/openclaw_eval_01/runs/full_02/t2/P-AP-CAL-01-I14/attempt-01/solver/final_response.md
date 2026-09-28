Done — I set the **Client Success** calendar (cs-east@northwind.example) to hidden in your calendar list, and confirmed `hidden: true` in the API response. It will no longer appear in your calendar list UI.

Note: I also reset its `selected` flag to off, since the list entry was still reporting it as selected even though you'd unchecked it (possibly a stale client-side state). The subscription itself is intact — if you ever want it back, it's just one toggle away.
