import asyncio
from concurrent.futures import ProcessPoolExecutor, wait
from modules.resource_manager import ResourceManager
import time
from config.config import (
    CURRENCY,
    BASE_URL,
)
from config.directory_config import DIR_INPUT, DIR_REPORTS
from modules.report_generate_csv import GenerateReport
from modules.amazon_api import AmazonAPI

executor = ProcessPoolExecutor(10)
loop = asyncio.get_event_loop()

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
    GenerateReport(ResourceManager(),DIR_REPORTS, data)

def main():
    resource_manager = ResourceManager()
    product_links = resource_manager.fetch_product_links(DIR_INPUT)
    futures = [executor.submit(worker, link) for link in product_links]
    wait(futures)

if __name__ == '__main__':
    manual_cron(30*60, main)
