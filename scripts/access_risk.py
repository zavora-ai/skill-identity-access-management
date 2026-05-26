#!/usr/bin/env python3
"""Assess risk of an access request based on resource sensitivity and user context."""
import json, sys

RESOURCE_SENSITIVITY = {"production": 10, "staging": 5, "development": 2, "admin": 10, "read": 1, "write": 5}

def assess(data):
    resource = data.get("resource", "")
    level = data.get("level", "read")
    duration_hours = data.get("duration_hours", 24)
    has_mfa = data.get("mfa_enrolled", False)
    
    sensitivity = RESOURCE_SENSITIVITY.get(resource, 3) + RESOURCE_SENSITIVITY.get(level, 3)
    time_risk = 2 if duration_hours > 8 else 1 if duration_hours > 4 else 0
    mfa_risk = 3 if not has_mfa and sensitivity > 5 else 0
    
    total = sensitivity + time_risk + mfa_risk
    risk = "critical" if total > 15 else "high" if total > 10 else "medium" if total > 5 else "low"
    
    return {
        "risk_level": risk,
        "score": total,
        "requires_approval": total > 5,
        "requires_mfa": sensitivity > 5,
        "max_duration": "1h" if total > 15 else "4h" if total > 10 else "24h",
        "flags": (["MFA not enrolled — required for this resource"] if mfa_risk > 0 else []) + (["Long duration requested"] if time_risk > 1 else []),
    }

if __name__ == "__main__":
    print(json.dumps(assess(json.loads(sys.argv[1])), indent=2))
