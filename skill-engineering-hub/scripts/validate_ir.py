#!/usr/bin/env python3
"""Validate a skill-ir.json file against the yao-meta-skill Skill IR 2.0
required-field contract (schema_version 2.0.0).

This is a lightweight structural check, not a full JSON Schema validator.
It enforces the same required fields and enums as yao's skill-ir/schema.json.

Optional drift check (recommended before yao handoff):
    python3 scripts/validate_ir.py skill-ir.json --skill-md SKILL.md
yao blocks compilation when IR trigger_surface.description drifts from the
SKILL.md frontmatter description, so both must match exactly (normalized).
"""

import argparse
import json
import re
import sys
from pathlib import Path

REQUIRED = [
    "schema_version",
    "name",
    "job_to_be_done",
    "trigger_surface",
    "workflow",
    "resources",
    "eval_plan",
    "risk",
    "governance",
]

TRIGGER_REQUIRED = ["description", "should_trigger", "should_not_trigger", "edge_cases"]
WORKFLOW_REQUIRED = ["steps", "decision_points", "failure_modes"]
RESOURCES_REQUIRED = ["references", "scripts", "assets", "reports"]
EVAL_REQUIRED = ["trigger", "output", "adversarial", "baseline"]
RISK_REQUIRED = ["output_risk", "execution_risk", "trust_boundary"]
GOV_REQUIRED = ["owner", "maturity", "review_cadence", "review_due"]

RISK_ENUM = {"low", "medium", "high"}
TRUST_ENUM = {"personal", "team", "external"}
MATURITY_ENUM = {"scaffold", "production", "library", "governed"}

PLACEHOLDER = "TODO"


def check_required(obj, fields, path):
    """Fields must exist and not be None. Empty arrays are legal (e.g. resources);
    empty strings are caught separately for string fields."""
    errors = []
    for f in fields:
        if f not in obj:
            errors.append(f"{path}.{f}: missing")
        elif obj[f] is None:
            errors.append(f"{path}.{f}: null")
    return errors


def check_strings(obj, fields, path):
    """String fields must be non-empty (arrays may be empty)."""
    errors = []
    for f in fields:
        v = obj.get(f)
        if isinstance(v, str) and v.strip() == "":
            errors.append(f"{path}.{f}: empty string")
    return errors


def normalize(text):
    return re.sub(r"\s+", " ", str(text or "")).strip().strip('"').strip("'")


def read_frontmatter_description(skill_md):
    text = Path(skill_md).read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    for line in parts[1].splitlines():
        if line.strip().startswith("description:"):
            return line.split(":", 1)[1].strip().strip('"').strip("'")
    return None


def check_description_drift(data, skill_md):
    """yao blocks compile when IR description drifts from SKILL.md frontmatter."""
    errors = []
    fm = read_frontmatter_description(skill_md)
    if fm is None:
        return ["--skill-md given but no frontmatter description found in SKILL.md"]
    ir_desc = normalize(data.get("trigger_surface", {}).get("description"))
    if normalize(fm) != ir_desc:
        errors.append(
            "description drift: IR trigger_surface.description must exactly match "
            "SKILL.md frontmatter description (yao blocks compile otherwise)\n"
            f"    SKILL.md: {normalize(fm)}\n"
            f"    IR:       {ir_desc}"
        )
    return errors


def main(argv=None):
    parser = argparse.ArgumentParser(description="Validate skill-ir.json (schema 2.0.0)")
    parser.add_argument("ir_path", help="path to skill-ir.json")
    parser.add_argument("--skill-md", help="optional SKILL.md path for description drift check")
    args = parser.parse_args(argv)

    with open(args.ir_path, "r", encoding="utf-8") as fh:
        data = json.load(fh)

    errors = []
    if data.get("schema_version") != "2.0.0":
        errors.append("schema_version: must be 2.0.0")
    errors += check_required(data, REQUIRED, "root")

    ts = data.get("trigger_surface", {})
    errors += check_required(ts, TRIGGER_REQUIRED, "trigger_surface")
    errors += check_strings(ts, ["description"], "trigger_surface")
    errors += check_required(data.get("workflow", {}), WORKFLOW_REQUIRED, "workflow")
    errors += check_required(data.get("resources", {}), RESOURCES_REQUIRED, "resources")
    errors += check_required(data.get("eval_plan", {}), EVAL_REQUIRED, "eval_plan")
    errors += check_strings(data.get("eval_plan", {}), ["baseline"], "eval_plan")
    errors += check_required(data.get("risk", {}), RISK_REQUIRED, "risk")
    errors += check_required(data.get("governance", {}), GOV_REQUIRED, "governance")
    errors += check_strings(data.get("governance", {}), ["owner", "review_cadence", "review_due"], "governance")
    errors += check_strings(data, ["name", "job_to_be_done"], "root")

    risk = data.get("risk", {})
    if risk.get("output_risk") not in RISK_ENUM:
        errors.append(f"risk.output_risk: must be one of {sorted(RISK_ENUM)}")
    if risk.get("execution_risk") not in RISK_ENUM:
        errors.append(f"risk.execution_risk: must be one of {sorted(RISK_ENUM)}")
    if risk.get("trust_boundary") not in TRUST_ENUM:
        errors.append(f"risk.trust_boundary: must be one of {sorted(TRUST_ENUM)}")
    if data.get("governance", {}).get("maturity") not in MATURITY_ENUM:
        errors.append(f"governance.maturity: must be one of {sorted(MATURITY_ENUM)}")

    # Any remaining placeholder means the export is incomplete.
    if PLACEHOLDER in json.dumps(data, ensure_ascii=False):
        errors.append(f"still contains {PLACEHOLDER!r} placeholders — fill from kit contracts first")

    if args.skill_md:
        errors += check_description_drift(data, args.skill_md)

    if errors:
        print("INVALID skill-ir.json")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("VALID skill-ir.json (schema 2.0.0 required fields present)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

