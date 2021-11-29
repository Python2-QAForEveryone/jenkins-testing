import pytest

from pages.ProjectPage import *
from pages.FolderPage import *
from pages.NewItemPage import *
from pages.ProjectPage import ProjectPageLocators
from pages.StringUtils import *
from pages.FreestylePage import *
from pages.ConsoleOutputPage import *


@pytest.mark.webtest
class TestFreestyleProject:
    projectNameString = generate_random_string(10)
    projectNameInt = generate_random_int(10)
    projectNameStringAndInt = generate_random_string_and_int(10)
    projectName = [projectNameString, projectNameInt, projectNameStringAndInt]
    project_name_special_symbol = [FolderPage.name_start_special_ch, FolderPage.name_only_one_or_two_dot,
                                   FolderPage.name_empty]
    test_name_verify_console_output= "freestyle000"
    test_name_verify_workspace_output= "freestyle001"


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
        User can create project with special symbols and letters and numbers
        TC_JN_182
        User can create project with special symbols
        TC_JN_183
        User can create project with twins special symbols
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

    def test_create_freestyle_project_add_action_disable(self):
        """
        TC_JN_165
        User create project and add action: Disable this project
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

    def test_created_freestyle_project_add_action_timestamps(self):
        """
        TC_JN_184
        User create project and add action: Add timestamps to the Console Output
        :return:
        """

        name = ProjectPage.create_new_default_job(self, self.projectNameStringAndInt,
                                                  NewItemPageLocators.FREESTYLE_PROJECT)
        URL_JOB_FOR_SAVE = TD.BASE_URL + f'job/{name}/configure'

        driver = FreestylePage(self.driver)
        driver.go_to_page(URL_JOB_FOR_SAVE)
        driver.get_wait_is_clickable(FreestylePageLocators.CHECKBOX_ADD_TIMESTAMPS_TO_CONSOLE_OUTPUT)
        driver.scroll_to_element(FreestylePageLocators.CHECKBOX_ADD_TIMESTAMPS_TO_CONSOLE_OUTPUT)
        driver.click(FreestylePageLocators.CHECKBOX_ADD_TIMESTAMPS_TO_CONSOLE_OUTPUT)
        driver.get_wait(NewItemPageLocators.SAVE_BUTTON)
        driver.click(NewItemPageLocators.SAVE_BUTTON)
        driver.get_wait(ProjectPageLocators.BUILD_NOW)
        driver.click(ProjectPageLocators.BUILD_NOW)
        driver.get_wait(ProjectPageLocators.BUILD_SUCCESS_LAST_JOB)
        driver.click(ProjectPageLocators.BUILD_SUCCESS_LAST_JOB)
        lst_of_time = driver.get_elements_text(ConsoleOutputPage.LINES_WITH_TIMESTAMPS)
        assert len(lst_of_time) > 0
        ProjectPage.delete_job(self, name)

    @pytest.mark.skip
    def test_created_freestyle_project_add_action_build_steps(self):
        """
        TC_JN_185
        User create project and add action: Add build steps > "dir" in the textarea
        :return:
        """

        name = ProjectPage.create_new_default_job(self, self.projectNameStringAndInt,
                                                  NewItemPageLocators.FREESTYLE_PROJECT)
        command = 'dir'
        subtext = f'{name}>{command}'
        URL_JOB_FOR_SAVE = TD.BASE_URL + f'job/{name}/configure'

        driver = FreestylePage(self.driver)
        driver.go_to_page(URL_JOB_FOR_SAVE)
        driver.scroll_to_bottom()
        driver.get_wait_is_clickable(FreestylePageLocators.BUTTON_ADD_BUILD_STEPS)
        driver.scroll_to_element(FreestylePageLocators.BUTTON_ADD_BUILD_STEPS)
        driver.click(FreestylePageLocators.BUTTON_ADD_BUILD_STEPS)
        driver.click(FreestylePageLocators.OPTION_EXECUTE_WINDOWS_COMMAND)
        driver.do_send_keys(FreestylePageLocators.TEXTAREA_COMMAND, command)
        driver.get_wait(NewItemPageLocators.SAVE_BUTTON)
        driver.click(NewItemPageLocators.SAVE_BUTTON)
        driver.get_wait(ProjectPageLocators.BUILD_NOW)
        driver.click(ProjectPageLocators.BUILD_NOW)
        driver.get_wait(ProjectPageLocators.BUILD_SUCCESS_LAST_JOB)
        driver.click(ProjectPageLocators.BUILD_SUCCESS_LAST_JOB)
        lst_of_text = driver.get_element_text(ConsoleOutputPage.LINES_TEXT).split("\n")
        assert ConsoleOutputPage.is_contains_text(driver, lst_of_text, subtext)
        ProjectPage.delete_job(self, name)

    @pytest.mark.skip
    def test_created_freestyle_project_add_post_build_action(self):
        """
        TC_JN_186
        User create project and add action: Add post-build action > Editable Email Notification
        :return:
        """

        name = ProjectPage.create_new_default_job(self, self.projectNameStringAndInt,
                                                  NewItemPageLocators.FREESTYLE_PROJECT)
        URL_JOB_FOR_SAVE = TD.BASE_URL + f'job/{name}/configure'

        driver = FreestylePage(self.driver)
        driver.go_to_page(URL_JOB_FOR_SAVE)
        driver.scroll_to_bottom()
        driver.get_wait_is_clickable(FreestylePageLocators.BUTTON_ADD_POST_BUILD_ACTION)
        driver.scroll_to_element(FreestylePageLocators.BUTTON_ADD_POST_BUILD_ACTION)
        driver.click(FreestylePageLocators.BUTTON_ADD_POST_BUILD_ACTION)
        driver.get_wait(FreestylePageLocators.OPTION_EDITABLE_EMAIL_NOTIFICATION)
        driver.click(FreestylePageLocators.OPTION_EDITABLE_EMAIL_NOTIFICATION)
        driver.get_wait(FreestylePageLocators.EDITABLE_AREA)
        driver.scroll_to_bottom()
        driver.click(NewItemPageLocators.SAVE_BUTTON)
        driver.get_wait(ProjectPageLocators.EMAIL_TEMPLATE_TESTING)
        assert driver.is_clickable(ProjectPageLocators.EMAIL_TEMPLATE_TESTING)
        ProjectPage.delete_job(self, name)
