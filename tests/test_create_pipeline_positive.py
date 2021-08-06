from pages.BasePage import BasePage
from pages.DashboardPage import DashboardPageLocators
from pages.DashboardPage import URLLocators

from selenium.webdriver.common.by import By
from config.TestData import TestData as TD
import time
import random
import pytest


class NewItemLocators:
    NEW_ITEM_NAME = (By.XPATH, '//*[@id="name"]')


class NewJobsLocators:
    PIPELINE_RADIO = (By.XPATH, '//*[@id="j-add-item-type-standalone-projects"]/ul/li[2]')
    SUBMIT_BTN = (By.XPATH, '//*[@id="ok-button"]')


class NewPipelineConfigure:
    SAVE_PIPELINE = (By.XPATH, '//*[@type="submit"]')


class TestCreatePipeline:

    def test_create_pipeline(self):
        driver = BasePage(self.driver)
        driver.click(DashboardPageLocators.TEXT_NEW_ITEM)
        time.sleep(2)
        #  verify if user is on the right page by checking current page url
        assert (URLLocators.URL_NEW_ITEM == driver.get_current_url())
        # generate a random numeral string with 3 digits
        rand_int_str = str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))
        test_name = 'pipeline_'+ rand_int_str
        time.sleep(2)

        if driver.is_element_present(NewItemLocators.NEW_ITEM_NAME):
            driver.do_send_keys(NewItemLocators.NEW_ITEM_NAME, test_name)
            time.sleep(2)
        else:
            print("Locator" + NewItemLocators.NEW_ITEM_NAME + "is not found")
        driver.get_element(NewJobsLocators.PIPELINE_RADIO)
        driver.click(NewJobsLocators.PIPELINE_RADIO)
        time.sleep(3)
        if driver.is_clickable(NewJobsLocators.SUBMIT_BTN):
            driver.get_element(NewJobsLocators.SUBMIT_BTN)
            driver.click(NewJobsLocators.SUBMIT_BTN)
        else:
            print("Submit button is not clickable!!!")
        time.sleep(5)
        # verify the job name is in the link
        assert (test_name in driver.get_current_url())
        driver.get_element(NewPipelineConfigure.SAVE_PIPELINE)
        driver.click(NewPipelineConfigure.SAVE_PIPELINE)
        time.sleep(5)
        # verify Jenkins has created page for a pipeline with format name plus [Jenkins]
        assert (driver.get_title() == test_name + " [Jenkins]")
       # print(driver.get_element_text('//*[@id="breadcrumbs"]') )
       # lst = driver.get_element_text('//*[@id="tasks"]')
        print(lst)
