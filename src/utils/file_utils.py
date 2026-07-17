from pathlib import Path
def validate_file(file_path:str|Path,allowed_extensions:list[str])->bool:
   '''
    Validate a file before processing
    Args:
       file_path: Path of the uploaded file
       allowed_extensions: List of allowed file extensions.
    Returns:
       True if the file passes validation, otherwise False.
   '''
    # File Existence CheckPoint
   path = Path(file_path)
   if not path.exists():
      return False
   allowed = {ext.lower() for ext in allowed_extensions}
   if path.suffix.lower() not in allowed:
      return False
   return True