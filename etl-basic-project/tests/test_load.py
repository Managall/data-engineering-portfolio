# test/tes_load.py

import os
import pandas as pd
from etl.load import load_data

def test_load_to_sqlite(tmp_path):
    # Crear DataFrame de prueba
    df = pd.DataFrame({
        "heightinches": [70.0, 65.0],
        "weightpounds": [150.0, 130.0]
    })

    db_path = tmp_path / "test.db"
    table_name = "health_data"


    load_data(df, str(db_path),table_name)

    assert db_path.exists()

    