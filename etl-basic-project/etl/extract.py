# etl/extract.py

import pandas as pd

def extract_data(filepath):
    """Carga el archivo CSV y retorna un DataFrame."""
    try:
        df = pd.read_csv(filepath)
        print(f"[Extract] Datos extraídos correctamente desde: {filepath}")
        return df
    except Exception as e:
        print(f"[Extract][Error] No se pudo leer el archivo: {e}")
        return None
