Task completed:
1. **Hid the "Family" calendar** (`johnson@northwind.example`) by patching its `hidden` field to `true`.
2. **Removed two hidden read-only calendars** from the calendar list:
   - `holidays@northwind.example` (hidden, reader)
   - `league@northwind.example` (hidden, reader)

Note: `oncall@northwind.example` was also hidden but had **writer** access, so it was correctly left in place.
