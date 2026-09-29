from pathlib import Path
app=Path('src/app.js').read_text(); css=Path('src/styles.css').read_text(); html=Path('index.html').read_text()
for x in ['localStorage','attempts:[]','errors:[]','revisionEvents:[]','studySessions:[]','exportData']:
    assert x in app, x
assert 'thead th{position:sticky;top:0' in css
assert 'My study data' in html
print('Sprint 4 static checks passed')
