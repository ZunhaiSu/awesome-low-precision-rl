#!/usr/bin/env python3
"""Check the portable catalog, manuscript references, template, and local links."""
import json,re,sys
from collections import Counter
from pathlib import Path
root=Path(__file__).resolve().parents[1]
rows=json.loads((root/'data/papers.json').read_text())
s=(root/'survey/survey.tex').read_text();body=s.split('\\begin{document}',1)[1]
assert len(rows)==20 and len({r['id'] for r in rows})==20
assert Counter(r['role'] for r in rows)=={'core':13,'support':6,'boundary':1}
assert all(r['title'] and r['authors'] and r['publication_url'].startswith('https://') for r in rows)
keys=set(re.findall(r'\\bibitem\{([^}]+)\}',s))
cites={key.strip() for group in re.findall(r'\\cite\w*(?:\[[^\]]*\])*\{([^}]+)\}',body) for key in group.split(',')}
assert cites<=keys,('undefined citations',cites-keys)
assert {r['key'] for r in rows}<=cites
bibkeys=set(re.findall(r'@\w+\{([^,]+),',(root/'references.bib').read_text()))
assert keys==bibkeys,('bibliography mismatch',keys^bibkeys)
labels=re.findall(r'\\label\{([^}]+)\}',body)
assert len(labels)==len(set(labels))
refs=set(re.findall(r'\\(?:eqref|ref)\{([^}]+)\}',body))
assert refs<=set(labels),('undefined labels',refs-set(labels))
embedded=s.split('\\begin{filecontents*}{mystyle.cls}\n',1)[1].split('\n\\end{filecontents*}',1)[0]
assert embedded==(root/'survey/mystyle.cls').read_text()
assert len(re.findall(r'^\\section\{',body.split('\\appendix',1)[0],re.M))==8
for path in root.rglob('*.md'):
 text=path.read_text()
 for target in re.findall(r'<img[^>]+src="([^"]+)"',text):
  if not target.startswith(('http:','https:')):assert (path.parent/target).exists(),(path,target)
 for target in re.findall(r'\]\(([^)]+)\)',text):
  if target.startswith(('http:','https:','#','mailto:')):continue
  assert (path.parent/target.split('#')[0]).exists(),(path,target)
for path in [root/'README.md',root/'data/papers.json',root/'references.bib']:
 text=path.read_text()
 assert '/Users/' not in text and 'file://' not in text,('private path',path)
assert not re.search(r'(?m)^\s*\\(?:input|include)\{',body),'unexpected external TeX input'
# Verify discussion-location metadata against actual citations in main-text subsections.
main=body.split('\\appendix',1)[0]
sec=sub=0
locations={}
for line in main.splitlines():
 if line.startswith('\\section{'):sec+=1;sub=0
 if line.startswith('\\subsection{'):sub+=1
 for group in re.findall(r'\\cite\w*(?:\[[^\]]*\])*\{([^}]+)\}',line):
  for key in group.split(','):locations.setdefault(key.strip(),set()).add(f'{sec}.{sub}')
for row in rows:
 expected=[row['primary_section']] + [x.strip() for x in row['secondary_sections'].split(';') if x.strip()]
 for loc in expected:
  if loc=='Box 1':
   assert row['key']=='qerl' and '3.4' in locations.get(row['key'],set())
  else:
   assert loc in locations.get(row['key'],set()),('section mapping',row['key'],loc)
evidence=json.loads((root/'data/evidence.json').read_text())['observations']
assert len({e['key'] for e in evidence})==len(evidence)
assert {e['key'] for e in evidence}=={r['key'] for r in rows if r['role']=='core'},'missing core evidence record'
assert all(e['url'].startswith('https://') and e['locator'] and e['observation'] and e['limit'] for e in evidence)
assert re.findall(r'(?m)^\\author(?:\[[^\]]*\])?\{([^}]+)\}',s)==['Zunhai Su']
assert re.findall(r'(?m)^\\affil(?:\[[^\]]*\])?\{([^}]+)\}',s)==['The University of Hong Kong']
figures=re.findall(r'\\begin\{figure\}',body)
markers=re.findall(r'% BEGIN FIGURE ([a-z_]+)',body)
assert len(figures)==len(markers)
assert len(markers)==len(set(markers))
assert all((root/'figures'/f'{name}.svg').exists() for name in markers),'missing figure export'
assert body.count('\\tableofcontents')==1
assert body.index('\\label{fig:overview}')<body.index('\\tableofcontents')<body.index('\\section{Introduction')<body.index('\\section{Problem Formulation')
assert (root/'Survey.pdf').read_bytes()==(root/'survey/survey.pdf').read_bytes(),'root PDF differs from manuscript PDF'
print(f'PASS: {len(rows)} focal papers; {len(keys)} references; 8 main sections; {len(figures)} figures; {len(evidence)} evidence records; citations, labels, locations, template and local links valid.')
