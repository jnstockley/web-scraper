<<<<<<< HEAD
import time
import os
from dotenv import load_dotenv
=======
import sys

from dotenv import load_dotenv

from util.healthcheck import healthcheck
from util.logging import logger


def main():
    logger.info("Hello from python-starter!")
>>>>>>> external/main

from src import logger
from src.scrapers import text, diff, cars_com

if __name__ == "__main__":
    load_dotenv()
<<<<<<< HEAD
    sleep_time_sec = int(os.environ["SLEEP_TIME_SEC"])
    logger.info("Starting WebScraper")
    scraper = os.environ.get("SCRAPER", "")
    url = os.environ.get("URL", "")
    logger.info(f"Scraper: {scraper}")
    while True:
        match scraper:
            case "text":
                scrape_text = os.environ.get("TEXT", "")
                logger.info("Using text scraper")
                logger.info(f"Checking URL: {url} for text: {scrape_text}")
                text.scrape(url, scrape_text)
            case "diff":
                percentage = float(os.environ.get("PERCENTAGE", 10))
                logger.info("Using diff scraper")
                logger.info(f"Checking URL: {url}")
                diff.scrape(url, percentage)
            case "cars_com":
                logger.info("Using cars_com scraper")
                cars_com.scrape(url)
            case _:
                logger.error("Invalid scraper specified")
                break
        logger.info(f"Sleeping for {sleep_time_sec} seconds")
        time.sleep(sleep_time_sec)
=======
    if len(sys.argv) > 1 and sys.argv[1] == "healthcheck":
        healthcheck()
    else:
        main()
>>>>>>> external/main
