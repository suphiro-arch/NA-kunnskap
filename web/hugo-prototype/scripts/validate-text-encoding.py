from pathlib import Path
import sys


SUSPICIOUS_CHARS = {chr(0x00C2), chr(0x00C3), chr(0x00E2), chr(0xFFFD)}
TARGETS = [
    Path("AGENTS.md"),
    Path("README.md"),
    Path("arkitektur"),
    Path("briefs"),
    Path("config/prompts"),
    Path("config/templates"),
    Path("results/Produktbeskrivelser"),
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
        if any(ch in line for ch in SUSPICIOUS_CHARS):
            findings.append((lineno, line.strip()))
    return findings


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
