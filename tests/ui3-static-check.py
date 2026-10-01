from pathlib import Path
h=Path('focus.html').read_text(); j=Path('src/ui3.js').read_text(); c=Path('src/ui3-shared.css').read_text()
for x in ['practice.html','revision.html','queue.html','analytics.html','cloud.html']: assert x in h or x in j
for x in ['smartprep.personal.v1','smartprep.focus.v1','setInterval','localStorage']: assert x in j
assert 'thead th{position:sticky;top:0' in c
assert 'prefers-reduced-motion' in c
print('UI Sprint 3 static checks passed')
