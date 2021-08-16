import random
import string

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

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
    edit_password = (''.join(random.choice(string.ascii_letters + string.digits) for i in range(10)))
    job_name = (''.join(random.choice(string.ascii_letters) for i in range(5)))

    username_id = (By.ID, "username")
    password_input_name = (By.NAME, "password1")
    enter_confirm_password = (By.NAME, "password2")
    fullname_name = (By.NAME, "fullname")
    email_name = (By.NAME, "email")
    BUTTON_CREATE_ID = (By.ID, "yui-gen1-button")

    USER_NAME = f'{name}'
    PASSWORD = f'{password}'
    PASSWORD_EDIT = f'{edit_password}'
    USER_FULLNAME = f'User {name}'
    USER_FULLNAME_EDIT = f'User {edit_name}'
    USER_EMAIL_EDIT = f"{edit_name}@gmail.com"
    USER_NAME_UNDERSCORE = '_'
    USER_NAME_HYPHEN = '-'
    USER_NAME_MORE_255_SYMBOLS = f'{name * 30}'

    USER_ID = (By.XPATH, f"//table[@id='people']//tr/td/a[text()='{name}']")
    USER_ID_UNDERSCORE = (By.XPATH, "//table[@id='people']//tr/td/a[text()='_']")
    USER_ID_HYPHEN = (By.XPATH, "//table[@id='people']//tr/td/a[text()='-']")
    USER_ID_MORE_255_SYMBOLS = (By.XPATH, f"//table[@id='people']//tr/td/a[text()='{name*30}']")
    USER_ID_DELETE = (By.XPATH, f"//a[contains(@href, 'user/{name.lower()}/delete')]/img[contains(@class, 'icon-edit-delete')]")
    USER_ID_YES = (By.ID, "yui-gen1-button")
    PEOPLE_LIST = (By.XPATH, f"//tr[@id='person-{name}']/td/a")
    PEOPLE_LIST_ALL_RECORD = (By.XPATH, "//tr[contains(@id, 'person')]/td/a[contains(@href, 'user')]")

    CREATE_USER = (By.XPATH, '//span[text() = "Create User"]')
    CONFIGURE_USER = (By.XPATH, f"//a[contains(@href, 'user/{name.lower()}/configure')]/img")
    INPUT_FULLNAME = (By.XPATH, '//input[@name="_.fullName"]')
    INPUT_EMAIL = (By.NAME, 'email.address')
    INPUT_PASSWORD = (By.NAME, 'user.password')
    INPUT_CONFIRM_PASSWORD = (By.NAME, 'user.password2')
    SAVE_BUTTON = (By.ID, 'yui-gen2-button')
    FULLNAME_TEXT = (By.TAG_NAME, 'h1')

    CREATE_USER_JOB = f'{job_name}'
    URL_JOB_CREATE = TestData.BASE_URL + f'job/{job_name}/configure'
    JOB_DELETE_PROJECT = (By.XPATH, '//span[text()="Delete Project"]')

    STARTED_BY_USER = (By.XPATH, f'//a[@href="/user/{name}")]')

    LOG_OUT_BUTTON = (By.XPATH, '//span[text()="log out"]')

    URL_USER_CREATE = TestData.BASE_URL + 'securityRealm/addUser'
    URL_USER_MANAGE = TestData.BASE_URL + 'securityRealm/'

    URL_JOB_CREATE = TestData.BASE_URL + 'view/all/newJob'

    def click_button_create_new_user(self):
        """
        push on the button
        :return:
        """
        self.click(self.CREATE_USER)
        return self

    def fill_all_field_and_click_save(self, name, password):
        """
        in the during create new user fill out all fields
        push on the button

        :param name:
        :param password:
        :return:

        this object
        """
        self.do_send_keys(ManageUserPage.username_id, name)
        self.do_send_keys(ManageUserPage.password_input_name, password)
        self.do_send_keys(ManageUserPage.enter_confirm_password, password)
        self.do_send_keys(ManageUserPage.fullname_name, f"User {name}")
        self.do_send_keys(ManageUserPage.email_name, f"{name}@gmail.com")
        self.click(ManageUserPage.BUTTON_CREATE_ID)
        return self
