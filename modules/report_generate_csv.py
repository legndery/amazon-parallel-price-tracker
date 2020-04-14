from modules.notification_manager import NotificationManager
from win10toast import ToastNotifier
from config.amazon_config import (
    DIRECTORY
)
from datetime import datetime
import os
from io import StringIO
import csv
header = ['asin', 'url', 'title', 'seller', 'merchant', 'price', 'date']
class GenerateReport:
    def __init__(self, data):
        self.data = data
        for product in self.data:
            product["date"] = self.get_now()
            print("Creating report...")
            filename = f'{DIRECTORY}/{product["asin"]}.csv'

            header_string = ','.join(header)
            last_product_price = StringIO(header_string + '\n' + self.read_last_line(filename))
            reader = csv.DictReader(last_product_price, delimiter=',')
            # compare the prices
            last_product=None
            for last_product in reader:
                pass
            if last_product is not None:
                NotificationManager.FirePriceNotification(last_product, product)
            self.write_csv_line(filename, product, last_product)
            # print("Done...")
    @staticmethod
    def get_now():
        now = datetime.now()
        return now.strftime("%d/%m/%Y %H:%M:%S")
    def write_csv_line(self, filename, product, last_product):
        with open(filename, 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=header)
            if last_product is None:
                writer.writeheader()
            writer.writerow(product)
    def read_last_line(self, filename):
      try:
        with open(filename, 'rb') as f:
          f.seek(-2, os.SEEK_END)
          while f.read(1) != b'\n':
            f.seek(-2, os.SEEK_CUR) 
          return f.readline().decode()
      except Exception as e:
        print(e)
        return ''

if __name__ == '__main__':
	GenerateReport([{"asin":"testcsv"}])