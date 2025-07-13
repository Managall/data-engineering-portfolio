# tests/test_extract.py
import pandas as pd
import pytest
from etl.extract import extract_data

def test_extract_data_success(tmp_path):
    # Crear un CSV temporal con datos válidos
    d = tmp_path / "data"
    d.mkdir()
    test_file = d / "source_data.csv"
    test_file.write_text("id,nombre,edad,email,suscrito\n1,Ana,28,ana@example.com,True")

    # Reemplazar la ruta esperada para el test
    from etl import extract
    extract.SOURCE_CSV_DATA = str(test_file)

    df = extract_data()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (1, 5)
