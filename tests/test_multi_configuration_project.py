import time

import pytest
from pages.NewItemPage import *
from pages.FolderPage import *
from pages.DashboardPage import *
from pages.StringUtils import *
from pages.ProjectPage import ProjectPageLocators
from selenium.webdriver.support import expected_conditions as EC

class TestMultiConfigurationProject:
    projectNameString = generate_random_string(10)
    projectNameInt = generate_random_int(10)
    projectNameStringAndInt = generate_random_string_and_int(10)
    projectName = [projectNameString, projectNameInt, projectNameStringAndInt]
    project_name_special_symbol = [FolderPage.name_start_special_ch, FolderPage.name_only_one_or_two_dot,
                             FolderPage.name_empty]

    @pytest.mark.parametrize("project_name", project_name_special_symbol)
    def test_create_project_with_special_symbol_01(self, project_name):
        driver = DashboardPage(self.driver)
        driver.click(DashboardPageLocators.TEXT_NEW_ITEM)
        driver.do_send_keys(NewItemPageLocators.ENTER_AN_ITEM_NAME, project_name)
        driver.click(NewItemPageLocators.MULTI_CONFIGURATION_PROJECT)
        assert driver.is_disabled(NewItemPageLocators.OK_BUTTON)
        assert driver.is_element_present(NewItemPageLocators.ERROR_MESSAGE)

    @pytest.mark.dependency()
    @pytest.mark.parametrize("project_name", projectName)
    def test_create_project_02(self, project_name):
        driver = DashboardPage(self.driver)
        driver.click(DashboardPageLocators.TEXT_NEW_ITEM)
        driver.do_send_keys(NewItemPageLocators.ENTER_AN_ITEM_NAME, project_name)
        driver.click(NewItemPageLocators.MULTI_CONFIGURATION_PROJECT)
        assert driver.is_enabled(NewItemPageLocators.OK_BUTTON)
        driver.click(NewItemPageLocators.OK_BUTTON)
        assert driver.get_current_url() == TestData.BASE_URL + f"job/{project_name}/configure"
        driver.get_wait(NewItemPageLocators.SAVE_BUTTON)
        assert driver.is_clickable(NewItemPageLocators.SAVE_BUTTON)
        driver.click(NewItemPageLocators.SAVE_BUTTON)

        assert driver.get_element_text(ProjectPageLocators.PROJECT_NAME) == "Project " + project_name
        assert driver.get_element_text(ProjectPageLocators.DELETE_PROJECT) == "Delete Multi-configuration project"

    @pytest.mark.dependency(depends=["test_create_project_02"])
    def test_disable_project_03(self):
        driver = DashboardPage(self.driver)
        driver.go_to_page(TestData.BASE_URL)
        driver.get_wait(ProjectLocators.job_by_name(TestMultiConfigurationProject.projectNameString))
        driver.click(ProjectLocators.job_by_name(TestMultiConfigurationProject.projectNameString))
        assert driver.get_element_text(ProjectPageLocators.PROJECT_NAME) == "Project " + TestMultiConfigurationProject.projectNameString
        assert driver.is_element_present(ProjectPageLocators.DISABLE_PROJECT_BUTTON)
        driver.click(ProjectPageLocators.DISABLE_PROJECT_BUTTON)
        assert driver.is_element_present(ProjectPageLocators.ENABLE_PROJECT_BUTTON)
        assert driver.get_element_text(ProjectPageLocators.DISABLE_PROJECT_WARNING) == "This project is currently disabled\nEnable"

    @pytest.mark.dependency(depends=["test_disable_project_03"])
    @pytest.mark.parametrize("project_name", projectName)
    def test_delete_project_05(self, project_name):
        driver = DashboardPage(self.driver)
        driver.go_to_page(TestData.BASE_URL)
        driver.get_wait(ProjectLocators.job_by_name(project_name))
        driver.click(ProjectLocators.job_by_name(project_name))
        assert driver.get_element_text(ProjectPageLocators.DELETE_PROJECT) == "Delete Multi-configuration project"
        driver.click(ProjectPageLocators.DELETE_PROJECT)
        driver.get_wait_for_alert()
        driver.accept_alert()
        driver.is_element_not_present(ProjectLocators.job_by_name(project_name))
