"""
here i save html code from a wix.com website
into page.html file.
"""

# ------------------------------------------------

import requests

# ------------------------------------------------

headers = {
    "User-Agent": "Chrome/5.0 (Windows NT 11.0)"
}


# request get fetch page
response = requests.get('https://www.wix.com/', headers=headers)


# save html code in another file
try:
    with open("page.html", "w", encoding = "utf-8") as file:
        # get html content and write in file
        file.write(response.text)

    print("html saved in file...")    


except Exception as e:
    print("Error:", e)


