import csv
from typing import List, Dict
from selenium.webdriver.chrome.webdriver import WebDriver
from scraper import extract_car_details
from SCRAPING_CONSTANTS import YAD2_BASE_URL


def page_cars_details_to_csv(cars: List[Dict[str, str]], web_driver_pool: List[WebDriver]):
    # Open or create a CSV file in append mode with UTF-8 encoding.
    with open('resources/car_details.csv', mode='a', newline='', encoding='utf-8') as csvfile:
        for car in cars:
            # Construct the URL for the current car.
            car_url = YAD2_BASE_URL + "/item/" + car['item-id']

            # Extract the details for the current car.
            car_details: dict[str, str] = extract_car_details(car_url, web_driver_pool)

            # Write the details for the current car to the CSV file.
            write_car_to_csv(car_details, csvfile)


def write_car_to_csv(car_details: Dict[str, str], csvfile):
    # Get the keys of the car details dictionary as fieldnames for the CSV writer.
    fieldnames = list(car_details.keys())

    # Create a CSV writer object for the current CSV file.
    csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write the header row to the CSV file if it is empty.
    if not csvfile.tell():
        csv_writer.writeheader()

    # Write the current car details to the CSV file.
    csv_writer.writerow(car_details)
