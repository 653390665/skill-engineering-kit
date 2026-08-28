#!/usr/bin/env python3
"""Build a clean install zip from a skill directory.

Excludes common audit logs, pressure-runs, local caches, macOS metadata, and pycache.
"""
from __future__ import annotations

import argparse
import zipfile
from pathlib import Path

EXCLUDE_PARTS = {"__MACOSX", "__pycache__", "pressure-runs", ".git"}
EXCLUDE_NAMES = {".DS_Store", "codex-run.log"}
EXCLUDE_SUFFIXES = {".pyc", ".pyo"}


def include(p: Path):
    if any(part in EXCLUDE_PARTS for part in p.parts):
        return False
    if p.name in EXCLUDE_NAMES:
        return False
    if p.suffix in EXCLUDE_SUFFIXES:
        return False
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source")
    ap.add_argument("output")
    args = ap.parse_args()
    src = Path(args.source).resolve()
    out = Path(args.output).resolve()
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for p in src.rglob("*"):
            if p.is_file() and include(p.relative_to(src)):
                z.write(p, arcname=str(src.name / p.relative_to(src)))
    print(out)

if __name__ == "__main__":
    main()
