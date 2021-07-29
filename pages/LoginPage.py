from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class LoginPage(BasePage):
    """
    initialized driver

    """

    def __init__(self, driver):
        super().__init__(driver)


class LoginPageLocators:
    INPUT_LOGIN = (By.ID, 'j_username')
    INPUT_PASSWORD = (By.ID, 'j_password')
    SIGN_IN_BUTTON = (By.NAME, 'Submit')
