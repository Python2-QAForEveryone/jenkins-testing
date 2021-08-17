from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class ProjectPageLocators:
    PROJECT_NAME = (By.XPATH, '//h1')
    DELETE_PROJECT = (By.XPATH, '//a/span[contains(text(),"Delete")]')
    DISABLE_PROJECT_BUTTON = (By.XPATH, '//button[text()="Disable Project"]')
    ENABLE_PROJECT_BUTTON = (By.XPATH, '// button[text() = "Enable"]')
    DISABLE_PROJECT_WARNING = (By.XPATH, "//div[@class='warning']")
    BUILD_NOW = (By.XPATH, "//a[@title='Build Now']//span[2]")
    BUILD_HISTORY_JOBS = (By.XPATH, '//tr[contains(@class, "build-row multi-line")]')
    BUILD_SUCCESS_JOBS = (By.XPATH, '//a[@class="build-status-link"]')
    # BUILD_SUCCESS_LAST_JOB = (By.XPATH, '//td[@class="build-row-cell"][1]//img')
    BUILD_SUCCESS_LAST_JOB = (By.XPATH, '//td[@class="build-row-cell"][1]//a[@class="build-status-link"]')

class ProjectPage(BasePage):
    """
    initialized driver
    added moving to the BasePage after log in
    """

    def __init__(self, driver):
        super().__init__(driver)

