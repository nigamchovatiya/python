"""
here i scrap 50 books and sort by
price low to high.

"""

# ------------------------------------------------

import requests
from bs4 import BeautifulSoup
import csv
import json
import time

# ------------------------------------------------


headers = {
    "User-Agent": "Mozilla/5.0"
}

base_url = "http://books.toscrape.com/catalogue/"


data = []

# star rating num assign
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4, 
    "Five": 5
}


for page in range(1, 4): # 1-3 page

    url = f"{base_url}page-{page}.html"
    print(f"\n---------{page} page --------")


    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()

    except requests.exceptions.RequestException as e:
        print("Request Error:", e)
        continue

    soup = BeautifulSoup(r.text, 'lxml')
    books = soup.select("article.product_pod")

    for book in books:

        # title
        try:
            title = book.select_one("h3 a").get("title")
        except:
            title = "No title"

        # price
        try:
            price_text = book.select_one(".price_color").text
            price_text = price_text.replace("Â", "").replace("£", "")
            price = float(price_text)
        except:
            price = 0.0

        # rating store class
        try:
            rating_class = book.select_one("p.star-rating").get("class")
            # rating_class = ['star-rating', 'three']
            rating_str = rating_class[1] # three
            rating = rating_map.get(rating_str, 0)
        except:
            rating = 0

        # store data
        data.append({
            "Title": title,
            "Price": price,
            "Rating": rating
        })

        # book 50 > store, break        
        if len(data) >= 50:
            break    


    # page break         
    if len(data) >= 50:
        break    

    time.sleep(2) # delay 2 sec before next request


# sorted book by price low to high
data.sort(key=lambda x: x["Price"])

# descending rating sort books
# data.sort(key=lambda x: x["Rating"], reverse=True)


# write a file 
try:
    # csv
    with open('books_sorted.csv', 'w', newline="", encoding="utf-8") as file:

        # write dictionary
        writer = csv.DictWriter(file, fieldnames=["Title", "Price", "Rating"])

        writer.writeheader() # write header
        writer.writerows(data) # write filter row

    # json
    with open("books_sorted.json", "w") as f:
        json.dump(data, f, indent=4) 

    print("Top 50 books sorted by price saved.")       

except Exception as e:
    print("Error:", e)   