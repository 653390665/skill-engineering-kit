#!/usr/bin/env python3
"""Build a clean install zip for a skill package.

Usage:
  python scripts/build_clean_package.py /path/to/package output.zip

This excludes common audit/log/cache files.
"""

from __future__ import annotations

import sys
import zipfile
from pathlib import Path

EXCLUDED_DIRS = {"__MACOSX", "__pycache__", "pressure-runs", ".git"}
EXCLUDED_FILES = {".DS_Store", "codex-run.log"}
EXCLUDED_SUFFIXES = {".pyc", ".pyo"}


def should_exclude(path: Path) -> bool:
    parts = set(path.parts)
    if parts & EXCLUDED_DIRS:
        return True
    if path.name in EXCLUDED_FILES:
        return True
    if path.suffix in EXCLUDED_SUFFIXES:
        return True
    return False


def build_zip(src: Path, out: Path) -> None:
    src = src.resolve()
    out = out.resolve()
    if not src.exists() or not src.is_dir():
        raise SystemExit(f"Source directory does not exist: {src}")
    if out.exists():
        out.unlink()
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in src.rglob("*"):
            if should_exclude(path):
                continue
            if path.is_file():
                arc = Path(src.name) / path.relative_to(src)
                zf.write(path, arc.as_posix())
    print(f"Wrote clean package: {out}")


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: build_clean_package.py /path/to/package output.zip")
        return 2
    build_zip(Path(sys.argv[1]), Path(sys.argv[2]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
