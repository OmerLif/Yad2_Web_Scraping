# Yad2_Web_Scraping
A Python-based web scraper for collecting and storing car listings data from the Yad2 website in a CSV file. 
Yad2 Car Scraper is a Python script that scrapes car listing data from the Yad2 website. The scraped data includes various car details, such as model, year, price, and more. This script can be customized by providing user query URLs and the number of pages to scrape. The output is saved as a CSV file.

## Features
Scrape car listings from Yad2 based on user query URL
Customize the number of pages to scrape
Save the scraped data to a CSV file
Easy to use and modify
## Requirements
Python 3.x
beautifulsoup4
requests
selenium
ChromeDriver
## Installation
Clone this repository or download the source code.

Install the required packages:

sh
Copy code
pip install -r requirements.txt
Download the ChromeDriver executable that matches your installed version of Google Chrome and save it to a location on your computer.
## Usage
Run the script using the following command:

sh
Copy code
python main.py --num_pages <num_pages> --user_query_url <user_query_url> --chrome_driver_path <chrome_driver_path>
Replace <num_pages>, <user_query_url>, and <chrome_driver_path> with the appropriate values.

<num_pages>: The number of pages to scrape (default: 1)
<user_query_url>: The user query URL to use for scraping (default: Example URL)
<chrome_driver_path>: The path to the ChromeDriver executable
For example:

sh
Copy code
python main.py --n 5 -u "https://www.yad2.co.il/vehicles/private-cars" -d "/path/to/chromedriver"
The scraped data will be saved in a CSV file in the same directory as the script.

## Customization
You can customize the script by modifying the constants in the SCRAPING_CONSTANTS.py file, such as the user agent, default URL, and default number of pages.
