"""
here i scrap diffrent diffrent element 
in a techforce site.
"""

# ----------------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ---------------------About title scrap------------------------

# setup driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 25)

# open website
driver.get("https://techforceglobal.com/")

# about title select
titles = wait.until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "div.section-title h1")
    )
)

title = titles[0] # first title select

# scroll webpage until element visible
driver.execute_script("arguments[0].scrollIntoView();", title)

print("Title:" ,title.text) # title print



# -----------------About button - page card scrap-------------------

# click btn explore more

about_btn = wait.until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "div.about-btn a.Main-Button")
    )
)

# about_btn.click() # normal click may fail

# click with js
driver.execute_script("arguments[0].click();", about_btn)

# wait for new page
# card-main div load until wait
wait.until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, "div.solution-card-main")
    )
)

# get all cards
cards = wait.until(
    EC.visibility_of_all_elements_located(
        (By.CSS_SELECTOR, "div.solution-card-main div.solution-card")
    )
)

# print first card detail
print(cards[0].text) # custom software development


# --------------Navbar fintech solution page h1 scrap-----------------

# reload homepage
driver.get("https://techforceglobal.com/")

# Scroll to footer
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Find Fintech link in footer
fintech_link = wait.until(
    EC.element_to_be_clickable(
        # find in footer in a title = "Fintech Solutions"
        (By.CSS_SELECTOR, "footer a[title = 'Fintech Solutions']")
    )
)

# Click js
driver.execute_script("arguments[0].click();", fintech_link)

# Wait for Fintech page to load
wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".banner-index-main"))
)

# get the h1 title
h1 = wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".banner-index-text h1")
    )
)

# print h1 title
print(h1.text)


# -------------Fintech page sildebar first title scrap----------------


# click connect with us in fintech page

cont_btn = wait.until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "div.nav-pills a#v-pills-2-tab")
    )
)

# scroll tab
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", cont_btn)

# click with js
driver.execute_script("arguments[0].click();", cont_btn)

# wait for tab content
wait.until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, "div#v-pills-tabContent")
    )
)

# get all details
details = wait.until(
    EC.visibility_of_all_elements_located(
        (By.CSS_SELECTOR, "div.tab-pane.active div.card-header h4")
    )
)

for d in details:
    print(d.text) # active tab print


# -------------------click case study and scrap data----------------------

# click button of case study in fintech page
click_btn = wait.until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "div.portfolio-txt a.case-study-btn")
    )
)

# scroll tab
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", click_btn)

# js click 
driver.execute_script("arguments[0].click();", click_btn)

# wait for tab content
wait.until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, "div.portfolioin-banntxt")
    )
)

# get all h3
all_heading = wait.until(
    EC.visibility_of_all_elements_located(
        # get all h3 in span
        (By.CSS_SELECTOR, "div.portfolioinner-banntxt ul li span > h3")
    )
)

for heading in all_heading:
    print(heading.text)



# ---------------- click book appoitment -------------------


book_btn = wait.until(
    EC.element_to_be_clickable(
        # (By.CSS_SELECTOR, "button.custom-btn a.text")
        (By.CSS_SELECTOR, "button.custom-btn")
    )
)

book_btn.click()

# wait for tab content
# wait.until(
#     EC.presence_of_element_located(
#         (By.CSS_SELECTOR, "div#root")
#     )
# )


# close browser
driver.quit()