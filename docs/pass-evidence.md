# 2026-11-19

## Pass test

1. Static gate exits 0 with 10 rule IDs, 0 network tokens, 0 storage tokens, 0 em dashes and 0 banned words.
2. SHA-256 vector for `abc` returns `ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad`.
3. Empty browser form shows `Paste a config first. Nothing was checked.` and no result.
4. Sample config produced score `0`, counts `critical 4`, `high 4`, `medium 1`, 9 findings, 9 chain entries.
5. Tool drift produced a `TOOL_DRIFT-1` finding after one tool was removed from the baseline.
6. Layout check at page width returned no horizontal overflow.
7. Page colours checked as background `rgb(6, 6, 10)` and text `rgb(247, 247, 245)`.

## Evidence

- Static gate: `PASS: 10 rules, 2 input boxes, zero network tokens, zero storage, SHA-256 vector clean, no banned words, JS syntax clean`
- Browser result attributes: `data-finding-count=9`, `data-chain-count=9`, `data-score=0`
