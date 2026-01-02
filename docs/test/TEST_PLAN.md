# Test Plan

## Objectives
- Verify requirements per RTM
- Validate interfaces per ICD/IO map
- Confirm safe commissioning + basic functional operation

## Test levels
1) Component tests (sensors, actuators)
2) Subsystem tests (motion + sensing)
3) System tests (integrated cycle)
4) Safety tests (interlocks, E-stop, fault handling)

## Test entry/exit criteria
### Entry
- Release lock established
- IO validation complete
- Facilities prechecks passed

### Exit
- All Must requirements verified
- No open Sev-1 issues
- Evidence linked in RTM

## Reporting
- Update RTM status after every execution batch
- Store evidence under `docs/test/evidence/` (redacted if external)
