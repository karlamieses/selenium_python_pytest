import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.init_tests import driver

from resources.cookies_popup import YoutubeCookiePopup

driver()


@pytest.fixture(scope='module')
def test_accept_all_cookies_closes_popup(driver):
    youtube_cookie_popup = YoutubeCookiePopup(driver)
    youtube_cookie_popup.open()
    youtube_cookie_popup.click_accept_cookies()

    WebDriverWait(driver, 10).until_not(
        EC.visibility_of_element_located(*youtube_cookie_popup.accept_cookie_button_locator))

    assert not driver.find_element(*youtube_cookie_popup.accept_cookie_button_locator)
