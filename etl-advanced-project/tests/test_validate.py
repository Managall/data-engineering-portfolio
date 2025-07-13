# tests/test_validate.py
import pandas as pd
import pytest
from etl.validate import validate_data

def test_validate_data_success():
    data = {
        "id": [1, 2],
        "nombre": ["Ana", "Beto"],
        "edad": [28, 35],
        "email": ["ana@example.com", "beto@example.com"],
        "suscrito": [True, False]
    }
    df = pd.DataFrame(data)
    result = validate_data(df)
    assert result.shape[0] == 2
    assert "edad" in result.columns
