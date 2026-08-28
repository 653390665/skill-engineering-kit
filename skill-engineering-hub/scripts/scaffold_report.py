#!/usr/bin/env python3
"""Create standard report skeletons for a target skill path."""
from __future__ import annotations

import argparse
from pathlib import Path
from datetime import date

REPORTS = {
    "STANDARD_AUDIT_REPORT.md": "# Skill Standard Audit Report\n\n## Target\n\n## Summary\n\n## Compliance Matrix\n\n## Issues\n\n## Next Action\n",
    "PRESSURE_TEST_BRIEF.md": "# Pressure Test Brief\n\n## Target\n\n## Scenario Matrix\n\n## Required Patterns\n\n## Forbidden Patterns\n",
    "OPTIMIZATION_REPORT.md": "# Skill Optimization Report\n\n## Top Findings\n\n## P0 Fixes\n\n## P1 Fixes\n\n## P2 Improvements\n",
    "RELEASE_GATE.md": "# Release Gate\n\n## Decision\n\n## Required Fixes\n",
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("target", help="Target directory where reports will be written")
    args = ap.parse_args()
    out = Path(args.target)
    out.mkdir(parents=True, exist_ok=True)
    for name, content in REPORTS.items():
        p = out / name
        if not p.exists():
            p.write_text(content + f"\nGenerated: {date.today().isoformat()}\n", encoding="utf-8")
            print(f"created {p}")
        else:
            print(f"exists {p}")

if __name__ == "__main__":
    main()
