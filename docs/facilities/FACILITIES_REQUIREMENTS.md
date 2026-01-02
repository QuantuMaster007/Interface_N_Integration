# Facilities Requirements — Integration Readiness

This document defines **site / facilities prerequisites** required for bring-up, commissioning, and SAT.
It is used to prevent late blockers by making utilities, safety, and network constraints explicit and testable.

---

## 1) Scope
Facilities readiness includes:
- **Power & grounding**
- **Network / VLAN / security approvals**
- **Utilities** (CDA, exhaust, vacuum, DI water — as applicable)
- **Safety infrastructure** (E-stops, interlocks, LOTO, signage)
- **Environmental constraints** (space, clearances, vibration/noise)

---

## 2) Facility prerequisites (minimum for Move-in / Install)
### 2.1 Power
- Voltage / phase: ______________________
- Breaker rating: ______________________
- Grounding / bonding verified: [ ] Yes [ ] No
- Power quality requirements (if any): ______________________
- Acceptance check:
  - [ ] Panel labeled
  - [ ] Correct receptacles installed
  - [ ] Measured voltage within spec

### 2.2 Network / VLAN / Security
- VLAN requested: ______________________
- Ports / drops available at tool location: [ ] Yes [ ] No
- Security approval complete: [ ] Yes [ ] No
- Acceptance check:
  - [ ] Switch port active
  - [ ] DHCP/static IP plan defined
  - [ ] Tool reachable from engineering subnet (as required)

### 2.3 Space / Access / Handling
- Footprint + keep-out zones confirmed: [ ] Yes [ ] No
- Rigging path cleared: [ ] Yes [ ] No
- Crane/forklift schedule reserved (if needed): [ ] Yes [ ] No

---

## 3) Utilities (apply as needed)
> Mark N/A if not required by your system.

### 3.1 CDA (Clean Dry Air)
- Pressure range: __________
- Flow requirement: __________
- Acceptance check: [ ] Regulator installed [ ] Leak check complete

### 3.2 Exhaust
- Exhaust type: __________ (house / dedicated)
- Flow requirement: __________
- Acceptance check: [ ] Hood connected [ ] Airflow verified

### 3.3 Vacuum
- Vacuum requirement: __________
- Acceptance check: [ ] Pump available [ ] Stable vacuum achieved

### 3.4 DI Water / Cooling
- DI water: [ ] Required [ ] N/A
- Cooling water: [ ] Required [ ] N/A
- Acceptance check: [ ] Flow verified [ ] Temperature within spec

---

## 4) Safety & EHS prerequisites (minimum for Power-on)
- LOTO plan reviewed: [ ] Yes [ ] No
- Emergency stops tested: [ ] Yes [ ] No
- Door/guard interlocks tested: [ ] Yes [ ] No
- Safety signage and access controls: [ ] Yes [ ] No
- Acceptance check:
  - [ ] E-stop triggers safe state
  - [ ] Door open triggers fail-safe behavior
  - [ ] Safety chain OK signal verified in IO map / PLC

---

## 5) Acceptance criteria by phase
### Move-in / Install Exit Criteria
- [ ] Power available and verified
- [ ] Network plan approved (or compliant temporary workaround)
- [ ] Space/access confirmed
- [ ] Required utilities available

### Commissioning Exit Criteria
- [ ] Safe power-on achieved
- [ ] Safety chain validated (E-stop + interlocks)
- [ ] Basic comms established (tool ↔ controls)

### SAT Exit Criteria
- [ ] Utilities stable under load
- [ ] Network stable + approved configuration
- [ ] Verification tests executed with evidence

---

## 6) Evidence expectations
Evidence examples:
- Photos of panel labeling + utility hookups
- Network approval ticket ID
- Voltage/pressure/flow readings
- Test logs showing safety chain signals (door open, E-stop)

Link evidence files under: `docs/evidence/`
