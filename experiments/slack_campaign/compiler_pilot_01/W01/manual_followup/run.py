"""One explicitly manual development intervention, continuing compiler history.

Not part of the automatic acceptance rate. Run from the repository root with
the campaign Python environment; original automatic artifacts remain preserved.
"""
from pathlib import Path

from grounding.slack_campaign.bedrock import Conversation, save
from grounding.slack_campaign.concept_compile import check_compilation, system_prompt
from grounding.slack_campaign.generate import read, dump
from grounding.slack_campaign.usage import report

out = Path(__file__).resolve().parent.parent
save(out / 'automatic_summary.json', read(out / 'summary.json'))
result = {'status': 'manual_repair_running', 'manual_intervention': True}
try:
    compiler = Conversation.resume(out / 'compiler')
    if compiler.turn != 2:
        raise ValueError('This recorded intervention is only for the two-turn pilot')
    compiled = compiler.ask((out / 'manual_followup/feedback.txt').read_text())
    save(out / 'compiled-3.json', compiled)
    previous = read(out / 'compiled-2.json')
    for field in ('seed', 'row_bindings', 'selector'):
        if compiled.get(field) != previous[field]:
            raise ValueError('Manual annotation repair changed ' + field)
    packet = read(out / 'input.json')
    case, checks = check_compilation(packet, compiled, read(out / 'locked_selector.json'))
    save(out / 'checks-3.json', checks)
    if checks['errors']:
        raise ValueError(str(checks['errors']))
    save(out / 'case-3.json', case)
    reviewer = Conversation(out / 'reviews/attempt-3/reviewer', system_prompt(True),
                            cache_system=True, max_tokens=5000)
    review = reviewer.ask(dump({'source': packet, 'compilation': compiled,
                               'case': case, 'mechanical_checks': checks}))
    save(out / 'review-3.json', review)
    if review.get('validity') != 'pass' or any(i['kind'] == 'validity' for i in review['issues']):
        raise ValueError('Independent review did not pass')
    save(out / 'case.json', case)
    result = {'status': 'review_pass_after_manual_annotation_feedback',
              'manual_intervention': True, 'compiler_attempts': 3, 'reviewer_calls': 2,
              'quality': review['quality'], 'computed_matches': checks['computed_matches'],
              'preserved': ['request', 'seed', 'row_bindings', 'selector'],
              'automatic_result': 'automatic_summary.json'}
except Exception as exc:
    result.update(status='manual_repair_failed', error=str(exc))
    raise
finally:
    save(out / 'summary.json', result)
    report(out)
