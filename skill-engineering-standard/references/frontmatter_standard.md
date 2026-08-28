# Frontmatter Standard

## Safest Form

```yaml
---
name: skill-name
description: Use when ...
---
```

## Naming Rules

- lowercase
- hyphen-separated
- no spaces
- avoid vague names
- directory name should match `name`

## Description Rules

Good description:

- says when to use the skill
- mentions the user intent
- differentiates from adjacent skills
- avoids marketing language

Bad description:

- too broad
- claims to do everything
- includes internal implementation details
- duplicates another skill's description

## Version Metadata

If the target runtime supports metadata, this is acceptable:

```yaml
---
name: skill-name
description: Use when ...
metadata:
  version: "1.0.0"
  updated: "2026-05-16"
---
```

If compatibility is uncertain, put version information in README and MANIFEST instead.

## Common Failure

Invalid top-level fields can make installation fail in stricter runtimes.
Use minimal frontmatter when distributing broadly.
