import time
from pages.BasePage import BasePage
from pages.DashboardPage import *
from pages.DashboardPage import URLLocators
from pages.PipelinePage import *
from pages.NewItemPage import NewItemPageLocators
from selenium.webdriver.common.by import By
from config.TestData import TestData as TD
from pages.ProjectPage import ProjectPageLocators

import pages.StringUtils
import pytest


class TestPipeline:
    pipelineName_String = pages.StringUtils.generate_random_string(10)
    pipelineName_Int = pages.StringUtils.generate_random_int(10)
    pipelineName_Int_and_String = pages.StringUtils.generate_random_string_and_int(10)
    pipelineName_valid = pages.StringUtils.generate_random_string(3)
    pipelineName_valid = "pipeline" + pipelineName_valid
    pipelineName = [pipelineName_String, pipelineName_Int, pipelineName_Int_and_String, pipelineName_valid]

    @pytest.mark.dependency()
    @pytest.mark.parametrize("pipeline_name", pipelineName)
    def test_create_pipeline(self, pipeline_name):
        driver = BasePage(self.driver)
        driver.go_to_page(TD.BASE_URL)
        driver.click(DashboardPageLocators.TEXT_NEW_ITEM)
        #  verify if user is on the right page by checking current page url
        assert (URLLocators.URL_NEW_ITEM == driver.get_current_url())
        driver.do_send_keys(NewItemPageLocators.NEW_PIPELINE_NAME, pipeline_name)
        driver.click(NewItemPageLocators.PIPELINE)
        driver.click(NewItemPageLocators.OK_BUTTON)
        assert (pipeline_name in driver.get_current_url())
        driver.click(NewItemPageLocators.OK_BUTTON)
        # verify Jenkins has created page for a pipeline with format name plus [Jenkins]
        assert (driver.get_title() == pipeline_name + " [Jenkins]")

    @pytest.mark.dependency(depends=["test_create_pipeline"])
    @pytest.mark.parametrize("pipeline_name", pipelineName)
    def test_pipeline_can_build_now(self, pipeline_name):
        driver = BasePage(self.driver)
        driver.go_to_page(PipelinePageLocators.URL_PIPELINE_PAGE+ pipeline_name)
        menu_tasks = driver.get_element_text(PipelinePageLocators.MENU_TASKS)
        assert ("Build Now" in menu_tasks)

    @pytest.mark.dependency(depends=["test_create_pipeline"])
    def test_pipeline_name_in_the_tab(self):
        driver = BasePage(self.driver)
        driver.go_to_page(PipelinePageLocators.URL_PIPELINE_PAGE + self.pipelineName_valid)
        tab_locator_valid = PipelinePageLocators.locator_for_tab(self, self.pipelineName_valid)
        driver.get_element(tab_locator_valid)
        driver.click(tab_locator_valid)
        assert (self.pipelineName_valid in driver.get_element_text(tab_locator_valid))
        assert driver.is_element_present(tab_locator_valid)

    @pytest.mark.dependency(depends=["test_create_pipeline"])
    def test_pipeline_disabled(self):
        driver = PipelinePage(self.driver)
        driver.get_element(PipelineConfigureLocators.MENU_ITEM_CONFIGURE)
        driver.click(PipelineConfigureLocators.MENU_ITEM_CONFIGURE)
        driver.click(PipelineConfigureLocators.BOX_DISABLE)
        driver.click(PipelineConfigureLocators.BTN_SAVE)
        menu_tasks = driver.get_element_text(PipelinePageLocators.MENU_TASKS)
        assert ("Build Now" not in menu_tasks)

    @pytest.mark.dependency(depends=["test_create_pipeline", "test_pipeline_disabled"])
    def test_pipeline_enabled(self):
        driver = PipelinePage(self.driver)
        driver.click(PipelineConfigureLocators.MENU_ITEM_CONFIGURE)
        driver.click(PipelineConfigureLocators.BOX_DISABLE)
        driver.click(PipelineConfigureLocators.BTN_SAVE)
        menu_tasks = driver.get_element_text(PipelinePageLocators.MENU_TASKS)
        assert ("Build Now" in menu_tasks)


    @pytest.mark.dependency(depends=["test_create_pipeline"])
    @pytest.mark.parametrize("project_name", pipelineName)
    def test_delete_pipeline_project(self, project_name):
        driver = DashboardPage(self.driver)
        driver.go_to_page(TD.BASE_URL)
        driver.get_wait(ProjectLocators.job_by_name(project_name))
        driver.click(ProjectLocators.job_by_name(project_name))
        driver.click(ProjectPageLocators.DELETE_PROJECT)
        driver.get_wait_for_alert()
        driver.accept_alert()
        assert driver.is_element_not_present(ProjectLocators.job_by_name(project_name))
