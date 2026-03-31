"""
It scrapes Techforce blog page and,

- Gets all blog links
- Opens each blog
- Extracts title, paragraphs, author, date
"""

# ------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ------------------------------------------------------

# setup
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 20)

driver.get("https://techforceglobal.com/blog/")

print("\n*------------------Blog List-------------------*\n")

# wait for blog cards
blogs = wait.until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, ".box-shado")
    )
)

# collect blog links
links = []

for blog in blogs:
    try:
        link = blog.find_element(By.CSS_SELECTOR, "b > a").get_attribute("href")
        links.append(link)
    except:
        continue

print("Total blogs found:", len(links))


# ------------------------------------------------------
# Open each blog and extract data
# ------------------------------------------------------

print("\n*------------------Blog Details-------------------*\n")

for link in links:
    try:
        driver.get(link)

        # wait blog content load
        blog_container = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".details-page.single-blog-content .col-md-8")
            )
        )

        # ---------------- Title ----------------
        title = blog_container.find_element(By.TAG_NAME, "h2").text.strip()

        # ---------------- Paragraphs ----------------
        paragraphs = blog_container.find_elements(By.TAG_NAME, "p")

        desc = []

        for p in paragraphs:
            text = p.get_attribute("textContent").strip()
            if text:
                clean_text = " ".join(text.split())
                desc.append(clean_text)

        # ---------------- Author & Date ----------------
        author = blog_container.find_element(By.CSS_SELECTOR, "p.mt-3 b").text.strip()
        date = blog_container.find_element(By.CSS_SELECTOR, "p.mt-3 font").text.strip()

        # ---------------- Print ----------------
        print("Title:", title)
        print("Author:", author)
        print("Date:", date)

        print("\nDescription:")
        for d in desc:
            print("-", d)

        print("=" * 60)

    except:
        continue


# ----------------------------------------------------------
# close browser
# ----------------------------------------------------------

driver.quit()