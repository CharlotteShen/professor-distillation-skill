#!/usr/bin/env python3
"""Validate the public professor-distillation skill skeleton."""

from __future__ import annotations

import re
import sys
from pathlib import Path

REQUIRED = [
    "SKILL.md",
    "references/workflow.md",
    "references/evidence-contract.md",
    "references/privacy-and-release.md",
    "assets/templates/catalog.csv",
    "assets/templates/claims.jsonl",
]

NAME_RE = re.compile(r"^[a-z0-9-]+$")


def _frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md missing YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("SKILL.md frontmatter is not closed")
    data: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data


def validate(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    if not skill_dir.is_dir():
        return [f"missing skill directory: {skill_dir}"]
    for rel in REQUIRED:
        if not (skill_dir / rel).is_file():
            errors.append(f"missing required file: {rel}")
    skill_md = skill_dir / "SKILL.md"
    if skill_md.exists():
        try:
            meta = _frontmatter(skill_md.read_text(encoding="utf-8"))
        except ValueError as exc:
            errors.append(str(exc))
        else:
            name = meta.get("name", "")
            desc = meta.get("description", "")
            if not NAME_RE.match(name):
                errors.append("frontmatter name must be lowercase hyphen-case")
            if not desc:
                errors.append("frontmatter description is required")
            if name and skill_dir.name != name:
                errors.append(f"directory name {skill_dir.name!r} must match skill name {name!r}")
    return errors


def main(argv: list[str]) -> int:
    skill_dir = Path(argv[1] if len(argv) > 1 else "professor-distillation")
    errors = validate(skill_dir)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"OK: {skill_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
