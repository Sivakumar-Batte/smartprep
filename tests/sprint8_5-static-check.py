from pathlib import Path
j=Path('src/cloud.js').read_text(); s=Path('supabase/sprint8_5_sync_upgrade.sql').read_text()
for x in ['signInWithPassword','signUp','resetPasswordForEmail','upsert','Safe two-way sync','payload']:
 assert x in j or x in Path('cloud.html').read_text(),x
for x in ['with check (auth.uid() = user_id)','client_id','unique index']:
 assert x in s.lower(),x
print('Sprint 8.5 static checks passed')
