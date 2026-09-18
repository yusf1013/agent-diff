"""Verify repair preserves conversation history and cannot become an unbounded loop."""
import copy
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from grounding.evaluation.run import build_repair_request, main, repair_saved_run


class RepairTests(unittest.TestCase):
    def test_exact_history_and_signed_blocks_preserved(self):
        request = {'system': 'original policy', 'max_tokens': 16000,
                   'thinking': {'type': 'adaptive', 'display': 'summarized'},
                   'messages': [{'role': 'user', 'content': [{'type': 'text', 'text': 'original evidence and instructions'}]}]}
        response = {'stop_reason': 'end_turn', 'content': [
            {'type': 'thinking', 'thinking': 'provider summary', 'signature': 'opaque-signature'},
            {'type': 'redacted_thinking', 'data': 'opaque-data'},
            {'type': 'text', 'text': '```json\n{"original":"answer"}\n```'}]}
        originals = copy.deepcopy((request, response))
        errors = ['L4: marker-only output for a substantive specification line', 'Unaccounted response paragraph']
        body, followup = build_repair_request(request, response, errors)
        self.assertEqual(body['messages'][:-2], request['messages'])
        self.assertEqual(body['messages'][-2], {'role': 'assistant', 'content': response['content']})
        self.assertEqual(body['messages'][-1], {'role': 'user', 'content': [{'type': 'text', 'text': followup}]})
        self.assertEqual({k:v for k,v in body.items() if k != 'messages'}, {k:v for k,v in request.items() if k != 'messages'})
        self.assertEqual((request, response), originals)
        for error in errors:
            self.assertIn(error, followup)
        self.assertNotIn('original evidence', followup)

    def test_no_repair_for_success_incomplete_or_second_repair(self):
        with self.assertRaises(ValueError):
            build_repair_request({}, {'stop_reason': 'end_turn'}, [])
        with self.assertRaises(ValueError):
            build_repair_request({}, {'stop_reason': 'max_tokens'}, ['error'])
        with tempfile.TemporaryDirectory() as d:
            parent=Path(d)/'previous'; parent.mkdir()
            (parent/'summary.json').write_text(json.dumps({'repair_turn': 1}))
            with self.assertRaisesRegex(ValueError, 'bound'):
                repair_saved_run(parent, Path(d)/'next')
            self.assertFalse((Path(d)/'next').exists())

    def test_explicit_repair_routes_to_saved_history(self):
        with patch('sys.argv', ['run.py', '--repair-from', '/tmp/prior', '--out', '/tmp/followup']), \
                patch('grounding.evaluation.run.repair_saved_run', return_value=0) as repair:
            self.assertEqual(main(), 0)
            repair.assert_called_once_with(Path('/tmp/prior'), Path('/tmp/followup'), 300)

    def test_automatic_followup_only_for_completed_validation_failure(self):
        for errors in ([], ['mechanical error']):
            with self.subTest(errors=errors), tempfile.TemporaryDirectory() as d:
                folder=Path(d)
                (folder/'schema.json').write_text('{}')
                (folder/'instructions.md').write_text('policy')
                sources={'prompt': {'test_id': 'example', 'run_id': 'recorded'}}
                def recorded_call(body, out, summary, *args):
                    (out/'summary.json').write_text(json.dumps({'status': 'returned', 'validation_errors': errors}))
                    return int(bool(errors))
                args=['run.py', '--inputs', str(folder), '--instructions', str(folder/'instructions.md'),
                      '--schema', str(folder/'schema.json'), '--out', str(folder/'output'), '--repair-on-validation-failure']
                with patch('sys.argv', args), patch('grounding.evaluation.run.build_packet', return_value=('evidence', sources, {'files': {}})), \
                        patch('grounding.evaluation.run.invoke_and_record', side_effect=recorded_call) as invoke, \
                        patch('grounding.evaluation.run.repair_saved_run', return_value=0) as repair:
                    self.assertEqual(main(), 0)
                    self.assertEqual(invoke.call_count, 1)
                    if errors:
                        repair.assert_called_once_with(folder/'output', folder/'output-repair-1', 300)
                    else:
                        repair.assert_not_called()


if __name__ == '__main__':
    unittest.main()
