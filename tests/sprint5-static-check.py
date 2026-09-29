from pathlib import Path
j=Path('src/practice.js').read_text(); c=Path('src/practice.css').read_text(); h=Path('practice.html').read_text()
for x in ["['V2','V3'].includes",'questionText','finalAnswer','negativeMark','ERROR_RETEST','Insufficient','Provisional','Reliable']:
    assert x in j,x
assert 'thead th{position:sticky;top:0' in c
assert 'Practice & Diagnostic Engine' in h
print('Sprint 5 static checks passed')
