# Identity Tool Sequences Reference

## Tool Inventory (mcp-identity, 8 tools)

| Tool | Risk | Purpose |
|------|------|---------|
| `lookup_user` | read | Find user by email/name/ID |
| `list_user_groups` | read | Group memberships |
| `check_mfa` | read | MFA enrollment status |
| `verify_user` | read | Confirm identity (challenge) |
| `list_entitlements` | read | Current access/permissions |
| `request_access` | write | Submit access request (needs approval) |
| `emergency_revoke` | destructive | Immediate access removal |
| `lifecycle_task` | write | Onboard/offboard/transfer |

## Sequence: Access Request (3 calls)

```
1. lookup_user(query: "sarah@company.com")
   → {id: "usr_123", name: "Sarah Mitchell", status: "active", department: "Engineering"}

2. list_entitlements(user_id: "usr_123")
   → [{resource: "github", level: "write"}, {resource: "aws-staging", level: "read"}]
   → Verify: does user already have the requested access?

3. request_access(
     user_id: "usr_123",
     resource: "aws-production",
     level: "read",
     justification: "Debugging production incident INC-1001",
     duration: "4h"
   )
   → {id: "req_456", status: "pending_approval", approver: "security-team"}
```

## Sequence: Emergency Revocation (1 call)

```
1. emergency_revoke(
     user_id: "usr_789",
     reason: "Account compromise detected — suspicious login from unknown IP"
   )
   → {status: "revoked", sessions_terminated: 5, tokens_invalidated: 12, timestamp: "2025-01-18T10:30:00Z"}
```

## Sequence: Employee Onboarding (2 calls)

```
1. lifecycle_task(
     type: "onboard",
     user_id: "emp_new_456",
     role: "engineer",
     department: "Engineering"
   )
   → {provisioned: ["email", "slack", "github", "jira", "vpn"], mfa_required: true}

2. check_mfa(user_id: "emp_new_456")
   → {enrolled: false, required: true, deadline: "2025-02-08"}
   → Flag: MFA not yet enrolled, remind user
```

## Sequence: Offboarding (2 calls)

```
1. lifecycle_task(type: "offboard", user_id: "emp_789")
   → {revoked: ["all_access"], disabled: ["email", "vpn"], transferred: ["drive_ownership → manager"]}

2. emergency_revoke(user_id: "emp_789", reason: "Employment terminated")
   → Ensures immediate session termination
```

## Sequence: MFA Compliance Check (2 calls)

```
1. lookup_user(query: "department:Engineering")
   → List of all engineering users

2. For each: check_mfa(user_id)
   → Flag non-compliant users (enrolled: false)
```

## Access Duration Guidelines

| Access Type | Max Duration | Renewal |
|-------------|-------------|---------|
| Production read | 4 hours | Re-request |
| Production write | 1 hour | Re-request + approval |
| Staging | 24 hours | Auto-renew |
| Development | 30 days | Auto-renew |
| Admin/privileged | 1 hour | Always re-request |
