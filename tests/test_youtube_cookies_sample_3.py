import pytest

from locators.cookies_popup_locators import CookiesPopupLocators
from pages.cookies_popup import CookiesPopup

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(scope='module')
def driver():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    yield driver

    driver.quit()


def test_accept_all_cookies_closes_popup(driver):
    youtube_cookie_popup = CookiesPopup(driver)
    youtube_cookie_popup.open()
    youtube_cookie_popup.click_accept_cookies(driver)

    accept_all_cookies_locator = driver.find_element(*CookiesPopupLocators.ACCEPT_ALL_COOKIES)

    assert WebDriverWait(driver, 30).until(EC.staleness_of(accept_all_cookies_locator))
