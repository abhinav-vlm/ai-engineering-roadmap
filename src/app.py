from pathlib import Path
from utils import validate_file
BASE_DIR = Path(__file__).resolve().parent.parent
csv_path = BASE_DIR/'data'/'raw'/'sample.csv'
allowed_extensions = ['.csv']

if not validate_file(csv_path,allowed_extensions):
    print("Invalid File")
    exit()