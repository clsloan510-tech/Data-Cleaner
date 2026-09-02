# Data-Cleaner

**A data-centric AI laboratory for data quality, cleaning, validation, machine learning, and monitoring.**

Data-Cleaner is designed as both a practical portfolio project and an experimental framework. It demonstrates how raw CSV, Excel, JSON, and tabular datasets can be profiled, cleaned, validated, modeled, and monitored—with measurable evidence of whether each intervention actually improves downstream machine-learning performance.

## Project philosophy

> **Detect → Explain → Propose → Validate → Measure → Monitor**

The project intentionally separates **detection** from **correction**. An unusual value is not automatically an error, and an automated system should not silently rewrite data without validation.

## Planned capabilities

- Automated data profiling and quality scoring
- Missing-value diagnosis and imputation
- Duplicate and near-duplicate detection
- Type, format, schema, and business-rule validation
- Categorical and text normalization
- Date/time validation
- Statistical and ML-based anomaly detection
- Entity resolution and schema matching
- Join/integrity validation
- Label-noise detection
- Feature-quality analysis and leakage detection
- Synthetic corruption with known ground truth
- ML benchmarking before vs. after cleaning
- LLM-assisted cleaning recommendations with validation gates
- Human-in-the-loop review and confidence scoring
- Data drift and schema-drift monitoring
- Explainability and error analysis
- Reproducible transformation logs and data lineage

## Repository roadmap

### Phase 1 — Foundation
1. Project architecture and documentation
2. Dataset registry and profiling engine
3. Data-quality metrics and validation framework
4. Core CSV/XLSX/JSON ingestion
5. Test suite and example datasets

### Phase 2 — Cleaning
6. Missing-data module
7. Duplicate detection
8. Type/format normalization
9. Date/time cleaning
10. Categorical/text cleaning
11. Outlier detection

### Phase 3 — Advanced data-centric ML
12. ML anomaly detection
13. Entity resolution
14. Schema matching
15. Label-noise detection
16. Leakage detection
17. Feature-quality analysis
18. Synthetic corruption benchmark

### Phase 4 — AI + experimentation
19. LLM-assisted cleaning plans
20. Human review workflow
21. Cleaning confidence scores
22. Before/after model benchmark
23. Explainability and error analysis

### Phase 5 — Production-style monitoring
24. Data drift
25. Schema drift
26. Data-quality regression tests
27. Automated reports
28. End-to-end demo pipeline

## Core research question

**How does progressively improving data quality affect the performance, robustness, fairness, and reliability of machine-learning models?**

We will compare pipelines such as:

`Raw → Basic Cleaning → Statistical Cleaning → ML-Assisted Cleaning → Hybrid/LLM-Assisted Cleaning`

Each experiment should report detection quality, correction quality, false positives/negatives, and downstream model performance where ground truth is available.

## Design principles

- Keep raw data immutable.
- Never silently overwrite source data.
- Prefer reversible transformations.
- Record what changed and why.
- Validate every automated correction.
- Distinguish anomalies from confirmed errors.
- Fit preprocessing steps only on training data when modeling.
- Test for leakage before evaluating models.
- Preserve reproducibility.
- Quantify uncertainty and confidence.
- Use human review for ambiguous cases.

## Project status

**Phase 1 — Foundation: In progress**

This repository is being built iteratively. Research notes and implementation decisions will be documented as the project evolves.

## License

MIT License
