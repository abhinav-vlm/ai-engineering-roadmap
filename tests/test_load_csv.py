import pytest
from pathlib import Path
from src.utils.csv_utils import load_csv
from configs.config import RAW_DATA_DIR

def test_load_csv_valid():
    df = load_csv(RAW_DATA_DIR/ "sample.csv")
    assert not df.empty

def test_load_csv_missing():
    with pytest.raises(FileNotFoundError):
        load_csv(RAW_DATA_DIR/'missing.csv')