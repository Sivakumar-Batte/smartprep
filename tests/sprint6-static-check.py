from pathlib import Path
j=Path('src/revision.js').read_text(); c=Path('src/revision.css').read_text(); h=Path('revision.html').read_text()
for x in ['FAILED','DIFFICULT','PARTIAL','EASY','RELEARN','revisionResults','dailyLimit','Export revision backup']:
 assert x in j,x
assert 'thead th{position:sticky;top:0' in c
assert 'Adaptive Revision Engine' in h
print('Sprint 6 static checks passed')
