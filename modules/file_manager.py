import glob

class FileManager:
    def __init__(self) -> None:
        pass
    def fetch_product_links(self, directory):
        txt_files = glob.glob(f'./{directory}/*.txt')
        link_list = []
        for file in txt_files:
            with open(file,'r') as f:
                link_list.extend(f.read().splitlines())
        return link_list

if __name__ == '__main__':
	FileManager().fetch_product_links()
