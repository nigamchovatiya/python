"""
here i Extract title, all links, and headings
in https://quotes.toscrape.com/ this link.
"""

# -----------------------------------------------

import requests
from bs4 import BeautifulSoup

# -----------------------------------------------

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get("https://quotes.toscrape.com/", headers=headers)


try:
    soup = BeautifulSoup(r.text, "lxml")

    # extract title
    print("\n----- title -----")
    title = soup.find("title")
    print("title:", title.text)


    # all links
    print("\n----- all links ----")
    links = soup.find_all("a")
     
    for link in links:
        print(link.text) 


    # headings
    print("\n----- headings -------")
    heading = soup.find_all("h1")
    for h in heading:
        print(h.text)        


except Exception as e:
    print("Error:", e)