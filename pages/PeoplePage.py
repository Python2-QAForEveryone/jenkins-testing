from selenium import webdriver
from webdriver_manager import driver

import tests
from pages.BasePage import BasePage
from config.TestData import TestData as TD, TestData
from selenium.webdriver.common.by import By


class PeoplePage(BasePage):
    TITLE = 'People - [Jenkins]'

    def __init__(self, driver):
        super().__init__(driver)

    # @staticmethod
    # def test_before():
    #     driver = webdriver.Chrome()
    #     driver.get(TestData.BASE_URL)
    #     driver.find_element_by_id('j_username').send_keys(TestData.LOGIN)
    #     driver.find_element_by_name('j_password').send_keys(TestData.PASSWORD)
    #     driver.find_element_by_name('Submit').click()
    #     driver.maximize_window()
    #     driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/div[2]/span/a/span[2]').click()
