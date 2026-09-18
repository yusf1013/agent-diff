"""Check input isolation and role-preserving assembly without model calls."""
import unittest
from grounding.paths import PROJECT_ROOT
ARCHIVED = PROJECT_ROOT / "archive/slack_campaign/prompts/v3"
from grounding.generation.concept_writer import PROMPTS, assignments, relationship, system_prompt, user_prompt


class ConceptWriterTests(unittest.TestCase):
    def test_versioned_inputs_inject_only_relevant_operation_menu(self):
        prompts = PROMPTS
        reaction = next(a for a in assignments() if a['referent_entity'] == 'REACTION')
        text = user_prompt(reaction, prompts)
        self.assertIn("Prefer removing the actor's own selected reaction", text)
        self.assertNotIn('Ordinary-member versus guest classification', text)
        self.assertIn('The assigned mode is SINGLE.', text)
        self.assertNotIn('The assigned mode is MULTIPLE.', text)
        self.assertNotIn('Downstream operation menu', user_prompt(reaction, ARCHIVED))
        self.assertNotEqual(system_prompt(ARCHIVED), system_prompt(prompts))

    def test_mode_instructions_are_exclusive(self):
        for prompts in (ARCHIVED, PROMPTS):
            for a in assignments():
                text = user_prompt(a, prompts)
                for mode in ('single', 'multiple', 'absent', 'underspecified'):
                    self.assertEqual(f'The assigned mode is {mode.upper()}.' in text,
                                     mode == a['resolution_mode'])
                self.assertNotIn('{match_count}', text)
                self.assertNotIn('{alternative_count}', text)

    def test_current_writer_limits_positive_variants_to_multiple_mode(self):
        prompts = PROMPTS
        shared = system_prompt(prompts)
        self.assertNotIn('Give multiple matches useful variants', shared)
        self.assertNotIn('an existing environment', shared)
        self.assertIn('a fresh environment', shared)
        for a in assignments():
            text = shared + user_prompt(a, prompts)
            self.assertEqual('Make useful positive variants' in text,
                             a['resolution_mode'] == 'multiple')

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
