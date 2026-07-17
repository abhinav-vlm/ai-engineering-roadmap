import pandas as pd 
from pathlib import Path

csv_path = Path(csv_path)

def load_csv(csv_path:str|Path)->pd.DataFrame:
    df = pd.read_csv(csv_path)
    return df
    
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