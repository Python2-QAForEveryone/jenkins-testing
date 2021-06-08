import pytest

from pages.DashboardLowerDropdownPage import DashboardLowerDropdownPage
from tests.locatorsDashboardLowerDropdown import DashboardLowerDropdownPageLocators, DashboardLowerDropdownLocators


class TestDashboardLowerDropdownPage:

    def test_dashboard_link_is_visible_and_clickable(self):
        driver = DashboardLowerDropdownPage(self.driver)
        assert driver.is_clickable(DashboardLowerDropdownPageLocators.DASHBOARD_LINK)
        assert driver.is_visible(DashboardLowerDropdownPageLocators.DASHBOARD_LINK)

    def test_dashboard_down_arrow_is_visible_and_clickable(self):
        driver = DashboardLowerDropdownPage(self.driver)
        driver.hover_over_element(DashboardLowerDropdownPageLocators.DASHBOARD_LINK)
        assert driver.is_visible(DashboardLowerDropdownPageLocators.MENU_SELECTOR)
        assert driver.is_clickable(DashboardLowerDropdownPageLocators.MENU_SELECTOR)

    @pytest.mark.parametrize("locator", DashboardLowerDropdownLocators.locators_for_dropdown)
    def test_dashboard_lower_dropdown_items_clickable(self, locator):
        driver = DashboardLowerDropdownPage(self.driver)
        driver.hover_element1_and_click_element2(DashboardLowerDropdownPageLocators.DASHBOARD_LINK,
                                                 DashboardLowerDropdownPageLocators.MENU_SELECTOR)
        assert driver.is_clickable(locator)

    @pytest.mark.parametrize('locator', DashboardLowerDropdownLocators.locators_for_dropdown)
    def test_dashboard_lower_dropdown_items_visible(self, locator):
        driver = DashboardLowerDropdownPage(self.driver)
        driver.hover_element1_and_click_element2(DashboardLowerDropdownPageLocators.DASHBOARD_LINK,
                                                 DashboardLowerDropdownPageLocators.MENU_SELECTOR)
        assert driver.is_visible(locator)
