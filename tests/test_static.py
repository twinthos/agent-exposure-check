#!/usr/bin/env python3
"""Static gate for Agent Exposure Check.

Run from the repo root: python3 tests/test_static.py
No third party packages. No network access.
"""
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "index.html"
TEXT = HTML.read_text(encoding="utf-8")
LOW = TEXT.lower()

BANNED = [
    "fetch(",
    "XMLHttpRequest",
    "localStorage",
    "sessionStorage",
    "<script src=",
    "<link rel=\"stylesheet\" href=\"http",
    "http://",
    "https://",
    "—",
    "–",
    "whop",
    "skool",
    "leverage",
    "seamless",
    "bespoke",
    "elevate",
    "unlock",
    "robust",
    "comprehensive",
    "world-class",
    "cutting-edge",
    "game-changing",
    "revolutionary",
    "guaranteed",
    "proven",
    "eliminates",
    "illustrative",
    "8138" + "48257",
    "twinthos@agentmail" + ".to",
]

REQUIRED = [
    "Agent Exposure Check",
    "No account. No upload. No tracking. No subscription.",
    "What this does not do",
    "CyberChef shows what a blob of data contains.",
    "Tamper evident, not tamper proof.",
    "Put this outside the agent.",
]

RULE_IDS = [
    "SECRET_IN_ENV",
    "REMOTE_EXEC",
    "PROMPT_INJECTION_PHRASE",
    "METADATA_SSRF",
    "WILDCARD_PERMISSION",
    "UNAUTH_REMOTE_ENDPOINT",
    "MISSING_HUMAN_APPROVAL",
    "TOOL_DRIFT",
    "DATA_EXFIL_WORDING",
    "OBFUSCATED_TOOL_NAME",
]

VECTOR = "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"


def main():
    failures = []
    for token in BANNED:
        if token.lower() in LOW:
            failures.append("banned token present: " + token)
    for phrase in REQUIRED:
        if phrase not in TEXT:
            failures.append("missing required text: " + phrase)
    for rule in RULE_IDS:
        if rule not in TEXT:
            failures.append("missing rule id: " + rule)

    if TEXT.count("<textarea") != 2:
        failures.append("expected 2 textareas, found " + str(TEXT.count("<textarea")))

    node = shutil.which("node")
    if not node:
        failures.append("node not found, cannot check JavaScript or SHA-256 vector")
    else:
        js = TEXT.split("<script>", 1)[1].split("</script>", 1)[0]
        check = Path(ROOT) / ".js-check.js"
        check.write_text(js, encoding="utf-8")
        run = subprocess.run([node, "--check", str(check)], capture_output=True, text=True)
        if run.returncode != 0:
            failures.append("inline JavaScript syntax failed: " + run.stderr.strip()[:200])

        sha = TEXT.split("/* SHA256_START */", 1)[1].split("/* SHA256_END */", 1)[0]
        probe = Path(ROOT) / ".sha-check.js"
        probe.write_text(sha + "\nconsole.log(sha256('abc'));\n", encoding="utf-8")
        run = subprocess.run([node, str(probe)], capture_output=True, text=True)
        probe.unlink(missing_ok=True)
        if run.returncode != 0 or run.stdout.strip() != VECTOR:
            failures.append("SHA-256 vector failed: " + (run.stdout or run.stderr).strip()[:120])

    check.unlink(missing_ok=True)

    if failures:
        print("FAIL")
        for item in failures:
            print(" - " + item)
        return 1

    print("PASS: 10 rules, 2 input boxes, zero network tokens, zero storage, SHA-256 vector clean, no banned words, JS syntax clean")
    return 0


if __name__ == "__main__":
    sys.exit(main())
