# IDB Release Test Plan

1. **Schema constraints** - required fields, score ranges, reporting-period format, foreign-key integrity.
2. **RBAC regression** - verify each demo role can only perform its approved actions.
3. **CRUD workflows** - create users, program records and support tickets; update account/ticket status.
4. **Reporting query** - aggregate program records and reconcile counts and quality averages.
5. **Export governance** - CSV actions are permission-gated and written to audit history.
6. **Backup/recovery control** - restore-check status is represented in the administration console.
7. **Data quality** - invalid synthetic records are flagged before reporting.
8. **Auditability** - role switches and operational actions create timestamped audit events.
9. **User support workflow** - create, prioritize and resolve synthetic IDB support tickets.
10. **Responsive UI** - administration, reporting, support and governance modules remain usable on narrow screens.

The public demo uses synthetic data only and is designed for recruiter inspection without credentials.
