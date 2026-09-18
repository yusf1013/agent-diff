"""Continuation integrity and bounded retries without paid API calls."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from grounding.common.bedrock import Conversation, save
from grounding.generation.concept_reflect import prepare, reflect_one, verify_originals
from grounding.tests.test_bedrock import returned_response


class ReflectionTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.folder = Path(temp.name)
        (self.folder / 'system.md').write_text('Shared original instructions')
        save(self.folder / 'assignments.json', [{'case_id': 'W01'}])
        case = self.folder / 'W01'
        case.mkdir()
        (case / 'input.md').write_text('Original assignment')
        self.writer = case / 'writer'
        self.factory = patch('grounding.common.bedrock.boto3.client').start()
        self.addCleanup(patch.stopall)
        self.client = self.factory.return_value
        self.client.invoke_model.return_value = returned_response('Original sketch', extra_blocks=[
            {'type': 'thinking', 'thinking': 'Original reasoning', 'signature': 'preserve-this'}])
        Conversation(self.writer, 'Shared original instructions', output_format='markdown',
                     cache_system=True).ask('Original assignment')
        self.cases, self.followup = prepare(self.folder)

    def test_followup_preserves_history_and_does_not_repeat(self):
        self.client.invoke_model.return_value = returned_response('Audit and repaired sketch')
        reflect_one(self.folder, 'W01', self.followup)
        verify_originals(self.folder)
        request = json.loads((self.writer / 'turn-02/request.json').read_text())
        self.assertEqual([m['role'] for m in request['messages']], ['user', 'assistant', 'user'])
        self.assertEqual(request['messages'][1]['content'][0]['signature'], 'preserve-this')
        self.assertEqual(request['messages'][2]['content'][0]['text'], self.followup)
        self.assertEqual(self.client.invoke_model.call_count, 2)
        reflect_one(self.folder, 'W01', self.followup)
        self.assertEqual(self.client.invoke_model.call_count, 2)
        self.assertFalse((self.writer / 'turn-03').exists())

    def test_changed_originals_are_rejected(self):
        (self.writer / 'turn-01/output.md').write_text('Manual correction')
        with self.assertRaisesRegex(ValueError, 'Original artifacts changed'):
            verify_originals(self.folder)
        with self.assertRaisesRegex(ValueError, 'original records changed'):
            prepare(self.folder)

    def test_incomplete_followup_is_not_retried(self):
        self.client.invoke_model.return_value = returned_response('Truncated', stop_reason='max_tokens')
        with self.assertRaisesRegex(RuntimeError, 'Incomplete model response'):
            reflect_one(self.folder, 'W01', self.followup)
        with self.assertRaisesRegex(ValueError, 'no automatic retry'):
            reflect_one(self.folder, 'W01', self.followup)
        self.assertEqual(self.client.invoke_model.call_count, 2)
        verify_originals(self.folder)


if __name__ == '__main__':
    unittest.main()
