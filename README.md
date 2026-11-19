# Agent Exposure Check

Paste an agent or MCP config. See what it can reach, what it can leak and what to block first.

Built by Twinthos Sentinel. Runs in one browser tab. No account. No upload. No tracking. No subscription.

## Why this exists

CyberChef is good at showing what is inside a blob of data. A business also needs to know which tool can delete a file, which server has no login and which instruction lives inside a document an agent will read. This tool names those things in plain English before they become an incident.

It sits beside Twinthos Sentinel. Sentinel watches live feeds and known vulnerabilities. This checks the config you paste, with no network calls at all.

## What it checks

1. Hardcoded secrets in environment values.
2. Remote code execution patterns such as `npx`, `uvx` and pipe to shell.
3. Instruction override phrases in tool descriptions.
4. Cloud metadata addresses that can expose temporary credentials.
5. Wildcard or root permissions.
6. Remote endpoints with no visible authentication.
7. Sensitive actions with no approval requirement.
8. Tool drift against an optional baseline config.
9. Outbound data wording that needs a named destination.
10. Unreadable tool names that nobody will challenge in review.

Each finding gives the evidence, why it matters and the first action to take.

## What it does not do

- It does not connect to your systems.
- It does not test an exploit or run a command.
- It does not decide what is safe for your organisation.
- It does not keep your config after you close the tab.
- It is not a certification and it is not a probability of breach.

## Run it

Open `index.html` in a modern browser. There is no build step and no dependency.

For a local server:

```sh
python3 -m http.server 8000
```

Then open `http://localhost:8000`.

Paste a config into the first box. Optionally paste an earlier version into the second box. Click `Check exposure`.

## Scoring

The score starts at 100. Each finding subtracts a fixed amount: 25 for critical, 15 for high, 8 for medium and 3 for low. The floor is 0. This is a heuristic to order the work, not a scientific measure of risk.

## Evidence chain

Findings are written into a local SHA-256 hash chain. Each entry carries the previous hash. This is tamper evident, not tamper proof. If someone controls the whole page, they can rewrite the chain. The tool says so on screen.

The browser uses Web Crypto when it is available and a local SHA-256 function otherwise.

## Privacy

All parsing, matching and hashing happens in the tab. The page loads no external script, font, stylesheet or image. It stores nothing. Closing the tab ends the session.

## Verify

From the repo root:

```sh
python3 tests/test_static.py
```

Expected output:

```text
PASS: 10 rules, 2 input boxes, zero network tokens, zero storage, SHA-256 vector clean, no banned words, JS syntax clean
```

The static gate checks ten rule IDs, two input boxes, zero network calls, zero storage calls, zero em dashes, zero banned words, JavaScript syntax and the SHA-256 vector for `abc`.

Browser check on a sample config with nine findings produced score `0`, counts `critical 4`, `high 4`, `medium 1`, and nine evidence chain entries. The empty form produced the error `Paste a config first. Nothing was checked.`

## Policy starter

The tool outputs a deny-by-default policy starter with `BLOCK` as the default and `ASK` for shell, external network and filesystem writes. Put the gate outside the agent. Check the rules with your own team before use.

## Files

- `index.html`: the whole tool.
- `tests/test_static.py`: the static gate.
- `docs/threat-model.md`: the ten checks and their limits.
- `SECURITY.md`: how to report a problem.
- `CHANGELOG.md`: version record.

## Licence

MIT. See `LICENSE`.
