import os

def validate_file(file_path:str,allowed_extensions:list[str])->bool:
    '''
    Validate a file before processing
    Args:
       file_path: Path of the uploaded file
       allowed_extensions: List of allowed file extensions.
    Returns:
       True if the file passes validation, otherwise False.
    '''
    # File Existence CheckPoint
    file_exists = os.path.exists(file_path)
    if not file_exists:
        return False