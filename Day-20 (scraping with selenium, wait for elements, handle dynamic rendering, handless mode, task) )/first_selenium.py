"""
selenium used for dynamic site scraping.

command: 
    - pip install selenium
    - pip install webdriver-manager

here basic selenium code open site automatic in chrome
"""


# ----------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
 
# ----------------------------------------------------------

# setup driver 
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
 
# open website 
driver.get("https://example.com")

# wait 4 sec to see 
time.sleep(4) 

# close browser
driver.quit()