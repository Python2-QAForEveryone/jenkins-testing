from pages.BasePage import BasePage
from pages.DashboardPage import DashboardPageLocators
from pages.DashboardPage import URLLocators
from pages.NewItemPage import *
from selenium.webdriver.common.by import By
from config.TestData import TestData as TD

import pages.StringUtils
import pytest


class NewItemLocators:
    NEW_ITEM_NAME = (By.XPATH, '//*[@id="name"]')


class NewJobsLocators:
    PIPELINE_RADIO = (By.XPATH, '//*[@id="j-add-item-type-standalone-projects"]/ul/li[2]')
    SUBMIT_BTN = (By.XPATH, '//*[@id="ok-button"]')
    MENU_TASKS = (By.XPATH, '//*[@id="tasks"]')


class NewPipelineConfigure:
    SAVE_PIPELINE = (By.XPATH, '//*[@type="submit"]')


class TestCreatePipeline:
    pipelineName_String = pages.StringUtils.generate_random_string(10)
    pipelineName_Int = pages.StringUtils.generate_random_int(10)
    pipelineName_Int_and_String = pages.StringUtils.generate_random_string_and_int(10)
    pipelineName_valid = pages.StringUtils.generate_random_string(3)
    pipelineName_valid = "pipeline_" + pipelineName_valid
    pipelineName = [pipelineName_String, pipelineName_Int, pipelineName_Int_and_String, pipelineName_valid]

    TAB_PART1 = '//a[contains(text(),\"'
    TAB_PART2 = '\")]'
    PIPELINE_NAME_VALID = f'{pipelineName_valid}'
    TAB_LOCATOR = (By.XPATH, TAB_PART1 + f'{pipelineName}' + TAB_PART2)
    TAB_LOCATOR_VALID = (By.XPATH, TAB_PART1 + f'{pipelineName_valid}' + TAB_PART2)

    @pytest.mark.dependency()
    @pytest.mark.parametrize("pipeline_name", pipelineName)
    def test_create_pipeline(self, pipeline_name):
        driver = BasePage(self.driver)
        driver.go_to_page(TD.BASE_URL)
        driver.click(DashboardPageLocators.TEXT_NEW_ITEM)
        #  verify if user is on the right page by checking current page url
        assert (URLLocators.URL_NEW_ITEM == driver.get_current_url())
        driver.do_send_keys(NewItemLocators.NEW_ITEM_NAME, pipeline_name)
        driver.get_element(NewItemPageLocators.PIPELINE)
        driver.click(NewItemPageLocators.PIPELINE)
        driver.get_element(NewItemPageLocators.OK_BUTTON)
        driver.click(NewItemPageLocators.OK_BUTTON)
        assert (pipeline_name in driver.get_current_url())
        driver.get_element(NewPipelineConfigure.SAVE_PIPELINE)
        driver.click(NewPipelineConfigure.SAVE_PIPELINE)
        # verify Jenkins has created page for a pipeline with format name plus [Jenkins]
        assert (driver.get_title() == pipeline_name + " [Jenkins]")

    @pytest.mark.dependency(depends=["test_create_pipeline"])
    @pytest.mark.parametrize("pipeline_name", pipelineName)
    def test_pipeline_can_build_now(self, pipeline_name):
        driver = BasePage(self.driver)
        driver.go_to_page(TD.BASE_URL + "job/" + pipeline_name)
        menu_tasks = driver.get_element_text(NewJobsLocators.MENU_TASKS)
        assert ("Build Now" in menu_tasks)

    @pytest.mark.dependency(depends=["test_create_pipeline"])
    def test_pipeline_name_in_the_tab(self):
        driver = BasePage(self.driver)
        driver.go_to_page(TD.BASE_URL + "job/" + self.pipelineName_valid)
        driver.get_element(self.TAB_LOCATOR_VALID)
        driver.click(self.TAB_LOCATOR_VALID)
        assert (self.pipelineName_valid in driver.get_element_text(self.TAB_LOCATOR_VALID))
        assert driver.is_element_present(self.TAB_LOCATOR_VALID)
