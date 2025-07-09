# etl/load.py

import sqlite3

def load_data(df, db_path):
    """Guarda el DataFrame en una base de datos SQLite."""
    try:
        conn = sqlite3.connect(db_path)
        df.to_sql("health_data", conn, if_exists="replace", index=False)
        conn.close()
        print(f"[Load] Datos cargados correctamente en la base: {db_path}")
    except Exception as e:
        print(f"[Load][Error] No se pudo cargar a la base de datos: {e}")
