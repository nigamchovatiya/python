"""
Web scraper with logging and retry mechanism.


mean:
logging record what your program doing and save in file.

benefits:
easily show a error, debug faster 


logging level:
 
1. Debug : detailed info, interest only when diagnosing
          problem.
    use: step-by-step execution, understanding flow.      

2. Info : confirmation hat things are working as expected.
    use: app start, task complete, user login, file saved.

3. Warning : An indication that somthing unexpected happened.
            , or indicate some problem in the near future.
    use: missing optional data, retry attempt happen.        

4. Error : Due to more serious problem, the software not able
          to perform some function.
    use: file not found, api request fail, db error.      

5. Critical : A serious error, indicate that the program
            itself may be unable to continue running. 
    use: system crash, db down, cannot continue execution.         

            
retry mechanism:
website sometime fail, so don't give up immediately.                                  
             

"""

# ---------------------------------------------------------

import time
import requests
from bs4 import BeautifulSoup
import logging

# ---------------------------------------------------------

# logging setup
logging.basicConfig(
    filename = "scraper.log",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)


# ---------------------------------------------------------

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
    # page fetching error 3 try 
    for i in range(3):
        try:
            res = requests.get(url, headers=headers, timeout=5)
            res.raise_for_status()

            logging.info("Page fetched successfully.")
            return res
        
        except Exception as e:
            logging.warning(f"Retry {i+1} failed: {e}")
            time.sleep(2) # delay 2 sec

    logging.error("Failed to Fetch page after retries")   
    return None     


# ---------------------------------------------------------

def scrape() -> None:
    """
    Scrape book titles from the website.

    """

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    url = "http://books.toscrape.com/"
    response = fetch_page(url, headers)

    if response is None:
        return
    
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.select(".product_pod")

    if not books:
        logging.warning("No books found.")
        return
    
    logging.info(f"Found {len(books)} books")

    for book in books:
        try:
            title = book.h3.a['title']
            print(title)

        except Exception as e:
            logging.error(f"Error parsing book: {e}")


# ---------------------------------------------------------

def main() -> None:
    """main program to execute"""

    try:
        logging.info("scraper started")
        scrape()
        logging.info("scraper finished")

    except Exception as e:
        logging.critical(f"Scraper crashed: {e}")           


# ---------------------------------------------------------

if __name__ == "__main__":
    main()
         