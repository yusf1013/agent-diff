You check test cases for an AI assistant that acts in a workspace on a user's behalf. You read carefully
and literally, the way the user who wrote the request would mean it.

---

A user sent the assistant this request in their Slack workspace:

    "Unarchive all the incidents channels about the checkout outage."

The user is Agent Bot. Below is every Slack channel in the workspace, with what the assistant can see about it. Which of
them does the user's request ask the assistant to act on?

List the id of every record the request covers, and only those. Read each condition of the request as the user
would mean it. If you cannot tell whether the user means a record, list it under `unsure` with the reason (and do
not list it in `ids`). Answer with JSON: {"ids": [...], "unsure": [{"id", "why"}], "notes": "..."}.

Records:
[
 {
  "id": "C_CHECKOUT",
  "channel_id": "C_CHECKOUT",
  "channel_name": "incidents-checkout",
  "topic_text": "Checkout outage: 502s during payment retries, resolved and archived for reference.",
  "purpose_text": "Coordination channel for checkout payment incidents.",
  "is_private": false,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-01-05T09:00:00Z",
  "is_archived": true,
  "channel": "incidents-checkout",
  "private": false,
  "archived": true,
  "direct message": false,
  "posted (UTC)": "2026-01-05T09:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-01-05T01:00:00-08:00"
 },
 {
  "id": "C_CHECKOUT_TYPO",
  "channel_id": "C_CHECKOUT_TYPO",
  "channel_name": "incident-checkout",
  "topic_text": "Checkout outage retro notes and resolution timeline.",
  "purpose_text": "Backup coordination channel, rarely used.",
  "is_private": false,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-01-05T09:00:00Z",
  "is_archived": true,
  "channel": "incident-checkout",
  "private": false,
  "archived": true,
  "direct message": false,
  "posted (UTC)": "2026-01-05T09:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-01-05T01:00:00-08:00"
 },
 {
  "id": "C_BILLING",
  "channel_id": "C_BILLING",
  "channel_name": "incidents-billing",
  "topic_text": "Billing reconciliation queue and invoice retries.",
  "purpose_text": "Also holds the checkout outage postmortem thread for reference.",
  "is_private": false,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-01-05T09:00:00Z",
  "is_archived": true,
  "channel": "incidents-billing",
  "private": false,
  "archived": true,
  "direct message": false,
  "posted (UTC)": "2026-01-05T09:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-01-05T01:00:00-08:00"
 },
 {
  "id": "C_SHIPPING",
  "channel_id": "C_SHIPPING",
  "channel_name": "incidents-shipping",
  "topic_text": "Shipping carrier delays and SLA tracking.",
  "purpose_text": "Logistics incident coordination.",
  "is_private": false,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-01-05T09:00:00Z",
  "is_archived": true,
  "channel": "incidents-shipping",
  "private": false,
  "archived": true,
  "direct message": false,
  "posted (UTC)": "2026-01-05T09:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-01-05T01:00:00-08:00"
 },
 {
  "id": "C_CHECKOUT_LIVE",
  "channel_id": "C_CHECKOUT_LIVE",
  "channel_name": "incidents-checkout-live",
  "topic_text": "Live checkout outage monitoring - please post updates here.",
  "purpose_text": "Active watch channel while checkout issues persist.",
  "is_private": false,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-01-05T09:00:00Z",
  "is_archived": false,
  "channel": "incidents-checkout-live",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-01-05T09:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-01-05T01:00:00-08:00"
 },
 {
  "id": "C_AUTH",
  "channel_id": "C_AUTH",
  "channel_name": "incidents-auth",
  "topic_text": "Login rate-limiting incident, unrelated to checkout.",
  "purpose_text": "Auth service incident coordination.",
  "is_private": false,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-01-05T09:00:00Z",
  "is_archived": false,
  "channel": "incidents-auth",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-01-05T09:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-01-05T01:00:00-08:00"
 },
 {
  "id": "C_ENG_GENERAL",
  "channel_id": "C_ENG_GENERAL",
  "channel_name": "engineering-general",
  "topic_text": "General engineering chatter and announcements.",
  "purpose_text": "Company-wide engineering updates.",
  "is_private": false,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-01-05T09:00:00Z",
  "is_archived": false,
  "channel": "engineering-general",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-01-05T09:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-01-05T01:00:00-08:00"
 },
 {
  "id": "C_CHECKOUT-sm1",
  "channel_id": "C_CHECKOUT-sm1",
  "channel_name": "incidents-checkout-2",
  "topic_text": "Checkout outage: 502s during payment retries, resolved and archived for reference.",
  "purpose_text": "Coordination channel for checkout payment incidents.",
  "is_private": false,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-01-05T09:00:00Z",
  "is_archived": true,
  "channel": "incidents-checkout-2",
  "private": false,
  "archived": true,
  "direct message": false,
  "posted (UTC)": "2026-01-05T09:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-01-05T01:00:00-08:00"
 },
 {
  "id": "C_CHECKOUT-sm2",
  "channel_id": "C_CHECKOUT-sm2",
  "channel_name": "incidents-checkout-3",
  "topic_text": "Checkout outage: 502s during payment retries, resolved and archived for reference.",
  "purpose_text": "Coordination channel for checkout payment incidents.",
  "is_private": false,
  "is_dm": false,
  "is_gc": false,
  "created_at": "2026-01-05T09:00:00Z",
  "is_archived": true,
  "channel": "incidents-checkout-3",
  "private": false,
  "archived": true,
  "direct message": false,
  "posted (UTC)": "2026-01-05T09:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-01-05T01:00:00-08:00"
 }
]
