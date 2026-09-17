"""Check input isolation and role-preserving assembly without model calls."""
import unittest
from .concept_writer import assignments, relationship, system_prompt, user_prompt


class ConceptWriterTests(unittest.TestCase):
    def test_mode_instructions_are_exclusive(self):
        for a in assignments():
            text = user_prompt(a)
            for mode in ('single', 'multiple', 'absent', 'underspecified'):
                self.assertEqual(f'The assigned mode is {mode.upper()}.' in text,
                                 mode == a['resolution_mode'])
            self.assertNotIn('{match_count}', text)
            self.assertNotIn('{alternative_count}', text)

    def test_long_route_directions_preserve_roles(self):
        self.assertEqual(relationship('MESSAGE', 'USER'), 'is authored by')
        self.assertEqual(relationship('REACTION', 'USER'), 'is contributed by')
        a = next(a for a in assignments() if a['route_id'] == 'R089')
        text = user_prompt(a)
        self.assertIn('User (position 2) holds Conversation Membership (position 3)', text)
        self.assertIn('Conversation Membership (position 3) belongs to conversation Conversation (position 4)', text)

    def test_assignment_counts_and_context_boundary(self):
        plan = assignments()
        self.assertEqual(len(plan), 10)
        self.assertEqual(len({a['case_id'] for a in plan}), 10)
        self.assertEqual({a['resolution_mode'] for a in plan}, {'single','multiple','absent','underspecified'})
        self.assertEqual(max(len(a['route_nodes']) - 1 for a in plan), 5)
        for a in plan:
            self.assertNotIn('source_context', a)
            self.assertNotIn('seed', a)
            text = user_prompt(a)
            self.assertNotIn('U01AGENBOT9', text)
            self.assertNotIn('C_INFRA', text)
        self.assertNotIn('slack_bench_v2', system_prompt())


if __name__ == '__main__':
    unittest.main()
