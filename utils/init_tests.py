import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def driver():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    yield driver

    driver.quit()
