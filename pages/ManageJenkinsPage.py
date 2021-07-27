from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class ManageJenkinsPage(BasePage):
    """
    initialized driver

    """

    def __init__(self, driver):
        super().__init__(driver)


class ManageJenkinsPageLocators:
    MANAGE_USERS = (By.XPATH, '//a[contains(@title, "Manage Users")]')
