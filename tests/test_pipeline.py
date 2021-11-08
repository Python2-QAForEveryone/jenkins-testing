import time
from pages.BasePage import BasePage
from pages.DashboardPage import *
from pages.FolderPage import *
from pages.DashboardPage import URLLocators
from pages.PipelinePage import *
from pages.NewItemPage import NewItemPageLocators
from pages.BuildHistoryPage import BuildHistoryPage
from selenium.webdriver.common.by import By
from config.TestData import TestData as TD
from pages.ProjectPage import ProjectPageLocators, ProjectPage

import pages.StringUtils
import pytest


class TestPipeline:
    pipelineName_String = pages.StringUtils.generate_random_string(10)
    pipelineName_Int = pages.StringUtils.generate_random_int(10)
    pipelineName_Int_and_String = pages.StringUtils.generate_random_string_and_int(10)
    pipelineName_valid = pages.StringUtils.generate_random_string(3)
    pipelineName_valid = "pipeline" + pipelineName_valid
    pipeline_testName = "test" + pipelineName_valid
    project_name_special_symbol = [FolderPage.name_start_special_ch, FolderPage.name_only_one_or_two_dot,
                                   FolderPage.name_empty]
    builds = ""
    name_only_letters = "PipelineNameHasOnlyLetterr"
    name_only_digits = "00012345678912345678911"
    name_only_letters_and_digits = "PipelineNameHasOnlyLettersAndDigits12344"
    name_with_max_length_255 = 255 * "G"

    pipelineName = [pipelineName_String, pipelineName_Int, pipelineName_Int_and_String, pipelineName_valid]
    namesfortest = [name_only_letters_and_digits, name_with_max_length_255, name_only_digits, name_only_letters]


    def test_create_pipeline_name_only_letters(self):
        driver = BasePage(self.driver)
        driver.go_to_page(TD.BASE_URL)
        driver.click(DashboardPageLocators.TEXT_NEW_ITEM)
        driver.do_send_keys(NewItemPageLocators.NEW_PIPELINE_NAME, self.name_only_letters)
        driver.click(NewItemPageLocators.PIPELINE)
        driver.click(NewItemPageLocators.OK_BUTTON)
        assert (self.name_only_letters in driver.get_current_url())
        driver.click(NewItemPageLocators.OK_BUTTON)
        assert (driver.get_title() == self.name_only_letters + " [Jenkins]")


    def test_delete_pipeline_name_only_letters(self):
        driver = DashboardPage(self.driver)
        driver.click(PipelinePageLocators.locator_pipeline_on_dashboard(self,self.name_only_letters))
        driver.click(PipelinePageLocators.DELETE_PIPELINE)
        driver.get_wait_for_alert()
        driver.accept_alert()
        assert driver.is_element_not_present(PipelinePageLocators.locator_pipeline_on_dashboard(self, self.name_only_letters))

    def test_create_pipeline_name_only_digits(self):
        driver = BasePage(self.driver)
        driver.go_to_page(TD.BASE_URL)
        driver.click(DashboardPageLocators.TEXT_NEW_ITEM)
        driver.do_send_keys(NewItemPageLocators.NEW_PIPELINE_NAME, self.name_only_digits)
        driver.click(NewItemPageLocators.PIPELINE)
        driver.click(NewItemPageLocators.OK_BUTTON)
        assert (self.name_only_digits in driver.get_current_url())
        driver.click(NewItemPageLocators.OK_BUTTON)
        assert (driver.get_title() == self.name_only_digits + " [Jenkins]")


    def test_delete_pipeline_name_only_digits(self):
        driver = DashboardPage(self.driver)
        driver.click(PipelinePageLocators.locator_pipeline_on_dashboard(self,self.name_only_digits))
        driver.click(PipelinePageLocators.DELETE_PIPELINE)
        driver.get_wait_for_alert()
        driver.accept_alert()
        assert driver.is_element_not_present(PipelinePageLocators.locator_pipeline_on_dashboard(self, self.name_only_digits))


    def test_create_pipeline_name_only_letters_and_digits(self):
        driver = BasePage(self.driver)
        driver.go_to_page(TD.BASE_URL)
        driver.click(DashboardPageLocators.TEXT_NEW_ITEM)
        driver.do_send_keys(NewItemPageLocators.NEW_PIPELINE_NAME, self.name_only_letters_and_digits)
        driver.click(NewItemPageLocators.PIPELINE)
        driver.click(NewItemPageLocators.OK_BUTTON)
        assert (self.name_only_letters_and_digits in driver.get_current_url())
        driver.click(NewItemPageLocators.OK_BUTTON)
        assert (driver.get_title() == self.name_only_letters_and_digits + " [Jenkins]")

    def test_delete_pipeline_name_only_letters_and_digits(self):
        driver = DashboardPage(self.driver)
        driver.click(PipelinePageLocators.locator_pipeline_on_dashboard(self,self.name_only_letters_and_digits))
        driver.click(PipelinePageLocators.DELETE_PIPELINE)
        driver.get_wait_for_alert()
        driver.accept_alert()
        assert driver.is_element_not_present(PipelinePageLocators.locator_pipeline_on_dashboard(self, self.name_only_letters_and_digits))

    def test_pipeline_name_max_length_255(self):
        driver = BasePage(self.driver)
        driver.go_to_page(TD.BASE_URL)
        driver.click(DashboardPageLocators.TEXT_NEW_ITEM)
        driver.do_send_keys(NewItemPageLocators.NEW_PIPELINE_NAME, self.name_with_max_length_255)
        driver.click(NewItemPageLocators.PIPELINE)
        driver.click(NewItemPageLocators.OK_BUTTON)
        assert (self.name_with_max_length_255 in driver.get_current_url())
        driver.click(NewItemPageLocators.OK_BUTTON)
        assert (driver.get_title() == self.name_with_max_length_255 + " [Jenkins]")

    def test_delete_pipeline_name_max_length_255(self):
        driver = DashboardPage(self.driver)
        driver.click(PipelinePageLocators.locator_pipeline_on_dashboard(self,self.name_with_max_length_255))
        driver.click(PipelinePageLocators.DELETE_PIPELINE)
        driver.get_wait_for_alert()
        driver.accept_alert()
        assert driver.is_element_not_present(PipelinePageLocators.locator_pipeline_on_dashboard(self, self.name_with_max_length_255))

    def test_pipeline_not_created_name_max_length_256(self):
        driver = BasePage(self.driver)
        driver.go_to_page(TD.BASE_URL)
        driver.click(DashboardPageLocators.TEXT_NEW_ITEM)
        driver.do_send_keys(NewItemPageLocators.NEW_PIPELINE_NAME, self.name_with_max_length_255 + "A")
        driver.click(NewItemPageLocators.PIPELINE)
        driver.click(NewItemPageLocators.OK_BUTTON)
        assert driver.is_element_present(PipelinePageLocators.PIPELINE_NOT_CREATED_ERROR)



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
        assert (driver.get_title() == pipeline_name + " [Jenkins]")

    @pytest.mark.dependency(depends=["test_create_pipeline"])
    @pytest.mark.parametrize("pipeline_name", pipelineName)
    def test_pipeline_can_build_now(self, pipeline_name):
        driver = BasePage(self.driver)
        driver.go_to_page(PipelinePageLocators.URL_PIPELINE_PAGE + pipeline_name)
        menu_tasks = driver.get_element_text(PipelinePageLocators.MENU_TASKS)
        assert ("Build Now" in menu_tasks)
        driver.click(ProjectPageLocators.BUILD_NOW)
        driver.get_wait_is_clickable(PipelinePageLocators.BUILDS_RECORDS)
        builds = driver.get_elements_text(PipelinePageLocators.BUILDS_RECORDS)
        assert builds[0] == "#1"

    @pytest.mark.dependency(depends=["test_create_pipeline", "test_pipeline_can_build_now"])
    @pytest.mark.parametrize("pipeline_name", pipelineName)
    def test_pipeline_build_is_on_BuildHistoryPage(self, pipeline_name):
        driver = BasePage(self.driver)
        driver.go_to_page(PipelinePageLocators.URL_PIPELINE_PAGE + pipeline_name)
        driver.click(PipelinePageLocators.BACK_TO_DASHBOARD)
        driver.click(DashboardPageLocators.TEXT_BUILD_HISTORY)
        list_of_builds_first = driver.get_elements_text(BuildHistoryPage.LIST_OF_BUILDS)
        pipeline_name_is_in_the_list = False
        for each in list_of_builds_first:
            if pipeline_name in each:
                pipeline_name_is_in_the_list = True

        assert pipeline_name_is_in_the_list == True

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

    @pytest.mark.dependency(depends=["test_create_pipeline", "test_pipeline_can_build_now",
                                     "test_pipeline_build_is_on_BuildHistoryPage"
                                     ])
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

    @pytest.mark.parametrize("project_name", project_name_special_symbol)
    def test_create_project_with_special_symbol_01(self, project_name):
        driver = DashboardPage(self.driver)
        driver.click(DashboardPageLocators.TEXT_NEW_ITEM)
        driver.do_send_keys(NewItemPageLocators.ENTER_AN_ITEM_NAME, project_name)
        driver.click(NewItemPageLocators.NEW_PIPELINE_NAME)
        assert driver.is_disabled(NewItemPageLocators.OK_BUTTON)
        assert driver.is_element_present(NewItemPageLocators.ERROR_MESSAGE)

    @pytest.mark.dependency(depends=["test_create_pipeline", "test_pipeline_name_in_the_tab"])
    def test_build_now_starts_and_finishes(self):
        driver = DashboardPage(self.driver)
        driver.click(DashboardPageLocators.TEXT_NEW_ITEM)
        driver.do_send_keys(NewItemPageLocators.NEW_PIPELINE_NAME, self.pipeline_testName)
        driver.click(NewItemPageLocators.PIPELINE)
        driver.click(NewItemPageLocators.OK_BUTTON)
        driver.get_wait_is_clickable(PipelinePageLocators.CREATE_PIPELINE_SAMPLES)
        driver.click(PipelinePageLocators.CREATE_PIPELINE_SAMPLES)
        driver.click(PipelinePageLocators.BUILD_HELLO_WORLD)
        driver.get_wait_is_clickable(NewItemPageLocators.OK_BUTTON)
        driver.click(NewItemPageLocators.OK_BUTTON)
        driver.click(PipelinePageLocators.BUILD_NOW)
        driver.get_wait_is_clickable(PipelinePageLocators.BUILDS_RECORDS)
        assert driver.is_clickable(PipelinePageLocators.BUILDS_RECORDS)

    @pytest.mark.dependency(
        depends=["test_create_pipeline", "test_pipeline_name_in_the_tab", "test_build_now_starts_and_finishes"])
    def test_view_build_details_click_name_tooltip(self):
        driver = PipelinePage(self.driver)
        driver.click(PipelinePageLocators.BACK_TO_DASHBOARD)
        driver.click(DashboardPageLocators.TEXT_BUILD_HISTORY)
        driver.get_wait_is_clickable(BuildHistoryPage.CHART_BUILD1)
        driver.click(BuildHistoryPage.CHART_BUILD1)
        text_tooltip = driver.get_element_text(BuildHistoryPage.CHART_TOOLTIP1)
        assert text_tooltip != ""

    @pytest.mark.dependency(depends=["test_create_pipeline",
                                     "test_build_now_starts_and_finishes",
                                     "test_view_build_details_click_name_tooltip"])
    def test_view_build_console_output(self):
        driver = DashboardPage(self.driver)
        driver.go_to_page(PipelinePageLocators.URL_PIPELINE_PAGE + self.pipeline_testName)
        driver.click(PipelinePageLocators.BUILD_STATUS)
        console_output_after_build = driver.get_element_text(PipelinePageLocators.CONSOLE_OUTPUT)
        driver.click(PipelinePageLocators.BACK_TO_PROJECT)
        driver.click(PipelinePageLocators.BACK_TO_DASHBOARD)
        driver.click(DashboardPageLocators.TEXT_BUILD_HISTORY)
        driver.click(BuildHistoryPage.get_console_output_from_the_list(self, self.pipeline_testName))
        console_output_build_history_page = driver.get_element_text(PipelinePageLocators.CONSOLE_OUTPUT)
        assert console_output_after_build == console_output_build_history_page

    @pytest.mark.dependency(depends=["test_view_build_console_output"])
    def test_delete_pipeline_project_test_name(self):
        driver = DashboardPage(self.driver)
        driver.click(PipelinePageLocators.locator_pipeline_on_dashboard(self, self.pipeline_testName))
        driver.click(PipelinePageLocators.DELETE_PIPELINE)
        driver.get_wait_for_alert()
        driver.accept_alert()
        assert driver.is_element_not_present(
            PipelinePageLocators.locator_pipeline_on_dashboard(self, self.pipeline_testName))
