from datetime import datetime
from modules.repository.repository import Repository
from config.directory_config import DIR_REPORTS_GRAPH
import matplotlib.pyplot as plt
import numpy as np
from textwrap import wrap

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
            self.plot_graph(product)
            print("Done...")
    def plot_graph(self, product):
        fig, ax = plt.subplots()
        yplots = self.repository.get_price(product["asin"])
        xplots = range(len(yplots))
        ax.plot(xplots, yplots)
        ax.set_title('\n'.join(wrap(product['title'])))
        ax.set_ylabel('Price in Rs')
        self.label_point(xplots, yplots, ax)
        ax.grid(True)
        width = len(xplots)/5
        if width > 4:
            ymin, ymax = ax.get_ylim()
            ax.set_yticks(np.arange(np.floor(ymin), np.floor(ymax), 25))
        else:
            width = 4
        fig.set_figwidth(width)
        plt.savefig(f"{DIR_REPORTS_GRAPH}/{product['asin']}.png")
        plt.close('all')
    def label_point(self, xplots, yplots, ax):
        prev_val = None
        for x,y in zip(xplots, yplots):
            if prev_val != y:
                ax.text(x-0.5, y+1, y)  
                prev_val = y