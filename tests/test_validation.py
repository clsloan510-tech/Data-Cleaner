import pandas as pd

from data_cleaner.validation import not_null, range_check, require_columns, unique


def test_required_columns():
    df = pd.DataFrame({"id": [1]})
    assert require_columns(df, ["id"]).passed
    assert not require_columns(df, ["id", "name"]).passed


def test_not_null_and_unique():
    df = pd.DataFrame({"id": [1, 2], "name": ["A", None]})
    assert not not_null(df, "name").passed
    assert unique(df, "id").passed


def test_range_check_inclusive():
    df = pd.DataFrame({"score": [0, 50, 100, 101]})
    result = range_check(df, "score", 0, 100)
    assert not result.passed
    assert result.violations == 1
