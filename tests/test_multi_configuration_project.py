import pytest

from pages.DashboardPage import *
from pages.ProjectPage import *
from pages.FolderPage import *
from pages.NewItemPage import *
from pages.ProjectPage import ProjectPageLocators
from pages.StringUtils import *


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
        driver.click(NewItemPageLocators.OK_BUTTON)
        driver.get_wait(NewItemPageLocators.SAVE_BUTTON)
        driver.click(NewItemPageLocators.SAVE_BUTTON)

        assert driver.get_element_text(ProjectPageLocators.PROJECT_NAME) == "Project " + project_name
        assert driver.get_element_text(ProjectPageLocators.DELETE_PROJECT) == "Delete Multi-configuration project"

    @pytest.mark.dependency(depends=["test_create_project_02"])
    def test_disable_project_03(self):
        driver = ProjectPage(self.driver)
        assert driver.is_element_present(ProjectPageLocators.DISABLE_PROJECT_BUTTON)
        driver.click(ProjectPageLocators.DISABLE_PROJECT_BUTTON)
        assert driver.is_element_present(ProjectPageLocators.ENABLE_PROJECT_BUTTON)
        assert driver.get_element_text(ProjectPageLocators.DISABLE_PROJECT_WARNING) == "This project is currently disabled\nEnable"

    @pytest.mark.dependency(depends=["test_disable_project_03"])
    def test_enable_project_04(self):
        driver = ProjectPage(self.driver)
        assert driver.is_element_present(ProjectPageLocators.ENABLE_PROJECT_BUTTON)
        driver.click(ProjectPageLocators.ENABLE_PROJECT_BUTTON)
        assert driver.is_element_not_present(ProjectPageLocators.ENABLE_PROJECT_BUTTON)
        assert driver.is_element_present(ProjectPageLocators.DISABLE_PROJECT_BUTTON)
        assert driver.is_element_present(ProjectPageLocators.BUILD_NOW)

    @pytest.mark.dependency(depends=["test_enable_project_04"])
    def test_add_description_05(self):
        driver = ProjectPage(self.driver)
        driver.click(ProjectPageLocators.ADD_DESCRIPTION_BUTTON)
        driver.do_send_keys(ProjectPageLocators.DESCRIPTION_TEXTAREA, "Project description")
        driver.click(ProjectPageLocators.SUBMIT_DESCRIPTION_BUTTON)
        assert driver.get_element_text(ProjectPageLocators.DESCRIPTION) == "Project description"

    @pytest.mark.dependency(depends=["test_add_description_05"])
    def test_edit_description_06(self):
        driver = ProjectPage(self.driver)
        assert driver.get_element_text(ProjectPageLocators.DESCRIPTION) == "Project description"
        driver.click(ProjectPageLocators.ADD_DESCRIPTION_BUTTON)
        driver.clear(ProjectPageLocators.DESCRIPTION_TEXTAREA)
        driver.do_send_keys(ProjectPageLocators.DESCRIPTION_TEXTAREA, "New description")
        driver.click(ProjectPageLocators.SUBMIT_DESCRIPTION_BUTTON)
        assert driver.get_element_text(ProjectPageLocators.DESCRIPTION) == "New description"

    @pytest.mark.dependency(depends=["test_edit_description_06"])
    def test_rename_07(self):
        driver = ProjectPage(self.driver)
        driver.click(ProjectPageLocators.RENAME)
        driver.clear(ProjectPageLocators.NEW_NAME);
        driver.do_send_keys(ProjectPageLocators.NEW_NAME, "NewProjectName")
        driver.click(ProjectPageLocators.RENAME_BUTTON)
        assert driver.get_element_text(ProjectPageLocators.PROJECT_NAME) == "Project NewProjectName"

    @pytest.mark.dependency(depends=["test_rename_07"])
    def test_rename_08(self):
        driver = ProjectPage(self.driver)
        assert driver.get_element_text(ProjectPageLocators.PROJECT_NAME) == "Project NewProjectName"
        driver.click(ProjectPageLocators.RENAME)
        driver.clear(ProjectPageLocators.NEW_NAME);
        driver.do_send_keys(ProjectPageLocators.NEW_NAME, TestMultiConfigurationProject.projectNameStringAndInt)
        driver.click(ProjectPageLocators.RENAME_BUTTON)
        assert driver.get_element_text(ProjectPageLocators.PROJECT_NAME) == "Project " + TestMultiConfigurationProject.projectNameStringAndInt

    @pytest.mark.dependency(depends=["test_rename_08"])
    def test_build_now_09(self):
        driver = ProjectPage(self.driver)
        number_of_jobs_before = driver.get_elements(ProjectPageLocators.COUNT_OF_BUILD_HISTORY)
        driver.click(ProjectPageLocators.BUILD_NOW)
        driver.get_wait(ProjectPageLocators.BUILD_SUCCESS_JOBS)
        number_of_jobs_after = driver.get_elements(ProjectPageLocators.COUNT_OF_BUILD_HISTORY)
        assert len(number_of_jobs_before) != len(number_of_jobs_after)
        assert driver.is_element_present(ProjectPageLocators.FIRST_BUILD)

    @pytest.mark.dependency(depends=["test_build_now_09"])
    def test_view_workspace_10(self):
        driver = ProjectPage(self.driver)
        driver.click(ProjectPageLocators.WORKSPACE)
        assert driver.get_element_text(ProjectPageLocators.PROJECT_NAME) == "Workspace of " + \
               TestMultiConfigurationProject.projectNameStringAndInt + " on master"

    @pytest.mark.dependency(depends=["test_view_workspace_10"])
    @pytest.mark.parametrize("project_name", projectName)
    def test_delete_project_11(self, project_name):
        driver = DashboardPage(self.driver)
        driver.go_to_page(TestData.BASE_URL)
        driver.get_wait(ProjectLocators.job_by_name(project_name))
        driver.click(ProjectLocators.job_by_name(project_name))
        driver.click(ProjectPageLocators.DELETE_PROJECT)
        driver.get_wait_for_alert()
        driver.accept_alert()
        assert driver.is_element_not_present(ProjectLocators.job_by_name(project_name))
