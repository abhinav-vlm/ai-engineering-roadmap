from configs.logging_config import logger
import pandas as pd 
from pathlib import Path

def load_csv(csv_path:str|Path)->pd.DataFrame:
    '''
    Load the Csv file into pandas DataFrame

    Args:
        csv_path: Path for the file uploaded
    
    Returns:
        A Pandas DataFrame with the file data inside it

    Raises:
        FileNotFoundError: If the file does not exist
        TypeError: If the file extension does not match
    '''
    try:
       csv_path = Path(csv_path) 
       df = pd.read_csv(csv_path)
       return df
    except FileNotFoundError:
        logger.error("CSV file not found: %s",csv_path)
        raise
    except TypeError:
        logger.error("csv_path must be a string or Path object")
        raise
    
def summarize_csv(df:pd.DataFrame)->dict:
    '''
    Generate summary statistics for a pandas DataFrame

    Args:
        DataFrame: A Pandas DataFrame given by the the load_csv function

    Returns:
        dict: A dictionary of rows,columns,column_names,missing_values
    '''
    rows,columns = df.shape
    column_names = df.columns.tolist()
    missing_values = df.isnull().sum().to_dict()
    return {
        'rows':rows,
        'columns':columns,
        "column_names":column_names,
        'missing_values':missing_values
    }