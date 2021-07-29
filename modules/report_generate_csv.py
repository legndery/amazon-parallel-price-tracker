from modules.notification_manager import NotificationManager
from win10toast import ToastNotifier
from modules.resource_manager import ResourceManager
from datetime import datetime
import os
from io import StringIO
import csv
header = ['asin', 'url', 'title', 'seller', 'merchant', 'price', 'date']
class GenerateReport:
    def __init__(self, resource_manager:ResourceManager, REPORT_DIR, data):
        self.data = data
        for product in self.data:
            product["date"] = self.get_now()
            print("Creating report...")
            filename = f'{REPORT_DIR}/{product["asin"]}.csv'

            header_string = ','.join(header)
            last_product_price = StringIO(header_string + '\n' + resource_manager.get_csv_last_line(filename))
            reader = csv.DictReader(last_product_price, delimiter=',')
            # compare the prices
            last_product=None
            for last_product in reader:
                pass
            if last_product is not None:
                NotificationManager.FirePriceNotification(last_product, product)
            resource_manager.write_csv_line(filename, product, last_product, header)
            print("Done...")
    @staticmethod
    def get_now():
        now = datetime.now()
        return now.strftime("%d/%m/%Y %H:%M:%S")

if __name__ == '__main__':
	GenerateReport([{"asin":"testcsv"}])