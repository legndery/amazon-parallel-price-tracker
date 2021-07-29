from modules.notification_manager import NotificationManager
from win10toast import ToastNotifier
from modules.resource_manager import ResourceManager
from datetime import datetime
from io import StringIO
import csv
class GenerateReport:
    def __init__(self, resource_manager:ResourceManager, REPORT_DIR, data):
        self.header = ['asin', 'url', 'title', 'seller', 'merchant', 'price', 'date']
        self.data = data
        self.resource_manager = resource_manager

        for product in self.data:
            product["date"] = self.get_now()
            print("Creating report...")
            filename = f'{REPORT_DIR}/{product["asin"]}.csv'
            last_product = self.get_last_product_from_csv(filename)
            if last_product is not None:
                NotificationManager.FirePriceNotification(last_product, product)
            resource_manager.write_csv_line(filename, product, self.header, last_product is None)
            print("Done...")
    @staticmethod
    def get_now():
        now = datetime.now()
        return now.strftime("%d/%m/%Y %H:%M:%S")
    def get_last_product_from_csv(self, filename):
        header_string = ','.join(self.header)
        last_product_price = StringIO(header_string + '\n' + self.resource_manager.get_csv_last_line(filename))
        reader = csv.DictReader(last_product_price, delimiter=',')
        last_product=None
        for last_product in reader:
            pass
        return last_product
if __name__ == '__main__':
	GenerateReport([{"asin":"testcsv"}])