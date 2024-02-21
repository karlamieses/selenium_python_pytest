from utils.env import BASE_URL
from locators.cookies_popup_locators import CookiesPopupLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CookiesPopup:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(BASE_URL)

    def click_accept_cookies(self, driver):
        (WebDriverWait(driver, 15).until(EC.presence_of_element_located(CookiesPopupLocators.ACCEPT_ALL_COOKIES))
         .click())

