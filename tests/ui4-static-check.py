from pathlib import Path
c=Path('src/ui4-unified.css').read_text(); j=Path('src/ui4-shell.js').read_text()
for x in ['practice.html','revision.html','queue.html','analytics.html','cloud.html','index.html','focus.html','app.html']: assert x in j
for x in ['thead th{position:sticky;top:0','prefers-reduced-motion','data-theme','sp-mobile']: assert x in c or x in j
assert 'service_role' not in j
print('UI Sprint 4 static checks passed')
