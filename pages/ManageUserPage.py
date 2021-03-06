from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from config.TestData import TestData
from pages.StringUtils import *


class ManageUserPage(BasePage):
    """
    initialized driver
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.go_to_page(ManageUserPage.URL_USER_MANAGE)

    name = generate_random_string(10)
    password = generate_random_string_and_int(10)
    edit_name = generate_random_string(10)
    edit_password = generate_random_string_and_int(10)
    job_name = generate_random_string(5)
    specific_symbol = generate_random_special_symbol(1)

    username_id = (By.ID, "username")
    password_input_name = (By.NAME, "password1")
    enter_confirm_password = (By.NAME, "password2")
    fullname_name = (By.NAME, "fullname")
    email_name = (By.NAME, "email")
    BUTTON_CREATE_ID = (By.ID, "yui-gen1-button")

    USER_NAME = f'{name}'
    USER_NAME_EDIT = f'{edit_name}'
    PASSWORD = f'{password}'
    PASSWORD_EDIT = f'{edit_password}'
    USER_FULLNAME = f'User {name}'
    USER_FULLNAME_EDIT = f'User {edit_name}'
    USER_EMAIL = f"{name}@gmail.com"
    USER_EMAIL_EDIT = f"{edit_name}@gmail.com"
    USER_NAME_UNDERSCORE = '_'
    USER_NAME_HYPHEN = '-'
    USER_NAME_MORE_255_SYMBOLS = f'{name * 30}'
    USER_FULLNAME_DOT = '.'
    USER_PASSWORD_DOT = '.'
    USER_FULLNAME_WITH_DOT = f'User . {name}'
    USER_PASSWORD_MORE_255_SYMBOLS = f'{password * 30}'
    USER_EMAIL_ETTA = '@'
    USER_EMAIL_WO_DOT = f'{name}@gmailcom'
    USER_EMAIL_WO_ETTA = f'{name}gmail.com'
    EMPTY_FIELD = ''
    USER_NAME_NOT_ALPHABETIC = 'Алфавит'
    USER_NAME_WITH_DOT = USER_NAME + '.'
    USER_NAME_WITH_SPECIAL_SYMBOL = USER_NAME + specific_symbol
    USER_NAME_WITH_ETTA = USER_NAME + '@'
    USER_NOT_CORRECT_NAME = [USER_NAME_NOT_ALPHABETIC, USER_NAME_WITH_ETTA, USER_NAME_WITH_DOT,
                             USER_NAME_WITH_SPECIAL_SYMBOL, EMPTY_FIELD]
    USER_PASSWORD_NOT_CORRECT = [EMPTY_FIELD, PASSWORD_EDIT]
    USER_EMAIL_NOT_CORRECT = [USER_EMAIL_WO_ETTA, EMPTY_FIELD]

    USER_ID = (By.XPATH, f"//table[@id='people']//tr/td/a[text()='{name}']")
    USER_ID_EDIT = (By.XPATH, f"//table[@id='people']//tr/td/a[text()='{edit_name}']")
    USER_ID_UNDERSCORE = (By.XPATH, "//table[@id='people']//tr/td/a[text()='_']")
    USER_ID_HYPHEN = (By.XPATH, "//table[@id='people']//tr/td/a[text()='-']")
    USER_ID_MORE_255_SYMBOLS = (By.XPATH, f"//table[@id='people']//tr/td/a[text()='{name * 30}']")
    USER_ID_DELETE = \
        (By.XPATH, f"//a[contains(@href, 'user/{name.lower()}/delete')]/img[contains(@class, 'icon-edit-delete')]")
    USER_ID_YES = (By.ID, "yui-gen1-button")
    PEOPLE_LIST = (By.XPATH, f"//tr[@id='person-{name}']/td/a")
    PEOPLE_LIST_ALL_RECORD = (By.XPATH, "//tr[contains(@id, 'person')]/td/a[contains(@href, 'user')]")

    CREATE_USER = (By.XPATH, '//span[text()="Create User"]')
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
    USER_DELETE_BUTTON = (By.XPATH, '//span[text()="Delete"]')
    USER_DELETE_YES_BUTTON = (By.ID, 'yui-gen1-button')

    STARTED_BY_USER = (By.CSS_SELECTOR, 'pre.console-output a')

    LOG_OUT_BUTTON = (By.XPATH, '//span[text()="log out"]')

    URL_USER_CREATE = TestData.BASE_URL + 'securityRealm/addUser'
    URL_USER_MANAGE = TestData.BASE_URL + 'securityRealm/'
    URL_USER_CREATE_ERROR = URL_USER_MANAGE + 'createAccountByAdmin'
    URL_JOB_VIEW_FROM_USER = TestData.BASE_URL + f'user/{name}/builds'

    ERRORS = (By.CLASS_NAME, 'error')
    ERROR_USER_CREATE_NAME = 'User name must only contain alphanumeric characters, underscore and dash'
    ERROR_USER_USERNAME = '\"\" is prohibited as a username for security reasons.'
    ERROR_USER_TAKEN_NAME = 'User name is already taken'
    ERROR_USER_PASSWORD = 'Password is required'
    ERROR_USER_FULLNAME = '\"\" is prohibited as a full name for security reasons.'
    ERROR_USER_EMAIL = 'Invalid e-mail address'
    ERROR_USER_PASSWORD_DONT_MATCH = 'Password didn\'t match'
    ERRORS_TEXT = [ERROR_USER_CREATE_NAME, ERROR_USER_PASSWORD_DONT_MATCH,
                   ERROR_USER_USERNAME, ERROR_USER_EMAIL, ERROR_USER_FULLNAME,
                   ERROR_USER_PASSWORD, ERROR_USER_TAKEN_NAME]

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

    def fill_all_field_and_click_save_diff_value(self, name, password, fullname, email):
        """
        in the during create new user fill out all fields
        push on the button

        :param email:
        :param fullname:
        :param name:
        :param password:
        :return:

        this object
        """
        self.do_send_keys(ManageUserPage.username_id, name)
        self.do_send_keys(ManageUserPage.password_input_name, password)
        self.do_send_keys(ManageUserPage.enter_confirm_password, password)
        self.do_send_keys(ManageUserPage.fullname_name, fullname)
        self.do_send_keys(ManageUserPage.email_name, email)
        self.click(ManageUserPage.BUTTON_CREATE_ID)
        return self

    def fill_all_field_and_click_save_with_all_diff_values(self, name, password1, password2, fullname, email):
        """
        in the during create new user fill out all fields
        push on the button

        :param email:
        :param fullname:
        :param name:
        :param password1:
        :param password2:
        :return:

        this object
        """
        self.do_send_keys(ManageUserPage.username_id, name)
        self.do_send_keys(ManageUserPage.password_input_name, password1)
        self.do_send_keys(ManageUserPage.enter_confirm_password, password2)
        self.do_send_keys(ManageUserPage.fullname_name, fullname)
        self.do_send_keys(ManageUserPage.email_name, email)
        self.click(ManageUserPage.BUTTON_CREATE_ID)
        return self

    def delete_user(self, name):
        """
        delete user from list
        :param name:
        :return:
        """
        URL_USER_FOR_DELETE = TestData.BASE_URL + f'securityRealm/user/{name}/'

        driver = ManageUserPage(self.driver)
        driver.go_to_page(URL_USER_FOR_DELETE)
        driver.click(ManageUserPage.USER_DELETE_BUTTON)
        driver.get_wait_and_click(self.USER_DELETE_YES_BUTTON)
