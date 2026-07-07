# Evidence Contract

## Claim Record

Use one JSON object per line:

```json
{
  "claim_id": "synthetic_2026_active_control_ext_001",
  "doc_id": "synthetic_2026_active_control",
  "claim": "The paper reports a laboratory validation of a controller on a two-story frame.",
  "page": 3,
  "location": "page 3",
  "quote_or_paraphrase": "Paraphrase of the local source passage, not copied from a real paper.",
  "evidence_type": "explicit",
  "confidence": "high",
  "extraction_quality_used": "B",
  "topic_tags": ["active control", "experimental validation"],
  "generated_by": "local_claim_extraction"
}
```

## Evidence Types

- `explicit`: directly stated by the source and grounded to a page or section.
- `pattern`: repeated across multiple local sources.
- `inference`: reasoned from evidence but not directly stated.
- `speculation`: a possible idea or gap, not a factual claim.

## Confidence

- `high`: strong page-grounded support and good extraction quality.
- `medium`: grounded but paraphrased, indirect, or extraction quality is imperfect.
- `low`: weak extraction, unclear page support, or unresolved ambiguity.

Do not mark an inference as high confidence unless the project deliberately defines and audits that policy.

## Required Output Discipline

For every substantive claim, include:

- citation or evidence ID
- `doc_id`
- page/location when available
- evidence type
- confidence
- extraction quality or visual-verification caveat

## Visual Gate

Equation, table, and figure claims need page-level visual verification. Text extraction can support text-level claims, but it is not enough for display-level details unless a local quality gate explicitly says so.

## Retrieval Misses

Say "I did not retrieve supporting evidence from the current local corpus" instead of "the professor has not worked on this." A corpus can be incomplete, metadata can be sparse, and search terms can miss relevant work.
