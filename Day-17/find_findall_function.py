
# ----------------------------------------------------------

import requests
from bs4 import BeautifulSoup

# ----------------------------------------------------------

url = "https://www.wix.com/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(url, headers = headers)

try:
    print("status:", r.status_code)

    soup = BeautifulSoup(r.text, "html.parser")

    # find() -------------------------
    print("\n-------find method--------")
    name = soup.find("p", class_="font_6 wixui-rich-text__text")
    print(name.text) # Hi, I'm Aria

    description = soup.find("span", {"class": "wixui-rich-text__text"})
    print(description.text)


    # findall() ----------------------------
    print("\n-------findall method--------")
    name = soup.find_all("p", class_="FBGLaT")
    
    for n in name:
        print(n.text) # footer section name return

    print(name[2]) # 2nd position name return   


except Exception as e:
    print("Error:", e)    
