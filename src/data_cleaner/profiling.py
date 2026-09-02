"""Dataset profiling primitives used by the quality-report layer."""

from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any

import pandas as pd


@dataclass(frozen=True)
class QualitySummary:
    rows: int
    columns: int
    missing_rate: float
    duplicate_rate: float
    numeric_valid_rate: float
    overall_score: float

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def profile_dataframe(df: pd.DataFrame) -> dict[str, Any]:
    """Return a JSON-serializable structural profile of a DataFrame."""
    rows, columns = df.shape
    missing = df.isna().mean().mean() if rows and columns else 0.0
    duplicate_rate = float(df.duplicated().mean()) if rows else 0.0

    column_profile: dict[str, dict[str, Any]] = {}
    for name in df.columns:
        series = df[name]
        column_profile[str(name)] = {
            "dtype": str(series.dtype),
            "missing_count": int(series.isna().sum()),
            "missing_rate": float(series.isna().mean()) if rows else 0.0,
            "unique_count": int(series.nunique(dropna=True)),
            "unique_rate": float(series.nunique(dropna=True) / rows) if rows else 0.0,
        }

    return {
        "rows": rows,
        "columns": columns,
        "duplicate_rows": int(df.duplicated().sum()),
        "missing_cells": int(df.isna().sum().sum()),
        "columns_profile": column_profile,
    }


def quality_summary(df: pd.DataFrame) -> QualitySummary:
    """Compute a transparent baseline quality score.

    This score is intentionally simple: it is a screening metric, not a claim of
    ground-truth data accuracy. Domain-specific validators should augment it.
    """
    rows, columns = df.shape
    if not rows or not columns:
        return QualitySummary(rows, columns, 0.0, 0.0, 0.0, 0.0)

    missing_rate = float(df.isna().mean().mean())
    duplicate_rate = float(df.duplicated().mean())
    completeness = 1.0 - missing_rate
    uniqueness = 1.0 - duplicate_rate
    overall = 100.0 * (0.7 * completeness + 0.3 * uniqueness)

    return QualitySummary(
        rows=rows,
        columns=columns,
        missing_rate=missing_rate,
        duplicate_rate=duplicate_rate,
        numeric_valid_rate=1.0,
        overall_score=round(overall, 2),
    )
