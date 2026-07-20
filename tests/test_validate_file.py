import pytest
from pathlib import Path
from src.utils.file_utils import validate_file
from configs.config import RAW_DATA_DIR

def test_validate_file_valid_csv():
    # Arrange
    file_path = RAW_DATA_DIR /"sample.csv"
    # Act
    result = validate_file(file_path)
    # Assert
    assert result is True

def test_validate_file_missing_file():
    # Arrange
    file_path = RAW_DATA_DIR /"missing.csv"
    # Act & Assert
    with pytest.raises(FileNotFoundError):
        validate_file(file_path)  

def test_validate_file_wrong_extension():
    # Arrange
    file_path = RAW_DATA_DIR /"notes.txt"
    # Act & Assert
    with pytest.raises(ValueError):
        validate_file(file_path)