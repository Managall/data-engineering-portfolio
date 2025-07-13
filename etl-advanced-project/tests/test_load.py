# tests/test_load.py
import pandas as pd
import sqlite3
from etl.load import load_data
from config import SQLITE_DB_PATH, SQLITE_DB_NAME

def test_load_data_creates_table(tmp_path):
    db_path = tmp_path / "test.db"
    df = pd.DataFrame({
        "id": [1],
        "nombre": ["ANA"],
        "edad": [28],
        "email": ["ana@example.com"],
        "suscrito": [True]
    })
    
    from etl import load
    load.SQLITE_DB_PATH = str(db_path)
    load.SQLITE_DB_NAME = "users_test"
    
    load_data(df)

    conn = sqlite3.connect(str(db_path))
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users_test")
    rows = cursor.fetchall()
    conn.close()

    assert len(rows) == 1
