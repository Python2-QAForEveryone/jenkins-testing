from pages.BasePage import BasePage
from pages.DashboardPage import DashboardPageLocators
from pages.DashboardPage import URLLocators
from pages.NewItemPage import *
from selenium.webdriver.common.by import By
from config.TestData import TestData as TD
import time

from datetime import datetime
from datetime import timezone

import pages.StringUtils
import pytest


class NewItemLocators:
    NEW_ITEM_NAME = (By.XPATH, '//*[@id="name"]')


class NewJobsLocators:
    PIPELINE_RADIO = (By.XPATH, '//*[@id="j-add-item-type-standalone-projects"]/ul/li[2]')
    SUBMIT_BTN = (By.XPATH, '//*[@id="ok-button"]')
    MENU_TASKS= (By.XPATH, '//*[@id="tasks"]')

class NewPipelineConfigure:
    SAVE_PIPELINE = (By.XPATH, '//*[@type="submit"]')


class TestCreatePipeline:

    pipelineNameString = pages.StringUtils.generate_random_string(10)
    pipelineNameInt = pages.StringUtils.generate_random_int(10)
    pipelineNameIntandString=pages.StringUtils.generate_random_string_and_int(10)
    pipelineName= [pipelineNameString, pipelineNameInt, pipelineNameIntandString]

    @pytest.mark.dependency()
    @pytest.mark.parametrize("pipeline_name", pipelineName)
    def test_create_pipeline(self, pipeline_name):
        driver = BasePage(self.driver)
        driver.go_to_page(TD.BASE_URL)
        time.sleep(5)
        driver.click(DashboardPageLocators.TEXT_NEW_ITEM)
        #  verify if user is on the right page by checking current page url
        assert (URLLocators.URL_NEW_ITEM == driver.get_current_url())
        if driver.is_element_present(NewItemLocators.NEW_ITEM_NAME):
            driver.do_send_keys(NewItemLocators.NEW_ITEM_NAME, pipeline_name)
            time.sleep(2)
        else:
            print("Locator" + NewItemLocators.NEW_ITEM_NAME + "is not found")
        driver.get_element(NewItemPageLocators.PIPELINE)
        driver.click(NewItemPageLocators.PIPELINE)
        time.sleep(3)
        if driver.is_clickable(NewItemPageLocators.OK_BUTTON):
            driver.get_element(NewItemPageLocators.OK_BUTTON)
            driver.click(NewItemPageLocators.OK_BUTTON)
        else:
            print("Submit button is not clickable!!!")
        # verify the job name is in the link
        assert (pipeline_name in driver.get_current_url())
        driver.get_element(NewPipelineConfigure.SAVE_PIPELINE)
        driver.click(NewPipelineConfigure.SAVE_PIPELINE)
        # verify Jenkins has created page for a pipeline with format name plus [Jenkins]
        assert (driver.get_title() == pipeline_name + " [Jenkins]")
        time_stamp=datetime.now()
        print("Pipeline created with valid random name "+pipeline_name+" at "+time_stamp.strftime("%d/%m/%Y %H:%M:%S"))

    @pytest.mark.dependency(depends=["test_create_pipeline"])
    @pytest.mark.parametrize("pipeline_name", pipelineName)
    def test_pipeline_enabled(self,pipeline_name):
        driver = BasePage(self.driver)
        print(TD.BASE_URL+"job/"+pipeline_name)
        driver.go_to_page(TD.BASE_URL+"job/"+pipeline_name)
        print(pipeline_name)
        menu_tasks= driver.get_element_text(NewJobsLocators.MENU_TASKS)
        assert ("Build Now" in menu_tasks)



