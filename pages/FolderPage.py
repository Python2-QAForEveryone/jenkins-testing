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
    name_special_ch_only = (''.join(random.choice(special_characters))) + \
                           (''.join(random.choice(special_characters)))
    name_twins_special_ch_only = (''.join(random.choice(special_characters))) * 2
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
    name_only_three_or_more_dots = '...'
    name_whitespace = (''.join(random.choice(white_spaces)))
    name_library = 'Library first'

    TITLE = f"{name} Config [Jenkins]"
    TITLE_JOB = f"All [{name}] [Jenkins]"
    TITLE_DIGITS_JOB = f"All [{name_digits}] [Jenkins]"
    TITLE_DIGITS = f"{name_digits} Config [Jenkins]"
    TITLE_START_DOT = f"{name_start_dot} Config [Jenkins]"
    TITLE_START_DOT_JOB = f"All [{name_start_dot}] [Jenkins]"
    TITLE_INSIDE_DOT = f"{name_inside_dot} Config [Jenkins]"
    TITLE_THREE_DOT = f"{name_only_three_or_more_dots} Config [Jenkins]"
    TITLE_INSIDE_DOT_JOB = f"All [{name_inside_dot}] [Jenkins]"
    TITLE_JOB_INSIDE_FOLDER = f"{name} [{name}] [Jenkins]"
    WRONG_TITLE = "Jenkins [Jenkins]"
    ALERT_TEXT = f"Delete the Project ‘{name}’?"


class FolderPageLocator:
    LINK_NEW_ITEM = (By.XPATH, "//a[@title='New Item']")
    ITEM_NAME = (By.ID, 'name')
    LINK_FOLDER = (By.CLASS_NAME, 'com_cloudbees_hudson_plugins_folder_Folder')
    OK_BUTTON = (By.XPATH, "//span/button[@type='submit']")
    OK_BUTTON_DISABLED = (By.XPATH, "//button[@id='ok-button'][@class='disabled']")
    SAVE_BUTTON = (By.XPATH, '//span[@name="Submit"]')
    WRONG_REQUEST = (By.CSS_SELECTOR, 'div#error-description > h2')
    ITEM_NAME_INVALID = (By.XPATH, "//div[@id='itemname-invalid'][contains(text(),'is an unsafe character')]")
    ERROR_PAGE = (By.XPATH, "//div[@id='main-panel']/p[contains(text(),'is an unsafe character')]")
    ITEM_NAME_REQUIRED = (By.XPATH, "//div[@id='itemname-required'][contains(text(),'This field cannot be empty')]")
    ITEM_NAME_NOT_ALLOWED = (By.XPATH, "//div[@id='itemname-invalid'][contains(text(),'is not an allowed name')]")
    ERROR_PAGE_NONAME = (By.XPATH, "//div[@id='main-panel']/p[contains(text(),'No name is specified')]")
    LINK_DELETE_FOLDER = (By.XPATH, "//a[@title='Delete Folder']")
    LINK_DELETE_PROJECT = (By.LINK_TEXT, 'Delete Project')
    BUTTON_YES = (By.ID, 'yui-gen1-button')
    LINK_EXIST_FOLDER = (By.CSS_SELECTOR, f'#job_{FolderPage.name} .model-link')
    EMPTY_FOLDER = (By.CSS_SELECTOR, ".h4")
    LINK_CREATE_NEW_JOB_IN_FOLDER = (By.CSS_SELECTOR, ".trailing-icon > .svg-icon")
    LINK_FREESTYLE = (By.CSS_SELECTOR, ".hudson_model_FreeStyleProject > .desc")
    BUTTON_SAVE_IN_FOLDER = (By.CSS_SELECTOR, "[type='submit']")
    BUTTON_OK_IN_FOLDER = (By.XPATH, "//form[@id=\'createItem\']/div[4]/div/span/button")
    BUTTON_PANEL = (By.CSS_SELECTOR, ".bottom-sticker-inner")
    BUTTON_ADD_LIBRARY = (By.ID, "yui-gen13-button")
    INPUT_FIELD_LIBRARY_NAME = (By.NAME, '_.name')
    LINK_PLUS_NEW_VIEW = (By.CSS_SELECTOR, '.addTab')
    INPUT_FIELD_VIEW_NAME = (By.ID, 'name')
    RADIOBUTTON_GLOBAL_VIEW = (By.XPATH, '//div/input[@value="hudson.model.ProxyView"]')
    RADIOBUTTON_LIST_VIEW = (By.XPATH, '//div/input[@value="hudson.model.ListView"]')
    RADIOBUTTON_MY_VIEW = (By.XPATH, '//div/input[@value="hudson.model.MyView"]')
    BUTTON_OK_VIEW = (By.ID, 'ok')
    BUTTON_OK_VIEW_CONFIGURATION = (By.ID, 'yui-gen2-button')
    TAB_CREATED_GLOBAL_VIEW = (By.CSS_SELECTOR, '#breadcrumbs .item:nth-of-type(5) .breadcrumbBarAnchor')
    LINK_EDIT_VIEW = (By.CSS_SELECTOR, '#tasks .task:nth-of-type(7) .task-link-text')
    DASHBOARD_TAB_FOLDER = (By.CSS_SELECTOR, '#breadcrumbs .item:nth-of-type(3) .breadcrumbBarAnchor')
    TAB_CREATED_LIST_VIEW = (By.CSS_SELECTOR, '.active > a')
    BUTTON_OK_LIST_VIEW_CONFIGURATION = (By.ID, 'yui-gen13-button')
    DASHBOARD_TAB_FOLDER_LIST_VIEW = (By.XPATH, f'//a[contains(text(),"{FolderPage.name}")]')
    LINK_NEW_FOLDER_ON_TOP_LIST = (By.XPATH, f"//li/a[@href='/job/{FolderPage.name}/']")
    CHECK_BOX_ADD_JOB_IN_LIST_VIEW = (By.NAME, f"{FolderPage.name}")


class URLLocators:
    URL_FOLDER_CREATE = TestData.BASE_URL + 'view/all/newJob'
    URL_FOLDER_PAGE = TestData.BASE_URL + f'job/{FolderPage.name}/configure'
    URL_EXIST_FOLDER = TestData.BASE_URL + f'job/{FolderPage.name}/'
    URL_CREATE_ITEM = TestData.BASE_URL + "view/all/createItem"
