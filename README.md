# Identity & Access Management Skill

> Zero-trust identity governance for AI agents — user lookup, MFA verification, least-privilege access requests, emergency revocation, and lifecycle automation.

[![Skill Standard](https://img.shields.io/badge/standard-agentskills.io-blue)](https://agentskills.io)
[![MCP Server](https://img.shields.io/badge/mcp--server-mcp--identity-green)](https://github.com/zavora-ai/mcp-identity)
[![ADK-Rust Enterprise](https://img.shields.io/badge/ADK--Rust-Enterprise-purple.svg)](https://enterprise.adk-rust.com)
[![License](https://img.shields.io/badge/license-Apache--2.0-orange)](LICENSE)

## What This Skill Does

| Workflow | Tool Calls | What It Achieves |
|----------|-----------|------------------|
| Access Request | 3 | Governed access with justification + time-bound |
| Emergency Revoke | 1 | Instant access removal (sessions + tokens) |
| Lifecycle (Onboard) | 2 | Full provisioning with MFA enforcement |
| Lifecycle (Offboard) | 2 | Complete access removal + ownership transfer |
| MFA Compliance | 2 | Audit enrollment across teams |

## Installation

```bash
git clone https://github.com/zavora-ai/skill-identity-access-management.git \
  ~/.skills/skills/identity-access-management
```

## Requirements

**Required:** `mcp-identity` (8 tools)

**Cross-MCP:**
- `mcp-hris` — employee lifecycle triggers
- `mcp-slack` — security alerts
- `mcp-notifications` — MFA reminders
- `mcp-itsm` — incident-driven access elevation

## Folder Structure

```
identity-access-management/
├── SKILL.md                       # Main skill (decision tree + workflows)
├── references/
│   ├── tool-sequences.md          # 8 tools + access duration guidelines
│   ├── cross-mcp-workflows.md     # Identity + HRIS + ITSM + Slack
│   └── examples.md                # 3 scenarios (grant, revoke, compliance)
├── README.md
└── LICENSE
```

## Success Criteria

| Metric | Target |
|--------|--------|
| Least privilege | 100% access grants are time-bounded |
| Revocation speed | Emergency revoke in 1 tool call |
| MFA compliance | Flag non-compliant users proactively |

## Contributors

| [<img src="https://github.com/jkmaina.png" width="80px;"/><br /><sub><b>James Karanja Maina</b></sub>](https://github.com/jkmaina) |
|:---:|

## License

Apache-2.0

---

Part of the [ADK-Rust Enterprise](https://enterprise.adk-rust.com) skills ecosystem. Built with ❤️ by [Zavora AI](https://zavora.ai)

## How It Works

### Zero-Trust Access Model

Every access request is evaluated:
1. **Verify identity** — who is requesting?
2. **Check MFA** — is their authentication strong enough?
3. **Assess risk** — resource sensitivity × duration × context
4. **Time-bound** — all grants expire (no permanent elevation)
5. **Audit** — every grant/revoke logged with justification

## Success Criteria

| Metric | Target |
|--------|--------|
| Least privilege | 100% access grants time-bounded |
| MFA compliance | Required for all privileged access |
| Revocation speed | Emergency revoke in 1 tool call |
| Offboarding SLA | Access removed within hours of termination |
