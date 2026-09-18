"""Offline checks for relocated inputs, stage ownership, and cost accounting."""
import asyncio
import json
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch, AsyncMock

from grounding.common.bedrock import save
from grounding.common.layout import writer_root
from grounding.common.usage import report
from grounding.generation import concept_compile, concept_writer, concept_batch
from grounding.paths import REPO_ROOT, relocate
from grounding.tests.test_concept_compile import fixture


class ReorganizationTests(unittest.TestCase):
    def test_old_paths_resolve_with_specific_moves_before_directory_moves(self):
        for old, new in [
            ('grounding/slack_campaign/concept_writer.py', 'grounding/generation/concept_writer.py'),
            ('grounding/slack_campaign/prompts/v4/writer.md', 'grounding/prompts/writer/writer.md'),
            ('experiments/slack_bedrock/results/a.json', 'grounding/runs/slack_baseline/a.json'),
            ('grounding/slack_ground_truth/reports/slack_98.json', 'grounding/reference_labels/slack/reports/slack_98.json'),
        ]:
            self.assertEqual(relocate(old), REPO_ROOT / new)
            self.assertEqual(relocate(REPO_ROOT / old), REPO_ROOT / new)
        self.assertEqual(relocate('/tmp/external-evidence.json'), Path('/tmp/external-evidence.json'))

    def test_writer_inputs_have_stage_layout_and_remain_usable_by_compiler(self):
        with tempfile.TemporaryDirectory() as d:
            folder = Path(d)
            _, plan = concept_writer.prepare(folder)
            for assignment in plan:
                cid = assignment['case_id']
                self.assertTrue((folder/'cases'/cid/'assignment.json').is_file())
                self.assertEqual(writer_root(folder, cid), folder/'cases'/cid/'generation')
                self.assertTrue((writer_root(folder, cid)/'input.md').is_file())
            # Historical layout remains readable, with no migration of raw records.
            legacy = folder/'old'; (legacy/'W01').mkdir(parents=True)
            self.assertEqual(writer_root(legacy, 'W01'), legacy/'W01')

    def test_compilation_separates_checker_and_reviewer_records(self):
        packet, compiled = fixture()
        packet['sketch']['final_sketch'] = 'fixed story'
        packet['assignment']['alternative_count'] = None
        with tempfile.TemporaryDirectory() as d, \
             patch.object(concept_compile, 'packet_for', return_value=packet), \
             patch.object(concept_compile, 'Conversation') as conversation, \
             patch.object(concept_compile, 'report'):
            compiler, reviewer = SimpleNamespace(ask=lambda _: compiled), SimpleNamespace(
                ask=lambda _: {'validity': 'pass', 'quality': 'adequate', 'issues': []})
            conversation.side_effect = [compiler, reviewer]
            out = Path(d)/'generation'
            result = concept_compile.run(Path(d), 'W01', out)
            self.assertEqual(result['status'], 'review_pass')
            self.assertTrue((out/'compiler/compiled-1.json').is_file())
            self.assertTrue((out/'validation/checks-1.json').is_file())
            self.assertTrue((out/'reviewer/review-1.json').is_file())
            self.assertTrue((out/'case.json').is_file())
            self.assertEqual(conversation.call_args_list[1].args[0], out/'reviewer/attempt-1')

    def test_execution_routes_environment_solver_and_evaluation_outputs(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d); out = root/'cases/W01'; case_path = root/'case.json'
            save(case_path, {'case_id': 'W01'})
            visibility = root/'visibility.json'; save(visibility, {'certified': True})
            prepared = {'visibility_certification_path': str(visibility)}
            async def fake_solver(case, prepared, solver_out, database_url, **kwargs):
                self.assertEqual(solver_out, out/'solver')
                self.assertEqual(kwargs['environment_out'], out/'environment')
                self.assertEqual(kwargs['evaluation_inputs'], out/'evaluation/inputs')
                solver_out.mkdir(parents=True)
                kwargs['evaluation_inputs'].mkdir(parents=True)
                return {'evaluation': {}, 'termination': 'done', 'final': 'Observed answer'}
            async def fake_evaluator(*command, **kwargs):
                target = Path(command[command.index('--out')+1])
                self.assertEqual(target, out/'evaluation/assessment')
                self.assertIn('grounding.evaluation.run', command)
                save(target/'summary.json', {'validation_errors': []})
                save(target/'assessment.json', {'obligations': {}})
                return SimpleNamespace(wait=AsyncMock(return_value=0))
            with patch.object(concept_batch, 'validate_case', return_value={'errors': []}), \
                 patch.object(concept_batch.runtime, 'prepare', return_value=prepared), \
                 patch.object(concept_batch.runtime, 'run_prepared', side_effect=fake_solver), \
                 patch.object(concept_batch.asyncio, 'create_subprocess_exec', side_effect=fake_evaluator):
                result = asyncio.run(concept_batch.execute(case_path, out, 'db', 'url', lambda _: None))
            self.assertEqual(result['status'], 'completed', result)
            self.assertTrue((out/'execution_summary.json').is_file())
            self.assertTrue((out/'solver/final_response.md').is_file())
            self.assertFalse((out/'solver/oracle_input').exists())

    def test_cost_ledger_includes_new_and_legacy_solver_layouts_once(self):
        with tempfile.TemporaryDirectory() as d:
            folder = Path(d)
            for path in ('execution/old/solver/old.json', 'cases/new/solver/new.json'):
                save(folder/path, {'test_id': path, 'steps': [{'turn': 1, 'usage': {'input_tokens': 10}}]})
            save(folder/'cases/new/generation/reviewer/attempt-1/turn-01/summary.json',
                 {'status': 'returned', 'usage': {'output_tokens': 5}})
            summary = report(folder)
            self.assertEqual(summary['invocations'], 3)
            self.assertEqual(summary['by_stage']['solver']['input_tokens'], 20)
            self.assertEqual(summary['by_stage']['reviewer']['output_tokens'], 5)


if __name__ == '__main__':
    unittest.main()
