No dedicated checkout-outage incident channel exists in the workspace. Here's what I found:

- **Only 3 channels exist:** `engineering-general`, `incidents-auth` (active, about a login rate-limiting incident), and `incidents-billing` (archived)
- **`incidents-billing`** is the only archived incident channel. Its topic is billing reconciliation and invoice retries, but its purpose notes it "also holds the checkout outage postmortem thread for reference"
- A message search for "checkout outage" turned up nothing

So there isn't one that's actually *about* the checkout outage — the closest match is the archived `incidents-billing`, which contains the postmortem thread. Want me to unarchive that one?
