from pathlib import Path
from configs.logging_config import logger
from configs.config import ALLOWED_EXTENSIONS

def validate_file(file_path:str|Path)->bool:
   '''
   Validate a file before processing
   Args:
      file_path: Path of the uploaded file
      allowed_extensions: List of allowed file extensions.
   Returns:
      True if the file passes validation.

   Raises:
      FileNotFoundError: If the file does not exist.
      ValueError: If the file extension is not allowed.
   '''
    # File Existence CheckPoint
   path = Path(file_path)
   if not path.exists():
      logger.error("Validation Failed: File does not exist.%s",path)
      raise FileNotFoundError(f"File does not exist: {path}")
   allowed = {ext.lower() for ext in ALLOWED_EXTENSIONS}

   if path.suffix.lower() not in allowed:
      logger.error("Validation Failed: Unsupported File extension.%s",path.suffix)
      raise ValueError(f"Unsupported File extension: {path.suffix}")

   return True