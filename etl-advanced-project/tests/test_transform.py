# tests/test_transform.py
import pandas as pd
from etl.transform import transform_data

def test_transform_data_uppercase():
    data = {
        "id": [1],
        "nombre": ["ana"],
        "edad": [28],
        "email": ["ana@example.com"],
        "suscrito": [True]
    }
    df = pd.DataFrame(data)
    transformed = transform_data(df)
    assert transformed["nombre"].iloc[0] == "Ana"
