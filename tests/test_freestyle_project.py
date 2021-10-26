import pytest

from pages.ProjectPage import *
from pages.FolderPage import *
from pages.NewItemPage import *
from pages.ProjectPage import ProjectPageLocators
from pages.StringUtils import *
from pages.FreestylePage import *


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

    @pytest.mark.parametrize("tab_name, assert_name", FreestylePageLocators.verify_works_tabs)
    def test_create_freestyle_project_and_verify_tabs(self, tab_name, assert_name):
        """
        TC_JN_143
        User create project and on the Configurate page verify General tab
        TC_JN_144
        User create project and on the Configurate page verify Source Code Management tab
        TC_JN_145
        User create project and on the Configurate page verify Build Triggers tab
        TC_JN_146
        User create project and on the Configurate page verify Build Environment tab
        TC_JN_147
        User create project and on the Configurate page verify Build tab
        TC_JN_148
        User create project and on the Configurate page verify Post-build Actions tab
        :return:
        """

        name = ProjectPage.create_new_default_job(self, self.projectNameStringAndInt,
                                                  NewItemPageLocators.FREESTYLE_PROJECT)
        URL_JOB_FOR_SAVE = TD.BASE_URL + f'job/{name}/configure'

        driver = FreestylePage(self.driver)
        driver.go_to_page(URL_JOB_FOR_SAVE)
        driver.get_wait(tab_name)
        driver.click(tab_name)
        assert driver.is_element_present(assert_name)
        driver.get_wait(NewItemPageLocators.SAVE_BUTTON)
        driver.click(NewItemPageLocators.SAVE_BUTTON)

        ProjectPage.delete_job(self, name)

    def test_create_freestyle_project_add_post_build_action(self):
        """
        TC_JN_165
        User create project and add post-build action: Disable this project
        :return:
        """

        name = ProjectPage.create_new_default_job(self, self.projectNameStringAndInt,
                                                  NewItemPageLocators.FREESTYLE_PROJECT)
        URL_JOB_FOR_SAVE = TD.BASE_URL + f'job/{name}/configure'

        driver = FreestylePage(self.driver)
        driver.go_to_page(URL_JOB_FOR_SAVE)
        driver.get_wait_is_clickable(FreestylePageLocators.CHECKBOX_DISABLE_THIS_PROJECT)
        driver.click(FreestylePageLocators.CHECKBOX_DISABLE_THIS_PROJECT)
        driver.get_wait(NewItemPageLocators.SAVE_BUTTON)
        driver.click(NewItemPageLocators.SAVE_BUTTON)
        driver.get_wait(ProjectPageLocators.ENABLE_PROJECT_BUTTON)
        assert driver.is_clickable(ProjectPageLocators.ENABLE_PROJECT_BUTTON)
        ProjectPage.delete_job(self, name)
