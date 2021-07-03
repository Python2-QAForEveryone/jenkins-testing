import random
import string

from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class CreateUserPage(BasePage):

    """
    initialized driver
    added moving to the BasePage after log in
    """
    def __init__(self, driver):
        super().__init__(driver)

    name = (''.join(random.choice(string.ascii_letters) for i in range(10)))

    username_id = (By.ID, "username")
    password_input_name = (By.NAME, "password1")
    enter_confirm_password = (By.NAME, "password2")
    fullname_name = (By.NAME, "fullname")
    email_name = (By.NAME, "email")
    button_create_id = (By.ID, "yui-gen1-button")

    USER_NAME = (By.XPATH, f'//tr[@id=\'person-{name}\']')
    PEOPLE_DELETE = (By.XPATH, f"//a[contains(@href, '/user/{name.lower()}')]")
    BUTTON_DELETE = (By.XPATH, f"//a[contains(@href, '/user/{name.lower()}/delete')]")
    BUTTON_YES = (By.ID, "yui-gen1-button")
