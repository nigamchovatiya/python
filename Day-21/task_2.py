"""
here i scrape a total country name and print,
find country with highest population, and 
filter under 1 million population country and 
print in all output in csv file. 
"""


# -----------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
 
 
# -------------------print country name----------------------
 
# setup driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 25)
 
# open website
driver.get("https://www.scrapethissite.com/pages/simple/")
 
# name select
countries  = wait.until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "div.country > h3.country-name")
    )
)
 
# scroll webpage until element visible
driver.execute_script("arguments[0].scrollIntoView();", countries [0])
 
for country in countries :
    print("Country:" ,country.text) # country print
 
total = len(countries)
print(total) # 250
 
 
# -------------find country with highest population---------------
 
# get country block
countries = wait.until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "div.country")
    )
)
 
# store data
data = []
 
for country in countries:
    name = country.find_element(By.CSS_SELECTOR,
            "h3.country-name").text.strip()
    population = country.find_element(By.CSS_SELECTOR,
            "span.country-population").text
    population = int(population.replace(",", ""))
 
    data.append({
        "Country": name,
        "Population": population
    })
 
# create dataframe
df = pd.DataFrame(data)
 
df.to_csv("countries_population.csv", index=False)
 
# find max population country
 
highest_populated_country = df.sort_values(by="Population",
                            ascending=False).iloc[0]
 
print("Highest Population Country:")
print(highest_populated_country)
 
highest_populated_country.to_frame().T.to_csv(
    "highest_population.csv", index=False
)
 
 
#---------------------- country under a 1 million population-----------------------
 
small_countries = df[df["Population"] < 1000000]
print("Countries under 1 Million population...")
print(small_countries)
small_countries.to_csv("small_countries.csv", index=False)
 
# close browser
driver.quit()
 