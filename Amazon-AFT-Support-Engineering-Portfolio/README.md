# Software Support Engineering Portfolio

Independent portfolio by **Junjun Hu (William)**, designed around the responsibilities in the public Amazon **Software Support Engineer, AFT Quality** job description.

> **Disclosure:** This is independent portfolio work. It is not affiliated with, endorsed by, or connected to Amazon or Amazon Fulfillment Technologies. All sites, systems, incidents, metrics, deployments and device data are synthetic and generic.

## Live portfolio modules

### 1. CV Fleet Health & Incident Console
- Synthetic NA / EU / FE device fleet
- Five generic vision / measurement system families
- Incoming ticket and incident view
- Layered host, storage, RAID, service, camera and REST troubleshooting
- Root-cause isolation and structured engineering handoff

### 2. Safe Deployment & Rollback Simulator
- Preflight -> staging -> canary -> phased production -> verification
- API-success, heartbeat and error-rate health gates
- Multi-region rollout scenario
- Automatic rollback decision when canary thresholds fail

### 3. Ops Automation & Runbook Toolkit
- Python log triage
- Python canary deployment guard
- RAID-health parser
- REST / JSON troubleshooting example
- XML configuration validation example
- Runbook / SOP patterns for recurring support issues

## JD mapping

| Public role responsibility / qualification | Portfolio evidence |
|---|---|
| Incoming tickets and extensive troubleshooting | Fleet Incident Console + log triage |
| Operations and maintenance coding | Python support tools |
| Staging / production deployment support | Deployment & Rollback Simulator |
| Develop tools to aid operations | log triage, deployment guard, RAID parser |
| Streamline SOPs and reduce engineering burden | Runbook candidates and automation |
| Knowledge-base development | documented troubleshooting patterns |
| Web services / distributed systems | multi-region fleet + REST health workflow |
| REST / JSON / XML | interactive inspectors and samples |
| Hardware / software RAID | RAID diagnostic workflow and parser |
| Global operations across time zones | synthetic NA / EU / FE deployment views |

## CLI tools

```bash
python tools/log_triage.py sample_data/support_logs.jsonl
python tools/deployment_guard.py sample_data/canary_metrics.json
python tools/raid_health.py sample_data/mdstat.txt
```

## Author
Junjun Hu (William)
