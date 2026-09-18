"""Test evidence preservation and mechanical rejection, not model verdicts."""
import copy
import json
import tempfile
import unittest
from pathlib import Path
from grounding.evaluation.adapter import FILES, build_packet, dump, paragraphs, pointer
from grounding.evaluation.validate import validate

SCHEMA = json.loads((Path(__file__).resolve().parents[2]/'grounding/evaluation/oracle-assessment.schema.json').read_text())


class AdapterTests(unittest.TestCase):
    def fixture(self):
        return {
            'prompt': {'test_id': 'example', 'run_id': 'recorded', 'prompt': 'Create a channel.'},
            'task_spec': [{'line': 1, 'text': '    Create the channel.', 'obligations': []}],
            'card': [],
            'initial_state': {'users': [{'user_id': 'A', 'name': 'A'}, {'user_id': 'B', 'name': 'B'}],
                              'channels': [{'id': 'X'}], 'members': [{'channel_id': 'X', 'user_id': 'A'}]},
            'diff': {'inserts': [{'__table__': 'channels', 'id': 'Y'}, {'__table__': 'members', 'user_id': 'A', 'channel_id': 'Y'}],
                     'deletes': [], 'updates': [{'before': {'name': 'old', 'updated_at': None}, 'after': {'name': 'new', 'updated_at': 'now'}}]},
            'response': {'final': 'Created it.\n\nAsk me for changes.'},
            'trajectory': {'steps': [{'action': 'literal command', 'observation': {'stdout': '{"members":["A"]}'},
                                      'assistant_text': ['<action>\nliteral command\n</action>', 'A distinct statement.']}], 'termination': 'done'},
        }

    def test_full_record_preservation_and_decoded_observation(self):
        original = self.fixture()
        with tempfile.TemporaryDirectory() as d:
            folder = Path(d)
            for key, filename in FILES.items():
                (folder/filename).write_text(json.dumps(original[key]))
            packet, sources, manifest = build_packet(folder)
            self.assertEqual(sources, original)
            for table, rows in original['initial_state'].items():
                for i, row in enumerate(rows):
                    self.assertIn(f'initial_state /{table}/{i}\n{dump(row)}', packet)
            self.assertIn('trajectory /steps/0/observation/stdout\n{"members":["A"]}', packet)
            self.assertIn('L1 |     Create the channel.', packet)
            self.assertIn('A distinct statement.', packet)
            self.assertEqual(len(manifest['duplicate_text_references']), 1)
            self.assertEqual(pointer(sources['trajectory'], '/steps/0/observation/stdout'), '{"members":["A"]}')

    def test_pointer_and_paragraph_conventions(self):
        self.assertEqual(pointer({'a/b': {'x~y': [3]}}, '/a~1b/x~0y/0'), 3)
        self.assertEqual(paragraphs(' One\nline\n \nTwo\n\n'), ['One\nline', 'Two'])

    def assessment(self):
        return {'schema_version': '3.0', 'test_id': 'example', 'run_id': 'recorded',
                'lines': [{'line': 1, 'task_status': 'active', 'execution_status': 'performed', 'grounding': {},
                           'evidence': [{'source': 'diff', 'location': '/inserts/0'}, {'source': 'diff', 'location': '/inserts/1'},
                                        {'source': 'diff', 'location': '/updates/0'}, {'source': 'response', 'location': '/final'}],
                           'explanation': 'Example only.'}], 'obligations': {}, 'unattributed': [], 'assessment_issue': None}

    def test_full_accounting_and_incidental_fields(self):
        a = self.assessment()
        self.assertFalse(validate(a, SCHEMA, self.fixture())['errors'])
        b = copy.deepcopy(a)
        b['lines'][0]['evidence'][2]['location'] = '/updates/0/after/name'
        self.assertIn('updates/0/updated_at', validate(b, SCHEMA, self.fixture())['missing_accounting_items'])
        b = copy.deepcopy(a)
        b['lines'][0]['evidence'].pop(1)
        self.assertIn('inserts/1', validate(b, SCHEMA, self.fixture())['missing_accounting_items'])
        b = copy.deepcopy(a)
        b['lines'][0]['evidence'][-1]['paragraphs'] = [1]
        self.assertIn('response:/final:2', validate(b, SCHEMA, self.fixture())['missing_accounting_items'])

    def test_substantive_line_cannot_be_replaced_by_marker(self):
        a = self.assessment()
        a['lines'] = [{'line': 1}]
        errors = validate(a, SCHEMA, self.fixture())['errors']
        self.assertTrue(any('marker-only' in e for e in errors))

    def test_bad_reference_and_link_are_rejected(self):
        a = self.assessment()
        a['lines'][0]['grounding'] = {'1': 'demonstrated_correct'}
        a['lines'][0]['evidence'].append({'source': 'initial_state', 'location': '/users/99'})
        errors = validate(a, SCHEMA, self.fixture())['errors']
        self.assertTrue(any('invented direct' in e for e in errors))
        self.assertTrue(any('Invalid evidence' in e for e in errors))


if __name__ == '__main__':
    unittest.main()
