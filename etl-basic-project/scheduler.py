# scheduler.py

import schedule
import time
import subprocess
from etl.logger import logger

def job():
    logger.info("⏰ Ejecutando pipeline ETL programado...")
    subprocess.run(["python","main.py"])

# Programar ejecución cada minuto (puedes cambiar hourly, daily, etc.)
schedule.every(1).minutes.do(job)

logger.info("🕒 Scheduler iniciado. Ejecutando ETL cada 1 minuto...")

while True:
    schedule.run_pending()
    time.sleep(1)