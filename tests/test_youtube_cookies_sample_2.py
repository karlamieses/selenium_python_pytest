import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from utils.env import BASE_URL


class YoutubeCookiePopup:

    def __init__(self, driver):
        self.driver = driver
        self.accept_cookie_button_locator = (By.XPATH, '//*[@id="content"]/div[2]/div[6]/div[1]/ytd-button-renderer[2]/'
                                                       'yt-button-shape/button/yt-touch-feedback-shape/div/div[2]')

    def open(self):
        self.driver.get(BASE_URL)

    def click_accept_cookies(self, driver):
        WebDriverWait(driver, 30).until(EC.presence_of_element_located(self.accept_cookie_button_locator)).click()


@pytest.fixture(scope='module')
def driver():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    yield driver

    driver.quit()


def test_accept_all_cookies_closes_popup(driver):
    youtube_cookie_popup = YoutubeCookiePopup(driver)
    youtube_cookie_popup.open()
    youtube_cookie_popup.click_accept_cookies(driver)

    accept_cookies_element = driver.find_element(*youtube_cookie_popup.accept_cookie_button_locator)

    assert WebDriverWait(driver, 30).until(EC.staleness_of(accept_cookies_element))

