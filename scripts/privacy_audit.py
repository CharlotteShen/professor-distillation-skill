#!/usr/bin/env python3
"""Conservative public-release audit for this skill repo."""

from __future__ import annotations

import re
import sys
from pathlib import Path

BLOCKED_DIRS = {
    ".git",
    "corpus",
    "knowledge_base",
    "notes",
    "outputs",
    "downloads",
    "papers",
    "raw",
    "processed",
    "indexes",
    "secrets",
}

BLOCKED_SUFFIXES = {
    ".pdf",
    ".enl",
    ".ris",
    ".bib",
    ".sqlite",
    ".db",
    ".rtf",
    ".key",
    ".pem",
}

BLOCKED_FILENAMES = {
    "page_text.jsonl",
    "canonical.md",
    "local_tools.yaml",
    ".env",
}

PATTERNS = [
    ("private absolute path", re.compile(r"/Users/[^\s)>'\"]+")),
    ("windows absolute path", re.compile(r"[A-Za-z]:\\\\Users\\\\")),
    ("api key marker", re.compile(r"(?i)(api[_-]?key|secret|token|password)\s*[:=]")),
    ("openai key", re.compile(r"sk-[A-Za-z0-9_-]{20,}")),
    ("anthropic key", re.compile(r"sk-ant-[A-Za-z0-9_-]{20,}")),
    ("github token", re.compile(r"gh[pousr]_[A-Za-z0-9_]{20,}")),
    ("private scaffold marker", re.compile(r"(?i)(distillation scaffold|worktrees|recursing-dijkstra|claude/thesis|supervisor)")),
    ("specific private professor marker", re.compile(r"(?i)(songye\s+zhu|hong kong polytechnic|hk polyu|polyu)")),
    ("mineru secret marker", re.compile(r"(?i)(mineru_api_key|mineru_exceed_limit|mineru.*backup)")),
    ("endnote private marker", re.compile(r"(?i)(\.enl|endnote library|library\.ris)")),
]

TEXT_SUFFIXES = {
    "",
    ".md",
    ".txt",
    ".py",
    ".yaml",
    ".yml",
    ".json",
    ".jsonl",
    ".csv",
    ".gitignore",
}

ALLOW_PATTERN_LABELS = {
    "professor-distillation/references/privacy-and-release.md": {
        "api key marker",
        "private scaffold marker",
        "endnote private marker",
    },
    "README.md": {"api key marker", "private scaffold marker", "endnote private marker"},
    "AGENTS.md": {"api key marker", "private scaffold marker", "endnote private marker"},
    "CLAUDE.md": {"api key marker", "private scaffold marker", "endnote private marker"},
    ".gitignore": {"endnote private marker"},
    # The audit script must contain the denylist literals it enforces.
    "scripts/privacy_audit.py": {
        "api key marker",
        "private absolute path",
        "private scaffold marker",
        "specific private professor marker",
        "mineru secret marker",
        "endnote private marker",
    },
}


def iter_files(root: Path):
    for path in root.rglob("*"):
        rel = path.relative_to(root)
        if any(part in BLOCKED_DIRS for part in rel.parts):
            if path.is_file() and ".git" not in rel.parts:
                yield path
            continue
        if path.is_file():
            yield path


def audit(root: Path) -> list[str]:
    findings: list[str] = []
    for path in iter_files(root):
        rel = path.relative_to(root).as_posix()
        parts = set(path.relative_to(root).parts)
        if parts & BLOCKED_DIRS and ".git" not in parts:
            findings.append(f"blocked directory content: {rel}")
        if path.name in BLOCKED_FILENAMES:
            findings.append(f"blocked filename: {rel}")
        if path.suffix.lower() in BLOCKED_SUFFIXES:
            findings.append(f"blocked suffix: {rel}")
        if path.stat().st_size > 250_000:
            findings.append(f"unexpected large file: {rel}")
        suffix = path.suffix.lower() or path.name if path.name == ".gitignore" else path.suffix.lower()
        if suffix not in TEXT_SUFFIXES and path.name != ".gitignore":
            findings.append(f"unexpected non-text file type: {rel}")
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            findings.append(f"non-utf8 file: {rel}")
            continue
        allowed_labels = ALLOW_PATTERN_LABELS.get(rel, set())
        for label, pattern in PATTERNS:
            if label in allowed_labels:
                continue
            for match in pattern.finditer(text):
                line = text.count("\n", 0, match.start()) + 1
                findings.append(f"{label}: {rel}:{line}")
    return findings


def main(argv: list[str]) -> int:
    root = Path(argv[1] if len(argv) > 1 else ".").resolve()
    findings = audit(root)
    if findings:
        for finding in findings:
            print(f"FAIL: {finding}")
        return 1
    print(f"OK: privacy audit clean for {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
