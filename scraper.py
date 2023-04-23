import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from SCRAPING_CONSTANTS import USER_AGENTS
import time
from typing import List, Dict
from utils.chrome_drive_utils import *
import random


def scrape_car_listings(page_url: str):
    """
    Scrape car listings from a given page URL.

    :param page_url: The URL of the page to scrape car listings from.
    :return: A list of BeautifulSoup car listing objects.
    """
    headers = {'User-Agent': random.choice(USER_AGENTS)}
    response = requests.get(page_url, headers=headers)
    time.sleep(1)
    soup = BeautifulSoup(response.content, 'html.parser')
    time.sleep(1)
    return soup.find_all('div', class_='feed_item')


def extract_car_details(url: str, web_driver_pool: List[webdriver.Chrome]) -> Dict[str, str]:
    """
    Extract car details from a car listing URL using a pool of web drivers.

    :param url: The URL of the car listing.
    :param web_driver_pool: A list of available web drivers.
    :return: A dictionary containing the extracted car details.
    """
    web_driver = web_driver_pool.pop(0)
    time.sleep(1)
    web_driver.get(url)
    time.sleep(1)

    details = initialize_car_details()

    translations = create_translations()

    extract_main_content_data(details, translations, web_driver)
    extract_details_wrapper_data(details, translations, web_driver)

    web_driver_pool.append(web_driver)
    details['link'] = url
    return details


def initialize_car_details() -> Dict[str, str]:
    """
    Initialize an empty dictionary with all possible car detail keys and empty string values.

    :return: A dictionary with car detail keys and empty string values.
    """
    return {
        "Car Model": "",
        "Car Subtitle": "",
        "Price": "",
        "Year of first drive": "",
        "Year": "",
        "Kilometre": "",
        "Hand": "",
        "Sale Area": "",
        "Engine Size": "",
        "Gas type": "",
        "Gir": "",
        "Color": "",
        "Test until": "",
        "Curr ownership": "",
        "Pre ownership": "",
        "Suited for handicapped": "",
        "link": ""
    }


def create_translations() -> Dict[str, str]:
    """
    Create a dictionary of translations for car detail keys.

    :return: A dictionary with Hebrew car detail keys and their English translations.
    """
    return {
        "קילומטראז'": "Kilometre",
        "סוג מנוע": "Gas type",
        "תיבת הילוכים": "Gir",
        "צבע": "Color",
        "תאריך עליה לכביש": "Year of first drive",
        "טסט עד": "Test until",
        "בעלות נוכחית": "Curr ownership",
        "בעלות קודמת": "Pre ownership",
        "מותאם לנכים": "Suited for handicapped",
        "שנה": "Year",
        "יד": "Hand",
        "סמ״ק": "Engine Size",
        "אזור מכירה": "Sale Area",
        "Price": "Price"
    }


def main_content_data_extraction(details, translations, web_driver):
    main_content = web_driver.find_element(By.CLASS_NAME, "main_content")
    details["Car Model"] = main_content.find_element(By.CLASS_NAME, "main_title").text.strip()
    details["Car Subtitle"] = main_content.find_element(By.CLASS_NAME, "second_title").text.strip()
    sale_area = main_content.find_element(By.CLASS_NAME, "address").find_elements(By.TAG_NAME, "span")[-1]
    details["Sale Area"] = sale_area.text.strip()
    price = main_content.find_element(By.CLASS_NAME, "price").text.strip()
    details["Price"] = price

    for cell in main_content.find_elements(By.CLASS_NAME, "cell"):
        label = cell.find_element(By.TAG_NAME, 'dt').text.strip()
        translated_key = translations.get(label, label)  # Get the English translation for the key
        details[translated_key] = cell.find_element(By.TAG_NAME, 'dd').text.strip()


def details_wrapper_data_extraction(details, translations, web_driver):
    details_wrapper = web_driver.find_element(By.CLASS_NAME, 'details_wrapper')
    for detail in details_wrapper.find_elements(By.TAG_NAME, 'dl'):
        key = detail.find_element(By.TAG_NAME, 'dt').text.strip()
        value = detail.find_element(By.TAG_NAME, 'dd').text.strip()
        translated_key = translations.get(key, key)  # Get the English translation for the key
        details[translated_key] = value


def extract_main_content_data(details: Dict[str, str], translations: Dict[str, str], web_driver: webdriver.Chrome):
    """
    Extract car details from the main content section of a car listing.

    :param details: A dictionary to store the extracted car details.
    :param translations: A dictionary with Hebrew car detail keys and their English translations.
    :param web_driver: A web driver instance used to extract car details.
    """
    main_content = web_driver.find_element(By.CLASS_NAME, "main_content")
    details["Car Model"] = main_content.find_element(By.CLASS_NAME, "main_title").text.strip()
    details["Car Subtitle"] = main_content.find_element(By.CLASS_NAME, "second_title").text.strip()
    sale_area = main_content.find_element(By.CLASS_NAME, "address").find_elements(By.TAG_NAME, "span")[-1]
    details["Sale Area"] = sale_area.text.strip()
    price = main_content.find_element(By.CLASS_NAME, "price").text.strip()
    details["Price"] = price

    for cell in main_content.find_elements(By.CLASS_NAME, "cell"):
        label = cell.find_element(By.TAG_NAME, 'dt').text.strip()
        translated_key = translations.get(label, label)  # Get the English translation for the key
        details[translated_key] = cell.find_element(By.TAG_NAME, 'dd').text.strip()


def extract_details_wrapper_data(details: Dict[str, str], translations: Dict[str, str], web_driver: webdriver.Chrome):
    """
    Extract car details from the details wrapper section of a car listing.

    :param details: A dictionary to store the extracted car details.
    :param translations: A dictionary with Hebrew car detail keys and their English translations.
    :param web_driver: A web driver instance used to extract car details.
    """
    details_wrapper = web_driver.find_element(By.CLASS_NAME, 'details_wrapper')
    for detail in details_wrapper.find_elements(By.TAG_NAME, 'dl'):
        key = detail.find_element(By.TAG_NAME, 'dt').text.strip()
        value = detail.find_element(By.TAG_NAME, 'dd').text.strip()
        translated_key = translations.get(key, key)  # Get the English translation for the key
        details[translated_key] = value
