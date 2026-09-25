# Test-suite method, version 1 (written before any v1 suite was generated or run)

Goal: from a domain model, build a suite that exposes as many distinct fact failures as possible per test case.
Budget is the number of distinct test cases. Trials per test are fixed metadata (3 here) that measure how often a
failure occurs; they are not budget. Tokens are recorded as telemetry.

## Inputs

1. **The domain model** and its **fact catalog** (`../fact_coverage_01/catalog/`): one requirement per fact
   (attribute, relationship role, hierarchy level, binding, derived representation). The catalog is open to extension.
2. **Scenarios**, hand-authored: a natural request whose identifying path uses several facts, a seed with one target,
   and one **decoy per (fact, substitute)**. A decoy satisfies every condition of the request except its fact, and
   every decoy claim is checked mechanically ([fdc.py](../fact_coverage_01/fdc.py)).

## Substitutes: how decoys are designed

A substitute is something in the domain model an agent could take for the requested fact. The families below are
derived from the model; the list is open to extension, but paraphrase or rewording of the request is never a
substitute.

| Family | Model basis | Example |
|---|---|---|
| F1 sibling role | the same value on another role between the same entities | created vs organized; owner vs creator; assigner vs task creator |
| F2 indirection | the fact holds for a containing, contained or related record, not the record itself | file inside a favorited folder; label on the parent issue; comment on a sub-issue |
| F3 direction | a directed relationship read in reverse | "ENG-7 is blocked by X" vs ENG-7 blocks X |
| F4 level | the other level of a hierarchy | nested vs direct folder; sub-team vs team; reply vs thread root |
| F5 split | the conditions hold on different related records | Priya's comment and a travel comment on the same file, by different people |
| F6 representation | the neighbouring representation of a derived or overridable value | UTC date vs local day; summary override vs name; series vs occurrence |
| F7 neighbouring value | by data type: the nearest value on the wrong side of the condition | version 2 for "3 or later"; the adjacent day; an all-day event ending on the date; one assignee for "two or more" |
| F8 partial identity | an identifier that shares part of the requested value | Maya Lopez for Maya Chen; dana.white for dana.whitfield; MOB-42 for ENG-42 |
| F0 plain | the decoy simply fails the fact | a spreadsheet for "the PDF"; another tag; another folder |

## Test forms

1. **Probe** (the unit test of one fact): the request plus "If there isn't one, just tell me." (plural: "If there
   aren't any…"); the seed with the target and all decoys removed except one. Correct behaviour: report that there is
   no match and change nothing. A failure is acting on the decoy, or presenting it as the match.
2. **Packed plain test**: for a scenario's F0 decoys only, one no-target "just tell me" test that keeps all of them.
   This is the economical alternative to one probe per plain fact; v1 runs both so the two can be compared.
3. **Target-present layer**: only for requests whose answer is a set (all matching records), the scenario as written,
   with its targets and decoys. A set answer can fail by including decoys next to real targets.
4. **Policy panel**, three tests per domain, measuring resolution behaviour once:
   - P1: the scenario with its target removed and the presupposing wording;
   - P2: one plain decoy, no target, presupposing wording;
   - P3: two records that both fully match a singular request (underspecified).

## Suite for a scenario

- one probe per decoy of families F1–F8;
- one probe per F0 decoy **and** (for comparison in v1) one packed plain test of the scenario's F0 decoys;
- the target-present test if the answer is a set;
- when a time or quantity fact's decoy is not a nearest value, add an F7 decoy that is.

The policy panel is per domain, not per scenario.

## Scoring

- A test **exposes** a failure if at least one of its 3 trials acts on a wrong record or presents one as the answer,
  confirmed by reading the trajectory, answer and state diff. The failure frequency (1/3, 2/3, 3/3) is reported with it.
- A failure is attributed to the fact whose decoy was acted on; distinct bugs are distinct facts. The mechanism (the
  substitute used, or a condition dropped) is recorded from the trajectory.
- Policy-panel failures count separately, as policy bugs.
- Mock artifacts (a replica limitation, an unobservable decoy) invalidate a test; they are not bugs.

## Reported numbers

Per suite: distinct test cases (probes, packed tests, layer tests, panel tests), distinct fact bugs, failure
frequencies, requests and tokens. The comparison baselines on the pilot's facts are B1 (the 31 cover cases, rerun
at 3 trials) and B2 (the pilot's 125 fact-sensitive cases, 16 bugs).
