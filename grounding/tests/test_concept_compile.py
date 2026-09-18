"""Checks at the model-to-executable boundary; no model or network calls."""
from copy import deepcopy
import unittest

from grounding.generation.concept_compile import (check_compilation, packet_for, ROOT, parse_sketch,
                              compiler_message, reviewer_message, mode_instructions,
                              system_prompt)
from grounding.generation.concept_writer import assignments
from grounding.generation.route_contract import build
from grounding.tests.test_validation import case_fixture


def fixture():
    source=case_fixture()
    packet={'assignment':{'case_id':'compile_test','resolution_mode':'single','match_count':1},
            'acting_user_id':'UA',
            'native_route':build(['MESSAGE','REACTION','USER','CONVERSATION_MEMBERSHIP','CONVERSATION']),
            'sketch':{'request':source['prompt'],'selection_conditions':'Rollout message reacted to by a security member.',
                      'rows':[{'row':1,'role':'match'},{'row':2,'role':'negative'}]}}
    compiled={'seed':source['seed'],'selector':source['private']['selector'],
              'row_bindings':[{'row':1,'referent':'1712345678.000001','support':[]},
                              {'row':2,'referent':'1712345678.000002','support':[]}],
              'annotation':{'name':'Security rollout message','scope':'All supplied messages',
                            'task_type':'state-changing','computation_attributes':[['messages.message_id']],
                            'written_attributes':['message_reactions.message_id','message_reactions.reaction_type']}}
    return packet,compiled


