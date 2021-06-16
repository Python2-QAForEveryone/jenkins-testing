import pytest

from pages.DashboardLowerDropdownModule import DashboardLowerDropdownModule
from tests.locatorsDashboardLowerDropdown import DashboardLowerDropdownModuleLocators, DashboardLowerDropdown, \
    ManageJenkins


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
        driver.get_wait(ManageJenkins.CONFIGURE_SYSTEM)
        # driver.get_wait(ManageJenkins.SCROLL_DOWN)
        # driver.hover_over_element(ManageJenkins.SCROLL_DOWN)
        driver.get_wait(ManageJenkins.PREPARE_FOR_SHUTDOWN)
        assert driver.is_clickable(locator)
        assert driver.is_visible(locator)

