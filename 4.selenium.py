"""
- For sites that require interaction (example: Pressing load more button)
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("user-agent=MyScraperBot")
driver = webdriver.Chrome(options=options)

# The URL we want to scrape
URL = "https://books.toscrape.com/"

driver.get(URL)

try:
    for _ in range(4): # load the first 5 pages
        # Find all book titles on the current page
        books = driver.find_elements(By.CSS_SELECTOR, 'article.product_pod h3 a')
        titles = [book.get_attribute('title') for book in books]
        print(titles)
        
        # Sleep for the rate limit delay
        time.sleep(3)
        
        # Check if the "next" button is present on the page
        next_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'li.next a'))
        )

        # Click the "next" button if it is not the last page
        if "next" in next_button.get_attribute('innerHTML').lower():
            next_button.click()
        else:
            print("No more pages to load.")
            break

        # Wait for the next page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'ul.pager'))
        )

except Exception as e:
    print(f"Finished loading pages or encountered an error: {e}")

# Don't forget to close the driver after your scrape is complete
driver.quit()
