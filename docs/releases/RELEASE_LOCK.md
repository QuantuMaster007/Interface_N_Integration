# Release Lock

## Purpose
Stop churn during integration by pinning versions.

## What gets pinned
- PLC project version
- Firmware version(s)
- HMI version
- Config files (IO map revision, parameters)
- Safety logic revision

## Rules
- No changes to pinned items without a Change Request
- Emergency fixes require rollback plan + retest scope
