"""
this program safe scraper data safely scrape in 
website with delay and print result. if error that 
also print in log file so that idea about what error.

logging concept + random delay 
If any error occurs, it is saved in the log file,  
and randome delay between request get 

"""


# -----------------------------------------------------

import requests
from bs4 import BeautifulSoup
import time
import random
import logging


# -----------------------------------------------------

# logging setup 
logging.basicConfig(
    filename = "safe-scraper.log",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)


# ------------------------------------------------------

# add random time delay between request
def random_delay() -> None:
    delay = random.uniform(1, 3)
    logging.info(f"Sleeping for {delay:.2f} seconds")
    time.sleep(delay)


# ------------------------------------------------------


def fetch_page(url: str, headers: dict) -> object:
    """
    fetch webpage with retry logic

    Args:
      url(str) : Target url.
      headers(dict) : Request headers.

    Return:
      object : Response object or None if failed.  

    """

    # retry mechanism 
    # page fetching error 3 time try 
    for i in range(3):
        try:

            random_delay() # delay before request

            res = requests.get(url, headers=headers, timeout=5)
            res.raise_for_status()

            logging.info("Page fetched successfully.")
            return res
        
        except Exception as e:
            logging.warning(f"Retry {i+1} failed: {e}")
            time.sleep(2) # delay 2 sec

    logging.error("Failed to Fetch page after retries")   
    return None 


# ------------------------------------------------------


def scrape() -> None:
    """
    Scrape book titles from the website.

    """

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    urls = [
        "http://books.toscrape.com/",
        "http://books.toscrape.com/catalogue/page-2.html",
        "http://books.toscrape.com/catalogue/page-3.html"
    ]


    for url in urls:
        logging.info("Scraping url start")

        response = fetch_page(url, headers)

        if response is None:
            continue
        
        soup = BeautifulSoup(response.text, "html.parser")
        books = soup.select(".product_pod")

        if not books:
            logging.warning("No books found.")
            continue
        
        logging.info(f"Found {len(books)} books")

        for book in books:
            try:
                title = book.h3.a['title']
                print(title)

            except Exception as e:
                logging.error(f"Error parsing book: {e}")

        logging.info("Scraping url finished")        


# ------------------------------------------------------


def main() -> None:
    """main program to execute"""

    try:
        logging.info("scraper started")
        scrape()
        logging.info("scraper finished")

    except Exception as e:
        logging.critical(f"Scrapper crashed: {e}")  
        
    
# ------------------------------------------------------

if __name__ == "__main__":
    main()