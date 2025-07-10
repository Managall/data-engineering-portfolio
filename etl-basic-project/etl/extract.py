# etl/extract.py

from .logger import logger
import pandas as pd

def extract_data(filepath):
    """Carga el archivo CSV y retorna un DataFrame."""
    try:
        df = pd.read_csv(filepath)
        logger.info(f"[Extract] Datos extraídos correctamente desde: {filepath}")
        return df
    except Exception as e:
        logger.error(f"[Extract][Error] No se pudo leer el archivo: {e}")
        return None
