"""
wait object:
  use to avoid when element load slowly.

useful condition:
EC.presence_of_element_located()     # element exists in DOM
EC.visibility_of_element_located()   # visible on screen
EC.element_to_be_clickable()         # ready to click
EC.text_to_be_present_in_element()   # wait for text  

"""

# -----------------------------------------------------

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# -----------------------------------------------------

# setup driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
 
# open website 
driver.get("https://books.toscrape.com/")

# create wait object - wait 10 sec
wait = WebDriverWait(driver, 10)

# wait for next button to be clickable
next_button = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "li.next a"))
)

# click next button
next_button.click()

# close browser
driver.quit()
