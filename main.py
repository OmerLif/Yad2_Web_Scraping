from csv_handler import page_cars_details_to_csv
from scraper import scrape_car_listings
from SCRAPING_CONSTANTS import *
from utils.chrome_drive_utils import *
import argparse


# The main function to scrape car details for a given number of pages and a user query URL.
def main(num_pages_to_scrape, user_query_url, chrome_driver_path):
    print("Starting Yad2 car details scraper...")
    # Iterate through each page number.
    for page_num in range(1, num_pages_to_scrape + 1):
        # Build the URL for the current page.
        url = user_query_url + PAGE_HTTP_PARAM + str(page_num)

        print(f"Scraping page {page_num} of {num_pages_to_scrape}...")
        # Scrape car listings from the current page.
        cars = scrape_car_listings(url)

        print(f"Found {len(cars)} car listings on page {page_num}.")
        # Initialize the pool of web drivers.
        print("Init web drivers for scraping")
        web_driver_pool = init_web_drivers(chrome_driver_path)

        # Scrape car details and save them to a CSV file.
        page_cars_details_to_csv(cars, web_driver_pool)
        print(f"Saved details for {len(cars)} cars on page {page_num} to CSV file.")

        # Close all web drivers.
        close_drivers(web_driver_pool)
        print("Finished scraping Yad2 car details.")


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
    print(f"Number of pages to scrape: {args.num_pages}")
    print(f"User query URL: {args.user_query_url}")
    print(f"ChromeDriver path: {args.chrome_driver_path}")
    return args.num_pages, args.user_query_url, args.chrome_driver_path


# The main entry point of the script.
if __name__ == '__main__':
    # Update the number of pages and the user query URL based on command-line arguments.
    num_pages, user_url_query, chrome_driver_path = update_user_url_num_pages()

    # Call the main function with the updated values.
    main(num_pages, user_url_query, chrome_driver_path)
