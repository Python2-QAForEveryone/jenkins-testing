import random
import string

from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from config.TestData import TestData


class ManageUserPage(BasePage):
    """
    initialized driver

    """

    def __init__(self, driver):
        super().__init__(driver)
        self.go_to_page(ManageUserPage.URL_USER_MANAGE)

    name = (''.join(random.choice(string.ascii_letters) for i in range(10)))
    password = (''.join(random.choice(string.ascii_letters + string.digits) for i in range(10)))
    edit_name = (''.join(random.choice(string.ascii_letters) for i in range(10)))

    username_id = (By.ID, "username")
    password_input_name = (By.NAME, "password1")
    enter_confirm_password = (By.NAME, "password2")
    fullname_name = (By.NAME, "fullname")
    email_name = (By.NAME, "email")
    BUTTON_CREATE_ID = (By.ID, "yui-gen1-button")

    USER_NAME = f'{name}'
    PASSWORD = f'{password}'

    USER_ID = (By.XPATH, f"//table[@id='people']//tr/td/a[text()='{name}']")
    USER_ID_DELETE = (By.XPATH, f"//a[contains(@href, 'user/{name.lower()}/delete')]/img[contains(@class, 'icon-edit-delete')]")
    USER_ID_DELETE_YES = (By.ID, "yui-gen1-button")

    CREATE_USER = (By.XPATH, '//span[text() = "Create User"]')
    LOG_OUT_BUTTON = (By.XPATH, '//span[text()="log out"]')

    URL_USER_CREATE = TestData.BASE_URL + 'securityRealm/addUser'
    URL_USER_MANAGE = TestData.BASE_URL + 'securityRealm/'

    def click_button_create_new_user(self):
        self.click(self.CREATE_USER)
        return self

    def fill_all_field_and_click_save(self):
        self.do_send_keys(ManageUserPage.username_id, ManageUserPage.name)
        self.do_send_keys(ManageUserPage.password_input_name, ManageUserPage.password)
        self.do_send_keys(ManageUserPage.enter_confirm_password, ManageUserPage.password)
        self.do_send_keys(ManageUserPage.fullname_name, f"User {ManageUserPage.name}")
        self.do_send_keys(ManageUserPage.email_name, f"{ManageUserPage.name}@gmail.com")
        self.click(ManageUserPage.BUTTON_CREATE_ID)
        return self
