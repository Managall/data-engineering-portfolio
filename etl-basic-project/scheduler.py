# scheduler.py

import schedule
import time
import logging
import subprocess
from datetime import datetime

# Configurar logging
logging.basicConfig(filename='etl.log', level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

def job():
    logging.info("⏰ Ejecutando pipeline ETL programado...")
    subprocess.run(["/home/mnajarro/managall/data-engineering-portfolio/etl-basic-project/venv/bin/python3", "/home/mnajarro/managall/data-engineering-portfolio/etl-basic-project/main.py"])

# Programar ejecución cada minuto (puedes cambiar hourly, daily, etc.)
schedule.every(1).minutes.do(job)

logging.info("🕒 Scheduler iniciado. Ejecutando ETL cada 1 minuto...")

while True:
    schedule.run_pending()
    time.sleep(1)