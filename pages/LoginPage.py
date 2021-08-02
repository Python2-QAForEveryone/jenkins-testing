from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class LoginPage(BasePage):
    """
    initialized driver

    """

    def __init__(self, driver):
        super().__init__(driver)

    INPUT_LOGIN = (By.ID, 'j_username')
    INPUT_PASSWORD = (By.NAME, 'j_password')
    SIGN_IN_BUTTON = (By.NAME, 'Submit')
    ALERT_INVALID_DATA = (By.XPATH, '//form[@name ="login"]/div[contains(@class, "alert")]')
    ALERT_TEXT = "Invalid username or password"

    def login_jenkins(self, login, password):
        """
        input login/password and push button Submit on the Login Page
        :param login:
        :param password:
        :return:
        """
        self.do_send_keys(LoginPage.INPUT_LOGIN, login)
        self.do_send_keys(LoginPage.INPUT_PASSWORD, password)
        self.click(LoginPage.SIGN_IN_BUTTON)