"""Explicit, composable validation helpers."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable

import pandas as pd


@dataclass(frozen=True)
class ValidationResult:
    rule: str
    passed: bool
    violations: int
    details: str = ""


def require_columns(df: pd.DataFrame, columns: list[str]) -> ValidationResult:
    """Validate that all required columns exist."""
    missing = [c for c in columns if c not in df.columns]
    return ValidationResult(
        rule="required_columns",
        passed=not missing,
        violations=len(missing),
        details="Missing: " + ", ".join(missing) if missing else "All required columns present",
    )


def not_null(df: pd.DataFrame, column: str) -> ValidationResult:
    """Validate that a column contains no missing values."""
    violations = int(df[column].isna().sum())
    return ValidationResult("not_null", violations == 0, violations, column)


def unique(df: pd.DataFrame, column: str) -> ValidationResult:
    """Validate uniqueness of a column, including duplicate occurrences."""
    violations = int(df[column].duplicated(keep=False).sum())
    return ValidationResult("unique", violations == 0, violations, column)


def range_check(
    df: pd.DataFrame,
    column: str,
    minimum: float | None = None,
    maximum: float | None = None,
) -> ValidationResult:
    """Validate numeric values against optional inclusive bounds."""
    series = pd.to_numeric(df[column], errors="coerce")
    mask = pd.Series(False, index=df.index)
    if minimum is not None:
        mask |= series < minimum
    if maximum is not None:
        mask |= series > maximum
    violations = int(mask.fillna(False).sum())
    return ValidationResult("range", violations == 0, violations, column)


def run_rules(df: pd.DataFrame, rules: list[Callable[[pd.DataFrame], ValidationResult]]) -> list[ValidationResult]:
    """Run validation rules without mutating the input DataFrame."""
    return [rule(df) for rule in rules]
