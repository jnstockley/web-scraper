from src.email_sender import send_email, send_email_str
from src.scrappers.cars_com import check_new_listings, export, parse, get_old_data
from src.scrappers.text_search import get_data, check_for_string


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

def tesla_main():
    data = get_data("https://www.tesla.com/NACS")
    found = check_for_string(data, "Hyundai")

    if found:
        send_email_str("Hyundai found in Tesla website")


if __name__ == '__main__':
    tesla_main()
