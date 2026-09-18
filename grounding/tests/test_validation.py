"""Relational construction checks, including plausible-but-wrong bindings."""

from copy import deepcopy
import unittest

from grounding.generation.selection import (
    SelectorError, canonical_handle, evaluate_selector, handle_key, validate_seed,
)
from grounding.generation.validate import validate_case


def seed_fixture():
    return {
        "teams": [{"team_id": "T1", "team_name": "Acme"}],
        "users": [
            {"user_id": user, "username": user.lower(), "email": user.lower() + "@acme.example", "real_name": name}
            for user, name in (("UA", "Casey"), ("U1", "Alex Rivera"), ("U2", "Morgan Park"))
        ],
        "channels": [
            {"channel_id": "CS", "channel_name": "security", "team_id": "T1"},
            {"channel_id": "CO", "channel_name": "operations", "team_id": "T1"},
        ],
        "user_teams": [{"user_id": user, "team_id": "T1", "role": "member"} for user in ("UA", "U1", "U2")],
        "channel_members": [
            {"channel_id": "CS", "user_id": "U1"},
            {"channel_id": "CO", "user_id": "U2"},
            {"channel_id": "CS", "user_id": "UA"},
            {"channel_id": "CO", "user_id": "UA"},
        ],
        "messages": [
            {"message_id": "1712345678.000001", "channel_id": "CO", "user_id": "U2", "message_text": "Rollout checklist ready"},
            {"message_id": "1712345678.000002", "channel_id": "CO", "user_id": "U1", "message_text": "Rollout checklist draft"},
            {"message_id": "1712345678.000003", "channel_id": "CS", "user_id": "U1", "message_text": "Office lunch"},
        ],
        "message_reactions": [
            {"message_id": "1712345678.000001", "user_id": "U1", "reaction_type": "thumbsup"},
            {"message_id": "1712345678.000001", "user_id": "U1", "reaction_type": "eyes"},
            {"message_id": "1712345678.000002", "user_id": "U2", "reaction_type": "thumbsup"},
            {"message_id": "1712345678.000003", "user_id": "U1", "reaction_type": "thumbsup"},
        ],
    }


def selector_fixture():
    return {
        "root_table": "messages", "scope": [],
        "focal": {
            "path": ["messages", "message_reactions", "users", "channel_members", "channels"],
            "joins": ["message_reactions.message_id", "message_reactions.user_id", "channel_members.user_id", "channel_members.channel_id"],
            "filters": [{"node": 4, "field": "channel_name", "op": "eq", "value": "security"}],
        },
        "auxiliary": [{"path": ["messages"], "joins": [], "filters": [
            {"node": 0, "field": "message_text", "op": "contains_ci", "value": "rollout"}
        ]}],
    }


def case_fixture():
    return {
        "case_id": "case_1", "prompt": "React to the rollout message that someone in #security reacted to.",
        "acting_user_id": "UA", "seed": seed_fixture(),
        "cards": [{
            "Test ID": "case_1", "Task type": "state-changing", "Grounding obligations": 1,
            "Grounding obligation name": "Resolve rollout messages reacted to by security members",
            "Grounding obligation description": "Select the rollout message with a security-member reactor.",
            "Resolution": "resolved", "Shared scope": "Seeded channels and messages", "Referent set": ["1712345678.000001"],
            "Alternative sufficient identifying sets": [["channels.channel_name", "messages.message_text"]],
            "Change-computation attributes": [["messages.message_id"]],
            "Written attributes": ["message_reactions.message_id", "message_reactions.user_id", "message_reactions.reaction_type"],
        }],
        "task_spec": [{"line": 1, "text": "React to the specified rollout message.", "obligations": [1]}],
        "private": {
            "selector": selector_fixture(), "focal_obligation": 1, "mode": "single",
            "expected_matches": ["1712345678.000001"], "near_misses": ["1712345678.000002"],
        },
    }


