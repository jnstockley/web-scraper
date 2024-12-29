import time
import os
from dotenv import load_dotenv

from src import logger
from src.scrappers import text, diff, cars_com


'''def main():
    old_data = get_old_data()

    url = ("https://www.cars.com/shopping/results/?dealer_id=&electric_total_range_miles_min=330&include_shippable"
           "=true&keyword=&list_price_max=&list_price_min=&makes[]=hyundai&maximum_distance=all&mileage_max=&models["
           "]=hyundai-ioniq_6&monthly_payment=&page_size=100&sort=listed_at_desc&stock_type=new&trims["
           "]=hyundai-ioniq_6-se&year_max=&year_min=&zip=52241")
    data = get_data(url)
    cars = parse(data)

    new_data = check_new_listings(old_data, cars)

    if new_data.shape[0] > 0:
        send_email(new_data)
        print("Sending email...")

    export(cars)'''


if __name__ == '__main__':
    load_dotenv()
    sleep_time_sec = int(os.environ['SLEEP_TIME_SEC'])
    logger.info(f"Starting WebScrapper")
    scrapper = os.environ.get('SCRAPPER', '')
    url = os.environ.get('URL', '')
    logger.info(f"Scrapper: {scrapper}")
    while True:
        match scrapper:
            case "text":
                scrape_text = os.environ.get('TEXT', '')
                logger.info("Using text scrapper")
                logger.info(f"Checking URL: {url} for text: {scrape_text}")
                text.scrape(url, scrape_text)
            case "diff":
                percentage = float(os.environ.get('PERCENTAGE', 10))
                logger.info("Using diff scrapper")
                logger.info(f"Checking URL: {url}")
                diff.scrape(url, percentage)
            case "cars_com":
                logger.info("Using cars_com scrapper")
                cars_com.scrape(url)
            case _:
                logger.error("Invalid scrapper specified")
                break
        logger.info(f"Sleeping for {sleep_time_sec} seconds")
        time.sleep(sleep_time_sec)
