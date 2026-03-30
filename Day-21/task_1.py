"""
here i scrap techforce page like all apify actors 
scrap and detail print and fill form using send_keys.
"""

# ----------------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


# ----------Apify actor and their information-------------

# setup driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 25)

# open website
driver.get("https://techforceglobal.com/")


# click a apify nav bar link

apify_btn = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//a[@title = 'Apify Actors']")
    )
)

# js click
driver.execute_script("arguments[0].click();", apify_btn)

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
print(total) # 7 actor



# --------------------apify all actor detail print-------------------

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


# -----------------------Fill contact us form-----------------------

# click navbar -> company btn
company_btn = driver.find_element(By.CSS_SELECTOR, "a[title='Company']")
company_btn.click()
 
# click sub -> contact us btn 
portfolio_btn = driver.find_element(By.CSS_SELECTOR, "a[title='Contact Us']")
portfolio_btn.click() 


# form field fill with keys
f_name = driver.find_element(By.CSS_SELECTOR, "#First_Name").send_keys("Soham")
l_name = driver.find_element(By.CSS_SELECTOR, "#Last_Name").send_keys("Patel")
email = driver.find_element(By.CSS_SELECTOR, "#Email").send_keys("randommail@gmail.com")
phone = driver.find_element(By.CSS_SELECTOR, "#Phone").send_keys("9114555555")
budget = Select(driver.find_element(By.CSS_SELECTOR, "#LEADCF10")
            ).select_by_value("Between 50K to 100K")
category = Select(driver.find_element(By.CSS_SELECTOR, "#LEADCF9")
            ).select_by_value("Ecommerce Solution")
description = driver.find_element(By.CSS_SELECTOR, "#Description"
            ).send_keys("random text")

# submit btn
submit_form = driver.find_element(By.CSS_SELECTOR, "#formsubmit")
 
# driver.execute_script("arguments[0].click()", submit_form)
# submit_form.click()    


# close browser
driver.quit()