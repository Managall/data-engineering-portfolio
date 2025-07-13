# main.py

from etl.extract import extract_data
from etl.validate import validate_data
from etl.transform import transform_data
from etl.load import load_data
from etl.logger import logger



logger.info("🚀 Iniciando pipeline ETL...")

# ETL Step 1: Extraer
df = extract_data()

# ETL Step 2: Validar
df_validado = validate_data(df)

# ETL Step 3: Transformar
df_transformado = transform_data(df_validado)

# ETL Step 4: Cargar
load_data(df_transformado)

logger.info("✅ Pipeline ETL finalizado con éxito.")

