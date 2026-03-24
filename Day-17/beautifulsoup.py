
# ----------------------------------------------------------

import requests
from bs4 import BeautifulSoup

# ----------------------------------------------------------

url = "https://webscraper.io/test-sites/e-commerce/allinone"

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(url, headers = headers)

try:
    print("status:", r.status_code)

    # html.parser convert raw html - structure tree 
    soup = BeautifulSoup(r.text, "html.parser")

    # print(soup) # print entire html
    print(soup.div) # print first div in html


except Exception as e:
    print("Error:", e)    

