# Security policy

## Scope

This policy covers `Agent Exposure Check` and its static test. The tool is defensive only. It parses text that you paste into the browser and reports patterns. It does not connect to systems, run commands or test exploits.

## Reporting a problem

Open a private security advisory on this repository. Do not post a public issue for a security flaw.

Include:

- What you pasted, with secrets removed.
- What you expected the tool to report.
- What it reported instead.
- Browser and operating system.

Do not include live tokens, passwords or private customer data.

## Response

- Acknowledge within 2 working days.
- Triage within 5 working days.
- Fix or give a written reason within 10 working days for confirmed defects.
- Credit reporters who want it when the fix ships.

## Supported version

Only the latest commit on `main` receives fixes.

## Out of scope

- Reports that a config contains a bad secret. The tool is designed to find that.
- Requests for exploit code, bypass techniques or attack tooling.
- Vulnerabilities in browsers or operating systems.
- Reports based only on a scanner score with no reproduction steps.

## Defensive line

Twinthos Sentinel exists for the benefit of humanity. Security here means protection. This project will not add code that attacks systems, steals secrets, evades controls or helps misuse an agent.

## Example identifiers

Any identifier that looks like `CVE-2025-EXAMPLE` in documentation is a placeholder. It is not a real vulnerability record.
