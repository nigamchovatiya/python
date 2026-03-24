"""
here i extract home page of book.toscrap.com
"""

# -------------------------------------------------

import requests
from bs4 import BeautifulSoup

# -------------------------------------------------

headers = {
    "User-Agent": "Mozilla/5.0"
}


for i in range(1,3):
    r = requests.get(f"http://books.toscrape.com/catalogue/page-{i}.html", headers = headers)


    soup = BeautifulSoup(r.text, 'lxml')

    books = soup.select('article.product_pod') 

    for index, book in enumerate(books, start=1):

        # title
        title = book.select_one("h3 a").get('title')

        # price
        price = book.select_one(".price_color").text

        # rating store class
        rating_class = book.select_one("p.star-rating").get("class")
        # rating_class = ['star-rating', 'three]
        rating = rating_class[1] # three
        

        # print
        print(f"{index}. {title}")
        print(f"  Price: {price}")
        print(f"  Ratings: {rating}")
        print("----------------------\n")


