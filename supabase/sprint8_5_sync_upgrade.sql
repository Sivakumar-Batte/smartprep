-- SmartPrep Sprint 8.5 sync upgrade. Run once in Supabase SQL Editor.
-- Adds lossless JSON payloads and stable client IDs to the existing tables.
create extension if not exists pgcrypto;

alter table public.attempts add column if not exists client_id text;
alter table public.attempts add column if not exists payload jsonb not null default '{}'::jsonb;
alter table public.attempts add column if not exists updated_at timestamptz not null default now();
alter table public.errors add column if not exists client_id text;
alter table public.errors add column if not exists payload jsonb not null default '{}'::jsonb;
alter table public.errors add column if not exists updated_at timestamptz not null default now();
alter table public.revision_events add column if not exists client_id text;
alter table public.revision_events add column if not exists payload jsonb not null default '{}'::jsonb;
alter table public.revision_events add column if not exists updated_at timestamptz not null default now();
alter table public.revision_results add column if not exists client_id text;
alter table public.revision_results add column if not exists payload jsonb not null default '{}'::jsonb;
alter table public.revision_results add column if not exists updated_at timestamptz not null default now();
alter table public.study_sessions add column if not exists client_id text;
alter table public.study_sessions add column if not exists payload jsonb not null default '{}'::jsonb;
alter table public.study_sessions add column if not exists updated_at timestamptz not null default now();
alter table public.test_sessions add column if not exists client_id text;
alter table public.test_sessions add column if not exists payload jsonb not null default '{}'::jsonb;
alter table public.test_sessions add column if not exists updated_at timestamptz not null default now();
alter table public.user_settings add column if not exists payload jsonb not null default '{}'::jsonb;

create unique index if not exists attempts_user_client_uidx on public.attempts(user_id,client_id);
create unique index if not exists errors_user_client_uidx on public.errors(user_id,client_id);
create unique index if not exists revision_events_user_client_uidx on public.revision_events(user_id,client_id);
create unique index if not exists revision_results_user_client_uidx on public.revision_results(user_id,client_id);
create unique index if not exists study_sessions_user_client_uidx on public.study_sessions(user_id,client_id);
create unique index if not exists test_sessions_user_client_uidx on public.test_sessions(user_id,client_id);

-- Ensure RLS is enabled and authenticated users can only access their own rows.
alter table public.attempts enable row level security;
alter table public.errors enable row level security;
alter table public.revision_events enable row level security;
alter table public.revision_results enable row level security;
alter table public.study_sessions enable row level security;
alter table public.test_sessions enable row level security;
alter table public.user_settings enable row level security;

do $$ declare t text; begin
  foreach t in array array['attempts','errors','revision_events','revision_results','study_sessions','test_sessions','user_settings'] loop
    execute format('drop policy if exists "smartprep own rows" on public.%I',t);
    execute format('create policy "smartprep own rows" on public.%I for all to authenticated using (auth.uid() = user_id) with check (auth.uid() = user_id)',t);
  end loop;
end $$;
