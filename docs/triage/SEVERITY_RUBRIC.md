# Issue Severity Rubric

## Sev-1 (Critical / Safety / Cannot proceed)
- Safety chain failure, interlock not functioning
- Electrical hazard or uncontrolled motion
- Data corruption that invalidates test evidence
- Blocks commissioning / power-on / qualification start

## Sev-2 (Major)
- Functional failure with workaround
- Significant performance miss
- Noncompliance with key requirement but not safety-critical

## Sev-3 (Minor)
- Cosmetic HMI issues
- Non-blocking alarms, logging gaps

## Required fields for every issue
- Observed behavior
- Expected behavior
- Repro steps
- Logs/screenshots
- Versions (PLC/firmware/HMI)
- As-built notes (wiring changes, facility deviations)
