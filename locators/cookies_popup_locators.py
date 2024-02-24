from selenium.webdriver.common.by import By


class CookiesPopupLocators(object):
    """This class contains all the locators for the cookies popup"""

    ACCEPT_ALL_COOKIES = (By.XPATH, '//*[@id="content"]/div[2]/div[6]/div[1]/ytd-button-renderer[2]/y'
                                    't-button-shape/button/yt-touch-feedback-shape/div/div[2]')

