# IDB Operations Portfolio - Junjun Hu (William)

**Live demo:** https://ofifc-idb-portfolio.vercel.app

Independent portfolio work built around the public OFIFC database-administration job description. This project is **not affiliated with OFIFC** and uses only synthetic demonstration data.

## What the live demo now supports

### 1) IDB Admin Console
- User CRUD and account status administration
- Four demo roles: Administrator, Analyst, Support and Viewer
- Permission-gated actions using an RBAC matrix
- Database health and performance indicators
- SQL-style reporting query workflow
- Controlled CSV exports
- Access-review workflow
- Release-test and backup/recovery controls
- Action audit trail

### 2) Program Data & Reporting
- Program-record CRUD
- Required-field/range/reporting-period validation
- Data-quality dashboard and exception queue
- Cross-program aggregation
- Dynamic descriptive statistics comparable to an SPSS/Python workflow
- Governed CSV exports

### 3) IDB Support & Training
- Support-ticket creation and resolution
- SLA and recurring-issue analysis
- Role-specific training resources
- Contractor development milestone tracking
- Senior-management briefing view

### 4) Governance & Audit
- Visible RBAC matrix
- Timestamped action history
- Audit-log CSV export
- Administration procedures and release controls

## PostgreSQL design

`database/schema.sql` contains a PostgreSQL-ready relational design for:
- `app_user`
- `program_record`
- `support_ticket`
- `audit_event`

It includes primary/foreign keys, validation constraints and reporting/audit indexes.

## JD mapping

| Public posting responsibility | Portfolio evidence |
|---|---|
| Database system administration and functionality | Admin Console + PostgreSQL schema |
| Analyze/document requirements and user needs | RBAC, validation and support workflows |
| Monitor system performance / secure access | Health view + role/access controls |
| Recommendations for system improvement | Performance recommendations and release view |
| Development testing | `docs/TEST_PLAN.md` + release test workflow |
| Manage IDB users and roles | User CRUD + RBAC + access review |
| Administration procedures and controls | Governance/Audit module |
| Report writing, queries and exports | Query workflow + CSV exports |
| Statistical software / analysis | Dynamic descriptive statistics |
| Front-end user support | Support queue + recurring issue analysis |
| Liaise across workgroups | Program/workgroup views |
| Briefings and status reports | Management briefing view |
| Monitor development projects / contractor liaison | Development milestone tracker |
| Training plans, tools and resources | Role-specific training plan |

## Source structure
- `index.html` - portfolio/module entry point
- `idb-admin-console/` - database administration prototype
- `program-data-reporting/` - reporting/quality prototype
- `idb-support-training/` - support/training prototype
- `database/schema.sql` - PostgreSQL-ready relational schema
- `docs/RBAC_MATRIX.md` - least-privilege role matrix
- `docs/TEST_PLAN.md` - database/release validation plan

## Implementation note
The public Vercel demo intentionally uses browser-local synthetic state so a recruiter can exercise CRUD, permissions, exports and audit workflows without credentials or access to any real organizational database. The repository includes the PostgreSQL-ready schema that would back the same workflow in a production implementation.
