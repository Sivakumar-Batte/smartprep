from pathlib import Path
j=Path('src/queue.js').read_text(); h=Path('queue.html').read_text(); c=Path('src/queue.css').read_text()
for x in ['revision:35','error:25','weakness:25','evidence:10','inactivity:5','Not yet practised','not exam forecasts']:
 assert x in j or x in h,x
assert 'thead th{position:sticky;top:0' in c
print('Sprint 7 static checks passed')
