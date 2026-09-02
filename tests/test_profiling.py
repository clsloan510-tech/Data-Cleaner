import pandas as pd

from data_cleaner.profiling import profile_dataframe, quality_summary


def test_profile_counts_missing_and_duplicates():
    df = pd.DataFrame({"id": [1, 2, 2], "name": ["A", None, "B"]})
    profile = profile_dataframe(df)
    assert profile["rows"] == 3
    assert profile["columns"] == 2
    assert profile["duplicate_rows"] == 1
    assert profile["missing_cells"] == 1


def test_quality_score_is_bounded():
    df = pd.DataFrame({"id": [1, 2, 3], "value": [10, 20, 30]})
    score = quality_summary(df).overall_score
    assert 0 <= score <= 100
    assert score == 100.0
