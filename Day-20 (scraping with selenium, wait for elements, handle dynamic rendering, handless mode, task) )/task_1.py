"""
selenium open books.toscrap website automatic and find
next button and click. 

locate elements:
# by ID
driver.find_element("id", "username")

# by Name
driver.find_element("name", "user")

# by class
driver.find_element("class name", "form-control")

# by tag
driver.find_element("tag name", "input")

# by CSS selector
  # id
  driver.find_element("css selector", "#username")

  # class
  driver.find_element("css selector", ".form-control")

# by XPath
driver.find_element("xpath", "//input[@id='username']")

"""


# ---------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


# ---------------------------------------------------------

# setup driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
 
# open website 
driver.get("https://books.toscrape.com/")

# find next button and click
next_button = driver.find_element("css selector", "li.next a")
next_button.click()
  
# wait to see result
time.sleep(4)

# close browser
driver.quit()
