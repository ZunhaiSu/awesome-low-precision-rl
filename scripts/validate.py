#!/usr/bin/env python3
"""Validate the public paper catalog, evidence views, links, and PDF-only release."""
import json
import hashlib
import re
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote

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
        assert (path.parent / unquote(target.split('#')[0])).exists(), (path, target)
for path in [root / 'README.md', root / 'data/papers.json']:
    text = path.read_text()
    assert '/Users/' not in text and 'file://' not in text, ('private path', path)

readme = (root / 'README.md').read_text().split('<!-- BEGIN GENERATED CATALOG -->')[1].split('<!-- END GENERATED CATALOG -->')[0]
for row in rows:
    title = row['title'].replace('--', '–').replace('|', '&#124;').replace('\n', ' ')
    url = row.get('reviewed_source_url') or row['publication_url']
    assert readme.count(f'[{title}]({url})') == 1, row['key']

tracked = subprocess.check_output(['git', 'ls-files', '-z'], cwd=root).decode().rstrip('\0').split('\0')
library = json.loads((root / 'papers/manifest.json').read_text())
entries = library['papers']
by_key = {r['key']: r for r in rows}
assert len(entries) == len(rows) and {e['key'] for e in entries} == set(by_key)
assert len({e['path'] for e in entries}) == len(entries)
mirrors = set()
for tier, count in [('main', 13), ('related', 16)]:
    group = [e for e in entries if e['reading_tier'] == tier]
    assert len(group) == count
    assert sorted(e['reading_number'] for e in group) == list(range(1, count + 1))
    assert [e['first_publication'] for e in sorted(group, key=lambda e: e['reading_number'])] == sorted(e['first_publication'] for e in group)
for entry in entries:
    paper = by_key[entry['key']]
    for field in ['title', 'authors', 'first_publication', 'reviewed_version']:
        assert entry[field] == paper[field], (entry['key'], field)
    assert entry['source_url'] == paper['reviewed_source_url']
    assert entry['official_pdf_url'].startswith('https://')
    path = root / entry['path']
    assert path.is_relative_to(root / 'papers') and '..' not in path.parts
    assert path.is_file() and entry['reading_scope'] and entry['reading_focus']
    assert entry['license']['evidence_url'] == entry['source_url']
    if entry['distribution'] == 'mirror':
        assert entry['pdf_path'] == entry['path'] and path.suffix == '.pdf'
        assert entry['license']['redistribution_verified'] is True
        assert entry['license']['url'].startswith('https://creativecommons.org/')
        assert path.read_bytes().startswith(b'%PDF-')
        assert hashlib.sha256(path.read_bytes()).hexdigest() == entry['source_pdf_sha256']
        mirrors.add(entry['path'])
    else:
        assert entry['distribution'] == 'official_link' and entry['pdf_path'] is None
        assert not entry['license']['redistribution_verified'] and path.suffix == '.md'
        assert entry['official_pdf_url'] in path.read_text()
assert len(mirrors) == library['counts']['pdf_mirrors'] == 11
assert len(entries) - len(mirrors) == library['counts']['official_links'] == 18
assert set(p for p in tracked if p.lower().endswith('.pdf')) == {'Survey.pdf'} | mirrors
assert not any(Path(p).suffix.lower() in {'.tex', '.cls', '.sty', '.bib', '.bst'} for p in tracked)
assert (root / 'Survey.pdf').read_bytes().startswith(b'%PDF-')
comparison_data=json.loads((root/'data/comparisons.json').read_text())
by_key={r['key']:r for r in rows}
assert comparison_data['literature_snapshot']=='2026-10-20'
assert len({r['key'] for r in comparison_data['regimes']})==len(comparison_data['regimes'])
assert len({r['id'] for r in comparison_data['comparisons']})==len(comparison_data['comparisons'])
for item in comparison_data['regimes']:
 assert item['key'] in by_key and item['url']==by_key[item['key']]['reviewed_source_url']
 assert all(item.get(f) for f in ['learner','rollout','collection','boundary','locator'])
for item in comparison_data['comparisons']:
 assert item['study_key'] in by_key and item['url']==by_key[item['study_key']]['reviewed_source_url']
 assert all(item.get(f) for f in ['setting','compared','outcome','checkpoint_rule','limit','locator'])


measurement_data=json.loads((root/'data/measurements.json').read_text())
measurements=measurement_data['records']
assert measurement_data['literature_snapshot']=='2026-10-20'
assert len(measurements)==len({m['key'] for m in measurements})==19
assert {m['key'] for m in measurements}=={r['key'] for r in rows if r['role']=='core'}
for item in measurements:
 assert item['url']==by_key[item['key']]['reviewed_source_url']
 assert item['title']==by_key[item['key']]['title']
 assert item['reviewed_version']==by_key[item['key']]['reviewed_version']
 assert all(item.get(f) for f in ['family','locator','measure','comparison','interpretation_limit'])
 assert item['title'] in (root/'docs/MEASUREMENTS.md').read_text()


# Keep repository and preferred-citation author records aligned with the manuscript.
cff=(root/'CITATION.cff').read_text()
authors=re.findall(r'family-names: "([^"\n]+)"\n\s+given-names: "([^"\n]+)"\n\s+affiliation: "([^"\n]+)"',cff)
expected_authors=[('Su','Zunhai','The University of Hong Kong'),('Wu','Wei','Meituan'),('Zhang','Yifan','Meituan'),('Tan','Jianchao','Meituan'),('Wong','Ngai','The University of Hong Kong')]
assert authors==expected_authors*2,'citation author/affiliation mismatch'

print(f'PASS: {len(rows)} linked titles; {len(evidence)} evidence records; 13 mainline / 16 related entries; {len(mirrors)} licensed PDF hashes; links and PDF-only survey release valid.')

# Timeline claims remain bound to paper metadata and recorded affiliation sources.
timeline=json.loads((root/'data/timeline.json').read_text())
canonical={p['key']:p for p in rows}
assert len({m['key'] for m in timeline['milestones']})==len(timeline['milestones'])
for m in timeline['milestones']:
 p=canonical[m['key']]
 assert m['title']==p['title'] and m['first_publication']==p['first_publication']
 assert m['source']==p['reviewed_source_url'] and m['source_locator']
 assert set(re.findall(r'[AB][12]',m['components']))==set(re.findall(r'[AB][12]',p['categories']))
 assert len(m['affiliations'])==len(set(m['affiliations']))
 assert m['displayed_marks']==m['affiliations'][:3]
 assert all(k in timeline['institutions'] for k in m['affiliations'])
for x in timeline['institutions'].values():
 assert x['name'] and x['short_name'] and x['asset_source'].startswith('https://')
assert (root/'figures/timeline.svg').is_file()
print(f"PASS: {len(timeline['milestones'])} source-bound timeline milestones; all affiliations retained; mark cap valid.")
