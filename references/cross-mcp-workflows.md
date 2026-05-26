# Identity Cross-MCP Workflows

## Identity + HRIS: Lifecycle Automation

### New hire → Full provisioning
```
HRIS: create_employee(name: "Alex", dept: "Engineering") → {id: "emp_456"}
IDENTITY: lifecycle_task(type: "onboard", user_id: "emp_456", role: "engineer")
  → Provisions: email, Slack, GitHub, Jira, VPN
IDENTITY: check_mfa(user_id: "emp_456") → {enrolled: false, deadline: "7 days"}
SLACK: send_message(channel: "@alex", text: "Welcome! Please enroll MFA within 7 days: [link]")
```

### Termination → Immediate revoke
```
HRIS: update_employee(id: "emp_789", status: "terminated")
IDENTITY: emergency_revoke(user_id: "emp_789", reason: "Employment terminated")
IDENTITY: lifecycle_task(type: "offboard", user_id: "emp_789")
```

## Identity + ITSM: Incident-Driven Access

### Production incident → Temporary elevated access
```
ITSM: get_ticket(id: "INC-1001") → {priority: "critical", assignee: "usr_123"}
IDENTITY: request_access(user_id: "usr_123", resource: "aws-production", level: "read", duration: "4h", justification: "Debugging INC-1001")
NOTIFICATIONS: send_notification(recipient: "security-approver", title: "Access request: production read for INC-1001")
```

## Identity + Slack: Security Alerts

### Suspicious activity → Alert + revoke
```
IDENTITY: emergency_revoke(user_id: "usr_789", reason: "Suspicious login from unknown IP")
SLACK: send_message(channel: "#security-alerts", text: "🚨 *Emergency Revoke*\nUser: usr_789\nReason: Suspicious login from 185.x.x.x (Russia)\nAll sessions terminated. All tokens invalidated.")
```

## Identity + Notifications: MFA Compliance

### Weekly MFA compliance check
```
IDENTITY: [for each user] check_mfa(user_id) → find non-compliant
NOTIFICATIONS: send_notification(recipient: non_compliant_user, title: "⚠️ MFA Required", body: "Please enroll MFA by [deadline]. Your access will be restricted.")
SLACK: send_message(channel: "#security", text: "📊 MFA Compliance: 95% (3 users non-compliant)")
```
