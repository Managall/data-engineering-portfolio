# etl/load.py

from .logger import logger
import sqlite3

def load_data(df, db_path, table_name):
    """Guarda el DataFrame en una base de datos SQLite."""
    try:
        conn = sqlite3.connect(db_path)
        df.to_sql(table_name, conn, if_exists="replace", index=False)
        conn.close()
        logger.info(f"[Load] Datos cargados correctamente en la base: {db_path}")
    except Exception as e:
        logger.error(f"[Load][Error] No se pudo cargar a la base de datos: {e}")
