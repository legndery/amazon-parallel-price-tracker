from modules.resource_manager import ResourceManager
import time
from config.config import (
    CURRENCY,
    BASE_URL,
)
from config.directory_config import DIR_INPUT, DIR_REPORTS
from modules.report_generate_csv import GenerateReport
from modules.amazon_api import AmazonAPI

if __name__ == '__main__':
    starttime = time.time()
    while True:
        resource_manager = ResourceManager()
        product_links = resource_manager.fetch_product_links(DIR_INPUT)
        am = AmazonAPI(BASE_URL, CURRENCY, product_links)
        data = am.run()
        GenerateReport(resource_manager,DIR_REPORTS, data)
        interval_time = 30.0*60.0
        time_to_sleep = interval_time - ((time.time() - starttime) % interval_time)
        print(f"Will sleep {time_to_sleep} seconds")
        time.sleep(time_to_sleep)
