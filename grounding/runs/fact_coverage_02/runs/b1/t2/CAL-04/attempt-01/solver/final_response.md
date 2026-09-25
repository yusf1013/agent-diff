Completed both tasks:
1. **Hid the "Family" calendar** (`johnson@northwind.example`): Set `hidden: true` via PATCH on the calendar list entry.
2. **Removed all hidden reader-only calendars**: Deleted `holidays@northwind.example` and `league@northwind.example` from the calendar list. The other hidden calendar (`oncall@northwind.example`) was left in place since it has "writer" access, not "reader".
