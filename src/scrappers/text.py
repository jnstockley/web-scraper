from src import logger
from src.email_sender import send_email_str
from src.scrappers import generic


def scrape(url: str, text: str):
    session = generic.create_tls_session()

    data = generic.make_tls_request("GET", url, session)

    if text in data:
        logger.info(f"Found {text} in {url}")

        send_email_str(f"Found {text} in {url}")

