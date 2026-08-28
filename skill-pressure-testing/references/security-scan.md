# Security Scan Layer

Security scanning is separate from behavior testing. A skill can pass behavior scenarios and still be dangerous if it hides prompt injection, credential access, or risky scripts.

## When To Scan

Scan when:

- installing a skill from GitHub or another external source
- publishing a skill for others
- the skill contains scripts
- the skill instructs network access, shell commands, credentials, browser automation, or file system traversal
- the skill includes hidden or minified content

## Tools To Consider

Use available tools when installed:

- `snyk/agent-scan`: scans agent configurations and skill-like bundles for security issues.
- `cisco-ai-defense/skill-scanner`: scans agent skills for prompt injection and malicious patterns.
- `getsentry/skills/skills/skill-scanner`: reference design for skill scanning.

If tools are unavailable, do manual inspection and state that automated scanning was not run.

## Manual Checks

- Search for credential terms: `api_key`, `token`, `secret`, `.env`, `ssh`, `cookie`.
- Search for exfiltration terms: `curl`, `wget`, `nc`, `scp`, `base64`, `webhook`.
- Search for destructive commands: `rm -rf`, `chmod 777`, `sudo`, `killall`, `dd`.
- Search for hidden text or suspicious encoding.
- Inspect scripts before running them.
- Check whether the skill asks the agent to ignore system or developer instructions.

## Report Fields

```md
## Security Scan

- Automated tools run:
- Manual checks run:
- Findings:
- False positives:
- Not checked:
- Release impact:
```

## Limitations

- A clean scan is not proof of safety.
- Scanners can miss social-engineering instructions.
- Manual review is still required for scripts and high-permission workflows.
- Do not run unknown scripts just to see what they do.
