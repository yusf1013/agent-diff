"""Mutation preservation, assignment locks, and native repair conversation tests."""

from copy import deepcopy
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch

from grounding.common.bedrock import Conversation, save
from grounding.archive.slack_campaign.generate import materialize, repair_construction, validate_assignment
from grounding.tests.test_validation import case_fixture, seed_fixture


def mutation_output(edits):
    return {"case_id": "case_1", "seed_edits": edits, "private": {"construction_explanation": "Declared local changes"}}


def assignment_fixture(case):
    return {
        "case_id": case["case_id"], "mode": "single", "referent_entity": "MESSAGE",
        "route_nodes": ["MESSAGE", "REACTION", "USER", "CONVERSATION_MEMBERSHIP", "CONVERSATION"],
        "requires_near_miss": True,
        "focal_condition": {"kind": "field", "field": "channels.channel_name", "node_index": 4},
        "stage": "introduce_focal_near_miss",
        "baseline_context": {"prompt": case["prompt"], "card": deepcopy(case["cards"][0])},
    }


class MaterializationTests(unittest.TestCase):
    def test_local_edits_preserve_every_untouched_row_and_source_object(self):
        source = seed_fixture()
        # Source data outside the seven authored tables must not disappear.
        source["user_settings"] = [{"user_id": "UA", "notification_level": "mentions"}]
        original = deepcopy(source)
        inserted = {"message_id": "1712345678.000004", "channel_id": "CO", "user_id": "UA", "message_text": "Deployment reminder"}
        output = mutation_output([
            {"table": "channels", "op": "update", "key": {"channel_id": "CO"}, "values": {"topic_text": "Scheduling"}},
            {"table": "messages", "op": "insert", "values": inserted},
            {"table": "message_reactions", "op": "delete", "key": {"message_id": "1712345678.000001", "user_id": "U1", "reaction_type": "eyes"}},
        ])
        output_before = deepcopy(output)
        actual = materialize(output, source)
        expected = deepcopy(original)
        expected["channels"][1]["topic_text"] = "Scheduling"
        expected["messages"].append(inserted)
        expected["message_reactions"].pop(1)
        self.assertEqual(actual["seed"], expected)
        self.assertEqual(source, original)
        self.assertEqual(output, output_before)
        self.assertNotIn("seed_edits", actual)
        actual["seed"]["users"][0]["real_name"] = "Changed after materialization"
        self.assertEqual(source, original)

    def test_wrong_primary_keys_never_select_an_arbitrary_row(self):
        for key in ({"user_id": "U1"}, {"channel_id": "CS"}, {"channel_id": "CS", "user_id": "U1", "extra": "x"}):
            with self.subTest(key=key), self.assertRaisesRegex(ValueError, "complete native primary key"):
                materialize(mutation_output([{"table": "channel_members", "op": "delete", "key": key}]), seed_fixture())
        with self.assertRaisesRegex(ValueError, "exactly one existing"):
            materialize(mutation_output([{"table": "users", "op": "update", "key": {"user_id": "missing"}, "values": {"title": "Engineer"}}]), seed_fixture())

    def test_primary_key_mutation_and_unknown_tables_rejected(self):
        with self.assertRaisesRegex(ValueError, "Primary-key mutation"):
            materialize(mutation_output([{"table": "users", "op": "update", "key": {"user_id": "U1"}, "values": {"user_id": "NEW"}}]), seed_fixture())
        with self.assertRaisesRegex(ValueError, "Unsupported edit table"):
            materialize(mutation_output([{"table": "fake_users", "op": "insert", "values": {}}]), seed_fixture())

    def test_mutation_cannot_replace_the_source_seed(self):
        for replacement in (seed_fixture(), {}, None):
            with self.subTest(replacement=replacement):
                output = mutation_output([])
                output["seed"] = replacement
                with self.assertRaisesRegex(ValueError, "not replace the source seed"):
                    materialize(output, seed_fixture())
        with self.assertRaisesRegex(ValueError, "not source edits"):
            materialize({"seed": seed_fixture(), "seed_edits": [{"op": "delete"}]})


