

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 15)

driver.get("https://web-scraping.dev/")

# get cards
cards = wait.until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.col a.card"))
)

static_page = cards[0]

# scroll to element (IMPORTANT)
driver.execute_script("arguments[0].scrollIntoView();", static_page)

# click using JS (BEST FIX)
driver.execute_script("arguments[0].click();", static_page)

# wait new page
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.products")))

# get titles
titles = wait.until(
    EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div.description h3"))
)

# extract data
data = []

for t in titles:
    print(t.text.strip())

driver.quit()