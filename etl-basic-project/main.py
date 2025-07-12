# main.py

from config import SOURCE_CSV_PATH, SQLITE_DB_PATH, SQLITE_DB_NAME
from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data
from etl.logger import logger

def run_pipeline():
    logger.info("🚀 Iniciando pipeline ETL...")
    
    # 1. Extract
    df = extract_data(SOURCE_CSV_PATH)
    if df is None:
        return

    # 2. Transform
    df_transformed = transform_data(df)

    # 3. Load
    load_data(df_transformed, SQLITE_DB_PATH, SQLITE_DB_NAME)

    logger.info("✅ Pipeline completado.")

if __name__ == "__main__":
    run_pipeline()
