#!/usr/bin/env python3
"""Lightweight skill package linter.

Usage:
  python scripts/lint_skill_package.py /path/to/skill-or-system

This script intentionally uses only the Python standard library.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

BAD_NAMES = {"__MACOSX", "__pycache__"}
BAD_SUFFIXES = {".pyc"}
BAD_FILES = {".DS_Store", "codex-run.log"}
LOCAL_PATH_PATTERNS = [re.compile("/" + "Users/" + r"[^\s)]+"), re.compile("C:" + r"\\Users\\[^\s)]+")]


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8", errors="ignore")


def check_frontmatter(skill_md: Path) -> list[str]:
    issues: list[str] = []
    text = read_text(skill_md)
    if not text.startswith("---\n"):
        return [f"{skill_md}: missing frontmatter block"]
    end = text.find("\n---", 4)
    if end == -1:
        return [f"{skill_md}: unclosed frontmatter block"]
    fm = text[4:end].strip().splitlines()
    fields = {}
    for line in fm:
        if not line.strip() or line.startswith("  "):
            continue
        if ":" in line:
            key, val = line.split(":", 1)
            fields[key.strip()] = val.strip()
    for required in ["name", "description"]:
        if required not in fields or not fields[required].strip():
            issues.append(f"{skill_md}: missing required frontmatter field `{required}`")
    name = fields.get("name", "").strip('"\'')
    if name and not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        issues.append(f"{skill_md}: name should be lowercase-hyphen, got `{name}`")
    return issues


def lint(root: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    if not root.exists():
        errors.append(f"Path does not exist: {root}")
        return errors, warnings

    skill_files = list(root.rglob("SKILL.md"))
    if not skill_files:
        errors.append("No SKILL.md found")
    for skill_md in skill_files:
        errors.extend(check_frontmatter(skill_md))

    for path in root.rglob("*"):
        if path.name in BAD_NAMES:
            errors.append(f"Forbidden directory/file name: {path}")
        if path.name in BAD_FILES:
            errors.append(f"Forbidden file in install package: {path}")
        if path.suffix in BAD_SUFFIXES:
            errors.append(f"Forbidden bytecode/cache file: {path}")
        if path.is_file() and path.suffix.lower() in {".md", ".txt", ".yaml", ".yml", ".json", ".py"}:
            text = read_text(path)
            for pattern in LOCAL_PATH_PATTERNS:
                if pattern.search(text):
                    warnings.append(f"Possible local absolute path in {path}")

    # Common docs warnings
    for doc in ["README.md", "MANIFEST.md"]:
        if not (root / doc).exists():
            warnings.append(f"Missing recommended root file: {doc}")

    return errors, warnings


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: lint_skill_package.py /path/to/skill-or-system")
        return 2
    root = Path(sys.argv[1]).resolve()
    errors, warnings = lint(root)
    print(f"Lint target: {root}")
    print(f"Errors: {len(errors)}")
    for item in errors:
        print(f"ERROR: {item}")
    print(f"Warnings: {len(warnings)}")
    for item in warnings:
        print(f"WARN: {item}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
