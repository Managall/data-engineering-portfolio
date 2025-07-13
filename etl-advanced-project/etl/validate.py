# etl/validate.py
import pandas as pd
import re
from config import EXPECTED_COLUMNS
from etl.logger import logger

def validate_data(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("[Validate] Iniciando validación de datos...")

    # Verificar columnas esperadas
    if list(df.columns) != EXPECTED_COLUMNS:
        raise ValueError(f"[Validate][Error] Las columnas no coinciden: {df.columns.to_list()}")
    
    # Validar valores nulos
    if df.isnull().any().any():
        logger.warning("[Validate] Se encontraron valores nulos. Serán eliminados.")
        df = df.dropna()

    # Validar tipo de dato: edad debe de ser entero
    df.loc[:, 'edad'] = pd.to_numeric(df['edad'], errors='coerce')
    df = df.dropna(subset=['edad'])

    # Validar que el correo tenga formato correcto
    email_pattern = re.compile(r"[^@]+@[^@]+\.[^@]+")
    df = df[df['email'].apply(lambda x: bool(email_pattern.match(str(x))))]

    # Eliminar duplicados por ID o email
    df = df.drop_duplicates(subset=["id", "email"])

    logger.info(f"[Validate] Validación completada. Registros válidos: {len(df)}")
    return df