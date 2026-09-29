You write test requests for an AI agent that acts in a workspace on a user's behalf. You are careful with
wording: a test request must read exactly as a real user would write it, and must ask for exactly what is intended.

---

Each item below is a request that asks the agent to act on ONE record in Linear. For each item:

1. Decide `plural_worthy`: could a real user plausibly ask the same thing about SEVERAL records at once, because
   several records can meet the same conditions? (Example: "Cancel the 8 a.m. meeting with Dana" -> "Cancel all the
   8 a.m. meetings with Dana" is plausible.) Answer false when the request picks out one record by something only
   one record can have (an exact unique title or name, "the most recent", "the one that...", a record the
   conditions make unique by nature), or when doing the action to several records makes no sense. Give the reason.
2. Write `plural_request`: the request rewritten to ask for every record that meets the same conditions.
   - Keep every condition of the original, word for word where you can, and add no new condition.
   - Keep the action and its values (tags, dates, names, emoji) unchanged.
   - Say it the way a user would ("every", "all", plural nouns).
   - Do not say where the records are beyond what the original says: no "including ...", "on any calendar",
     "in all channels", "hidden", "private", "archived", "subfolders", "every page", "anywhere".
   If `plural_worthy` is false, still write your best plural wording.
3. Write `search_words`: the one to three words a user would type into Linear's search box to look for these
   records (content words, no search operators).
4. Write `variants`: three different values of the record's main text that a real record meeting EVERY condition of
   the request could have. Keep every word or phrase a condition needs (a quoted phrase, a topic, a file extension,
   a name the condition checks) and change the rest, so the three read like three different real records.
   The current value is given. Keep each variant about as long as the current value.

Answer with JSON: {"items": [{"id", "plural_worthy", "reason", "plural_request", "search_words", "variants"}]},
one entry per item, in the same order.

Items:
[
 {
  "id": "LIN-21",
  "record": "a Linear issue",
  "request": "Assign to Priya Nair the Web team issue about the login redirect that Omar Haddad created on September 10.",
  "text_field": "title",
  "current_value": "Login redirect loops after SSO"
 },
 {
  "id": "LIN-22",
  "record": "a Linear document",
  "request": "Rename the doc Leo Park last edited in the Checkout Redesign project to \"Checkout QA plan\".",
  "text_field": "title",
  "current_value": "Checkout test notes"
 },
 {
  "id": "LIN-23",
  "record": "a Linear comment",
  "request": "Reopen the comment thread on WEB-5 that Maya Chen resolved.",
  "text_field": "body",
  "current_value": "The retry wrapper hides the real failure."
 },
 {
  "id": "LIN-26",
  "record": "a Linear issue",
  "request": "Set the priority to Low on the Web team issue that Dana Whitfield is subscribed to.",
  "text_field": "title",
  "current_value": "Search results jump on scroll"
 },
 {
  "id": "AR-LIN-21",
  "record": "a Linear issue",
  "request": "Set the priority to Urgent on the Web team's issue about the login timeout that Maya Chen created on June 3rd.",
  "text_field": "title",
  "current_value": "Login timeout on SSO redirect"
 },
 {
  "id": "AR-LIN-22",
  "record": "a Linear document",
  "request": "Update the title of the roadmap document in the Mobile Redesign project that Leo Park last edited to \"Mobile Redesign Roadmap v2\".",
  "text_field": "title",
  "current_value": "Mobile Redesign Roadmap"
 },
 {
  "id": "AR-LIN-23",
  "record": "a Linear comment",
  "request": "Reopen the comment thread on WEB-7 about payment retries timing out that Sam Rivera resolved.",
  "text_field": "body",
  "current_value": "The payment retry logic times out under load and needs a backoff."
 },
 {
  "id": "AR-LIN-24",
  "record": "a Linear issue",
  "request": "Set the priority to Urgent on the issue about checkout hangs for guest users on Safari that's assigned to Priya Nair in the Web Platform team's Cycle 4.",
  "text_field": "title",
  "current_value": "Checkout hangs for guest users on Safari"
 },
 {
  "id": "AR-LIN-25",
  "record": "a Linear issue",
  "request": "In the Support team, set priority to Urgent for the issue assigned to Priya Nair that's tagged Customer Tier.",
  "text_field": "title",
  "current_value": "Renewal terms dispute for Meridian Logistics"
 },
 {
  "id": "AR-LIN-26",
  "record": "a Linear issue",
  "request": "In the Web team, set the priority to Urgent for the Design system audit issue that Sam Rivera is subscribed to.",
  "text_field": "title",
  "current_value": "Design system audit"
 },
 {
  "id": "AP-LIN-01",
  "record": "a Linear issue",
  "request": "Set the priority to Urgent for the issue in the Web team's Done state that's assigned to Priya Nair, whose description mentions the rollback window, and that was completed on October 2, 2026.",
  "text_field": "title",
  "current_value": "Payment migration incident follow-up"
 },
 {
  "id": "AP-LIN-02",
  "record": "a Linear issue",
  "request": "Bump the priority of the security review ticket assigned to Priya Chen, our guest reviewer from vendorworks.example, to Urgent.",
  "text_field": "title",
  "current_value": "Security review: Payments API"
 },
 {
  "id": "AP-LIN-04",
  "record": "a Linear cycle",
  "request": "Move the end date to October 20 for the cycle named Cycle 14 that starts September 29 and includes an Urgent issue assigned to Priya Nair.",
  "text_field": "name",
  "current_value": "Cycle 14"
 },
 {
  "id": "AP-LIN-05",
  "record": "a Linear issue",
  "request": "Set the priority to Urgent on the issue with a resolved comment from Priya Nair about the payment gateway timeout, posted on March 3.",
  "text_field": "title",
  "current_value": "Checkout error handling cleanup"
 },
 {
  "id": "AP-LIN-06",
  "record": "a Linear attachment",
  "request": "On issue WEB-14, rename the attachment titled 'Deploy runbook' that links to https://runbooks.northwind.example/deploy-staging to 'Deploy runbook (v2)'.",
  "text_field": "title",
  "current_value": "Deploy runbook"
 },
 {
  "id": "AP-LIN-07",
  "record": "a Linear document",
  "request": "Rename the Growth team's document titled \"Draft notes\" that mentions the referral program pilot to \"Referral pilot \u2014 launch notes\".",
  "text_field": "title",
  "current_value": "Draft notes"
 },
 {
  "id": "AP2-LIN-01",
  "record": "a Linear issue",
  "request": "Set the priority to Urgent on the Web team's issue in the Website Redesign project that's marked Done, was completed on August 14, and whose description mentions the pagination fix.",
  "text_field": "title",
  "current_value": "Fix checkout regression"
 },
 {
  "id": "AP2-LIN-02",
  "record": "a Linear issue",
  "request": "Set to Urgent priority the 'Renew SSO certificate' issue that's assigned to our guest contractor Dana Whitfield and was filed by leo.park@northwind.example.",
  "text_field": "title",
  "current_value": "Renew SSO certificate"
 },
 {
  "id": "AP2-LIN-03",
  "record": "a Linear team",
  "request": "Rename the private team whose key starts with GR and whose description mentions the Q3 OKR pilot rollout to 'Growth Pod'.",
  "text_field": "name",
  "current_value": "Growth"
 },
 {
  "id": "AP2-LIN-04",
  "record": "a Linear cycle",
  "request": "The Fall Kickoff cycle that starts September 29 and includes the checkout timeout issue assigned to Sam Rivera needs its end date pushed to October 20.",
  "text_field": "name",
  "current_value": "Fall Kickoff"
 },
 {
  "id": "AP2-LIN-05",
  "record": "a Linear issue",
  "request": "Set the priority to Urgent on the issue where Priya commented about the API timeout, in a comment thread posted on September 22 that Leo has already resolved.",
  "text_field": "title",
  "current_value": "Improve payment retry queue"
 },
 {
  "id": "AP2-LIN-06",
  "record": "a Linear attachment",
  "request": "Rename the attachment titled \"Marketing brief\" on ENG-14 that links to Dropbox to \"Marketing brief (archived)\".",
  "text_field": "title",
  "current_value": "Marketing brief"
 },
 {
  "id": "G4-LIN-01",
  "record": "a Linear project",
  "request": "Set the description of the high-priority at-risk project with the Meridian milestone due December 2, 2026 to 'Pivoting to usage-based pricing'.",
  "text_field": "name",
  "current_value": "Atlas"
 },
 {
  "id": "G4-LIN-02",
  "record": "a Linear issue",
  "request": "Set the estimate to 5 on the overdue high-priority issue assigned to Maya Chen on the Web team.",
  "text_field": "title",
  "current_value": "Fix checkout redirect loop"
 },
 {
  "id": "G4-LIN-04",
  "record": "a Linear issue",
  "request": "Set the estimate to 5 on the \"Checkout crash on Safari\" issue with the \"Crash log\" link from PagerDuty uploaded by Maya Chen.",
  "text_field": "title",
  "current_value": "Checkout crash on Safari"
 },
 {
  "id": "G4-LIN-05",
  "record": "a Linear issue",
  "request": "Set the estimate to 3 on the issue assigned to Maya Chen in the Web team's cycle ending October 12.",
  "text_field": "title",
  "current_value": "Checkout hangs on promo code apply"
 },
 {
  "id": "G4-LIN-06",
  "record": "a Linear issue",
  "request": "Set the estimate to 3 for the Todo issue assigned to Maya Chen in the Web team with the Bug label from the Web team.",
  "text_field": "title",
  "current_value": "Checkout button unresponsive on Safari"
 },
 {
  "id": "G4-LIN-07",
  "record": "a Linear issue",
  "request": "Set the priority to High on the issue assigned to Maya Chen in the Atlas project in Web's Cycle 4.",
  "text_field": "title",
  "current_value": "Fix checkout timeout on Safari"
 },
 {
  "id": "G4-LIN-08",
  "record": "a Linear issue",
  "request": "Set the priority of the 3-point sub-issue of MOB-42 due on October 15 to High.",
  "text_field": "title",
  "current_value": "Fix Apple Pay sheet layout"
 }
]
