-- IDB Operations Portfolio - PostgreSQL-ready schema
-- Synthetic portfolio artifact; no OFIFC internal data.

CREATE TYPE user_status AS ENUM ('active','review_due','inactive');

CREATE TABLE app_user (
  user_id BIGSERIAL PRIMARY KEY,
  display_name TEXT NOT NULL,
  workgroup TEXT NOT NULL,
  role_code TEXT NOT NULL,
  status user_status NOT NULL DEFAULT 'active',
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE program_record (
  record_id BIGSERIAL PRIMARY KEY,
  program TEXT NOT NULL,
  reporting_period TEXT NOT NULL CHECK (reporting_period ~ '^20[0-9]{2}-Q[1-4]$'),
  completeness_score NUMERIC(5,2) CHECK (completeness_score BETWEEN 0 AND 100),
  outcome_score NUMERIC(4,2) CHECK (outcome_score BETWEEN 0 AND 10),
  created_by BIGINT REFERENCES app_user(user_id),
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE support_ticket (
  ticket_id BIGSERIAL PRIMARY KEY,
  issue TEXT NOT NULL,
  area TEXT NOT NULL,
  priority TEXT NOT NULL,
  status TEXT NOT NULL,
  opened_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  resolved_at TIMESTAMPTZ
);

CREATE TABLE audit_event (
  event_id BIGSERIAL PRIMARY KEY,
  actor_user_id BIGINT REFERENCES app_user(user_id),
  action TEXT NOT NULL,
  entity_type TEXT NOT NULL,
  entity_id TEXT,
  reason TEXT,
  event_time TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX idx_program_record_period_program ON program_record(reporting_period, program);
CREATE INDEX idx_audit_event_time ON audit_event(event_time DESC);
CREATE INDEX idx_support_ticket_status_priority ON support_ticket(status, priority);
