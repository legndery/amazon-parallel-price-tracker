from datetime import datetime
from modules.repository.repository import Repository

import matplotlib.pyplot as plt

class ReportGenerator:
    def __init__(self, repository:Repository, data):
        self.data = data
        self.repository = repository
    @staticmethod
    def get_now():
        now = datetime.now()
        return now.strftime("%d/%m/%Y %H:%M:%S")
    def generate(self, cb):
        for product in self.data:
            product["date"] = self.get_now()
            print("Creating report...")
            last_product = self.repository.get_last_product(product["asin"])
            cb(last_product, product)
            self.repository.append_product(product)
            plt.title(product['title'])
            plt.ylabel('Price in Rs')
            plt.plot(self.repository.get_price(product["asin"]))
            plt.grid(True)
            plt.savefig(f"{product['asin']}.png")
            print("Done...")

if __name__ == '__main__':
    from repository.sql_repository import SqlRepository, Base
    ReportGenerator(SqlRepository(Base), [{"asin":"B07YFF3JCN", "title":"asdf"}]).generate(lambda a,b: print())