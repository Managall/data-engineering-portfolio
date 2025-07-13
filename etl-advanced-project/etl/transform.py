# etl/trnsform.py
import pandas as pd
from etl.logger import logger

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("[Transform] Iniciando transformación de datos...")

    # Estandarizar el nombre a formato Title (Primera letra en mayúscula)
    df['nombre'] = df['nombre'].str.title()

    # Convertir el campo 'suscrito' en booleano si no lo es
    df['suscrito'] = df['suscrito'].apply(lambda x: str(x).lower() in ['true', '1', 'yes'])

    logger.info("[Transform] Transformación completada.")
    return df