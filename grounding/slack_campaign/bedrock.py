"""Small recorded native Bedrock conversation; no tools or hidden retry loop."""
from __future__ import annotations

import copy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import time

import boto3
from botocore.config import Config


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + '.tmp')
    temp.write_text(json.dumps(value, indent=2, ensure_ascii=False, default=str) + '\n')
    temp.replace(path)


def parse_json(text):
    text = text.strip()
    fence = re.fullmatch(r'```(?:json)?\s*\n(.*?)\n```', text, re.S)
    if fence:
        return json.loads(fence.group(1))
    blocks = list(re.finditer(r'```(?:json)?\s*\n(.*?)\n```', text, re.S))
    if len(blocks) == 1:
        # A single explicitly delimited object has no answer-selection ambiguity.
        # Preserve the original prose and fence in answer.txt for audit.
        return json.loads(blocks[0].group(1))
    return json.loads(text)


class Conversation:
    def __init__(self, folder, system, *, model='us.anthropic.claude-sonnet-5',
                 region='us-west-1', effort='medium', max_tokens=24000,
                 output_format='json', cache_system=False):
        """Record one conversation, optionally returning plain Markdown/text.

        With cache_system=True, ``system`` must be the shared static prefix;
        put case-specific information in ask(). Native usage records show
        whether that prefix actually meets the model's caching minimum.
        """
        if output_format not in ('json', 'text', 'markdown'):
            raise ValueError('output_format must be json, text, or markdown')
        self.folder = Path(folder)
        self.folder.mkdir(parents=True, exist_ok=False)
        self.model, self.region = model, region
        self.output_format = output_format
        # Native InvokeModel explicit caching, default five-minute TTL:
        # https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html
        system_blocks = ([{'type': 'text', 'text': system,
                           'cache_control': {'type': 'ephemeral'}}]
                         if cache_system else system)
        self.body = {'anthropic_version': 'bedrock-2023-05-31', 'max_tokens': max_tokens,
                     'thinking': {'type': 'adaptive', 'display': 'summarized'},
                     'output_config': {'effort': effort}, 'system': system_blocks, 'messages': []}
        self.turn = 0
        (self.folder / 'instructions.md').write_text(system)

    @classmethod
    def resume(cls, folder):
        """Continue saved native history, including untouched thinking signatures."""
        obj = cls.__new__(cls)
        obj.folder = Path(folder)
        turns = sorted(obj.folder.glob('turn-*/request.json'))
        if not turns:
            raise ValueError('No saved conversation to resume')
        last = turns[-1].parent
        info = json.loads((last / 'summary.json').read_text())
        response = json.loads((last / 'response.json').read_text())
        if response.get('stop_reason') != 'end_turn':
            raise ValueError('Cannot repair incomplete model output')
        obj.body = json.loads((last / 'request.json').read_text())
        obj.body['messages'].append({'role': 'assistant', 'content': response['content']})
        obj.model, obj.region = info['model'], info['region']
        obj.turn = info['turn']
        # Historical conversations predate explicit output-format provenance.
        obj.output_format = info.get('output_format', 'json')
        return obj

    def ask(self, message):
        self.turn += 1
        out = self.folder / f'turn-{self.turn:02d}'
        out.mkdir()
        self.body['messages'].append({'role': 'user', 'content': [{'type': 'text', 'text': message}]})
        body = copy.deepcopy(self.body)
        save(out / 'request.json', body)
        summary = {'started_utc': datetime.now(timezone.utc).isoformat(), 'model': self.model,
                   'region': self.region, 'turn': self.turn, 'status': 'running',
                   'output_format': self.output_format,
                   'request_sha256': hashlib.sha256(json.dumps(body).encode()).hexdigest(),
                   'usage': None, 'cost_usd': None,
                   'cost_note': 'Native token usage; Bedrock supplies no dollar figure.',
                   'output_directory': str(out.resolve())}
        save(out / 'summary.json', summary)
        started = time.monotonic()
        parsed = None
        try:
            client = boto3.client('bedrock-runtime', region_name=self.region,
                                  config=Config(read_timeout=600, connect_timeout=15,
                                                retries={'total_max_attempts': 1}))
            response = client.invoke_model(modelId=self.model, contentType='application/json',
                                           accept='application/json', body=json.dumps(body))
            raw = json.loads(response['body'].read())
            save(out / 'response.json', raw)
            save(out / 'response_metadata.json', response['ResponseMetadata'])
            summary.update(usage=raw.get('usage'), stop_reason=raw.get('stop_reason'),
                           status='returned' if raw.get('stop_reason') == 'end_turn' else 'incomplete')
            blocks = raw.get('content', [])
            text = '\n'.join(b['text'] for b in blocks if b.get('type') == 'text')
            thinking = [b for b in blocks if b.get('type') in ('thinking', 'redacted_thinking')]
            (out / 'answer.txt').write_text(text)
            (out / 'thinking.txt').write_text('\n\n'.join(b.get('thinking', '') for b in thinking))
            save(out / 'thinking_blocks.json', thinking)
            self.body['messages'].append({'role': 'assistant', 'content': copy.deepcopy(blocks)})
            save(out / 'conversation.json', self.body['messages'])
            if summary['status'] != 'returned':
                raise RuntimeError('Incomplete model response: ' + str(raw.get('stop_reason')))
            if self.output_format == 'json':
                try:
                    parsed = parse_json(text)
                    save(out / 'output.json', parsed)
                except ValueError as exc:
                    summary['parse_error'] = str(exc)
            else:
                parsed = text
                (out / 'output.md').write_text(text)
        except Exception as exc:
            summary['status'] = 'error' if summary['status'] == 'running' else summary['status']
            summary['error'] = f'{type(exc).__name__}: {exc}'
            if hasattr(exc, 'response'):
                save(out / 'api_error.json', exc.response)
        finally:
            summary['elapsed_seconds'] = round(time.monotonic() - started, 3)
            save(out / 'summary.json', summary)
        if parsed is None:
            kind = 'JSON' if self.output_format == 'json' else 'text'
            raise RuntimeError(f'No complete {kind} at {out}: ' + str(summary.get('error', summary.get('parse_error'))))
        return parsed
