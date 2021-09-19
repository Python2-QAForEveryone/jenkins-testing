import random
import string
from config.TestData import TestData
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class FolderPage(BasePage):
    """
    initialized driver
    added moving to the BasePage after log in
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.go_to_page(URLLocators.URL_FOLDER_CREATE)

    special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '[', ']', '<', '>', '/', '\\', '|', ':', ';']
    dots = ['.', '..']
    three_or_more_dots = ['...', '....', '.....', '......', '.......', '........']
    white_spaces = [' ', '  ', '   ', '    ', '     ', '      ', '       ', '        ']

    name = (''.join(random.choice(string.ascii_letters) for i in range(10)))
    long_name = (''.join(random.choice(string.ascii_letters) for i in range(256)))
    name_start_special_ch = (''.join(random.choice(special_characters))) \
                            + (''.join(random.choice(string.ascii_letters) for i in range(9)))
    name_inside_special_ch = (''.join(random.choice(string.digits) for i in range(3))) \
                             + (''.join(random.choice(special_characters))) \
                             + (''.join(random.choice(string.ascii_letters) for i in range(6)))
    name_digits = (''.join(random.choice(string.digits) for i in range(10)))
    name_empty = ''
    name_start_dot = '.' + (''.join(random.choice(string.ascii_letters) for i in range(9)))
    name_inside_dot = (''.join(random.choice(string.digits) for i in range(3))) \
                      + '.' + (''.join(random.choice(string.ascii_letters) for i in range(6)))
    name_only_one_or_two_dot = (''.join(random.choice(dots)))
    # name_only_three_or_more_dots = (''.join(random.choice(three_or_more_dots)))
    name_only_three_or_more_dots = '...'
    name_whitespace = (''.join(random.choice(white_spaces)))

    TITLE = f"{name} Config [Jenkins]"
    TITLE_JOB = f"All [{name}] [Jenkins]"
    TITLE_DIGITS_JOB = f"All [{name_digits}] [Jenkins]"
    TITLE_DIGITS = f"{name_digits} Config [Jenkins]"
    TITLE_START_DOT = f"{name_start_dot} Config [Jenkins]"
    TITLE_START_DOT_JOB = f"All [{name_start_dot}] [Jenkins]"
    TITLE_INSIDE_DOT = f"{name_inside_dot} Config [Jenkins]"
    TITLE_INSIDE_DOT_JOB = f"All [{name_inside_dot}] [Jenkins]"
    TITLE_JOB_INSIDE_FOLDER = f"{name} [{name}] [Jenkins]"
    WRONG_TITLE = "Jenkins [Jenkins]"


class FolderPageLocator:
    LINK_NEW_ITEM = (By.XPATH, "//a[@title='New Item']")
    ITEM_NAME = (By.ID, 'name')
    LINK_FOLDER = (By.CLASS_NAME, 'com_cloudbees_hudson_plugins_folder_Folder')
    OK_BUTTON = (By.ID, 'ok-button')
    OK_BUTTON_DISABLED = (By.XPATH, "//button[@id='ok-button'][@class='disabled']")
    SAVE_BUTTON = (By.XPATH, '//span[@name="Submit"]')
    WRONG_REQUEST = (By.CSS_SELECTOR, 'div#error-description > h2')
    ITEM_NAME_INVALID = (By.XPATH, "//div[@id='itemname-invalid'][contains(text(),'is an unsafe character')]")
    ERROR_PAGE = (By.XPATH, "//div[@id='main-panel']/p[contains(text(),'is an unsafe character')]")
    ITEM_NAME_REQUIRED = (By.XPATH, "//div[@id='itemname-required'][contains(text(),'This field cannot be empty')]")
    ITEM_NAME_NOT_ALLOWED = (By.XPATH, "//div[@id='itemname-invalid'][contains(text(),'is not an allowed name')]")
    ERROR_PAGE_NONAME = (By.XPATH, "//div[@id='main-panel']/p[contains(text(),'No name is specified')]")
    LINK_DELETE_FOLDER = (By.XPATH, "//a[@title='Delete Folder']")
    BUTTON_YES = (By.ID, 'yui-gen1-button')
    LINK_EXIST_FOLDER = (By.CSS_SELECTOR, f'#job_{FolderPage.name} .model-link')
    EMPTY_FOLDER = (By.CSS_SELECTOR, ".h4")
    LINK_CREATE_NEW_JOB_IN_FOLDER = (By.CSS_SELECTOR, ".trailing-icon > .svg-icon")
    LINK_FREESTYLE = (By.CSS_SELECTOR, ".hudson_model_FreeStyleProject > .desc")
    BUTTON_SAVE_IN_FOLDER = (By.CSS_SELECTOR, "[type='submit']")
    BUTTON_OK_IN_FOLDER = (By.XPATH, "//form[@id=\'createItem\']/div[4]/div/span/button")
    BUTTON_PANEL = (By.CSS_SELECTOR, ".bottom-sticker-inner")


class URLLocators:
    URL_FOLDER_CREATE = TestData.BASE_URL + 'view/all/newJob'
    URL_PEOPLE_MANAGE = TestData.BASE_URL + f'job/{FolderPage.name}/configure'
    URL_FOLDER_PAGE = TestData.BASE_URL + f'job/{FolderPage.name}/configure'
    URL_EXIST_FOLDER = TestData.BASE_URL + f'job/{FolderPage.name}/'
