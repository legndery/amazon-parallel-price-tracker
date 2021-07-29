INPUT_DIRECTORY="./inputs"
import glob
import os
import csv

class ResourceManager:
    def __init__(self) -> None:
        pass
    def fetch_product_links(self):
        txt_files = glob.glob('./inputs/*.txt')
        link_list = []
        for file in txt_files:
            with open(file,'r') as f:
                link_list.extend(f.read().splitlines())
        return link_list
    
    def get_csv_last_line(self, filename):
      try:
        with open(filename, 'rb') as f:
          f.seek(-2, os.SEEK_END)
          while f.read(1) != b'\n':
            f.seek(-2, os.SEEK_CUR) 
          return f.readline().decode()
      except Exception as e:
        print(e)
        return ''
    
    def write_csv_line(self, filename, product, last_product, header):
        with open(filename, 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=header)
            if last_product is None:
                writer.writeheader()
            writer.writerow(product)
if __name__ == '__main__':
	ResourceManager().fetch_product_links()
