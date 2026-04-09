from __future__ import annotations

import argparse
import shutil
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


SUSPICIOUS_TOKENS = ("\u00c3", "\u00c2", "\u00e2", "\ufffd")
DEFAULT_EXTENSIONS = {".md", ".yaml", ".yml", ".toml", ".json", ".txt", ".py", ".ps1", ".html"}
DEFAULT_EXCLUDE_DIRS = {".git", "node_modules", ".venv", "venv"}

# Targeted replacements for residual artifacts that are not always solved by reinterpretation.
TARGETED_REPLACEMENTS = {
    "\ufffd?": "-",
    "\ufffd.rsaken": "\u00c5rsaken",
    "\ufffd.rsak:": "\u00c5rsak:",
    "\ufffd.pne": "\u00c5pne",
    "\ufffd.pen": "\u00c5pen",
    "\ufffd~ker": "\u00d8ker",
    "\ufffd~kosystemet": "\u00d8kosystemet",
    "\ufffd~kt": "\u00d8kt",
    "\ufffd~nsket": "\u00d8nsket",
    "\ufffd~vrige": "\u00d8vrige",
    "DF\ufffd~": "DF\u00d8",
    "f\ufffdrsteutkast": "f\u00f8rsteutkast",
}


@dataclass
class Change:
    path: Path
    before_score: int
    after_score: int


def suspicious_score(text: str) -> int:
    return sum(text.count(token) for token in SUSPICIOUS_TOKENS)


def latin1_reinterpret_if_better(text: str) -> tuple[str, bool]:
    before = suspicious_score(text)
    if before == 0:
        return text, False

    try:
        candidate = text.encode("latin-1").decode("utf-8")
    except UnicodeError:
        return text, False

    after = suspicious_score(candidate)
    return (candidate, after < before)


def apply_targeted_replacements(text: str) -> str:
    updated = text
    for old, new in TARGETED_REPLACEMENTS.items():
        updated = updated.replace(old, new)
    return updated


def iter_text_files(root: Path, extensions: set[str]) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in DEFAULT_EXCLUDE_DIRS for part in path.parts):
            continue
        if path.suffix.lower() in extensions:
            files.append(path)
    return files


def build_backup_path(backup_root: Path, repo_root: Path, file_path: Path) -> Path:
    relative = file_path.relative_to(repo_root)
    return backup_root / relative


def main() -> int:
    parser = argparse.ArgumentParser(description="Safely repair likely mojibake in text files.")
    parser.add_argument("--root", default=".", help="Repo root to scan.")
    parser.add_argument("--apply", action="store_true", help="Write changes to disk. Default is dry-run.")
    parser.add_argument("--no-backup", action="store_true", help="Do not create backups when applying.")
    args = parser.parse_args()

    repo_root = Path(args.root).resolve()
    files = iter_text_files(repo_root, DEFAULT_EXTENSIONS)

    changes: list[Change] = []
    writes: list[tuple[Path, str]] = []

    for path in files:
        original = path.read_text(encoding="utf-8")
        before = suspicious_score(original)

        rewritten, improved = latin1_reinterpret_if_better(original)
        if improved:
            candidate = rewritten
        else:
            candidate = original

        candidate = apply_targeted_replacements(candidate)
        after = suspicious_score(candidate)

        if candidate != original and after <= before:
            changes.append(Change(path=path, before_score=before, after_score=after))
            writes.append((path, candidate))

    print(f"Scanned files: {len(files)}")
    print(f"Candidate changes: {len(changes)}")

    for item in changes[:50]:
        rel = item.path.relative_to(repo_root)
        print(f"- {rel} ({item.before_score} -> {item.after_score})")
    if len(changes) > 50:
        print(f"... and {len(changes) - 50} more")

    if not args.apply:
        print("Dry-run complete. Re-run with --apply to write changes.")
        return 0

    backup_root: Path | None = None
    if not args.no_backup:
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        backup_root = repo_root / ".backups" / "encoding" / timestamp
        backup_root.mkdir(parents=True, exist_ok=True)

    for path, content in writes:
        if backup_root is not None:
            backup_path = build_backup_path(backup_root, repo_root, path)
            backup_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, backup_path)
        path.write_text(content, encoding="utf-8")

    if backup_root is not None:
        print(f"Backups written to: {backup_root}")
    print("Apply complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
