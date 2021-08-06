from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class ProjectPageLocators:
    PROJECT_NAME = (By.XPATH, '//h1')
    DELETE_PROJECT = (By.XPATH, '//a/span[contains(text(),"Delete")]')
    DISABLE_PROJECT_BUTTON = (By.XPATH, '//button[text()="Disable Project"]')
    ENABLE_PROJECT_BUTTON = (By.XPATH, '// button[text() = "Enable"]')
    DISABLE_PROJECT_WARNING = (By.XPATH, "//div[@class='warning']")
    BUILD_NOW = (By.XPATH, "//a[@title='Build Now']//span[2]")

class ProjectPage(BasePage):
    """
    initialized driver
    added moving to the BasePage after log in
    """

    def __init__(self, driver):
        super().__init__(driver)

