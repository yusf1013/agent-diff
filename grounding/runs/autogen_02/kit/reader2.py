"""The cold reader in expected-set mode, for the underspecified variants (plan, Phase 2).

The reader reads the variant's request cold (turn 1: the request alone) and then every seeded record (turn 2),
judging each candidate against **its own** conditions from turn 1. It is not told which records are meant to fit.
Code then compares the records it finds fitting with the intended set (the target and the freed near misses, or the
target and its clone). A second match is the point of these tests, so it is not a finding; a different match set is.

Turn 2 also asks whether the request asks for a single record.
"""
from __future__ import annotations

from pathlib import Path

from grounding.runs.autogen_01.kit import agent
from grounding.runs.autogen_01.kit.reader import CONTEXT, KIT as A1_KIT, SERVICE, TURN1, TURN2, candidates, render_seed

TURN2X = {
    "type": "object",
    "properties": {**TURN2["properties"],
                   "asks_for_one": {"type": "boolean"},
                   "asks_for_one_note": {"type": "string"}},
    "required": TURN2["required"] + ["asks_for_one", "asks_for_one_note"],
}


def read(case: dict, workspace: Path, log_dir: Path, calls_log: Path, label: str) -> dict:
    system = (A1_KIT / "prompts" / "reader.md").read_text()
    domain = case["domain"]
    first = agent.run(agent.Call(
        role="reader", workspace=workspace, log_dir=log_dir, calls_log=calls_log, tools=[], schema=TURN1,
        system_append=system, label=label,
        prompt=f"A user of {SERVICE[domain]} gave an assistant this request:\n\n> {case['prompt']}\n\n"
               f"{CONTEXT[domain]}\n\nStep 1: list the conditions a record must meet for this request to refer "
               "to it, and every phrase that could reasonably be read in more than one way."))
    own = (agent.structured(first) or {}).get("conditions", [])
    table, ids = candidates(case)
    conds = ("Use your own conditions from step 1 as the author's conditions, with these ids:\n" +
             "\n".join(f"- r{i + 1}: {c}" for i, c in enumerate(own)))
    prompt = (f"Step 2. These are all the records in the service:\n\n{render_seed(case)}\n\n{conds}\n\n"
              f"The candidate records are the rows of `{table}`: {', '.join(ids)}.\n"
              "For every candidate, give the ids of the conditions it fails under the careful reading (an empty list "
              "if it meets all of them), whether a careful colleague could still argue that it meets the request "
              "(contestable), and a short note. Then say whether the conditions faithfully capture the request as "
              "you read it in step 1 (and what differs). For each ambiguity you listed, say whether a careful reader "
              "would genuinely be unsure which reading was meant, and whether the readings select different "
              "candidates. Say whether the request reads like something a real user would write, without hints "
              "that only a test would contain. Finally, say whether the request refers to one specific record, as "
              "\"the ...\" does (asks_for_one: true), as opposed to allowing any record of a kind (\"a ...\") or "
              "asking for several (asks_for_one: false), and why.")
    second = agent.run(agent.Call(
        role="reader", workspace=workspace, log_dir=log_dir, calls_log=calls_log, tools=[], schema=TURN2X,
        system_append=system, label=label, resume=first["session_id"], prompt=prompt))
    answer2 = agent.structured(second) or {}
    missing = [i for i in ids if i not in {str(r.get("id")) for r in answer2.get("records", [])}]
    if missing:
        third = agent.run(agent.Call(
            role="reader", workspace=workspace, log_dir=log_dir, calls_log=calls_log, tools=[], schema=TURN2X,
            system_append=system, label=label, resume=first["session_id"],
            prompt=f"You did not assess these candidates: {', '.join(missing)}. Give your complete answer again, "
                   "covering every candidate."))
        answer2 = agent.structured(third) or answer2
    return {"turn1": agent.structured(first) or {}, "turn2": answer2, "session_id": first.get("session_id")}


def contestable(case: dict, verdict: dict, intended) -> dict:
    """Records outside the intended set that the reader says a careful colleague could argue fit: id -> note. They are
    recorded, not findings: a near miss kept from the scenario is contestable or not whatever the rewording."""
    intended = {str(x) for x in intended}
    return {str(r.get("id")): r.get("note", "") for r in verdict.get("turn2", {}).get("records", [])
            if r.get("contestable") and str(r.get("id")) not in intended and r.get("fails")}


def problems(case: dict, verdict: dict, intended, wording: bool = True) -> list[str]:
    """Findings of the expected-set check: the reader's matches must be exactly `intended`, no phrase may be genuinely
    ambiguous in a way that changes the matches, and the request must be natural and ask for one record.

    `wording=False` (the clone, whose request is the scenario's own, unchanged) keeps only the match-set findings;
    `wording_notes` gives the others, which are then recorded, not findings."""
    out = _match_findings(case, verdict, intended)
    return out + wording_notes(verdict) if wording else out


def wording_notes(verdict: dict) -> list[str]:
    t2 = verdict.get("turn2", {})
    out = []
    for a in t2.get("ambiguity_effects", []):
        if a.get("changes_matches") and a.get("careful_reader_unsure"):
            out.append(f"The reader finds the phrase \"{a.get('phrase')}\" genuinely ambiguous, in a way that changes "
                       f"which records fit: {a.get('explain')}")
    if t2.get("natural") is False:
        out.append(f"The reader finds the request unnatural: {t2.get('naturalness_note')}")
    if t2.get("asks_for_one") is False:
        out.append(f"The reader says the request does not ask for a single record: {t2.get('asks_for_one_note')}")
    return out


def _match_findings(case: dict, verdict: dict, intended) -> list[str]:
    t2 = verdict.get("turn2", {})
    by_id = {str(r.get("id")): r for r in t2.get("records", [])}
    _, ids = candidates(case)
    intended = {str(x) for x in intended}
    out = []
    missing = [i for i in ids if i not in by_id]
    if missing:
        out.append(f"The reader did not assess {missing}.")
    fits = {i for i in ids if i in by_id and not by_id[i].get("fails")}
    for i in sorted(intended - fits):
        if i in by_id:
            out.append(f"The reader says the intended match `{i}` does not fit the request: it fails "
                       f"{by_id[i].get('fails')} ({by_id[i].get('note', '')}).")
    for i in sorted(fits - intended):
        out.append(f"The reader says `{i}` fits the request, but it is not meant to ({by_id[i].get('note', '')}).")
    return out
