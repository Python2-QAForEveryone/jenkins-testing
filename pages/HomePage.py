from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    TITLE = 'Dashboard [Jenkins]'
    NEW_ITEM = (By.XPATH, "//a[@title='New Item']")

    def __init__(self, driver):
        super().__init__(driver)
