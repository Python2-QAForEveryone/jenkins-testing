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

    name = (''.join(random.choice(string.ascii_letters) for i in range(10)))

    TITLE = f"{name} Config [Jenkins]"


class FolderPageLocator:
    LINK_NEW_ITEM = (By.XPATH, "//a[@title='New Item']")
    ITEM_NAME = (By.ID, 'name')
    LINK_FOLDER = (By.CLASS_NAME, 'com_cloudbees_hudson_plugins_folder_Folder')
    OK_BUTTON = (By.XPATH, '//span[@class="yui-button primary large-button"]')


class URLLocators:

    URL_FOLDER_CREATE = TestData.BASE_URL + 'view/all/newJob'
    URL_PEOPLE_MANAGE = TestData.BASE_URL + f'job/{FolderPage.name}/configure'
