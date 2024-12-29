'''import os
from dataclasses import dataclass
import json
from datetime import datetime

import requests
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame


@dataclass
class Car:
    listing_id: str
    listing_url: str
    dealer_url: str
    listing_name: str
    price: str
    location: str

    def as_dict(self):
        return {'listing_id': self.listing_id, 'listing_url': self.listing_url, 'dealer_url': self.dealer_url,
                'listing_name': self.listing_name, 'price': self.price, 'location': self.location}


def get_old_data() -> DataFrame:
    data_directory = './data/'
    if os.path.exists(data_directory) and os.path.isfile(f"{data_directory}/previous_cars.csv"):
        return pd.read_csv(f"{data_directory}/previous_cars.csv")
    return pd.DataFrame()


def get_data(url: str) -> str:
    res = requests.get(url)
    return res.content.decode(encoding='utf-8')


def parse(data: str) -> list[Car]:
    cars_dict = []

    soup = BeautifulSoup(data, 'html.parser')
    car_sections = soup.find_all("div", {"class": "sds-page-section__content"})

    total_cars = 0

    for car_section in car_sections:
        cars = car_section.find_all("div", {'class': 'vehicle-card-main'})
        total_cars += len(cars)
        for car in cars:
            car_json = json.loads(
                car.find("spark-button", {'class': 'lead-form-modal-button--desktop srp'})['data-override-payload'])
            location = car.find('div', {'class': 'miles-from'}).text.strip()
            try:
                dealer_link = car.find("a", {'class': 'sds-link--ext'})['href']
            except TypeError:
                dealer_link = ''

            title = car.find('a', {'class': 'vehicle-card-link'}).text.strip()
            price = car_json['msrp'] if car_json['price'] is None else car_json['price']

            car_dict = Car(listing_id=car_json['listing_id'],
                           listing_url=f"https://www.cars.com/vehicledetail/{car_json['listing_id']}",
                           dealer_url=dealer_link, listing_name=title, price=price, location=location)

            cars_dict.append(car_dict)

    return cars_dict


def check_new_listings(previous_cars: DataFrame, new_cars: list[Car]) -> DataFrame:
    new_cars_df = pd.DataFrame([x.as_dict() for x in new_cars])
    if len(previous_cars.columns) > 0:
        return new_cars_df[~new_cars_df['listing_id'].isin(previous_cars['listing_id'])]
    return new_cars_df


def export(cars: list[Car]) -> None:
    data_directory = '/web-scrapper/data/'
    archive_directory = '/web-scrapper/data/archive/'
    if not os.path.exists(data_directory):
        os.makedirs(data_directory)

    if not os.path.exists(archive_directory):
        os.makedirs(archive_directory)

    df = pd.DataFrame([x.as_dict() for x in cars])

    df.to_csv(f"{data_directory}/previous_cars.csv", index=False)
    df.to_csv(f"{archive_directory}/cars_{datetime.now()}.csv", index=False)'''
