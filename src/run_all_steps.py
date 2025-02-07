import os
import subprocess

def check_file_exists(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f'File not found: {file_path}')

def run_script(script_name):
    subprocess.run(['python', script_name], check=True)

