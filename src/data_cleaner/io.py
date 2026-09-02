"""Input/output helpers for common tabular formats."""

from pathlib import Path

import pandas as pd

SUPPORTED_EXTENSIONS = {".csv", ".xlsx", ".xls", ".json", ".parquet"}


def read_table(path: str | Path, **kwargs) -> pd.DataFrame:
    """Read a supported tabular file based on its extension."""
    path = Path(path)
    suffix = path.suffix.lower()
    if suffix not in SUPPORTED_EXTENSIONS:
        raise ValueError(f"Unsupported file type: {suffix or '<none>'}")
    if suffix == ".csv":
        return pd.read_csv(path, **kwargs)
    if suffix in {".xlsx", ".xls"}:
        return pd.read_excel(path, **kwargs)
    if suffix == ".json":
        return pd.read_json(path, **kwargs)
    return pd.read_parquet(path, **kwargs)
