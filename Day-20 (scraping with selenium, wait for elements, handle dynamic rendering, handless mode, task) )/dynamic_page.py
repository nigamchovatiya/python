"""
here program is fetch dynamic site data and print 
in a csv file.
"""

# ------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

# ------------------------------------------------------

# setup driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 15)

# open website
driver.get("https://web-scraping.dev/")

# get cards
cards = wait.until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.col a.card"))
)

static_page = cards[0] # first card select

# scroll webpage until element visible
driver.execute_script("arguments[0].scrollIntoView();", static_page)

# selenium click fails
# static_page.click()

# click using JS
driver.execute_script("arguments[0].click();", static_page)


# wait new page
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.products")))

# get titles
titles = wait.until(
    EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div.description h3"))
)

# extract data
data = []

for title in titles:
    text = title.text.strip()
    data.append([text])


# save data in csv
with open("dynamic_page.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    
    writer.writerow(["Product Title"])
    writer.writerows(data)   


print(data) # list print


driver.quit()