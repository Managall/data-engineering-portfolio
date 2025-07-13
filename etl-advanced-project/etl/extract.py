# etl/extract.py
import pandas as pd
from config import SOURCE_CSV_DATA, EXPECTED_COLUMNS
from etl.logger import logger

def extract_data():
    try:
        df = pd.read_csv(SOURCE_CSV_DATA)
        missing_cols = [col for col in EXPECTED_COLUMNS if col not in df.columns]
        if missing_cols:
            raise ValueError(f"Columnas faltantes en el CSV: {missing_cols}")
        
        logger.info(f"[Extract] Datos extraídos correctamente desde: {SOURCE_CSV_DATA}")
        return df
    
    except Exception as e:
        logger.error(f"[Extract][Error] No se puede leer el archivo: {e}")
