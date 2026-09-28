**Task could not be completed due to insufficient permissions.**

Here's what I found and attempted:

1. **Located the calendar**: `leo-oncall@northwind.example` ("Leo on-call"), owned by Leo Park.
2. **Found the event**: "On-call handoff" (ID: `ev_handoff`), scheduled for 2018-06-19 at 09:00–09:30 PT.
3. **Attempted to add Priya Nair** (`priya.nair@northwind.example`) as an attendee via a PATCH request.
4. **Result**: The API returned a **403 Forbidden** error — *"Insufficient permissions for calendar: leo-oncall@northwind.example"*.

**Root cause**: The authenticated user only has **`reader`** access to Leo's on-call calendar. The `reader` role permits viewing events but does **not** allow modifying events or adding/removing guests. At least `writer` or `commenter` access (or being the organizer/owner) would be required to add Priya as a guest.

**Next steps**: Ask Leo Park (or an admin) to grant your account at least **writer** access to his on-call calendar, after which the guest addition can be completed.
