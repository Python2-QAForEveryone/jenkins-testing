import random
import string

from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from pages.DashboardPage import DashboardPageLocators, DashboardPage
from config.TestData import TestData
from pages.ManageJenkinsPage import ManageJenkinsPageLocators


class ManageUserPage(BasePage):
    """
    initialized driver

    """

    def __init__(self, driver):
        super().__init__(driver)
        self.go_to_page(ManageUserPage.URL_USER_MANAGE)

    name = (''.join(random.choice(string.ascii_letters) for i in range(10)))
    edit_name = (''.join(random.choice(string.ascii_letters) for i in range(10)))

    username_id = (By.ID, "username")
    password_input_name = (By.NAME, "password1")
    enter_confirm_password = (By.NAME, "password2")
    fullname_name = (By.NAME, "fullname")
    email_name = (By.NAME, "email")
    BUTTON_CREATE_ID = (By.ID, "yui-gen1-button")

    USER_NAME = f'{name.lower()}'

    USER_ID = (By.XPATH, f"//a[contains(@href, '/user/{name.lower()}/')]//..//../td[2]/a")
    USER_ID_1 = (By.XPATH, f"//a[text()={name}][1]")

    CREATE_USER = (By.XPATH, '//span[text() = "Create User"]')

    URL_USER_CREATE = TestData.BASE_URL + 'securityRealm/addUser'
    URL_USER_MANAGE = TestData.BASE_URL + 'securityRealm/'

    def go_to_manage_user_page(self):
        self.driver = DashboardPage(self.driver)
        self.driver.click(DashboardPageLocators.TEXT_MANAGE_JENKINS)
        self.driver.click(ManageJenkinsPageLocators.MANAGE_USERS)

    def click_button_create_user(self):
        self.driver.click(ManageUserPage.CREATE_USER)

    def fill_all_field_and_click_save(self):
        self.driver.do_send_keys(ManageUserPage.username_id, ManageUserPage.name)
        self.driver.do_send_keys(ManageUserPage.password_input_name, "12345")
        self.driver.do_send_keys(ManageUserPage.enter_confirm_password, "12345")
        self.driver.do_send_keys(ManageUserPage.fullname_name, f"User {ManageUserPage.name}")
        self.driver.do_send_keys(ManageUserPage.email_name, f"{ManageUserPage.name}@gmail.com")
        self.driver.click(ManageUserPage.BUTTON_CREATE_ID)
