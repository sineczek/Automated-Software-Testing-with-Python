from tests.acceptance.locators.base_page import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return 'http://127.1:5000' # bez / na końcu

    @property
    def title(self):
        return self.driver.find_element(*BasePageLocators.TITLE)
    
