import pytest
from pathlib import Path
from src.utils.csv_utils import load_csv,summarize_csv
from configs.config import RAW_DATA_DIR

def test_summarize_csv():
    df = load_csv(RAW_DATA_DIR/ "sample.csv")
    summary = summarize_csv(df)
    assert isinstance (summary,dict)
    assert "rows" in summary
    assert "columns" in summary
    assert "column_names" in summary
    assert "missing_values" in summary