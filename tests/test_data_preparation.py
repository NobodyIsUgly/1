import pytest
from src.data_preparation import load_data, validate_data, prepare_data
import pandas as pd

def test_load_data():
    file_path = 'data/processed/match_data.csv'
    data = load_data(file_path)
    assert data is not None
    assert not data.empty

def test_validate_data():
    data = {
        'outcome': [1, 0, 1],
        'feature1': [2.0, 3.0, None],
        'feature2': [4.0, None, 6.0],
        'feature3': [7.0, 8.0, 9.0]
    }
    df = pd.DataFrame(data)
    validated_data = validate_data(df)
    assert validated_data is not None
    assert not validated_data empty

def test_prepare_data():
    data = {
        'outcome': [1, 0, 1],
        'feature1': [2.0, 3.0, 4.0],
        'feature2': [4.0, 5.0, 6.0],
        'feature3': [7.0, 8.0, 9.0]
    }
    df = pd.DataFrame(data)
    X_train, X_test, y_train, y_test = prepare_data(df)
    assert X_train is not None
    assert X_test is not None
    assert y_train is not None
    assert y_test is not None

