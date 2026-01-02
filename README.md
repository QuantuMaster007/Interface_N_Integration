# Interface & Integration — ICD + Test + Bring-up

A **systems-integration execution repo** that shows how I translate messy HW + Controls + Facilities constraints into a **repeatable bring-up + verification plan** — with pinned versions, interface control, and evidence-based test closure.

**What this demonstrates (in 60 seconds):**
- ✅ How I baseline and control interfaces using an **ICD + IO map**
- ✅ How I prevent churn during integration with a **Release Lock / Version Matrix**
- ✅ How I run bring-up with a **commissioning checklist + entry/exit gates**
- ✅ How I close requirements using an **RTM (requirement → test → evidence)**
- ✅ How I triage failures using a **severity rubric + workflow**

---

## Most important artifacts (start here)
**1) Interface control**
- ICD overview: [`docs/interfaces/ICD_OVERVIEW.md`](docs/interfaces/ICD_OVERVIEW.md)
- IO map (machine-readable): [`data/sample/io_map.csv`](data/sample/io_map.csv)
- Protocols/comms notes: [`docs/interfaces/PROTOCOLS.md`](docs/interfaces/PROTOCOLS.md)

**2) Requirements → Verification (traceability)**
- Requirements: [`docs/requirements/REQUIREMENTS.md`](docs/requirements/REQUIREMENTS.md)
- RTM (source of truth): [`docs/requirements/RTM.csv`](docs/requirements/RTM.csv)

**3) Bring-up & Commissioning**
- Bring-up plan: [`docs/bringup/BRINGUP_PLAN.md`](docs/bringup/BRINGUP_PLAN.md)
- Commissioning checklist: [`docs/bringup/COMMISSIONING_CHECKLIST.md`](docs/bringup/COMMISSIONING_CHECKLIST.md)

**4) Test execution + evidence**
- Test plan: [`docs/test/TEST_PLAN.md`](docs/test/TEST_PLAN.md)
- Test cases: [`docs/test/test_cases/`](docs/test/test_cases/)

**5) Triage discipline**
- Severity rubric: [`docs/triage/SEVERITY_RUBRIC.md`](docs/triage/SEVERITY_RUBRIC.md)
- Failure triage workflow: [`docs/triage/FAILURE_TRIAGE_WORKFLOW.md`](docs/triage/FAILURE_TRIAGE_WORKFLOW.md)

**6) Release lock (anti-churn controls)**
- Release lock rules: [`docs/releases/RELEASE_LOCK.md`](docs/releases/RELEASE_LOCK.md)
- Version matrix: [`docs/releases/VERSION_MATRIX.md`](docs/releases/VERSION_MATRIX.md)

---

## Evidence outputs (proof this repo runs)
After running the commands below, this repo produces “evidence” files:
- IO map validation output: `docs/evidence/io_map_validation_output.md`
- RTM status summary: `docs/evidence/rtm_summary_output.md`

---

## Quick start (run + generate evidence)
Validate interface consistency (IO map):
```bash
python src/validators/validate_io_map.py data/sample/io_map.csv
```
Summarize requirements closure (RTM):
```bash
python src/tooling/rtm_summary.py docs/requirements/RTM.csv
```

---


**Important:**  
- The tree must be between the triple backticks.  
- Use `text` after the first backticks (helps formatting).  
- Don’t indent the backticks.

---

### Copy/paste this working vertical tree (already formatted)
Paste this **inside** the ` ```text ` block:

```text
docs/
├─ interfaces/
│  ├─ ICD_OVERVIEW.md
│  ├─ SIGNAL_SPEC_TEMPLATE.md
│  └─ PROTOCOLS.md
├─ requirements/
│  ├─ REQUIREMENTS.md
│  └─ RTM.csv
├─ bringup/
│  ├─ BRINGUP_PLAN.md
│  └─ COMMISSIONING_CHECKLIST.md
├─ test/
│  ├─ TEST_PLAN.md
│  └─ test_cases/
│     ├─ TC-001_BASIC_CYCLE.md
│     └─ TC-010_INTERLOCK_DOOR_OPEN.md
├─ triage/
│  ├─ SEVERITY_RUBRIC.md
│  └─ FAILURE_TRIAGE_WORKFLOW.md
├─ releases/
│  ├─ RELEASE_LOCK.md
│  └─ VERSION_MATRIX.md
└─ evidence/
   ├─ io_map_validation_output.md
   └─ rtm_summary_output.md

data/
└─ sample/
   └─ io_map.csv

src/
├─ validators/
│  └─ validate_io_map.py
└─ tooling/
   └─ rtm_summary.py

.github/
├─ ISSUE_TEMPLATE/
│  └─ bug.yml
└─ pull_request_template.md
```
---

## License
```text
MIT License
Copyright (c) 2026
```
```
