# Benchmarks

> **Chinese version:** [阅读中文版](README.md)

> Working-class standpoint evaluation questions, machine-readable data, and scoring rules for Worker AI Spark.

---

## Directory contents

| File | Description |
| --- | --- |
| `first-batch.md` | Complete first question set (a core document at manifesto level) |
| `first-batch.zh-CN.jsonl` | Machine-readable 24 basic scenarios (Chinese) |
| `schema.md` | JSONL fields |
| `scoring-rubric.md` | Five dimensions, question grades, and major disqualifying conditions |
| `evaluation-protocol.md` | Multi-model runs, version freezing, human scoring, review, publication |
| `evaluation-record-template.md` | Individual evaluation record template |
| `results/` | Reproducible raw run packages, question scores, batch reports, follow-up plans |

---

## Usage

1. Read `first-batch.md` for rationale and question background.
2. Use `first-batch.zh-CN.jsonl` for batch model queries.
3. Freeze versions, prompts, and parameters under `evaluation-protocol.md`.
4. Score independently by human reviewers using the five dimensions in `scoring-rubric.md`.
5. Use `evaluation-record-template.md` for individual records.
6. Put raw run packages and batch technical reports in `results/`; cross-batch narrative reports may go in `../model-evaluations/`.

---

## Validation

Run all commands from the **repository root**. Validate machine-readable data with
`scripts/validate_benchmarks.py`:

```bash
python scripts/validate_benchmarks.py
```

The default first batch requires exactly 24 questions, unique IDs `WAI-001` … `WAI-024`, valid fields, and nonempty titles/scenarios/questions. Validation also fixes scoring-rule references and privacy levels and prohibits Markdown headings in field values.

An alternative JSONL path may be supplied as the first argument; other files need not have 24 questions. Version 0.2+ records additionally validate co-creation sources, principle links, scoring elements, worker/expert review status and counts, and publication licenses; see [schema.en.md](schema.en.md).

Check Markdown originals against basic JSONL question fields:

```bash
python scripts/validate_benchmark_sources.py
```

Basic-field mismatches cause a nonzero exit. Follow-up questions are reported separately as warnings and never automatically rewritten. Markdown currently contains follow-ups only for questions 1–2, whereas JSONL includes them for all 24, producing 22 source-drift warnings for questions 3–24 pending human review.

General `source_notes` describe the record, not proof that every field has a Markdown source or has been reviewed. Preserve warnings to distinguish basic-question alignment from follow-up adoption; do not remove follow-ups or invent sources just to silence warnings.

The existing [24-question pilot](results/wai-20260825-deepseek-pilot/README.en.md) used only scenarios and main questions. Verification on 2026-09-15 found its input hash matches current JSONL and none of the 72 saved requests appended follow-ups. Before future use, establish their sources and adoption decision, then freeze versions and request scope; do not rewrite past records as though follow-ups ran.

Complete offline standard-library tests:

```bash
python -B -m unittest discover -s scripts -p "test_*.py"
```

---

## Important reminders

- Evaluation is not legal advice; acknowledge regional differences when no jurisdiction is given.
- Major disqualifying issues involving safety, privacy, or basic rights must not be hidden by averages.
- Questions themselves may be biased or incomplete; propose revisions through [the guide](../CONTRIBUTING.en.md).
