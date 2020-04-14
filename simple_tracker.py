import time
from config.amazon_config import (
    CURRENCY,
    BASE_URL,
)
from modules.report_generate_csv import GenerateReport
from modules.amazon_api import AmazonAPI

if __name__ == '__main__':
    starttime = time.time()
    while True:
        am = AmazonAPI(BASE_URL, CURRENCY)
        data = am.run()
        GenerateReport(data)
        interval_time = 30.0*60.0
        time_to_sleep = interval_time - ((time.time() - starttime) % interval_time)
        print(f"Will sleep {time_to_sleep} seconds")
        time.sleep(time_to_sleep)
