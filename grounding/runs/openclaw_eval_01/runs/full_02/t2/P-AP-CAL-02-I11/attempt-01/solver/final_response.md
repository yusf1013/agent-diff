I checked your calendar list, and there's no match:

- **Team Calendar** (`team-sales@northwind.example`) — you have **reader** access on this one, not writer. It's also owned by leo.park@northwind.example, so it's not something you share out — and with reader access I can't even inspect its sharing/ACL to confirm design-team sharing (the API returns 403 for that).

Your other calendars are your personal one (owner) and **Marketing Sync** (reader), neither of which fits either.

So per your instruction, I haven't hidden anything. If you'd like, I can still hide the Team Calendar as-is (reader access is enough for that via the calendar list), or re-check later if access changes — just say the word.

⚠️ 🛠️ Exec failed: `fetch https://www.googleapis.com/calendar/v3/calendars/team-sales%40northwind.example/acl -> run jq`
