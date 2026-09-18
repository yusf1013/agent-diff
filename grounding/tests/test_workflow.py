"""Meaningful checks on mechanical assembly boundaries, with no model calls."""
import copy
import unittest
from grounding.archive.slack_campaign.workflow import assignments, check_design, role_handles

class WorkflowTests(unittest.TestCase):
    def test_plan_preserves_every_retained_route_once(self):
        plan=assignments()
        self.assertEqual(len(plan),174)
        self.assertEqual(len({a['route_id'] for a in plan}),174)
        for root in {a['referent_entity'] for a in plan}:
            self.assertEqual({a['resolution_mode'] for a in plan if a['referent_entity']==root},
                             {'single','multiple','absent','underspecified'})

    def test_intermediate_records_cannot_become_referents(self):
        design={'roles':[{'role':'channel','entity':'channels'}, {'role':'author','entity':'users'}],
                'obligations':[{'table':'channels','mode':'single','target_roles':['channel','author'],
                                'candidate_role_sets':None}]}
        errors=check_design(design,{'route_nodes':['CONVERSATION'],'resolution_mode':'single'})
        self.assertTrue(any('author' in e for e in errors))

    def test_missing_binding_not_silently_empty(self):
        with self.assertRaisesRegex(ValueError,'Missing role binding'):
            role_handles({}, {}, ['required'])
        self.assertEqual(role_handles({}, {'a':['U1'],'b':['U1']},['a','b']),['U1'])

if __name__=='__main__':unittest.main()
