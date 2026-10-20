#!/usr/bin/env python3
"""Validate the public paper catalog, evidence views, links, and PDF-only release."""
import json
import re
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path

root = Path(__file__).resolve().parents[1]
rows = json.loads((root / 'data/papers.json').read_text())
assert rows and len({r['id'] for r in rows}) == len(rows)
assert len({r['key'] for r in rows}) == len(rows)
assert all(r['role'] in {'core', 'support', 'boundary'} for r in rows)
domains = {'direct_low_precision', 'general_TIM', 'higher_precision_comparison',
           'diagnostic_reference', 'exploration_boundary'}
for row in rows:
    assert row['title'] and row['authors'] and row['regime'] and row['replication_status']
    assert row['evidence_domain'] in domains
    assert row['publication_url'].startswith('https://')
    if re.fullmatch(r'v\d+', row['reviewed_version']):
        assert row['reviewed_source_url'] == row['arxiv_url'] + row['reviewed_version']
subprocess.run([sys.executable, str(root / 'scripts/build_tables.py'), '--check'], check=True)

evidence = json.loads((root / 'data/evidence.json').read_text())['observations']
assert len({e['key'] for e in evidence}) == len(evidence)
assert {e['key'] for e in evidence} == {r['key'] for r in rows if r['role'] == 'core'}
assert all(e['url'].startswith('https://') and e['locator'] and e['observation'] and e['limit']
           for e in evidence)

class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.targets = []
    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if (tag == 'a' and key == 'href') or (tag == 'img' and key == 'src'):
                self.targets.append(value)

for path in root.rglob('*.md'):
    text = path.read_text()
    parser = LinkParser()
    parser.feed(text)
    targets = parser.targets + re.findall(r'\]\(([^)]+)\)', text)
    for target in targets:
        if not target or target.startswith(('http:', 'https:', '#', 'mailto:')):
            continue
        assert (path.parent / target.split('#')[0]).exists(), (path, target)
for path in [root / 'README.md', root / 'data/papers.json']:
    text = path.read_text()
    assert '/Users/' not in text and 'file://' not in text, ('private path', path)

readme = (root / 'README.md').read_text().split('<!-- BEGIN GENERATED CATALOG -->')[1].split('<!-- END GENERATED CATALOG -->')[0]
for row in rows:
    title = row['title'].replace('--', '–').replace('|', '&#124;').replace('\n', ' ')
    url = row.get('reviewed_source_url') or row['publication_url']
    assert readme.count(f'[{title}]({url})') == 1, row['key']

tracked = subprocess.check_output(['git', 'ls-files', '-z'], cwd=root).decode().rstrip('\0').split('\0')
assert [p for p in tracked if p.lower().endswith('.pdf')] == ['Survey.pdf']
assert not any(Path(p).suffix.lower() in {'.tex', '.cls', '.sty', '.bib', '.bst'} for p in tracked)
assert (root / 'Survey.pdf').read_bytes().startswith(b'%PDF-')
print(f'PASS: {len(rows)} linked paper titles; {len(evidence)} evidence records; metadata, generated views, local links, and PDF-only manuscript release valid.')
