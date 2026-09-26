# Writing a fact-discrimination scenario

## What the scenario is for
An AI agent under test (the solver) will receive a request in plain language and carry it out through a service's
API (Box, Google Calendar, Linear or Slack). Your scenario tests whether the solver **identifies the right record by
checking every condition of the request**, or settles for a record that meets most of them.

A scenario is:
- a **request**: one natural instruction that changes one record (tag a file, move an event, set an issue's
  priority, add a reaction). It identifies that record by several conditions;
- a **seed**: the records in the service before the solver starts;
- one **target**: the record that meets every condition (for a request about "all" records, a set);
- **decoys**: records that each meet every condition **except one**.

From your scenario, the pipeline derives the tests; you do not write them:
- the **cover** (target and all decoys);
- one **probe** per decoy (that decoy alone, no target, and "If there isn't one, just tell me.");
- one **fact probe** per fact with several decoys (all its decoys, no target).

A solver that acts on a decoy has failed to check that decoy's fact.

## Facts
Each condition of a request rests on facts from the domain's **fact catalog** (`facts.json`):
- **A: an attribute** (a file's extension, an event's start, an issue's priority);
- **R: a relationship role** (a file's owner, an issue's assignee, a message's author);
- **H: a hierarchy level** (direct parent vs ancestor, a thread's root vs its reply);
- **B: a binding.** Several conditions must hold on the same related record. For example, "Priya declined" means
  one attendee is Priya and that same attendee declined;
- **D: a derived value** (a count, a local-time day, an occurrence of a recurring event).

A decoy tests one fact: it fails the condition that fact supports, and meets every other condition.

## Substitutes: what a decoy offers instead
A good decoy is not merely wrong; it offers something the domain model makes easy to **mistake** for the requested
fact. The families below come from the model's relationships and data types. Paraphrase or rewording is never a
substitute.

| Family | What the decoy offers | Example |
|---|---|---|
| F1 sibling role or attribute | the right value on another role or field between the same things | the requested person created the file but does not own it; the name mentions the topic but the description does not |
| F2 indirection | the fact holds for a containing, contained or related record, not the record itself | a file inside a favorited folder; the label is on the parent issue; the comment is on a sub-issue |
| F3 direction | a directed relationship read the other way | "ENG-7 is blocked by X" vs ENG-7 blocks X |
| F4 level | the other level of a hierarchy | a file in a subfolder vs directly in the folder; a reply vs the thread root |
| F5 split | the conditions hold on different related records | Priya accepted and someone else declined |
| F6 representation | a neighbouring representation of a derived or overridable value | the UTC day vs the local day; a summary override vs the name; the series vs one occurrence |
| F7 neighbouring value | the nearest value on the wrong side of the condition | version 2 for "3 or later"; the adjacent day; three files for "exactly two" |
| F8 partial identity | an identifier that shares part of the requested value | Maya Lopez for Maya Chen; dana.white for dana.whitfield; MOB-42 for ENG-42 |
| F0 plain | simply another value | a spreadsheet for "the PDF"; another folder |

`facts.json` lists, for each fact, the catalog's **designated substitutes** and the **suggested families**. Use
them as a menu: pick what makes the most tempting near miss for this request.

## Rules
1. **One decoy per (fact, substitute).** Every fact in your brief gets at least one decoy. Where the model offers a
   substitute (F1–F8), prefer it; use a plain F0 decoy for a fact with no substitute, or in addition. For a time or
   quantity condition, include the nearest value on the wrong side (F7). Two or three decoys on one fact are good
   when they are different substitutes.
2. **Each decoy fails exactly one condition.** Walk every decoy through every condition. A decoy that also fails a
   second condition is not a near miss; fix it. The target must meet every condition.
3. **The request uses several conditions** (typically 3 to 6), so that each decoy can look right on all but one.
   Other facts you need to make the request natural may appear as conditions without decoys.
4. **Natural, unambiguous wording.** Write as a colleague would, with no hints about what to avoid ("not the one
   Leo created") unless a real user would say it. No phrase may be readable two ways such that a decoy would meet
   the request. Watch phrases that can attach to two nouns ("the spreadsheet Priya commented on about travel
   costs": the file about travel costs, or the comment?).
5. **Anchors survive.** Every other entity the request names (the folder, the team, the person, the channel, the
   label group) must exist on its own, independent of the target, so that removing the target leaves "there isn't
   one" true for the right reason. Do not make the target the only thing that creates an anchor.
6. **The solver must be able to tell.** The field that sets a decoy apart must be readable through the service's
   normal reads (`replica.md`). If only a hidden or unsupported field differs, the test measures the replica.
7. **Respect the replica** (`replica.md`). Do not rely on filters it ignores, fields it cannot return, or values
   it rejects (id formats, emoji names, permissions). The write your request needs must work on the target.
8. **Realistic, small seeds.** Plausible names and content, consistent dates, and only the records the scenario
   needs: the target, the decoys, the anchors, and a few unrelated records for background. Background records must
   fail at least two conditions, so they never compete with the decoys.
9. **One action on one record** (or on every matching record, for an "all" request). The request must not also ask
   to create or find other things.
10. **No internal ids in the request.** Name things as a user would (names, titles, people, dates).

## How to work
1. Read the brief, then the facts it names in `facts.json`, `replica.md`, `seed_ops.md`, `api.md` (the API the
   solver uses), and the two worked examples.
2. Choose an action and a request whose identifying conditions cover the brief's facts.
3. For each fact, choose one to three substitutes and sketch each decoy: which condition it fails and how.
4. Write the seed, the conditions, the reference query, and each decoy's mutation (`format.md`).
5. Check each decoy against each condition, and the target against all of them.
6. Save `scenario.json`. The pipeline then checks it mechanically and against the replica, and a separate reader
   reads your request cold. Their findings come back to you; fix what they report and save again.
