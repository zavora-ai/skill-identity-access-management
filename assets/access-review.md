# 🔐 Access Review Report

**Generated:** {timestamp}
**Tenant:** {tenant_name}
**Review Period:** {start_date} → {end_date}

## Summary

| Metric | Value |
|--------|-------|
| Total Users | {total_users} |
| Active | {active_count} ✅ |
| Inactive (>90d) | {inactive_count} ⚠️ |
| Suspended | {suspended_count} ❌ |
| Privileged Accounts | {privileged_count} |

## Role Distribution

| Role | Users | Last Reviewed | Status |
|------|-------|---------------|--------|
| {role_1} | {users_1} | {reviewed_1} | {status_1} |
| {role_2} | {users_2} | {reviewed_2} | {status_2} |
| {role_3} | {users_3} | {reviewed_3} | {status_3} |

## Findings

| Finding | Severity | Accounts Affected |
|---------|----------|-------------------|
| {finding_1} | {sev_1} | {affected_1} |
| {finding_2} | {sev_2} | {affected_2} |

## Recommendations

{recommendations}

---
*Reviewed by {agent_name} • Policy: {access_policy}*
