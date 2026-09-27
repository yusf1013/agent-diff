There is no incidents channel about a checkout outage in your workspace. The only incidents channels that exist are:

1. **incidents-auth** (active) — covers a login rate-limiting incident, explicitly noted as unrelated to checkout.
2. **incidents-shipping** (archived) — covers shipping carrier delays and SLA tracking.

Neither of these is about a checkout outage, so there's nothing to unarchive. If a checkout incident channel existed previously, it may have been deleted rather than archived, in which case it can't be recovered via the API.
