from pathlib import Path
from utils import validate_file,load_csv,summarize_csv

allowed_extensions = ['.csv']

def print_summary(summary,csv_path):
    file = Path(csv_path).name
    print(f"File:{file}")
    # if this functioon ran means file is valid
    print("Status: Valid")
    print(f"Rows:{summary['rows']}")
    print(f"Columns:{summary['columns']}")
    print("Columns:")
    for cols in summary['column_names']:
        print(f'-{cols}')
    print(f"Missing Values:{summary['missing_values'].items}")
    for column,count in summary['missing_values']:
        print(f"{column}:{count}")
def main():
    # Build csv path
    BASE_DIR = Path(__file__).resolve().parent.parent
    csv_path = BASE_DIR/'data'/'raw'/'sample.csv'

    # Validate
    if not validate_file(csv_path,allowed_extensions):
       print("Invalid File")
       exit()

    # Load CSV
    df = load_csv(csv_path)

    # Summarize CSV
    summary = summarize_csv(df)

    # Print Summary
    print_summary(summary,csv_path)