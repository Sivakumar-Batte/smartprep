from pathlib import Path
h=Path('app.html').read_text(); j=Path('src/ui2.js').read_text(); c=Path('src/ui2.css').read_text()
for x in ['queue.html','practice.html','revision.html','analytics.html','cloud.html','index.html']: assert x in j or x in h
for x in ['smartprep.personal.v1','focusedMinutes','revisionResults','No activity yet']: assert x in j
for x in ['@media(max-width:650px)','bottom','data-theme']: assert x in c or x in h
print('UI Sprint 2 static checks passed')
