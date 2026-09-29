from pathlib import Path
j=Path('src/analytics.js').read_text(); c=Path('src/analytics.css').read_text(); h=Path('analytics.html').read_text()
for x in ['masteryAttempts','masteryAccuracy','conceptCoverage','focusedMinutes','not exam-result predictions']:
 assert x in j or x in h,x
assert 'thead th{position:sticky;top:0' in c
print('Sprint 8 static checks passed')
