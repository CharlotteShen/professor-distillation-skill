# Demonstrating Subagents With Synthetic Data

The public demo uses invented records only. It demonstrates the role behavior, not real professor knowledge.

## Corpus Readiness Levels

- `starter`: 1-2 digested papers. Use `paper_analyst`, cautious `librarian`, and `evidence_auditor` checks only.
- `usable`: 5-10 digested papers. Add early theme retrieval, simple meeting prep, and narrow synthesis.
- `strong`: 20+ digested papers with page-grounded claims. Add cross-paper synthesis, gap generation, manuscript review, writing-style pattern extraction, and external-gap screening.

A role can run earlier, but its conclusions must be narrower and lower-confidence.

## Synthetic Demo Files

Use files under `assets/templates/demo-corpus/`:

- `catalog.csv`: six invented papers.
- `claims.jsonl`: eighteen invented page-grounded claims.
- `methods.jsonl`: six invented methods.
- `research_gaps.jsonl`: three invented candidate gaps.

All IDs start with `synthetic_`. All evidence text is synthetic and written for this demo.

## Sample Prompts

### Librarian

```text
Use the professor-distillation librarian role on assets/templates/demo-corpus. Find synthetic evidence about adaptive damping and report doc_id, page, confidence, and extraction quality. Do not infer absence if retrieval misses.
```

### Paper Analyst

```text
Use the paper analyst role for synthetic_2026_frame_damping. Produce a structured note from the synthetic claims and methods only. Mark missing equation or figure evidence as not visually verified.
```

### Synthesis Analyst

```text
Use the synthesis analyst role on all synthetic_* demo records. Summarize recurring themes across adaptive damping, sensor placement, and meeting-prep validation. Cite synthetic evidence IDs.
```

### Evidence Auditor

```text
Use the evidence auditor role to inspect a draft claim: "The synthetic corpus proves adaptive damping is always best." Identify overclaiming and cite which synthetic records do or do not support it.
```

### Manuscript Reviewer

```text
Use the manuscript reviewer role to critique this synthetic abstract against the demo corpus: "We propose a controller and validate it numerically." Focus on novelty, assumptions, validation, and missing evidence.
```

### Gap Generator

```text
Use the gap generator role on the synthetic demo corpus. Propose two cautious research gaps with evidence IDs, novelty risk, minimum study, and confidence.
```

### External Gap Checker

```text
Use the external gap checker role to design search queries for synthetic_gap_001. Do not claim novelty; only prepare the screening plan.
```

### Meeting Prep

```text
Use the meeting prep role to prepare a 10-minute meeting from the synthetic demo corpus. Include claims to mention, likely objections, and what not to overclaim.
```

### Writing-Style Analyst

```text
Use the writing-style analyst role on synthetic notes only. Extract structural guidance such as problem-framing order and validation-story pattern without imitating prose.
```

## Example Output Shape

A librarian-style demo answer should stay compact and evidence-indexed:

```text
Query/topic: adaptive damping

Matches:
- synthetic_claim_001 | doc_id: synthetic_2026_frame_damping | location: page 2 | evidence_type: explicit | confidence: high | extraction_quality: B
  Use: supports a synthetic claim that adaptive damping reduced peak drift in the benchmark frame.
- synthetic_claim_002 | doc_id: synthetic_2026_frame_damping | location: page 3 | evidence_type: explicit | confidence: high | extraction_quality: B
  Use: supports a synthetic limitation about delay-sensitive controller tuning.

Limitation: this is a six-document synthetic demo, so it is usable for role behavior but not strong enough for real gap or manuscript claims.
```

## Expected Demo Discipline

Every demo answer should cite synthetic evidence IDs, state confidence and limitations, and say when the synthetic corpus is too small for a role's stronger conclusions.
