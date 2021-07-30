from selenium import webdriver

CURRENCY = '₹'
BASE_URL = "http://www.amazon.in/"

def get_chrome_web_driver(options):
    return webdriver.Chrome("./chromedriver.exe", chrome_options=options)

class ChromeOptionsBuilder:
    def __init__(self) -> None:
        self.options = webdriver.ChromeOptions()
    def ignore_certificate_error(self):
        self.options.add_argument('--ignore-certificate-errors')
        return self
    def browser_as_incognito(self):
        self.options.add_argument('--incognito')
        return self
    def headless(self):
        self.options.add_argument('--headless')
        return self
    def loglevel(self, level):
        self.options.add_argument(f'log-level={level}')
        return self
    def build(self):
        return self.options