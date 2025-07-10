# etl/transform.py

from .logger import logger

def transform_data(df):
    logger.info("[Transform] Iniciando transformación de datos...")

    # Limpiar nombres de las columnas
    df.columns = (
    df.columns
    .str.strip()  # elimina espacios al inicio y fin
    .str.replace('"', '')  # elimina comillas dobles
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("(", "")
    .str.replace(")", "")
    )

    # Validar columnas esperadas
    expected_columns = {"index","heightinches","weightpounds"}
    actual_columns = set(df.columns)
    
    if not expected_columns.issubset(actual_columns):
        logger.error(f"[Transform] Columnas faltantes, Esperadas: {expected_columns}, Encontradas: {actual_columns}")
        return None
    
    # Limpieza y conversión de tipos
    df = df.dropna()
    try:
        df["heightinches"] = df["heightinches"].astype(float)
        df["weightpounds"] = df["weightpounds"].astype(float)
    except Exception as e:
        logger.error("[Transform] Transformaciones aplicadas correctamente.")
        return None

    logger.info("[Transform] Transformaciones completadas.")
    return df

