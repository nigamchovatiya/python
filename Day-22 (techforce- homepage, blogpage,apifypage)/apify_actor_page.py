"""
It scraped a apify-actor page and,

- Scrape all visible data of that page and print. 

"""


# ----------------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# ----------------------------------------------------

# setup driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 25)

# open website
driver.get("https://techforceglobal.com/apify-actors/")


# ---------------------------------------------------
# Details of Our Apify Actors
# ---------------------------------------------------

print("\n*------------------Smart scraping solution-------------------*\n")

# wait for section load
apify_section = wait.until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, "div.banner-index-main-content > .banner-index-text")
    )
)

h1 = apify_section.find_element(By.TAG_NAME, "h1").get_attribute("textContent").strip()
p = apify_section.find_element(By.TAG_NAME, "p").get_attribute("textContent").strip()

print("Heading:", h1)
print("Paragraph:", p)



# ---------------------------------------------------
# The Future of Data Scraping
# ---------------------------------------------------

print("\n*-------------The Future of data scraping--------------*\n")

# wait for new page
wait.until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, ".portfolio")
    )
)

# get all apify-actor
actors = wait.until(
    EC.visibility_of_all_elements_located(
        (By.CSS_SELECTOR, "div.portfolio-grid .portfolio-box")
    )
)

for actor in actors:
    title = actor.find_element(By.CSS_SELECTOR, "h3")
    print(actor.text) # all actor print


total = len(actors)
print("Total Actors:", total) # 7 actor


# --------------------apify all actors detail print-------------------

# loop 7 actor 7 times
for i in range(total):

    # re-fetch all actor links every time (VERY IMPORTANT)
    actors = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "div.portfolio-grid .portfolio-box a")
        )
    )

    actor = actors[i]   # use index

    # scroll
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", actor)

    # click
    driver.execute_script("arguments[0].click();", actor)

    # wait detail page
    wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div.portfolioinner-banntxt")
        )
    )

    print(f"\n---Actor {i+1}---") # actor + 1

    # get details
    all_heading = wait.until(
        EC.visibility_of_all_elements_located(
            (By.CSS_SELECTOR, "div.portfolioinner-banntxt ul li")
        )
    )

    for heading in all_heading:
        h3 = heading.find_element(By.CSS_SELECTOR, "h3").text
        p = heading.find_element(By.CSS_SELECTOR, "p").text

        print(h3)
        print(p)

    # go back
    driver.back()

    # wait grid again
    wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div.portfolio-grid")
        )
    )  



# ----------------------------------------------------------
# close browser
# ----------------------------------------------------------

driver.quit()
