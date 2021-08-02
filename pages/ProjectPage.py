from pages.BasePage import BasePage
from config.TestData import TestData as TD
from selenium.webdriver.common.by import By


class ProjectPageLocators:
    PROJECT_NAME = (By.XPATH, '//h1')
    DELETE_PROJECT = (By.XPATH, '//a/span[contains(text(),"Delete")]')
    DISABLE_PROJECT_BUTTON = (By.XPATH, '//button[text()="Disable Project"]')
    ENABLE_PROJECT_BUTTON = (By.XPATH, '// button[text() = "Enable"]')
    DISABLE_PROJECT_WARNING = (By.XPATH, "//div[@class='warning']")

class NewItemPage(BasePage):
    """
    initialized driver
    added moving to the BasePage after log in
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.go_to_page(TD.BASE_URL)
