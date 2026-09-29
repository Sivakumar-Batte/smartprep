from pathlib import Path
css=Path('src/styles.css').read_text(); app=Path('src/app.js').read_text(); html=Path('index.html').read_text()
assert 'thead th{position:sticky;top:0;background:#e6f2ef;z-index:2}' in css
assert 'breadcrumb' in html and 'qClear' in app and 'cClear' in app
print('Sprint 3 static checks passed')
