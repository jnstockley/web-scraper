import time
import os
import logging

from src.email_sender import send_email
from src.scrappers.cars_com import get_old_data, get_data, parse, check_new_listings, export


def main():
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

    export(cars)


if __name__ == '__main__':
    print("Starting...")
    try:
        sleep_time_secs = int(os.environ['SLEEP_TIME_SEC'])
    except KeyError:
        print("Default sleep_time_sec to 21600")
        sleep_time_secs = 21600

    while True:
        main()
        print(f"Sleeping for {sleep_time_secs} seconds...")
        time.sleep(sleep_time_secs)
