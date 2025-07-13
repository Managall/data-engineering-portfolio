# etl/load.py
# -
import sqlite3
from config import SQLITE_DB_PATH, SQLITE_DB_NAME
from etl.logger import logger

def load_data(df):
    try:
        conn = sqlite3.connect(SQLITE_DB_PATH)
        df.to_sql(SQLITE_DB_NAME, conn, if_exists='replace', index=False)
        conn.close()
        logger.info(f"[Load] Datos cargados correctamente en la tabla '{SQLITE_DB_NAME}' de la base de datos '{SQLITE_DB_PATH}'" )
    except Exception as e:
        logger.error(f"[Load][Error] No se pudo cargar los datos: {e}")