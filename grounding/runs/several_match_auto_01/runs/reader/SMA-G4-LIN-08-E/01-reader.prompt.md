You check test cases for an AI assistant that acts in a workspace on a user's behalf. You read carefully
and literally, the way the user who wrote the request would mean it.

---

A user sent the assistant this request in their Linear workspace:

    "Set the priority of all the 3-point sub-issues of MOB-42 due on October 15 to High."

The user is Jordan Lee. Below is every Linear issue in the workspace, with what the assistant can see about it. Which of
them does the user's request ask the assistant to act on?

List the id of every record the request covers, and only those. Read each condition of the request as the user
would mean it. If you cannot tell whether the user means a record, list it under `unsure` with the reason (and do
not list it in `ids`). Answer with JSON: {"ids": [...], "unsure": [{"id", "why"}], "notes": "..."}.

Records:
[
 {
  "id": "i-mob-42",
  "identifier": "MOB-42",
  "title": "Checkout crash on launch",
  "teamId": "t-mob",
  "stateId": "t-mob-st-1",
  "creatorId": "u-actor (Jordan Lee)",
  "priority": 0.0,
  "priorityLabel": "No priority",
  "number": 42.0,
  "createdAt": "2026-06-01T09:00:00",
  "updatedAt": "2026-06-01T09:00:00",
  "team": "Mobile",
  "state": "Todo",
  "issues": []
 },
 {
  "id": "i-mob-421",
  "identifier": "MOB-421",
  "title": "Checkout crash, enterprise follow-up",
  "teamId": "t-mob",
  "stateId": "t-mob-st-1",
  "creatorId": "u-actor (Jordan Lee)",
  "priority": 0.0,
  "priorityLabel": "No priority",
  "number": 421.0,
  "createdAt": "2026-06-01T09:00:00",
  "updatedAt": "2026-06-01T09:00:00",
  "team": "Mobile",
  "state": "Todo",
  "issues": []
 },
 {
  "id": "i-mob-7",
  "identifier": "MOB-7",
  "title": "Push notification settings",
  "teamId": "t-mob",
  "stateId": "t-mob-st-1",
  "creatorId": "u-actor (Jordan Lee)",
  "priority": 0.0,
  "priorityLabel": "No priority",
  "number": 7.0,
  "createdAt": "2026-06-01T09:00:00",
  "updatedAt": "2026-06-01T09:00:00",
  "team": "Mobile",
  "state": "Todo",
  "issues": []
 },
 {
  "id": "i-mob-50",
  "identifier": "MOB-50",
  "title": "Fix Apple Pay sheet layout",
  "teamId": "t-mob",
  "stateId": "t-mob-st-1",
  "creatorId": "u-actor (Jordan Lee)",
  "priority": 4.0,
  "priorityLabel": "Low",
  "number": 50.0,
  "createdAt": "2026-06-01T09:00:00",
  "updatedAt": "2026-06-01T09:00:00",
  "estimate": 3,
  "dueDate": "2026-10-15",
  "parentId": "i-mob-42",
  "team": "Mobile",
  "state": "Todo",
  "issues": [
   {
    "id": "i-mob-42",
    "identifier": "MOB-42",
    "title": "Checkout crash on launch",
    "teamId": "t-mob",
    "stateId": "t-mob-st-1",
    "creatorId": "u-actor",
    "priority": 0.0,
    "priorityLabel": "No priority",
    "number": 42.0,
    "createdAt": "2026-06-01T09:00:00",
    "updatedAt": "2026-06-01T09:00:00"
   }
  ]
 },
 {
  "id": "i-mob-51",
  "identifier": "MOB-51",
  "title": "Fix Apple Pay sheet copy",
  "teamId": "t-mob",
  "stateId": "t-mob-st-1",
  "creatorId": "u-actor (Jordan Lee)",
  "priority": 4.0,
  "priorityLabel": "Low",
  "number": 51.0,
  "createdAt": "2026-06-01T09:00:00",
  "updatedAt": "2026-06-01T09:00:00",
  "estimate": 2,
  "dueDate": "2026-10-15",
  "parentId": "i-mob-42",
  "team": "Mobile",
  "state": "Todo",
  "issues": [
   {
    "id": "i-mob-42",
    "identifier": "MOB-42",
    "title": "Checkout crash on launch",
    "teamId": "t-mob",
    "stateId": "t-mob-st-1",
    "creatorId": "u-actor",
    "priority": 0.0,
    "priorityLabel": "No priority",
    "number": 42.0,
    "createdAt": "2026-06-01T09:00:00",
    "updatedAt": "2026-06-01T09:00:00"
   }
  ]
 },
 {
  "id": "i-mob-52",
  "identifier": "MOB-52",
  "title": "Fix Apple Pay sheet analytics",
  "teamId": "t-mob",
  "stateId": "t-mob-st-1",
  "creatorId": "u-actor (Jordan Lee)",
  "priority": 3.0,
  "priorityLabel": "Medium",
  "number": 52.0,
  "createdAt": "2026-06-01T09:00:00",
  "updatedAt": "2026-06-01T09:00:00",
  "estimate": 5,
  "dueDate": "2026-10-15",
  "parentId": "i-mob-42",
  "team": "Mobile",
  "state": "Todo",
  "issues": [
   {
    "id": "i-mob-42",
    "identifier": "MOB-42",
    "title": "Checkout crash on launch",
    "teamId": "t-mob",
    "stateId": "t-mob-st-1",
    "creatorId": "u-actor",
    "priority": 0.0,
    "priorityLabel": "No priority",
    "number": 42.0,
    "createdAt": "2026-06-01T09:00:00",
    "updatedAt": "2026-06-01T09:00:00"
   }
  ]
 },
 {
  "id": "i-mob-53",
  "identifier": "MOB-53",
  "title": "Fix Apple Pay sheet dark mode",
  "teamId": "t-mob",
  "stateId": "t-mob-st-1",
  "creatorId": "u-actor (Jordan Lee)",
  "priority": 4.0,
  "priorityLabel": "Low",
  "number": 53.0,
  "createdAt": "2026-06-01T09:00:00",
  "updatedAt": "2026-06-01T09:00:00",
  "estimate": 3,
  "dueDate": "2026-10-16",
  "parentId": "i-mob-42",
  "team": "Mobile",
  "state": "Todo",
  "issues": [
   {
    "id": "i-mob-42",
    "identifier": "MOB-42",
    "title": "Checkout crash on launch",
    "teamId": "t-mob",
    "stateId": "t-mob-st-1",
    "creatorId": "u-actor",
    "priority": 0.0,
    "priorityLabel": "No priority",
    "number": 42.0,
    "createdAt": "2026-06-01T09:00:00",
    "updatedAt": "2026-06-01T09:00:00"
   }
  ]
 },
 {
  "id": "i-mob-54",
  "identifier": "MOB-54",
  "title": "Fix Apple Pay sheet voiceover",
  "teamId": "t-mob",
  "stateId": "t-mob-st-1",
  "creatorId": "u-actor (Jordan Lee)",
  "priority": 4.0,
  "priorityLabel": "Low",
  "number": 54.0,
  "createdAt": "2026-10-15T09:00:00",
  "updatedAt": "2026-10-15T09:00:00",
  "estimate": 3,
  "dueDate": "2026-10-22",
  "parentId": "i-mob-42",
  "team": "Mobile",
  "state": "Todo",
  "issues": [
   {
    "id": "i-mob-42",
    "identifier": "MOB-42",
    "title": "Checkout crash on launch",
    "teamId": "t-mob",
    "stateId": "t-mob-st-1",
    "creatorId": "u-actor",
    "priority": 0.0,
    "priorityLabel": "No priority",
    "number": 42.0,
    "createdAt": "2026-06-01T09:00:00",
    "updatedAt": "2026-06-01T09:00:00"
   }
  ]
 },
 {
  "id": "i-mob-55",
  "identifier": "MOB-55",
  "title": "Fix Apple Pay sheet layout follow-up",
  "teamId": "t-mob",
  "stateId": "t-mob-st-1",
  "creatorId": "u-actor (Jordan Lee)",
  "priority": 4.0,
  "priorityLabel": "Low",
  "number": 55.0,
  "createdAt": "2026-06-01T09:00:00",
  "updatedAt": "2026-06-01T09:00:00",
  "estimate": 3,
  "dueDate": "2026-10-15",
  "parentId": "i-mob-421",
  "team": "Mobile",
  "state": "Todo",
  "issues": [
   {
    "id": "i-mob-421",
    "identifier": "MOB-421",
    "title": "Checkout crash, enterprise follow-up",
    "teamId": "t-mob",
    "stateId": "t-mob-st-1",
    "creatorId": "u-actor",
    "priority": 0.0,
    "priorityLabel": "No priority",
    "number": 421.0,
    "createdAt": "2026-06-01T09:00:00",
    "updatedAt": "2026-06-01T09:00:00"
   }
  ]
 },
 {
  "id": "i-mob-56",
  "identifier": "MOB-56",
  "title": "MOB-42 follow-up: Apple Pay sheet",
  "teamId": "t-mob",
  "stateId": "t-mob-st-1",
  "creatorId": "u-actor (Jordan Lee)",
  "priority": 4.0,
  "priorityLabel": "Low",
  "number": 56.0,
  "createdAt": "2026-06-01T09:00:00",
  "updatedAt": "2026-06-01T09:00:00",
  "estimate": 3,
  "dueDate": "2026-10-15",
  "parentId": "i-mob-7",
  "team": "Mobile",
  "state": "Todo",
  "issues": [
   {
    "id": "i-mob-7",
    "identifier": "MOB-7",
    "title": "Push notification settings",
    "teamId": "t-mob",
    "stateId": "t-mob-st-1",
    "creatorId": "u-actor",
    "priority": 0.0,
    "priorityLabel": "No priority",
    "number": 7.0,
    "createdAt": "2026-06-01T09:00:00",
    "updatedAt": "2026-06-01T09:00:00"
   }
  ]
 },
 {
  "id": "i-mob-57",
  "identifier": "MOB-57",
  "title": "Polish saved-card search",
  "teamId": "t-mob",
  "stateId": "t-mob-st-1",
  "creatorId": "u-actor (Jordan Lee)",
  "priority": 4.0,
  "priorityLabel": "Low",
  "number": 57.0,
  "createdAt": "2026-06-01T09:00:00",
  "updatedAt": "2026-06-01T09:00:00",
  "estimate": 5,
  "dueDate": "2026-10-22",
  "parentId": "i-mob-42",
  "team": "Mobile",
  "state": "Todo",
  "issues": [
   {
    "id": "i-mob-42",
    "identifier": "MOB-42",
    "title": "Checkout crash on launch",
    "teamId": "t-mob",
    "stateId": "t-mob-st-1",
    "creatorId": "u-actor",
    "priority": 0.0,
    "priorityLabel": "No priority",
    "number": 42.0,
    "createdAt": "2026-06-01T09:00:00",
    "updatedAt": "2026-06-01T09:00:00"
   }
  ]
 },
 {
  "id": "i-mob-50-sm0-v",
  "identifier": "MOB-422",
  "title": "Fix Google Pay button alignment",
  "teamId": "t-mob",
  "stateId": "t-mob-st-1",
  "creatorId": "u-actor (Jordan Lee)",
  "priority": 4.0,
  "priorityLabel": "Low",
  "number": 422.0,
  "createdAt": "2026-06-01T09:00:00",
  "updatedAt": "2026-06-01T09:00:00",
  "estimate": 3,
  "dueDate": "2026-10-15",
  "parentId": "i-mob-42",
  "team": "Mobile",
  "state": "Todo",
  "issues": [
   {
    "id": "i-mob-42",
    "identifier": "MOB-42",
    "title": "Checkout crash on launch",
    "teamId": "t-mob",
    "stateId": "t-mob-st-1",
    "creatorId": "u-actor",
    "priority": 0.0,
    "priorityLabel": "No priority",
    "number": 42.0,
    "createdAt": "2026-06-01T09:00:00",
    "updatedAt": "2026-06-01T09:00:00"
   }
  ]
 },
 {
  "id": "i-mob-50-sm1-v",
  "identifier": "MOB-423",
  "title": "Fix card expiry input spacing",
  "teamId": "t-mob",
  "stateId": "t-mob-st-1",
  "creatorId": "u-actor (Jordan Lee)",
  "priority": 4.0,
  "priorityLabel": "Low",
  "number": 423.0,
  "createdAt": "2026-06-01T09:00:00",
  "updatedAt": "2026-06-01T09:00:00",
  "estimate": 3,
  "dueDate": "2026-10-15",
  "parentId": "i-mob-42",
  "team": "Mobile",
  "state": "Todo",
  "issues": [
   {
    "id": "i-mob-42",
    "identifier": "MOB-42",
    "title": "Checkout crash on launch",
    "teamId": "t-mob",
    "stateId": "t-mob-st-1",
    "creatorId": "u-actor",
    "priority": 0.0,
    "priorityLabel": "No priority",
    "number": 42.0,
    "createdAt": "2026-06-01T09:00:00",
    "updatedAt": "2026-06-01T09:00:00"
   }
  ]
 }
]
