import os

def write_file(working_directory, file_path, content):
    # Construct the absolute path of the target file
    abs_path = os.path.abspath(os.path.join(working_directory, file_path))
    # Get the absolute path of the working directory
    abs_work = os.path.abspath(working_directory)
    # Check if the target file is inside the working directory
    inside = abs_path.startswith(abs_work + os.sep)

    # Ensure the file is within the working directory
    if not inside:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    try:
        # Ensure the directory exists
        dir_name = os.path.dirname(abs_path)
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        
        # Write the content to the file
        with open(abs_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: {e}'