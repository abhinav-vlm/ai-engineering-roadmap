from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

DATA_DIR = BASE_DIR / "data"

RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
EXTERNAL_DATA_DIR = DATA_DIR / "external"

MODELS_DIR = BASE_DIR / "models"

ALLOWED_EXTENSIONS = {'.csv'}