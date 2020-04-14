INPUT_DIRECTORY="./inputs"
import glob

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

if __name__ == '__main__':
	ResourceManager().fetch_product_links()
