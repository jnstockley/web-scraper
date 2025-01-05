import time
import os
from dotenv import load_dotenv

from src import logger
from src.scrappers import text, diff, cars_com

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
