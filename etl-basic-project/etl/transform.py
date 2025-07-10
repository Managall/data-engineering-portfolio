# etl/transform.py

from .logger import logger

def transform_data(df):
    """Aplica transformaciones simples al DataFrame."""
    logger.info("[Transform] Iniciando transformación de datos...")

    # Renombrar columnas
    df.columns = (
    df.columns
    .str.strip()  # elimina espacios al inicio y fin
    .str.replace('"', '')  # elimina comillas dobles
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("(", "")
    .str.replace(")", "")
    )

    # Eliminar filas con valores faltantes
    df = df.dropna()

    # Convertir a tipos correctos
    try:
        df["heightinches"] = df["heightinches"].astype(float)
        df["weightpounds"] = df["weightpounds"].astype(float)
    except Exception as e:
        logger.error("[Transform] Transformaciones aplicadas correctamente.")
        return None

    logger.info("[Transform] Transformaciones completadas.")
    return df

