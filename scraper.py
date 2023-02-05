# Selenium imports
from selenium import webdriver
from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
)
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# Global settings for the driver
chrome_options = Options()
chrome_options.add_experimental_option(
    "detach", True
)  # keeps driver open until manual termination
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
)  # Set up user-agent for ethical scraping


def scraper(amazon_link: str):
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        chrome_options=chrome_options,
    )
    driver.get(amazon_link)
