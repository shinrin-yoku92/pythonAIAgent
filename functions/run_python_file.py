import os
import subprocess


def run_python_file(working_directory, file_path, args=[]):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found'
    if not abs_file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        result = subprocess.run(
            ["python3", abs_file_path] + args,
            capture_output=True,
            text=True,
            cwd=abs_working_dir,
            timeout=30,
        )
        stdout_text = result.stdout.strip()
        stderr_text = result.stderr.strip()
        output = f'STDOUT: {stdout_text}\nSTDERR: {stderr_text}'
        if not stdout_text and not stderr_text:
            output = "No output produced"
        if result.returncode != 0:
            return output + f'\nProcess exited with code {result.returncode}'
        return output
        
    except subprocess.TimeoutExpired:
        return f'Error: Execution of "{file_path}" timed out'
    except Exception as e:
        return f'Error executing "{file_path}": {e}'
    