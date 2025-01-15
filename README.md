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
1. Set these specific env variables
2. ```dotenv
    SCRAPPER=text # Scrapper to use
    URL=<URL> # URL to scrape
    TEXT=<TEXT> # Text to look for
   ```
3. Ensure all other required env variables are set

### Diff
1. Set these specific env variables
2. ```dotenv
    SCRAPPER=diff # Scrapper to use
    URL=<URL> # URL to scrape
    PERCENTAGE=<PERCENTAGE_DIFF> # Percentage difference to look for
   ```
3. Ensure all other required env variables are set

### Cars.com
1. Set these specific env variables
2. ```dotenv
    SCRAPPER=cars_com # Scrapper to use
    URL=https://www.cars.com/shopping/results/ # URL to scrape, must be on the results page, for a specific search
   ```
3. Ensure all other required env variables are set

### Required env variables
```dotenv
SLEEP_TIME_SEC= # Time to sleep between each scrape
SENDER_EMAIL= # Email to send from
FROM_EMAIL= # Name to send from i.e. '"Web Scrapper" <no-reply@jstockley.com>'
RECEIVER_EMAIL= # Email to send to
PASSWORD= # Password for the sender's email
SMTP_SERVER= # SMTP server to use
SMTP_PORT= # SMTP port to use
TLS= # True/False to use TLS
```

### Running multiple of the same scrapper
To run 2+ scrappers of the same type, i.e. 2 `diff` scrappers, make sure the host folder mapping is different
Ex:
```yaml
  diff-scrapper-1:
    image: jnstockley/web-scrapper:latest
    volumes:
      - ./diff-scrapper-1-data/:/web-scrapper/data/
    environment:
      - TZ=America/Chicago
      - SCRAPPER=diff
      - URL=https://google.com
      - PERCENTAGE=5
      - SLEEP_TIME_SEC=21600

  diff-scrapper-2:
    image: jnstockley/web-scrapper:latest
    volumes:
      - ./diff-scrapper-2-data/:/web-scrapper/data/
    environment:
      - TZ=America/Chicago
      - SCRAPPER=diff
      - URL=https://yahoo.com
      - PERCENTAGE=5
      - SLEEP_TIME_SEC=21600
```
