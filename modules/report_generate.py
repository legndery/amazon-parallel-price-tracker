from win10toast import ToastNotifier
from amazon_config import (
    DIRECTORY
)
import json
from datetime import datetime
product_links = [
    "https://www.amazon.in/dp/B073GF2CL6/",
    "https://www.amazon.in/dp/B07YFF3JCN/"
]

class GenerateReport:
    def __init__(self, filters, base_link, currency, data):
        self.data = data
        self.filters = filters
        self.base_link = base_link
        self.currency = currency
        for product in self.data:
            product["date"] = self.get_now()
            print("Creating report...")
            product_history = []
            with open(f'{DIRECTORY}/{product["asin"]}.json', 'r+') as f:
                product_history = json.load(f)
                # compare the prices
                if len(product_history) > 0:
                    old_price = product_history[-1]["price"]
                    new_price = product["price"]
                    if old_price > new_price:
                        ToastNotifier().show_toast("Amazon Price Alert", f"{product['title']}\nPRICE DECREASED", duration=5)
                        print("PRICE DECREASED!!!!!!!")
                product_history.append(product)
                f.seek(0)
                json.dump(product_history, f,indent=4)
                f.truncate()
            print("Done...")

    @staticmethod
    def get_now():
        now = datetime.now()
        return now.strftime("%d/%m/%Y %H:%M:%S")

    def get_best_item(self):
        try:
            return sorted(self.data, key=lambda k: k['price'])[0]
        except Exception as e:
            print(e)
            print("Problem with sorting items")
            return None