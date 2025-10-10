import os

def get_files_info(working_directory, directory="."):
    # This function retrieves information about files in the specified directory.
    dir_path = os.path.join(working_directory, directory)
    
    
    
    files_info = []

    for root, dirs, files in os.walk(dir_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_info = {
                "name": filename,
                "path": file_path,
                "size": os.path.getsize(file_path),
                "is_directory": False
            }
            files_info.append(file_info)

    return files_info
