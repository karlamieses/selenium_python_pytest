import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.env import BASE_URL


@pytest.fixture(scope='module')
def driver():
    # Options provides attributes to the browser, in this case chrome
    # "detach", won't close the browser as soon as is launched
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)

    # This launch the browser/driver
    yield driver

    # Close the browser/driver
    driver.quit()


def test_accept_button_closes_cookies_concept_popup(driver):
    # This tells the browser to go to our base_url = ""https://www.youtube.com/""
    driver.get(BASE_URL)

    # This search the element and store it into a variable, XPATHs locators are not recommended ⚠️
    accept_all = (By.XPATH, '//*[@id="content"]/div[2]/div[6]/div[1]/ytd-button-renderer[2]/yt-button-shape/button/'
                            'yt-touch-feedback-shape/div/div[2]')

    accept_all_element = driver.find_element(*accept_all)

    WebDriverWait(driver, 30).until(EC.presence_of_element_located(accept_all)).click()

    assert WebDriverWait(driver, 30).until(EC.staleness_of(accept_all_element))

