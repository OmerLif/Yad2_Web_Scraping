import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from SCRAPING_CONSTANTS import DEFAULT_CHROME_DRIVE_PATH


def close_drivers(web_driver_pool):
    for web_driver in web_driver_pool:
        web_driver.quit()


def init_web_drivers(chrome_driver_path=None, pool_size=10):
    # Create a pool of web drivers
    options = Options()
    options.add_argument('--headless')

    # Set the path to the ChromeDriver executable
    if not chrome_driver_path:
        chrome_driver_path = os.environ.get('CHROME_DRIVER_PATH', DEFAULT_CHROME_DRIVE_PATH)
    web_driver_pool = [
        webdriver.Chrome(executable_path=chrome_driver_path, options=options)
        for _ in range(pool_size)]
    return web_driver_pool
