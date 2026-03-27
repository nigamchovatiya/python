"""
here js site quotes.toscrape scrape after a full content load 
and save csv in quotes and author name. 

"""


# -----------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

# -----------------------------------------------------------------

# setup driver 
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# create wait object - wait 10 sec
wait = WebDriverWait(driver, 10)

# js site
driver.get("https://quotes.toscrape.com/js/")


# wait for content load
quotes = wait.until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "quote"))
)

# extract data
data = []

for q in quotes:
    text = q.find_element(By.CLASS_NAME, "text")
    author = q.find_element(By.CLASS_NAME, "author")
    data.append([text.text, author.text])

# save to csv
with open("quotes.csv", 'w', newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Quotes", "Author Name"])
    writer.writerows(data)



driver.quit()


