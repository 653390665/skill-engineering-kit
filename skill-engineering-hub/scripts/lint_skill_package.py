#!/usr/bin/env python3
"""Static lint for a skill package.

This is intentionally lightweight and dependency-free.
It checks structure, frontmatter presence, package cleanliness, and common local artifacts.
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

BAD_NAMES = {"__MACOSX", "__pycache__", ".DS_Store"}
BAD_SUFFIXES = {".pyc", ".pyo"}
LOCAL_PATH_RE = re.compile(r"/(Users|home)/[^\s)]+")


def parse_frontmatter(text: str):
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    return text[4:end]


def lint(path: Path):
    errors = []
    warnings = []

    if not path.exists():
        return [f"Path does not exist: {path}"], []

    skill_md = path / "SKILL.md"
    if not skill_md.exists():
        errors.append("Missing SKILL.md")
    else:
        text = skill_md.read_text(encoding="utf-8", errors="ignore")
        fm = parse_frontmatter(text)
        if fm is None:
            errors.append("SKILL.md missing valid YAML-style frontmatter block")
        else:
            if "name:" not in fm:
                errors.append("SKILL.md frontmatter missing name")
            if "description:" not in fm:
                errors.append("SKILL.md frontmatter missing description")
            # common invalid top-level fields are warnings here because schemas vary
            for bad in ["version:", "updated:"]:
                if re.search(rf"^{bad}", fm, flags=re.MULTILINE):
                    warnings.append(f"Frontmatter has top-level {bad} ; prefer metadata.{bad[:-1]}")

    for required in ["README.md", "MANIFEST.md"]:
        if not (path / required).exists():
            warnings.append(f"Missing {required}")

    for root, dirs, files in os.walk(path):
        root_p = Path(root)
        for name in list(dirs) + list(files):
            p = root_p / name
            if name in BAD_NAMES:
                warnings.append(f"Local/cache artifact present: {p.relative_to(path)}")
            if p.suffix in BAD_SUFFIXES:
                warnings.append(f"Python cache artifact present: {p.relative_to(path)}")
        for file in files:
            p = root_p / file
            if p.suffix.lower() in {".md", ".txt", ".yaml", ".yml", ".json", ".py"}:
                try:
                    text = p.read_text(encoding="utf-8", errors="ignore")
                except Exception:
                    continue
                if LOCAL_PATH_RE.search(text):
                    warnings.append(f"Possible local absolute path in {p.relative_to(path)}")

    return errors, warnings


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path", help="Skill package directory")
    args = ap.parse_args()
    errors, warnings = lint(Path(args.path))
    print(f"Errors: {len(errors)}")
    for e in errors:
        print(f"ERROR: {e}")
    print(f"Warnings: {len(warnings)}")
    for w in warnings:
        print(f"WARNING: {w}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