class RelationalSelectionTests(unittest.TestCase):
    def test_same_person_binding_and_auxiliary_negative(self):
        result = evaluate_selector(seed_fixture(), selector_fixture())
        self.assertEqual(result["matches"], ["1712345678.000001"])
        # M2 is authored by a security member, but its reactor isn't one.
        self.assertEqual(result["focal_negatives"], ["1712345678.000002"])
        self.assertEqual(result["focal_matches"], ["1712345678.000001", "1712345678.000003"])
        self.assertEqual(result["population"], ["1712345678.000001", "1712345678.000002", "1712345678.000003"])

    def test_distinct_count_uses_entities_not_join_rows(self):
        selector = selector_fixture()
        selector["focal"]["count"] = {"node": 2, "op": "eq", "value": 1}
        self.assertEqual(evaluate_selector(seed_fixture(), selector)["matches"], ["1712345678.000001"])
        selector["focal"]["count"]["value"] = 2
        self.assertEqual(evaluate_selector(seed_fixture(), selector)["matches"], [])
        selector["focal"]["count"] = {"node": 1, "op": "eq", "value": 2}
        self.assertEqual(evaluate_selector(seed_fixture(), selector)["matches"], ["1712345678.000001"])

    def test_count_zero_and_scoped_root(self):
        selector = selector_fixture()
        selector["focal"]["count"] = {"node": 1, "op": "eq", "value": 0}
        self.assertEqual(evaluate_selector(seed_fixture(), selector)["matches"], ["1712345678.000002"])
        selector["scope"] = [{"field": "message_id", "op": "in", "value": ["1712345678.000001", "1712345678.000003"]}]
        self.assertEqual(evaluate_selector(seed_fixture(), selector)["matches"], [])

    def test_inverse_join_and_composite_handle(self):
        selector = {
            "root_table": "channel_members", "scope": [], "auxiliary": [],
            "focal": {"path": ["channel_members", "users"], "joins": ["channel_members.user_id"], "filters": [{"node": 1, "field": "real_name", "op": "eq", "value": "Alex Rivera"}]},
        }
        self.assertEqual(evaluate_selector(seed_fixture(), selector)["matches"], [{"channel_id": "CS", "user_id": "U1"}])
        handle = canonical_handle("message_reactions", seed_fixture()["message_reactions"][0])
        self.assertEqual(handle_key("message_reactions", handle), handle_key("message_reactions", dict(reversed(list(handle.items())))))
        with self.assertRaises(SelectorError):
            handle_key("channel_members", {"id": "CS:U1"})

    def test_unknown_field_and_wrong_relationship_are_rejected(self):
        selector = selector_fixture()
        selector["focal"]["filters"][0]["field"] = "departed"
        with self.assertRaises(SelectorError):
            evaluate_selector(seed_fixture(), selector)
        selector = selector_fixture()
        selector["focal"]["joins"][0] = "messages.user_id"
        with self.assertRaises(SelectorError):
            evaluate_selector(seed_fixture(), selector)

    def test_literal_defaults_but_not_guessed_creation_times(self):
        selector = {"root_table": "channels", "scope": [], "auxiliary": [], "focal": {"path": ["channels"], "joins": [], "filters": [{"node": 0, "field": "is_archived", "op": "eq", "value": False}]}}
        self.assertEqual(len(evaluate_selector(seed_fixture(), selector)["matches"]), 2)
        selector["focal"]["filters"] = [{"node": 0, "field": "created_at", "op": "gt", "value": "2025-01-01T00:00:00"}]
        with self.assertRaisesRegex(SelectorError, "dynamic database default"):
            evaluate_selector(seed_fixture(), selector)


