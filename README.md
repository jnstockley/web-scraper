# WebScrapper
* This program can scrap data from websites using different scrappers, and send an email when 
matches/ changes deadening on the scrapper used
* There are 2 types of scrappers:
    - Generic: Can scrap any website, but might not be as exact
    - Specific: Can scrap only specific websites, but will be more exact

## Generic Scrappers
 - Text
 - Diff

## Specific Scrappers
 - Cars.com

## How to use
### Text
1. Set these specifics env variables
2. ```dotenv
    SCRAPPER=text # Scrapper to use
    URL=<URL> # URL to scrape
    TEXT=<TEXT> # Text to look for
   ```
3. Ensure all other required env variables are set

### Diff
1. Set these specifics env variables
2. ```dotenv
    SCRAPPER=diff # Scrapper to use
    URL=<URL> # URL to scrape
    PERCENTAGE=<PERCENTAGE_DIFF> # Percentage difference to look for
   ```
3. Ensure all other required env variables are set

### Cars.com
1. Set these specifics env variables
2. ```dotenv
    SCRAPPER=cars_com # Scrapper to use
    URL=https://www.cars.com/shopping/results/ # URL to scrape, must be on the results page, for a specifc search
   ```
3. Ensure all other required env variables are set

### Required env variables
```dotenv
SLEEP_TIME_SEC= # Time to sleep between each scrape
SENDER_EMAIL= # Email to send from
FROM_EMAIL= # Name to send from i.e. '"Web Scrapper" <no-reply@jstockley.com>'
RECEIVER_EMAIL= # Email to send to
PASSWORD= # Password for the sender email
SMTP_SERVER= # SMTP server to use
SMTP_PORT= # SMTP port to use
TLS= # True/False to use TLS
```