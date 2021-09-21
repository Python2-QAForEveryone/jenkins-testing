import random
import string

from pages import StringUtils
from pages.BasePage import BasePage
from config.TestData import TestData
from selenium.webdriver.common.by import By


class FreestylePage(BasePage):
    """
    initialized driver
    added moving to the BasePage after log in
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.go_to_page(URLLocators.URL_FREESTYLE_CREATE)

    name = StringUtils.generate_random_string(10)


class URLLocators:
    URL_FREESTYLE_CREATE = TestData.BASE_URL + 'view/all/newJob'
    URL_FREESTYLE_PAGE = TestData.BASE_URL + f'job/{FreestylePage.name}/configure'
    URL_EXIST_FREESTYLE = TestData.BASE_URL + f'job/{FreestylePage.name}/'
