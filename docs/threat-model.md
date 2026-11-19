# Threat model and check limits

This document explains what each check looks for and where it can be wrong. It is a map of the tool, not a claim of coverage.

The checks are deliberately simple. They work on pasted text. They do not execute the config. A clean result means these ten checks found nothing in this paste. It does not mean the agent is safe.

| ID | Severity | Looks for | Main limit | OWASP agentic area |
| --- | --- | --- | --- | --- |
| SECRET_IN_ENV | critical | Key, token, secret or password values in config text | Cannot tell a live key from a stale test value | ASI03 identity and privilege abuse |
| REMOTE_EXEC | critical | `npx`, `uvx`, `pipx run`, pipe to shell, inline node or python code | Cannot prove the fetched package is malicious | ASI04 supply chain |
| PROMPT_INJECTION_PHRASE | critical | Phrases that tell a model to forget rules or hide instructions | Misses paraphrases and non English wording | ASI01 goal hijack |
| METADATA_SSRF | critical | Known cloud metadata addresses | Cannot see addresses generated at run time | ASI02 tool misuse |
| WILDCARD_PERMISSION | high | Wildcards, root paths, full access, admin scopes | May flag a deliberate internal test scope | ASI03 identity and privilege abuse |
| UNAUTH_REMOTE_ENDPOINT | high | URL fields with no auth, token or key marker nearby | Absence of a marker is not proof of no auth | ASI07 insecure communication |
| MISSING_HUMAN_APPROVAL | high | Sensitive action words with no approval word nearby | A policy may require approval elsewhere | ASI09 human trust exploitation |
| TOOL_DRIFT | high | New, removed or changed tools versus a baseline | Needs both inputs to be valid JSON | ASI04 supply chain |
| DATA_EXFIL_WORDING | medium | Words about upload, send, webhook or external destinations | Many tools legitimately send data | ASI02 tool misuse |
| OBFUSCATED_TOOL_NAME | low | Tool names that are long and hard to read | A valid name may look unusual | ASI10 rogue agents |

## Scoring

Start at 100. Subtract 25 for each critical finding, 15 for high, 8 for medium and 3 for low. Floor at 0. The score orders work. It does not measure breach probability.

## False confidence controls

- The result page states that a clean scan is not proof of safety.
- Secrets are redacted in evidence before hashing or display.
- The evidence chain is labelled tamper evident, not tamper proof.
- The policy output is labelled as a starter and put outside the agent.
- The tool says what it does not do on the first screen.

## Changes to this model

Add a check only when it can be shown with a pasted input and a clear expected finding. Add a matching limit in this table at the same time.
