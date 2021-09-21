import pytest

from pages.ProjectPage import *
from pages.FolderPage import *
from pages.NewItemPage import *
from pages.ProjectPage import ProjectPageLocators
from pages.StringUtils import *


@pytest.mark.webtest
class TestFreestyleProject:
    projectNameString = generate_random_string(10)
    projectNameInt = generate_random_int(10)
    projectNameStringAndInt = generate_random_string_and_int(10)
    projectName = [projectNameString, projectNameInt, projectNameStringAndInt]
    project_name_special_symbol = [FolderPage.name_start_special_ch, FolderPage.name_only_one_or_two_dot,
                                   FolderPage.name_empty]

    @pytest.mark.parametrize("project_name", projectName)
    def test_create_freestyle_project(self, project_name):
        """
        TC_JN_122
        User can create project with StringName
        TC_JN_123
        User can create project with IntName
        TC_JN_125
        User can create project with StringName and IntName
        :param project_name:
        :return:
        """
        name = ProjectPage.create_new_default_job(self, project_name, NewItemPageLocators.FREESTYLE_PROJECT)
        URL_JOB = TD.BASE_URL + f'job/{name}/'
        ProjectPage.click_save_button_into_project(self, name)

        driver = ProjectPage(self.driver)
        driver.go_to_page(URL_JOB)

        assert driver.get_element_text(ProjectPageLocators.PROJECT_NAME) == "Project " + project_name
        assert driver.get_element_text(ProjectPageLocators.DELETE_PROJECT) == "Delete Project"
        ProjectPage.delete_job(self, name)

    @pytest.mark.parametrize("project_name", project_name_special_symbol)
    def test_create_freestyle_project_with_special_symbol(self, project_name):
        """
        TC_JN_124
        User can create project with special symbols
        :param project_name:
        :return:
        """
        driver = DashboardPage(self.driver)
        driver.click(DashboardPageLocators.TEXT_NEW_ITEM)
        driver.do_send_keys(NewItemPageLocators.ENTER_AN_ITEM_NAME, project_name)
        driver.click(NewItemPageLocators.FREESTYLE_PROJECT)
        assert driver.is_disabled(NewItemPageLocators.OK_BUTTON)
        assert driver.is_element_present(NewItemPageLocators.ERROR_MESSAGE)
