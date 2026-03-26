"""
in this add random delay between a two request.

why add delay:
  avoid getting block, reduce server load,
  act like a human 

"""

# -------------------------------------------------

import requests
import random 
from bs4 import BeautifulSoup
import logging
import time

# ------------------------------------------------

# logging setup
logging.basicConfig(
    filename = 'randomdelay.log',
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)


# -------------------------------------------------

def fetch_page(url: list) -> None:
    """
    fetch data of page and print.

    Args:
      url(list) : Take url list
    
    """

    headers = {
        "User-Agent": "Mozilla/5.0"
    }


    try:
        logging.info("fetching url.")

        response = requests.get(url, headers = headers,
                            timeout=5)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        books = soup.select(".product_pod")

        logging.info(f"Found {len(books)} books")

    except Exception as e:
        logging.error(f"Request failed: {e}")    


# -------------------------------------------------

def main() -> None:
    """main program to execute"""

    urls = [
        "http://books.toscrape.com/",
        "http://books.toscrape.com/catalogue/page-2.html"
    ]

    try:
        logging.info("scraper started")

        for url in urls:
            fetch_page(url)

            # Add random delay (1 - 3 seconds)
            delay = random.uniform(1, 3)
 
            logging.info(f"Sleeping for {delay:.2f} seconds")
            time.sleep(delay) # delay add after one url fetch

        logging.info("scraper finished")

    except Exception as e:
        logging.critical(f"Scraper crashed: {e}")    


# ------------------------------------------------

if __name__ == "__main__":
    main()