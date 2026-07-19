from configs.logging_config import logger
import pandas as pd 
from pathlib import Path

def load_csv(csv_path:str|Path)->pd.DataFrame:
    csv_path = Path(csv_path) 
    try:
       df = pd.read_csv(csv_path)
       return df
    except FileNotFoundError:
        logger.error("CSV file not found: %s",csv_path)
        raise
    except TypeError:
        logger.error("csv_path must be a string or Path object")
        raise
    
def summarize_csv(df:pd.DataFrame)->dict:
    rows,columns = df.shape
    column_names = df.columns.tolist()
    missing_values = df.isnull().sum().to_dict()
    return {
        'rows':rows,
        'columns':columns,
        "column_names":column_names,
        'missing_values':missing_values
    }