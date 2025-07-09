# main.py

from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data

def run_pipeline():
    print("🚀 Iniciando pipeline ETL...")
    
    filepath = "data/source_data.csv"
    db_path = "data/output.db"

    # 1. Extract
    df = extract_data(filepath)
    if df is None:
        return

    # 2. Transform
    df_transformed = transform_data(df)

    # 3. Load
    load_data(df_transformed, db_path)

    print("✅ Pipeline completado.")

if __name__ == "__main__":
    run_pipeline()
