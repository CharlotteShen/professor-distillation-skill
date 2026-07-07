---
name: professor-distillation
description: Local-first professor research distillation workflow for research students. Use when setting up or operating a private citation-grounded knowledge base for a professor's corpus, including document intake, extraction quality checks, claim recording, evidence retrieval, synthesis, manuscript critique, research-gap generation, and meeting prep. Also use when auditing such a workflow for privacy, evidence discipline, and non-impersonation.
---

# Professor Distillation

Build and operate a private, local-first research distillation workflow around a professor's corpus.

## Core Rules

- Keep corpus data private and local.
- Do not impersonate the professor or claim private knowledge.
- Do not commit PDFs, extracted page text, EndNote libraries/exports, real notes, private claims, secrets, or generated outputs.
- Cite evidence for every substantive research claim.
- Carry `doc_id`, page/location, quote/paraphrase, `evidence_type`, `confidence`, and extraction quality.
- Treat retrieval misses as misses, not evidence of absence.
- Warn before equation/table/figure claims unless relevant pages are visually verified.
- Prefer deterministic local files: CSV, SQLite, Markdown, JSON, JSONL.
- Do not require OpenAI API, vector search, or full RAG for the baseline workflow.

## Workflow

1. For setup or end-to-end operation, read `references/workflow.md`.
2. For claims, confidence, retrieval, and visual-gate rules, read `references/evidence-contract.md`.
3. Before publishing or sharing any derivative, read `references/privacy-and-release.md` and run the audit scripts.
4. Use `assets/templates/` as starter files for a private downstream workspace.

## Agent Outputs

When answering with this skill, keep evidence and uncertainty visible:

- What local artifacts were read.
- Which claims are explicit evidence versus inference.
- Which source pages or records support each claim.
- Which claims are blocked pending extraction or visual verification.
- Which outputs are safe to commit and which must stay private.