class ConstructionValidationTests(unittest.TestCase):
    def test_valid_case_and_seed(self):
        self.assertEqual(validate_seed(seed_fixture()), [])
        result = validate_case(case_fixture())
        self.assertEqual(result["errors"], [])
        self.assertEqual(result["computed_matches"], ["1712345678.000001"])

    def test_message_id_api_compatibility_separate_from_schema(self):
        for invalid_id in ("M1", "nan", "inf", "-inf", "1e1000"):
            with self.subTest(message_id=invalid_id):
                case = case_fixture()
                old_id = case["seed"]["messages"][0]["message_id"]
                case["seed"]["messages"][0]["message_id"] = invalid_id
                for reaction in case["seed"]["message_reactions"]:
                    if reaction["message_id"] == old_id:
                        reaction["message_id"] = invalid_id
                self.assertEqual(validate_seed(case["seed"]), [])
                self.assertTrue(any("API compatibility:" in error for error in validate_case(case)["errors"]))

    def test_filler_creates_accidental_match(self):
        case = case_fixture()
        case["seed"]["message_reactions"].append({"message_id": "1712345678.000002", "user_id": "U1", "reaction_type": "eyes"})
        result = validate_case(case)
        self.assertEqual(result["computed_matches"], ["1712345678.000001", "1712345678.000002"])
        self.assertTrue(any("expected_matches differs" in e for e in result["errors"]))
        self.assertTrue(any("outside scoped focal negatives" in e for e in result["errors"]))

    def test_false_negative_fails_auxiliary(self):
        case = case_fixture()
        case["private"]["near_misses"] = ["1712345678.000003"]
        self.assertTrue(any("outside scoped focal negatives" in e for e in validate_case(case)["errors"]))

    def test_enrichment_does_not_require_negative(self):
        case = case_fixture()
        case["private"]["near_misses"] = []
        case["private"]["require_near_miss"] = False
        self.assertEqual(validate_case(case)["errors"], [])
        case["private"].pop("require_near_miss")
        self.assertTrue(any("requires at least one" in e for e in validate_case(case)["errors"]))

    def test_seed_integrity_checks_every_table(self):
        for mutate, needle in (
            (lambda seed: seed["users"].append(deepcopy(seed["users"][0])), "duplicate unique key"),
            (lambda seed: seed["messages"][0].update(user_id="missing"), "does not reference"),
            (lambda seed: seed["channels"][0].update(is_private="false"), "invalid bool"),
            (lambda seed: seed["users"][0].update(departed=True), "unknown field"),
            (lambda seed: seed.update(files=[{"file_id": "F1", "user_id": "missing"}]), "does not reference"),
        ):
            with self.subTest(needle=needle):
                seed = seed_fixture()
                mutate(seed)
                self.assertTrue(any(needle in e for e in validate_seed(seed)))

    def test_candidate_sets_are_not_joint_targets(self):
        case = case_fixture()
        case["seed"]["message_reactions"].append({"message_id": "1712345678.000002", "user_id": "U1", "reaction_type": "eyes"})
        case["private"].update(mode="underspecified", expected_matches=["1712345678.000001", "1712345678.000002"], candidate_sets=[["1712345678.000001"], ["1712345678.000002"]], near_misses=[], require_near_miss=False)
        case["cards"][0].update(Resolution="underspecified", **{"Referent set": {"selection": "one(messages)", "partial_constraints": [], "candidate_sets": [["1712345678.000001"], ["1712345678.000002"]]}})
        self.assertEqual(validate_case(case)["errors"], [])
        case["cards"][0]["Referent set"]["candidate_sets"] = [["1712345678.000001", "1712345678.000002"]]
        self.assertTrue(any("at least two distinct" in e for e in validate_case(case)["errors"]))

    def test_delegated_choose_one_is_explicit(self):
        case = case_fixture()
        case["seed"]["message_reactions"].append({"message_id": "1712345678.000002", "user_id": "U1", "reaction_type": "eyes"})
        case["private"].update(expected_matches=["1712345678.000001", "1712345678.000002"], near_misses=[], require_near_miss=False)
        case["cards"][0]["Referent set"] = ["1712345678.000001", "1712345678.000002"]
        self.assertTrue(any("single mode requires" in e for e in validate_case(case)["errors"]))
        case["private"]["selection"] = "choose_one"
        self.assertEqual(validate_case(case)["errors"], [])

    def test_multiple_is_collection_intent_not_seed_cardinality(self):
        case = case_fixture()
        case["private"]["mode"] = "multiple"
        self.assertEqual(validate_case(case)["errors"], [])

    def test_absence_recomputed_and_links_checked(self):
        case = case_fixture()
        case["private"]["selector"]["focal"]["filters"][0]["value"] = "legal"
        case["private"].update(mode="absent", expected_matches=[], near_misses=["1712345678.000001"])
        case["cards"][0].update(Resolution="absent", **{"Referent set": []})
        self.assertEqual(validate_case(case)["errors"], [])
        case["task_spec"][0]["obligations"] = [2]
        self.assertTrue(any("1-based card indices" in e for e in validate_case(case)["errors"]))

    def test_extra_card_fields_rejected(self):
        case = case_fixture()
        case["cards"][0]["construction_trace"] = "not a card field"
        self.assertTrue(any("fixed card fields differ" in e for e in validate_case(case)["errors"]))

    def test_identifying_and_computation_attributes_use_real_fields(self):
        for field in ("Alternative sufficient identifying sets", "Change-computation attributes"):
            case = case_fixture()
            case["cards"][0][field] = [["users.departed"]]
            self.assertTrue(any("unknown real field 'users.departed'" in e for e in validate_case(case)["errors"]))
        case = case_fixture()
        case["cards"][0]["Written attributes"] = ["channels.project_status"]
        self.assertTrue(any("unknown real field" in e for e in validate_case(case)["errors"]))
        # Scope and descriptions remain prose, not field-identifier grammars.
        case = case_fixture()
        case["cards"][0]["Shared scope"] = "The departed person is not a users.departed field."
        self.assertEqual(validate_case(case)["errors"], [])


if __name__ == "__main__":
    unittest.main()
