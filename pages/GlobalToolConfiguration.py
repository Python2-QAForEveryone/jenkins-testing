from pages.BasePage import BasePage
from config.TestData import TestData
from selenium.webdriver.common.by import By

class GlobalToolConfiguration(BasePage):
    TITLE = 'Global Tool Configuration'

    def __init__(self, driver):
        super().__init__(driver)
