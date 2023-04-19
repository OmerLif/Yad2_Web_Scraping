import sys
from csv_handler import page_cars_details_to_csv
from scraper import scrape_car_listings
from SCRAPING_CONSTANTS import *
from utils import init_web_drivers, close_drivers
import argparse



# The main function to scrape car details for a given number of pages and a user query URL.
def main(num_pages_to_scrape, user_query_url, chrome_driver_path):
    # Iterate through each page number.
    for page_num in range(1, num_pages_to_scrape + 1):
        # Build the URL for the current page.
        url = user_query_url + PAGE_HTTP_PARAM + str(page_num)

        # Scrape car listings from the current page.
        cars = scrape_car_listings(url)

        # Initialize the pool of web drivers.
        web_driver_pool = init_web_drivers(chrome_driver_path)

        # Scrape car details and save them to a CSV file.
        page_cars_details_to_csv(cars, web_driver_pool)

        # Close all web drivers.
        close_drivers(web_driver_pool)


# Update the number of pages, the user query URL and the path for the chrome driver based on command-line arguments.
def update_user_url_num_pages():
    parser = argparse.ArgumentParser(description='Scrape car details from Yad2')
    parser.add_argument('-n', '--num_pages', type=int, default=DEFAULT_NUM_PAGES,
                        help='Number of pages to scrape (default: {})'.format(DEFAULT_NUM_PAGES))
    parser.add_argument('-u', '--user_query_url', type=str, default=DEFAULT_USER_SITE_QUERY_URL,
                        help='User query URL (default: {})'.format(DEFAULT_USER_SITE_QUERY_URL))
    parser.add_argument('-d', '--chrome_driver_path', type=str, default=DEFAULT_CHROME_DRIVE_PATH,
                        help='Path to ChromeDriver executable (default: {})'.format(DEFAULT_CHROME_DRIVE_PATH))

    args = parser.parse_args()

    return args.num_pages, args.user_query_url, args.chrome_driver_path


# The main entry point of the script.
if __name__ == '__main__':
    # Update the number of pages and the user query URL based on command-line arguments.
    num_pages, user_url_query, chrome_driver_path = update_user_url_num_pages()

    # Call the main function with the updated values.
    main(num_pages, user_url_query, chrome_driver_path)
