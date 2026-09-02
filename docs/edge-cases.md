# Edge Cases and Safety Checklist

The project should treat data cleaning as a decision system, not a delete-and-fill script.

## Missing data

- Empty strings, whitespace-only values, `NULL`, `None`, and `NaN`
- Numeric zeros that are valid observations
- Sentinel values such as `-999` or `999999`
- Missingness concentrated in one subgroup
- Columns that are entirely missing
- MCAR/MAR/MNAR considerations

## Duplicates

- Exact duplicate rows
- Duplicate IDs with different attributes
- Near-duplicates caused by spelling/formatting differences
- Legitimate repeated transactions
- Duplicate records across files

## Types and formats

- Numbers stored as strings
- Currency symbols and thousands separators
- Percentages represented as `0.25` vs `25%`
- Mixed date formats
- Time zones and daylight-saving transitions
- Leading zeros in identifiers
- Excel cells with mixed inferred types

## Categories and text

- Case differences
- Leading/trailing/internal whitespace
- Punctuation
- Abbreviations
- Misspellings
- Unicode normalization
- Semantically equivalent labels

## Outliers

- Statistical outliers that are legitimate
- Data-entry errors
- Extreme but valid business events
- Multivariate anomalies that univariate rules miss
- Distribution-dependent thresholds

## Joins and entities

- One-to-one vs one-to-many assumptions
- Join explosions
- Missing foreign keys
- Conflicting attributes
- Entity aliases
- Fuzzy-match false positives

## ML safety

- Target leakage
- Temporal leakage
- Train/test contamination
- Fitting imputers/scalers on the full dataset
- Removing minority observations as 'outliers'
- Cleaning away meaningful signal
- Class imbalance

## Automation policy

Automated systems should classify findings as **confirmed**, **probable**, or **ambiguous**. Ambiguous findings should be routed for review rather than silently changed.

Every transformation should be reproducible, logged, and testable.
