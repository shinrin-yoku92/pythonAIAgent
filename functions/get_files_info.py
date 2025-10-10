import os

# This function retrieves information about files in the specified directory.
def get_files_info(working_directory, directory="."):
    # Construct the absolute path of the target directory
    dir_path = os.path.join(working_directory, directory)
    # Get absolute paths for comparison
    abs_path = os.path.abspath(dir_path)
    # Get the absolute path of the working directory
    abs_work = os.path.abspath(working_directory)
    # Check if the target directory is inside the working directory
    inside = (abs_path == abs_work)  or abs_path.startswith(abs_work + os.sep)

    # Ensure the directory is within the working directory
    if not inside:
        return (f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    
    # Ensure the directory exists and is a directory
    if not os.path.isdir(abs_path):
        return (f'Error: "{directory}" is not a directory')

    try:
        entries = os.listdir(abs_path)
        lines = []
        for name in entries:
            p = os.path.join(abs_path, name)
            size = os.path.getsize(p)
            is_dir = os.path.isdir(p)
            lines.append(f'- {name}: file_size={size} bytes, is_dir={is_dir}')
        return "\n".join(lines)
    except Exception as e:
        return (f'Error: {e}')