class AssignmentLockTests(unittest.TestCase):
    def setUp(self):
        self.case = case_fixture()
        self.case["prompt"] = "React with 'thumbsup' to the rollout message that a member of #security reacted to."
        self.case["private"]["require_near_miss"] = True
        self.assignment = assignment_fixture(self.case)

    def test_valid_assignment_and_locked_literal(self):
        self.assertEqual(validate_assignment(self.case, self.assignment)["errors"], [])
        self.case["prompt"] = self.case["prompt"].replace("thumbsup", "eyes")
        errors = validate_assignment(self.case, self.assignment)["errors"]
        self.assertTrue(any("literal must remain unchanged" in error for error in errors))
        self.assertTrue(any("prompt verbatim" in error for error in errors))

    def test_focal_field_path_and_stage_cannot_be_relaxed(self):
        self.case["private"]["selector"]["focal"]["filters"][0]["field"] = "purpose_text"
        errors = validate_assignment(self.case, self.assignment)["errors"]
        self.assertTrue(any("assigned field" in error for error in errors))
        self.case = case_fixture()
        self.case["private"]["selector"]["focal"]["path"] = ["messages"]
        self.case["private"]["selector"]["focal"].update(joins=[], filters=[])
        self.assertTrue(any("Focal path" in error for error in validate_assignment(self.case, self.assignment)["errors"]))
        self.case = case_fixture()
        self.case["private"]["require_near_miss"] = False
        self.assertTrue(any("assigned stage" in error for error in validate_assignment(self.case, self.assignment)["errors"]))

    def test_absent_focal_negative_or_swapped_answer_rejected(self):
        self.case["private"]["near_misses"] = []
        self.assertTrue(any("requires at least one" in error for error in validate_assignment(self.case, self.assignment)["errors"]))
        self.case = case_fixture()
        self.case["cards"][0]["Referent set"] = ["1712345678.000002"]
        errors = validate_assignment(self.case, self.assignment)["errors"]
        self.assertTrue(any("preserve the source intended referents" in error for error in errors))

    def test_malformed_focal_index_returns_repairable_errors(self):
        self.case["private"]["focal_obligation"] = 999
        errors = validate_assignment(self.case, self.assignment)["errors"]
        self.assertTrue(any("1-based card index" in error for error in errors))


class NativeConversationTests(unittest.TestCase):
    def test_resume_and_followup_preserve_complete_native_assistant_content(self):
        with tempfile.TemporaryDirectory() as temporary:
            folder = Path(temporary) / "author"
            turn = folder / "turn-02"
            previous_assistant = [
                {"type": "thinking", "thinking": "Prior returned summary", "signature": "opaque-prior-signature"},
                {"type": "text", "text": '{"status":"designed"}'},
            ]
            latest_assistant = [
                {"type": "thinking", "thinking": "Latest returned summary", "signature": "opaque-latest-signature"},
                {"type": "redacted_thinking", "data": "opaque-redacted-payload"},
                {"type": "text", "text": '{"answer":"original"}'},
            ]
            request = {
                "anthropic_version": "bedrock-2023-05-31", "max_tokens": 24000,
                "thinking": {"type": "adaptive", "display": "summarized"},
                "output_config": {"effort": "medium"}, "system": "Frozen instructions",
                "messages": [
                    {"role": "user", "content": [{"type": "text", "text": "Design"}]},
                    {"role": "assistant", "content": previous_assistant},
                    {"role": "user", "content": [{"type": "text", "text": "Compile"}]},
                ],
            }
            response = {"stop_reason": "end_turn", "content": latest_assistant}
            save(turn / "request.json", request)
            save(turn / "response.json", response)
            save(turn / "summary.json", {"model": "model-id", "region": "region-id", "turn": 2})
            original_request = (turn / "request.json").read_bytes()
            original_response = (turn / "response.json").read_bytes()
            conversation = Conversation.resume(folder)
            expected = deepcopy(request)
            expected["messages"].append({"role": "assistant", "content": latest_assistant})
            self.assertEqual(conversation.body, expected)
            self.assertEqual(conversation.turn, 2)
            next_native = {"stop_reason": "end_turn", "content": [{"type": "text", "text": '{"repaired":true}'}], "usage": {"input_tokens": 23, "output_tokens": 7}}
            with patch("grounding.common.bedrock.boto3.client") as client:
                client.return_value.invoke_model.return_value = {"body": io.BytesIO(json.dumps(next_native).encode()), "ResponseMetadata": {"RequestId": "local-test"}}
                self.assertEqual(conversation.ask("Thanks. Fix only this validation error."), {"repaired": True})
                sent = json.loads(client.return_value.invoke_model.call_args.kwargs["body"])
            expected["messages"].append({"role": "user", "content": [{"type": "text", "text": "Thanks. Fix only this validation error."}]})
            self.assertEqual(sent, expected)
            self.assertEqual(sent["messages"][1]["content"], previous_assistant)
            self.assertEqual(sent["messages"][3]["content"], latest_assistant)
            self.assertEqual((turn / "request.json").read_bytes(), original_request)
            self.assertEqual((turn / "response.json").read_bytes(), original_response)

    def test_incomplete_native_turn_cannot_be_repaired_as_completed(self):
        with tempfile.TemporaryDirectory() as temporary:
            turn = Path(temporary) / "turn-01"
            save(turn / "request.json", {"messages": []})
            save(turn / "response.json", {"stop_reason": "max_tokens", "content": []})
            save(turn / "summary.json", {"model": "m", "region": "r", "turn": 1})
            with self.assertRaisesRegex(ValueError, "incomplete"):
                Conversation.resume(temporary)


