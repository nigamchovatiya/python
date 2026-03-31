"""
It scraped a techforce global website and,

- All visible data of home page extract and print.

"""

# ------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

# ------------------------------------------------------


# setup
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 35)

driver.get("https://techforceglobal.com/")


# ------------------------------------------------------
# Hero section - first section
# ------------------------------------------------------

print("\n*-------------Breadcrumb Section-----------------*\n")

# wait for hero section
wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, ".Hero-Section")
    )
)

# get ALL paragraphs inside hero section
paragraphs = wait.until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, ".Hero-Section p")
    )
)

# find paragraph with visible text
final_paragraph = ""

for p in paragraphs:
    text = p.get_attribute("textContent").strip()
    
    # check visible paragraph
    if p.is_displayed() and text:
        final_paragraph = text
        break

# get title (same approach)
titles = driver.find_elements(
    By.CSS_SELECTOR, ".Hero-Section h3#quote"
)

final_title = ""

for t in titles:
    text = t.get_attribute("textContent").strip()
    if t.is_displayed() and text:
        final_title = text
        break

# print
print("Title:\n",final_title)
print("Paragraph:\n",final_paragraph)


# ------------------------------------------------------
# About content
# ------------------------------------------------------

print("\n*-------------About Section-----------------*\n")

# about content
right_about = wait.until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "div.about-right")
    )
)

# get title and paragraph and ul-li

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

# about paragraph 
about_paragraph = wait.until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "div.section-title p")
    )
)

paragraph = ""

for p in about_paragraph:
    text = p.get_attribute("textContent").strip()
    
    # check visible paragraph
    if p.is_displayed() and text:
        final_paragraph = text
        break

print("About Paragraph:", final_paragraph)

# get all li items
all_ul = wait.until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "div.section-title ul.features > li")
    )
)

# loop and print each li
print("\nAbout li:")

for li in all_ul:
    text = li.text.strip()
    print(text)


# -------------------------------------------------------
# Technology stack        
# -------------------------------------------------------       

print("\n*---------------Technology Stack--------------*\n") 

# wait for main container load
technology = wait.until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, ".homepage-tech-logos-main")
    )
)

# get all elements inside a technology stack section
ul_navs = wait.until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, ".nav > li")
    )
)

# all li print
for li in ul_navs:
    all_nav = li.text.strip()
    print(all_nav)


# -------------------------------------------------------
# Services Techforce Providers      
# -------------------------------------------------------

print("\n*--------------Service Techforce Provided---------------*\n")

# wait for section
service_section = wait.until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, ".services-section")
    )
)

# card select
cards = wait.until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, ".services-section .slick-slide")
    )
)

print("Total cards found:", len(cards))
print("Services:\n")

for card in cards:
    try:
        # skip hidden slides
        if not card.is_displayed():
            continue

        # extract safely
        h3 = card.find_element(By.TAG_NAME, "h3").get_attribute("textContent").strip()
        btn = card.find_element(By.TAG_NAME, "button").get_attribute("textContent").strip()

        # active card heading and button text return
        print("Heading:", h3)
        print("Button:", btn)
        print("-" * 40)

    except Exception as e:
        continue


# -------------------------------------------------------
# Featured Case Study  
# -------------------------------------------------------

print("\n*------------------Featured Case Study-------------------*\n")

# wait for portfolio section
portfolio_section = wait.until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, ".portfolio-section")
    )
)

# combine both card main section
cards = portfolio_section.find_elements(
    By.CSS_SELECTOR, ".portfolio-main > div, .portfolio-main1 > div"
)

print("Case Studies:\n")

seen = set()

for card in cards:
    try:
        h5 = card.find_element(By.TAG_NAME, "h5").get_attribute("textContent").strip()
        p = card.find_element(By.TAG_NAME, "p").get_attribute("textContent").strip()

        key = (h5, p)

        if key in seen:
            continue

        seen.add(key)

        print("Heading:", h5)
        print("Paragraph:", p)
        print("-" * 40)

    except:
        continue


# -------------------------------------------------------
# Our Process  
# -------------------------------------------------------

print("\n*------------------Our Process-------------------*\n")

# wait for section
process_section = wait.until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, ".Our-Approach-Section")
    )
)

# get ALL cards inside section
cards = process_section.find_elements(By.CSS_SELECTOR, ".card")

print("Total cards:", len(cards))
print("Process Steps:\n")

for card in cards:
    try:
        h3 = card.find_element(By.TAG_NAME, "h3").get_attribute("textContent").strip()
        p = card.find_element(By.TAG_NAME, "p").get_attribute("textContent").strip()


        print("Heading:", h3)
        print("Paragraph:", p)
        print("-" * 40)

    except:
        continue


# -------------------------------------------------------
# Testimonials
# -------------------------------------------------------

print("\n*------------------Our Success Story-------------------*\n")

# wait for section
testimonial_section = wait.until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, ".Testimonial-section div.testimonialAllContent")
    )
)

# get heading inside section
heading = testimonial_section.find_element(By.TAG_NAME, "h1").get_attribute("textContent").strip()

# print testimonial slide data
print("Heading:", heading)


# -------------------------------------------------------
# Contact with us
# -------------------------------------------------------

print("\n*------------------Contact with us-------------------*\n")

# wait for section 
contact_section = wait.until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, "div.contact-details")
    )
)

# get header and and location and contact no
heading = contact_section.find_element(By.TAG_NAME, "h2").get_attribute("textContent").strip()

# print heading
print("Heading:", heading)


# Contact details box
detail_box = wait.until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "div.contact-details-box > .contact-country")
    )
)

for contact_all in detail_box:
    p = contact_all.find_element(By.CSS_SELECTOR,
        "p").text.strip()
    print(p)


# -------------------------------------------------------
# Contact us Form 
# -------------------------------------------------------

print("\n*------------------Contact Form-------------------*\n")

# wait for form
form_detail = wait.until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, "div.con_foot_form")
    )
)

# scroll form 
driver.execute_script("arguments[0].scrollIntoView({block:'center'});", form_detail)



f_name = form_detail.find_element(By.CSS_SELECTOR, "#First_Name").send_keys("Amit")
l_name = form_detail.find_element(By.CSS_SELECTOR, "#Last_Name").send_keys("Kapadiya")
email = form_detail.find_element(By.CSS_SELECTOR, "#Email").send_keys("amit56@gmail.com")
phone_number = form_detail.find_element(By.CSS_SELECTOR, "#Phone").send_keys("9114555555")
category = Select(form_detail.find_element(By.CSS_SELECTOR, "#LEADCF10")
    ).select_by_value("BlockChain Development")
description = form_detail.find_element(By.CSS_SELECTOR, "#Description"
    ).send_keys("I want to develop a blockchain site.")

time.sleep(5)


submit_form = form_detail.find_element(By.CSS_SELECTOR, "#formsubmit")

print("Form fill successfully.")


# -------------------------------------------------------
# Footer paragraph 
# -------------------------------------------------------

print("\n*------------------Footer Message-------------------*\n")

# wait content load
footer_paragraph = wait.until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, "div.footer-main div.widget")
    )
)

final_paragraph = footer_paragraph.find_element(By.TAG_NAME, "p").get_attribute("textContent").strip()

print(final_paragraph)


# ----------------------------------------------------------
# close browser
# ----------------------------------------------------------

driver.quit()