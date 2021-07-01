import pytest

from pages.DashboardLowerDropdownModule import DashboardLowerDropdownModule
from tests.locatorsDashboardLowerDropdown import DashboardLowerDropdownModuleLocators, DashboardLowerDropdown, \
    ManageJenkins, URLLocators


class TestDashboardLowerDropdownPage:

    def test_dashboard_link_is_visible_and_clickable_01(self):
        driver = DashboardLowerDropdownModule(self.driver)
        assert driver.is_clickable(DashboardLowerDropdownModuleLocators.DASHBOARD_LINK)
        assert driver.is_visible(DashboardLowerDropdownModuleLocators.DASHBOARD_LINK)

    def test_dashboard_down_arrow_is_visible_and_clickable_02(self):
        driver = DashboardLowerDropdownModule(self.driver)
        driver.hover_over_element(DashboardLowerDropdownModuleLocators.DASHBOARD_LINK)
        assert driver.is_visible(DashboardLowerDropdownModuleLocators.MENU_SELECTOR)
        assert driver.is_clickable(DashboardLowerDropdownModuleLocators.MENU_SELECTOR)

    @pytest.mark.parametrize("locator", DashboardLowerDropdown.dropdownLocators)
    def test_dashboard_lower_dropdown_items_clickable_03(self, locator):
        driver = DashboardLowerDropdownModule(self.driver)
        driver.hover_element1_and_click_element2(DashboardLowerDropdownModuleLocators.DASHBOARD_LINK,
                                                 DashboardLowerDropdownModuleLocators.MENU_SELECTOR)
        assert driver.is_clickable(locator)

    @pytest.mark.parametrize('locator', DashboardLowerDropdown.dropdownLocators)
    def test_dashboard_lower_dropdown_items_visible_04(self, locator):
        driver = DashboardLowerDropdownModule(self.driver)
        driver.hover_element1_and_click_element2(DashboardLowerDropdownModuleLocators.DASHBOARD_LINK,
                                                 DashboardLowerDropdownModuleLocators.MENU_SELECTOR)
        assert driver.is_visible(locator)

    @pytest.mark.parametrize("locator", ManageJenkins.system_configuration_locators)
    def test_manage_jenkins_dropdown_items_clickable_and_visible_05(self, locator):
        driver = DashboardLowerDropdownModule(self.driver)
        driver.hover_element1_and_click_element2(DashboardLowerDropdownModuleLocators.DASHBOARD_LINK,
                                                 DashboardLowerDropdownModuleLocators.MENU_SELECTOR)
        driver.get_wait(DashboardLowerDropdown.MANAGE_JENKINS)
        driver.hover_over_element(DashboardLowerDropdown.MANAGE_JENKINS)
        driver.get_wait(ManageJenkins.CONFIGURE_SYSTEM)
        assert driver.is_clickable(locator)
        assert driver.is_visible(locator)

    @pytest.mark.parametrize("locator", ManageJenkins.security_locators)
    def test_manage_jenkins_dropdown_items_clickable_and_visible_06(self, locator):
        driver = DashboardLowerDropdownModule(self.driver)
        driver.hover_element1_and_click_element2(DashboardLowerDropdownModuleLocators.DASHBOARD_LINK,
                                                 DashboardLowerDropdownModuleLocators.MENU_SELECTOR)
        driver.get_wait(DashboardLowerDropdown.MANAGE_JENKINS)
        driver.hover_over_element(DashboardLowerDropdown.MANAGE_JENKINS)
        driver.get_wait(ManageJenkins.CONFIGURE_SYSTEM)
        assert driver.is_clickable(locator)
        assert driver.is_visible(locator)

    @pytest.mark.parametrize("locator", ManageJenkins.status_information_locators)
    def test_manage_jenkins_dropdown_items_clickable_and_visible_07(self, locator):
        driver = DashboardLowerDropdownModule(self.driver)
        driver.hover_element1_and_click_element2(DashboardLowerDropdownModuleLocators.DASHBOARD_LINK,
                                                 DashboardLowerDropdownModuleLocators.MENU_SELECTOR)
        driver.get_wait(DashboardLowerDropdown.MANAGE_JENKINS)
        driver.hover_over_element(DashboardLowerDropdown.MANAGE_JENKINS)
        driver.get_wait(ManageJenkins.CONFIGURE_SYSTEM)
        assert driver.is_clickable(locator)
        assert driver.is_visible(locator)

    @pytest.mark.parametrize("locator", ManageJenkins.troubleshooting_locators)
    def test_manage_jenkins_dropdown_items_clickable_and_visible_08(self, locator):
        driver = DashboardLowerDropdownModule(self.driver)
        driver.hover_element1_and_click_element2(DashboardLowerDropdownModuleLocators.DASHBOARD_LINK,
                                                 DashboardLowerDropdownModuleLocators.MENU_SELECTOR)
        driver.get_wait(DashboardLowerDropdown.MANAGE_JENKINS)
        driver.hover_over_element(DashboardLowerDropdown.MANAGE_JENKINS)
        driver.get_wait(ManageJenkins.CONFIGURE_SYSTEM)
        assert driver.is_clickable(locator)
        assert driver.is_visible(locator)

    @pytest.mark.parametrize("locator", ManageJenkins.tools_and_actions_locators)
    def test_manage_jenkins_dropdown_items_clickable_and_visible_09(self, locator):
        driver = DashboardLowerDropdownModule(self.driver)
        driver.hover_element1_and_click_element2(DashboardLowerDropdownModuleLocators.DASHBOARD_LINK,
                                                 DashboardLowerDropdownModuleLocators.MENU_SELECTOR)
        driver.get_wait(DashboardLowerDropdown.MANAGE_JENKINS)
        driver.hover_over_element(DashboardLowerDropdown.MANAGE_JENKINS)
        driver.get_wait(ManageJenkins.PREPARE_FOR_SHUTDOWN)
        assert driver.is_clickable(locator)
        assert driver.is_visible(locator)

    def test_goto_newItem_from_dropdown_10(self):
        driver = DashboardLowerDropdownModule(self.driver)
        driver.hover_element1_and_click_element2(DashboardLowerDropdownModuleLocators.DASHBOARD_LINK,
                                                 DashboardLowerDropdownModuleLocators.MENU_SELECTOR)
        driver.get_wait(DashboardLowerDropdown.NEW_ITEM)
        driver.click(DashboardLowerDropdown.NEW_ITEM)
        assert driver.get_current_url() == URLLocators.URL_NEW_ITEM

    def test_goto_people_from_dropdown_11(self):
        driver = DashboardLowerDropdownModule(self.driver)
        driver.hover_element1_and_click_element2(DashboardLowerDropdownModuleLocators.DASHBOARD_LINK,
                                                 DashboardLowerDropdownModuleLocators.MENU_SELECTOR)
        driver.get_wait(DashboardLowerDropdown.PEOPLE)
        driver.click(DashboardLowerDropdown.PEOPLE)
        assert driver.get_current_url() == URLLocators.URL_PEOPLE

    def test_goto_buildHistory_from_dropdown_12(self):
        driver = DashboardLowerDropdownModule(self.driver)
        driver.hover_element1_and_click_element2(DashboardLowerDropdownModuleLocators.DASHBOARD_LINK,
                                                 DashboardLowerDropdownModuleLocators.MENU_SELECTOR)
        driver.get_wait(DashboardLowerDropdown.BUILD_HISTORY)
        driver.click(DashboardLowerDropdown.BUILD_HISTORY)
        assert driver.get_current_url() == URLLocators.URL_BUILD_HISTORY

    def test_goto_manageJenkins_from_dropdown_13(self):
        driver = DashboardLowerDropdownModule(self.driver)
        driver.hover_element1_and_click_element2(DashboardLowerDropdownModuleLocators.DASHBOARD_LINK,
                                                 DashboardLowerDropdownModuleLocators.MENU_SELECTOR)
        driver.get_wait(DashboardLowerDropdown.MANAGE_JENKINS)
        driver.click(DashboardLowerDropdown.MANAGE_JENKINS)
        assert driver.get_current_url() == URLLocators.URL_MANAGE_JENKINS

    def test_goto_myViews_from_dropdown_14(self):
        driver = DashboardLowerDropdownModule(self.driver)
        driver.hover_element1_and_click_element2(DashboardLowerDropdownModuleLocators.DASHBOARD_LINK,
                                                 DashboardLowerDropdownModuleLocators.MENU_SELECTOR)
        driver.get_wait(DashboardLowerDropdown.MY_VIEWS)
        driver.click(DashboardLowerDropdown.MY_VIEWS)
        assert driver.get_current_url() == URLLocators.URL_MY_VIEWS

    def test_goto_lockableResourses_from_dropdown_15(self):
        driver = DashboardLowerDropdownModule(self.driver)
        driver.hover_element1_and_click_element2(
            DashboardLowerDropdownModuleLocators.DASHBOARD_LINK,
            DashboardLowerDropdownModuleLocators.MENU_SELECTOR)
        driver.get_wait(DashboardLowerDropdown.LOCKABLE_RESOURCES)
        driver.click(DashboardLowerDropdown.LOCKABLE_RESOURCES)
        assert driver.get_current_url() == URLLocators.URL_LOCKABLE_RESOURCES

    def test_goto_newView_from_dropdown_16(self):
        driver = DashboardLowerDropdownModule(self.driver)
        driver.hover_element1_and_click_element2(
            DashboardLowerDropdownModuleLocators.DASHBOARD_LINK,
            DashboardLowerDropdownModuleLocators.MENU_SELECTOR)
        driver.get_wait(DashboardLowerDropdown.NEW_VIEW)
        driver.click(DashboardLowerDropdown.NEW_VIEW)
        assert driver.get_current_url() == URLLocators.URL_NEW_VIEW