class AnnotationRepairTests(unittest.TestCase):
    def prepare(self, folder):
        case = case_fixture()
        case['seed']['message_reactions'].append({
            'message_id': '1712345678.000002', 'user_id': 'U1', 'reaction_type': 'eyes'})
        candidates = [['1712345678.000001'], ['1712345678.000002']]
        case['private'].update(mode='underspecified', require_near_miss=False, near_misses=[],
                               expected_matches=['1712345678.000001', '1712345678.000002'],
                               candidate_sets=deepcopy(candidates))
        case['cards'][0].update(Resolution='underspecified', **{
            'Referent set': {'selection': 'set(messages)', 'partial_constraints': [],
                             'candidate_sets': deepcopy(candidates)}})
        case['task_spec'] = [
            {'line': 1, 'text': 'Look up the relevant reactors.', 'obligations': [1]},
            {'line': 2, 'text': case['prompt'], 'obligations': [1]},
        ]
        assignment = assignment_fixture(case)
        assignment.update(mode='underspecified', requires_near_miss=False)
        save(folder / 'input.json', {'assignment': assignment, 'source': None})
        save(folder / 'case.json', case)
        save(folder / 'summary.json', {'status': 'construction_validated', 'semantic_repairs': 1, 'runtime_repairs': 1})
        save(folder / 'semantic_repair.json', {'issues': ['Historical semantic repair']})
        save(folder / 'runtime_repair.json', {'issues': ['Historical runtime repair']})
        output = {'cards': deepcopy(case['cards']), 'task_spec': [
            {'line': 1, 'text': case['prompt'], 'obligations': [1]}]}
        output['cards'][0]['Referent set']['selection'] = 'one(messages)'
        review = {'decision': 'pass', 'issues': [], 'checks': [
            {'name': name, 'status': 'pass'} for name in (
                'prompt_path_fidelity', 'resolution', 'negatives', 'realism_and_hints',
                'api_scope', 'cards_and_spec', 'mutation_integrity')]}
        return case, output, review

    def test_annotation_repair_freezes_case_and_has_its_own_bound(self):
        with tempfile.TemporaryDirectory() as temporary:
            folder = Path(temporary)
            original, output, review = self.prepare(folder)
            author, reviewer = Mock(), Mock()
            author.ask.return_value = output
            reviewer.ask.return_value = review
            with patch('grounding.archive.slack_campaign.generate.Conversation.resume', side_effect=[author, reviewer]) as resume:
                summary = repair_construction(folder, ['Use one(messages); retain alternatives. Remove intermediate lookup task.'], kind='annotation')
                self.assertEqual(summary['status'], 'construction_validated')
                self.assertEqual(summary['annotation_repairs'], 1)
                self.assertEqual(summary['semantic_repairs'], 1)
                self.assertEqual(summary['runtime_repairs'], 1)
                updated = json.loads((folder / 'case.json').read_text())
                for field in original.keys() - {'cards', 'task_spec'}:
                    self.assertEqual(updated[field], original[field])
                self.assertEqual(updated['cards'][0]['Referent set']['selection'], 'one(messages)')
                self.assertEqual(updated['cards'][0]['Referent set']['candidate_sets'], original['cards'][0]['Referent set']['candidate_sets'])
                self.assertEqual(len(updated['task_spec']), 1)
                self.assertEqual(resume.call_count, 2)
                self.assertIn('Return exactly {cards:[...],task_spec:[...]}', author.ask.call_args.args[0])
                with self.assertRaisesRegex(ValueError, 'already attempted'):
                    repair_construction(folder, ['Again'], kind='annotation')
                self.assertEqual(resume.call_count, 2)
            self.assertEqual(json.loads((folder / 'case-before-annotation-repair.json').read_text()), original)

    def test_annotation_repair_rejects_protected_keys_before_review(self):
        for protected in ('prompt', 'acting_user_id', 'seed', 'private'):
            with self.subTest(protected=protected), tempfile.TemporaryDirectory() as temporary:
                folder = Path(temporary)
                original, output, _ = self.prepare(folder)
                output[protected] = deepcopy(original[protected])
                author = Mock()
                author.ask.return_value = output
                with patch('grounding.archive.slack_campaign.generate.Conversation.resume', return_value=author) as resume:
                    summary = repair_construction(folder, ['Fix annotation only'], kind='annotation')
                self.assertEqual(summary['status'], 'invalid_after_annotation_repair')
                self.assertEqual(resume.call_count, 1)
                self.assertTrue(any('all other case fields are frozen' in error for error in summary['errors']))
                self.assertEqual(json.loads((folder / 'case.json').read_text()), original)

    def test_annotation_repair_cannot_change_competing_referents(self):
        with tempfile.TemporaryDirectory() as temporary:
            folder = Path(temporary)
            original, output, _ = self.prepare(folder)
            output['cards'][0]['Referent set']['candidate_sets'].reverse()
            # Even reordering the alternatives is unnecessary for this narrow repair.
            author = Mock()
            author.ask.return_value = output
            with patch('grounding.archive.slack_campaign.generate.Conversation.resume', return_value=author) as resume:
                summary = repair_construction(folder, ['Fix annotation only'], kind='annotation')
            self.assertEqual(summary['status'], 'invalid_after_annotation_repair')
            self.assertTrue(any('changed O1 candidate_sets' in error for error in summary['errors']))
            self.assertEqual(resume.call_count, 1)
            self.assertEqual(json.loads((folder / 'case.json').read_text()), original)


if __name__ == "__main__":
    unittest.main()
