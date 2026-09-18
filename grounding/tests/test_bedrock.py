"""Recorded native conversations remain compatible without making model calls."""
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from grounding.common.bedrock import Conversation, save


def returned_response(text, *, extra_blocks=(), stop_reason='end_turn'):
    raw = {
        'stop_reason': stop_reason,
        'content': [*extra_blocks, {'type': 'text', 'text': text}],
        'usage': {'input_tokens': 30, 'output_tokens': 20,
                  'cache_creation_input_tokens': 1200, 'cache_read_input_tokens': 0},
    }
    return {'body': io.BytesIO(json.dumps(raw).encode()), 'ResponseMetadata': {}}


class ConversationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.folder = Path(self.temp.name) / 'writer'
        self.factory = patch('grounding.common.bedrock.boto3.client').start()
        self.addCleanup(patch.stopall)
        self.client = self.factory.return_value

    def test_json_default_preserves_request_and_output_contract(self):
        self.client.invoke_model.return_value = returned_response('{"accepted": true}')
        conversation = Conversation(self.folder, 'Shared instructions')
        self.assertEqual(conversation.ask('Case one'), {'accepted': True})
        body = json.loads(self.client.invoke_model.call_args.kwargs['body'])
        self.assertEqual(body['system'], 'Shared instructions')
        self.assertNotIn('cache_control', body)
        self.assertEqual(json.loads((self.folder / 'turn-01/output.json').read_text()),
                         {'accepted': True})
        self.assertFalse((self.folder / 'turn-01/output.md').exists())

    def test_text_output_and_cached_common_prefix(self):
        answer = 'Route: Message → Reaction → User\n\n| Message | Reactions |\n| A | Tom 👍 |'
        self.client.invoke_model.return_value = returned_response(answer)
        conversation = Conversation(self.folder, 'Shared instructions',
                                    output_format='markdown', cache_system=True)
        self.assertEqual(conversation.ask('Assigned mode: multiple'), answer)
        body = json.loads(self.client.invoke_model.call_args.kwargs['body'])
        self.assertEqual(body['system'], [{'type': 'text', 'text': 'Shared instructions',
                                        'cache_control': {'type': 'ephemeral'}}])
        self.assertEqual(body['messages'], [{'role': 'user', 'content': [
            {'type': 'text', 'text': 'Assigned mode: multiple'}]}])
        self.assertEqual((self.folder / 'turn-01/output.md').read_text(), answer)
        self.assertFalse((self.folder / 'turn-01/output.json').exists())
        summary = json.loads((self.folder / 'turn-01/summary.json').read_text())
        self.assertEqual(summary['output_format'], 'markdown')
        self.assertEqual(summary['usage']['cache_creation_input_tokens'], 1200)
        self.assertNotIn('parse_error', summary)

    def test_resume_preserves_text_format_and_native_assistant_blocks(self):
        native_blocks = [{'type': 'thinking', 'thinking': 'Recorded reasoning',
                          'signature': 'signature-kept-verbatim'},
                         {'type': 'redacted_thinking', 'data': 'opaque-data'}]
        self.client.invoke_model.side_effect = [
            returned_response('First table', extra_blocks=native_blocks),
            returned_response('Repaired table'),
        ]
        original = Conversation(self.folder, 'Shared instructions',
                                output_format='text', cache_system=True)
        original.ask('First request')
        resumed = Conversation.resume(self.folder)
        self.assertEqual(resumed.ask('Please fix the missing row.'), 'Repaired table')
        body = json.loads(self.client.invoke_model.call_args.kwargs['body'])
        self.assertEqual(body['messages'][1], {'role': 'assistant', 'content': [
            *native_blocks, {'type': 'text', 'text': 'First table'}]})
        self.assertEqual(body['messages'][0]['content'][0]['text'], 'First request')
        self.assertEqual(body['messages'][2]['content'][0]['text'], 'Please fix the missing row.')
        self.assertEqual(body['system'], original.body['system'])
        self.assertEqual((self.folder / 'turn-02/output.md').read_text(), 'Repaired table')
        self.assertEqual(json.loads((self.folder / 'turn-02/summary.json').read_text())[
            'output_format'], 'text')

    def test_legacy_resume_defaults_to_json(self):
        self.client.invoke_model.side_effect = [returned_response('{"a": 1}'),
                                               returned_response('{"a": 2}')]
        Conversation(self.folder, 'Instructions').ask('Request')
        path = self.folder / 'turn-01/summary.json'
        legacy_summary = json.loads(path.read_text())
        del legacy_summary['output_format']
        save(path, legacy_summary)
        resumed = Conversation.resume(self.folder)
        self.assertEqual(resumed.ask('Repair'), {'a': 2})
        self.assertTrue((self.folder / 'turn-02/output.json').exists())

    def test_incomplete_text_is_saved_but_not_accepted_or_resumed(self):
        self.client.invoke_model.return_value = returned_response(
            'Unfinished table', stop_reason='max_tokens')
        conversation = Conversation(self.folder, 'Instructions', output_format='text')
        with self.assertRaisesRegex(RuntimeError, 'Incomplete model response'):
            conversation.ask('Request')
        self.assertEqual((self.folder / 'turn-01/answer.txt').read_text(), 'Unfinished table')
        self.assertFalse((self.folder / 'turn-01/output.md').exists())
        with self.assertRaisesRegex(ValueError, 'Cannot repair incomplete model output'):
            Conversation.resume(self.folder)


if __name__ == '__main__':
    unittest.main()
