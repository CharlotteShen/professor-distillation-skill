# Workflow

## 1. Private Workspace Setup

Create a private project for one professor or research group. Keep raw sources, extracted text, generated notes, search indexes, and meeting outputs out of public repos.

Recommended private layout:

```text
corpus/metadata/catalog.csv
corpus/raw/                 # gitignored
corpus/processed/           # private unless sources are clearly shareable
knowledge_base/claims.jsonl
knowledge_base/methods.jsonl
notes/paper_notes/          # private
notes/synthesis_notes/      # private by default
outputs/                    # gitignored generated artifacts
```

## 2. Corpus Intake

Track each document in a catalog. Use stable `doc_id` values that do not expose private identifiers. Keep reference-manager integration export-only unless the user explicitly asks otherwise.

Minimum catalog fields:

```csv
doc_id,title,authors,year,source_type,relationship_level,venue,doi,url,status,extraction_quality
```

## 3. Text Extraction

Prefer page-grounded extraction. Record extraction quality in a status file. If extraction quality is weak, allow text-level summaries only with caution.

Do not use extracted text as proof for equation, table, or figure claims unless the relevant pages are visually verified or otherwise quality-gated for that claim type.

## 4. Claim Recording

Create page-grounded claim records. Prefer specific claims over generic summaries. Preserve original model labels when calibrating or reviewing labels.

Use JSONL so records remain inspectable and easy to audit.

## 5. Retrieval And Synthesis

Use deterministic local retrieval first: keyword search, SQLite FTS, CSV filters, and direct evidence bundles. Do not treat retrieval misses as evidence that the professor never worked on a topic.

Synthesis should separate:

- explicit source evidence
- repeated corpus patterns
- inference from multiple papers
- speculation or proposed gaps

## 6. Research Roles

Useful role prompts:

- librarian: find documents and evidence IDs
- paper analyst: turn one source into structured evidence
- synthesis analyst: compare themes across papers
- evidence auditor: find unsupported or overconfident claims
- manuscript reviewer: critique drafts against local evidence
- gap generator: propose cautious research opportunities
- meeting prep: prepare agenda, likely questions, and what not to overclaim

Roles organize local evidence. They do not impersonate the professor.

## 7. Meeting Prep

A meeting packet should include:

- papers or claims to mention
- evidence IDs and source pages
- likely professor questions
- concise answer bullets
- unresolved uncertainties
- do-not-overclaim cautions

## 8. Maintenance

After each corpus or claim update:

1. Run a knowledge-base audit.
2. Regenerate synthesis/search artifacts.
3. Spot-check retrieval for the changed topic.
4. Update a private handoff note.
5. Keep generated outputs private unless intentionally sanitized.
