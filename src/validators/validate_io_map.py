#!/usr/bin/env python3
"""
Validate IO map CSV for common TPM/EPM integration issues:
- required columns present
- unique signal_id
- direction values valid
- domain values valid
- update_rate_ms numeric
- basic completeness checks for safety signals
"""
import csv
import sys

REQUIRED_COLS = [
    "signal_id","signal_name","direction","domain","type","update_rate_ms","failsafe_behavior"
]
VALID_DIRECTION = {"Input","Output"}
VALID_DOMAIN = {"Hardware","Controls","Facilities","Safety"}

def die(msg: str) -> None:
    print(f"ERROR: {msg}")
    sys.exit(2)

def warn(msg: str) -> None:
    print(f"WARNING: {msg}")

def main(path: str) -> None:
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        cols = r.fieldnames or []
        missing = [c for c in REQUIRED_COLS if c not in cols]
        if missing:
            die(f"Missing required columns: {missing}")

        seen = set()
        row_n = 1
        for row in r:
            row_n += 1
            sid = row["signal_id"].strip()
            if not sid:
                die(f"Row {row_n}: empty signal_id")
            if sid in seen:
                die(f"Row {row_n}: duplicate signal_id {sid}")
            seen.add(sid)

            direction = row["direction"].strip()
            if direction not in VALID_DIRECTION:
                die(f"Row {row_n} ({sid}): invalid direction '{direction}' (use Input/Output)")

            domain = row["domain"].strip()
            if domain not in VALID_DOMAIN:
                warn(f"Row {row_n} ({sid}): unusual domain '{domain}' (expected one of {sorted(VALID_DOMAIN)})")

            try:
                int(row["update_rate_ms"])
            except Exception:
                die(f"Row {row_n} ({sid}): update_rate_ms must be an integer")

            failsafe = row["failsafe_behavior"].strip()
            if not failsafe:
                warn(f"Row {row_n} ({sid}): missing failsafe_behavior")

            # Safety hygiene checks
            if domain == "Safety" and not row.get("alarm_id","").strip():
                warn(f"Row {row_n} ({sid}): Safety signal missing alarm_id")

        print(f"OK: {len(seen)} signals validated. No blocking errors.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python src/validators/validate_io_map.py <path_to_io_map.csv>")
        sys.exit(1)
    main(sys.argv[1])
