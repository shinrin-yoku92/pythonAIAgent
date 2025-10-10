import os
from config import MAX_CHARS

# This function retrieves the content of a specified file.
def get_file_content(working_directory, file_path):
    # Construct the absolute path of the target file
    abs_path = os.path.abspath(os.path.join(working_directory, file_path))
    # Get the absolute path of the working directory
    abs_work = os.path.abspath(working_directory)
    # Check if the target file is inside the working directory
    inside = (abs_path == abs_work) or abs_path.startswith(abs_work + os.sep)

    # Ensure the file is within the working directory
    if not inside:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    # Ensure the file exists and is a file
    if not os.path.isfile(abs_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    # Read and return the file content
    try:
        with open(abs_path, 'r', encoding='utf-8') as f:
            content = f.read(MAX_CHARS + 1)  # Read one extra character to check for truncation
        if len(content) > MAX_CHARS:
            content = content[:MAX_CHARS] + f'[...File "{file_path}" truncated at 10000 characters]'
        return content
    except Exception as e:
        return f'Error: {e}'