from pathlib import Path
h=Path('ui.html').read_text(); c=Path('src/modern-ui.css').read_text(); j=Path('src/modern-ui.js').read_text()
for x in ['queue.html','practice.html','revision.html','analytics.html','cloud.html','index.html']: assert x in h
for x in ['bottom-nav','data-theme','@media(max-width:650px)']: assert x in c
for x in ['smartprep.personal.v1','revisionResults','focusedMinutes']: assert x in j
print('Modern UI static checks passed')
