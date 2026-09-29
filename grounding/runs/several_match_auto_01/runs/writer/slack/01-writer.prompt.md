You write test requests for an AI agent that acts in a workspace on a user's behalf. You are careful with
wording: a test request must read exactly as a real user would write it, and must ask for exactly what is intended.

---

Each item below is a request that asks the agent to act on ONE record in Slack. For each item:

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
3. Write `search_words`: the one to three words a user would type into Slack's search box to look for these
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
  "id": "SLK-21",
  "record": "a Slack message",
  "request": "Add a :thumbsup: reaction to the message Priya Sharma posted in #deploys on September 23 about the rollback.",
  "text_field": "message_text",
  "current_value": "Rollback of payments-api finished; error rates are back to normal."
 },
 {
  "id": "SLK-22",
  "record": "a Slack message",
  "request": "Add an :eyes: reaction to Diego Alvarez's reply in the #incidents thread about the checkout outage.",
  "text_field": "message_text",
  "current_value": "Rolled back the gateway config; watching the error rate."
 },
 {
  "id": "SLK-23",
  "record": "a Slack channel",
  "request": "Set the topic of the private channel whose purpose is coordinating vendor contracts to \"Renewals due Oct 31\".",
  "text_field": "channel_name",
  "current_value": "legal-ops"
 },
 {
  "id": "SLK-24",
  "record": "a Slack channel",
  "request": "Post \"Reminder: expense reports are due Friday\" in the private channel that both Priya Sharma and Leo Park are members of.",
  "text_field": "channel_name",
  "current_value": "finance-leads"
 },
 {
  "id": "AR-SLK-21",
  "record": "a Slack message",
  "request": "React with :eyes: to the message Leo Park posted in #incidents on Tuesday.",
  "text_field": "message_text",
  "current_value": "Rolled back the payment gateway config after the spike."
 },
 {
  "id": "AR-SLK-22",
  "record": "a Slack message",
  "request": "In #launch-prep, add a rocket reaction to Leo Park's reply in the thread about tonight's payments launch checklist.",
  "text_field": "message_text",
  "current_value": "All checklists are in, we're clear to ship."
 },
 {
  "id": "AR-SLK-23",
  "record": "a Slack channel",
  "request": "Archive the private channel whose purpose mentions onboarding new hires and that has Diego Alvarez as a member.",
  "text_field": "channel_name",
  "current_value": "new-hire-onboarding"
 },
 {
  "id": "AR-SLK-24",
  "record": "a Slack message",
  "request": "React with the eyes emoji on the message in #incidents about the payment gateway timeout that was posted by someone who's a member of #payments-oncall.",
  "text_field": "message_text",
  "current_value": "Seeing 504s tied to a payment gateway timeout on checkout after the last deploy."
 },
 {
  "id": "AP-SLK-01",
  "record": "a Slack message",
  "request": "In #launch-planning, add a :tada: reaction to the message from Farhan Malik \u2014 the one who goes by Deebo \u2014 confirming the launch date, the one that @nadia.brooks already flagged with :eyes:.",
  "text_field": "message_text",
  "current_value": "Confirmed: the launch date is set for March 3."
 },
 {
  "id": "AP-SLK-02",
  "record": "a Slack channel",
  "request": "Unarchive the incidents channel about the checkout outage.",
  "text_field": "channel_name",
  "current_value": "incidents-checkout"
 },
 {
  "id": "AP-SLK-03",
  "record": "a Slack message",
  "request": "Add a rocket reaction to the message about the rollout timeline in #eng-updates that Priya reacted to with eyes.",
  "text_field": "message_text",
  "current_value": "Rollout timeline: shipping to prod Friday 3pm."
 },
 {
  "id": "AP-SLK-04",
  "record": "a Slack user",
  "request": "Invite to #incident-response whoever posted the message in #incidents about the deploy freeze that got 4 replies.",
  "text_field": "real_name",
  "current_value": "Diego Alvarez"
 },
 {
  "id": "AP-SLK-05",
  "record": "a Slack channel",
  "request": "Archive the most recently created channel that our workspace owner belongs to and that currently has exactly four members.",
  "text_field": "channel_name",
  "current_value": "launch-ops"
 },
 {
  "id": "AP2-SLK-01",
  "record": "a Slack message",
  "request": "Add an :eyes: reaction to the message in #product-launch where Diego Alvarez said the launch date is confirmed, the one that already has a :thumbsup: from @priya.sharma and a :tada: from Metrics Bot.",
  "text_field": "message_text",
  "current_value": "The launch date is confirmed for October 12."
 },
 {
  "id": "AP2-SLK-02",
  "record": "a Slack channel",
  "request": "Invite Aisha Khan to the channel with 'incident' in its name, whose Topic mentions postmortems, and that hasn't been archived yet.",
  "text_field": "channel_name",
  "current_value": "incident-response"
 },
 {
  "id": "AP2-SLK-03",
  "record": "a Slack message",
  "request": "In #incidents, add a rocket reaction to the payment gateway outage message that Diego Alvarez reacted to with fire.",
  "text_field": "message_text",
  "current_value": "Update: payment gateway outage \u2014 rollback deployed, monitoring error rates now."
 },
 {
  "id": "AP2-SLK-04",
  "record": "a Slack message",
  "request": "Add a check reaction to Diego's message in #incidents that mentions the gateway rollback, the one with 4 replies in its thread.",
  "text_field": "message_text",
  "current_value": "Posted the gateway rollback notes for the postmortem."
 },
 {
  "id": "AP2-SLK-05",
  "record": "a Slack channel",
  "request": "Archive the channel that our workspace owner belongs to, that was created before March 2026, and that only has 5 members.",
  "text_field": "channel_name",
  "current_value": "proj-atlas"
 },
 {
  "id": "G4-SLK-01",
  "record": "a Slack message",
  "request": "Add the eyes reaction to the message from ana.torre@northwind.example in #releases that says 'Release cut is ready' and that a bot reacted to with tada.",
  "text_field": "message_text",
  "current_value": "Release cut is ready"
 },
 {
  "id": "G4-SLK-02",
  "record": "a Slack message",
  "request": "Add an eyes reaction to the release checklist message that Maya Chen posted in #launch-plan and that Diego Alvarez reacted to with thumbsup.",
  "text_field": "message_text",
  "current_value": "The release checklist is final, all items signed off for Thursday's deploy."
 },
 {
  "id": "G4-SLK-03",
  "record": "a Slack message",
  "request": "Add the eyes reaction to the latest message from Diego Alvarez in #deployments about the gateway rollback, posted at 12:40.",
  "text_field": "message_text",
  "current_value": "Gateway rollback complete, traffic is recovering."
 },
 {
  "id": "G4-SLK-04",
  "record": "a Slack message",
  "request": "Add an eyes reaction to Maya Chen's launch checklist card in #launch-readiness that lists the rollback steps.",
  "text_field": "message_text",
  "current_value": "Launch readiness \u2014 card below with the final sequence."
 },
 {
  "id": "G4-SLK-05",
  "record": "a Slack message",
  "request": "Add the eyes reaction to Maya Chen's message about the deploy checklist in my direct message with Maya Chen.",
  "text_field": "message_text",
  "current_value": "Deploy checklist for Friday is ready: env, flags, rollback plan."
 },
 {
  "id": "G4-SLK-06",
  "record": "a Slack message",
  "request": "Add a thumbsup reaction to Diego Alvarez's message about the gateway rollback in #deployments that already has exactly 3 eyes reactions.",
  "text_field": "message_text",
  "current_value": "Gateway rollback is done, error rate is back to normal."
 },
 {
  "id": "G4-SLK-07",
  "record": "a Slack channel",
  "request": "Set the topic of the private channel with Diego Alvarez's message about the gateway rollback to Post-release monitoring.",
  "text_field": "channel_name",
  "current_value": "release-ops"
 },
 {
  "id": "G4-SLK-08",
  "record": "a Slack message",
  "request": "Add the eyes reaction to my message that says 'Q3 launch checklist is ready for review' in my one-to-one DM with Maya Chen.",
  "text_field": "message_text",
  "current_value": "Q3 launch checklist is ready for review"
 }
]
