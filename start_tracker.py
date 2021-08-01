import asyncio
from concurrent.futures import ProcessPoolExecutor, wait
from modules.repository.csv_repository import CsvRepository
from modules.file_manager import FileManager
import time
from config.config import (
    CURRENCY,
    BASE_URL,
    REPORT_FIELDS,
)
from config.directory_config import DIR_INPUT, DIR_REPORTS
from modules.report_generator_abstract import ReportGenerator
from modules.amazon_api import AmazonAPI
from modules.notification_manager import NotificationManager

from modules.repository.sql_repository import SqlRepository, Base

executor = ProcessPoolExecutor(10)
loop = asyncio.get_event_loop()
csv_repository = CsvRepository(REPORT_FIELDS)

sql_repository = SqlRepository(Base)

def manual_cron(interval_time_in_sec, callback):
    starttime = time.time()
    while True:
        callback()
        time_to_sleep = interval_time_in_sec - ((time.time() - starttime) % interval_time_in_sec)
        print(f"Will sleep {time_to_sleep} seconds")
        time.sleep(time_to_sleep)

def worker(links):
    am = AmazonAPI(BASE_URL, CURRENCY, [links])
    data = am.run()
    ReportGenerator(sql_repository, data).generate(NotificationManager.FirePriceNotification)

def main():
    product_links = FileManager().fetch_product_links(DIR_INPUT)
    futures = [executor.submit(worker, link) for link in product_links]
    wait(futures)

if __name__ == '__main__':
    manual_cron(60*60, main)