class CompilationTests(unittest.TestCase):
    def test_compiler_and_reviewer_receive_only_assigned_mode_instructions(self):
        shared = {review: system_prompt(review) for review in (False, True)}
        for a in assignments():
            packet = {'assignment': a}
            for review in (False, True):
                message = (reviewer_message(packet, {}, {}, {}) if review
                           else compiler_message(packet))
                full = shared[review] + message
                for mode in ('single', 'multiple', 'absent', 'underspecified'):
                    self.assertEqual(f'The assigned mode is {mode.upper()}.' in full,
                                     mode == a['resolution_mode'])
                self.assertEqual('singular request with these unresolved' in full,
                                 a['resolution_mode'] == 'underspecified')
                self.assertEqual("requested target's absence is" in full,
                                 a['resolution_mode'] == 'absent')
                self.assertNotIn('{match_count}', full)
                self.assertNotIn('{alternative_count}', full)
                if a['resolution_mode'] in ('single', 'multiple'):
                    self.assertIn(f"exactly\n{a['match_count']}", message)
                elif a['resolution_mode'] == 'underspecified':
                    self.assertIn(f"exactly\n{a['alternative_count']} competing", message)
        for text in shared.values():
            self.assertNotIn('The assigned mode is', text)
            self.assertNotIn('For underspecified,', text)

    def test_mode_instructions_reject_unknown_or_missing_assignment_values(self):
        with self.assertRaises(ValueError):
            mode_instructions({'resolution_mode': 'invented'})
        with self.assertRaises(KeyError):
            mode_instructions({'resolution_mode': 'multiple'})

    def test_existing_sketches_extract_final_conditions_and_counts(self):
        for i in range(1,11):
            packet=packet_for(ROOT/'grounding/runs/slack_campaign/writer_pilot_04',f'W{i:02}')
            self.assertTrue(packet['sketch']['request'])
            self.assertTrue(packet['sketch']['selection_conditions'])
        self.assertIn('public channel',packet_for(ROOT/'grounding/runs/slack_campaign/writer_pilot_04','W05')['sketch']['selection_conditions'])

    def test_assembly_uses_locked_source_and_computed_set(self):
        packet,compiled=fixture()
        case,checks=check_compilation(packet,compiled)
        self.assertEqual(checks['errors'],[])
        self.assertEqual(case['prompt'],packet['sketch']['request'])
        self.assertEqual(case['cards'][0]['Referent set'],['1712345678.000001'])

    def test_full_assigned_route_can_extend_for_another_stated_condition(self):
        packet,compiled=fixture()
        packet['native_route']=build(['MESSAGE','REACTION','USER'])
        case,checks=check_compilation(packet,compiled)
        self.assertEqual(checks['errors'],[])
        self.assertEqual(case['cards'][0]['Identifying paths'][0]['entities'],
                         ['messages','message_reactions','users','channel_members','channels'])

    def test_assigned_route_cannot_be_shortened(self):
        packet,compiled=fixture()
        compiled['selector']['focal']['path']=compiled['selector']['focal']['path'][:3]
        compiled['selector']['focal']['joins']=compiled['selector']['focal']['joins'][:2]
        _,checks=check_compilation(packet,compiled)
        self.assertTrue(any('assigned full route' in e for e in checks['errors']))

    def test_absence_retains_negatives_but_has_empty_referent_set(self):
        packet,compiled=fixture()
        packet['assignment'].update(resolution_mode='absent',match_count=0)
        for row in packet['sketch']['rows']: row['role']='negative'
        for row in compiled['seed']['messages']: row['message_text']='Office lunch'
        case,checks=check_compilation(packet,compiled)
        self.assertEqual(checks['errors'],[])
        self.assertEqual(case['cards'][0]['Resolution'],'absent')
        self.assertEqual(case['cards'][0]['Referent set'],[])

    def test_underspecified_preserves_two_competing_singleton_sets(self):
        packet,compiled=fixture()
        packet['assignment'].update(resolution_mode='underspecified',match_count=None)
        for row in packet['sketch']['rows']: row['role']='alternative'
        compiled['seed']['channel_members'].append({'channel_id':'CS','user_id':'U2'})
        packet['sketch']['rows'].append({'row':3,'role':'negative'})
        compiled['row_bindings'].append({'row':3,'referent':'1712345678.000003','support':[]})
        case,checks=check_compilation(packet,compiled)
        self.assertEqual(checks['errors'],[])
        card=case['cards'][0]
        self.assertEqual(card['Resolution'],'underspecified')
        self.assertIsNone(card['Alternative sufficient identifying sets'])
        self.assertEqual(card['Referent set']['candidate_sets'],
                         [['1712345678.000001'],['1712345678.000002']])

    def test_filler_introducing_extra_match_fails(self):
        packet,compiled=fixture()
        compiled['seed']['messages'][2]['message_text']='Another rollout checklist'
        _,checks=check_compilation(packet,compiled)
        self.assertTrue(any('recomputed matches' in e for e in checks['errors']))

    def test_same_count_wrong_set_fails(self):
        packet,compiled=fixture()
        compiled['seed']['messages'][0]['message_text']='Office lunch'
        compiled['seed']['messages'][2]['message_text']='Rollout plan'
        _,checks=check_compilation(packet,compiled)
        self.assertEqual(len(checks['computed_matches']),1)
        self.assertTrue(any('recomputed matches' in e for e in checks['errors']))

    def test_selector_cannot_be_narrowed_to_force_pass(self):
        packet,compiled=fixture(); locked=deepcopy(compiled['selector'])
        compiled['selector']['scope']=[{'field':'message_id','op':'eq','value':'1712345678.000001'}]
        _,checks=check_compilation(packet,compiled,locked)
        self.assertTrue(any('Selector changed' in e for e in checks['errors']))

    def test_model_cannot_relabel_story_or_bind_two_rows_to_one_root(self):
        packet,compiled=fixture()
        compiled['row_bindings'][1]['referent']=compiled['row_bindings'][0]['referent']
        _,checks=check_compilation(packet,compiled)
        self.assertTrue(any('same root' in e for e in checks['errors']))

    def test_missing_required_row_and_invented_support_are_rejected(self):
        packet,compiled=fixture(); omitted=deepcopy(compiled)
        omitted['row_bindings'].pop()
        self.assertTrue(check_compilation(packet,omitted)[1]['errors'])
        compiled['row_bindings'][0]['support']=[{'table':'users','handle':'invented'}]
        self.assertTrue(any('does not exist' in e for e in check_compilation(packet,compiled)[1]['errors']))

    def test_null_negative_cannot_hide_a_root_in_its_support(self):
        packet,compiled=fixture()
        compiled['row_bindings'][1]={'row':2,'referent':None,
            'support':[{'table':'messages','handle':'1712345678.000002'}]}
        _,checks=check_compilation(packet,compiled)
        self.assertTrue(any('null referent contradicts' in e for e in checks['errors']))


if __name__=='__main__':unittest.main()
