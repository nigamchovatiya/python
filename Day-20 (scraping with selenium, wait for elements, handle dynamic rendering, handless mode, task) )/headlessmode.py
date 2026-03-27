"""
headless mode:
Runs the browser in the background without opening a window.

Faster and saves system resources.

why use:
 faster
 save memory
 automation server
"""

# ------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
 
# ------------------------------------------------------

options = Options() # setting create
options.add_argument("--headless=new")  # headless mode
# browser runs in background

# setup driver
driver = webdriver.Chrome(
    service = Service(ChromeDriverManager().install()),
    options = options # setting assign in driver
    
)
  
driver.get("https://example.com")
print(driver.title)

# close browser
driver.quit()