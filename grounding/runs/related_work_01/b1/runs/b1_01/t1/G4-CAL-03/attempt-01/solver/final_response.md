Done. The Budget review with Maya Chen (Thu June 21, 10:00–11:00 AM) is now set to **Room 5B** on your primary calendar, and Maya was sent an update.

One heads-up: this Calendar API setup doesn't support in-place event updates (PATCH/PUT return 404), so I had to remove the old event and re-create it with the new location. The time, attendee, and details are all preserved, but internally it's technically a new event ID — if Maya's client shows a cancellation + new invite rather than a clean "location changed" update, that's why.
