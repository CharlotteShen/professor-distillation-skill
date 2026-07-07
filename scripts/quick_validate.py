#!/usr/bin/env python3
"""Validate the public professor-distillation skill skeleton."""

from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

REQUIRED = [
    "SKILL.md",
    "references/workflow.md",
    "references/evidence-contract.md",
    "references/privacy-and-release.md",
    "references/agent-roles.md",
    "references/demo-subagents.md",
    "assets/templates/catalog.csv",
    "assets/templates/claims.jsonl",
    "assets/templates/demo-corpus/catalog.csv",
    "assets/templates/demo-corpus/claims.jsonl",
    "assets/templates/demo-corpus/methods.jsonl",
    "assets/templates/demo-corpus/research_gaps.jsonl",
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


def _jsonl(path: Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path.name}:{line_no} invalid JSON: {exc}") from exc
    return rows


def _validate_demo(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    demo = skill_dir / "assets/templates/demo-corpus"
    catalog_path = demo / "catalog.csv"
    if not catalog_path.exists():
        return ["missing demo catalog"]
    catalog = list(csv.DictReader(catalog_path.open(encoding="utf-8")))
    doc_ids = {row.get("doc_id", "") for row in catalog}
    if len(catalog) != 6:
        errors.append("demo catalog must contain exactly 6 synthetic papers")
    for doc_id in doc_ids:
        if not doc_id.startswith("synthetic_"):
            errors.append(f"demo doc_id must start with synthetic_: {doc_id}")
    claims_path = demo / "claims.jsonl"
    if claims_path.exists():
        try:
            claims = _jsonl(claims_path)
        except ValueError as exc:
            errors.append(str(exc))
            claims = []
        if len(claims) != 18:
            errors.append("demo claims.jsonl must contain exactly 18 claims")
        required = {"doc_id", "claim_id", "page", "location", "evidence_type", "confidence", "extraction_quality_used"}
        for claim in claims:
            missing = sorted(required - claim.keys())
            if missing:
                errors.append(f"demo claim missing fields {missing}: {claim.get('claim_id')}")
            if not str(claim.get("claim_id", "")).startswith("synthetic_"):
                errors.append(f"demo claim_id must start with synthetic_: {claim.get('claim_id')}")
            if claim.get("doc_id") not in doc_ids:
                errors.append(f"demo claim references unknown doc_id: {claim.get('doc_id')}")
    for name in ("methods.jsonl", "research_gaps.jsonl"):
        path = demo / name
        if path.exists():
            try:
                rows = _jsonl(path)
            except ValueError as exc:
                errors.append(str(exc))
                continue
            for row in rows:
                ids: list[str] = []
                for key, value in row.items():
                    if key.endswith("_id"):
                        ids.append(str(value))
                    elif key.endswith("_ids") and isinstance(value, list):
                        ids.extend(str(item) for item in value)
                if not ids or not all(value.startswith("synthetic_") for value in ids):
                    errors.append(f"demo {name} ids must start with synthetic_: {row}")
    return errors


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
    errors.extend(_validate_demo(skill_dir))
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
