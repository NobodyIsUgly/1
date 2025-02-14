import pytest
from src.train_model import build_model, train_model, evaluate_model
import pandas as pd

def test_build_model():
    input_shape = 3
    model = build_model(input_shape)
    assert model is not None
    assert len(model.layers) == 3

def test_train_model():
    model = build_model(3)
    X_train = pd.DataFrame([[2.0, 4.0, 6.0], [3.0, 5.0, 7.0]])
    y_train = pd.DataFrame([1, 0])
    train_model(model, X_train, y_train)
    assert model.history is not None

def test_evaluate_model():
    model = build_model(3)
    X_test = pd.DataFrame([[2.0, 4.0, 6.0], [3.0, 5.0, 7.0]])
    y_test = pd.DataFrame([1, 0])
    evaluate_model(model, X_test, y_test)
    assert 'accuracy' in model.metrics_names

