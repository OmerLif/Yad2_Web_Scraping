import os

USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
]
DEFAULT_USER_SITE_QUERY_URL = "https://www.yad2.co.il/vehicles/cars?carFamilyType=1&manufacturer=48,19,21,27&price=25000-50000"
PAGE_HTTP_PARAM = "&page="
YAD2_BASE_URL = "https://www.yad2.co.il"
DEFAULT_NUM_PAGES = 5
DEFAULT_CHROME_DRIVE_PATH = os.path.join(os.getcwd(), 'chromedriver')