# etl/transform.py

def transform_data(df):
    """Aplica transformaciones simples al DataFrame."""
    print("[Transform] Iniciando transformación de datos...")

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
    df["heightinches"] = df["heightinches"].astype(float)
    df["weightpounds"] = df["weightpounds"].astype(float)

    print("[Transform] Transformaciones aplicadas correctamente.")
    return df
