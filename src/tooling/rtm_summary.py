#!/usr/bin/env python3
"""
Generate a simple RTM status summary from RTM.csv.
"""
import csv
from collections import Counter

def main(path: str) -> None:
    c = Counter()
    total = 0
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            total += 1
            c[(row.get("status") or "Unknown").strip()] += 1
    print(f"RTM total requirements: {total}")
    for k, v in c.most_common():
        print(f"- {k}: {v}")

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("rtm_csv", help="Path to RTM.csv")
    args = ap.parse_args()
    main(args.rtm_csv)
