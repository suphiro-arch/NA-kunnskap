from pathlib import Path
import re
import sys


SUSPICIOUS_CHARS = {chr(0x00C2), chr(0x00C3), chr(0x00E2), chr(0xFFFD)}
QUESTION_MARK_IN_WORD = re.compile(r"[A-Za-zÆØÅæøå]\?[A-Za-zÆØÅæøå]")
QUESTION_MARK_PREFIX = re.compile(r"^\?[A-Za-zÆØÅæøå]+$")
QUESTION_MARK_SHORT_TOKEN = re.compile(r"^[A-Za-zÆØÅæøå]\?$")
TARGETS = [
    Path("AGENTS.md"),
    Path("README.md"),
    Path("arkitektur"),
    Path("briefs"),
    Path("config/prompts"),
    Path("config/templates"),
    Path("arkitektur/produkter/produktbeskrivelser"),
    Path("arkitektur/ressurser"),
    Path("sources"),
    Path("web/hugo-prototype/content"),
]
EXTENSIONS = {".md", ".yaml", ".yml", ".html", ".toml"}


def iter_files():
    for target in TARGETS:
        if target.is_file():
            if target.suffix.lower() in EXTENSIONS:
                yield target
            continue

        if not target.exists():
            continue

        for path in target.rglob("*"):
            if path.is_file() and path.suffix.lower() in EXTENSIONS:
                yield path


def find_suspicious_lines(path: Path):
    text = path.read_text(encoding="utf-8")
    findings = []
    for lineno, line in enumerate(text.splitlines(), start=1):
        if any(ch in line for ch in SUSPICIOUS_CHARS) or has_suspicious_question_mark(line):
            findings.append((lineno, line.strip()))
    return findings


def has_suspicious_question_mark(line: str) -> bool:
    # Vanlige spørsmål og URL-parametere skal ikke gi treff.
    for raw_token in line.split():
        if "?" not in raw_token:
            continue

        if "://" in raw_token:
            continue

        token = raw_token.strip("`*_[](){}<>\"'.,;:!")
        if not token or token == "?":
            continue

        if token.endswith("?") and token.count("?") == 1 and not token.startswith("?"):
            continue

        if QUESTION_MARK_IN_WORD.search(token):
            return True

        if QUESTION_MARK_PREFIX.match(token):
            return True

        if QUESTION_MARK_SHORT_TOKEN.match(token):
            return True

    return False


def main():
    failures = []
    for path in iter_files():
        findings = find_suspicious_lines(path)
        if findings:
            failures.append((path, findings))

    if not failures:
        print("OK: Ingen tegnkodingsfeil funnet i validerte tekstfiler.")
        return 0

    print("FEIL: Fant mistenkelige tegnkodingssekvenser i tekstfiler:")
    for path, findings in failures:
        print(f"- {path}")
        for lineno, line in findings[:10]:
            print(f"  Linje {lineno}: {line}")
        if len(findings) > 10:
            print(f"  ... og {len(findings) - 10} flere linjer")
    return 1


if __name__ == "__main__":
    sys.exit(main())
