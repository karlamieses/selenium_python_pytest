from utils.env import BASE_URL

from selenium.webdriver.common.by import By


class YoutubeCookiePopup:

    def __init__(self, driver):
        self.driver = driver
        self.accept_cookie_button_locator = (
            By.XPATH, '//*[@id="content"]/div[2]/div[6]/div[1]/ytd-button-renderer[2]/y'
            't-button-shape/button/yt-touch-feedback-shape/div/div[2]')

    def open(self):
        self.driver.get(BASE_URL)

    def click_accept_cookies(self):
        accept_cookie_button = self.driver.find_element(*self.accept_cookie_button_locator)
        accept_cookie_button.click()
