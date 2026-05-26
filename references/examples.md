# Identity Skill Examples

## Example 1: "Grant Sarah production access for debugging"

**User says:** "Sarah needs read access to production to debug the payment outage"

**Tool calls:**
```
1. lookup_user(query: "sarah@company.com")
   → {id: "usr_123", name: "Sarah Mitchell", status: "active", mfa: true}

2. list_entitlements(user_id: "usr_123")
   → [{resource: "aws-staging", level: "write"}, {resource: "github", level: "write"}]
   → Does NOT have production access currently

3. request_access(
     user_id: "usr_123",
     resource: "aws-production",
     level: "read",
     justification: "Debugging payment outage INC-1001",
     duration: "4h"
   )
   → {id: "req_456", status: "pending_approval"}
```

**Response:**
```
✅ Access request submitted

**User:** Sarah Mitchell
**Resource:** AWS Production (read-only)
**Duration:** 4 hours (auto-expires)
**Justification:** Debugging payment outage INC-1001
**Status:** ⏳ Pending security team approval

MFA verified ✅ — Sarah has MFA enrolled.
```

## Example 2: "Revoke access for compromised account"

**User says:** "We detected suspicious login on Tom's account. Revoke everything now."

**Tool calls:**
```
1. emergency_revoke(
     user_id: "usr_tom",
     reason: "Suspicious login detected from unknown IP. Potential account compromise."
   )
   → {status: "revoked", sessions_terminated: 3, tokens_invalidated: 8}
```

**Response:**
```
🚨 Emergency Revocation Complete

**User:** Tom Wilson
**Action:** All access revoked immediately
**Sessions terminated:** 3
**Tokens invalidated:** 8

All active sessions have been killed. Tom cannot access any systems until security review is complete.

Next steps:
1. Investigate the suspicious login (IP, time, location)
2. Reset Tom's credentials
3. Re-enable after security clearance
```

## Example 3: "Check MFA compliance for engineering"

**User says:** "Are all engineers MFA compliant?"

**Tool calls:**
```
1. lookup_user(query: "department:Engineering")
   → [45 users]

2. check_mfa(user_id: "usr_1") → {enrolled: true}
   ... (batch check)
   check_mfa(user_id: "usr_42") → {enrolled: false, deadline: "overdue"}
   check_mfa(user_id: "usr_43") → {enrolled: false, deadline: "2025-02-01"}
```

**Response:**
```
## MFA Compliance: Engineering

**Compliant:** 43/45 (95.6%)
**Non-compliant:** 2 users

| User | Status | Deadline |
|------|--------|----------|
| Tom Wilson | ❌ Not enrolled | 🚨 OVERDUE |
| Alex Johnson | ❌ Not enrolled | Feb 1 (3 days) |

**Recommended actions:**
1. Tom Wilson — overdue. Restrict access until enrolled.
2. Alex Johnson — new hire, deadline approaching. Send reminder.

Want me to send MFA enrollment reminders?
```
