"""Access-review boundary checks; mock conversation makes no model calls."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from grounding.tests.test_validation import case_fixture
from grounding.archive.slack_campaign.verify_access import access_input, check_review, verify_access


class AccessReviewTests(unittest.TestCase):
    def setUp(self):
        self.case = case_fixture()
        self.report = {"probes": [
            {"probe": {"method": "conversations.history", "params": {"channel": "CO"}}, "errors": [],
             "pages": [{"status_code": 200, "body": {"ok": True, "messages": [], "has_more": False}}]},
            {"probe": {"method": "users.info", "params": {"user": "HIDDEN_ID"}}, "errors": [],
             "pages": [{"status_code": 200, "body": {"ok": True, "user": {"id": "HIDDEN_ID"}}}]},
        ]}
        self.prior = {"certified": False, "errors": ["SECRET_PRIOR_DIAGNOSIS"], "discoverable_probe_indices": [0]}
        self.review = {"status": "established", "matches": self.case['private']['expected_matches'], "focal_negatives": self.case['private']['near_misses'],
                       "evidence": [{"probe": 0, "explanation": "Complete recorded collection."}], "limitations": []}

    def test_model_input_excludes_private_truth_and_unknown_probes(self):
        payload = access_input(self.case, self.report, self.prior)
        text = json.dumps(payload)
        self.assertNotIn("HIDDEN_ID", text)
        self.assertNotIn("SECRET_PRIOR_DIAGNOSIS", text)
        self.assertNotIn("near_misses", text)
        self.assertNotIn("expected_matches", text)
        self.assertNotIn("cards", payload)
        self.assertNotIn("seed", payload)
        self.assertNotIn(self.case['private']['expected_matches'][0], text)

    def test_wrong_answers_or_unsupported_evidence_do_not_certify(self):
        payload = access_input(self.case, self.report, self.prior)
        self.assertEqual(check_review(self.review, self.case, self.case['seed'], payload), [])
        wrong = {**self.review, "matches": self.case['private']['near_misses']}
        self.assertTrue(check_review(wrong, self.case, self.case['seed'], payload))
        missing = {**self.review, "focal_negatives": []}
        self.assertTrue(check_review(missing, self.case, self.case['seed'], payload))
        hidden = {**self.review, "evidence": [{"probe": 1, "explanation": "Unprovided result"}]}
        self.assertTrue(check_review(hidden, self.case, self.case['seed'], payload))

    def test_bounded_mock_review_saves_method(self):
        review = self.review
        class FakeConversation:
            def __init__(self, folder, system, **kwargs):
                assert kwargs['max_tokens'] == 8000
                assert kwargs['effort'] == 'medium'
            def ask(self, message):
                assert 'SECRET_PRIOR_DIAGNOSIS' not in message
                return review
        with tempfile.TemporaryDirectory() as folder:
            with patch('grounding.archive.slack_campaign.verify_access.Conversation', FakeConversation):
                result = verify_access(self.case, self.case['seed'], self.report, self.prior, Path(folder)/'access')
            self.assertTrue(result['certified'])
            self.assertEqual(result['method'], 'model_access_review')
            self.assertTrue((Path(folder)/'access/prior_forward_check.json').exists())

    def test_one_repair_continues_same_conversation_and_preserves_first_attempt(self):
        correct = self.review
        wrong = {**correct, 'matches': [[handle] for handle in correct['matches']], 'focal_negatives': []}
        instances = []
        class FakeConversation:
            def __init__(self, folder, system, **kwargs):
                self.messages = []
                instances.append(self)
            def ask(self, message):
                if not self.messages:
                    self.messages.extend([{'role': 'user', 'content': message},
                                          {'role': 'assistant', 'content': wrong, 'signature': 'untouched-native'}])
                    return wrong
                assert self.messages[-1]['signature'] == 'untouched-native'
                assert 'Validation failed' in message
                assert 'discoverable_probes' not in message
                for handle in correct['matches'] + correct['focal_negatives']:
                    assert handle not in message
                self.messages.extend([{'role': 'user', 'content': message}, {'role': 'assistant', 'content': correct}])
                return correct
        with tempfile.TemporaryDirectory() as folder:
            out = Path(folder)/'access'
            with patch('grounding.archive.slack_campaign.verify_access.Conversation', FakeConversation):
                result = verify_access(self.case, self.case['seed'], self.report, self.prior, out)
            self.assertTrue(result['certified'], result)
            self.assertEqual(result['repair_count'], 1)
            self.assertEqual(len(instances), 1)
            self.assertEqual(len(instances[0].messages), 4)
            first = json.loads((out/'attempt-01.json').read_text())
            self.assertEqual(first['review'], wrong)
            self.assertTrue(first['errors'])
            self.assertEqual(json.loads((out/'attempt-02.json').read_text())['errors'], [])

    def test_repair_is_bounded_after_repeated_validation_failure(self):
        correct = self.review
        calls = []
        class FakeConversation:
            def __init__(self, *args, **kwargs): pass
            def ask(self, message):
                calls.append(message)
                return {**correct, 'focal_negatives': []}
        with tempfile.TemporaryDirectory() as folder:
            with patch('grounding.archive.slack_campaign.verify_access.Conversation', FakeConversation):
                result = verify_access(self.case, self.case['seed'], self.report, self.prior, Path(folder)/'access')
            self.assertFalse(result['certified'])
            self.assertEqual(len(calls), 2)
            self.assertEqual(result['repair_count'], 1)


if __name__ == '__main__':
    unittest.main()
