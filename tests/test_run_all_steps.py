import pytest
from src.run_all_steps import check_file_exists, run_script
import os

def test_check_file_exists():
    file_path = 'config/.env'
    check_file_exists(file_path)
    assert os.path.exists(file_path)

def test_run_script():
    script_name = 'src/data_collection.py'
    run_script(script_name)
    assert True

