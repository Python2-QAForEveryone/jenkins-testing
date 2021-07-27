import pytest
from pages.NewItemPage import *
from pages.DashboardPage import *
from pages.StringUtils import *
from pages.ProjectPage import ProjectPageLocators


class TestMultiConfigurationProject:
    projectNameString = generate_random_string(10)
    projectNameInt = generate_random_int(10)
    projectNameStringAndInt = generate_random_string_and_int(10)
    projectName = [projectNameString, projectNameInt, projectNameStringAndInt]

    @pytest.mark.parametrize("project_name", projectName)
    def test_create_project_with_string_01(self, project_name):
        driver = DashboardPage(self.driver)
        driver.click(DashboardPageLocators.TEXT_NEW_ITEM)
        driver.do_send_keys(NewItemPageLocators.ENTER_AN_ITEM_NAME, project_name)
        driver.click(NewItemPageLocators.MULTI_CONFIGURATION_PROJECT)
        assert driver.is_clickable(NewItemPageLocators.OK_BUTTON)
        driver.click(NewItemPageLocators.OK_BUTTON)
        assert driver.is_clickable(NewItemPageLocators.SAVE_BUTTON)
        driver.click(NewItemPageLocators.SAVE_BUTTON)

        assert driver.get_element_text(ProjectPageLocators.PROJECT_NAME) == "Project " + project_name
        assert driver.get_element_text(ProjectPageLocators.DELETE_PROJECT) == "Delete Multi-configuration project"

    def test_create_project_with_special_symbol_02(self):
        special_symbol = generate_random_special_symbol(1)
        project_name_special_symbol = generate_random_string_and_int(9).join(special_symbol)
        driver = DashboardPage(self.driver)
        driver.click(DashboardPageLocators.TEXT_NEW_ITEM)
        driver.do_send_keys(NewItemPageLocators.ENTER_AN_ITEM_NAME, project_name_special_symbol)
        driver.click(NewItemPageLocators.MULTI_CONFIGURATION_PROJECT)
        assert driver.is_disabled(NewItemPageLocators.OK_BUTTON)
        assert driver.get_element_text(
            NewItemPageLocators.ERROR_MESSAGE) == "» ‘" + special_symbol + "’ is an unsafe character"
